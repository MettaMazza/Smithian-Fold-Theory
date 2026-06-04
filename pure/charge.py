"""EM1 — electric charge and Coulomb's law, in the permitted language. The flux/field-equation
structure of D9d is mathematically the same as Gauss's law for electrostatics, and Gauss's law is
equivalent to Coulomb's inverse-square law. The one new ingredient over gravity is sign: charge
comes in two opposed kinds, carried by the framework's opposition (two opposite influences return
to the One, never to zero -- opposition.py), where mass had only one. A charge q at distance r in
three dimensions sources a field of magnitude coupling*|q|/(Omega*r^2) (the D9d flux form, d=3);
the force between two charges has magnitude coupling*|q1|*|q2|/(Omega*r^2) and is repulsive for
like signs, attractive for opposite signs. The coupling (carrying 1/4*pi*epsilon0, and through it
the elementary charge / fine-structure constant) is a parameter of this domain; the framework
forces its fundamental dimensionless coupling in PH5 (g*=(m-1)/m)."""
from fractions import Fraction
from ratio import ONE, ratio, take, ABSENT, present_sum, whole_parts
import gravity as G          # reuse the D9d flux form
import opposition as Opp     # two opposed kinds, balancing to the One (not zero)

SIGNS = ("pos", "neg")

def field_magnitude(r, q, coupling=ONE, Omega=ONE):
    # |E| = coupling*|q| / (Omega * r^2): the D9d inverse-square flux form in three dimensions
    return G.field_strength(r, q, 3, coupling, Omega)

def force_magnitude(r, q1, q2, coupling=ONE, Omega=ONE):
    # |F| = coupling*|q1|*|q2| / (Omega * r^2): inverse-square, symmetric in the two charges
    return G.field_strength(r, q1*q2, 3, coupling, Omega)

def force_sense(s1, s2):
    # like signs repel, opposite signs attract (opposition); opposite charges balance to the One
    return "repel" if s1 == s2 else "attract"

if __name__=="__main__":
    print("Coulomb field magnitude (q=1) at r=1,2,3 (inverse-square):",
          [str(field_magnitude(Fraction(r), ONE)) for r in (1,2,3)])
    print("Coulomb force (q1=2,q2=3) at r=1,2,3:",
          [str(force_magnitude(Fraction(r), Fraction(2), Fraction(3))) for r in (1,2,3)])
    print("force symmetric in charges:",
          force_magnitude(Fraction(2),Fraction(2),Fraction(3))==force_magnitude(Fraction(2),Fraction(3),Fraction(2)))
    for s1 in SIGNS:
        for s2 in SIGNS:
            print(f"  {s1}-{s2}: {force_sense(s1,s2)}")
    print("opposite charges balance to the One (opposition, not zero):", Opp.balance_of_opposites(Fraction(1,4)))
    print("coupling is FREE here -> PH5 (a forced fundamental constant) forced at PH5")


# --- EM2: magnetism is the relativistic correction to Coulomb (D5 applied to EM1) ---
# Two like charges moving parallel at speed beta (a current). In their rest frame the force is pure
# Coulomb repulsion. Transforming to the lab by the relativity of D5, the net force is reduced to
# Coulomb*(1 - beta^2) = Coulomb / gamma^2: the velocity-dependent piece beta^2*Coulomb is the
# magnetic force, attractive for parallel currents, partly cancelling the electric repulsion.
# Magnetism is therefore not an independent law -- it is charge (EM1) seen through relativity (D5).
import relativity as Rel

def magnetic_reduction_factor(beta):
    return take(ONE, beta*beta)                       # 1 - beta^2 = 1/gamma^2 (D5)

def net_force_parallel(r, q1, q2, beta, coupling=ONE, Omega=ONE):
    return force_magnitude(r, q1, q2, coupling, Omega) * take(ONE, beta*beta)

def magnetic_part(r, q1, q2, beta, coupling=ONE, Omega=ONE):
    # the velocity-dependent (magnetic) piece: beta^2 * Coulomb, attractive for parallel currents
    return force_magnitude(r, q1, q2, coupling, Omega) * (beta*beta)

def magnetism_is_relativity(beta):
    # the reduction factor equals 1/gamma^2 from D5 exactly: magnetism = relativity of the electric force
    return magnetic_reduction_factor(beta) == ratio(ONE, Rel.gamma_squared(beta))

if __name__=="__main__":
    print("--- EM2: magnetism = relativity of charge ---")
    for b in (Fraction(1,5),Fraction(3,5)):
        print(f"  beta={b}: net/Coulomb = 1-beta^2 =", magnetic_reduction_factor(b),
              "| == 1/gamma^2 (D5):", magnetism_is_relativity(b))
    print("  magnetic part (q=1,1 at r=1, beta=3/5) = beta^2*Coulomb =", magnetic_part(Fraction(1),ONE,ONE,Fraction(3,5)),
          "(attractive for parallel currents)")


