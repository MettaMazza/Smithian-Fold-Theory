"""Fold Chess — Rung 3 (phase 3a): generalized 4-piece state model and move
generation for KQKR (white: K+Q, black: K+R), under fold law.

New at this rung: a black piece, so check constraints run in both directions,
pins are real (a queen move may expose the white king to the rook and is then
illegal), and captures cross material boundaries into the solved 3-piece
tables. States are rationals (index + 1)/P exactly as at Rung 1.

Phase 3a ships ONLY the state model and movegen; the solver (3b) does not
start until the movegen survives the external rules referee on a large
seeded sample (rules_check4.py).
"""

import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import (_rank, _file, _on_board, _king_zone, _kings_touch,
                        _QUEEN_RAYS, _ROOK_RAYS, find_fold_prime)

Z = 1 - 1
BOARD = 64
NSTATES4 = 2 * BOARD ** 4          # (wk, wq, br, bk, stm)

WTM = Z
BTM = 1

# capture-transition sentinels (resolved against 3-piece tables by the solver)
CAP_WXR = NSTATES4 + 1             # white captures the rook  -> KQK table
CAP_BXQ = NSTATES4 + 2             # black captures the queen -> colour-flipped KRK


def encode4(wk, wq, br, bk, stm):
    return (((wk * BOARD + wq) * BOARD + br) * BOARD + bk) * 2 + stm


def decode4(idx):
    stm = idx % 2
    idx //= 2
    bk = idx % BOARD
    idx //= BOARD
    br = idx % BOARD
    idx //= BOARD
    wq = idx % BOARD
    wk = idx // BOARD
    return wk, wq, br, bk, stm


def _slider_attacks(psq, rays, occupied, transparent=None):
    """Squares a slider attacks: rays stop AT occupied squares (which are
    attacked), passing through `transparent` (a king evaluating its own
    retreat squares must be transparent to the ray that checks it)."""
    out = set()
    r, c = _rank(psq), _file(psq)
    for dr, dc in rays:
        rr, cc = r + dr, c + dc
        while _on_board(rr, cc):
            t = rr * 8 + cc
            out.add(t)
            if t in occupied and t != transparent:
                break
            rr += dr
            cc += dc
    return out


def white_in_check(wk, wq, br, bk):
    """Is the white king attacked by black? (rook rays; black king adjacency
    is excluded at the state level by the kings-touch rule)."""
    return wk in _slider_attacks(br, _ROOK_RAYS, {wq, bk}, None)


def black_in_check(wk, wq, br, bk):
    return bk in _slider_attacks(wq, _QUEEN_RAYS, {wk, br}, None)


def is_legal4(wk, wq, br, bk, stm):
    sqs = [wk, wq, br, bk]
    if len(set(sqs)) != 4:
        return False
    if _kings_touch(wk, bk):
        return False
    if stm == WTM and black_in_check(wk, wq, br, bk):
        return False
    if stm == BTM and white_in_check(wk, wq, br, bk):
        return False
    return True


def _gen4(idx):
    """Yield (from_sq, to_sq, successor) for every fully legal move of the
    side to move. Capture successors are (sentinel, payload) pairs resolved
    by the solver in the 3-piece tables:
      (CAP_WXR, kqk_index)  — white queen or king takes the rook
      (CAP_BXQ, krk_index_colour_flipped) — black rook or king takes the queen
    Non-capture successors are plain 4-piece indices."""
    from fold_chess import encode as encode3
    wk, wq, br, bk, stm = decode4(idx)
    out = []
    if stm == WTM:
        # --- white king moves (may capture the rook)
        bk_zone = set(_king_zone(bk))
        for t in _king_zone(wk):
            if t == wq or t == bk:
                continue
            if t in bk_zone:                       # would touch the black king
                continue
            if t == br:
                # capture the rook iff the rook is undefended by the black king
                if not _kings_touch(br, bk):
                    out.append((wk, t, (CAP_WXR, encode3(t, wq, bk, BTM))))
                continue
            # after the move, white king must not stand in rook fire
            if t in _slider_attacks(br, _ROOK_RAYS, {wq, bk}, None):
                continue
            out.append((wk, t, encode4(t, wq, br, bk, BTM)))
        # --- white queen moves (may capture the rook; may be pinned)
        r, c = _rank(wq), _file(wq)
        for dr, dc in _QUEEN_RAYS:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                t = rr * 8 + cc
                if t == wk or t == bk:
                    break
                if t == br:
                    # capture: afterwards white king must not be in check
                    # (rook is gone, so only adjacency matters — none possible)
                    out.append((wq, t, (CAP_WXR, encode3(wk, t, bk, BTM))))
                    break
                # pin test: with the queen on t, does the rook hit the king?
                if wk in _slider_attacks(br, _ROOK_RAYS, {t, bk}, None):
                    rr += dr
                    cc += dc
                    continue
                out.append((wq, t, encode4(wk, t, br, bk, BTM)))
                rr += dr
                cc += dc
    else:
        # --- black king moves (may capture the queen)
        danger = _slider_attacks(wq, _QUEEN_RAYS, {wk, br, bk}, bk)
        danger.update(_king_zone(wk))
        for t in _king_zone(bk):
            if t == wk or t == br:
                continue
            if t == wq:
                # capture the queen iff undefended by the white king;
                # the remaining K+R(black) vs K is the colour-flip of our KRK
                if not _kings_touch(wq, wk):
                    out.append((bk, t, (CAP_BXQ, _flip_to_krk(wk, br, t))))
                continue
            if t in danger:
                continue
            out.append((bk, t, encode4(wk, wq, br, t, WTM)))
        # --- black rook moves (may capture the queen; may be pinned to bk)
        r, c = _rank(br), _file(br)
        for dr, dc in _ROOK_RAYS:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                t = rr * 8 + cc
                if t == bk or t == wk:
                    break
                if t == wq:
                    # capture: afterwards black king must not be in check;
                    # only the queen gave checks, and it is gone
                    out.append((br, t, (CAP_BXQ, _flip_to_krk(wk, t, bk))))
                    break
                # pin test: with the rook on t (and br vacated), is bk in
                # queen fire? Interposition on the pin line passes naturally,
                # because the ray stops at t before reaching bk.
                if bk in _slider_attacks(wq, _QUEEN_RAYS, {wk, t}, None):
                    rr += dr
                    cc += dc
                    continue
                out.append((br, t, encode4(wk, wq, t, bk, WTM)))
                rr += dr
                cc += dc
    return out


def successors4(idx):
    """Successor view of _gen4 (what the solver consumes)."""
    return [s for _, _, s in _gen4(idx)]


def moves4(idx):
    """(from_sq, to_sq) view of _gen4 (what the rules referee compares)."""
    return [(f, t) for f, t, _ in _gen4(idx)]


def _flip_to_krk(wk, rook_sq, bk):
    """Colour-flip a position where BLACK holds the rook into our KRK table's
    convention (WHITE holds the rook): swap colours and flip ranks (s -> s
    XOR 56), side to move flips to white-to-move (the capture handed the
    move to the queen's former owner)."""
    from fold_chess import encode as encode3
    f = lambda s: s ^ 56
    # black king becomes the white(rook-side) king, white king becomes the
    # bare king; after black's capture it is white to move in the real game,
    # which is the BARE side to move = BTM in the flipped KRK convention.
    return encode3(f(bk), f(rook_sq), f(wk), 1)


if __name__ == "__main__":
    P = find_fold_prime(NSTATES4)
    print("Rung 3 state space: %d raw states; fold prime P = %d" % (NSTATES4, P))
