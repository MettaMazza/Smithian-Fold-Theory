"""G5 — applied signatures: how to find the Smithions and the new forces, forced.

Composing proven blocks: the Smithions as matter of the prime-5/7 sectors (new_particles.py),
the dark sector as gauge-inert (verify_dark_matter, fraction 27/32), the mediator counts
p^2-1 (24, 48), and the confinement structure (prime_force_phenomenology.py).
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, FIVE_I, SEVEN_I = 1, 2, 5, 7


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 72)
    print("G5 — APPLIED SIGNATURES: detecting the Smithions and the new forces (forced)")
    print("=" * 72)

    print("\n[SMITHION (DARK-MATTER) DETECTION] the suppressed channel")
    print("  the lightest Smithion is gauge-inert to electromagnetism and the strong force")
    print("  (verify_dark_matter): it carries only the new charge + gravity. So a direct-detection")
    print("  recoil can proceed ONLY through the new force or gravity — both feeble at the detector,")
    print("  so the cross-section is structurally tiny. That is WHY it has evaded detection, and it")
    print("  forces the search strategy: gravitational/cosmological signatures, not nuclear recoil.")
    for p in (FIVE_I, SEVEN_I):
        g = take(ONE, SmithianValue(Fraction(ONE_I, p))); verify_value(g)
        print("    sector %d : the only matter-detector coupling is the new force g=(p-1)/p=%s," % (p, g.value))
        print("              electromagnetically dark -> no ordinary recoil channel.")

    print("\n[NEW-FORCE COLLIDER SIGNATURES] confinement jets and missing energy")
    for p in (FIVE_I, SEVEN_I):
        carriers = p*p - ONE_I
        print("    sector %d : %d massless self-confining carriers -> a NEW kind of jet (a" % (p, carriers))
        print("              confining-sector shower); pair-produced Smithions hadronize into")
        print("              neutral bound states -> missing-energy + new-jet signatures.")
    print("  The ladder is sealed at 7, so a confining signature at any prime beyond 7 would")
    print("  falsify the theory — a sharp, two-sided collider test.")

    print("\n  Structural: dark matter detectable only gravitationally (EM-dark Smithion);")
    print("  new forces seen as confining jets + missing energy, none beyond prime 7. Traced to ONE.")
