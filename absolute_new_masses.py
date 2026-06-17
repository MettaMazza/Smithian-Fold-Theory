"""Absolute scale of the new particles — what the fold forces, stated exactly.

The Smithions (new_particles.py) are coloured matter; the coloured sharpened cubic forces
their mass RATIOS (up-type and down-type, three generations each), validated by reproducing
the quark families at colour 3. Those ratios are forced and traced to the One.

The ABSOLUTE scale (the lightest member's mass) is a separate quantity. Reading the engine
firsthand — the running g_p(d) = 1 - 1/(p+2^d), the coupling convergence (verify_coupling_
convergence), and the Planck hierarchy 2^(127/2) at the strong depth 7 — there is NO forced
per-sector confinement-scale rule: the Planck hierarchy is specific to the strong sector and
generalizes to absurd sub-eV scales at the new sectors' depths, and the fold's coupling runs
UP toward the UV, so "stronger coupling => heavier" is not a forced implication. Like the
quark sector, the overall scale would need one measured member as the anchor. So the absolute
scale is not determined by the present structure, and this module does not fabricate one — it
reports the forced ratios and states the scale honestly as anchor-dependent. (Earlier claims
that the Smithions are "heavy, above the strong scale" were an unforced assertion and are
withdrawn.)
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError
from new_particles import spectrum, FIVE_I, SEVEN_I

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
    print("=" * 78)
    print("ABSOLUTE SCALE OF THE NEW PARTICLES — the forced ratios; the scale is anchor-set")
    print("=" * 78)

    names = {FIVE_I: "PENTA-SMITHIONS (5-charge force)", SEVEN_I: "HEPTA-SMITHIONS (7-charge force)"}
    for m in (FIVE_I, SEVEN_I):
        coupling = Fraction(m - ONE_I, m)
        beta = m - ONE_I
        print("\n[%s]" % names[m])
        print("  coupling (p-1)/p = %s ; beta-slope = %d   (both forced from the prime sector)"
              % (coupling, beta))
        for kind in ("down", "up"):
            _d, _I2, r = spectrum(m, kind)   # coloured cubic + confinement lift
            print("  %s-type FORCED mass RATIOS (lightest = 1):  1 : %.4g : %.4g"
                  % (kind, r[1], r[2]))

    print("\n--- WHAT IS FORCED, AND WHAT IS ANCHOR-DEPENDENT ---")
    print("  FORCED   : all twelve Smithion mass RATIOS (up- and down-type, coloured cubic +")
    print("             confinement lift), validated against the quark families at colour 3;")
    print("             the charges (5, 7), couplings (4/5, 6/7), and mediators (24, 48).")
    print("  ANCHOR   : the absolute scale (the lightest member's mass) is set by one measured")
    print("             member of the sector, exactly as the electron anchors the leptons.")
    print("             It is NOT determined by the present structure (no forced per-sector")
    print("             confinement-scale rule), and is not fabricated here.")
    print("  WITHDRAWN: the earlier 'heavy, above the strong scale' claim — unforced.")
    print("\n  Ratios traced to ONE; the absolute scale awaits a measured member or a forced")
    print("  per-sector scale principle (not yet in the engine).")
