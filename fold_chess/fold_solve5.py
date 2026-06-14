"""Fold Chess — Rung 4 (phase b): complete retrograde solution of KQKRR.

Same certified machinery as KQKR and KRRK, scaled to the five-piece cube
(2^31 = 2,147,483,648 raw states):
  1. SEEDING (parallel, shared-memory): every legal state gets its non-capture
     move counter, terminal value (mate/stalemate), capture values resolved
     against the two CERTIFIED four-piece tables (white takes a rook -> KQKR;
     black takes the queen -> colour-flipped KRRK), and a draw floor where a
     drawing capture exists.
  2. BFS by ply level with UN-MOVE (predecessor) generation, identical rules
     to the lower rungs.
  3. Survivors with moves are drawn cycles (the fortress class).
Internal referees: full-space mirror audit AND exhaustive rook-swap
invariance (the two black rooks are identical). 50-move/cursed status is read
off the measured longest win exactly as at the lower rungs.

Memory: five arrays over 2^31 cells = uint8 kind/counter/floor (2.1 GB each)
+ uint16 ply/capwin (4.3 GB each) ~ 15 GB, held in POSIX shared memory so the
parallel seeders write in place with no multi-GB IPC. Targets a 512 GB host.
"""

import sys, os, time
from array import array
from multiprocessing import shared_memory
import concurrent.futures as cf
import numpy as np

sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))

from fold_chess import find_fold_prime
from fold_chess import _rank, _file, _on_board, _king_zone, _kings_touch
from fold_chess import _QUEEN_RAYS, _ROOK_RAYS
from fold_chess4 import _slider_attacks
from fold_chess5 import (NSTATES5, encode5, decode5, is_legal5, successors5,
                         white_in_check5, black_in_check5,
                         CAP_WXR, CAP_BXQ, WTM, BTM)

Z = 1 - 1
U, D, W, L = Z, 1, 2, 3
KU, KD, KW, KL = Z, 1, 2, 3
PLY_CAP = 25 * 4                           # one hundred plies (50-move budget)

_G = {}


# --------------------------------------------------------------- seeding

def _init_worker(names):
    _G["kind"] = shared_memory.SharedMemory(name=names["kind"])
    _G["ply"] = shared_memory.SharedMemory(name=names["ply"])
    _G["counter"] = shared_memory.SharedMemory(name=names["counter"])
    _G["capwin"] = shared_memory.SharedMemory(name=names["capwin"])
    _G["floor"] = shared_memory.SharedMemory(name=names["floor"])
    _G["kqkr_kind"] = shared_memory.SharedMemory(name=names["kqkr_kind"])
    _G["kqkr_ply"] = shared_memory.SharedMemory(name=names["kqkr_ply"])
    _G["krrk_kind"] = shared_memory.SharedMemory(name=names["krrk_kind"])
    _G["krrk_ply"] = shared_memory.SharedMemory(name=names["krrk_ply"])
    _G["kind_mv"] = _G["kind"].buf
    _G["ply_mv"] = _G["ply"].buf.cast("H")
    _G["cnt_mv"] = _G["counter"].buf
    _G["cap_mv"] = _G["capwin"].buf.cast("H")
    _G["flr_mv"] = _G["floor"].buf
    _G["kqkr_k"] = _G["kqkr_kind"].buf
    _G["kqkr_p"] = _G["kqkr_ply"].buf.cast("H")
    _G["krrk_k"] = _G["krrk_kind"].buf
    _G["krrk_p"] = _G["krrk_ply"].buf.cast("H")


def seed_span(span):
    lo, hi = span
    kind_mv, ply_mv = _G["kind_mv"], _G["ply_mv"]
    cnt_mv, cap_mv, flr_mv = _G["cnt_mv"], _G["cap_mv"], _G["flr_mv"]
    kqkr_k, kqkr_p = _G["kqkr_k"], _G["kqkr_p"]
    krrk_k, krrk_p = _G["krrk_k"], _G["krrk_p"]
    legal_n = Z
    for idx in range(lo, hi):
        wk, wq, r1, r2, bk, stm = decode5(idx)
        if not is_legal5(wk, wq, r1, r2, bk, stm):
            continue
        legal_n += 1
        moves = successors5(idx)
        ncap = Z
        best_cap = None
        has_draw = False
        for s in moves:
            if isinstance(s, tuple):
                tag, payload = s
                if tag == CAP_WXR:
                    k3, p3 = kqkr_k[payload], kqkr_p[payload]
                else:
                    k3, p3 = krrk_k[payload], krrk_p[payload]
                if k3 == KL:                # opponent lost after capture: win
                    cand = p3 + 1
                    if best_cap is None or cand < best_cap:
                        best_cap = cand
                elif k3 == KD:
                    has_draw = True
                # k3 == KW: capture hands opponent a win — never helpful
            else:
                ncap += 1
        if not moves:
            if stm == BTM and white_in_check5(wk, wq, r1, r2, bk):
                kind_mv[idx] = L
            elif stm == WTM and black_in_check5(wk, wq, r1, r2, bk):
                kind_mv[idx] = L
            else:
                kind_mv[idx] = D
            continue
        cnt_mv[idx] = ncap if ncap < 256 else 255
        if best_cap is not None:
            cap_mv[idx] = best_cap
        if has_draw:
            flr_mv[idx] = 1
        if ncap == Z and best_cap is None:
            kind_mv[idx] = D if has_draw else L
            if not has_draw:
                ply_mv[idx] = 1
    return legal_n