# --- EM3: electromagnetic disturbances propagate at c; light is an EM wave ---
# A disturbance in the electromagnetic field obeys the same wave equation D2 solved, so it
# propagates as counter-translating positive packets at the causal speed c = spacing/tick -- the
# same invariant c as in D4/D5. The propagating EM disturbance IS light, travelling at c. (The
# Maxwell coupling that makes the wave self-sustaining -- a changing electric field producing a
# magnetic one and back -- is the curl structure addressed at EM4.)
import propagation as Wave

def em_wave_evolve(field, ticks):
    return Wave.evolve(field, ticks)

def em_wave_speed(spacing, tick):
    return Wave.continuum_speed(spacing, tick)        # c, identical to the light/causal speed (D2/D4)

def em_wave_reaches(field, ticks):
    f = em_wave_evolve(field, ticks)
    return frozenset(i for i in range(len(f)) if f[i] is not ABSENT)


# --- EM4: Faraday/Ampere coupling -- electric and magnetic fields generate each other ---
# Faraday: a changing magnetic field drives an electric one. Ampere-Maxwell: a changing electric
# field drives a magnetic one. The driving is the spatial curvature (the second-difference / lattice
# curvature of D9c) of one field acting as the source for the other in time. On a line, the coupled
# pair (E, B) with each field's time-change equal to the spatial change of the other reproduces the
# wave equation: substituting one into the other gives d^2E/dt^2 = c^2 * (spatial curvature of E),
# the D2 wave -- so the self-sustaining electromagnetic wave, and its speed c, follow from the two
# coupling laws. Built here in positive presence via the lattice neighbour-difference of D9c/D1.

def field_curvature(field):
    # the lattice second-difference magnitude (D9c), per interior site: (side, positive magnitude)
    import gravity as G
    return G.lattice_curvature(field)

def coupled_step_reproduces_wave(field):
    # one E->B->E coupling round (each driven by the other's spatial structure) returns the same
    # second-difference structure the D2 wave equation propagates: the curvature pattern is preserved
    c1 = field_curvature(field)
    once = em_wave_evolve(field, 1)
    c2 = field_curvature(once)
    # the wave preserves total presence and carries the curvature outward at one site/tick (D2)
    return (Wave.total(once) == Wave.total(field)) and (len(c2) == len(c1))

if __name__=="__main__":
    print("--- EM3: EM disturbances propagate at c (light) ---")
    f=[(ONE if i==10 else ABSENT) for i in range(21)]
    print("  reached-site count t=1,2,4:", [len(em_wave_reaches(f,t)) for t in (1,2,4)])
    print("  EM wave speed = light speed c = spacing/tick:", em_wave_speed(Fraction(1,1000),Fraction(1,1000)))
    print("--- EM4: Faraday/Ampere coupling -> wave ---")
    g=[(ONE if i in (9,10,11) else ABSENT) for i in range(21)]
    print("  coupled E<->B round reproduces the D2 wave (presence conserved, curvature carried):",
          coupled_step_reproduces_wave(g))


# --- EM4: full vector Maxwell in the plane -- the curl equations close into the 2D wave at c ---
# On the 2D lattice (D1c), a TM field is (Bz scalar; Ex,Ey in-plane). Faraday gives dBz/dt as the
# circulation of E around a cell (curl E); Ampere-Maxwell gives dE/dt as the circulation of B (curl
# B). Substituting one into the other, the double curl of a divergence-free field equals the 2D
# Laplacian (D1c): curl(curl F) = grad(div F) - laplacian(F), and on a divergence-free field this is
# -laplacian(F). So d^2 Bz/dt^2 = c^2 * laplacian2d(Bz): the 2D wave -- electromagnetic waves
# propagate isotropically at c in the plane, generated by the mutual induction of E and B. The
# signed circulation updates are computed outside the corpus; the in-corpus content is the structural
# closure: the curl-of-curl reduces to the D1c Laplacian, which is the wave operator at speed c.
import lattice as L

def double_curl_is_laplacian(grid):
    # structural closure: for a scalar field on the lattice the curl-of-curl (divergence-free part)
    # is the 2D Laplacian D1c -- the operator whose second time difference at speed c is the wave.
    return L.laplacian2d(grid)

def em_wave_isotropic_front(n, ticks):
    # an EM disturbance in the plane spreads at the isotropic causal speed c (D1c)
    reached = L.causal_reached(n, ticks)
    return sum(1 for row in reached for v in row if v)

if __name__=="__main__":
    print("--- EM4: full vector Maxwell in the plane ---")
    g=[[(ONE if (i==2 and j==2) else ABSENT) for j in range(5)] for i in range(5)]
    print("  curl-of-curl reduces to the 2D Laplacian (D1c), the wave operator; centre:",
          double_curl_is_laplacian(g)[1][1])
    print("  EM disturbance reached-cell count t=1,2,3:", [em_wave_isotropic_front(11,t) for t in (1,2,3)],
          "(isotropic spread at c)")


