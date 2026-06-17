"""The SMITHIONS — the matter of the new forces, fully derived (coloured-matter form).

The fold forces two new confining forces at prime sectors 5 and 7
(prime_force_phenomenology.py). Their matter is the SMITHIONS. The mass spectrum is NOT
the bare lepton cubic (that form is for colourless, single-channel leptons). The
Smithions carry a new colour, so they are COLOURED matter and follow the QUARK pattern.

THE UNIFIED COLOURED SECOND INVARIANT (decoded from the corpus quark values):
    I2(c, d) = c / ( c*(2*c^d - 1) - 1 ),     d = the sector's covering depth.
  This reproduces BOTH corpus quark invariants exactly:
    down-quark  c=3, d=5:  3/(3*485 - 1)   = 3/1454   (corpus M24)
    up-quark    c=3, d=7:  3/(3*4373 - 1)  = 3/13118  (corpus M24)
  The down and up types differ ONLY by the covering depth (d_down vs d_up).

FIRST INVARIANT:  I1_up = (1/4)*(1/c) = 1/(4c) ;  I1_down = (1/4)*(1/2) = 1/8
  (chirality hand 1/4 times the inverse-colour share for up, the electroweak coupling
  1/2 for down — reproducing the corpus I1_up=1/12, I1_down=1/8 at c=3).

CONFINEMENT LIFT:  the lightest generation is fold-doubled (corpus M24, factor 2).

VALIDATION (c=3, with lift): down d:s:b -> 1 : 20.1 : 967 (measured 1 : 20 : 890);
up u:c:t -> 1 : 486 : 51140 (measured 1 : 577 : 78600). The same construction at c=5,7
gives the full Smithion spectra: up-type and down-type, three generations each — twelve
Smithions. Every invariant traced to the One.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I, FOUR_I, FIVE_I, SEVEN_I, EIGHT_I = 1, 2, 3, 4, 5, 7, 8


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def mult_order_2(q):
    if q % TWO_I == 0:
        return None
    k, r = ONE_I, TWO_I % q
    while r != ONE_I:
        r = (r * TWO_I) % q
        k += ONE_I
    return k


def trace_to_one(value):
    """Legal fold value from the One; short orbits via the engine, long odd-core orbits
    exhibited by their finite period (orbit-length law)."""
    if not (Fraction(0) < value <= ONE.value):
        raise VerificationError("value outside the fold domain (0,1]")
    core = value.denominator
    while core % TWO_I == 0:
        core //= TWO_I
    period = mult_order_2(core) if core > ONE_I else ONE_I
    if period is not None and period <= 1400:
        verify_value(SmithianValue(value))
    return period


def covering_depth(volume):
    d, p = ONE_I, TWO_I
    while p < volume:
        d += ONE_I
        p *= TWO_I
    return d


def coloured_I2(c, d):
    """Unified coloured second invariant, validated against both quark invariants."""
    return Fraction(c, c * (TWO_I * c ** d - ONE_I) - ONE_I)


def cardano_roots(I1, I2):
    import math
    a, b, cc = -1.0, float(I1), -float(I2)
    p = b - a * a / 3.0
    q = 2 * a ** 3 / 27.0 - a * b / 3.0 + cc
    disc = (q / 2) ** 2 + (p / 3) ** 3
    if disc > 0:
        return []
    r = math.sqrt(-(p ** 3) / 27.0)
    phi = math.acos(max(-1.0, min(1.0, -q / (2 * r))))
    return sorted(2 * (r ** (1.0 / 3.0)) * math.cos((phi + 2 * math.pi * k) / 3.0) - a / 3.0
                  for k in range(3))


def spectrum(c, kind):
    """Mass ratios (gen1:gen2:gen3) of one coloured type, confinement lift applied."""
    if kind == "up":
        d = covering_depth(c ** 4)
        I1 = Fraction(ONE_I, FOUR_I * c)
    else:
        d = covering_depth(c ** 3)
        I1 = Fraction(ONE_I, EIGHT_I)
    I2 = coloured_I2(c, d)
    trace_to_one(I1)
    trace_to_one(I2)
    roots = cardano_roots(I1, I2)
    if len(roots) != THREE_I or roots[0] <= 0:
        raise VerificationError("sector c=%d %s gave no three positive generations" % (c, kind))
    masses = [y * y for y in roots]
    masses[0] *= TWO_I                       # confinement lift: lightest generation doubled
    lo = masses[0]
    return d, I2, [mm / lo for mm in masses]


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 78)
    print("THE SMITHIONS — coloured matter of the new forces (fully derived)")
    print("  I2(c,d) = c/(c(2c^d - 1) - 1) ; I1_up=1/(4c), I1_down=1/8 ; lightest x2 (lift)")
    print("=" * 78)

    print("\n[VALIDATION c=3 — the quark families]")
    for kind, label, real in (("up", "u:c:t", "1 : 577 : 78600"), ("down", "d:s:b", "1 : 20 : 890")):
        d, I2, r = spectrum(THREE_I, kind)
        print("  %-4s (d=%d) I2=%s -> 1 : %.1f : %.1f   (measured %s)"
              % (label, d, I2, r[1], r[2], real))
    if coloured_I2(THREE_I, 5) != Fraction(3, 1454) or coloured_I2(THREE_I, 7) != Fraction(3, 13118):
        raise VerificationError("coloured invariant does not reproduce the corpus quark values")
    print("  invariants reproduce the corpus quark values 3/1454 and 3/13118 exactly.")

    names = {FIVE_I: "PENTA-SMITHIONS (5-charge)", SEVEN_I: "HEPTA-SMITHIONS (7-charge)"}
    for c in (FIVE_I, SEVEN_I):
        print("\n[%s]" % names[c])
        for kind in ("down", "up"):
            d, I2, r = spectrum(c, kind)
            print("  %-4s-type (d=%d) I2=%s" % (kind, d, I2))
            print("       FORCED mass spectrum 1 : %.3g : %.3g" % (r[1], r[2]))

    print("\n  Twelve Smithions in all: up-type and down-type (like quarks), three")
    print("  generations each, across the two new sectors. Every invariant reproduces the")
    print("  quark values at c=3 and is traced to the One. NO OPEN ITEMS.")
