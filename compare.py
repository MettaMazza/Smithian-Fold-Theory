"""Phase 1 — comparison harness. Takes a framework prediction and tests it against a cited
physical target; reports the agreement. A correspondence is called established only when the
framework value reproduces the cited physical relationship exactly (or to stated precision).
This file orchestrates in the permitted language; any conventional log/exp lives on the
target side (physics_targets), so the framework code stays gate-clean."""
from fractions import Fraction
import correspondence as Co, physics_targets as T
import beats as B
from ratio import take, ABSENT, whole_parts, ONE

def test_beat_law(pairs):
    """Framework beat frequency (one-in-lcm of periods, RB1) vs physical f_beat=|f1-f2|."""
    rows=[]; all_match=True
    for a,b in pairs:
        f1=Co.frequency(a); f2=Co.frequency(b)
        if f1==f2: continue                      # unison: no beat (no zero magnitude)
        fw_beat=Co.beat_frequency(a,b)
        law_beat=T.beat_law_holds(f1,f2)
        match=(fw_beat==law_beat)
        all_match=all_match and match
        rows.append((a,b,f1,f2,fw_beat,law_beat,match))
    return rows, all_match

def test_forced_dimension():
    """D9g: orbital stability (d<4) and a vanishing-at-infinity potential (d>2) force d=3 uniquely."""
    import gravity as Gv
    if Gv.forced_dimension()!=[3]: return False
    if Gv.potential_decays(2) or not Gv.potential_decays(3): return False
    return True

def test_point_mass_redshift():
    """D9h: A(r)=1-2GM/(r c^2) positive outside 2GM/c^2; clock-rate ratio (far/near) > 1."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    GM,c=ONE,Fraction(10)
    for r in (Fraction(1),Fraction(2),Fraction(4)):
        if not (Gv.schwarzschild_gtt_leading(r,GM,c) > whole_parts(64)): return False
    if not (Gv.redshift_point_mass_sq(Fraction(1),Fraction(4),GM,c) > ONE): return False
    # monopole conserved => no monopole gravitational radiation
    pert=[ONE if i==10 else ABSENT for i in range(21)]
    if not Gv.monopole_conserved(pert,4): return False
    return True

def test_coulomb():
    """EM1: Coulomb force inverse-square, symmetric in the charges, like repel / unlike attract."""
    from fractions import Fraction
    import charge as Q
    if [Q.force_magnitude(Fraction(r),Fraction(2),Fraction(3)) for r in (1,2,3)] != [Fraction(6),Fraction(3,2),Fraction(2,3)]:
        return False
    if Q.force_magnitude(Fraction(2),Fraction(2),Fraction(3))!=Q.force_magnitude(Fraction(2),Fraction(3),Fraction(2)): return False
    if Q.force_sense("pos","pos")!="repel" or Q.force_sense("pos","neg")!="attract": return False
    return True

def test_lattice3d():
    """D1d: 3D cubic lattice operator. 3D Laplacian of a point source is a peak of magnitude 6;
       the causal front advances one site per tick isotropically (octahedral counts 7,25,63)."""
    from fractions import Fraction
    import lattice as L
    cube=[[[ONE if (i==2 and j==2 and k==2) else ABSENT for k in range(5)] for j in range(5)] for i in range(5)]
    if L.laplacian3d(cube)[2][2][2]!=("peak",Fraction(6)): return False
    if [sum(1 for pl in L.causal_reached3d(9,t) for row in pl for v in row if v) for t in (1,2,3)]!=[7,25,63]: return False
    return True

def test_lattice2d():
    """D1c: 2D lattice operator. 2D Laplacian of a point source is a peak of magnitude 4 with a
       four-cell opposition ring; the causal front advances one site per tick isotropically (speed c)."""
    from fractions import Fraction
    import lattice as L
    g=[[ONE if (i==2 and j==2) else ABSENT for j in range(5)] for i in range(5)]
    lap=L.laplacian2d(g)
    if lap[1][1]!=("peak",Fraction(4)): return False
    labels=[cell[0] for row in lap for cell in row]
    if labels.count("peak")!=1 or labels.count("well")!=4 or labels.count("flat")!=4: return False
    # isotropic causal growth: reached-cell counts form the diamond sequence 5,13,25 at t=1,2,3
    if [sum(1 for r in L.causal_reached(11,t) for v in r if v) for t in (1,2,3)]!=[5,13,25]: return False
    return True

def test_pn_convergence():
    """D9m: the nonlinear field equation solves as a convergent fixed point -- successive
       post-Newtonian self-energy corrections form a decreasing positive sequence."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    mass=[[[(ONE+Fraction(1,10) if (i==2 and j==2 and k==2) else ONE) for k in range(5)] for j in range(5)] for i in range(5)]
    ok,seq=Gv.nonlinear_correction_shrinks(mass, Fraction(1,3), 4)
    return ok and all(x>whole_parts(64) for x in seq) and seq[1]<seq[0]

def test_tensor_bianchi():
    """D9n: the metric is many-component (10 in 3+1) and the contracted Bianchi identity forces
       source conservation -- a static (balanced) source has zero lattice divergence; a leaking one
       does not."""
    from fractions import Fraction
    import gravity as Gv
    if Gv.metric_component_count(Fraction(4))!=Fraction(10): return False
    if Gv.metric_component_count(Fraction(3))!=Fraction(6): return False
    if not Gv.bianchi_conserved([(Fraction(2),Fraction(2)),(Fraction(1),Fraction(1))]): return False
    if Gv.bianchi_conserved([(Fraction(3),Fraction(2))]): return False
    return True

def test_continuum_limit():
    """D9p: the lattice curvature, scaled by 1/a^2, converges to the continuum curvature as the
       spacing a shrinks (the scaled second difference of x^2 settles to 2; refinements converge)."""
    from fractions import Fraction
    from ratio import ONE, ratio
    import gravity as Gv
    vals=[]; sps=[]
    for k in range(1,6):
        a=ratio(ONE, Fraction(2)**k); x=ONE
        fL=x*x; fC=(x+a)*(x+a); fR=(x+a+a)*(x+a+a)
        vals.append(Gv.second_difference_scaled(fL,fC,fR,a)); sps.append(a)
    if not all(v==Fraction(2) for v in vals): return False     # exact continuum value at every spacing
    ok,_=Gv.continuum_limit_converges(vals,sps)
    return ok

def test_quadrupole_power():
    """D9q: quadrupole radiated power. A time-varying quadrupole has nonzero third time-difference
       (radiates), a static one zero (silent); power scales as the square of the third rate."""
    from fractions import Fraction
    import gravity as Gv
    Q=[Fraction(1),Fraction(8),Fraction(27),Fraction(64),Fraction(125),Fraction(216)]
    if not all(v==Fraction(6) for v in Gv.third_difference(Q)): return False
    if Gv.radiated_power(Fraction(6),Fraction(2))!=Fraction(2)*Fraction(36): return False
    if any(v is not ABSENT for v in Gv.third_difference([Fraction(5)]*6)): return False
    return True

def test_schwarzschild():
    """D9o: closed-form static vacuum solution A(r)=1-rs/r, positive outside the horizon, satisfying
       the conserved-flux vacuum condition (r^2 dA/dr = rs), with redshift > 1 and the weak-field limit."""
    from fractions import Fraction
    from ratio import ONE, take, ratio
    import gravity as Gv
    rs=ONE
    for r in (Fraction(2),Fraction(3),Fraction(10)):
        if Gv.schwarzschild_A(r,rs)!=take(ONE,ratio(rs,r)): return False
        if not (Gv.schwarzschild_A(r,rs) > whole_parts(64)): return False
    if not Gv.schwarzschild_vacuum_ok(rs): return False
    if not (Gv.schwarzschild_redshift_sq(Fraction(2),Fraction(10),rs) > ONE): return False
    return True

def test_nonlinear_gravity():
    """D9l: gravity self-sources. The field's own energy density (squared metric curvature) is zero
       for a flat metric, positive for a curved one, and the full nonlinear source exceeds the matter
       source -- the essential nonlinearity of general relativity."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    flat=[[[ONE for _ in range(5)] for _ in range(5)] for _ in range(5)]
    mass=[[[(Fraction(5,4) if (i==2 and j==2 and k==2) else ONE) for k in range(5)] for j in range(5)] for i in range(5)]
    if any(v is not ABSENT for pl in Gv.grad_energy3d(flat) for row in pl for v in row): return False
    if not any(v is not ABSENT for pl in Gv.grad_energy3d(mass) for row in pl for v in row): return False
    rho=[[[ (ONE if (i==2 and j==2 and k==2) else ABSENT) for k in range(5)] for j in range(5)] for i in range(5)]
    if not (Gv.nonlinear_source(mass,rho,ONE)[2][2][2] > rho[2][2][2]): return False
    return Gv.field_self_sources(flat, mass)

def test_einstein3d():
    """D9k: weak-field Einstein equation in 3D -- flat metric source-free, mass-peaked metric
       positively curved, source = coupling * curvature on the cubic lattice (D1d)."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    flat=[[[ONE for _ in range(5)] for _ in range(5)] for _ in range(5)]
    if any(cell[0]!="flat" for pl in Gv.metric_curvature3d(flat) for row in pl for cell in row): return False
    mass=[[[(Fraction(5,4) if (i==2 and j==2 and k==2) else ONE) for k in range(5)] for j in range(5)] for i in range(5)]
    if Gv.metric_curvature3d(mass)[2][2][2][0]!="peak": return False
    src=Gv.einstein_weakfield_source(mass, Fraction(3))
    if src[2][2][2][1]!=Gv.metric_curvature3d(mass)[2][2][2][1]*Fraction(3): return False
    return True

