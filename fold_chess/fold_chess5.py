"""Fold Chess — Rung 4 (phase a): five-piece state model and move generation
for KQKRR (white: K+Q, black: K + two rooks), under fold law.

New at this rung: two enemy rooks, so (i) the white king/queen may be checked
by EITHER rook, (ii) capturing one rook must respect defence by the OTHER
rook, and (iii) the two black rooks are identical, so the value field carries
an exhaustive rook-swap symmetry. Captures cross material boundaries into the
two CERTIFIED four-piece tables:
  - white (K or Q) takes a rook  -> KQKR   (white K+Q vs black K+remaining R)
  - black (K or R) takes the queen -> KRRK (colour-flipped: two rooks vs bare K)
States are rationals (index + 1)/P exactly as at every prior rung.

Phase a ships ONLY the state model and movegen; the solver does not start
until the movegen survives the external rules referee on a large seeded
sample (rules_check5.py) with zero diffs.
"""

import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import (_rank, _file, _on_board, _king_zone, _kings_touch,
                        _QUEEN_RAYS, _ROOK_RAYS, find_fold_prime)
from fold_chess4 import _slider_attacks

Z = 1 - 1
BOARD = 64
NSTATES5 = 2 * BOARD ** 5          # (wk, wq, r1, r2, bk, stm)

WTM = Z
BTM = 1

# capture-transition sentinels (resolved against the 4-piece tables by solver)
CAP_WXR = NSTATES5 + 1             # white captures a rook  -> KQKR table
CAP_BXQ = NSTATES5 + 2             # black captures the queen -> colour-flipped KRRK


def encode5(wk, wq, r1, r2, bk, stm):
    return ((((wk * BOARD + wq) * BOARD + r1) * BOARD + r2) * BOARD + bk) * 2 + stm


def decode5(idx):
    stm = idx % 2
    idx //= 2
    bk = idx % BOARD
    idx //= BOARD
    r2 = idx % BOARD
    idx //= BOARD
    r1 = idx % BOARD
    idx //= BOARD
    wq = idx % BOARD
    wk = idx // BOARD
    return wk, wq, r1, r2, bk, stm


def white_in_check5(wk, wq, r1, r2, bk):
    """White king attacked by EITHER black rook."""
    if wk in _slider_attacks(r1, _ROOK_RAYS, {wq, r2, bk}, None):
        return True
    if wk in _slider_attacks(r2, _ROOK_RAYS, {wq, r1, bk}, None):
        return True
    return False


def black_in_check5(wk, wq, r1, r2, bk):
    """Black king attacked by the white queen."""
    return bk in _slider_attacks(wq, _QUEEN_RAYS, {wk, r1, r2}, None)


def is_legal5(wk, wq, r1, r2, bk, stm):
    sqs = [wk, wq, r1, r2, bk]
    if len(set(sqs)) != 5:
        return False
    if _kings_touch(wk, bk):
        return False
    if stm == WTM and black_in_check5(wk, wq, r1, r2, bk):
        return False
    if stm == BTM and white_in_check5(wk, wq, r1, r2, bk):
        return False
    return True


def _flip_to_krrk(bk, r1, r2, wk):
    """Colour-flip a position where BLACK holds the two rooks (vs white's bare
    king) into the KRRK table convention (WHITE holds the rooks vs a bare black
    king): swap colours, flip ranks (s -> s XOR 56). The real side to move
    after black's capture is white (the bare side); in KRRK that is the bare
    side to move = BTM. Rook order is irrelevant (rook-swap symmetry)."""
    from fold_chessRR import encodeRR
    f = lambda s: s ^ 56
    return encodeRR(f(bk), f(r1), f(r2), f(wk), BTM)


