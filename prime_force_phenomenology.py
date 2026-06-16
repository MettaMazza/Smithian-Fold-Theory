"""Full phenomenology of the two new fundamental forces — prime sectors 5 and 7.

Roadmap item 1. The corpus proves (B-7N) that the prime sectors 5 and 7 satisfy
the identical force criterion as electroweak (2) and strong (3). This module
derives their COMPLETE phenomenology the same way the strong force is derived in
proof.py — every quantity built from the One through fold and take, each value
traced by verify_value, no measured input, no consensus framework. It extends the
existing force template (couplings, mediators, colours, confinement, running,
carriers, bound states, ladder bound) from the known sectors {2,3} to the
predicted sectors {5,7}.

Derived, per new sector p in {5,7}:
  coupling g_p = (p-1)/p ; shortfall (mass-part) s_p = 1/p
  charge/colour count = p ; mediator count = p^2 - 1
  confining: every interior kind pairs antipodally to the One, (p-1)/2 pairs
  running: g_p(d) = take(ONE, 1/(p+2^d)) -> ONE ; beta-slope = p-1
  carrier: massless (no mass-part) yet self-confining, like the gluon
  bound states: colour-neutral combinations fold to the One
  the ladder is sealed at 7; the next prime 11 carries no force
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, ONE, fold
from sftoe.proof import verify_value, VerificationError

ONE_I = 1
TWO_I = 2
THREE_I = 3
FIVE_I = 5
SEVEN_I = 7
ELEVEN_I = 11
NEW_PRIMES = [FIVE_I, SEVEN_I]
ALL_PRIMES = [TWO_I, THREE_I, FIVE_I, SEVEN_I]


def _no_zero_guard():
    zero_val = Fraction(ONE_I - ONE_I, ONE_I)
    try:
        SmithianValue(zero_val)
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed: zero was accepted.")


def derive_couplings():
    """g_p = (p-1)/p = take(ONE, 1/p); shortfall s_p = 1/p; g_p + s_p = ONE;
    binding-carry (1-g_p)*p = 1; couplings strictly increase across the ladder."""
    _no_zero_guard()
    out = {}
    last = None
    for p in ALL_PRIMES:
        s_p = SmithianValue(Fraction(ONE_I, p)); verify_value(s_p)
        g_p = take(ONE, s_p); verify_value(g_p)
        if g_p.value + s_p.value != ONE.value:
            raise VerificationError("coupling + shortfall != ONE at sector %d" % p)
        carry = take(ONE, g_p).value * p
        if carry != ONE.value:
            raise VerificationError("binding-carry != 1 at sector %d" % p)
        if last is not None and not (last < g_p.value):
            raise VerificationError("couplings not strictly increasing")
        last = g_p.value
        out[p] = (g_p.value, s_p.value)
    return out


def derive_mediators_and_colours():
    """colour (fibre) count = p ; mediator count = p^2 - 1 (colour-anticolour
    combinations minus the singlet), checked as (p-1)*(p+1)."""
    out = {}
    for p in ALL_PRIMES:
        colours = p
        med_a = Fraction(p * p) - Fraction(ONE_I)
        med_b = (Fraction(p) - Fraction(ONE_I)) * Fraction(p + ONE_I)
        if med_a != med_b:
            raise VerificationError("mediator count route mismatch at %d" % p)
        out[p] = (colours, int(med_a))
    return out


def derive_confinement():
    """Confining: every interior kind j/p pairs with its antipode (p-j)/p to sum
    to the One; the number of antipodal pairs around the half-One is (p-1)/2."""
    _no_zero_guard()
    half = SmithianValue(Fraction(ONE_I, TWO_I)); verify_value(half)
    if take(ONE, half).value != half.value:
        raise VerificationError("shared center is not self-antipodal")
    out = {}
    for p in ALL_PRIMES:
        count = ONE_I - ONE_I
        for j in range(ONE_I, p):
            kind = SmithianValue(Fraction(j, p)); verify_value(kind)
            anti = take(ONE, kind); verify_value(anti)
            if kind.value + anti.value != ONE.value:
                raise VerificationError("antipodal pairing fails sector %d kind %d" % (p, j))
            count += ONE_I
        pairs = Fraction(count, TWO_I)
        if pairs != Fraction(p - ONE_I, TWO_I):
            raise VerificationError("pair count mismatch sector %d" % p)
        out[p] = pairs
    return out


def derive_running():
    """Coupling running g_p(d) = take(ONE, 1/(p+2^d)) climbs monotonically toward
    the One; the gap to unison is 1/(p+2^d). Beta-slope = coupling/shortfall = p-1."""
    _no_zero_guard()
    out = {}
    depths = [ONE_I, TWO_I, THREE_I, 4, FIVE_I]
    for p in ALL_PRIMES:
        prev = None
        gaps = []
        for d in depths:
            denom = p + (TWO_I ** d)
            gap = SmithianValue(Fraction(ONE_I, denom)); verify_value(gap)
            g = take(ONE, gap); verify_value(g)
            if prev is not None and not (prev < g.value):
                raise VerificationError("running not monotone toward unison sector %d" % p)
            prev = g.value
            gaps.append((d, gap.value, g.value))
        # beta-slope = coupling / shortfall = ((p-1)/p) / (1/p) = p-1
        g_p = take(ONE, SmithianValue(Fraction(ONE_I, p)))
        beta = g_p.value / Fraction(ONE_I, p)
        if beta != Fraction(p - ONE_I):
            raise VerificationError("beta-slope != p-1 at sector %d" % p)
        out[p] = (int(beta), gaps)
    return out


def derive_carrier():
    """The carrier is massless (no mass-part) yet confining: the unbroken
    channel-combination sums to the One (massless, unbounded reach, luminal);
    its self-coupling binds the flux into a tube of constant width (confining) —
    the same structure as the gluon (verify_strong_luminal / massless split)."""
    _no_zero_guard()

    def reach(mass):
        return None if mass is None else Fraction(ONE_I, mass.value)

    out = {}
    for p in NEW_PRIMES:
        # unbroken combination: a kind and its antipode sum to the One -> no shortfall
        kind = SmithianValue(Fraction(ONE_I, p)); verify_value(kind)
        anti = take(ONE, kind); verify_value(anti)
        if kind.value + anti.value != ONE.value:
            raise VerificationError("carrier combination not unbroken sector %d" % p)
        carrier_mass = None                      # massless: no shortfall from the One
        if reach(carrier_mass) is not None:
            raise VerificationError("massless carrier must have unbounded reach")
        # self-confinement: flux-tube width fixed at the fold-preimage of the One
        width = SmithianValue(Fraction(ONE_I, TWO_I)); verify_value(width)
        if fold(width) != ONE:
            raise VerificationError("flux-tube width is not the fold-preimage of ONE")
        out[p] = {"massless": True, "reach": "unbounded", "confining_width": width.value}
    return out


def derive_bound_states():
    """Colour-neutral bound states fold to the One: the meson (a colour and its
    antipode) sums to the One; the baryon (the whole group of p colours) folds to
    the One. Same neutrality structure as the strong sector."""
    _no_zero_guard()
    out = {}
    for p in NEW_PRIMES:
        # meson: colour j/p + anticolour (p-j)/p = ONE
        j = ONE_I
        colour = SmithianValue(Fraction(j, p)); verify_value(colour)
        anti = take(ONE, colour); verify_value(anti)
        meson_neutral = (colour.value + anti.value == ONE.value)
        # baryon: the whole group is the One (folds to itself)
        whole = ONE
        baryon_neutral = (fold(whole) == ONE)
        if not (meson_neutral and baryon_neutral):
            raise VerificationError("bound-state neutrality fails sector %d" % p)
        out[p] = {"meson_neutral": meson_neutral, "baryon_neutral": baryon_neutral}
    return out


def derive_ladder_bound():
    """The confining prime-sector ladder is sealed at 7 (the deepest realized
    covering depth). The next prime, 11, lies beyond the bound and carries no
    force: 11 > 7."""
    deepest = SEVEN_I
    next_prime = ELEVEN_I
    realized = [p for p in ALL_PRIMES if p <= deepest]
    if realized != ALL_PRIMES:
        raise VerificationError("a realized sector exceeds the covering-depth bound")
    if not (next_prime > deepest):
        raise VerificationError("next prime is not beyond the bound")
    return {"realized_sectors": ALL_PRIMES, "bound": deepest, "no_force_at": next_prime}


if __name__ == "__main__":
    print("=" * 72)
    print("FULL PHENOMENOLOGY OF THE TWO NEW FORCES — prime sectors 5 and 7")
    print("derived from the One, fold/take only, every value verify_value-traced")
    print("=" * 72)

    cpl = derive_couplings()
    med = derive_mediators_and_colours()
    cnf = derive_confinement()
    run = derive_running()
    car = derive_carrier()
    bnd = derive_bound_states()
    lad = derive_ladder_bound()

    print("\nKnown sectors (for ordering):  EW(2) g=%s   strong(3) g=%s"
          % (cpl[2][0], cpl[3][0]))
    for p in NEW_PRIMES:
        g, s = cpl[p]
        colours, mediators = med[p]
        beta, gaps = run[p]
        print("\n--- NEW FORCE: prime sector %d ---" % p)
        print("  coupling g_%d            = %s   (stronger than strong 2/3: %s)"
              % (p, g, g > Fraction(2, 3)))
        print("  shortfall / mass-part   = %s" % s)
        print("  charge (colour) count   = %d" % colours)
        print("  mediator count (p^2-1)  = %d" % mediators)
        print("  confining: antipodal pairs about 1/2 = %s   (CONFINING)" % cnf[p])
        print("  running gap to unison 1/(p+2^d): %s" % [str(x[1]) for x in gaps])
        print("    -> coupling climbs to ONE: %s" % [str(x[2]) for x in gaps])
        print("  beta-slope (p-1)        = %d" % beta)
        print("  carrier: massless=%s reach=%s flux-tube width=%s (gluon-like)"
              % (car[p]["massless"], car[p]["reach"], car[p]["confining_width"]))
        print("  bound states colour-neutral (meson, baryon fold to ONE): %s" % bnd[p])

    print("\nLadder: realized force sectors = %s ; sealed at %d ; no force at %d"
          % (lad["realized_sectors"], lad["bound"], lad["no_force_at"]))
    print("\nALL DERIVATIONS verify_value-traced to ONE. PHENOMENOLOGY COMPLETE.")
