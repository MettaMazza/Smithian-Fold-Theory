"""Fold Chess — complete retrograde solution of KRRK (prerequisite table
for the five-piece climb; see FOLD_CHESS_5_PLAN.md).

Same certified machinery as KQKR (parallel seeding, level-synchronous
predecessor BFS, capture values from the certified KRK table), plus one
referee unique to this ending: the two rooks are identical, so every
position carries two index representations (rooks swapped) whose values
must agree EXACTLY across the whole space — an exhaustive internal
consistency proof at zero design cost.
"""

import sys, os, time
from array import array
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))

from fold_chess import solve as solve3, find_fold_prime
from fold_chess import _rank, _file, _on_board, _king_zone, _kings_touch, _ROOK_RAYS
from fold_chess4 import _slider_attacks, WTM, BTM
from fold_chessRR import (NSTATES_RR, encodeRR, decodeRR, is_legalRR,
                          successorsRR, black_in_checkRR, CAP_KXR)

Z = 1 - 1
U, D, W, L = Z, 1, 2, 3
KU, KD, KW, KL = Z, 1, 2, 3
PLY_CAP = 25 * 4

_G = {}


def _init_worker(krk_kind, krk_ply):
    _G["krk_kind"] = krk_kind
    _G["krk_ply"] = array("H", krk_ply)


def seed_chunk(span):
    lo, hi = span
    krk_kind, krk_ply = _G["krk_kind"], _G["krk_ply"]
    n = hi - lo
    kind = bytearray(n)
    ply = array("H", bytes(2 * n))
    counter = bytearray(n)
    capwin = array("H", bytes(2 * n))
    floor = bytearray(n)
    legal_n = Z
    for idx in range(lo, hi):
        wk, r1, r2, bk, stm = decodeRR(idx)
        if not is_legalRR(wk, r1, r2, bk, stm):
            continue
        legal_n += 1
        j = idx - lo
        moves = successorsRR(idx)
        ncap = Z
        best_cap = None
        has_draw = False
        for s in moves:
            if isinstance(s, tuple):
                _, payload = s
                k3, p3 = krk_kind[payload], krk_ply[payload]
                if k3 == KL:
                    cand = p3 + 1
                    if best_cap is None or cand < best_cap:
                        best_cap = cand
                elif k3 == KD:
                    has_draw = True
                # k3 == KW: capture hands white a won KRK — never helpful
            else:
                ncap += 1
        if not moves:
            if stm == BTM and black_in_checkRR(wk, r1, r2, bk):
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
            kind[j] = D if has_draw else L
            if not has_draw:
                ply[j] = 1
    return lo, hi, bytes(kind), ply.tobytes(), bytes(counter), capwin.tobytes(), bytes(floor), legal_n


def _line(a, b):
    ra, ca = _rank(a), _file(a)
    rb, cb = _rank(b), _file(b)
    dr = (rb > ra) - (rb < ra)
    dc = (cb > ca) - (cb < ca)
    if not (ra == rb or ca == cb):
        return False, set()
    out = set()
    rr, cc = ra + dr, ca + dc
    while (rr, cc) != (rb, cb):
        out.add(rr * 8 + cc)
        rr += dr
        cc += dc
    return True, out


def predecessorsRR(idx):
    """States with a legal NON-CAPTURE move into idx."""
    wk, r1, r2, bk, stm = decodeRR(idx)
    occ = {wk, r1, r2, bk}
    out = []
    if stm == BTM:
        # white moved last; predecessor wtm states need black NOT in check
        a1, b1 = _line(r1, bk)
        a2, b2 = _line(r2, bk)
        for u in _king_zone(wk):
            if u in occ or _kings_touch(u, bk):
                continue
            chk1 = a1 and (r2 not in b1) and (u not in b1)
            chk2 = a2 and (r1 not in b2) and (u not in b2)
            if chk1 or chk2:
                continue
            out.append(encodeRR(u, r1, r2, bk, WTM))
        for which, rsq, other, a_o, b_o in ((1, r1, r2, a2, b2), (2, r2, r1, a1, b1)):
            attack_bk = _slider_attacks(bk, _ROOK_RAYS, {wk, other}, None)
            r, c = _rank(rsq), _file(rsq)
            for dr, dc in _ROOK_RAYS:
                rr, cc = r + dr, c + dc
                while _on_board(rr, cc):
                    u = rr * 8 + cc
                    if u in occ:
                        break
                    # at p the moving rook sits on u: it must not check bk,
                    # and the OTHER rook must not check bk through {wk, u}
                    chk_self = u in attack_bk
                    chk_other = a_o and (wk not in b_o) and (u not in b_o)
                    if not chk_self and not chk_other:
                        if which == 1:
                            out.append(encodeRR(wk, u, r2, bk, WTM))
                        else:
                            out.append(encodeRR(wk, r1, u, bk, WTM))
                    rr += dr
                    cc += dc
    else:
        # black moved last; btm predecessors are unconstrained by white-check
        for u in _king_zone(bk):
            if u in occ or _kings_touch(wk, u):
                continue
            out.append(encodeRR(wk, r1, r2, u, BTM))
    return out


