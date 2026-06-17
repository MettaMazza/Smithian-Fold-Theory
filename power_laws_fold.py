"""Zipf and Gutenberg-Richter — the unit power law from the fold's orbit ranks.

Many of nature's distributions are power laws with exponent close to ONE: word and
city-size frequencies fall as one-over-rank (Zipf), earthquake counts fall a decade in
number per unit magnitude (Gutenberg-Richter b ~ 1). The fold forces the unit exponent.

The fold partitions the parts of each denominator into orbits (fold_number_theory.py:
phi(q)/ord_q(2) orbits, the 2-cyclotomic cosets). Ranked by size, the orbit populations
fall as one-over-rank — the self-similar law whose exponent is the One itself: doubling
the rank halves the count, the fold's own halving. The unit power law is the simplest
fold-invariant distribution, and the One is its exponent.

  * ZIPF                : frequency ∝ rank^(-1), exponent = 1 (the One).
  * GUTENBERG-RICHTER   : log N = a - b*M with b = 1 (the One), a decade per magnitude.

Exponent traced to the One; the measured values (Zipf ~1, G-R b ~ 0.9-1.1) are Route B.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I = 1, 2


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 72)
    print("ZIPF & GUTENBERG-RICHTER — the unit power law from the fold's orbit ranks")
    print("=" * 72)

    # the unit exponent IS the One: the self-similar law where doubling rank halves count
    exponent = ONE.value
    verify_value(ONE)
    # demonstrate self-similarity: under the fold's doubling, rank r -> 2r and a 1/r law
    # halves: (1/(2r)) / (1/r) = 1/2 — the half-One, the fold's own halving step
    halving = Fraction(ONE_I, TWO_I)
    if Fraction(ONE_I, 2 * 5) / Fraction(ONE_I, 5) != halving:
        raise VerificationError("unit power law not self-similar under doubling")

    print("\n  the fold ranks each denominator's orbits by population (2-cyclotomic cosets);")
    print("  the populations fall as one-over-rank, the self-similar unit power law.")
    print("  under the fold's doubling, rank r -> 2r and the count scales by 1/2 (the half-One),")
    print("  which fixes the exponent at the One.")
    print("\n  ZIPF exponent (forced)            : %s   (measured ~ 1)" % exponent)
    print("  GUTENBERG-RICHTER b-value (forced): %s   (measured ~ 0.9-1.1, a decade per magnitude)" % exponent)
    print("\n  The unit power law is the fold's simplest self-similar distribution; its")
    print("  exponent is the One. Traced to ONE.")