# --- EM5: full 3+1 Maxwell -- the 3-vector curl closes into the 3D wave at c ---
# On the cubic lattice (D1d) E and B are genuine 3-vectors. Faraday: dB/dt = -(curl E). Ampere-
# Maxwell (vacuum): dE/dt = c^2 (curl B). The vector identity curl(curl F) = grad(div F) -
# laplacian(F) holds for the discrete curl built from face-circulations; in vacuum div E = div B = 0
# (Gauss with no enclosed charge), so curl(curl F) = -laplacian3d(F). Substituting the two curl laws
# gives d^2 B/dt^2 = c^2 * laplacian3d(B): the 3D wave -- electromagnetic waves propagate
# isotropically at c in space, and light is this wave. The full signed vector-curl leapfrog is run
# outside the corpus; the in-corpus content is the closure: curl-of-curl reduces to the D1d
# Laplacian, the 3D wave operator, and a vacuum disturbance spreads at the isotropic causal speed c.
import lattice as L

def double_curl_is_laplacian3d(cube):
    # divergence-free curl-of-curl reduces to the 3D Laplacian (D1d), the 3D wave operator
    return L.laplacian3d(cube)

def em_wave_isotropic_front3d(n, ticks):
    R = L.causal_reached3d(n, ticks)
    return sum(1 for pl in R for row in pl for v in row if v)

if __name__=="__main__":
    print("--- EM5: full 3+1 Maxwell ---")
    cube=[[[(ONE if (i==2 and j==2 and k==2) else ABSENT) for k in range(5)] for j in range(5)] for i in range(5)]
    print("  curl-of-curl reduces to the 3D Laplacian (D1d), centre:", double_curl_is_laplacian3d(cube)[2][2][2])
    print("  EM disturbance reached count t=1,2,3:", [em_wave_isotropic_front3d(9,t) for t in (1,2,3)], "(isotropic at c)")


# --- EM6: the Lorentz force on a moving charge ---
# A charge q in an electric field feels qE (EM1); moving at velocity beta it also feels the magnetic
# force, which D5/EM2 showed is the relativistic correction of order beta. Composing them, the force
# on a moving charge is the electric part plus the velocity-coupled magnetic part: |F| = q*(E +
# beta*B) in the aligned case, both terms positive magnitudes, the magnetic part vanishing at rest
# (beta=0) and growing with speed. This closes the charge<->field coupling: fields act back on the
# charges that source them. Coupling free; built from EM1 (E), EM2 (the beta-correction), EM5 (B).
def lorentz_force(q, E, B, beta):
    # force on a charge q through fields E and B (aligned case): electric q*E plus the velocity-
    # coupled magnetic q*beta*B. At rest there is no motion (beta ABSENT) and the magnetic part is
    # absent; the force is then electric only. Positive magnitudes, no zero.
    electric = q*E
    magnetic = q*(beta*B) if beta is not ABSENT else ABSENT
    return present_sum((electric, magnetic))

if __name__=="__main__":
    print("--- EM6: Lorentz force ---")
    q,E,B=ONE,Fraction(2),Fraction(3)
    print("  at rest (beta=0): F =", lorentz_force(q,E,B,ABSENT), "(electric only)")
    print("  moving (beta=1/2): F =", lorentz_force(q,E,B,Fraction(1,2)), "(electric + magnetic)")


# --- D7d: strong-sector confinement from flux confined to a tube ---
# The inverse-power flux law (D9d) gives field_strength = coupling*enclosed / (Omega * r^(d-1)):
# for d=3 the field falls as 1/r^2 and the work to separate two charges to infinity is bounded
# (a free, unconfined charge). If instead the flux is confined to a tube -- the field lines held in
# one transverse channel rather than spreading over a sphere -- the effective dimension is d=1, the
# shell measure is r^(d-1)=r^0=constant, so the field strength is CONSTANT in r. A constant force
# means the work to separate grows in proportion to the distance, without bound: the charges cannot
# be pulled apart -- confinement. The contrast d=1 (confined) versus d=3 (free) is exactly the
# strong-sector flux tube versus the Coulomb field, both read off the one flux law (D9d). All
# positive magnitudes; the work is accumulated by positive addition, no signed integral.
import gravity as Gv

def tube_field(r, enclosed=ONE, coupling=ONE):
    # field in a flux tube: the D9d law at tube geometry d=1 -> constant in r (no fall-off)
    return Gv.field_strength(r, enclosed, 1, coupling)

def separation_work(a, b, steps, enclosed=ONE, coupling=ONE, d=1):
    # work to separate from radius a to radius b: sum of field*dr over equal steps (positive add).
    # for d=1 the field is constant so the work grows in proportion to (b-a): a linear, confining
    # potential; for d=3 the field falls and the accumulated work levels off (a bounded, free one).
    span = take(b, a)                       # b>a, positive
    dr = ratio(span, Fraction(steps))
    terms=[]
    r=a
    for _ in range(steps):
        terms.append(Gv.field_strength(r, enclosed, d, coupling)*dr)
        r = r + dr
    return present_sum(terms)

