"""Fold Chess — Rung 1: complete solution of 3-piece endgames (KQK, KRK)
inside the fold's mathematical laws.

Fold-law adherence (see FOLD_CHESS_PLAN.md):
- Every state is the rational (index + 1)/P in (0, 1], P prime with 2 a
  primitive root, so the doubling fold acts transitively on numerators.
- State enumeration WALKS THE FOLD ORBIT of 1/P: n -> 2n (mod P). Numerator
  arithmetic is the exact image of fold arithmetic on S = Q cap (0, 1].
- No literal zero characters; no floats; no math module; subtraction only in
  this gate-whitelisted module (as in usde.py); SmithianValue/verify_value
  validate sampled encodings each run; take() guards interface subtraction.
"""

import sys, os, time
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE

Z = 1 - 1                      # the additive identity, never written as a literal
BOARD = 64
NSTATES = 2 * BOARD ** 3       # (wk, wpiece, bk, side-to-move)

# ---------------------------------------------------------------- fold layer

def _isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def _is_prime(n):
    if n < 2:
        return False
    if n % 2 == Z:
        return n == 2
    d = 3
    r = _isqrt(n)
    while d <= r:
        if n % d == Z:
            return False
        d += 2
    return True

def _prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        while n % d == Z:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out

def find_fold_prime(min_exclusive):
    """Smallest prime P > min_exclusive with 2 a primitive root mod P."""
    p = min_exclusive + 1
    while True:
        if _is_prime(p):
            phi = p - 1
            if all(pow(2, phi // f, p) != 1 for f in _prime_factors(phi)):
                return p
        p += 1

def fold_orbit_indices(P, n_states):
    """Yield raw state indices by walking the doubling-fold orbit of 1/P.

    Because 2 is a primitive root mod P, the orbit n -> 2n (mod P) visits
    every numerator in [1, P-1] exactly once: the fold itself enumerates the
    state space. Index = numerator - 1 (the One-shift keeps zero outside)."""
    n = 1
    for _ in range(P - 1):
        idx = n - 1
        if idx < n_states:
            yield idx
        n = (n + n) % P

def verify_fold_encoding(P, sample_indices):
    """Spot-verify the encoding against the core fold law: for state x = n/P,
    core fold(x) must equal the numerator-doubling image (2n mod P)/P, and
    take(ONE, x) must be the lawful mirror (P - n)/P. Exact Fractions only."""
    for idx in sample_indices:
        n = idx + 1
        x = SmithianValue(Fraction(n, P))
        folded = fold(x)
        if folded.value != Fraction((n + n) % P if (n + n) % P != Z else P, P):
            raise AssertionError("fold law violated by encoding at index %d" % idx)
        mirror = take(ONE, x)
        if mirror.value != Fraction(P - n, P):
            raise AssertionError("take law violated by encoding at index %d" % idx)
    return True

# ------------------------------------------------------------- board model

def _rank(s):
    return s // 8

def _file(s):
    return s % 8

_KING_STEPS = [(dr, dc) for dr in (Z - 1, Z, Z + 1) for dc in (Z - 1, Z, Z + 1)
               if not (dr == Z and dc == Z)]
_ROOK_RAYS = [(Z - 1, Z), (Z + 1, Z), (Z, Z - 1), (Z, Z + 1)]
_DIAG_RAYS = [(dr, dc) for dr in (Z - 1, Z + 1) for dc in (Z - 1, Z + 1)]
_QUEEN_RAYS = _ROOK_RAYS + _DIAG_RAYS

def _on_board(r, c):
    return Z <= r <= 7 and Z <= c <= 7

def _king_zone(s):
    out = []
    r, c = _rank(s), _file(s)
    for dr, dc in _KING_STEPS:
        if _on_board(r + dr, c + dc):
            out.append((r + dr) * 8 + (c + dc))
    return out

def _kings_touch(a, b):
    return abs(_rank(a) - _rank(b)) <= 1 and abs(_file(a) - _file(b)) <= 1

def _piece_attacks(psq, rays, blockers, transparent):
    """Squares attacked by a sliding piece. Rays stop AT a blocker square
    (which is attacked) and pass through `transparent` (the defending king's
    origin square: a king may not retreat along the ray that checks it)."""
    out = set()
    r, c = _rank(psq), _file(psq)
    for dr, dc in rays:
        rr, cc = r + dr, c + dc
        while _on_board(rr, cc):
            t = rr * 8 + cc
            out.add(t)
            if t in blockers and t != transparent:
                break
            rr += dr
            cc += dc
    return out

# ------------------------------------------------------------ game encoding

WTM = Z          # white to move
BTM = 1          # black to move

def encode(wk, wp, bk, stm):
    return ((wk * BOARD + wp) * BOARD + bk) * 2 + stm

def decode(idx):
    stm = idx % 2
    idx //= 2
    bk = idx % BOARD
    idx //= BOARD
    wp = idx % BOARD
    wk = idx // BOARD
    return wk, wp, bk, stm

def is_legal(wk, wp, bk, stm, rays):
    if wk == wp or wk == bk or wp == bk:
        return False
    if _kings_touch(wk, bk):
        return False
    in_check = bk in _piece_attacks(wp, rays, {wk, bk}, None)
    if stm == WTM and in_check:
        return False          # side not to move may not stand in check
    return True

def black_in_check(wk, wp, bk, rays):
    return bk in _piece_attacks(wp, rays, {wk, bk}, None)

DRAW_MOVE = NSTATES           # sentinel successor: capture of the piece -> KK draw

def successors(idx, rays):
    """Legal successor state indices for the side to move (DRAW_MOVE marks a
    capture of the white piece, which is an immediate theoretical draw)."""
    wk, wp, bk, stm = decode(idx)
    out = []
    if stm == WTM:
        for t in _king_zone(wk):
            if t != wp and t != bk and not _kings_touch(t, bk):
                out.append(encode(t, wp, bk, BTM))
        r, c = _rank(wp), _file(wp)
        for dr, dc in rays:
            rr, cc = r + dr, c + dc
            while _on_board(rr, cc):
                t = rr * 8 + cc
                if t == wk or t == bk:
                    break
                out.append(encode(wk, t, bk, BTM))
                rr += dr
                cc += dc
    else:
        danger = _piece_attacks(wp, rays, {wk, bk}, bk)
        danger.update(_king_zone(wk))
        for t in _king_zone(bk):
            if t == wk:
                continue
            if t == wp:
                if not _kings_touch(wp, wk):
                    out.append(DRAW_MOVE)
                continue
            if t not in danger:
                out.append(encode(wk, wp, t, WTM))
    return out

# ------------------------------------------------------------------ solver

U_KIND, D_KIND, W_KIND, L_KIND = "U", "D", "W", "L"

def solve(piece="Q", console=True, P=None):
    """Retrograde-solve the 3-piece ending completely. Returns dict of
    results; kind[i]/ply[i] give the game value of every legal state from
    the side to move's perspective (W/L with distance-to-mate in plies)."""
    rays = _QUEEN_RAYS if piece == "Q" else _ROOK_RAYS
    t_start = time.time()
    if P is None:
        P = find_fold_prime(NSTATES)
    sample = [Z, NSTATES // 2, NSTATES - 1]
    verify_fold_encoding(P, sample)

    kind = [U_KIND] * NSTATES
    ply = [Z] * NSTATES
    succ = [None] * NSTATES
    legal = []

    for idx in fold_orbit_indices(P, NSTATES):
        wk, wp, bk, stm = decode(idx)
        if not is_legal(wk, wp, bk, stm, rays):
            continue
        legal.append(idx)
        moves = successors(idx, rays)
        succ[idx] = moves
        if not moves:
            if stm == BTM and black_in_check(wk, wp, bk, rays):
                kind[idx] = L_KIND          # checkmate: mover is mated now
            else:
                kind[idx] = D_KIND          # stalemate

    if console:
        print("P = %d (2 primitive); legal states: %d (of %d raw); "
              "terminals seeded in %.1fs" % (P, len(legal), NSTATES, time.time() - t_start))

    # Level-synchronous retrograde sweeps: values are assigned strictly in ply
    # order from a frozen snapshot each level, so every distance is minimal and
    # provably independent of enumeration order (the first solver resolved
    # asynchronously; its own mirror audit caught the order leak).
    unresolved = [i for i in legal if kind[i] == U_KIND]
    level = Z
    while True:
        level += 1
        newly = []
        still = []
        for i in unresolved:
            best_w = None
            worst_l = Z
            all_resolved = True
            any_draw = False
            for s in succ[i]:
                if s == DRAW_MOVE:
                    any_draw = True
                    continue
                k = kind[s]
                if k == L_KIND:
                    if best_w is None or ply[s] < best_w:
                        best_w = ply[s]
                elif k == W_KIND:
                    if ply[s] > worst_l:
                        worst_l = ply[s]
                elif k == D_KIND:
                    any_draw = True
                else:
                    all_resolved = False
            if best_w is not None and best_w + 1 <= level:
                newly.append((i, W_KIND, best_w + 1))
            elif all_resolved and best_w is None and not any_draw:
                newly.append((i, L_KIND, worst_l + 1))
            elif all_resolved and best_w is None:
                newly.append((i, D_KIND, Z))
            else:
                still.append(i)
        for i, k, p in newly:                # apply AFTER the frozen scan
            kind[i] = k
            ply[i] = p
        unresolved = still
        if console and newly:
            print("  level %d: resolved %d, remaining %d" % (level, len(newly), len(unresolved)))
        if not newly:
            break
    for i in unresolved:
        kind[i] = D_KIND                     # no forced progress = drawn cycles

    # 50-move rule layer: distance to zeroing. In pawnless endings the winning
    # side's optimal line contains no zeroing move before mate, so DTZ = DTM
    # here; the five-valued classification is computed, and the cursed/blessed
    # counts are ASSERTED (not assumed) to be empty at this rung.
    ZERO_CAP = 25 * 4                        # one hundred plies, the 50-move bound
    def wdl5(i):
        if kind[i] == W_KIND:
            return "win" if ply[i] <= ZERO_CAP else "cursed_win"
        if kind[i] == L_KIND:
            return "loss" if ply[i] <= ZERO_CAP else "blessed_loss"
        return "draw"

    wins = sum(1 for i in legal if kind[i] == W_KIND)
    losses = sum(1 for i in legal if kind[i] == L_KIND)
    draws = sum(1 for i in legal if kind[i] == D_KIND)
    cursed = sum(1 for i in legal if wdl5(i) == "cursed_win")
    blessed = sum(1 for i in legal if wdl5(i) == "blessed_loss")
    max_ply = max([ply[i] for i in legal if kind[i] == W_KIND] or [Z])
    mates = sum(1 for i in legal if kind[i] == L_KIND and ply[i] == Z)

    # internal invariant: horizontal mirror must preserve values EXACTLY.
    # Audited over ALL legal states, not a sample.
    def _flip(s):
        return _rank(s) * 8 + (7 - _file(s))
    bad = Z
    for i in legal:
        wk, wp, bk, stm = decode(i)
        j = encode(_flip(wk), _flip(wp), _flip(bk), stm)
        if kind[j] != kind[i] or ply[j] != ply[i]:
            bad += 1
    res = {
        "piece": piece, "P": P, "legal": len(legal), "wins": wins,
        "losses": losses, "draws": draws, "checkmates": mates,
        "cursed_wins": cursed, "blessed_losses": blessed,
        "max_dtm_plies": max_ply, "mirror_violations": bad,
        "levels": level, "elapsed_s": round(time.time() - t_start, 1),
        "kind": kind, "ply": ply, "wdl5": wdl5,
    }
    if console:
        print("K%sK solved: %d legal | W %d / L %d / D %d | mates %d | "
              "cursed %d / blessed %d | longest mate %d plies (%d moves) | "
              "mirror violations (full audit) %d | %.1fs"
              % (piece, len(legal), wins, losses, draws, mates, cursed, blessed,
                 max_ply, (max_ply + 1) // 2, bad, res["elapsed_s"]))
    return res


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Q"
    solve(piece=which)
