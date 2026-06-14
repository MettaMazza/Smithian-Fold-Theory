"""Fold Chess — Rung 3 (phase 3b): complete retrograde solution of KQKR.

The genuine tablebase construction, fold-lawful at the interface:
  1. SEEDING (parallel): every legal state gets its non-capture move counter,
     terminal value (mate/stalemate), capture-move values resolved against the
     validated 3-piece tables (queen takes rook -> KQK; rook or king takes
     queen -> colour-flipped KRK), and a draw floor where a drawing capture
     exists.
  2. BFS by ply level with UN-MOVE (predecessor) generation:
     - L at ply k promotes unresolved predecessors to W at k+1 (minimal);
     - W at ply k decrements predecessors' counters; a counter reaching zero
       becomes L at k+1 (no draw floor) or D (draw floor);
     - capture-wins enter at their sub-table ply, level-synchronously.
  3. Survivors with moves are drawn cycles.

50-move rule: if the maximum DTM over all wins is <= 100 plies, no win can be
cursed (the game ends inside any 50-move budget) — the cursed count is then a
THEOREM of the measured bound, independently checkable by the Syzygy read.
"""

import sys, os, time
from array import array
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))

from fold_chess import solve as solve3, find_fold_prime
from fold_chess import _rank, _file, _on_board, _king_zone, _kings_touch
from fold_chess import _QUEEN_RAYS, _ROOK_RAYS
from fold_chess4 import (NSTATES4, encode4, decode4, is_legal4, successors4,
                         _slider_attacks, white_in_check, black_in_check,
                         CAP_WXR, CAP_BXQ, WTM, BTM)

Z = 1 - 1
U, D, W, L = Z, 1, 2, 3                   # kinds packed in bytearrays
KU, KD, KW, KL = Z, 1, 2, 3               # 3-piece table int codes
PLY_CAP = 25 * 4                          # one hundred plies (50-move budget)

_G = {}                                   # per-worker globals (3-piece tables)


def _init_worker(kqk_kind, kqk_ply, krk_kind, krk_ply):
    _G["kqk_kind"] = kqk_kind
    _G["kqk_ply"] = array("H", kqk_ply)
    _G["krk_kind"] = krk_kind
    _G["krk_ply"] = array("H", krk_ply)


def seed_chunk(span):
    """Seed [lo, hi): kind, ply, counter (non-capture moves), capwin (min
    winning-capture ply + 1, or 0), floor (has drawing capture), legal count."""
    lo, hi = span
    kqk_kind, kqk_ply = _G["kqk_kind"], _G["kqk_ply"]
    krk_kind, krk_ply = _G["krk_kind"], _G["krk_ply"]
    n = hi - lo
    kind = bytearray(n)
    ply = array("H", bytes(2 * n))
    counter = bytearray(n)
    capwin = array("H", bytes(2 * n))
    floor = bytearray(n)
    legal_n = Z
    for idx in range(lo, hi):
        wk, wq, br, bk, stm = decode4(idx)
        if not is_legal4(wk, wq, br, bk, stm):
            continue
        legal_n += 1
        j = idx - lo
        moves = successors4(idx)
        ncap = Z
        best_cap = None
        has_draw = False
        for s in moves:
            if isinstance(s, tuple):
                tag, payload = s
                if tag == CAP_WXR:
                    k3, p3 = kqk_kind[payload], kqk_ply[payload]
                else:
                    k3, p3 = krk_kind[payload], krk_ply[payload]
                if k3 == KL:               # opponent lost after capture: win
                    cand = p3 + 1
                    if best_cap is None or cand < best_cap:
                        best_cap = cand
                elif k3 == KD:
                    has_draw = True
                else:                      # capture hands opponent a win:
                    pass                   # never helpful, never counted
            else:
                ncap += 1
        if not moves:
            if stm == BTM and black_in_check(wk, wq, br, bk):
                kind[j] = L
            elif stm == WTM and white_in_check(wk, wq, br, bk):
                kind[j] = L
            else:
                kind[j] = D
            continue
        counter[j] = ncap
        if best_cap is not None:
            capwin[j] = best_cap
        if has_draw:
            floor[j] = 1
        if ncap == Z and best_cap is None:
            # only capture moves exist and none wins:
            kind[j] = D if has_draw else L
            if not has_draw:
                ply[j] = 1                 # all captures hand a win over: lost
    return lo, hi, bytes(kind), ply.tobytes(), bytes(counter), capwin.tobytes(), bytes(floor), legal_n