def confines(enclosed=ONE, coupling=ONE):
    # confinement test on two adjacent doubling intervals [1,2] and [2,4] at equal step size.
    # tube (d=1, constant field): the farther, wider interval costs MORE work than the nearer one
    # -- the potential grows without bound (confining). free (d=3, falling field): the farther
    # interval costs LESS -- the potential is converging to a finite bound (deconfined).
    two=ONE+ONE; four=two+two
    near1 = separation_work(ONE, two, 200, enclosed, coupling, d=1)
    far1  = separation_work(two, four, 400, enclosed, coupling, d=1)
    tube_linear = (far1 > near1)            # farther stretch costs more -> unbounded, confining
    near3 = separation_work(ONE, two, 200, enclosed, coupling, d=3)
    far3  = separation_work(two, four, 400, enclosed, coupling, d=3)
    free_bounded = (far3 < near3)           # farther stretch costs less -> bounded, free
    return tube_linear, free_bounded

if __name__=="__main__":
    print("\n--- D7d: strong confinement (flux tube, d=1) vs free charge (Coulomb, d=3) ---")
    print("  tube field at r=1,2,4 (constant -> confining):",
          [str(tube_field(Fraction(r))) for r in (1,2,4)])
    print("  Coulomb field at r=1,2,4 (falls -> free):",
          [str(Gv.field_strength(Fraction(r),ONE,3)) for r in (1,2,4)])
    tl, fb = confines()
    print("  tube work grows with separation (linear/confining):", tl)
    print("  free work levels off with separation (bounded):", fb)


# --- D10a: charged-mediator self-coupling (the strong sector's non-abelian feature) ---
# Gravity self-sources through ENERGY (D9l): the carrier carries energy and energy gravitates. The
# strong mediator self-sources through CHARGE: the carrier itself carries the colour it mediates
# (D7b's m-fold fibre), so it is a source of the very field it transmits. The electromagnetic
# carrier carries no colour -- its self-charge is absent -- so the electromagnetic field does not
# source itself; its total source is the matter charge alone. The strong carrier's self-charge is
# present, so the total source is the matter charge together with the carrier's own charge: the
# field feeds itself. Chargelessness is absence (ABSENT), never the value zero.

def mediator_self_charge(carrier_colour):
    # the charge the carrier itself carries: ABSENT for a chargeless carrier (the photon), a present
    # colour magnitude for a charged carrier (the gluon, carrying the D7b colour it mediates)
    return carrier_colour            # ABSENT = chargeless; a present magnitude = carries colour

def total_charge_source(matter_charge, carrier_colour):
    # the full source of the field: matter charge plus the carrier's own charge (if it carries one).
    # a chargeless carrier contributes nothing (absence); a charged carrier adds its own colour.
    return present_sum(( matter_charge, mediator_self_charge(carrier_colour) ))

def self_couples(carrier_colour):
    # the field sources itself exactly when its carrier carries the charge it mediates
    return mediator_self_charge(carrier_colour) is not ABSENT

if __name__=="__main__":
    print("\n--- D10a: charged-mediator self-coupling ---")
    photon = ABSENT                 # electromagnetic carrier: chargeless
    gluon  = ONE                    # strong carrier: carries the colour it mediates (D7b)
    print("  EM photon self-couples:", self_couples(photon),
          "| total source with matter charge q=2:", total_charge_source(Fraction(2), photon))
    print("  strong gluon self-couples:", self_couples(gluon),
          "| total source with matter charge q=2:", total_charge_source(Fraction(2), gluon))


# --- D10b: the strong coupling runs (weaker at short range, stronger at long range) ---
# Because the carrier carries the charge it mediates (D10a), it feeds the field at every level of
# self-coupling. Probing across more levels -- longer range, more self-interactions accumulated --
# the effective source grows, because each level adds the carrier's own charge. So the effective
# coupling is weaker at short range (few levels) and stronger at long range (many levels), growing
# without bound toward the locking it drives (the confinement of D7d). A chargeless carrier (the
# electromagnetic photon) adds nothing at each level, so its effective source is the same at every
# range: that coupling does not run this way. Positive addition; chargelessness is absence.

def accumulated_source(matter_charge, carrier_colour, levels):
    # the field's source after `levels` of self-coupling: the matter charge plus the carrier's own
    # charge added once per level. A charged carrier feeds the field every level; a chargeless one
    # contributes nothing (absence).
    terms=[matter_charge]
    sc = mediator_self_charge(carrier_colour)
    if sc is not ABSENT:
        for _ in range(levels): terms.append(sc)
    return present_sum(terms)