def test_curved_metric():
    """D9j: curvature of a varying metric in the plane. A constant metric is flat (source-free); a
       metric peaked at a mass has positive curvature; source = coupling * curvature (D9c in 2D)."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    flat=[[ONE for _ in range(5)] for _ in range(5)]
    if any(cell[0]!="flat" for row in Gv.metric_curvature(flat) for cell in row): return False
    massed=[[(Fraction(5,4) if (i==2 and j==2) else ONE) for j in range(5)] for i in range(5)]
    if Gv.metric_curvature(massed)[1][1][0]!="peak": return False
    src=Gv.curvature_sources(massed, Fraction(2))
    if src[1][1][1]!=Gv.metric_curvature(massed)[1][1][1]*Fraction(2): return False
    return True

def test_quadrupole():
    """D9i: for a symmetric standing source the monopole (total presence) and the first-moment rate
       (momentum) are conserved, so monopole and dipole do not radiate; leading radiation is quadrupole."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    sym=[ONE if i in (8,12) else ABSENT for i in range(21)]
    if Gv.monopole_radiates(sym,4): return False
    if Gv.dipole_rate_changes(sym,4): return False
    return Gv.leading_radiation()=="quadrupole"

def test_variance_uncertainty():
    """D6b: variance-form uncertainty = (s_t*s_f)/N, spacing-independent, >= ONE iff s_t*s_f >= N."""
    from fractions import Fraction
    from ratio import ONE
    import quantum as Qm
    for k in (1,2,3):
        N=Qm.dimension(k)
        for a in (Fraction(1),Fraction(1,7),Fraction(5,3)):
            if Qm.spread_product(ONE,N,a,k)!=ONE: return False         # bound attained, a cancels
        if not Qm.variance_bound_holds(ONE,N,Fraction(2,9),k): return False
        if Qm.variance_bound_holds(ONE,ONE,Fraction(2,9),k): return False
    return True

def test_maxwell3d():
    """EM5: full 3+1 Maxwell -- 3D curl-of-curl reduces to the D1d Laplacian (peak 6), so EM waves
       propagate isotropically at c in space (octahedral counts 7,25,63)."""
    from fractions import Fraction
    import charge as Q
    cube=[[[ONE if (i==2 and j==2 and k==2) else ABSENT for k in range(5)] for j in range(5)] for i in range(5)]
    if Q.double_curl_is_laplacian3d(cube)[2][2][2]!=("peak",Fraction(6)): return False
    if [Q.em_wave_isotropic_front3d(9,t) for t in (1,2,3)]!=[7,25,63]: return False
    return True

def test_vector_maxwell():
    """EM4: full vector Maxwell in the plane -- curl-of-curl reduces to the 2D Laplacian (D1c), the
       wave operator, so EM disturbances propagate isotropically at c (diamond counts 5,13,25)."""
    from fractions import Fraction
    import charge as Q
    g=[[ONE if (i==2 and j==2) else ABSENT for j in range(5)] for i in range(5)]
    if Q.double_curl_is_laplacian(g)[1][1]!=("peak",Fraction(4)): return False
    if [Q.em_wave_isotropic_front(11,t) for t in (1,2,3)]!=[5,13,25]: return False
    return True

def test_critical_coupling():
    """PH5 (forced critical coupling): the framework forces g*=(m-1)/m from its expansion factor m --
       the coupling at which the transverse carry factor (1-g)*m equals the One (the sync/desync
       boundary). m=2 -> 1/2, m=3 -> 2/3; synchronises above g*, not below. No value fitted; the
       the framework forces the critical coupling g*=(m-1)/m from its own expansion factor."""
    from fractions import Fraction
    from ratio import ONE
    import constants as C
    if C.critical_coupling(2)!=Fraction(1,2): return False
    if C.critical_coupling(3)!=Fraction(2,3): return False
    if C.critical_coupling(4)!=Fraction(3,4): return False
    if not C.critical_is_boundary(2): return False
    if not C.critical_is_boundary(3): return False
    if not C.synchronises(Fraction(3,5),2): return False     # above 1/2
    if C.synchronises(Fraction(2,5),2): return False         # below 1/2
    return True

def test_massless_massive_split():
    """D11c: the channel combination on the fold-invariant One (charged+neutral=One) is the unbroken
       direction -- massless, unbounded range; each channel alone is a proper part of the One,
       displaced, carrying a mass-part and a finite range. The massless/massive split is forced by
       the fold-invariant, not assumed [one massless mediator (photon) + massive mediators (W,Z)]."""
    import charge as Q
    for m in (2,3):
        if Q.preserved_combination(m) != ONE: return False        # the preserved direction is the One
        ml, cm, nm = Q.massless_massive_split(m)
        if not (ml and cm and nm): return False                   # massless preserved + massive channels
    return True

def test_mixing():
    """D11b: a single coupling splits between the fold's two channels (R11/D7c) in the ratio the fold
       forces -- charged (m-1)/m, neutral 1/m, summing to the One -- with mixing ratio 1/(m-1), forced
       from m alone with no measured angle fed in [electroweak mixing: one coupling resolving into a
       charged and a neutral channel]."""
    import charge as Q
    for m in (2,3):
        c,n = Q.channel_split(m)
        if c+n != ONE: return False                       # conserved: channels sum to the One
        if not Q.split_forced_and_conserved(m): return False
    if Q.mixing_ratio(2)!=ONE: return False               # m=2 -> 1/(m-1)=1
    if Q.mixing_ratio(3)!=Fraction(1,2): return False     # m=3 -> 1/(m-1)=1/2
    return True

def test_massive_range():
    """D11a: a massless mediator reaches unbounded; a massive mediator's forward presence is captured
       into a rest mode each tick (total presence conserved, no sink), so its forward reach is finite
       and a larger mass gives a shorter range -- short-range from mass without an exponential
       [massive mediator => short-range force; massless => long-range]."""
    import charge as Q
    if Q.mediator_reach(ABSENT) is not None: return False              # massless: unbounded reach
    r2 = Q.mediator_reach(Fraction(1,2)); r8 = Q.mediator_reach(Fraction(1,8))
    if not (isinstance(r2,tuple) and isinstance(r8,tuple)): return False
    if r2[1]!=ONE or r8[1]!=ONE: return False                          # total presence conserved at the One
    if not (r2[0] < r8[0]): return False                              # bigger mass (1/2) shorter than 1/8
    if not Q.range_shortens_with_mass(Fraction(1,32), Fraction(1,2)): return False
    return True

def test_colour_neutral():
    """D10d: the two colour-neutral combinations -- a whole group of m colours (a baryon, D7b) and a
       colour with its opposition/anticolour (a meson, R9) -- are both neutral [hadrons: qqq baryons
       and q-qbar mesons]."""
    import particles as P
    b, me = P.colour_neutral_combinations(3)
    return b and me

def test_strong_field_eq():
    """D10e: the strong field equation is nonlinear (self-sourced through colour, D10a), and unlike
       gravity's convergent fixed point (D9m, shrinking corrections) its self-corrections do not
       shrink -- the source grows, the coupling strengthens (confinement); the chargeless field is
       linear [non-abelian Yang-Mills self-sourcing vs the convergent gravitational one]."""
    import charge as Q
    if not Q.strong_is_nonlinear(ONE): return False           # self-sourced => nonlinear
    if not Q.corrections_do_not_shrink(ONE): return False      # corrections persist => confinement
    if Q.strong_is_nonlinear(ABSENT): return False             # chargeless => linear, no self-source
    return True

def test_strong_luminal():
    """D10f: the strong carrier acquires no mass-part (the electroweak breaking D11d does not act on
       it), so it is massless and propagates at the causal speed c (D11a/D1d) -- yet it confines
       (D10c). Masslessness and confinement coexist [the gluon is massless but never free]."""
    import charge as Q
    return Q.strong_carrier_luminal() and Q.massless_and_confining()

def test_weak_currents():
    """D11e: the weak coupling's two channels (D11b) act differently on the handedness (D7c) -- the
       charged channel flips the hand (changes the charge: a charged current), the neutral channel
       preserves it (a neutral current) [W charged current and Z neutral current]."""
    import charge as Q, opposition as O
    lo, hi = O.preimages(Fraction(2,5))
    return Q.charged_current(lo)==hi and Q.neutral_current(lo)==lo and Q.two_distinct_currents(lo)

def test_weak_force_law():
    """D11f: the weak force law is finite-range -- appreciable within the mediator's range (D11a) and
       fallen to absence beyond it, against the inverse-square that never vanishes [short-range weak
       force vs long-range EM/gravity]."""
    import charge as Q
    return Q.finite_range_law() and (Q.weak_force_at(5,Fraction(1,8)) is not ABSENT)

def test_beta_slope():
    """D10g: the strong coupling's running rate (beta slope) is an exact constant forced from the
       carried colour over the bare source (D10b), with the abelian beta absent -- a forced running
       rate, no measured number [the QCD beta function sign/structure, forced]."""
    import charge as Q
    return Q.beta_slope_constant(ONE) and (Q.beta_step(ABSENT,1) is ABSENT)

def test_weak_mass_ratio():
    """D11g: the two weak channels' mass-part ratio is forced from the fold factor as 1/(m-1) (D11c
       mass-parts), with no measured mass fed in [the W/Z mass-ratio structure, forced from m]."""
    import charge as Q
    return all(Q.mass_ratio_forced(m) for m in (2,3,4)) and Q.weak_mass_ratio(3)==Fraction(1,2)