def _gen5(idx):
    """Yield (from_sq, to_sq, successor) for every fully legal move of the
    side to move. Capture successors are (sentinel, payload) resolved by the
    solver in the certified 4-piece tables:
      (CAP_WXR, kqkr_index)              — white queen/king takes a rook
      (CAP_BXQ, krrk_index_colour_flip)  — black rook/king takes the queen
    Non-capture successors are plain 5-piece indices."""
    from fold_chess4 import encode4
    wk, wq, r1, r2, bk, stm = decode5(idx)
    out = []
    if stm == WTM:
        # --- white king moves (may capture a rook)
        bk_zone = set(_king_zone(bk))
        for t in _king_zone(wk):
            if t == wq or t == bk:
                continue
            if t in bk_zone:                      # would touch the black king
                continue
            if t == r1 or t == r2:
                other = r2 if t == r1 else r1
                # capture the rook iff afterwards the king is not attacked by
                # the OTHER rook (captured rook gone, king vacated wk)
                if t not in _slider_attacks(other, _ROOK_RAYS, {wq, bk}, None):
                    out.append((wk, t, (CAP_WXR, encode4(t, wq, other, bk, BTM))))
                continue
            # non-capture: t must not be in fire of either rook (king vacated)
            if t in _slider_attacks(r1, _ROOK_RAYS, {wq, bk, r2}, None):
                continue
            if t in _slider_attacks(r2, _ROOK_RAYS, {wq, bk, r1}, None):
                continue
            out.append((wk, t, encode5(t, wq, r1, r2, bk, BTM)))
        # --- white queen moves (may capture a rook; may be pinned)
        r, c = _rank(wq), _file(wq)
        for dr, dc in _QUEEN_RAYS:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                t = rr * 8 + cc
                if t == wk or t == bk:
                    break
                if t == r1 or t == r2:
                    other = r2 if t == r1 else r1
                    # capture: afterwards white king must not be in check by
                    # the other rook (queen now on t as a blocker)
                    if wk not in _slider_attacks(other, _ROOK_RAYS, {t, bk}, None):
                        out.append((wq, t, (CAP_WXR, encode4(wk, t, other, bk, BTM))))
                    break
                # pin test: with the queen on t, does either rook hit the king?
                if wk in _slider_attacks(r1, _ROOK_RAYS, {t, bk, r2}, None):
                    rr += dr
                    cc += dc
                    continue
                if wk in _slider_attacks(r2, _ROOK_RAYS, {t, bk, r1}, None):
                    rr += dr
                    cc += dc
                    continue
                out.append((wq, t, encode5(wk, t, r1, r2, bk, BTM)))
                rr += dr
                cc += dc
    else:
        # --- black king moves (may capture the queen)
        danger = _slider_attacks(wq, _QUEEN_RAYS, {wk, r1, r2, bk}, bk)
        danger.update(_king_zone(wk))
        for t in _king_zone(bk):
            if t == r1 or t == r2 or t == wk:
                continue
            if t == wq:
                # capture the queen iff undefended by the white king
                if not _kings_touch(wq, wk):
                    out.append((bk, t, (CAP_BXQ, _flip_to_krrk(t, r1, r2, wk))))
                continue
            if t in danger:
                continue
            out.append((bk, t, encode5(wk, wq, r1, r2, t, WTM)))
        # --- black rook moves (each rook; may capture the queen; may be pinned)
        for which in (1, 2):
            rsq = r1 if which == 1 else r2
            other = r2 if which == 1 else r1
            r, c = _rank(rsq), _file(rsq)
            for dr, dc in _ROOK_RAYS:
                rr, cc = r + dr, c + dc
                while _on_board(rr, cc):
                    t = rr * 8 + cc
                    if t == bk or t == wk or t == other:
                        break
                    if t == wq:
                        # capture the queen: afterwards black king cannot be in
                        # check (only the queen checked it, and it is gone)
                        if which == 1:
                            out.append((rsq, t, (CAP_BXQ, _flip_to_krrk(bk, t, other, wk))))
                        else:
                            out.append((rsq, t, (CAP_BXQ, _flip_to_krrk(bk, other, t, wk))))
                        break
                    # pin test: with this rook on t (rsq vacated), is bk in
                    # queen fire? blockers {wk, t, other rook}
                    if bk in _slider_attacks(wq, _QUEEN_RAYS, {wk, t, other}, None):
                        rr += dr
                        cc += dc
                        continue
                    if which == 1:
                        out.append((rsq, t, encode5(wk, wq, t, r2, bk, WTM)))
                    else:
                        out.append((rsq, t, encode5(wk, wq, r1, t, bk, WTM)))
                    rr += dr
                    cc += dc
    return out


def successors5(idx):
    return [s for _, _, s in _gen5(idx)]


def moves5(idx):
    return [(f, t) for f, t, _ in _gen5(idx)]


if __name__ == "__main__":
    P = find_fold_prime(NSTATES5)
    print("Rung 4 state space: %d raw states (= 2^%d); fold prime P = %d"
          % (NSTATES5, NSTATES5.bit_length() - 1, P))
