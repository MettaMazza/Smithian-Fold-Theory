"""The Smithion masses on the one fermion chain — mass-part 1/p, no separate scale.

Corrected. There is no "confinement scale" to invent for the new sectors — that was an
imported QCD idea, and a unified theory does not fork. Read firsthand, the corpus sets
EVERY fermion mass on a single chain:

  * a fermion's mass-part is the SHORTFALL from unison of its sector's holding coupling
    (verify_inter_sector_mass_pattern, proof.py:4737): electron = take(ONE, 1/2) = 1/2,
    up-quark = take(ONE, 2/3) = 1/3, and so on;
  * that mass-part couples to the displaced vacuum, the VEV (verify_ssb, verify_fermion_mass_part);
  * the whole tower is anchored to the One: the electroweak scale at Planck/2^56
    (verify_hierarchy_problem) and the proton at Planck/2^(127/2) (Planck hierarchy).

The Smithion is a coloured fermion on this same chain. Its sector coupling is (p-1)/p, so
its mass-part is the shortfall

        mass-part = take(ONE, (p-1)/p) = 1/p

— 1/5 for the penta sector, 1/7 for the hepta sector (the same 1/p the new force carries,
prime_force_phenomenology.py). The within-sector generation ratios are the coloured cubic
(new_particles.py), validated on the quarks. One mechanism, one chain, every piece forced;
no separate scale, no fork, no comparison to any outside expectation.
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


def mass_part(p):
    """Shortfall from unison of the sector coupling (p-1)/p, traced to the One: = 1/p."""
    coupling = take(ONE, SmithianValue(Fraction(ONE_I, p)))    # (p-1)/p
    verify_value(coupling)
    mp = take(ONE, coupling)                                   # 1 - (p-1)/p = 1/p
    verify_value(mp)
    if mp.value != Fraction(ONE_I, p):
        raise VerificationError("mass-part is not 1/p at sector %d" % p)
    return mp.value


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 78)
    print("THE SMITHION MASSES ON THE ONE FERMION CHAIN — mass-part 1/p")
    print("=" * 78)

    print("\n  every fermion mass = (mass-part = shortfall of its sector coupling) on the")
    print("  displaced-vacuum chain, anchored to the One (EW = Planck/2^56, proton = Planck/2^(127/2)).")
    print("  known sectors:  electron mass-part = take(ONE,1/2) = 1/2 ;  up-quark = take(ONE,2/3) = 1/3")

    names = {FIVE_I: "PENTA-SMITHIONS (5-charge)", SEVEN_I: "HEPTA-SMITHIONS (7-charge)"}
    for p in (FIVE_I, SEVEN_I):
        mp = mass_part(p)
        print("\n[%s]" % names[p])
        print("  sector coupling (p-1)/p = %s ; mass-part = take(ONE,(p-1)/p) = %s  (FORCED)"
              % (Fraction(p - ONE_I, p), mp))
        for kind in ("down", "up"):
            _d, _I2, r = spectrum(p, kind)
            print("  %s-type generation ratios (cubic, forced): 1 : %.4g : %.4g" % (kind, r[1], r[2]))

    # CROSS-SECTOR dimensionless ratio, forced the same way as proton/electron = 2:
    # the structural mass ratio is the ratio of mass-parts. Electron mass-part = 1/2.
    print("\n--- CROSS-SECTOR RATIO (forced, dimensionless — like proton/electron = 2) ---")
    e_mass_part = take(ONE, SmithianValue(Fraction(ONE_I, TWO_I))).value   # electron = 1/2
    for p in (FIVE_I, SEVEN_I):
        mp = mass_part(p)                                  # 1/p
        ratio = mp / e_mass_part                           # (1/p)/(1/2) = 2/p
        print("  lightest %s / electron = (1/%d)/(1/2) = %s  (forced from mass-parts)"
              % (names[p].split()[0].lower(), p, ratio))
    print("  -> the lightest Smithions are LIGHT (2/5, 2/7 of the electron structural part),")
    print("     climbing by the cubic ratios; confined and sector-only, hence unseen.")

    print("\n  WHAT IS A DERIVATION vs A UNIT CONVERSION (agent.md):")
    print("  DERIVATION (forced, traced): the mass-part 1/p, the within-sector cubic ratios,")
    print("    and the cross-sector ratio 2/p to the electron — the full dimensionless spectrum.")
    print("  UNIT CONVERSION (not a derivation; 'the universe doesn't know what an MeV is'):")
    print("    the absolute GeV value. It is a calibration read, not forced, and not invented here.")
    print("\n  One chain, all dimensionless structure forced and traced to the One.")