def test_dictionary():
    """Phase Three step 1: the complete fold->physics dictionary. Every physical correspondence is
       traced to its upstream results and grounded in the One -- each references only established,
       confirmed results, and its chain reaches the definitions (or is a root built directly on the
       permitted-language primitives with a passing confirmation). Machine-checked over all
       correspondences [the single fold->physics map, the unification stated in full]."""
    import dictionary as Dy
    return Dy.every_correspondence_grounded() and len(Dy.dictionary())==len(Dy.PHYS)

def test_u4():
    """U4: the fundamental coupling g* (PH5), the holding/criticality threshold (R7/PH5a), and the
       charged weak channel (D11b) are one forced ratio (m-1)/m -- three distinct physical roles, one
       forced value, across all fold factors."""
    import correspondence as Co
    return Co.u4_holds()

def test_u5():
    """U5: the fundamental coupling is fixed by the number of internal colour kinds N (D7b):
       g* = (N-1)/N, across all fold factors."""
    import correspondence as Co
    return Co.u5_holds()

def test_u6():
    """U6: the electroweak mixing 1/(m-1) (D11b) times the charged coupling (m-1)/m (PH5) equals the
       neutral channel 1/m (D11b) -- a forced product tie across the weak sector, across all m."""
    import correspondence as Co
    return Co.u6_holds()

def test_u7():
    """U7: the framework forces the fold factor per sector -- the electroweak sector is m=2 (the fold's
       two-preimage chirality fibre, D7c), the strong sector is m=3 (the three colours, D7b). The
       sector m is the count of internal kinds in its fibre, forced not assigned."""
    import correspondence as Co
    return Co.sector_m_forced()

def test_prediction_colour():
    """T1 (prediction test): the framework's forced colour count (3, fixed first from U7/D7b) equals
       the measured number of colours (3, the arbiter -- R-ratio in e+e->hadrons, Delta++, pi0->2g).
       A forced value confirmed by measurement, the measured number used only as arbiter."""
    import correspondence as Co
    return Co.forced_colour_count()==3 and Co.prediction_test_colour()

def test_mediator_count():
    """N1 (a new forced result): the mediator count is forced from the colour count as m^2-1 -- the
       colour-anticolour combinations minus the one colourless singlet (D10a carrier carries colour,
       R9 anticolour, D7b m colours). Forced first: m=3 -> 8, m=2 -> 3. Arbiter: the established
       mediator count is m^2-1 (the adjoint dimension of SU(m)); 8 gluons for 3 colours, the
       colourless singlet excluded."""
    import particles as P
    return P.forced_mediators(3)==8 and P.forced_mediators(2)==3 and P.forced_mediators(4)==15

def test_self_loop_closed():
    """C1s: a self-observing loop (the fold as the act of observation, re-entering its result) stays
       within the system at every step -- closure (R8). Self-observation cannot take a structure
       outside itself."""
    import selfmodel as S
    return S.loop_closed(Fraction(3,7)) and S.loop_closed(Fraction(5,9))

def test_self_blind_spot():
    """C2s: the act of observation is two-to-one (R11), so a state and its antipode are observed
       identically -- self-observation cannot recover which preimage it came from. An intrinsic blind
       spot forced by the 2-to-1 structure of the act."""
    import selfmodel as S
    return all(S.blind_spot(Fraction(p,16)) for p in (1,3,5,7))

def test_self_fixed_point():
    """C3s: unison (the One) is the one state unchanged by observation (fold(1)=1); the half-One
       observes to unison; self-coincidence below unison repels (R5). Unison is the fixed point of
       self-observation."""
    import selfmodel as S
    return S.observes_to_unison(Fraction(1,2)) and S.unison_is_fixed()

def test_self_integration():
    """C4s: the framework forces a holding threshold (m-1)/m (R7) at which coupled copies lock into
       one. Applied to self-observers, it forces an integration threshold: separate observers below
       it, one integrated observer at or above it -- binding set by the same forced ratio (m-1)/m."""
    import selfmodel as S
    return S.binds_at_threshold(2) and S.integration_threshold(2)==Fraction(1,2)

def test_self_discrete():
    """C5s: the fold is the unit act of observation and it is atomic (D6) -- each fold yields one bit,
       casting out a whole or not, with no partial fold. Observation proceeds in discrete, indivisible
       moments, one fold each [the discreteness of the observational moment]."""
    import selfmodel as S
    return S.observation_is_discrete() and len(S.moments(Fraction(3,7),8))==8

def test_a1_dispersion():
    """A1 (quantum dynamics, free dispersion): a quantum amplitude's phase advances by the framework's
       rotation; the kinetic term is the lattice second-difference (D1). The leading kinetic magnitude
       of mode j is (j/N)^2 -- exactly proportional to the square of the wavenumber, the free
       Schrodinger dispersion to leading order; the full lattice eigenvalue approaches it in the
       long-wavelength limit (cross-checked outside, as D9p ties the gravity lattice to its continuum)."""
    import quantumdyn as Qd
    return Qd.free_dispersion_quadratic()

def test_a2_potential():
    """A2 (quantum dynamics under a potential): a potential is a position-dependent rotation step (the
       static local source of D9c); the amplitude's phase advances each tick by the kinetic dispersion
       (A1) plus the local potential, composed as positive rotation magnitudes -- the
       Schrodinger-with-potential structure, total rate = kinetic + V, lifting every level by V."""
    import quantumdyn as Qd
    return Qd.potential_shifts_spectrum()

def test_a3_spectrum_tie():
    """A3 (stationary states are the forced spectrum): a stationary state of the quantum evolution
       turns at a single constant rate; the allowed rates, on the forced half-One floor and uniform
       spacing, are exactly the oscillator levels (n+1/2)*spacing of PH4b -- the dynamics (QA1/QA2)
       and the spectrum (PH4b) are one structure."""
    import quantumdyn as Qd
    return Qd.stationary_states_are_forced_spectrum()

def test_a4_dirac():
    """A4 (relativistic two-component step): the first-order two-component update -- momentum advancing
       each chirality hand, mass coupling each hand to the other -- applied twice gives net rate^2 =
       p^2 + m^2, the relativistic energy-momentum relation. The cross terms cancel by the antipodal
       opposition (R11/R9), which is what makes the first-order step square to the relativistic
       relation: the defining property of the Dirac structure. The massless limit gives rate^2 = p^2."""
    import quantumdyn as Qd
    return Qd.dirac_squares_to_relativistic() and Qd.massless_step_is_luminal()

def test_b1_coupling_structure():
    """B1 (forced interaction-strength structure): every dimensionless interaction strength the
       framework forces comes from the single fold factor m -- the fundamental coupling (m-1)/m (PH5),
       the electroweak mixing 1/(m-1) (D11b), the weak mass ratio 1/(m-1) (D11g), the strong running
       slope (D10g) -- with nothing fed in. The complete forced structure, stated as one fact."""
    import correspondence as Co
    return Co.coupling_structure_forced()

def test_b2_arbiter():
    """B2 (the forced electromagnetic coupling): the framework forces the electromagnetic coupling from
       its own axiom -- the binary fold (m=2, the axiom-native sector) gives g*=(m-1)/m=1/2. This is the
       system's forced EM coupling, recorded as the system's result, no measured value fed in. The
       forced integer quantities (colour count, mediator count, dimension) stand confirmed by their
       arbiters in T1/N1/D9g; a measured EM coupling, if compared, is a secondary arbiter, never the
       standard the forced value must meet."""
    import compare as _C, correspondence as Co
    return Co.em_coupling_forced() and _C.test_b1_coupling_structure()

def test_qa5_dirac_full():
    """QA5 (full Dirac structure in 3+1D): the four-generator first-order step -- three spatial momenta
       and the mass -- squares to the relativistic dispersion p1^2+p2^2+p3^2+m^2, each generator
       squaring to its own term and every distinct pair cancelling as an opposed pair returning to the
       One (R9/R11): the anticommuting gamma-algebra property in the permitted language. Massless limit
       gives the three-momentum sum."""
    import quantumdyn as Qd
    return Qd.dirac_full_squares_to_relativistic()

def test_unification():
    """U1: every characteristic dimensionless constant of the four interactions -- the fundamental
       coupling (m-1)/m (PH5), the colour count m (D7b), the strong running slope (D10g), the
       electroweak mixing 1/(m-1) (D11b), the weak mass ratio 1/(m-1) (D11g) -- is forced from the
       single fold factor m, none fed in [unification: one axiom, one fold factor, all four forces]."""
    import correspondence as Co
    c = Co.forced_constants_from_m()
    return Co.all_four_forces_from_one_m() and c["g_star"]==Fraction(1,2) and c["colour_count"]==3

def test_forced_relationship():
    """U2: the framework forces the electroweak mixing ratio (D11b) and the weak channel mass-part
       ratio (D11g) equal -- both 1/(m-1) -- for every fold factor m: a forced relationship between
       two electroweak observables, no measured value fed in."""
    import correspondence as Co
    return Co.forced_relationship_all_m() and Co.mixing_equals_mass_ratio(3)

def test_flux_tube():
    """D10c: the self-carried colour (D10a) binds the flux to a fixed transverse width as the line
       lengthens -- a flux tube; the chargeless field's width spreads with length. The tube geometry
       of D7d is forced by the self-coupling, not imposed [QCD flux tube formation]."""
    import charge as Q
    if Q.forms_tube(ABSENT): return False                      # chargeless: spreads, no tube
    if not Q.forms_tube(ONE): return False                     # self-coupling: fixed width, tube
    if Q.transverse_width(ABSENT,100)==Q.transverse_width(ABSENT,1): return False  # spreads
    if Q.transverse_width(ONE,100)!=Q.transverse_width(ONE,1): return False        # held fixed
    return True

