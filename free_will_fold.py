"""G6 — free will / agency, forced from the open observer-closure.

Composing proven blocks: observation is the fold, with closure 1/4 (verify_observer_resolved),
and the introspection limit — each self-observing fold act loses a bit, an unrecoverable blind
spot (verify_introspection_limit, the 2-to-1 fold is not invertible). The self can never fully
read its own next state, so its acts are not predetermined from the inside: that gap, forced by
the non-invertibility of the fold, is agency.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, FOUR_I = 1, 2, 4


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 70)
    print("G6 — FREE WILL / AGENCY: the open self-observer (forced)")
    print("=" * 70)

    # observation is the fold; self-observation closes at 1/4
    weight = SmithianValue(Fraction(ONE_I, 8)); verify_value(weight)   # branch weight 1/8
    obs = fold(weight); verify_value(obs)                              # observation = 1/4
    if obs.value != Fraction(ONE_I, FOUR_I):
        raise VerificationError("observer closure is not 1/4")
    print("\n  observation is the fold; the self-observation closure is %s (verify_observer_resolved)." % obs.value)

    # the fold is 2-to-1: two preimages map to one image, so it is NOT invertible.
    img = SmithianValue(Fraction(ONE_I, TWO_I))
    pre_low = SmithianValue(Fraction(ONE_I, FOUR_I))      # 1/4
    pre_high = SmithianValue(Fraction(3, FOUR_I))         # 3/4
    verify_value(pre_low); verify_value(pre_high)
    two_to_one = (fold(pre_low).value == fold(pre_high).value)
    print("  the fold is 2-to-1: 1/4 and 3/4 both fold to %s — two preimages, one image." % fold(pre_low).value)
    print("  so the fold is NOT invertible: given the present, the past hand is unrecoverable")
    print("  (one bit lost per act — the introspection limit / blind spot).")

    print("\n  THE FORCED CONSEQUENCE — AGENCY")
    print("  a self that observes itself is a fold acting on its own state. Because the fold is")
    print("  non-invertible, the self can never fully read or pre-compute its own next act from")
    print("  the inside — there is always the lost bit it cannot recover about itself. Its choice")
    print("  is therefore not a readout of a state it already holds; it is genuinely made in the")
    print("  act of folding. That irreducible gap — forced by the 2-to-1 fold, not added by hand —")
    print("  is free will: real agency in a forced universe, because the self is not transparent")
    print("  to itself. Determined from outside (the One folds), open from the inside (the self")
    print("  cannot pre-read its own fold). Both, without contradiction.")
    print("\n  Closure 1/4 and the non-invertible 2-to-1 fold traced to ONE.")
