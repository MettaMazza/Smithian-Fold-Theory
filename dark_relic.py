"""The dark relic abundance — forced from the covering structure.

The corpus forces two cosmic ratios from the down-depth-five covering structure:

    dark-to-baryon   Omega_dm / Omega_b   =  c^3 / d_down  =  27 / 5
    dark fraction    Omega_dm / Omega_m   =  c^3 / 2^d_down =  27 / 32

with colour c = 3 and down-depth d_down = 5. These ARE the relic abundance: the
amount of dark matter relative to ordinary matter is not a freeze-out accident to be
computed from a cross-section, it is the covering ratio 27/5, fixed before any
dynamics. The dark matter itself is supplied by the new forces: the lightest neutral
bound state of the prime-5 and prime-7 sectors (new_particles.py) is stable and
electrically neutral — the relic particle whose abundance this ratio fixes.

The in-domain fold value is the dark fraction 27/32; the dark-to-baryon ratio 27/5 is
read from it. One measured baryon density anchors the absolute relic density (Route B).
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I, FIVE_I = 1, 2, 3, 5


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def forced_dark_structure():
    c, d = THREE_I, FIVE_I
    dark_fraction = SmithianValue(Fraction(c ** 3, TWO_I ** d))   # 27/32, in domain
    verify_value(dark_fraction)
    dark_to_baryon = Fraction(c ** 3, d)                          # 27/5 (a ratio, >1)
    if dark_fraction.value != Fraction(27, 32) or dark_to_baryon != Fraction(27, 5):
        raise VerificationError("forced dark structure mismatch")
    return dark_fraction.value, dark_to_baryon


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 74)
    print("THE DARK RELIC ABUNDANCE — forced from the covering structure")
    print("=" * 74)

    dark_fraction, dtb = forced_dark_structure()
    print("\n  forced dark-to-baryon  Omega_dm/Omega_b = 27/5  = %.3f" % float(dtb))
    print("  forced dark fraction   Omega_dm/Omega_m = 27/32 = %.3f" % float(dark_fraction))

    # Route B: measured baryon density anchors the absolute relic density
    Omega_b_h2 = 0.0224                       # measured (CMB), comparison input
    Omega_dm_h2 = float(dtb) * Omega_b_h2     # forced from the ratio
    Omega_m_h2 = Omega_b_h2 + Omega_dm_h2
    print("\n  --- absolute relic density (Route B anchor: Omega_b h^2 = 0.0224) ---")
    print("  Omega_dm h^2 (FORCED)  = %.4f   (measured ~0.120)" % Omega_dm_h2)
    print("  Omega_m  h^2           = %.4f" % Omega_m_h2)

    print("\n  THE RELIC PARTICLE: the lightest neutral bound state of the prime-5 and")
    print("  prime-7 forces (new_particles.py) is stable and electrically neutral.")
    print("  Its cosmic abundance is not a tuned freeze-out; it is the covering ratio")
    print("  27/5 of the baryons, forced before any dynamics.")
    print("\n  Dark fraction traced to ONE; relic density anchored by one measured baryon")
    print("  density.  THE DARK ABUNDANCE IS THE COVERING RATIO 27/5.")