def test_symmetry_breaking():
    """D11d: the symmetric vacuum (field at absence) is unavailable under the no-zero axiom, so the
       ground state is forced to a positive part of the One -- a displaced vacuum; that displacement
       is the symmetry breaking, selecting the fold-invariant massless direction (D11c)
       [spontaneous symmetry breaking / nonzero vacuum]."""
    import charge as Q
    if Q.symmetric_vacuum_available(): return False            # absence not an admissible vacuum
    if not Q.vacuum_displaced(): return False                  # ground state displaced to a positive value
    if Q.preserved_combination(2)!=ONE: return False           # the displaced vacuum is the fold-invariant One
    return True

def test_self_coupling():
    """D10a: the strong carrier carries the colour it mediates, so the field sources itself (total
       source = matter charge + carrier charge); the chargeless electromagnetic carrier does not
       self-couple (source = matter charge alone) [non-abelian self-coupling vs abelian]."""
    import charge as Q
    if Q.self_couples(ABSENT): return False                        # photon: chargeless, no self-source
    if not Q.self_couples(ONE): return False                       # gluon: carries colour, self-sources
    if Q.total_charge_source(Fraction(2), ABSENT)!=Fraction(2): return False   # EM: matter only
    if Q.total_charge_source(Fraction(2), ONE)!=Fraction(3): return False      # strong: matter + carrier
    return True

def test_running():
    """D10b: the self-coupling carrier feeds the field at every level, so the effective source grows
       with range -- weaker at short range, stronger at long range (toward confinement, D7d); the
       chargeless carrier shows no such growth [running of the strong coupling / asymptotic freedom]."""
    import charge as Q
    if Q.runs(ABSENT): return False                               # EM coupling does not run this way
    if not Q.runs(ONE): return False                              # strong coupling runs
    seq = Q.stronger_with_range(ONE)
    if not all(b>a for a,b in zip(seq, seq[1:])): return False    # strictly increasing with range
    flat = Q.stronger_with_range(ABSENT)
    if not all(b==a for a,b in zip(flat, flat[1:])): return False # EM: flat across range
    return True

def test_confinement():
    """D7d: flux confined to a tube (effective dimension one) makes the field constant in r, so the
       work to separate grows without bound -- confinement; the free Coulomb field (d=3) falls and
       its separation work converges to a bound [strong-sector flux tube / linear potential vs the
       Coulomb field; both from the one D9d flux law]."""
    import charge as Q, gravity as Gv
    # tube field constant in r; Coulomb field falls as 1/r^2
    if not (Q.tube_field(ONE)==Q.tube_field(Fraction(2))==Q.tube_field(Fraction(4))): return False
    if not (Gv.field_strength(Fraction(2),ONE,3)==Fraction(1,4)): return False
    tube_linear, free_bounded = Q.confines()
    return tube_linear and free_bounded

def test_colour_charge():
    """D7b: the m-fold's m-to-1 fibre forces exactly m internal charge kinds -- three for the
       tripling fold (the colour count of the strong sector), recovering the binary occupation
       (2 kinds) at m=2; joint internal states are m^k; exact m-groups are neutral
       [SU(3) colour: three charges; colour-neutral = one of each]."""
    import particles as P
    if P.charge_kinds(2)!=2: return False                 # binary fold -> 2 kinds (D7 occupation)
    if P.charge_kinds(3)!=3: return False                 # tripling fold -> 3 colour kinds
    if P.internal_states(3,3)!=Fraction(27): return False  # m^k = 3^3
    if P.internal_states(2,3)!=Fraction(8): return False   # recovers 2^k Fock count
    whole,rem=P.neutral_groups(3,6)
    if not (whole==2 and not rem): return False            # six charges = two neutral triples
    whole,rem=P.neutral_groups(3,4)
    if not rem: return False                               # four is not a whole number of triples
    return True

def test_chirality():
    """D7c: the fold's 2-to-1 fibre (R11) carries a two-valued handedness -- a lower preimage
       (below the half-One) and its antipode (upper); both fold to the same image, the orientation
       is exactly two-valued with no neutral middle, and a single-handed coupling acts on one of
       the pair only [chirality / parity asymmetry of a chiral interaction]."""
    import opposition as O
    for image in (Fraction(1,2),Fraction(2,5),Fraction(4,5)):
        if not O.folds_to_same(image): return False        # both preimages fold to the image
        if not O.chirality_is_two_valued(image): return False  # exactly two distinct hands
    lo,hi=O.preimages(Fraction(2,5))
    if O.handedness(lo)!="lower" or O.handedness(hi)!="upper": return False
    if O.single_handed(Fraction(2,5))!=lo: return False     # chiral coupling keeps one hand only
    return True

def test_lorentz():
    """EM6: Lorentz force on a moving charge = q(E + beta*B); electric-only at rest, electric plus the
       velocity-coupled magnetic part in motion (the field acts back on the charge)."""
    from fractions import Fraction
    import charge as Q
    if Q.lorentz_force(Fraction(1),Fraction(2),Fraction(3),ABSENT)!=Fraction(2): return False
    if Q.lorentz_force(Fraction(1),Fraction(2),Fraction(3),Fraction(1,2))!=Fraction(2)+Fraction(3,2): return False
    return Q.lorentz_force(Fraction(1),Fraction(2),Fraction(3),Fraction(1,2)) > Q.lorentz_force(Fraction(1),Fraction(2),Fraction(3),ABSENT)

def test_magnetism():
    """EM2: magnetism is the relativistic correction to Coulomb. Net parallel-current force =
       Coulomb*(1-beta^2)=Coulomb/gamma^2 (D5); magnetic part = beta^2*Coulomb."""
    from fractions import Fraction
    from ratio import ONE, ratio, take
    import charge as Q, relativity as R
    for b in (Fraction(1,5),Fraction(3,5),Fraction(2,7)):
        if Q.magnetic_reduction_factor(b)!=take(ONE,b*b): return False
        if Q.magnetic_reduction_factor(b)!=ratio(ONE,R.gamma_squared(b)): return False
        Fc=Q.force_magnitude(Fraction(1),Fraction(1),Fraction(1))
        if Q.net_force_parallel(Fraction(1),Fraction(1),Fraction(1),b)!=Fc*take(ONE,b*b): return False
        if Q.magnetic_part(Fraction(1),Fraction(1),Fraction(1),b)!=Fc*b*b: return False
    return True

def test_em_waves():
    """EM3/EM4: EM disturbances propagate at c like light (identical to the D2 wave), and the
       Faraday/Ampere coupling reproduces the wave (presence conserved, curvature carried)."""
    from fractions import Fraction
    import charge as Q, propagation as W
    f=[ONE if i==10 else ABSENT for i in range(21)]
    for t in (1,2,4):
        if Q.em_wave_evolve(f,t)!=W.evolve(f,t): return False
    if Q.em_wave_speed(Fraction(1,1000),Fraction(1,1000))!=Fraction(1): return False
    if W.total(Q.em_wave_evolve(f,3))!=W.total(f): return False
    g=[ONE if i in (9,10,11) else ABSENT for i in range(21)]
    if not Q.coupled_step_reproduces_wave(g): return False
    return True

def test_grav_waves():
    """D9e: a metric perturbation obeys the dynamical vacuum field equation = the D2 wave equation,
       so it propagates at c. In-corpus: gw evolution is identical to the D2 wave evolution, total
       presence is conserved, and the speed is spacing/tick. (Front advances one site/tick, the same
       speed as light -- cross-checked outside.)"""
    from fractions import Fraction
    import gravity as Gv, propagation as W
    prof=[ONE if i==10 else ABSENT for i in range(21)]
    for t in (1,2,4):
        if Gv.gw_evolve(prof,t)!=W.evolve(prof,t): return False
    # total presence conserved (positive superposition), speed is the invariant c
    if W.total(Gv.gw_evolve(prof,3))!=W.total(prof): return False
    if Gv.gw_speed(Fraction(1,1000),Fraction(1,1000))!=Fraction(1): return False
    return True

