"""Absolute scale of the new particles — what the fold forces, and what it does not.

The Smithions (new_particles.py) are coloured matter; their forced (down-type) mass
ratios come from the neutral-channel sharpened cubic, validated against the down-quark.
An absolute mass needs one more thing: the sector's overall scale. For the leptons that
scale is anchored by the measured electron; the new sectors have no measured member yet,
so their absolute scale is set by their CONFINEMENT scale, which the fold places — forced
— above the strong scale:

  * couplings (p-1)/p = 4/5, 6/7  exceed the strong sector's 2/3,
  * running beta-slopes p-1 = 4, 6  exceed the strong sector's 2,

so both new forces reach binding strength at HIGHER energy than the strong force. Their
lightest matter therefore sits above the strong (proton) scale, and the heavier
generations climb by the forced ratios. This module states exactly that: the ratios
(forced), the ordering (forced, above the strong scale), and the lower bound — and it
does NOT invent a central GeV value the fold does not force.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError
from new_particles import spectrum, FIVE_I, SEVEN_I

ONE_I, TWO_I, THREE_I = 1, 2, 3
PROTON_GEV = 0.938                            # the strong-sector scale (Route B anchor)


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
    print("ABSOLUTE SCALE OF THE NEW PARTICLES — forced ratios, forced ordering")
    print("=" * 78)

    names = {FIVE_I: "PENTA-SMITHIONS (5-charge force)", SEVEN_I: "HEPTA-SMITHIONS (7-charge force)"}
    for m in (FIVE_I, SEVEN_I):
        coupling = Fraction(m - ONE_I, m)
        beta = m - ONE_I
        print("\n[%s]" % names[m])
        print("  coupling (p-1)/p = %s  > strong 2/3 ;  beta-slope = %d > strong 2"
              % (coupling, beta))
        print("  => confines ABOVE the strong scale: lightest member heavier than the proton")
        for kind in ("down", "up"):
            _d, _I2, r = spectrum(m, kind)   # full coloured spectrum, confinement lift applied
            print("  %s-type FORCED mass ladder, lightest at the strong-scale lower bound"
                  " (>= %.3f GeV):" % (kind, PROTON_GEV))
            for gi, ratio in enumerate(r, start=1):
                lo = ratio * PROTON_GEV
                print("    generation %d :  mass = %.4g x m_low   (>= %.4g GeV)" % (gi, ratio, lo))

    print("\n--- WHAT IS FORCED, AND WHAT IS ANCHORED ---")
    print("  FORCED   : all twelve Smithion mass RATIOS (up-type and down-type, coloured")
    print("             cubic + confinement lift, validated against the quark families at")
    print("             c=3), and that both sectors confine ABOVE the strong scale (heavy).")
    print("  ANCHORED : a single absolute number needs one measured member of the sector,")
    print("             as the electron anchors the leptons — none measured yet, so the")
    print("             prediction is the ratio-ladder above a forced lower bound.")
    print("\n  Ratios traced to ONE; ordering forced by the couplings and beta-slopes.")