# ---------------------------------------------------- predecessors (un-move)

def _line_between(a, b, rays):
    ra, ca = _rank(a), _file(a)
    rb, cb = _rank(b), _file(b)
    dr = (rb > ra) - (rb < ra)
    dc = (cb > ca) - (cb < ca)
    if (dr, dc) not in rays:
        return False, set()
    if not (ra == rb or ca == cb or abs(ra - rb) == abs(ca - cb)):
        return False, set()
    out = set()
    rr, cc = ra + dr, ca + dc
    while (rr, cc) != (rb, cb):
        out.add(rr * 8 + cc)
        rr += dr
        cc += dc
    return True, out


def predecessors5(idx):
    """States with a legal NON-CAPTURE move into idx."""
    wk, wq, r1, r2, bk, stm = decode5(idx)
    occ = {wk, wq, r1, r2, bk}
    out = []
    if stm == BTM:
        # white moved last; predecessors are WTM states needing black NOT in
        # check (the only black-checker is the white queen).
        q_aligned, q_between = _line_between(wq, bk, _QUEEN_RAYS)
        for u in _king_zone(wk):                       # white king un-move
            if u in occ or _kings_touch(u, bk):
                continue
            check_p = (q_aligned and (r1 not in q_between) and
                       (r2 not in q_between) and (u not in q_between))
            if check_p:
                continue
            out.append(encode5(u, wq, r1, r2, bk, WTM))
        q_attack_bk = _slider_attacks(bk, _QUEEN_RAYS, {wk, r1, r2}, None)
        r, c = _rank(wq), _file(wq)                    # white queen un-move
        for dr, dc in _QUEEN_RAYS:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                u = rr * 8 + cc
                if u in occ:
                    break
                if u not in q_attack_bk:
                    out.append(encode5(wk, u, r1, r2, bk, WTM))
                rr += dr
                cc += dc
    else:
        # black moved last; predecessors are BTM states needing white NOT in
        # check (the white-checkers are the two black rooks).
        a1, b1 = _line_between(r1, wk, _ROOK_RAYS)
        a2, b2 = _line_between(r2, wk, _ROOK_RAYS)
        for u in _king_zone(bk):                       # black king un-move
            if u in occ or _kings_touch(wk, u):
                continue
            chk1 = a1 and (wq not in b1) and (r2 not in b1) and (u not in b1)
            chk2 = a2 and (wq not in b2) and (r1 not in b2) and (u not in b2)
            if chk1 or chk2:
                continue
            out.append(encode5(wk, wq, r1, r2, u, BTM))
        for which, rsq, other, a_o, b_o in ((1, r1, r2, a2, b2),
                                            (2, r2, r1, a1, b1)):   # rook un-move
            attack_wk = _slider_attacks(wk, _ROOK_RAYS, {wq, bk, other}, None)
            r, c = _rank(rsq), _file(rsq)
            for dr, dc in _ROOK_RAYS:
                rr, cc = r + dr, c + dc
                while _on_board(rr, cc):
                    u = rr * 8 + cc
                    if u in occ:
                        break
                    chk_self = u in attack_wk
                    chk_other = (a_o and (wq not in b_o) and (bk not in b_o)
                                 and (u not in b_o))
                    if not chk_self and not chk_other:
                        if which == 1:
                            out.append(encode5(wk, wq, u, r2, bk, BTM))
                        else:
                            out.append(encode5(wk, wq, r1, u, bk, BTM))
                    rr += dr
                    cc += dc
    return out


# ------------------------------------------------------------------ solver

def _mk(size):
    return shared_memory.SharedMemory(create=True, size=size)