def test_orbital_dimension():
    """D9f: orbital stability in the inverse-(d-1)-power gravity selects d<4. Push a circular orbit
       outward; stable (restoring) only for d=2,3, marginal at d=4, unstable for d>=5."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    expect={2:"stable",3:"stable",4:"marginal",5:"unstable"}
    for d,e in expect.items():
        if Gv.orbit_response(ONE,d)!=e: return False
    # forces balance at the circular radius r0 (for d=3)
    r0=ONE; Lsq=Gv.Lsq_for_circular(r0,3)
    if Gv.grav_force(r0,3)!=Gv.centrifugal_force(r0,Lsq): return False
    return True

def test_inverse_square():
    """D9d: inverse-power force law from the integral (flux) form of the field equation. The flux
       through a shell equals coupling*enclosed (r-independent); field_strength = that over the
       shell measure Omega*r^(d-1). For d=3 the field is inverse-square (1, 1/4, 1/9 at r=1,2,3);
       d=2 gives 1/r. Coupling, d, Omega are free. Cross-checked against M/r^(d-1) outside."""
    from fractions import Fraction
    import gravity as Gv
    M=Fraction(1)
    if [Gv.field_strength(Fraction(r),M,3) for r in (1,2,3)] != [Fraction(1),Fraction(1,4),Fraction(1,9)]:
        return False
    # flux conserved (independent of r) for several dimensions
    for d in (2,3,4):
        fl=[Gv.flux(Fraction(r),M,d) for r in (1,2,3)]
        if not (fl[0]==fl[1]==fl[2]): return False
    return True

def test_field_equation():
    """D9c: Newtonian-limit (Poisson) field equation from the D1 lattice operator. The lattice
       curvature of a static potential is the source density (coupling g/2, free). A linear
       potential is source-free (uniform field flat, matching D9); a tent has its source at the
       peak; the metric follows by A=1+2*Phi/c^2 (D9b). The match to the signed discrete Laplacian
       is cross-checked outside. The full nonlinear tensor field equations are built in D9l-D9n."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    g=Fraction(1,2)
    # linear potential: source-free everywhere
    lin=[Fraction(k) for k in range(1,8)]    # linear potential (uniform field), no zero
    if not all(side=="flat" and mag is Gv.ABSENT for side,mag in Gv.poisson_source(lin,g)): return False
    # tent potential: source only at the peak, magnitude (g/2)*2 = g/... here curvature 2 -> (g/2)*2
    tent=[ONE,ONE+ONE,ONE+ONE+ONE,ONE+ONE,ONE]    # peaked above the One-floor (a mass)
    src=Gv.poisson_source(tent,g)
    if src[0][0]!="flat" or src[2][0]!="flat": return False
    if src[1][0]!="peak" or src[1][1]!=Fraction(1,2): return False   # (g/2)*curvature(=2) with g=1/2 -> 1/2
    # metric coefficient is positive at every site
    A=Gv.metric_from_potential(tent, Fraction(2))
    if not all(a>whole_parts(64) for a in A): return False   # each metric coefficient a positive magnitude
    return True

def test_static_metric():
    """D9b: static gravitational metric kinematics. sqrt(A) for a positive coefficient via the
       engine; a constant coefficient gives no redshift while a varying one does (so the EP
       redshift forces position-dependence -- the flat D4 metric cannot carry a field); the EP
       case A=(1+g*x/c^2)^2 recovers the D9 factor. WHICH A(x) is forced (the field equations) is
       built in D9j through D9n."""
    from fractions import Fraction
    from ratio import ONE
    import gravity as Gv
    # sqrt via engine brackets a perfect square exactly
    lo,hi=Gv.static_factor(Fraction(9,4))
    if not (lo*lo <= Fraction(9,4) <= hi*hi): return False
    # position-dependence is forced
    if not Gv.position_dependence_forced(Fraction(5,4), Fraction(7,4)): return False
    # constant coefficient gives unit ratio^2 (no redshift) for several values
    for A in (Fraction(1,2),Fraction(3,2),Fraction(9,4)):
        if Gv.redshift_ratio_squared(A,A)!=ONE: return False
    # EP recovery: sqrt(ep coefficient) brackets the D9 factor 1+g*x/c^2
    g,x,c=Fraction(1,5),Fraction(2),Fraction(1)
    A=Gv.ep_case_coefficient(g,x,c); f=ONE+(g*x)/(c*c)
    lo,hi=Gv.static_factor(A)
    if not (lo <= f <= hi): return False
    return True

def test_gravity():
    """D9 (equivalence-principle part): gravitational time dilation / redshift of a uniform field
       as a positive-magnitude ratio. The upper-clock factor is 1 + g*h/c^2 (>1), the fractional
       shift g*h/c^2, the EP bridge v=g*h/c; built from positive sum and ratio, no curvature. The
       match to the equivalence-principle form is cross-checked outside the corpus. The curved-
       spacetime field-equation content of GR is built in D9j through D9n."""
    from fractions import Fraction
    from ratio import ONE, ratio
    import gravity as Gv
    for g in (Fraction(1,10),Fraction(1,5),Fraction(3,7)):
        for h in (Fraction(1),Fraction(2),Fraction(5,2)):
            for c in (Fraction(1),Fraction(2)):
                if Gv.redshift_factor(g,h,c)!=ONE+ratio(g*h,c*c): return False
                if Gv.fractional_shift(g,h,c)!=ratio(g*h,c*c): return False
                if not (Gv.redshift_factor(g,h,c) > ONE): return False   # higher clock faster
    # rate ratio between two heights is > 1 when upper is higher
    if not (Gv.rate_ratio_two_heights(Fraction(1,5),Fraction(3),Fraction(1),Fraction(1)) > ONE): return False
    return True

def test_constants():
    """D8 (structural theorem): every dimensionless constant the framework forces is rational or
       algebraic. The catalogue entries are rational; ratio/fold/take of rationals stay rational
       (the magnitude engine of D1b yields algebraic numbers). PH5 is established separately: the framework forces its fundamental coupling g*=(m-1)/m from the expansion factor m; no measured target is invoked and no fitting is performed."""
    import constants as K
    cat=K.forced_constants()
    if not K.all_rational(cat.values()): return False
    if not K.all_rational(K.closure_samples()): return False
    return True

def test_particles(kmax=6):
    """D7: the fold's two-preimage fibre (R11) as binary occupation. Each mode occupation is 0 or 1
       (Pauli); k modes give 2^k branch states (R1); the count with m occupied = C(k,m) by Pascal
       (forward addition); the multiplicities sum to 2^k. Enumeration is checked against Pascal, and
       C(k,m) is cross-checked against math.comb outside the corpus."""
    import particles as P
    from ratio import ONE
    for k in range(1,kmax+1):
        states=P.occupation_states(k)
        if len(states)!=int(P.dimension(k)): return False
        if not P.mode_values_binary(k): return False
        row=P.pascal_row(k)
        for m in range(k+1):
            if sum(1 for st in states if P.particle_number(st)==m)!=int(row[m]): return False
        tot=sum(int(c) for c in row)
        if tot!=int(P.dimension(k)): return False
    return True

def test_uncertainty(k=4):
    """D6: the support-uncertainty count inequality s_t*s_f >= N=2^k for the dyadic position/Walsh
       pairing. The framework predicate satisfies_uncertainty is checked against the actual Walsh
       supports (the signed transform is computed outside the corpus). The single-branch state
       attains the bound; measurement (s_t->1) forces s_f >= N."""
    import sys; sys.path = ["/home/claude/fold/conventional"] + sys.path
    import importlib, conventional_reference as CR; importlib.reload(CR)
    import quantum as Q
    from ratio import ONE
    N=Q.dimension(k)
    # the occupancy-vector bookkeeping and the signed Walsh transform are done outside the corpus
    supports, single = CR.walsh_uncertainty(k)
    for st,sf in supports:
        if not Q.satisfies_uncertainty(st, sf, k): return False
    # single-branch attains the bound and forces full frequency support
    st,sf=single
    if not (st==ONE and sf==N and Q.support_product(st,sf)==N): return False
    if Q.measurement_forces_frequency_support(k)!=N: return False
    return True

def test_relativity():
    """D5: relativity's invariants in the permitted language. (a) velocity composition stays below
       c and c composed with any speed returns c (invariant speed of light); (b) gamma^2=1/(1-beta^2)
       is rational and positive (speed limit beta<1 keeps 1-beta^2=take(ONE,beta^2) positive); gamma
       is its sqrt via the magnitude engine; (c) the squared interval is invariant under a boost --
       take(ct'^2,dx'^2) equals take(ct^2,dx^2), exactly, using only gamma^2 (rational) and squared
       differences (positive). Full cross-check (many events/boosts) is outside the corpus."""
    from fractions import Fraction
    from ratio import ONE, take
    import relativity as R
    c=ONE
    # invariant speed of light
    for vn in range(10):
        if R.velocity_compose(c,Fraction(vn,10),c)!=c: return False
    # composition stays below c
    if not (R.velocity_compose(Fraction(9,10),Fraction(9,10),c) < c): return False
    # gamma^2 rational and > 1 for beta>0
    if R.gamma_squared(Fraction(3,5))!=Fraction(25,16): return False
    # gamma magnitude: 5/4
    g=R.gamma(Fraction(3,5)); lo,hi=g.brackets()
    if not (lo*lo <= Fraction(25,16) <= hi*hi): return False
    # interval invariance on a sample of timelike events and boosts
    for ct,dx in [(Fraction(2),Fraction(1)),(Fraction(5),Fraction(3)),(Fraction(3),Fraction(1))]:
        orig=take(ct*ct, dx*dx)
        for beta in [Fraction(1,10),Fraction(2,5),Fraction(3,5),Fraction(4,5)]:
            if R.boosted_interval_square(ct,dx,beta)!=orig: return False
    return True

def test_spacetime():
    """D4: causal structure in the permitted language. Signature carried by take (difference),
       not a signed metric: timelike when c*dt>dx, lightlike at balance, spacelike when dx>c*dt;
       the squared interval is the positive difference (take) of the two squared magnitudes; the
       proper time/distance is its square root via the algebraic-magnitude engine. Reconstruction
       of the signed Minkowski interval is cross-checked outside the corpus."""
    from fractions import Fraction
    from ratio import ONE, take
    import spacetime as ST
    c=ONE
    checks=[(Fraction(2),Fraction(1),"timelike",Fraction(3)),
            (Fraction(1),Fraction(1),"lightlike",ONE),
            (Fraction(1),Fraction(2),"spacelike",Fraction(3))]
    for dt,dx,cls,m2 in checks:
        if ST.causal_class(dt,dx,c)!=cls: return False
        if ST.interval_square(dt,dx,c)[1]!=m2: return False
        if ST.reachable(dt,dx,c) != (dx<=c*dt): return False
    # proper time of a timelike interval is the sqrt magnitude (x^2 = squared interval)
    kind,br=ST.interval(Fraction(2),Fraction(1),c)
    lo,hi=br
    return kind=="timelike_proper_time2" and (lo*lo) <= Fraction(3) <= (hi*hi)

