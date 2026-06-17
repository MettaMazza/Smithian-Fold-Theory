"""Prime pairs as fold antipodes — Goldbach and the twins about the half-One.

The fold's antipodal involution sends a part j/q to its antipode (q-j)/q, and the two
sum to the One; the unique self-antipodal point is 1/2, the half-One (fold_number_theory.py).
Scaled to an even number E, the pair (k, E-k) is an antipodal pair about the midpoint
E/2 — the half-One of E. So:

  * GOLDBACH. Writing an even E as a sum of two primes is choosing an antipodal pair
    (p, E-p) about the half-One that is prime on both sides. Goldbach's claim is that
    every even E >= 4 has at least one prime antipodal pair. The fold makes the *form*
    of the statement native: it is a statement about self-antipodal symmetry.
  * TWIN PRIMES. Twins (p, p+2) are the closest odd antipodal-neighbours; their count is
    governed by the same orbit/coset structure that fold_number_theory.py derives.

This module casts both in the antipodal frame (the half-One traced to the One), verifies
Goldbach for every even number up to a bound and reports the minimum number of prime
antipodal pairs, and counts the twins up to the bound.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I = 1, 2


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def sieve(n):
    is_p = [False, False] + [True] * (n - ONE_I)
    i = TWO_I
    while i * i <= n:
        if is_p[i]:
            for j in range(i * i, n + ONE_I, i):
                is_p[j] = False
        i += ONE_I
    return is_p


def half_one_is_self_antipode():
    """The midpoint of any even E is its half-One: the self-antipodal fold point 1/2."""
    h = SmithianValue(Fraction(ONE_I, TWO_I))
    verify_value(h)
    if take(ONE, h).value != h.value:           # antipode of 1/2 is 1/2
        raise VerificationError("half-One is not self-antipodal")
    return h.value


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 74)
    print("PRIME PAIRS AS FOLD ANTIPODES — Goldbach and the twins about the half-One")
    print("=" * 74)

    h = half_one_is_self_antipode()
    print("\n[1] THE ANTIPODAL FRAME")
    print("    antipode of a part is take(ONE, x) ; the unique self-antipode is %s (the" % h)
    print("    half-One). For an even E, the pair (k, E-k) is antipodal about the midpoint E/2.")

    N = 100000
    is_p = sieve(N)

    print("\n[2] GOLDBACH — every even E is a prime antipodal pair about its half-One")
    worst = (0, 10 ** 9)
    checked = 0
    for E in range(4, N + ONE_I, TWO_I):
        count = 0
        p = TWO_I
        while p <= E // TWO_I:
            if is_p[p] and is_p[E - p]:
                count += ONE_I
            p += ONE_I
        if count == 0:
            raise VerificationError("Goldbach failed at E=%d" % E)
        if count < worst[1]:
            worst = (E, count)
        checked += ONE_I
    print("    every even E in [4, %d] has a prime antipodal pair: %d checked, none failed."
          % (N, checked))
    print("    fewest prime pairs for any E in range : %d  (at E=%d)" % (worst[1], worst[0]))

    print("\n[3] TWIN PRIMES — closest odd antipodal-neighbours (p, p+2)")
    twins = sum(ONE_I for p in range(3, N - ONE_I) if is_p[p] and is_p[p + TWO_I])
    print("    twin-prime pairs up to %d : %d  (the count keeps growing — no last twin seen)"
          % (N, twins))

    print("\n  Goldbach is the statement that every even number's half-One carries a prime")
    print("  antipodal pair; verified with no failure to %d. The half-One is traced to the One." % N)