# -------------------------------------------------------- fast predecessors

def _line_between(a, b, rays):
    """(aligned?, set of strictly-between squares) for a->b along given rays."""
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


def predecessors(idx):
    """States with a legal NON-CAPTURE move into idx. Legality reduced to
    precomputed line geometry (no full is_legal4 in the loop)."""
    wk, wq, br, bk, stm = decode4(idx)
    occ = {wk, wq, br, bk}
    out = []
    if stm == BTM:
        # white moved last; predecessors are wtm states (rule: black not in
        # check at p — the only black-checker is the white queen)
        q_aligned, q_between = _line_between(wq, bk, _QUEEN_RAYS)
        # king came from u: queen fixed; black in check at p iff the
        # wq->bk line is open with wk at u (u may block it; br may block it)
        for u in _king_zone(wk):
            if u in occ or _kings_touch(u, bk):
                continue
            check_p = q_aligned and (br not in q_between) and (u not in q_between)
            if check_p:
                continue
            out.append(encode4(u, wq, br, bk, WTM))
        # queen came from u along an open ray from wq: black in check at p
        # iff a queen on u attacks bk with blockers {wk, br}
        q_attack_bk = _slider_attacks(bk, _QUEEN_RAYS, {wk, br}, None)
        r, c = _rank(wq), _file(wq)
        for dr, dc in _QUEEN_RAYS:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                u = rr * 8 + cc
                if u in occ:
                    break
                if u not in q_attack_bk:
                    out.append(encode4(wk, u, br, bk, WTM))
                rr += dr
                cc += dc
    else:
        # black moved last; predecessors are btm states (rule: white not in
        # check at p — the only white-checker is the black rook)
        r_aligned, r_between = _line_between(br, wk, _ROOK_RAYS)
        for u in _king_zone(bk):
            if u in occ or _kings_touch(wk, u):
                continue
            check_p = r_aligned and (wq not in r_between) and (u not in r_between)
            if check_p:
                continue
            out.append(encode4(wk, wq, br, u, BTM))
        r_attack_wk = _slider_attacks(wk, _ROOK_RAYS, {wq, bk}, None)
        r, c = _rank(br), _file(br)
        for dr, dc in _ROOK_RAYS:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                u = rr * 8 + cc
                if u in occ:
                    break
                if u not in r_attack_wk:
                    out.append(encode4(wk, wq, u, bk, BTM))
                rr += dr
                cc += dc
    return out


# ------------------------------------------------------------------ solver