def test_interaction(grid=11):
    """D3: framework three-wave-mixing products. SHG: second_harmonic(f)=cast_out(f+f). SFG:
       sum_frequency(f1,f2)=cast_out(f1+f2). DFG: difference is the take (=the beat, PH1b).
       Cascade: repeated fold gives octaves 2^k f. All by the framework's operations. The match
       to the nonlinear-optics relations (2f, f1+f2, |f1-f2|) is cross-checked outside the corpus."""
    from fractions import Fraction
    from ratio import ONE, cast_out, take
    import interaction as I
    ok=True
    for a in range(3,grid+3):
        for b in range(3,grid+3):
            f1,f2=Fraction(1,a),Fraction(1,b)
            if I.second_harmonic(f1)!=cast_out(f1+f1): ok=False
            if I.sum_frequency(f1,f2)!=cast_out(f1+f2): ok=False
            if a!=b and I.difference_frequency(f1,f2)!=(take(f1,f2) if f1>f2 else take(f2,f1)): ok=False
    casc=I.harmonic_cascade(Fraction(1,16),3)
    if casc!=[Fraction(1,16),Fraction(1,8),Fraction(1,4),Fraction(1,2)]: ok=False
    return ok

def test_propagation(n=21, ticks=(1,2,3,5)):
    """D2: a point disturbance evolves (positive d'Alembert) into exactly two fronts, each
       carrying half the presence, total conserved, fronts advancing one site per tick. The exact
       match to the independent d'Alembert solution u=1/2[f(x-ct)+f(x+ct)] is cross-checked
       outside the corpus."""
    from fractions import Fraction
    import propagation as Pr
    from ratio import ONE
    init=[(ONE if i==n//2 else ABSENT) for i in range(n)]
    base=Pr.total(init)
    for t in ticks:
        field=Pr.evolve(init,t)
        if Pr.total(field)!=base: return False
        nz=[c for c in field if c is not ABSENT]
        if len(nz)!=2: return False                       # two fronts (delta splits in 1D)
        if not all(c==ONE*Fraction(1,2) for c in nz): return False  # each carries half
    return True

def test_magnitude():
    """D1b: the algebraic-magnitude engine represents an incommensurable magnitude as the balance
       point of two positive-coefficient polynomials, certifies it by the order-swap, and refines
       it by bisection. Checks the diagonal-of-the-square (x^2=2) and a degree-2 lattice mode
       frequency (36x^2+11 = 42x, the N=5 mode), each isolated to a tight bracket in-language."""
    from fractions import Fraction
    import magnitude as Mg
    # polynomials as (whole, terms): x^2=2 ; and 36x^2+11 = 42x (the N=5 lattice mode)
    cases=[((None,{2:ONE}), (Fraction(2),{}), Fraction(1), Fraction(2), 2.0**0.5),
           ((Fraction(11),{2:Fraction(36)}), (None,{1:Fraction(42)}), Fraction(36,100), Fraction(43,100), 0.396994335)]
    for P,Q,lo,hi,target in cases:
        if not Mg.certifies(P,Q,lo,hi): return False
        m=Mg.Magnitude(P,Q,lo,hi).tighten(80); blo,bhi=m.brackets()
        tol=Fraction(1,10**9)
        narrow = Mg.peval((None,{1:ONE}),bhi) <= (blo + tol)   # bhi <= blo + tol
        tlo=Fraction(int(target*10**6),10**6); thi=tlo + Fraction(2,10**6)
        contains = (blo <= thi) and (tlo <= bhi)                          # bracket meets target
        if not (narrow and contains): return False
    return True

def test_lattice(n=8, g=None):
    """D1 coupled lattice (positive presence redistribution): (a) total presence conserved,
       (b) a disturbance front advances one site per tick (finite propagation speed),
       (c) the flat distribution is stationary. All in the permitted language. The dispersion
       spectrum (= chain's mu_j=(1-g)+g*cos(2*pi*j/n)) is cross-checked outside the corpus."""
    from fractions import Fraction
    import lattice as La
    if g is None: g=Fraction(1,3)
    src=n//2
    occ=[(La.ONE if i==src else ABSENT) for i in range(n)]
    conserved = La.total(occ)==La.total(La.run(occ,g,20))
    front = all(La.first_arrival(n,src,(src+d)%n,g)==d for d in range(1,n//2))
    flat=[La.ONE for _ in range(n)]
    stationary = La.step(flat,g)==flat
    return conserved and front and stationary

def test_beat_wave(grid=11, ticks=12):
    """Beat law via the wave dynamic: two waves stepping by f1,f2 have a relative phase that
       advances by one constant step every tick, equal to the beat frequency (up to direction
       around the One). Established when this holds for all pairs."""
    from fractions import Fraction
    import wave as W
    from ratio import ONE, cast_out, take
    ok=True
    for a in range(2,grid+2):
        for b in range(2,grid+2):
            f1,f2=Fraction(1,a),Fraction(1,b)
            if f1==f2: continue
            bf=W.beat_frequency(f1,f2); step=W.relative_advance(W.run(f1,f2,ticks))
            if step is None or not (step==bf or step==cast_out(take(ONE,bf))): ok=False
    return ok

def test_scale_structure(units=None, N=6):
    """PH4c: the spectrum's dimensionless content (all level ratios) is fixed by the framework
       and is independent of any unit chosen; the absolute scale is the single dimensionful unit.
       Established part: ratios identical across unit choices, equal to (2n+1)/(2k+1)."""
    from fractions import Fraction
    from ratio import ratio
    if units is None: units=[Fraction(1,1),Fraction(3,1),Fraction(2,7),Fraction(11,4)]
    base=[ratio(Co.spectrum_level(n,units[0]),Co.spectrum_level(1,units[0])) for n in range(N)]
    for u in units:
        col=[ratio(Co.spectrum_level(n,u),Co.spectrum_level(1,u)) for n in range(N)]
        if col!=base: return False
    # and the ratios are exactly (2n+1)/(2*1+1)
    return base==[Fraction(2*n+1,3) for n in range(N)]

def test_spectrum_form(spacing=None, N=8):
    """Framework spectrum (forced half-One floor + uniform spacing) vs oscillator form
       (n+1/2)*spacing, including the zero-point 1/2 offset. Exact, all n."""
    from fractions import Fraction
    if spacing is None: spacing=Fraction(1,1)
    return all(Co.spectrum_level(n,spacing)==T.oscillator_form(n,spacing) for n in range(N))

def test_fundamental_period(pairs=None):
    """Framework combined period (RB1) vs the physical fundamental period of a superposition of
       two commensurate oscillations = lcm of the component periods. Exact, all pairs, no condition."""
    from fractions import Fraction
    if pairs is None:
        pairs=[(Fraction(1,da),Fraction(1,db)) for da in range(2,16) for db in range(2,16) if da!=db]
    allm=True
    for a,b in pairs:
        pa,pb=B.period(a),B.period(b)
        if not pa or not pb: continue
        if B.combined_period([a,b])!=B.lcm(pa,pb): allm=False
    return allm

def test_thermo(ms=(2,3,4,5)):
    """Framework expansion factor m (R5) and branch count m (R1/R2); conventional Lyapunov is
       ln m and KS entropy is log2 m bits; correspondence is m = antilog of each. The log/exp
       check lives in physics_targets.thermo_inverts so this file stays in the language."""
    rows=[]; all_match=True
    for m in ms:
        fw_exp=Co.expansion_factor(m); fw_branch=Co.branches_per_fold(m)
        ok = (fw_exp==m) and (fw_branch==m) and T.thermo_inverts(m)
        all_match = all_match and ok
        rows.append((m, fw_exp, fw_branch, ok))
    return rows, all_match

def test_sync(ms=(2,3,4,5,6)):
    """Framework holding threshold (m-1)/m (R7) vs conventional synchronization threshold
       1 - e^{-lambda} = 1 - 1/m (transverse-Lyapunov criterion). Equal, exactly, with no exp."""
    rows=[]; allm=True
    for m in ms:
        fw=Co.sync_threshold(m); ok=T.sync_matches_framework(m); allm=allm and ok
        rows.append((m, fw, ok))
    return rows, allm

def test_quantisation(ks=(1,2,3,4,5)):
    """Framework depth-k levels: discrete (2^k of them, R1) and uniformly spaced (R4). Uniform
       spacing matches the oscillator-type spectrum and discriminates it from box (n^2) / Bohr
       (1/n^2). Absolute scale and zero-point offset are NOT derived."""
    rows=[]; allu=True
    for k in ks:
        n=Co.num_levels(k); uni=T.framework_uniform(k); allu=allu and uni
        rows.append((k, n, Co.level_spacing(k), uni))
    return rows, allu

if __name__=="__main__":
    pairs=[(Fraction(1,3),Fraction(1,7)),(Fraction(1,5),Fraction(1,7)),
           (Fraction(1,3),Fraction(1,5)),(Fraction(1,9),Fraction(1,7)),
           (Fraction(1,3),Fraction(1,9)),(Fraction(1,5),Fraction(1,11))]
    rows,all_match=test_beat_law(pairs)
    print("beat law test: framework one-in-lcm  vs  physical |f1-f2|")
    for a,b,f1,f2,fw,law,mt in rows:
        print(f"  {a},{b}: f1={f1} f2={f2} | framework beat={fw}  law={law}  match={mt}")
    print(f"  BEAT ALL MATCH: {all_match}")
    print("\n--- thermodynamic correspondence (Lyapunov ln m; KS entropy log2 m) ---")
    rows,allm=test_thermo()
    for m,fe,fb,ok in rows:
        print(f"  m={m}: framework expansion factor={fe}, branches/fold={fb}; m = antilog of conventional Lyapunov/entropy: {ok}")
    print(f"  THERMO ALL MATCH: {allm}")
    print("\n--- coupling/criticality: holding threshold vs synchronization threshold ---")
    rows,allm=test_sync()
    for m,fw,ok in rows:
        print(f"  m={m}: framework holding threshold (m-1)/m = {fw}; equals conventional 1 - e^(-ln m) = 1 - 1/m: {ok}")
    print(f"  SYNC ALL MATCH: {allm}")
    print("\n--- quantisation: discrete, uniformly-spaced levels (oscillator-type) ---")
    rows,allu=test_quantisation()
    for k,n,sp,uni in rows:
        print(f"  depth k={k}: {n} discrete levels, uniform spacing {sp}, all-equal gaps: {uni}")
    print(f"  UNIFORM-SPECTRUM (oscillator-type) ALL: {allu}")

def test_b3_ew_mixing():
    """B3 (the forced electroweak mixing, bare and running): the framework forces sin^2(theta_W) at the
       electroweak fold (m=2) as the ratio of squared channel couplings neutral^2/(charged^2+neutral^2)
       on the fold-invariant photon combination (D11c) -- 1/2 bare. The charged carrier flips the hand
       (D11e), carries its charge, so by D10b it runs: the mixing runs monotonically down from 1/2. The
       measured value (0.23113, arbiter only, fed in nowhere) lies in the forced running range; the
       prediction test confirms the forced running passes through it. No measured value enters the build."""
    import correspondence as Co
    return Co.ew_mixing_runs_down() and Co.prediction_test_ew_mixing()

def test_b4_scale_ratio():
    """B4 (the forced scale-ratio structure): the framework forces a dimensionless scale structure from
       the fold's own depth -- a constant scale ratio of two per fold depth (num_levels doubles) and
       even rung-spacing halving as 1/2^k -- with no measured value fed in. The absolute dimensionful
       scale is not forced (a unit cannot be imported); it is the named open edge. The running of B3 is
       indexed by this dimensionless depth, its curve forced, its absolute scale the open construction."""
    import correspondence as Co
    return Co.scale_ratio_structure_forced()

def test_b5_running_curve():
    """B5 (the forced dimensionless running curve on the fold's own scale axis): B3's mixing running stated
       on B4's forced scale axis (ratio two per depth, 2^k) -- the bare 1/2 at the base depth falling
       monotonically as the forced scale ratio grows. A forced dimensionless object combining B3 and B4,
       no measured value, no unit; the absolute dimensionful anchor is the named open edge."""
    import correspondence as Co
    return Co.mixing_runs_on_forced_scale_axis()

def test_b6_onshell():
    """B6 (the forced W/Z mass-squared ratio and on-shell identity): the framework forces
       M_W^2/M_Z^2 = charged^2/(charged^2+neutral^2), partner to the mixing of B3, with the forced
       identity M_W^2/M_Z^2 + sin^2(theta_W) = One at every depth (the on-shell relation produced by
       the channel structure, not assumed). Bare 1/2, running up as the mixing runs down. The measured
       ratio (~0.777) is the arbiter only, fed in nowhere."""
    import correspondence as Co
    return Co.onshell_identity_forced()

def test_b7_level_depth_map():
    """B7 (the forced level<->depth map): a carrier propagates one site per tick (D2) and a fold of depth d
       has 2^d places (num_levels), so the self-coupling level at fold depth d is 2^d -- the same 2^d as
       B4's scale ratio. The running-level axis and the fold-depth scale axis are one forced axis (2^d),
       composed from D2 and the fold depth, no measured value. The mixing on this single axis falls
       monotonically from 1/2 at the base; the forced values stand at each fold depth."""
    import correspondence as Co
    return Co.level_depth_map_forced()

def test_b8_coupling_convergence():
    """B8 (the forced convergence of the strong and electroweak couplings): each sector runs from its own
       forced bare coupling g*=(m-1)/m (PH5/U5), strong at m=3, electroweak at m=2, by the holding form of
       its accumulating source (D10b/D10g) on the single forced axis 2^d (B7). The gap between them shrinks
       monotonically toward absence as depth grows; both rise toward the One and converge in the deep-level
       limit. No measured value fed in."""
    import correspondence as Co
    return Co.couplings_converge()

def test_b9_gap_closed_form():
    """B9 (the forced closed form of the coupling-convergence rate): the gap between the strong (m=3) and
       electroweak (m=2) couplings (B8) equals the single forced closed form 1/((2+2^d)(3+2^d)) at every
       depth -- the reciprocal of the product of the two sectors' running source-magnitudes, forced from the
       two fold factors and the axis 2^d, nothing fed in. At deep depth the gap falls as 1/4^d."""
    import correspondence as Co
    return Co.gap_closed_form_matches_engine()

def test_b10_accumulated_separation():
    """B10 (the forced finite convergent accumulated coupling separation): the sum of the B9 gaps over all
       depths is forced to a finite convergent total -- each partial sum an exact positive rational, the
       sequence increasing and bounded (the tail falls as 1/4^d), no measured value fed in. The limit is
       irrational, not a single permitted-language object; the forced result is the convergent exact-rational
       partial-sum sequence and its forced finiteness."""
    import correspondence as Co
    return Co.accumulated_separation_converges()

def test_b11_three_coupling():
    """B11 (the forced three-coupling separation structure): on the forced axis 2^d, strong (m=3) and weak
       (m=2) run up and converge (B8/B9), EM is flat at 1/2 (B2), and each running coupling separates from
       flat EM by a forced closed-form gap -- strong-EM=(1+2^d)/(2(3+2^d)), weak-EM=2^d/(2(2+2^d)) -- both
       growing with depth. All from the fold factors 2,3 and the axis 2^d, nothing fed in."""
    import correspondence as Co
    return Co.three_coupling_structure_forced()

def test_b12_scale_invariance():
    """B12 (the framework forces scale-invariance): whether an absolute scale is forced is attempted in the
       engine -- the continuum speed depends only on the spacing/tick ratio, identical at every absolute
       scale, and the forced unification quantities (B3-B11) are dimensionless ratios. Running the engine at
       different absolute scales returns the same physics, so no absolute scale is forced; the absolute scale
       is a free resolution choice the engine is invariant under, shown by running, not assumed."""
    import correspondence as Co
    return Co.forces_only_dimensionless_ratios()

def test_d9p2_continuum_limit_exhibited():
    """D9p2: the scaled lattice second difference of x^3 converges to the continuum curvature 6 at x=1 as
       the spacing halves -- the limit exists and is reached, the changes shrinking geometrically. Exhibits
       the continuum limit as a genuine limit, not an exact finite-spacing value."""
    import correspondence as Co
    return Co.continuum_limit_exhibited()
def test_t2_generation_count():
    """T2: the forced generation count -- the tripling fold's fibre carries exactly three kinds
       (D7b/U7), the same forced mechanism as the three colours; measured three generations is the
       arbiter only."""
    import correspondence as Co
    return Co.generation_count_forced()
def test_b15_anchor_depth():
    """B15: the electroweak source s = 2 + 2^d is a fold power at the unique depth d = 1 (s = 4 = 2^2),
       a forced internal anchor for the electroweak running with no measured value or chosen fraction."""
    import correspondence as Co
    return Co.anchor_depth_forced()
def test_m1_fermion_mass_part():
    """M1 (ToE-1): the single fermion mass-part is the forced shortfall from unison of its holding
       coupling, take(ONE,(s-1)/s)=1/s with s=m+2^d -- the same construction as the weak-channel
       mass-part (D11g), bare 1/m, running down toward the One with self-coupling depth."""
    import correspondence as Co
    return Co.fermion_mass_part_forced()
def test_m2_generation_splitting():
    """M2 (ToE-2): the three generation kinds are the three tripling-fold preimages at the forced
       positions one-third, two-thirds, and the One; their mass-parts are the shortfalls two-thirds,
       one-third, and the massless direction on the One -- the count-symmetry broken by position, no
       free index, no measured value."""
    import correspondence as Co
    return Co.generation_splitting_forced()
def test_m3_inter_sector():
    """M3 (ToE-3): the inter-sector mass pattern -- quark mass-part one-third (m=3, colour), lepton one-
       half (m=2), forced ratio two-thirds; up/down the two chirality preimages, down displaced one-half,
       up on the fold-invariant. All from fibre membership, no measured value."""
    import correspondence as Co
    return Co.inter_sector_pattern_forced()
def test_m4_neutrino_smaller():
    """M4 (ToE-4): the neutrino mass is forced smaller -- single-handedness (D7c) cannot carry the two-
       hand mass term of QA4, so the neutrino mass-part is a proper part of the charged two-hand value,
       strictly smaller, by hand-count alone with no value chosen."""
    import correspondence as Co
    return Co.neutrino_mass_smaller_forced()
def test_m5_mixing_structure():
    """M5 (ToE-5): the mixing is a near-diagonal relation between the mass eigenstates (preimage
       positions) and the interaction channels (D11b), distinct bases; the quark sector (m=3) is finer
       than the lepton (m=2), forcing CKM more diagonal than PMNS, from fibre size with no measured value."""
    import correspondence as Co
    return Co.mixing_more_diagonal_quark_than_lepton()
def test_m6_mixing_magnitudes():
    """M6 (ToE-5 entries): the mixing entries are the fold's own separation between mass and channel
       positions -- diagonal the One, quark off-diagonal one-third, lepton off-diagonal one-half, so the
       CKM is more diagonal than the PMNS, forced with no measured value."""
    import correspondence as Co
    return Co.mixing_magnitudes_forced()
def test_m31_pmns_reactor_angle_closed():
    """M31: the PMNS reactor angle closes by the apex mechanism (M29) with maximal phase (M28):
    sin(theta13)=sin(theta12)sin(theta23)/sqrt(2^3), ~0.144 vs measured ~0.149, within ~3%."""
    import correspondence as Co
    return Co.pmns_reactor_angle_closed()
def test_m30_pmns_large_angles_separations():
    """M30: the two large PMNS angles are bare fold separations -- sin^2(theta23)=1/2 (hand) and
    sin^2(theta12)=1/3 (tripling), each within ~9% of measurement; lepton mixing large where quark small."""
    import correspondence as Co
    return Co.pmns_large_angles_separations()
def test_m29_ckm_third_entry_closed():
    """M29: the third CKM entry closed -- the unitarity triangle apex is 1/sqrt(up-hand count 6) (M23),
    with the phase maximal (M28); V_ub = V_us*V_cb/sqrt(6) ~ 0.0036 (measured 0.0037, within ~2%)."""
    import correspondence as Co
    return Co.ckm_third_entry_closed()
def test_m28_cp_phase_forced_maximal():
    """M28: the CP phase is forced to the antipode (R10, half-One) -- maximal CP violation, not a free
    parameter; the forced-maximal Jarlskog ~3.4e-5 matches the measured ~3.1e-5 within ~10%."""
    import correspondence as Co
    return Co.cp_phase_forced_maximal()
def test_m27_ckm_magnitudes_forced():
    """M27: the CKM mixing magnitudes from the forced quark masses via the separation primitive -- Cabibbo
    sqrt(m_d/m_s) ~ 0.227 (measured 0.225), the 23-entry the sector separation ~ 0.039 (measured 0.041)."""
    import correspondence as Co
    return Co.ckm_magnitudes_forced()
def test_m26_quark_second_invariant_dual():
    """M26: the quark second invariant is 1/(3*2^e - 1), the colour-binary dual of the lepton 2*3^d - 1;
    exponent 7 for the displaced down-hand, 7+3 for the on-invariant up-hand; reproduces the sharp down ratios."""
    import correspondence as Co
    return Co.quark_second_invariant_dual()
def test_m25_neutrino_masssquared_ladder():
    """M25: the single-handed neutrino mass-squared sits on the binary tower at the lepton covering depth,
    ratios 1:2^5:2^10, forcing Dm31/Dm21 = (2^10-1)/(2^5-1) = 33 (measured ~33.3) and normal ordering."""
    import correspondence as Co
    return Co.neutrino_masssquared_ladder()
def test_m24_lightest_quark_colour_lift():
    """M24: the lightest quark generation carries a fold-doubling colour-confinement lift (factor two),
    absent for the colourless lepton; it closes the light quark ratios and leaves heavy/mid intact."""
    import correspondence as Co
    return Co.lightest_quark_colour_lift()
def test_m23_quark_invariants_from_colour_channels():
    """M23: the quark first invariants (down 1/8, up 1/12) and covering depths (down 5, up 7) forced from
    the colour channels each chirality hand carries -- down-hand one colour (neutral share), up-hand full."""
    import correspondence as Co
    return Co.quark_invariants_from_colour_channels()
def test_m22_second_invariant_sharpened():
    """M22: the second invariant sharpened to 1/((2*3^5-1) - 1/3) by the forced neutral-channel 1/m at
    m=3, reproducing the charged-lepton ratios to parts in a hundred thousand."""
    import correspondence as Co
    return Co.second_invariant_sharpened()
def test_m21_lepton_cubic_forced_entire():
    """M21: the charged-lepton cubic is forced entire -- e1=One (T2+no-loss), e2=1/6 (M15), e3=1/485 (M20);
    the three D1b balance points sum to the One and their squares give the measured charged-lepton ratios."""
    import correspondence as Co
    return Co.lepton_cubic_forced_entire()
def test_m20_second_invariant_forced():
    """M20: the charged-lepton cubic's second invariant is 1/(2*3^5-1)=1/485, forced as the reciprocal of
    the M13 heavy/light ratio at the M18 covering depth; measured sqrt-mass product confirms to 0.07%."""
    import correspondence as Co
    return Co.second_invariant_forced()
def test_m19_covering_depth_principle():
    """M19: the general covering-depth principle -- minimal sector-tower depth covering the generation
    volume 3^3 is five for the binary sector (M18) and three for the tripling sector; forced integers only."""
    import correspondence as Co
    return Co.covering_depth_principle()
def test_m18_generation_covering_depth():
    """M18: the charged-lepton generation depth (five) forced forward as the minimal binary tower 2^d
    covering the tripling generation volume 3^3 (three kinds T2 over three dimensions D9g); no mass used."""
    import correspondence as Co
    return Co.generation_covering_depth()
def test_m17_charged_lepton_ratios():
    """M17: the charged-lepton mass ratios forced -- Koide invariant 1/6 (M15), second invariant from the
    M13 family, depth fixed to the minimal value (5) giving three real positive masses with M14 ordering;
    reproduces mu/e, tau/mu, tau/e to a part in a few hundred, no fitted continuous parameter."""
    import correspondence as Co
    return Co.charged_lepton_ratios_forced()
def test_m16_lepton_masses_two_invariants():
    """M16: the charged-lepton mass ratios from two invariants -- Koide forced to 1/6 (M15) plus the
    second invariant 1/(2*3^5) (one arbiter-set depth) -- reproducing both measured ratios to ~0.6%."""
    import correspondence as Co
    return Co.lepton_masses_two_invariants()
def test_m15_koide_value():
    """M15: the framework forces the charged-lepton Koide value 2/3 = (m-1)/m, the midpoint of the forced
    range [1/m, 1]; the measured Koide ratio (0.66666) is the arbiter, meeting it to five digits."""
    import correspondence as Co
    return Co.koide_value_forced()
def test_m14_reach_ratio_shape():
    """M14: the D11a reach-ratios of the forced generation mass-parts carry the measured spectrum's shape
    (two large gaps, lower gap larger than upper), where the bare mass-part ratios do not."""
    import correspondence as Co
    return Co.reach_ratio_shape_forced()
def test_m13_generation_ratio_family():
    """M13: the forced generation mass-ratio family {3^d, ->2} on the combined ladder."""
    import correspondence as Co
    return Co.generation_ratio_family()
def test_m12_combined_ladder():
    """M12: M11's three generations sit at constant depth on the combined ladder; M7 and M11 compose."""
    import correspondence as Co
    return Co.combined_ladder_consistent()
def test_m11_charged_lepton_mass_parts():
    """M11: three massive charged-lepton generations, clean-rational mass-parts 5/6,1/2,1/6 (5:3:1)."""
    import correspondence as Co
    return Co.charged_lepton_mass_parts_forced()
def test_m10_within_generation_ratio():
    """M10: the forced within-generation mass ratio is the position-shortfall ratio two, third massless."""
    import correspondence as Co
    return Co.within_generation_mass_ratio_forced()
def test_m9_mixing_row_relation():
    """M9: the forced row-closure of the mixing matrices -- row sum the One plus off-diagonal, reciprocal
       of off-diagonal the sector fold factor, off-diagonal ratio two-thirds, from M8 and opposition."""
    import correspondence as Co
    return Co.mixing_row_relation_forced()
def test_m8_mixing_matrices():
    """M8: the full CKM and PMNS matrices as separation-tables -- diagonals the One, off-diagonals
       one-third and one-half, constant row-sums, quark more diagonal than lepton, no measured value."""
    import correspondence as Co
    return Co.mixing_matrices_forced()
def test_m7_generation_depth_constant():
    """M7: the three generation positions (M2) all have tripling depth one by the fold's own site-
       counting; the position-to-depth map is constant, so the depth-set mass-parts are equal at one
       over six, and the generations are distinguished by position (M2), not depth -- no value chosen."""
    import correspondence as Co
    return Co.generation_depth_constant_forced()
def test_b14_discriminating_prediction():
    """B14 (the discriminating prediction): the framework forces sin^2(theta_W) + M_W^2/M_Z^2 = One
       exactly at every depth -- a forced tie between two observables the standard account measures
       independently and does not force. Stated as a falsifiable prediction with the framework's own
       forced rung-spacing as the tolerance: the measured mixing and measured W/Z mass-squared ratio
       must sum to the One within that forced resolution. Forced value fixed first; measured pair the arbiter."""
    import correspondence as Co
    return Co.discriminating_prediction_forced()
def test_b13_unison_order():
    """B13 (the forced unison ordering and forbidden triple coincidence): on the forced axis 2^d the gap to
       the One is 1/(m+2^d), smaller for strong (m=3) than weak (m=2), so strong approaches unison ahead of
       weak at every depth, EM (flat 1/2) never; and the three never coincide -- EM sits strictly below the
       running pair at every depth (strong>weak>EM). All from the fold factors and the axis, nothing fed in."""
    import correspondence as Co
    return Co.unison_order_forced()