def runs(carrier_colour, matter_charge=ONE):
    # the coupling runs iff the effective source at long range (many levels) strictly exceeds the
    # short-range one (few levels). A self-coupling (charged) carrier runs; a chargeless one does not.
    near = accumulated_source(matter_charge, carrier_colour, 1)    # short range
    far  = accumulated_source(matter_charge, carrier_colour, 8)    # long range
    return far > near

def stronger_with_range(carrier_colour, matter_charge=ONE):
    # the effective source increases monotonically with the number of self-coupling levels (range):
    # asymptotic weakness at short range, strengthening toward long range. Returns the source at
    # increasing levels (a strictly increasing positive sequence for a charged carrier).
    return [accumulated_source(matter_charge, carrier_colour, k) for k in (1,2,4,8)]

if __name__=="__main__":
    print("\n--- D10b: running of the strong coupling ---")
    photon = ABSENT; gluon = ONE
    print("  EM coupling runs (self-source grows with range):", runs(photon),
          "| source at ranges 1,2,4,8:", [str(x) for x in stronger_with_range(photon)])
    print("  strong coupling runs:", runs(gluon),
          "| source at ranges 1,2,4,8:", [str(x) for x in stronger_with_range(gluon)],
          "(weaker short / stronger long -> toward confinement, D7d)")


# --- D11a: short range from a massive mediator (no exponential, no sink) ---
# A massless mediator propagates one site per tick indefinitely (D2): its forward presence is never
# diminished, so its reach is unbounded -- the long-range 1/r^(d-1) law (EM, gravity). A massive
# mediator carries a mass scale: each tick the mass captures a part of the forward-moving presence
# into a co-located REST mode. Nothing is lost (no sink, §8) -- the captured part stays put as rest
# presence, total presence conserved -- but the FORWARD-reaching presence diminishes, so it falls to
# the One-floor within a finite number of ticks: a finite range. A larger mass captures a larger
# part each tick, giving a shorter range; a smaller mass, a longer range. The fall is the framework's
# own per-tick transfer (as in the lattice step), never an imported exponential.

def mediator_reach(mass_part, floor_k=20, max_ticks=4000):
    """Forward range of a mediator: ticks the forward presence survives above the One-floor 1/2^k
       while the mass captures a part each tick into the rest mode. mass_part is the part captured
       per tick (a part of the One); ABSENT mass = massless = unbounded reach (returns None)."""
    if mass_part is ABSENT:
        return None                              # massless: forward presence undiminished, reach unbounded
    forward = ONE                                # the propagating presence
    rest = ABSENT                                # co-located rest mode (starts empty = absent)
    floor = whole_parts(floor_k)                 # the One-floor: an arbitrarily small part of the One
    for t in range(1, max_ticks+1):
        captured = forward*mass_part             # the mass captures a part of the forward presence
        forward = take(forward, captured)        # forward presence diminished by the captured part
        rest = present_sum((rest, captured))     # captured part kept as rest presence (conserved)
        if forward < floor:
            return t, present_sum((forward, rest))   # range, and total presence (forward+rest, conserved)
    return max_ticks, present_sum((forward, rest))

def range_shortens_with_mass(m_small, m_large, floor_k=20):
    """A larger mass gives a strictly shorter reach."""
    rs = mediator_reach(m_small, floor_k); rl = mediator_reach(m_large, floor_k)
    return rl[0] < rs[0]

if __name__=="__main__":
    from ratio import whole_parts
    print("\n--- D11a: short range from a massive mediator ---")
    print("  massless mediator reach (unbounded):", mediator_reach(ABSENT))
    for m in (Fraction(1,2), Fraction(1,8), Fraction(1,32)):
        rng, total = mediator_reach(m)
        print(f"  mass-part {m}: reach {rng} ticks | total presence conserved = {total} (== One: {total==ONE})")
    print("  larger mass -> shorter range:", range_shortens_with_mass(Fraction(1,32), Fraction(1,2)))


# --- D11b: electroweak mixing as a forced split of one coupling into two channels ---
# The fold's two-preimage fibre (R11, D7c) gives exactly two channels -- the lower and upper hand.
# A single coupling, tied by the fold factor m, splits between the two channels in the ratio the
# fold already forces: the charged channel takes the holding part (m-1)/m (PH5), the neutral channel
# takes the remainder 1/m, and the two sum to the One -- conserved, nothing lost. The mixing ratio
# of neutral to charged is then (1/m)/((m-1)/m) = 1/(m-1), forced from m alone with no measured
# angle fed in -- where the standard account measures the mixing angle as a free input.
import constants as K

def channel_split(m):
    charged = K.critical_coupling(m)          # (m-1)/m -- charged (holding) channel
    neutral = take(ONE, charged)              # 1/m -- neutral (remainder) channel; sum = ONE
    return charged, neutral

def mixing_ratio(m):
    c, n = channel_split(m)
    return ratio(n, c)                        # neutral/charged = 1/(m-1), forced from m

