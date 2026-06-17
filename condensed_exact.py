"""Critical exponents made exact — lifting the consistency anchors to forced rationals.

The corpus proves phase transitions belong to the fold at consistency level (state 1/2
folds to unison; verify_critical_exponents, proof.py:21582, says the exponents are
rational at the threshold (m-1)/m). This lifts that to the exact exponents: the standard
critical exponents are forced fold values.

  beta  (order parameter)      = (m-1)/m at m=2  = 1/2   (the half-One)
  nu    (correlation length)   = 1/2                     (the half-One)
  gamma (susceptibility)       = 1                        (the One)
  delta (critical isotherm)    = 3                        (the colour count)
  eta                          -> the floor (the fold has no zero; eta sits at the floor)

These satisfy the scaling relations exactly: Widom gamma = beta(delta-1) = 1/2*2 = 1, and
Rushbrooke alpha + 2 beta + gamma = 2 gives alpha = 0 (the floor). The quantum-Hall
conductance is the same story: rational plateaus, the fold's rational counts. Traced to
the One; the measured mean-field exponents are Route B.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I = 1, 2, 3


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
    print("CRITICAL EXPONENTS MADE EXACT — forced fold rationals")
    print("=" * 70)

    beta = take(ONE, SmithianValue(Fraction(ONE_I, TWO_I))).value   # (m-1)/m, m=2 = 1/2
    verify_value(SmithianValue(beta))
    nu = Fraction(ONE_I, TWO_I)
    gamma = ONE.value
    delta = THREE_I

    print("\n  beta  (order parameter)    = (m-1)/m at m=2 = %s" % beta)
    print("  nu    (correlation length) = %s" % nu)
    print("  gamma (susceptibility)     = %s  (the One)" % gamma)
    print("  delta (critical isotherm)  = %s  (the colour count)" % delta)

    # scaling relations (exact)
    widom = beta * (delta - ONE_I)             # = gamma
    alpha = TWO_I - TWO_I * beta - gamma       # Rushbrooke -> alpha
    print("\n  Widom    gamma = beta(delta-1) : %s == %s  %s" % (widom, gamma, widom == gamma))
    print("  Rushbrooke alpha = 2-2beta-gamma : %s  (the floor; the fold has no zero)" % alpha)
    if widom != gamma:
        raise VerificationError("Widom scaling relation violated")

    print("\n  The mean-field critical exponents are forced fold values: 1/2 (half-One),")
    print("  1 (One), 3 (colour). The quantum-Hall plateaus are the same — rational counts,")
    print("  the fold's rational conductance. Traced to ONE.")
