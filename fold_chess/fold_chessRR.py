"""Fold Chess — KRRK state model and movegen (prerequisite table for the
five-piece KQKRR climb; see FOLD_CHESS_5_PLAN.md).

White: K + R + R. Black: bare K. Simpler than KQKR (no black piece, hence
no pins on white and no checks against white); the new wrinkle is two
IDENTICAL white pieces: every position has two index representations
(rooks swapped) which must carry identical values — a free exhaustive
internal invariant for the solver, and capture of either rook lands in the
certified KRK table.
"""

import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import (_rank, _file, _on_board, _king_zone, _kings_touch,
                        _ROOK_RAYS, encode as encode3)
from fold_chess4 import _slider_attacks, WTM, BTM

Z = 1 - 1
BOARD = 64
NSTATES_RR = 2 * BOARD ** 4          # (wk, r1, r2, bk, stm)

CAP_KXR = NSTATES_RR + 1             # black king captures a rook -> KRK table


def encodeRR(wk, r1, r2, bk, stm):
    return (((wk * BOARD + r1) * BOARD + r2) * BOARD + bk) * 2 + stm


def decodeRR(idx):
    stm = idx % 2
    idx //= 2
    bk = idx % BOARD
    idx //= BOARD
    r2 = idx % BOARD
    idx //= BOARD
    r1 = idx % BOARD
    wk = idx // BOARD
    return wk, r1, r2, bk, stm


def black_in_checkRR(wk, r1, r2, bk):
    occ = {wk, r1, r2}
    return (bk in _slider_attacks(r1, _ROOK_RAYS, occ, None)
            or bk in _slider_attacks(r2, _ROOK_RAYS, occ, None))


def is_legalRR(wk, r1, r2, bk, stm):
    if len({wk, r1, r2, bk}) != 4:
        return False
    if _kings_touch(wk, bk):
        return False
    if stm == WTM and black_in_checkRR(wk, r1, r2, bk):
        return False                  # side not to move may not stand in check
    return True


def _genRR(idx):
    """Yield (from_sq, to_sq, successor). (CAP_KXR, krk_index) marks the
    black king capturing an undefended rook — resolved in the certified KRK
    table (white keeps the other rook, WHITE remains the rook side)."""
    wk, r1, r2, bk, stm = decodeRR(idx)
    out = []
    occ = {wk, r1, r2, bk}
    if stm == WTM:
        for t in _king_zone(wk):
            if t in occ or _kings_touch(t, bk):
                continue
            out.append((wk, t, encodeRR(t, r1, r2, bk, BTM)))
        for which, rsq in ((1, r1), (2, r2)):
            rr_, cc_ = _rank(rsq), _file(rsq)
            for dr, dc in _ROOK_RAYS:
                a, b = rr_ + dr, cc_ + dc
                while _on_board(a, b):
                    t = a * 8 + b
                    if t in occ:
                        break
                    if which == 1:
                        out.append((rsq, t, encodeRR(wk, t, r2, bk, BTM)))
                    else:
                        out.append((rsq, t, encodeRR(wk, r1, t, bk, BTM)))
                    a += dr
                    b += dc
    else:
        danger = _slider_attacks(r1, _ROOK_RAYS, {wk, r2}, bk)
        danger |= _slider_attacks(r2, _ROOK_RAYS, {wk, r1}, bk)
        danger.update(_king_zone(wk))
        for t in _king_zone(bk):
            if t == wk:
                continue
            if t == r1 or t == r2:
                # capture a rook iff undefended (by king or the other rook)
                other = r2 if t == r1 else r1
                # after the capture the bk origin is VACATED: blockers on the
                # other rook's ray to t are the white king only
                defended = (_kings_touch(t, wk)
                            or t in _slider_attacks(other, _ROOK_RAYS, {wk}, None))
                if not defended:
                    # white keeps the other rook and it is WHITE to move:
                    # no colour flip here (unlike KQKR's rook capture)
                    out.append((bk, t, (CAP_KXR, encode3(wk, other, t, WTM))))
                continue
            if t in danger:
                continue
            out.append((bk, t, encodeRR(wk, r1, r2, t, WTM)))
    return out


def successorsRR(idx):
    return [s for _, _, s in _genRR(idx)]


def movesRR(idx):
    return [(f, t) for f, t, _ in _genRR(idx)]


if __name__ == "__main__":
    print("KRRK raw states: %d" % NSTATES_RR)
