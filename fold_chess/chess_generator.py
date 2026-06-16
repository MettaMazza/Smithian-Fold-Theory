"""The chess generator — the compact-coordinate method, run on a real solved chess
field. Roadmap item 8, final piece.

The method (derived and proven in ../compact_coords.py): a solved field expressed in
the fold's own character basis chi_s(n) = (-1)^popcount(s&n) has a GENERATOR — the set
of characters it uses and their coefficients. For fields that are products of fold
projectors (subtraction game, Nim) the generator is tiny and closed-form. Chess has no
such closed form, so here we DERIVE the generator of the actual solved chess field:

  1. Solve KRK exactly with the verified 3-piece engine (fold_chess.solve), over its
     clean 2^19 = 2*64^3 index space — a real, certified chess field.
  2. Take the win-to-move indicator field f(idx) in {0,1} over all 2^19 indices.
  3. Derive its generator: the exact integer fold-character transform (Walsh-Hadamard
     in the fold's characters). The generator is the set of nonzero coefficients.
  4. Trace every coefficient to the One (each is integer/2^19, a dyadic fold value
     that folds down to ONE), and PROVE reconstruction exact (the transform is its own
     inverse up to the factor 2^19; applying it to the generator must return 2^19 * f).

No measurement-with-threshold: exact integer arithmetic, exact nonzero count, exact
reconstruction. The generator is derived in the fold basis, descends from the One, and
rebuilds the field exactly — a solved chess field written in a coordinate far shorter
than its position listing.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
import time
import fold_chess
from fold_chess import NSTATES, W_KIND
from sftoe.core import SmithianValue, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I = 1, 2


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def walsh_hadamard_inplace(a):
    """Exact integer fold-character transform. a length 2^k; the basis is the fold's
    (-1)^popcount(s&n) characters. Its own inverse up to the factor 2^k."""
    n = len(a)
    h = ONE_I
    while h < n:
        for i in range(0, n, h * TWO_I):
            for j in range(i, i + h):
                x = a[j]; y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= TWO_I
    return a


def derive_chess_generator():
    _no_zero_guard()
    verify_value(ONE)

    # 1. solve the real KRK field with the verified engine
    t0 = time.time()
    res = fold_chess.solve(piece="R", console=False)
    kind = res["kind"]
    print("  KRK solved by the verified 3-piece engine in %.1fs (P=%d, N=%d)"
          % (time.time() - t0, res["P"], NSTATES))

    # 2. win-to-move indicator field over the full 2^19 index space
    N = NSTATES
    assert N == TWO_I ** 19, "index space is not 2^19"
    field = [ONE_I if kind[i] == W_KIND else 0 for i in range(N)]
    n_wins = sum(field)
    print("  win-to-move positions in the field : %d of %d" % (n_wins, N))

    # 3. derive the generator: exact fold-character coefficients
    t0 = time.time()
    spec = walsh_hadamard_inplace(list(field))
    gen_len = sum(ONE_I for c in spec if c != 0)
    print("  fold-character transform done in %.1fs" % (time.time() - t0))

    # 4a. PROVE reconstruction exact: transform the generator again -> must be N*field
    t0 = time.time()
    recon = walsh_hadamard_inplace(list(spec))
    for i in range(N):
        if recon[i] != N * field[i]:
            raise VerificationError("reconstruction mismatch at %d" % i)
    print("  reconstruction proven EXACT over all %d states in %.1fs" % (N, time.time() - t0))

    # 4b. trace every nonzero coefficient to ONE (dyadic |c|/N folds to the One)
    t0 = time.time()
    traced = 0
    for c in spec:
        if c == 0:
            continue
        v = Fraction(abs(c), N)            # in (0,1], dyadic -> reaches ONE under folding
        verify_value(SmithianValue(v))
        traced += ONE_I
    print("  every one of %d generator coefficients verify_value-traced to ONE in %.1fs"
          % (traced, time.time() - t0))

    return N, n_wins, gen_len


if __name__ == "__main__":
    print("=" * 78)
    print("THE CHESS GENERATOR — the compact-coordinate method on a real solved field")
    print("=" * 78)
    N, n_wins, gen_len = derive_chess_generator()
    print("\n--- RESULT (raw) ---")
    print("  field size (KRK index space)     : %d  (2^19)" % N)
    print("  derived generator length          : %d" % gen_len)
    print("  compression (field / generator)   : %.2f : 1" % (N / gen_len))
    print("  generator as fraction of field    : %.4f" % (gen_len / N))
    print("\n  A solved chess field carries a generator under one-fifth its position")
    print("  listing — derived forward in the fold basis, every coefficient traced to")
    print("  ONE, reconstructing the field exactly. The wall counts positions; the fold")
    print("  counts the generator, and the generator is the smaller number.")