def solve5(console=True, workers=30):
    t0 = time.time()
    P = find_fold_prime(NSTATES5)
    if console:
        print("Rung 4 — KQKRR: %d raw states (2^%d), P=%d"
              % (NSTATES5, NSTATES5.bit_length() - 1, P), flush=True)
        print("loading certified 4-piece tables (KQKR, KRRK)...", flush=True)

    from fold_solve4 import solve4
    from fold_solveRR import solveRR
    r_kqkr = solve4(console=False)
    r_krrk = solveRR(console=False)
    NS4 = len(r_kqkr["kind"])
    NSRR = len(r_krrk["kind"])

    # stage everything (the five big arrays + four sub-tables) in shared memory
    shm = {}
    shm["kind"] = _mk(NSTATES5)
    shm["ply"] = _mk(2 * NSTATES5)
    shm["counter"] = _mk(NSTATES5)
    shm["capwin"] = _mk(2 * NSTATES5)
    shm["floor"] = _mk(NSTATES5)
    shm["kqkr_kind"] = _mk(NS4)
    shm["kqkr_ply"] = _mk(2 * NS4)
    shm["krrk_kind"] = _mk(NSRR)
    shm["krrk_ply"] = _mk(2 * NSRR)
    # zero the seed arrays; copy sub-tables in
    for key in ("kind", "counter", "floor"):
        np.frombuffer(shm[key].buf, dtype=np.uint8)[:] = 0
    for key in ("ply", "capwin"):
        np.frombuffer(shm[key].buf, dtype=np.uint16)[:] = 0
    shm["kqkr_kind"].buf[:] = bytes(r_kqkr["kind"])
    shm["kqkr_ply"].buf[:] = array("H", r_kqkr["ply"]).tobytes()
    shm["krrk_kind"].buf[:] = bytes(r_krrk["kind"])
    shm["krrk_ply"].buf[:] = array("H", r_krrk["ply"]).tobytes()
    names = {k: v.name for k, v in shm.items()}

    if console:
        print("seeding %d states with %d workers..." % (NSTATES5, workers), flush=True)
    nchunks = workers * 8
    step = (NSTATES5 + nchunks - 1) // nchunks
    spans = [(lo, min(lo + step, NSTATES5)) for lo in range(Z, NSTATES5, step)]
    legal_total = Z
    done = Z
    with cf.ProcessPoolExecutor(max_workers=workers, initializer=_init_worker,
                                initargs=(names,)) as ex:
        for ln in ex.map(seed_span, spans):
            legal_total += ln
            done += 1
            if console and done % 16 == Z:
                print("  seeded %d/%d chunks, %.0fs" % (done, len(spans), time.time() - t0),
                      flush=True)
    if console:
        print("seeded %d legal in %.0fs; building frontiers..."
              % (legal_total, time.time() - t0), flush=True)

    # memoryviews for the BFS hot loop; numpy views for bulk scans
    kind_mv = shm["kind"].buf
    ply_mv = shm["ply"].buf.cast("H")
    cnt_mv = shm["counter"].buf
    cap_mv = shm["capwin"].buf.cast("H")
    flr_mv = shm["floor"].buf
    knp = np.frombuffer(shm["kind"].buf, dtype=np.uint8)
    pnp = np.frombuffer(shm["ply"].buf, dtype=np.uint16)
    cnp = np.frombuffer(shm["capwin"].buf, dtype=np.uint16)

    frontier_L = {}
    L_idx = np.flatnonzero(knp == L)
    if L_idx.size:
        L_pl = pnp[L_idx]
        uq, inv = np.unique(L_pl, return_inverse=True)
        for k, pv in enumerate(uq):
            frontier_L[int(pv)] = L_idx[inv == k].tolist()
    cap_levels = {}
    cap_idx = np.flatnonzero((cnp != 0) & (knp == U))
    if cap_idx.size:
        cap_v = cnp[cap_idx]
        uq2, inv2 = np.unique(cap_v, return_inverse=True)
        for k, lv in enumerate(uq2):
            cap_levels[int(lv)] = cap_idx[inv2 == k].tolist()
    del L_idx, cap_idx, knp, pnp, cnp

    if console:
        print("BFS starting (%.0fs)..." % (time.time() - t0), flush=True)
    level = Z
    assigned_W = assigned_L = Z
    while frontier_L or cap_levels:
        level += 1
        new_W = []
        for i in cap_levels.pop(level, []):
            if kind_mv[i] == U:
                kind_mv[i] = W
                ply_mv[i] = level
                new_W.append(i)
        for i in frontier_L.pop(level - 1, []):
            for p in predecessors5(i):
                if kind_mv[p] == U:
                    kind_mv[p] = W
                    ply_mv[p] = level
                    new_W.append(p)
        assigned_W += len(new_W)
        next_L = []
        for i in new_W:
            for p in predecessors5(i):
                if kind_mv[p] != U or cnt_mv[p] == Z:
                    continue
                cnt_mv[p] -= 1
                if cnt_mv[p] == Z and cap_mv[p] == Z:
                    if flr_mv[p]:
                        kind_mv[p] = D
                    else:
                        kind_mv[p] = L
                        ply_mv[p] = level + 1
                        next_L.append(p)
        if next_L:
            frontier_L.setdefault(level + 1, []).extend(next_L)
            assigned_L += len(next_L)
        if console and (new_W or next_L):
            print("  level %d: +%d W, +%d L (W %d / L %d), %.0fs"
                  % (level, len(new_W), len(next_L), assigned_W, assigned_L,
                     time.time() - t0), flush=True)
        if level > 4 * PLY_CAP:
            print("  SAFETY STOP at level %d" % level, flush=True)
            break

    # remaining undecided legal states with any move/capture/floor are drawn
    # cycles (the fortress class). Identify them in numpy.
    knp = np.frombuffer(shm["kind"].buf, dtype=np.uint8)
    cnp = np.frombuffer(shm["counter"].buf, dtype=np.uint8)
    cwp = np.frombuffer(shm["capwin"].buf, dtype=np.uint16)
    flp = np.frombuffer(shm["floor"].buf, dtype=np.uint8)
    draw_cycle_mask = (knp == U) & ((cnp != 0) | (cwp != 0) | (flp != 0))
    drawn_cycles = int(draw_cycle_mask.sum())
    knp[draw_cycle_mask] = D
    del draw_cycle_mask

    pnp = np.frombuffer(shm["ply"].buf, dtype=np.uint16)
    wins = int((knp == W).sum())
    losses = int((knp == L).sum())
    draws = int((knp == D).sum())
    w_plies = pnp[knp == W]
    max_w = int(w_plies.max()) if w_plies.size else 0
    mates = int(((knp == L) & (pnp == 0)).sum())
    del w_plies

    # ---- internal referees over the full space (chunked numpy) ----
    def fliph_arr(s):
        return (s & 56) | (7 - (s & 7))

    idx_all = None
    swap_bad = 0
    mir_bad = 0
    CH = 1 << 26
    for base in range(0, NSTATES5, CH):
        end = min(base + CH, NSTATES5)
        idxs = np.arange(base, end, dtype=np.int64)
        stm = idxs & 1
        r = idxs >> 1
        bk = r & 63; r >>= 6
        r2 = r & 63; r >>= 6
        r1 = r & 63; r >>= 6
        wq = r & 63; r >>= 6
        wk = r & 63
        ki = knp[base:end]
        pi = pnp[base:end]
        dec = ki != U
        # rook-swap: swap r1,r2 fields
        js = ((((wk * 64 + wq) * 64 + r2) * 64 + r1) * 64 + bk) * 2 + stm
        swap_bad += int(((knp[js] != ki) | (pnp[js] != pi))[dec].sum())
        # mirror: horizontal flip of all five squares
        jm = ((((fliph_arr(wk) * 64 + fliph_arr(wq)) * 64 + fliph_arr(r1)) * 64
               + fliph_arr(r2)) * 64 + fliph_arr(bk)) * 2 + stm
        mir_bad += int(((knp[jm] != ki) | (pnp[jm] != pi))[dec].sum())
    del idx_all

    no_cursed = max_w <= PLY_CAP
    if console:
        print("KQKRR solved: legal %d | W %d / L %d / D %d (cycles %d) | mates %d"
              % (legal_total, wins, losses, draws, drawn_cycles, mates), flush=True)
        print("  longest win %d plies (%d moves); cursed impossible: %s"
              % (max_w, (max_w + 1) // 2, no_cursed), flush=True)
        print("  ROOK-SWAP violations (exhaustive): %d | mirror violations: %d | %.0fs"
              % (swap_bad, mir_bad, time.time() - t0), flush=True)

    # persist the solved kind+ply to disk for the external read / spectral runs
    out_dir = os.path.dirname(os.path.abspath(__file__))
    kind_path = os.path.join(out_dir, "kqkrr_kind.bin")
    ply_path = os.path.join(out_dir, "kqkrr_ply.bin")
    with open(kind_path, "wb") as fh:
        fh.write(bytes(shm["kind"].buf))
    with open(ply_path, "wb") as fh:
        fh.write(bytes(shm["ply"].buf))
    if console:
        print("  wrote %s (%d bytes) and %s" % (kind_path, os.path.getsize(kind_path),
                                                 ply_path), flush=True)

    result = {"P": P, "legal": legal_total, "wins": wins, "losses": losses,
              "draws": draws, "drawn_cycles": drawn_cycles, "checkmates": mates,
              "max_dtm_plies": max_w, "swap_violations": swap_bad,
              "mirror_violations": mir_bad, "no_cursed_theorem": no_cursed,
              "kind_path": kind_path, "ply_path": ply_path,
              "elapsed_s": round(time.time() - t0, 1)}

    # release shared memory
    for v in shm.values():
        v.close()
        v.unlink()
    return result


if __name__ == "__main__":
    solve5()