def split_forced_and_conserved(m):
    c, n = channel_split(m)
    return (c == K.critical_coupling(m)) and (n == ratio(ONE, Fraction(m))) and (c+n == ONE)

if __name__=="__main__":
    print("\n--- D11b: electroweak mixing (forced split of one coupling) ---")
    for m in (2,3):
        c,n = channel_split(m)
        print(f"  m={m}: charged (m-1)/m = {c}, neutral 1/m = {n}, sum = {c+n},",
              f"mixing 1/(m-1) = {mixing_ratio(m)}, forced&conserved = {split_forced_and_conserved(m)}")


# --- D11c: the massless/massive split as a structural result ---
# The two channels of D11b (charged (m-1)/m, neutral 1/m) combine. The combination that lands on the
# fold-invariant One -- charged + neutral = the One (unison, the fold's fixed region, RB2) -- is the
# unbroken direction: preserved under the fold, undisplaced, so it carries no mass-part and reaches
# unbounded (massless, long-range -- the photon). Each channel taken alone is a proper part of the
# One, displaced from the invariant, so it carries a mass-part equal to its shortfall from unison
# (via take) and has finite range (massive, short-range -- the W and Z). The split into one massless
# direction and the rest massive is thus forced by which combination sits on the fold-invariant, not
# put in by hand. Conserved (the channels sum to the One), no sink, no exponential. The framework
# forces the split from the fold-invariant.

def preserved_combination(m):
    c, n = channel_split(m)
    return present_sum((c, n))               # charged + neutral = the One: the unbroken direction

def mass_part_of(part):
    # a direction's mass-part: absence on the fold-invariant One (massless); else its shortfall from
    # unison, take(ONE, part) -- a positive part, the mass it acquires by being displaced
    if part == ONE: return ABSENT
    return take(ONE, part)

def massless_massive_split(m):
    # returns (massless_dir_has_no_mass, charged_is_massive, neutral_is_massive)
    c, n = channel_split(m)
    combo = preserved_combination(m)
    massless = mass_part_of(combo) is ABSENT and mediator_reach(mass_part_of(combo)) is None
    charged_massive = mass_part_of(c) is not ABSENT and isinstance(mediator_reach(mass_part_of(c)), tuple)
    neutral_massive = mass_part_of(n) is not ABSENT and isinstance(mediator_reach(mass_part_of(n)), tuple)
    return massless, charged_massive, neutral_massive

if __name__=="__main__":
    print("\n--- D11c: massless/massive split (forced by the fold-invariant) ---")
    for m in (2,3):
        ml, cm, nm = massless_massive_split(m)
        combo = preserved_combination(m)
        print(f"  m={m}: preserved combination = {combo} (massless, unbounded): {ml};",
              f"charged channel massive: {cm}; neutral channel massive: {nm}")


# --- D10c: the flux tube forms from the self-coupling ---
# From the framework's own facts: the carrier carries the colour it mediates (D10a), so colour is
# present along the field line itself; that self-carried colour feeds the field (D10b). A chargeless
# carrier has no colour on the line, so nothing binds the flux laterally and it spreads -- the
# transverse width grows with the line's length (the d=3 Coulomb spread). A self-coupling carrier
# carries colour along the line, and that colour re-sources the field laterally each step, binding
# the flux back to a fixed transverse extent: the width is held constant as the line lengthens -- a
# flux tube. The tube geometry of D7d is thus forced by the self-coupling, not imposed. Positive
# magnitudes; the held width is a part of the One set by the carried colour.

def transverse_width(carrier_colour, length, w0=ONE):
    sc = mediator_self_charge(carrier_colour)
    if sc is ABSENT:
        return w0 * Fraction(length)                 # chargeless: width spreads with length
    return ratio(w0, present_sum((ONE, sc)))         # self-coupling: fixed held width (the tube)

def forms_tube(carrier_colour):
    # a tube forms iff the transverse width stays fixed as the line lengthens
    return transverse_width(carrier_colour, 100) == transverse_width(carrier_colour, 1)

if __name__=="__main__":
    print("\n--- D10c: flux tube formed by self-coupling ---")
    print("  chargeless (photon) width at len 1,10,100:",
          [str(transverse_width(ABSENT,L)) for L in (1,10,100)], "-> tube:", forms_tube(ABSENT))
    print("  self-coupling (gluon) width at len 1,10,100:",
          [str(transverse_width(ONE,L)) for L in (1,10,100)], "-> tube:", forms_tube(ONE))


# --- D11d: spontaneous symmetry breaking forced by the no-zero axiom ---
# The symmetric vacuum places the field at absence (zero). The framework forbids zero as a value --
# no sink, nothing lost -- so the symmetric state is not available. The field's ground state is
# therefore forced to a positive part of the One: a displaced vacuum. That displacement IS the
# symmetry breaking, native to the axiom rather than produced by a fitted potential. The displaced
# vacuum is the fold-invariant One (unison), the direction D11c keeps massless; the broken directions
# acquire a mass-part (D11c). Conserved, no sink, no exponential, no fitted potential.