def solveRR(console=True, workers=8):
    t_start = time.time()
    P = find_fold_prime(NSTATES_RR)
    if console:
        print("loading KRK table...")
    krk = solve3(piece="R", console=False)
    code = {"U": KU, "D": KD, "W": KW, "L": KL}
    krk_kind = bytes(code[k] for k in krk["kind"])
    krk_ply = array("H", krk["ply"]).tobytes()

    if console:
        print("seeding %d raw states with %d workers..." % (NSTATES_RR, workers))
    kind = bytearray(NSTATES_RR)
    ply = array("H", bytes(2 * NSTATES_RR))
    counter = bytearray(NSTATES_RR)
    capwin = array("H", bytes(2 * NSTATES_RR))
    floor = bytearray(NSTATES_RR)
    legal_total = Z

    import concurrent.futures as cf
    chunk = NSTATES_RR // (workers * 4)
    spans = [(lo, min(lo + chunk, NSTATES_RR)) for lo in range(Z, NSTATES_RR, chunk)]
    with cf.ProcessPoolExecutor(max_workers=workers, initializer=_init_worker,
                                initargs=(krk_kind, krk_ply)) as ex:
        for lo, hi, kb, pb, cb, wb, fb, ln in ex.map(seed_chunk, spans):
            kind[lo:hi] = kb
            pv = array("H"); pv.frombytes(pb); ply[lo:hi] = pv
            counter[lo:hi] = cb
            cw = array("H"); cw.frombytes(wb); capwin[lo:hi] = cw
            floor[lo:hi] = fb
            legal_total += ln
    if console:
        print("seeded %d legal in %.1fs" % (legal_total, time.time() - t_start))

    frontier_L = {}
    cap_levels = {}
    for i in range(NSTATES_RR):
        if kind[i] == L:
            frontier_L.setdefault(ply[i], []).append(i)
        elif capwin[i] != Z and kind[i] == U:
            cap_levels.setdefault(capwin[i], []).append(i)

    level = Z
    while frontier_L or cap_levels:
        level += 1
        new_W = []
        for i in cap_levels.pop(level, []):
            if kind[i] == U:
                kind[i] = W
                ply[i] = level
                new_W.append(i)
        for i in frontier_L.pop(level - 1, []):
            for p in predecessorsRR(i):
                if kind[p] == U:
                    kind[p] = W
                    ply[p] = level
                    new_W.append(p)
        next_L = []
        for i in new_W:
            for p in predecessorsRR(i):
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
        if level > 4 * PLY_CAP:
            print("SAFETY STOP")
            break

    drawn = Z
    for i in range(NSTATES_RR):
        if kind[i] == U and (counter[i] != Z or capwin[i] != Z or floor[i] != Z):
            kind[i] = D
            drawn += 1

    wins = sum(1 for i in range(NSTATES_RR) if kind[i] == W)
    losses = sum(1 for i in range(NSTATES_RR) if kind[i] == L)
    draws = sum(1 for i in range(NSTATES_RR) if kind[i] == D)
    max_w = max([ply[i] for i in range(NSTATES_RR) if kind[i] == W] or [Z])
    mates = sum(1 for i in range(NSTATES_RR) if kind[i] == L and ply[i] == Z)

    # internal referees: rook-swap invariance (exhaustive) + mirror audit
    swap_bad = Z
    for i in range(NSTATES_RR):
        if kind[i] == U:
            continue
        wk, r1, r2, bk, stm = decodeRR(i)
        j = encodeRR(wk, r2, r1, bk, stm)
        if kind[j] != kind[i] or ply[j] != ply[i]:
            swap_bad += 1
    def flip_h(s):
        return _rank(s) * 8 + (7 - _file(s))
    mir_bad = Z
    for i in range(NSTATES_RR):
        if kind[i] == U:
            continue
        wk, r1, r2, bk, stm = decodeRR(i)
        j = encodeRR(flip_h(wk), flip_h(r1), flip_h(r2), flip_h(bk), stm)
        if kind[j] != kind[i] or ply[j] != ply[i]:
            mir_bad += 1

    no_cursed = max_w <= PLY_CAP
    if console:
        print("KRRK solved: legal %d | W %d / L %d / D %d (cycles %d) | mates %d"
              % (legal_total, wins, losses, draws, drawn, mates))
        print("  longest win %d plies (%d moves) | cursed impossible: %s"
              % (max_w, (max_w + 1) // 2, no_cursed))
        print("  ROOK-SWAP violations (exhaustive): %d | mirror violations: %d | %.1fs"
              % (swap_bad, mir_bad, time.time() - t_start))
    return {"P": P, "kind": kind, "ply": ply, "legal": legal_total,
            "wins": wins, "losses": losses, "draws": draws,
            "max_dtm_plies": max_w, "swap_violations": swap_bad,
            "mirror_violations": mir_bad, "checkmates": mates,
            "elapsed_s": round(time.time() - t_start, 1)}


if __name__ == "__main__":
    solveRR()
