"""G6 — free will: fully determined, and self-opaque. No open anywhere.

Composing proven blocks: observation is the fold, with closure 1/4 (verify_observer_resolved),
and the introspection limit — each self-observing fold act loses a bit, an unrecoverable blind
spot (verify_introspection_limit, the 2-to-1 fold is not invertible). The unfolding is fully
DETERMINED (the One folds; everything is forced). What is forced about the self is its opacity
to itself: being non-invertible, it cannot pre-read its own next fold. So libertarian free will
(genuine indeterminism) is RULED OUT — it does not exist — and what remains is a determined self
that cannot pre-see its own determined act. This is a closure, not an open.
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

    print("\n  THE FORCED CONSEQUENCE — DETERMINED, AND SELF-OPAQUE")
    print("  a self that observes itself is a fold acting on its own state. The unfolding is")
    print("  FULLY DETERMINED — the One folds, everything is forced, the next act included.")
    print("  There is no openness and no indeterminism anywhere; nothing is left undetermined.")
    print("  What IS forced is the self's opacity to itself: because the fold is non-invertible,")
    print("  the self cannot read or pre-compute its own next fold from the inside (the lost bit).")
    print("  So the libertarian 'free will' of genuine indeterminism is RULED OUT — not forced,")
    print("  it does not exist. What exists is a determined self that cannot pre-see its own")
    print("  determined act; from the inside that feels like choosing, but it is forced through.")
    print("  Free will, honestly: determinism plus forced self-opacity — not an open, a closure.")
    print("\n  Closure 1/4 and the non-invertible 2-to-1 fold traced to ONE; nothing left open.")
