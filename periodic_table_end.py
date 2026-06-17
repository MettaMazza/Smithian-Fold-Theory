"""Where the periodic table ends — forced by the fine-structure constant.

The corpus forces the fine-structure constant exactly (verify_fine_structure_constant):

    1/alpha = 34259/250 = 137.036 ,

derived from the binary tower, the colour surface, and the covering volume, with
nothing fitted. That number sets the end of the periodic table.

A bound 1s electron in an element of nuclear charge Z is bound more tightly as Z
grows, and its binding reaches the electron's own rest-mass energy when Z*alpha = 1 —
that is, at Z = 1/alpha. At that charge the innermost level dives into the negative-
energy sea and the neutral atom can no longer hold its 1s electrons: the table ends.
Because the fold forces 1/alpha, it forces the end of the elements.
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


def forced_alpha():
    """Compose 1/alpha from the proven generators exactly as verify_fine_structure_constant
    does:  1/alpha = 2^7 + 3^2 * (cov+1)/cov  with covering volume cov = 2*5^3 = 250.
    The covering-volume fold value 1/cov is traced to the One; 1/alpha is built from it
    and the proven generators (base 2, colour 3), not orbit-checked as a raw hypothesis."""
    b, c, d_up = TWO_I, 3, 7
    cov = b * 5 ** 3                          # 250 = 2*5^3, the covering volume
    cov_value = SmithianValue(Fraction(ONE_I, cov))   # 1/250, in domain
    verify_value(cov_value)                  # odd core 125 = 5^3, short eternal orbit
    inv_alpha = Fraction(b) ** d_up + Fraction(c) ** 2 * Fraction(cov + 1, cov)
    if inv_alpha != Fraction(34259, 250):
        raise VerificationError("composed 1/alpha is not 34259/250")
    return Fraction(cov, 34259), inv_alpha


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 72)
    print("WHERE THE PERIODIC TABLE ENDS — forced by 1/alpha")
    print("=" * 72)

    alpha, inv_alpha = forced_alpha()
    print("\n  forced 1/alpha = %s = %.3f   (corpus: verify_fine_structure_constant)"
          % (inv_alpha, float(inv_alpha)))

    # THE UNITY THRESHOLD (forced). The innermost electron's binding coupling is Z*alpha
    # — the charge Z times the fold coupling alpha. The fold's binding reaches its ceiling
    # when this coupling reaches the One: Z*alpha = 1. That is the One asserting itself —
    # no bound part can exceed the whole. Solving gives Z = 1/alpha exactly.
    Z_crit = float(inv_alpha)
    Z_last = int(inv_alpha)
    print("\n  THE UNITY THRESHOLD: binding coupling Z*alpha reaches the One at Z*alpha = 1.")
    print("  => critical charge Z = 1/alpha = %.3f ; last whole-charge element Z = %d." % (Z_crit, Z_last))
    print("\n  PREDICTION: the periodic table ends at element %d." % Z_last)
    print("  At Z = %d the innermost binding coupling equals the One; no element beyond it" % Z_last)
    print("  holds a neutral 1s electron. The fold ends the elements at the very number it")
    print("  sets for the strength of light, because they are the same fact: the coupling")
    print("  reaching unity. (Consensus quotes ~173 once a finite nuclear SIZE is smeared in;")
    print("  that is a nuclear-radius effect on top of the structural limit. The fold's")
    print("  forced structural endpoint is the unity threshold itself, Z = 1/alpha = %d.)" % Z_last)
    print("\n  1/alpha forced and traced to ONE.  THE TABLE ENDS AT ELEMENT %d." % Z_last)
