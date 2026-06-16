"""Fold Chess — KRRRK (three white rooks vs a bare black king), the five-piece
prerequisite for the six-piece KQKRRR climb. Captures land in the certified
KRRK table (black king takes a rook -> two rooks vs bare king). Three identical
rooks => a 3! rook-permutation symmetry on the value field. State model and
movegen only; the solver runs after the rules referee passes with zero diffs.
"""
import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import (_rank, _file, _on_board, _king_zone, _kings_touch,
                        _ROOK_RAYS, find_fold_prime)
from fold_chess4 import _slider_attacks
from fold_chessRR import encodeRR

Z = 1 - 1
BOARD = 64
NSTATES_3R = 2 * BOARD ** 5          # (wk, r1, r2, r3, bk, stm)
WTM = Z
BTM = 1
CAP_KXR = NSTATES_3R + 1             # black king captures a rook -> KRRK table


def encode3R(wk, r1, r2, r3, bk, stm):
    return ((((wk * BOARD + r1) * BOARD + r2) * BOARD + r3) * BOARD + bk) * 2 + stm


def decode3R(idx):
    stm = idx % 2
    idx //= 2
    bk = idx % BOARD
    idx //= BOARD
    r3 = idx % BOARD
    idx //= BOARD
    r2 = idx % BOARD
    idx //= BOARD
    r1 = idx % BOARD
    wk = idx // BOARD
    return wk, r1, r2, r3, bk, stm


def black_in_check3R(wk, r1, r2, r3, bk):
    if bk in _slider_attacks(r1, _ROOK_RAYS, {wk, r2, r3}, None):
        return True
    if bk in _slider_attacks(r2, _ROOK_RAYS, {wk, r1, r3}, None):
        return True
    if bk in _slider_attacks(r3, _ROOK_RAYS, {wk, r1, r2}, None):
        return True
    return False


def is_legal3R(wk, r1, r2, r3, bk, stm):
    if len({wk, r1, r2, r3, bk}) != 5:
        return False
    if _kings_touch(wk, bk):
        return False
    # the side NOT to move may not already be in check; only the bare black
    # king can be in check, so when WTM (black not to move) bk must be safe.
    if stm == WTM and black_in_check3R(wk, r1, r2, r3, bk):
        return False
    return True


def _genRRR(idx):
    """Legal moves of the side to move. Black king may capture a rook iff that
    rook is undefended (by the king or by either other rook); the remaining two
    rooks form the certified KRRK position (no colour flip)."""
    wk, r1, r2, r3, bk, stm = decode3R(idx)
    out = []
    if stm == WTM:
        # white king moves (cannot pass into the black king's zone or onto a rook)
        bk_zone = set(_king_zone(bk))
        for t in _king_zone(wk):
            if t in (r1, r2, r3, bk):
                continue
            if t in bk_zone:
                continue
            out.append((wk, t, encode3R(t, r1, r2, r3, bk, BTM)))
        # white rook moves (each rook; blocked by the other rooks, kings)
        for which in (1, 2, 3):
            rsq = (r1, r2, r3)[which - 1]
            others = [s for k, s in ((1, r1), (2, r2), (3, r3)) if k != which]
            r, c = _rank(rsq), _file(rsq)
            for dr, dc in _ROOK_RAYS:
                rr, cc = r + dr, c + dc
                while _on_board(rr, cc):
                    t = rr * 8 + cc
                    if t == wk or t == bk or t in others:
                        break
                    nr = [r1, r2, r3]
                    nr[which - 1] = t
                    out.append((rsq, t, encode3R(wk, nr[0], nr[1], nr[2], bk, BTM)))
                    rr += dr
                    cc += dc
    else:
        # bare black king moves (may capture an undefended rook)
        danger = set(_king_zone(wk))
        for which in (1, 2, 3):
            rsq = (r1, r2, r3)[which - 1]
            others = [s for k, s in ((1, r1), (2, r2), (3, r3)) if k != which]
            danger |= _slider_attacks(rsq, _ROOK_RAYS, {wk} | set(others), None)
        for t in _king_zone(bk):
            if t == wk:
                continue
            if t in (r1, r2, r3):
                # capture rook t iff t is not defended (not in danger from the
                # rest), i.e. the remaining KRRK position has bk legally on t.
                which = (r1, r2, r3).index(t) + 1
                others = [s for k, s in ((1, r1), (2, r2), (3, r3)) if k != which]
                defended = (t in _slider_attacks(others[0], _ROOK_RAYS, {wk, others[1]}, None)
                            or t in _slider_attacks(others[1], _ROOK_RAYS, {wk, others[0]}, None)
                            or _kings_touch(t, wk))
                if not defended:
                    out.append((bk, t, (CAP_KXR, encodeRR(wk, others[0], others[1], t, BTM))))
                continue
            if t in danger:
                continue
            out.append((bk, t, encode3R(wk, r1, r2, r3, t, WTM)))
    return out


def successors3R(idx):
    return [s for _, _, s in _genRRR(idx)]


def moves3R(idx):
    return [(f, t) for f, t, _ in _genRRR(idx)]


if __name__ == "__main__":
    P = find_fold_prime(NSTATES_3R)
    print("KRRRK raw states: %d (2^%d); fold prime P=%d"
          % (NSTATES_3R, NSTATES_3R.bit_length() - 1, P))