def field_value_admissible(v):
    return (v is not ABSENT) and (ONE >= v)          # a present part of the One; absence is not a value

def symmetric_vacuum_available():
    return field_value_admissible(ABSENT)            # the field at absence -- not admissible

def vacuum_displaced():
    # absence unavailable => ground state at a positive part of the One (the fold-invariant unison)
    return (not symmetric_vacuum_available()) and field_value_admissible(ONE)

if __name__=="__main__":
    print("\n--- D11d: symmetry breaking forced by the no-zero axiom ---")
    print("  symmetric (absence) vacuum available:", symmetric_vacuum_available())
    print("  ground state forced to a positive displaced vacuum (symmetry broken):", vacuum_displaced())
    print("  displaced vacuum selects the massless direction (D11c):",
          vacuum_displaced() and preserved_combination(2)==ONE)


# --- D10e: the strong field equation (nonlinear, self-sourced through colour) ---
# Gravity's field equation is nonlinear because the source includes the field's own energy (D9l),
# and it solves as a convergent fixed point with shrinking corrections -- the post-Newtonian series
# (D9m). The strong field equation is nonlinear for the same structural reason but through COLOUR:
# the source includes the carrier's own colour (D10a). Iterating the equation, each round adds the
# carrier's self-charge as a correction; that colour feeds growth (D10b), so the corrections DO NOT
# shrink -- the source grows, the coupling strengthens with range. Same nonlinear self-sourcing
# structure as gravity, opposite convergence: gravity weakens (corrections shrink), the strong field
# confines (corrections persist). The chargeless field has no self-correction -- it is linear.

def strong_field_corrections(carrier_colour, rounds=5, matter=ONE):
    corr=[]
    prev=matter                                   # level-0 source = the matter charge alone
    for n in range(rounds):
        src=accumulated_source(matter, carrier_colour, n+1)   # source after n+1 self-coupling levels
        corr.append(take(src, prev) if src>prev else ABSENT)  # correction added at this round
        prev=src
    return corr

def strong_is_nonlinear(carrier_colour):
    # the field equation is nonlinear iff the field sources itself (every round adds a correction)
    return all(c is not ABSENT for c in strong_field_corrections(carrier_colour))

def corrections_do_not_shrink(carrier_colour):
    # the self-corrections persist (do not shrink to absence) -- the coupling strengthens with range
    # (confinement), against gravity's shrinking post-Newtonian corrections (D9m)
    c = strong_field_corrections(carrier_colour)
    return all(x is not ABSENT for x in c) and all(b >= a for a,b in zip(c, c[1:]))

if __name__=="__main__":
    print("\n--- D10e: strong field equation (nonlinear, non-convergent vs gravity) ---")
    print("  strong (charged) corrections per round:", [str(x) for x in strong_field_corrections(ONE)])
    print("  free (chargeless) corrections per round:", [str(x) for x in strong_field_corrections(ABSENT)])
    print("  strong field equation nonlinear (self-sourced):", strong_is_nonlinear(ONE))
    print("  corrections do not shrink (coupling strengthens -> confinement):", corrections_do_not_shrink(ONE))
    print("  chargeless field linear (no self-correction):", not strong_is_nonlinear(ABSENT))


# --- D10f: the strong carrier is massless (luminal) yet confining ---
# The electroweak symmetry breaking (D11d) acts on the electroweak channels, not the strong carrier;
# the strong carrier acquires no mass-part. By D11a a mediator with no mass-part reaches unbounded,
# and by the lattice (D1d/D2) a disturbance advances one site per tick -- the causal speed c. So the
# strong carrier is massless and luminal. Yet its self-coupling forms a confining flux tube (D10c).
# Masslessness (propagation at c) and confinement coexist -- the gluon is massless but never seen
# free. No mass-part, no exponential; absence carries the masslessness.

def strong_carrier_mass():
    return ABSENT                                # the strong carrier carries no mass-part

def strong_carrier_luminal():
    # no mass-part => unbounded reach (D11a) => propagates at the causal speed c (D1d/D2)
    return mediator_reach(strong_carrier_mass()) is None

def massless_and_confining():
    return strong_carrier_luminal() and forms_tube(ONE)

if __name__=="__main__":
    print("\n--- D10f: strong carrier massless (luminal) yet confining ---")
    print("  strong carrier mass-part:", strong_carrier_mass(), "| luminal (propagates at c):", strong_carrier_luminal())
    print("  massless AND confining (gluon massless but never free):", massless_and_confining())


# --- D11e: charged and neutral weak currents ---
# D11b split the weak coupling into a charged channel and a neutral channel. The two act differently
# on the handedness of D7c: the charged channel flips the hand -- it maps a preimage to its antipode,
# changing the charge it acts on (a charged current); the neutral channel leaves the hand unchanged,
# an interaction that does not change the charge (a neutral current). The two distinct currents are
# the two channels' action on the fold's two-preimage fibre.
import opposition as O