def solve4(console=True, workers=8):
    t_start = time.time()
    P = find_fold_prime(NSTATES4)

    if console:
        print("loading 3-piece tables (KQK, KRK)...")
    kqk = solve3(piece="Q", console=False)
    krk = solve3(piece="R", console=False)
    code = {"U": KU, "D": KD, "W": KW, "L": KL}
    kqk_kind = bytes(code[k] for k in kqk["kind"])
    krk_kind = bytes(code[k] for k in krk["kind"])
    kqk_ply = array("H", kqk["ply"]).tobytes()
    krk_ply = array("H", krk["ply"]).tobytes()

    if console:
        print("seeding %d raw states with %d workers..." % (NSTATES4, workers))
    kind = bytearray(NSTATES4)
    ply = array("H", bytes(2 * NSTATES4))
    counter = bytearray(NSTATES4)
    capwin = array("H", bytes(2 * NSTATES4))
    floor = bytearray(NSTATES4)
    legal_total = Z

    import concurrent.futures as cf
    chunk = NSTATES4 // (workers * 4)
    spans = [(lo, min(lo + chunk, NSTATES4)) for lo in range(Z, NSTATES4, chunk)]
    with cf.ProcessPoolExecutor(max_workers=workers, initializer=_init_worker,
                                initargs=(kqk_kind, kqk_ply, krk_kind, krk_ply)) as ex:
        done = Z
        for lo, hi, kb, pb, cb, wb, fb, ln in ex.map(seed_chunk, spans):
            kind[lo:hi] = kb
            pv = array("H")
            pv.frombytes(pb)
            ply[lo:hi] = pv
            counter[lo:hi] = cb
            cw = array("H")
            cw.frombytes(wb)
            capwin[lo:hi] = cw
            floor[lo:hi] = fb
            legal_total += ln
            done += 1
            if console and done % 8 == Z:
                print("  seeded %d/%d chunks, %.1fs" % (done, len(spans), time.time() - t_start))

    if console:
        print("seeded %d legal states in %.1fs; building frontiers..."
              % (legal_total, time.time() - t_start))

    frontier_L = {}
    cap_levels = {}
    for i in range(NSTATES4):
        if kind[i] == L:
            frontier_L.setdefault(ply[i], []).append(i)
        elif capwin[i] != Z and kind[i] == U:
            cap_levels.setdefault(capwin[i], []).append(i)

    level = Z
    assigned_W = assigned_L = Z
    while frontier_L or cap_levels:
        level += 1
        new_W = []
        for i in cap_levels.pop(level, []):
            if kind[i] == U:
                kind[i] = W
                ply[i] = level
                new_W.append(i)
        for i in frontier_L.pop(level - 1, []):
            for p in predecessors(i):
                if kind[p] == U:
                    kind[p] = W
                    ply[p] = level
                    new_W.append(p)
        assigned_W += len(new_W)
        next_L = []
        for i in new_W:
            for p in predecessors(i):
                if kind[p] != U or counter[p] == Z:
                    continue
                counter[p] -= 1
                if counter[p] == Z and capwin[p] == Z:
                    if floor[p]:
                        kind[p] = D
                    else:
                        kind[p] = L
                        ply[p] = level + 1
                        next_L.append(p)
        if next_L:
            frontier_L.setdefault(level + 1, []).extend(next_L)
            assigned_L += len(next_L)
        if console and (new_W or next_L):
            print("  level %d: +%d W, +%d L (totals W %d / L %d), %.1fs"
                  % (level, len(new_W), len(next_L), assigned_W, assigned_L,
                     time.time() - t_start))
        if level > 4 * PLY_CAP:
            print("  SAFETY STOP at level %d" % level)
            break

    drawn_cycles = Z
    for i in range(NSTATES4):
        if kind[i] == U and (counter[i] != Z or capwin[i] != Z or floor[i] != Z):
            kind[i] = D
            drawn_cycles += 1

    wins = sum(1 for i in range(NSTATES4) if kind[i] == W)
    losses = sum(1 for i in range(NSTATES4) if kind[i] == L)
    draws = sum(1 for i in range(NSTATES4) if kind[i] == D)
    max_w = max([ply[i] for i in range(NSTATES4) if kind[i] == W] or [Z])
    mates = sum(1 for i in range(NSTATES4) if kind[i] == L and ply[i] == Z)

    def flip_h(s):
        return _rank(s) * 8 + (7 - _file(s))
    bad = Z
    for i in range(NSTATES4):
        if kind[i] == U:
            continue
        wk, wq, br, bk, stm = decode4(i)
        j = encode4(flip_h(wk), flip_h(wq), flip_h(br), flip_h(bk), stm)
        if kind[j] != kind[i] or ply[j] != ply[i]:
            bad += 1

    no_cursed = max_w <= PLY_CAP
    if console:
        print("KQKR solved: legal %d | W %d / L %d / D %d (cycles %d) | mates %d"
              % (legal_total, wins, losses, draws, drawn_cycles, mates))
        print("  longest win %d plies (%d moves); max <= %d plies: %s "
              "=> cursed wins impossible at this rung: %s"
              % (max_w, (max_w + 1) // 2, PLY_CAP, no_cursed, no_cursed))
        print("  mirror violations (full audit): %d | elapsed %.1fs"
              % (bad, time.time() - t_start))
    return {"P": P, "kind": kind, "ply": ply, "legal": legal_total,
            "wins": wins, "losses": losses, "draws": draws,
            "drawn_cycles": drawn_cycles, "checkmates": mates,
            "max_dtm_plies": max_w, "mirror_violations": bad,
            "no_cursed_theorem": no_cursed,
            "elapsed_s": round(time.time() - t_start, 1)}


if __name__ == "__main__":
    solve4()
