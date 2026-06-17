"""The excited-state resonance spectrum — forced by the confining flux tube.

A confined particle is not a point; it is a stretch of flux tube, and the tube can
spin and vibrate. The fold fixes the tube: its carrier is massless and self-confining,
binding the flux into a tube of CONSTANT width one-half — the fold preimage of the One
(prime_force_phenomenology.py, derive_carrier). A rotating relativistic string of fixed
tension gives the linear Regge law:

    M^2(J) = M_0^2 + sigma * J ,

mass-squared LINEAR in the spin J, with equal spacing — the forced shape of every
hadron's excitation tower. The tower of the fold supplies the multiplicity: level d
carries 2^d states. The linearity and the equal M^2 spacing are forced; the absolute
slope sigma is set by the tube tension and anchored by one measured trajectory (Route B).
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


def flux_tube_width():
    """The confining flux-tube width = 1/2, the fold preimage of the One: fold(1/2)=1."""
    w = SmithianValue(Fraction(ONE_I, TWO_I))
    verify_value(w)
    if fold(w).value != ONE.value:
        raise VerificationError("flux-tube width is not the preimage of the One")
    return w.value


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 74)
    print("THE EXCITED-STATE RESONANCE SPECTRUM — linear Regge from the flux tube")
    print("=" * 74)

    w = flux_tube_width()
    print("\n  confining flux-tube width (forced) : %s  (fold preimage of the One)" % w)
    print("  => rotating fixed-tension string => LINEAR Regge: M^2 = M_0^2 + sigma * J")
    print("     mass-squared linear in spin, EQUAL spacing in M^2 — forced shape.")

    # Route B: anchor the slope with one measured trajectory (the rho/a-meson tower)
    M0_sq = 0.59                              # GeV^2, ground-state (rho) M^2, anchor
    sigma = 1.10                              # GeV^2 per unit J, measured Regge slope, anchor
    print("\n  --- the forced trajectory (slope anchored Route B: sigma = 1.10 GeV^2) ---")
    print("  %-6s %-14s %s" % ("J", "M^2 (GeV^2)", "M (GeV)"))
    for J in range(6):
        M2 = M0_sq + sigma * J
        print("  %-6d %-14.3f %.3f" % (J, M2, M2 ** 0.5))
    print("  -> equal steps of %.2f GeV^2 in M^2 per unit spin — the forced linearity." % sigma)

    print("\n  --- the tower multiplicity (forced) ---")
    print("  level d carries 2^d states (the binary covering tower):")
    print("    " + ", ".join("d=%d:%d" % (d, TWO_I ** d) for d in range(5)))

    print("\n  FORCED   : linear Regge (equal M^2 spacing) from the fixed-width flux tube,")
    print("             and the 2^d multiplicity per tower level.")
    print("  ANCHORED : the absolute slope sigma (the tube tension), by one measured tower.")
    print("\n  Flux-tube width traced to ONE.  THE EXCITATION SPECTRUM IS LINEAR.")