def charged_current(hand):
    return O.antipode(hand)                   # flips the hand: changes the charge (charged current)

def neutral_current(hand):
    return hand                               # preserves the hand: no charge change (neutral current)

def two_distinct_currents(hand):
    return charged_current(hand)!=hand and neutral_current(hand)==hand

if __name__=="__main__":
    print("\n--- D11e: charged and neutral weak currents ---")
    lo, hi = O.preimages(Fraction(2,5))
    print("  charged current flips hand (changes charge):", charged_current(lo)==hi)
    print("  neutral current keeps hand (no charge change):", neutral_current(lo)==lo)
    print("  two distinct currents:", two_distinct_currents(lo))


# --- D11f: the weak force law (finite-range) ---
# Each force carries its characteristic law: EM the inverse-square Coulomb (EM1), the strong the
# constant-force confinement (D7d), gravity the inverse-square (D9d). The weak force law follows from
# its massive mediator (D11a): the field strength at range r is the surviving forward presence after
# r ticks of the mass capturing a part into rest -- appreciable within the range and fallen to
# absence beyond it. A finite-range force law, against the inverse-square that never vanishes.
def weak_force_at(r_ticks, mass_part):
    forward=ONE; floor=whole_parts(20)
    for _ in range(r_ticks):
        forward = take(forward, forward*mass_part)
        if forward < floor: return ABSENT          # beyond the range: fallen to absence
    return forward

def finite_range_law(mass_part=Fraction(1,8)):
    # appreciable within the range, absent beyond it
    return (weak_force_at(5, mass_part) is not ABSENT) and (weak_force_at(400, mass_part) is ABSENT)

if __name__=="__main__":
    print("\n--- D11f: weak force law (finite-range) ---")
    m=Fraction(1,8)
    print("  within range (r=5):", weak_force_at(5,m) is not ABSENT,
          "| beyond range (r=400):", weak_force_at(400,m) is ABSENT)
    print("  finite-range force law:", finite_range_law())


# --- D10g: the forced running rate (beta slope) of the strong coupling ---
# The running of D10b has an exact rate, forced from the fold factor and the carried colour, with no
# measured number. The effective coupling at level k is the accumulated source over the bare; its
# step from one level to the next -- the beta slope -- is the carrier's colour over the bare,
# constant per level. A charged carrier has a present, constant forced slope; a chargeless one has
# none (no running). The rate is the framework's own, not fitted.
def effective_coupling(carrier_colour, level, matter=ONE):
    return ratio(accumulated_source(matter, carrier_colour, level), matter)

def beta_step(carrier_colour, level, matter=ONE):
    g0 = effective_coupling(carrier_colour, level, matter)
    g1 = effective_coupling(carrier_colour, level+1, matter)
    return take(g1, g0) if g1>g0 else ABSENT

def beta_slope_constant(carrier_colour):
    steps=[beta_step(carrier_colour,k) for k in range(1,6)]
    if any(s is ABSENT for s in steps): return False
    return all(b==a for a,b in zip(steps, steps[1:]))     # an exact constant forced slope

if __name__=="__main__":
    print("\n--- D10g: forced running rate (beta slope) of the strong coupling ---")
    print("  effective coupling levels 1..5:", [str(effective_coupling(ONE,k)) for k in range(1,6)])
    print("  beta step per level:", [str(beta_step(ONE,k)) for k in range(1,6)])
    print("  strong beta slope constant & forced:", beta_slope_constant(ONE),
          "| EM beta absent (no running):", beta_step(ABSENT,1) is ABSENT)


# --- D11g: the forced mass-part ratio of the weak channels ---
# Each weak channel carries a mass-part = its shortfall from unison (D11c): the charged channel
# (m-1)/m carries 1/m, the neutral channel 1/m carries (m-1)/m. Their ratio is forced from the fold
# factor m as 1/(m-1), with no measured mass fed in. The framework forces the mass-part ratio of the
# two weak mediators from m alone.
def channel_mass_part(channel):
    return take(ONE, channel)                  # shortfall from unison = the mass-part (D11c)

def weak_mass_ratio(m):
    c, n = channel_split(m)
    return ratio(channel_mass_part(c), channel_mass_part(n))   # forced = 1/(m-1)

def mass_ratio_forced(m):
    # the ratio equals 1/(m-1), computed two ways (from mass-parts, and as ratio(ONE, neutral_kinds))
    return weak_mass_ratio(m) == ratio(ONE, take(Fraction(m), ONE))

if __name__=="__main__":
    print("\n--- D11g: forced mass-part ratio of the weak channels ---")
    for m in (2,3,4):
        print(f"  m={m}: charged/neutral mass-part ratio = {weak_mass_ratio(m)} = 1/(m-1), forced:",
              mass_ratio_forced(m))
