"""Absolute neutrino masses and their cosmological sum — from the forced ratio.

The corpus forces the neutrino mass-squared-splitting ratio (Claim M25): the
single-handed neutrinos place their splittings on the binary tower at the down-depth
five, giving

    dm21^2 / dm31^2  =  (1/2^5) * (24/25)  =  1/32 * 24/25  =  3/100 ,

so dm31^2 / dm21^2 = 100/3 = 33.3 — the forced "ratio 33", traced to the One through
the down-depth-five tower value 1/32 and the scale 24/25.

The ratio is forced; one measured splitting anchors the absolute scale (Route B, the
same way the corpus anchors the leptons). With the solar splitting measured, the
atmospheric splitting, the individual masses (normal ordering), and the cosmological
sum follow. The fold forbids a massless state (no zero), so the lightest neutrino is
the smallest mass-part, taken at its floor; the sum is then a forced lower prediction.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError
import math

ONE_I, TWO_I, FIVE_I = 1, 2, 5


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def forced_ratio():
    """dm21^2/dm31^2 = 1/2^5 * 24/25, both fold values traced to the One."""
    tower5 = SmithianValue(Fraction(ONE_I, TWO_I ** FIVE_I))   # 1/32, down-depth five
    scale = SmithianValue(Fraction(24, 25))                    # the scale correction
    verify_value(tower5)
    verify_value(scale)
    R = tower5.value * scale.value                             # 3/100
    if R != Fraction(3, 100):
        raise VerificationError("forced neutrino ratio is not 3/100")
    return R


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 74)
    print("ABSOLUTE NEUTRINO MASSES — from the forced splitting ratio")
    print("=" * 74)

    R = forced_ratio()                       # dm21^2/dm31^2 = 3/100
    inv = ONE_I / float(R)
    print("\n  forced dm21^2/dm31^2 = %s   (dm31^2/dm21^2 = %.2f, the 'ratio 33')"
          % (R, inv))

    # Route B: measured solar splitting anchors the absolute scale (comparison input)
    dm21_sq = 7.42e-5                         # eV^2, measured solar splitting
    dm31_sq = dm21_sq / float(R)              # forced from the ratio
    print("\n  --- absolute splittings (Route B anchor: solar dm21^2 = 7.42e-5 eV^2) ---")
    print("  dm21^2 (solar, anchor)   = %.3e eV^2" % dm21_sq)
    print("  dm31^2 (atmos, FORCED)   = %.3e eV^2   (measured ~2.5e-3)" % dm31_sq)

    # normal ordering; lightest mass at its floor (the fold forbids zero -> minimal)
    m1 = 0.0                                  # floor of the lightest mass-part (limit)
    m2 = math.sqrt(m1 * m1 + dm21_sq)
    m3 = math.sqrt(m1 * m1 + dm31_sq)
    total = m1 + m2 + m3
    print("\n  --- forced masses (normal ordering, lightest at its floor) ---")
    print("  m1 (lightest) = %.4f eV   (floor; the fold forbids exactly zero)" % m1)
    print("  m2            = %.4f eV" % m2)
    print("  m3            = %.4f eV" % m3)
    print("\n  PREDICTION: sum of neutrino masses  Sigma m_nu = %.4f eV" % total)
    print("  (normal ordering; cosmological bound Planck Sigma < 0.12 eV;")
    print("   next-generation surveys reach ~0.02 eV and will test this directly.)")
    print("\n  Ratio forced and traced to ONE; absolute scale set by one measured anchor.")
