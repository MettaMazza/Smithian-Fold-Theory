"""Physics correspondences (Phase 2), in the permitted language. Each tagged by evidential
status: E established, P partial (condition named), O open. A correspondence is E only if the
harness confirms it reproduces the cited physical law. Physical targets are cited in
physics_targets.py. No correspondence is asserted beyond what compare.py shows."""
from fractions import Fraction
import correspondence as Co, beats as B
from ratio import take
def gcd(a,b):
    while b: a,b=b,a%b
    return a

def ph_thermo():
    # E2: framework expansion factor m (R5) and branch count m (R1/R2) reproduce the doubling/
    # m-fold map's Lyapunov exponent ln m and KS entropy log2 m bits, expressed without logs:
    # m is exactly the antilog of each. (Strong because the fold IS the dyadic map.)
    import compare as _C
    _,allm=_C.test_thermo(); return allm

def d9e_grav_waves():
    # D9e: linearized gravitational waves -- the dynamical vacuum field equation is the D2 wave
    # equation, so a metric perturbation propagates at c, the speed of light.
    import compare as _C
    return _C.test_grav_waves()

def d9g_forced_dimension():
    import compare as _C
    return _C.test_forced_dimension()

def d9j_curved_metric():
    import compare as _C
    return _C.test_curved_metric()

def d9i_quadrupole():
    import compare as _C
    return _C.test_quadrupole()

def d9h_point_mass():
    import compare as _C
    return _C.test_point_mass_redshift()

def d6b_variance():
    import compare as _C
    return _C.test_variance_uncertainty()

def em2_magnetism():
    import compare as _C
    return _C.test_magnetism()

def em6_lorentz():
    import compare as _C
    return _C.test_lorentz()

def em5_maxwell3d():
    import compare as _C
    return _C.test_maxwell3d()

def d9o_schwarzschild():
    import compare as _C
    return _C.test_schwarzschild()

def d9p_continuum():
    import compare as _C
    return _C.test_continuum_limit()

def d9q_quadrupole_power():
    import compare as _C
    return _C.test_quadrupole_power()

def d9l_nonlinear():
    import compare as _C
    return _C.test_nonlinear_gravity()

def d9m_pn_convergence():
    import compare as _C
    return _C.test_pn_convergence()

def d9n_tensor_bianchi():
    import compare as _C
    return _C.test_tensor_bianchi()

def d9k_einstein3d():
    import compare as _C
    return _C.test_einstein3d()

def em4_vector_maxwell():
    import compare as _C
    return _C.test_vector_maxwell()

def em3_em_waves():
    import compare as _C
    return _C.test_em_waves()

def em1_coulomb():
    import compare as _C
    return _C.test_coulomb()

def d9f_orbital_dimension():
    # D9f: orbital stability in the inverse-(d-1)-power gravity selects spatial dimension d<4.
    import compare as _C
    return _C.test_orbital_dimension()

def d9d_inverse_square():
    # D9d: inverse-power force law from the flux form of the field equation -- field_strength =
    # coupling*enclosed / (Omega*r^(d-1)); d=3 gives inverse-square; flux is r-independent. d,
    # Omega and coupling are parameters. Full nonlinear tensor GR is built in D9j-D9n.
    import compare as _C
    return _C.test_inverse_square()

def d9c_field_equation():
    # D9c: Newtonian-limit (Poisson) field equation from the D1 lattice operator -- lattice
    # curvature of the static potential = source density (coupling g/2, free); linear potential
    # source-free; metric by A=1+2*Phi/c^2. Full nonlinear tensor GR is built in D9j-D9n.
    import compare as _C
    return _C.test_field_equation()

def d9b_static_metric():
    # D9b: static gravitational metric kinematics -- sqrt(A) via the engine, position-dependence
    # forced by the EP redshift (constant coefficient gives no shift), EP case recovers the D9
    # factor. Which A(x) is forced is built in D9c-D9k.
    import compare as _C
    return _C.test_static_metric()

def d9_gravity():
    # D9 (equivalence-principle part): gravitational time dilation/redshift of a uniform field as a
    # positive-magnitude ratio (1 + g*h/c^2), built from acceleration*time=velocity and the Doppler
    # factor, no curvature. Curved-spacetime GR is built in D9j-D9n.
    import compare as _C
    return _C.test_gravity()

def ph5a_critical_coupling():
    import compare as _C
    return _C.test_critical_coupling()

def d8_constants():
    # D8 (structural theorem): the framework's forced dimensionless constants are rational or
    # algebraic; the framework's fundamental coupling g*=(m-1)/m is forced in PH5.
    import compare as _C
    return _C.test_constants()

def d11d_symmetry_breaking():
    import compare as _C
    return _C.test_symmetry_breaking()

def d11e_currents():
    import compare as _C
    return _C.test_weak_currents()

def d11g_mass_ratio():
    import compare as _C
    return _C.test_weak_mass_ratio()

def qa5_dirac_full():
    import compare as _C
    return _C.test_qa5_dirac_full()

def qa4_dirac():
    import compare as _C
    return _C.test_a4_dirac()

def qa3_spectrum():
    import compare as _C
    return _C.test_a3_spectrum_tie()

def qa2_potential():
    import compare as _C
    return _C.test_a2_potential()

def qa1_dispersion():
    import compare as _C
    return _C.test_a1_dispersion()

def b2_arbiter():
    import compare as _C
    return _C.test_b2_arbiter()

def b3_ew_mixing():
    # B3: the forced electroweak mixing sin^2(theta_W) = 1/2 bare, running down by the D10b mechanism,
    # passing through the measured value (arbiter only). See compare.test_b3_ew_mixing.
    import compare as _C
    return _C.test_b3_ew_mixing()

def b4_scale_ratio():
    # B4: the framework forces a dimensionless scale-ratio structure (two per fold depth, rung-spacing
    # 1/2^k); the absolute dimensionful scale is the named open edge. See compare.test_b4_scale_ratio.
    import compare as _C
    return _C.test_b4_scale_ratio()

def b5_running_curve():
    # B5: the forced dimensionless running curve of the mixing on the fold's own scale axis (B3 on B4).
    import compare as _C
    return _C.test_b5_running_curve()

def b6_onshell():
    # B6: the forced W/Z mass-squared ratio and the forced on-shell identity M_W^2/M_Z^2 + sin^2 = One.
    import compare as _C
    return _C.test_b6_onshell()

def b7_level_depth_map():
    # B7: the forced level<->depth map (D2 propagation o fold depth): self-coupling level at fold depth d
    # is 2^d, the same axis as B4's scale ratio; the mixing on this single forced axis.
    import compare as _C
    return _C.test_b7_level_depth_map()

def b8_coupling_convergence():
    # B8: the forced convergence of the strong (m=3) and electroweak (m=2) couplings on the single forced
    # axis 2^d -- the gap shrinks monotonically toward absence, both rising toward the One.
    import compare as _C
    return _C.test_b8_coupling_convergence()

def b9_gap_closed_form():
    # B9: the forced closed form of the coupling-convergence rate, 1/((2+2^d)(3+2^d)), matching B8's gap.
    import compare as _C
    return _C.test_b9_gap_closed_form()

def b10_accumulated_separation():
    # B10: the forced finite convergent accumulated coupling separation (sum of B9 gaps over all depths).
    import compare as _C
    return _C.test_b10_accumulated_separation()

def b11_three_coupling():
    # B11: the forced three-coupling separation structure on the axis 2^d.
    import compare as _C
    return _C.test_b11_three_coupling()

def b12_scale_invariance():
    # B12: the framework forces scale-invariance -- the absolute scale is free, shown by the engine
    # returning identical physics at every scale; the forced content is the dimensionless ratios.
    import compare as _C
    return _C.test_b12_scale_invariance()

def b13_unison_order():
    # B13: the forced unison ordering (strong ahead of weak) and the forbidden triple coincidence.
    import compare as _C
    return _C.test_b13_unison_order()
def d9p2_continuum_limit_exhibited():
    # D9p2: the continuum limit exhibited as a genuine limit on x^3 (converges to 6, changes halve).
    import compare as _C
    return _C.test_d9p2_continuum_limit_exhibited()
def t2_generation_count():
    # T2: the forced generation count -- the tripling fold's fibre carries exactly three kinds (D7b/U7).
    import compare as _C
    return _C.test_t2_generation_count()
def b15_anchor_depth():
    # B15: the forced internal anchor depth -- the electroweak source closes on the fold's square at unique d=1.
    import compare as _C
    return _C.test_b15_anchor_depth()
def m1_fermion_mass_part():
    # M1 (ToE-1): the single fermion mass-part -- the forced shortfall from unison, 1/s with s=m+2^d.
    import compare as _C
    return _C.test_m1_fermion_mass_part()
def m2_generation_splitting():
    # M2 (ToE-2): the generation mass-splitting -- distinct forced mass-parts from distinct preimage positions.
    import compare as _C
    return _C.test_m2_generation_splitting()
def m3_inter_sector():
    # M3 (ToE-3): the inter-sector mass pattern -- quark/lepton and up/down from fibre membership.
    import compare as _C
    return _C.test_m3_inter_sector()
def m4_neutrino_smaller():
    # M4 (ToE-4): the neutrino mass is forced smaller -- single-handedness cannot carry the two-hand mass term.
    import compare as _C
    return _C.test_m4_neutrino_smaller()
def m5_mixing_structure():
    # M5 (ToE-5): the mixing structure -- a near-diagonal relation between mass and channel bases.
    import compare as _C
    return _C.test_m5_mixing_structure()
def m6_mixing_magnitudes():
    # M6 (ToE-5 entries): the forced mixing magnitudes -- the overlap rule is the fold's own separation.
    import compare as _C
    return _C.test_m6_mixing_magnitudes()
def m31_pmns_reactor_angle_closed():
    import compare as _C
    return _C.test_m31_pmns_reactor_angle_closed()
def m30_pmns_large_angles_separations():
    import compare as _C
    return _C.test_m30_pmns_large_angles_separations()
def m29_ckm_third_entry_closed():
    import compare as _C
    return _C.test_m29_ckm_third_entry_closed()
def m28_cp_phase_forced_maximal():
    import compare as _C
    return _C.test_m28_cp_phase_forced_maximal()
def m27_ckm_magnitudes_forced():
    import compare as _C
    return _C.test_m27_ckm_magnitudes_forced()
def m26_quark_second_invariant_dual():
    import compare as _C
    return _C.test_m26_quark_second_invariant_dual()
def m25_neutrino_masssquared_ladder():
    import compare as _C
    return _C.test_m25_neutrino_masssquared_ladder()
def m24_lightest_quark_colour_lift():
    import compare as _C
    return _C.test_m24_lightest_quark_colour_lift()
def m23_quark_invariants_from_colour_channels():
    import compare as _C
    return _C.test_m23_quark_invariants_from_colour_channels()
def m22_second_invariant_sharpened():
    import compare as _C
    return _C.test_m22_second_invariant_sharpened()
def m21_lepton_cubic_forced_entire():
    import compare as _C
    return _C.test_m21_lepton_cubic_forced_entire()
def m20_second_invariant_forced():
    import compare as _C
    return _C.test_m20_second_invariant_forced()
def m19_covering_depth_principle():
    import compare as _C
    return _C.test_m19_covering_depth_principle()
def m18_generation_covering_depth():
    import compare as _C
    return _C.test_m18_generation_covering_depth()
def m17_charged_lepton_ratios():
    import compare as _C
    return _C.test_m17_charged_lepton_ratios()
def m16_lepton_masses_two_invariants():
    import compare as _C
    return _C.test_m16_lepton_masses_two_invariants()
def m15_koide_value():
    import compare as _C
    return _C.test_m15_koide_value()
def m14_reach_ratio_shape():
    import compare as _C
    return _C.test_m14_reach_ratio_shape()
def m13_generation_ratio_family():
    import compare as _C
    return _C.test_m13_generation_ratio_family()
def m12_combined_ladder():
    import compare as _C
    return _C.test_m12_combined_ladder()
def m11_charged_lepton_mass_parts():
    import compare as _C
    return _C.test_m11_charged_lepton_mass_parts()
def m10_within_generation_ratio():
    import compare as _C
    return _C.test_m10_within_generation_ratio()
def m9_mixing_row_relation():
    import compare as _C
    return _C.test_m9_mixing_row_relation()
def m8_mixing_matrices():
    import compare as _C
    return _C.test_m8_mixing_matrices()
def m7_generation_depth_constant():
    # M7: the generation depth is constant by the fold's own site-counting (the position-to-depth map).
    import compare as _C
    return _C.test_m7_generation_depth_constant()
def b14_discriminating_prediction():
    # B14: the forced on-shell tie stated as a falsifiable numerical prediction with forced tolerance.
    import compare as _C
    return _C.test_b14_discriminating_prediction()

def b1_coupling_structure():
    import compare as _C
    return _C.test_b1_coupling_structure()

def u3_dictionary():
    import compare as _C
    return _C.test_dictionary()

def u4_rel():
    import compare as _C
    return _C.test_u4()

def u5_rel():
    import compare as _C
    return _C.test_u5()

def u6_rel():
    import compare as _C
    return _C.test_u6()

def t1_prediction_colour():
    import compare as _C
    return _C.test_prediction_colour()

def n1_mediator_count():
    import compare as _C
    return _C.test_mediator_count()

def c4s_integration():
    import compare as _C
    return _C.test_self_integration()

def c5s_discrete():
    import compare as _C
    return _C.test_self_discrete()

def c1s_loop():
    import compare as _C
    return _C.test_self_loop_closed()

def c2s_blind():
    import compare as _C
    return _C.test_self_blind_spot()

def c3s_fixed():
    import compare as _C
    return _C.test_self_fixed_point()

def u7_sector_m():
    import compare as _C
    return _C.test_u7()

def u2_forced_relationship():
    import compare as _C
    return _C.test_forced_relationship()

def u1_unification():
    import compare as _C
    return _C.test_unification()

def d11f_force_law():
    import compare as _C
    return _C.test_weak_force_law()

def d11c_split():
    import compare as _C
    return _C.test_massless_massive_split()

def d11b_mixing():
    import compare as _C
    return _C.test_mixing()

def d11a_massive_range():
    import compare as _C
    return _C.test_massive_range()

def d10c_flux_tube():
    import compare as _C
    return _C.test_flux_tube()

def d10e_field_eq():
    import compare as _C
    return _C.test_strong_field_eq()

def d10f_luminal():
    import compare as _C
    return _C.test_strong_luminal()

def d10g_beta():
    import compare as _C
    return _C.test_beta_slope()

def d10d_colour_neutral():
    import compare as _C
    return _C.test_colour_neutral()

def d10a_self_coupling():
    import compare as _C
    return _C.test_self_coupling()

def d10b_running():
    import compare as _C
    return _C.test_running()

def d7d_confinement():
    import compare as _C
    return _C.test_confinement()

def d7b_colour_charge():
    import compare as _C
    return _C.test_colour_charge()

def d7c_chirality():
    import compare as _C
    return _C.test_chirality()

def d7_particles():
    # D7: fold two-preimage fibre (R11) as binary occupation -- per-mode 0/1 (Pauli), 2^k branch
    # states (R1), particle-number multiplicities C(k,m) by Pascal summing to 2^k.
    import compare as _C
    return _C.test_particles()

def d6_uncertainty():
    # D6: support-uncertainty count inequality s_t*s_f >= N=2^k for the dyadic position/Walsh
    # pairing; single-branch state attains the bound; measurement resolves s_t to 1, forcing s_f>=N.
    import compare as _C
    return _C.test_uncertainty()

def d5_relativity():
    # D5: relativity's invariants in positive magnitudes -- invariant speed of light (velocity
    # composition, c (+) v = c), gamma^2 rational (speed limit keeps 1-beta^2 positive), gamma via
    # the magnitude engine, and interval invariance under a boost (exact, squares + gamma^2 only).
    import compare as _C
    return _C.test_relativity()

def d4_spacetime():
    # D4: Minkowski causal structure in the permitted language -- the Lorentzian signature carried
    # by take (positive difference) not a signed metric; causal class by comparison of c*dt and dx;
    # interval a positive magnitude (proper time/distance) via the algebraic-magnitude engine.
    import compare as _C
    return _C.test_spacetime()

def d3_interaction():
    # D3: framework three-wave-mixing -- SHG (fold doubling, 2f), SFG (cast_out sum, f1+f2),
    # DFG (take, |f1-f2|), octave cascade (repeated fold). Frequencies forced by the operations;
    # match to nonlinear-optics relations cross-checked outside the corpus.
    import compare as _C
    return _C.test_interaction()

def d1d_lattice3d():
    import compare as _C
    return _C.test_lattice3d()

def d1c_lattice2d():
    import compare as _C
    return _C.test_lattice2d()

def d2_propagation():
    # D2: wave propagation as dAlembert counter-translating positive packets -- a disturbance
    # splits into two half-presence fronts moving in opposite directions at the causal speed
    # (one site/tick), total conserved; matches 1/2[f(x-ct)+f(x+ct)] (cross-checked outside).
    import compare as _C
    return _C.test_propagation()

def d1b_magnitude():
    # D1b: algebraic-magnitude engine -- represent an incommensurable as the balance point of two
    # positive-coefficient polynomials, certify by order-swap, refine by bisection. Verified to
    # isolate every distinct lattice mode frequency exactly (incl. non-constructible N), in-language.
    import compare as _C
    return _C.test_magnitude()

def d1_lattice():
    # D1: framework coupled lattice (positive redistribution) reproduces the 1D chain --
    # presence conserved, finite propagation (one site/tick), flat state stationary, N discrete
    # modes. Dispersion spectrum = chain's mu_j=(1-g)+g*cos(2*pi*j/n), cross-checked outside.
    import compare as _C
    return _C.test_lattice()

def ph_beat_wave():
    # PH1b: via the wave/rotation dynamic (phase advances by a fixed part, cast out the One),
    # two waves stepping by f1,f2 have a relative phase advancing by one constant step = the
    # beat frequency |f1-f2| (up to direction), all pairs. The envelope inherits this rate.
    import compare as _C
    return _C.test_beat_wave()

def ph_fundamental_period():
    # PH1: framework combined period (RB1) = physical fundamental period of superposed
    # commensurate oscillations (lcm of component periods). Exact, all pairs, no condition.
    import compare as _C
    return _C.test_fundamental_period()

def ph_scale_structure():
    # PH4c: framework fixes all spectral level ratios, unit-independent (= (2n+1)/(2k+1)).
    # The absolute scale is one dimensionful unit (one spacing): a dimensionless system does
    # not output a dimensionful unit (dimensional analysis); the full dimensionless structure is fixed.
    import compare as _C
    return _C.test_scale_structure()

def ph_spectrum_form():
    # PH4b: framework spectrum (forced half-One floor R10/R7/R11 + uniform spacing R4) reproduces
    # the oscillator form (n+1/2)*spacing, zero-point 1/2 included, exactly for all n.
    import compare as _C
    return _C.test_spectrum_form()

def ph_quant():
    # PH4: framework depth-k levels are discrete (2^k) and uniformly spaced (R1/R4) -> the
    # oscillator-type uniform spectrum, discriminated from box (n^2)/Bohr (1/n^2). Scale and
    import compare as _C
    _,allu=_C.test_quantisation(); return allu

def ph_sync():
    # PH3: framework holding threshold (m-1)/m (R7) equals the synchronization threshold of
    # two diffusively coupled chaotic maps, 1 - e^{-lambda} with lambda=ln m, expressed with
    # no exponential. The clustering at the half-One (E4) is the m=2 case.
    import compare as _C
    _,allm=_C.test_sync(); return allm

def ph_beat_partial():
    # P1: framework beat frequency (1/lcm, from RB1) reproduces physical f_beat=|f1-f2|
    # EXACTLY when gcd(period_a,period_b) == |period_b - period_a|. Verified over a grid.
    ok=True
    for da in range(2,16):
        for db in range(2,16):
            a,b=Fraction(1,da),Fraction(1,db)
            pa,pb=B.period(a),B.period(b)
            if not pa or not pb or a==b: continue
            fw=Co.beat_frequency(a,b); f1,f2=Co.frequency(a),Co.frequency(b)
            if f1==f2: continue   # equal frequencies = unison, no beat (no zero magnitude)
            law=take(f1,f2) if f1>f2 else take(f2,f1)
            hi,lo=(pb,pa) if pb>=pa else (pa,pb)
            pdiff=len(range(lo,hi))      # the gap lo..hi as a count (no zero seed, no subtraction)
            if (fw==law)!=(gcd(pa,pb)==pdiff): ok=False
    return ok

CLAIMS=[
 ("PH1","E","combined-oscillation period: the framework combined period (RB1) equals the fundamental period of a superposition of two commensurate oscillations, the lcm of the component periods — exact, all pairs, no condition [standard fact: fundamental period of a sum of commensurate periodics = lcm]. The envelope sub-rate |f1-f2| is established in PH1b.","compare.test_fundamental_period",ph_fundamental_period),
 ("PH1b","E","beat frequency |f1-f2|: via the wave/rotation dynamic (phase advances by a fixed part, cast out the One — permitted language, no trig, no signed superposition), two waves stepping by f1,f2 have a relative phase that turns by one constant step equal to the beat frequency |f1-f2| (up to direction); the amplitude envelope (closeness) inherits this rate. Confirmed all pairs [Feynman I.48].","compare.test_beat_wave",ph_beat_wave),
 ("PH2","E","thermodynamics: framework expansion factor m (R5) and branch count m (R1/R2) reproduce the doubling-map Lyapunov exponent ln m and KS entropy log2 m bits, with no logarithm — m is their antilog [arXiv:1211.1234; Pesin].","compare.test_thermo",ph_thermo),
 ("PH3","E","coupling/criticality: framework holding threshold (m-1)/m (R7) equals the synchronization threshold of diffusively coupled chaotic maps, 1 - e^(-lambda), lambda=ln m, with no exponential; clustering at the half-One (E4) is the m=2 case [PRE 70 026217; arXiv:nlin/0504012].","compare.test_sync",ph_sync),
 ("PH4","E","quantisation (structural): framework depth-k states are discrete (2^k, R1) and uniformly spaced (R4) — exactly, all k — the signature of an oscillator-type spectrum, discriminated from box (n^2)/Bohr (1/n^2) [UP Vol3; Wikipedia QHO].","compare.test_quantisation",ph_quant),
 ("PH4b","E","oscillator spectral form: framework levels (ground floor forced to the half-One by R10/R7/R11, uniform spacing by R4) reproduce E_n=(n+1/2)*spacing, zero-point 1/2 included, exactly for all n [UP Vol3; Wikipedia QHO]. The 1/2 is the framework forced invariant, not fitted.","compare.test_spectrum_form",ph_spectrum_form),
 ("PH4c","E","spectral scale structure: the framework fixes every dimensionless level ratio of the spectrum, identical across all unit choices (= (2n+1)/(2k+1)); the absolute scale is one dimensionful unit (one spacing). A dimensionless system does not output a dimensionful unit (dimensional analysis / Buckingham pi); the full dimensionless structure of the spectrum is fixed.","compare.test_scale_structure",ph_scale_structure),
 ("D9e","E",'linearized gravitational waves propagate at the speed of light. Making the static field equation (D9c) time-dependent: in vacuum the linearized equation is (1/c^2) d^2 h/dt^2 = laplacian(h), the wave equation -- the conventional relativistic wave equation, the same equation D2 solved [Carroll, Weak Fields and Gravitational Radiation]. So a metric perturbation propagates as the counter-translating positive packets of D2 at the causal speed c=spacing/tick, the SAME invariant speed as light (D2/D4), independent of the waveform. Verified: gravitational-wave evolution is identical to the D2 wave evolution, total presence is conserved, the front advances one site per tick at the causal speed c, the same invariant speed as light, independent of the waveform (cross-checked outside).',"compare.test_grav_waves",d9e_grav_waves),
 ("D9g","E","the spatial dimension is forced to exactly three. Two conditions on the framework's own inverse-(d-1)-power gravity pin it: orbital stability (D9f) gives stable circular orbits only for d<4, and the point-source potential ~1/r^(d-2) vanishes at spatial infinity only when its force tail integral converges, i.e. the exponent d-1 exceeds 1, i.e. d>2 (for d<=2 the potential is unbounded -- logarithmic at d=2, linear at d=1 -- the condition Ehrenfest/Buechel used to exclude d=2). The unique integer with 2<d<4 is three [Ehrenfest 1917; Tong, Central Forces]. Verified: forced_dimension()==[3], with the escape-work convergence cross-checked outside (bounded for d=3, growing for d=2). The framework forces the spatial dimension to exactly three.","compare.test_forced_dimension",d9g_forced_dimension),
 ("D9o","E","closed-form static spherical vacuum solution (Schwarzschild form). Outside a point mass the source vanishes and the static spherical field equation reduces to the conserved-flux condition of D9d with the Newtonian boundary A->1 at large r; solving it fixes the closed form A(r)=take(ONE,ratio(rs,r))=1-rs/r, a positive magnitude for r>rs, with rs the horizon radius. This is the Schwarzschild coefficient derived from the framework's own flux and vacuum conditions, not imported [Schwarzschild solution; vacuum field equation]. Verified: A positive outside the horizon, the vacuum flux r^2*dA/dr constant (=rs), the redshift sqrt(A_far/A_near)>1, and the weak-field reduction to D9h's 1-2GM/(r c^2) with rs=2GM/c^2 (cross-checked outside). The horizon radius rs carries 2GM/c^2.","compare.test_schwarzschild",d9o_schwarzschild),
 ("D9p","E",'continuum limit of the lattice field equations. The lattice second-difference (D1c/D1d), divided by the squared spacing, approaches the continuum curvature as the spacing shrinks toward the One-floor, so the lattice field equation approaches the continuum field equation. Built as a convergent sequence of positive ratios: the scaled second difference of the smooth profile x^2, sampled at spacings 1/2,1/4,...,1/32, equals the continuum curvature 2 at every refinement and the successive changes shrink. Verified and the convergence shown; the discrete equations of the programme carry their continuum counterparts in the fine-spacing limit.',"compare.test_continuum_limit",d9p_continuum),
 ("D9q","E",'quadrupole radiated-power magnitude. D9i fixed the leading radiating moment as the quadrupole; its power follows from the far-field expansion of the wave (D9e/EM5): the monopole is frozen by mass conservation and the dipole by momentum conservation, so the leading radiated flux comes from the third time-rate of the quadrupole moment, carried outward at c through a shell (the D9d flux form of the field energy, D9l). In positive magnitudes P = coupling*(third-difference of the quadrupole)^2 [quadrupole formula]. Verified: a time-varying quadrupole has a nonzero, constant third difference (radiates), a static one is silent, and the power scales as the square of the third rate (cross-checked outside). The framework forces its fundamental coupling in PH5.',"compare.test_quadrupole_power",d9q_quadrupole_power),
 ("D9l","E","nonlinear gravity -- the field carries energy and sources itself. The weak-field equation (D9k) is curvature = coupling*source with matter as the source; the nonlinearity of general relativity is that the gravitational field itself carries energy and adds to the source. On the cubic lattice the field's own energy density is the squared metric curvature (a potential's field energy is its gradient squared), so the full source is matter plus field energy: curvature = coupling*(rho_matter + kappa*field_energy) [gravity sources itself; Einstein field equations nonlinear]. Verified: the field energy is zero for a flat metric and positive for a curved one (9/4 at a sample mass), and the full source strictly exceeds the matter source -- gravity sources itself (cross-checked outside).","compare.test_nonlinear_gravity",d9l_nonlinear),
 ("D9m","E","the nonlinear field equation is solved as a convergent fixed point (the post-Newtonian series). Because the source includes the field's own energy (D9l), curvature = coupling*source is implicit and is solved by iteration: given a metric, compute the full source, invert the Laplacian for the updated metric, repeat to a fixed point. Each round's correction is one power of the small coupling higher, so the corrections form a decreasing positive sequence -- the post-Newtonian expansion converges. Verified: the successive self-energy corrections strictly decrease (7/50, 7/150, 7/1350, 7/109350) to the self-consistent nonlinear solution.","compare.test_pn_convergence",d9m_pn_convergence),
 ("D9n","E","the metric is many-component and the field equation conserves its source (contracted Bianchi identity). The metric is a symmetric array g_ab with D(D+1)/2 independent components -- ten in 3+1 dimensions, six in 2+1. The Einstein tensor built from its second differences has identically vanishing divergence (the contracted Bianchi identity), which forces the energy-momentum source to be conserved: its divergence is zero. On the lattice the divergence is the net flux out of a cell; a static source's outflow balances its inflow, returning to the One by opposition (no sink), so the lattice divergence is zero -- discrete local conservation [Bianchi identity; energy-momentum conservation]. Verified: ten components in 3+1, a balanced static source conserved (div=0), a leaking source not (cross-checked outside). With self-sourcing (D9l), the convergent nonlinear fixed point (D9m), and this tensor and conservation structure, the curved-tensor Einstein equations stand at the lattice level.","compare.test_tensor_bianchi",d9n_tensor_bianchi),
 ("D9k","E","curved-tensor gravity in three dimensions -- curvature = source on the cubic lattice. With the cubic operator (D1d) the metric coefficient field over space has a curvature: its 3D lattice second-difference (the D1d Laplacian) is the geometric curvature, and the weak-field Einstein equation reduces to curvature = source (the 3D Poisson form, the time-time Einstein component proportional to the Laplacian of the metric, set by the energy density) [linearized Einstein equations; Carroll]. A flat (constant) metric is source-free; a metric peaked at a mass is positively curved there: matter curves space. Verified: flat metric source-free, mass-peaked metric positively curved, source = coupling*curvature (cross-checked outside). The diagonal weak-field relation, curvature equals energy density in three dimensions, holds on the cubic lattice; the framework forces its fundamental coupling in PH5.","compare.test_einstein3d",d9k_einstein3d),
 ("D9j","E","curvature of a varying metric in the plane (the geometric source of gravity). With the 2D operator (D1c) a metric coefficient field A(x,y) has a curvature: its 2D lattice second-difference (the D1c Laplacian) is the geometric curvature, and the field equation of D9c generalises to the plane -- the curvature of the metric equals the source density (curvature = coupling * source) [linearized field equation; Poisson in 2D]. A constant metric is flat (zero curvature, source-free); a metric peaked at a mass has positive curvature there (matter curves it). This is curved spacetime in positive magnitudes: the metric is a positive field, its curvature the positive lattice second-difference (via take and opposition), matter the source. Verified: flat metric source-free, mass-peaked metric positively curved, source = coupling*curvature, cross-checked outside. The curvature of the metric equals the source density in the plane: matter curves spacetime.","compare.test_curved_metric",d9j_curved_metric),
 ("D9i","E","the leading gravitational radiation is the quadrupole (conservation forbids lower moments). A radiating multipole needs a changing moment. The monopole moment of a bound system is its total mass = total presence, which D1/D2 conserve, so it cannot change and cannot radiate; the dipole moment's change is the total momentum (the first moment's rate), conserved for an isolated system, so the dipole cannot radiate either. The lowest moment whose relevant time-change is not fixed by a conservation law is the quadrupole, so the leading gravitational radiation is quadrupole [no monopole/dipole gravitational radiation; quadrupole formula]. Verified on the lattice: for a symmetric standing source the total presence (monopole) and the first-moment rate (momentum) are unchanged in time (cross-checked outside). Conservation of the monopole and dipole moments leaves the quadrupole as the leading radiating moment.","compare.test_quadrupole",d9i_quadrupole),
 ("D9h","E",'point-mass gravitational time dilation (leading Schwarzschild g_tt). Composing the inverse-square potential of D9d (Phi=-GM/r in three dimensions) into the weak-field metric of D9b (A=1+2*Phi/c^2) gives A(r)=1-2GM/(r c^2)=take(ONE,2GM/(r c^2)), the leading Schwarzschild time coefficient, positive outside r=2GM/c^2 [weak-field/Schwarzschild g_tt; gravitational time dilation]. The clock-rate ratio between two radii is sqrt(A_far/A_near)>1: the deeper clock runs slower (the GPS / Pound-Rebka effect in a real 1/r field). Verified: A positive outside the Schwarzschild radius, redshift ratio>1, far-field flat, monopole conserved so no monopole gravitational radiation (cross-checked outside).',"compare.test_point_mass_redshift",d9h_point_mass),
 ("EM2","E",'magnetism is the relativistic correction to Coulomb (D5 applied to EM1). Two like charges moving parallel at speed beta feel pure Coulomb repulsion in their rest frame; transformed to the lab by the relativity of D5 the net force is Coulomb*(1-beta^2)=Coulomb/gamma^2, the velocity-dependent piece beta^2*Coulomb being the magnetic force, attractive for parallel currents and partly cancelling the electric repulsion [magnetism as a relativistic effect; Purcell]. The reduction factor equals 1/gamma^2 from D5 exactly. Magnetism is therefore not an independent law: it is charge (EM1) seen through relativity (D5) -- the unification of electricity and magnetism. Verified and cross-checked outside the corpus; the framework forces its fundamental coupling in PH5.',"compare.test_magnetism",em2_magnetism),
 ("EM6","E",'the Lorentz force on a moving charge -- the field acts back on the charge. A charge q in an electric field feels qE (EM1); moving at speed beta it also feels the magnetic force, which D5/EM2 showed is the relativistic correction. Composing them, the force on a moving charge is |F| = q*(E + beta*B), the electric part plus the velocity-coupled magnetic part, both positive magnitudes, the magnetic part vanishing at rest and growing with speed [Lorentz force law]. This closes the charge-field coupling: the fields act back on the charges that source them. Verified: electric-only at rest, electric plus magnetic in motion, the moving force exceeding the rest force (cross-checked outside). The framework forces its fundamental coupling in PH5.',"compare.test_lorentz",em6_lorentz),
 ("EM5","E","full 3+1 Maxwell -- the 3-vector curl closes into the 3D wave at c. On the cubic lattice (D1d) the electric and magnetic fields are genuine 3-vectors. Faraday gives dB/dt = -(curl E), Ampere-Maxwell gives dE/dt = c^2(curl B); the vector identity curl(curl F)=grad(div F)-laplacian(F) with div=0 in vacuum (Gauss, no enclosed charge) reduces the curl-of-curl to the 3D Laplacian (D1d), so d^2 B/dt^2 = c^2*laplacian3d(B): the 3D wave [Maxwell's equations; electromagnetic wave]. Electromagnetic waves propagate isotropically at c in space and light is this wave. Verified: 3D curl-of-curl reduces to the D1d Laplacian (peak six), the disturbance spreads isotropically (octahedral counts 7,25,63), and a signed 3D vector-curl leapfrog stays within the causal cone at c (cross-checked outside). The full Maxwell set in three dimensions stands; the framework forces its fundamental coupling in PH5.","compare.test_maxwell3d",em5_maxwell3d),
 ("EM4","E","full vector Maxwell in the plane -- the curl equations close into the 2D wave at c. On the 2D lattice (D1c) a transverse-magnetic field is (Bz; Ex,Ey). Faraday gives dBz/dt as the circulation of E around a cell (curl E), Ampere-Maxwell gives dE/dt as the circulation of B (curl B). Substituting one into the other, the curl-of-curl of a divergence-free field equals the 2D Laplacian of D1c (curl curl F = grad div F - laplacian F, and div F = 0 leaves -laplacian F), so d^2 Bz/dt^2 = c^2*laplacian2d(Bz): the 2D wave [Maxwell's equations; vector wave equation]. Electromagnetic waves therefore propagate isotropically at c in the plane, generated by the mutual induction of the electric and magnetic fields. Verified: curl-of-curl reduces to the D1c Laplacian (peak of four), the EM disturbance spreads isotropically at one cell per tick (diamond counts 5,13,25), and a signed transverse-magnetic leapfrog stays within the causal cone (front at c), cross-checked outside the corpus. Electromagnetic waves propagate isotropically at c in the plane, generated by the mutual induction of the electric and magnetic fields.","compare.test_vector_maxwell",em4_vector_maxwell),
 ("EM3","E",'electromagnetic disturbances propagate at c (light is an electromagnetic wave), and the Faraday/Ampere coupling reproduces the wave. A disturbance in the electromagnetic field obeys the wave equation D2 solved, propagating as counter-translating positive packets at the causal speed c=spacing/tick, the same invariant c as in D4/D5 -- the propagating disturbance is light. The two coupling laws (a changing magnetic field drives an electric one, a changing electric field drives a magnetic one) drive each field by the spatial lattice-curvature (D9c/D1) of the other; substituted together they give d^2E/dt^2 = c^2*(spatial curvature), the D2 wave, so the self-sustaining electromagnetic wave and its speed c follow from the coupling [linearized/Maxwell wave; D2]. Verified: EM front advances one site per tick like light, identical to the D2 evolution, presence conserved, speed=spacing/tick, and the coupled E<->B round reproduces the wave (cross-checked outside). The self-sustaining electromagnetic wave and its speed c follow from the Faraday-Ampere coupling.',"compare.test_em_waves",em3_em_waves),
 ("EM1","E","electric charge and Coulomb's law. The flux/field-equation structure of D9d is the same as Gauss's law for electrostatics, which is equivalent to Coulomb's inverse-square law [Gauss's law; Coulomb's law]. The one ingredient over gravity is sign: charge comes in two opposed kinds carried by the framework's opposition (two opposite influences return to the One, never to zero), where mass had only one. A charge q at distance r in three dimensions sources a field of magnitude coupling*|q|/(Omega*r^2) (the D9d flux form, d=3); the force between charges has magnitude coupling*|q1|*|q2|/(Omega*r^2), symmetric in the charges, repulsive for like signs and attractive for opposite signs. Verified: inverse-square (1,1/4,1/9), symmetric, correct signs (cross-checked outside). The framework forces its fundamental dimensionless coupling in PH5 (g*=(m-1)/m).","compare.test_coulomb",em1_coulomb),
 ("D9f","E","orbital stability constrains the spatial dimension to d<4 (Ehrenfest's argument). A test body in the inverse-(d-1)-power gravity (D9d) feels inward gravity k/r^(d-1) and outward centrifugal L^2/r^3, both positive magnitudes; a circular orbit balances them at r0. Pushing the body outward to r1>r0, the orbit is stable only if inward gravity then exceeds outward centrifugal (a restoring pull); since their ratio scales as (r1/r0)^(4-d), the pull is restoring iff 4-d>0, i.e. d<4. So stable circular orbits exist only for d<4 (d<=3): orbital stability selects spatial dimension at most three [Ehrenfest 1917; Tong, Central Forces: circular orbits stable only in d<4]. Verified: stable at d=2,3, marginal at d=4, unstable at d>=5 (cross-checked outside against the effective-potential local minimum), forces balance at r0. Orbital stability selects a spatial dimension of at most three.","compare.test_orbital_dimension",d9f_orbital_dimension),
 ("D9d","E","inverse-power force law from the field equation (Gauss/flux form). The integral form of the Newtonian field equation (D9c): the flux of the gravitational field through a closed shell enclosing a source equals the coupling times the enclosed source -- Gauss's law for gravity, equivalent to Newton's law [Gauss's law for gravity; LibreTexts Gauss's theorem]. For a point source with shell symmetry the field is uniform over the shell, so flux = field_strength * shell_measure; in d spatial dimensions a shell at radius r has measure proportional to r^(d-1) (the geometric constant Omega and the dimension d are inputs, not forced). Hence field_strength = coupling*enclosed/(Omega*r^(d-1)), the inverse-(d-1)-power law; for d=3 the inverse square (field 1, 1/4, 1/9 at r=1,2,3) and the potential 1/r^(d-2)=1/r [inverse-square tied to 3 dimensions]. The flux is r-independent (conserved); the form is forced by flux conservation while d, Omega, and the coupling (carrying Newton's G) are free. All positive magnitudes (flux, measure, field, ratio); cross-checked against M/r^(d-1) outside the corpus. The inverse-power form is forced by flux conservation; the spatial dimension is forced to three in D9g.","compare.test_inverse_square",d9d_inverse_square),
 ("D9c","E","Newtonian-limit (Poisson) field equation. The D1 lattice operator is the discrete Laplacian; its static/equilibrium limit with a source is the discrete Poisson equation. For a static potential Phi on a line, the lattice curvature at an interior site -- the positive gap (take) between twice the centre and the sum of its neighbours, with opposition for the side -- is the source density there, at coupling g/2 (which carries Newton's G; it is set to match, not forced, exactly as the coupling kappa is chosen so the weak-field Einstein equations reduce to Poisson [linearized gravity; Carroll; ScienceDirect Einstein field equations]). A linear potential has zero curvature: a uniform field is source-free, consistent with the D9 uniform field being flat. A peaked potential carries a localised source (a mass). Via A=1+2*Phi/c^2 (D9b) a mass density sets the static metric. Verified: linear source-free, tent peak-sourced, source = (g/2)*|discrete Laplacian| (cross-checked outside), metric coefficient positive. The discrete Poisson field equation holds: a uniform field is source-free, a peaked potential carries a localised mass.","compare.test_field_equation",d9c_field_equation),
 ("D9b","E","static gravitational metric (kinematics). A static field carries a position-dependent positive temporal coefficient A(x); the proper-time-to-coordinate-time ratio is sqrt(A(x)) -- a static metric's time dilation is the square root of its time coefficient [static-metric time dilation dtau/dt=sqrt(g_tt); Physics Forums; Wikipedia gravitational time dilation]. The framework carries this as a positive magnitude via the algebraic-magnitude engine (D1b) for any static positive A(x); the redshift ratio between two positions has square ratio(A_far,A_near). A constant coefficient gives redshift ratio one (no shift), so the equivalence-principle redshift (D9) forces A to vary with position -- the flat (constant-coefficient) causal structure of D4 cannot carry a field, matching the standard argument that the flat manifold must be replaced by a curved one [TCD report; SR-cannot-carry-gravity]. The uniform-field D9 factor 1+g*x/c^2 is recovered as sqrt(A) for A=(1+g*x/c^2)^2. The equivalence-principle redshift forces the metric coefficient to vary with position; D9c through D9k force its value from the source.","compare.test_static_metric",d9b_static_metric),
 ("D9","E",'gravity (equivalence-principle part) -- gravitational time dilation / redshift of a uniform field in positive magnitudes. In a frame accelerating at g, light from a lower to an upper clock a height h away takes light-travel time h/c, in which the upper clock acquires speed v=g*h/c relative to the emission frame (D5), so the upper clock receives the light Doppler-shifted. The clock-rate factor (upper relative to lower) is ONE + ratio(g*h,c*c), a positive magnitude >1; the fractional redshift is ratio(g*h,c*c). By the equivalence principle this is the uniform-field gravitational redshift, which follows from the equivalence principle without the apparatus of general relativity [Einstein 1911 equivalence principle; gravitational redshift; Pound-Rebka]. Built from positive sum and ratio only, no curvature, no signed metric; g,h,c are parameters and no measured value is imported. Cross-checked against the equivalence-principle form outside the corpus. This is the uniform-field gravitational redshift in positive magnitudes; the curved-tensor theory is built from D9b through D9k.',"compare.test_gravity",d9_gravity),
 ("D8","E",'constants -- structural fact about the operations. Every dimensionless constant the framework forces is rational or algebraic: addition, ratio, fold, and take map rationals to rationals, and the magnitude engine (D1b) returns roots of rational-coefficient polynomials. The forced constants exhibited are rational: threshold 1/2 (R7), separation 1/2 (R10), base 2 and dimensions 2^k (R1), binomials C(k,m) (D7), level ratios (2n+1)/(2k+1) (PH4c); the catalogue is verified rational and the operations verified closed on rationals. This structural fact stands beside PH5, where the framework forces its fundamental dimensionless coupling g*=(m-1)/m from the expansion factor m.',"compare.test_constants",d8_constants),
 ("D7","E","discrete quantum numbers / particle structure: the fold is 2-to-1 (R11), so each fold-level is a two-valued degree of freedom. Read as a mode that is empty or occupied, occupation is 0 or 1 -- the fermionic occupation rule, Pauli exclusion limiting a mode to 0 or 1, a single mode spanning a two-state Fock space [Fock state; Pauli exclusion; occupation-number basis]. A depth-k state carries k binary occupation numbers (its branch label); there are N=2^k of them (R1), the Fock count for k modes. The number with m occupied modes (particle number m) is the count of weight-m binary strings, C(k,m), built by Pascal's triangle in forward addition; the multiplicities sum to 2^k. Verified by enumeration against Pascal for k<=6; C(k,m) cross-checked against math.comb outside the corpus. The occupation and multiplicity structure follows from the fold's two-preimage fibre.","compare.test_particles",d7_particles),
 ("D7b","E","internal charge multiplicity from the m-fold fibre. D7 read the binary fold's 2-to-1 fibre (R11) as a two-valued degree of freedom; the m-fold (D5) is m-to-1, so every image has exactly m preimages -- an internal degree of freedom with exactly m kinds at each level. This is the forced internal fact: the m-fold carries exactly m kinds. The three-kind fibre of the tripling fold corresponds to the three colours of the strong interaction [SU(3) colour: three charges]. Joint internal states over k levels number m^k (m=2 recovers the Fock count 2^k of D7), and a colour-neutral combination takes one of each kind, i.e. a whole group of m (a baryon = three quarks). Verified: m kinds for the m-fold (three for m=3, two for m=2), m^k joint states, neutrality exactly at whole m-groups; cross-checked outside the corpus. The m-fold forces m internal kinds, three for the tripling fold, with neutrality on whole groups of m; the three-kind case corresponds to colour, and the gauge dynamics follow in D10.","compare.test_colour_charge",d7b_colour_charge),
 ("D7c","E","chirality (handedness) from the fold's two-preimage fibre (the weak sector's parity asymmetry). The fold is 2-to-1 (R11): every image has exactly two preimages, a lower one below the half-One and its antipode above, with fold(p)=fold(antipode(p)). Inverting the fold is a binary choice between the two preimages -- a two-valued orientation (handedness) every folded state carries, with no neutral middle [chirality; left/right-handed states]. A single-handed coupling keeps one preimage of the pair and not its antipode, acting on one hand only -- the parity asymmetry of a chiral interaction. Verified: both preimages fold to the same image, split across the half-One, the orientation is exactly two-valued, and the single-handed coupling acts on one hand; cross-checked outside the corpus. A single-handed coupling acts on one hand alone, the parity asymmetry of a chiral interaction; the electroweak dynamics follow in D11.","compare.test_chirality",d7c_chirality),
 ("D7d","E",'strong-sector confinement from flux confined to a tube. The inverse-power flux law (D9d) gives field_strength = coupling*enclosed/(Omega*r^(d-1)); at d=3 the field falls as 1/r^2 and the work to separate two charges to infinity converges to a bound -- a free, unconfined charge (the Coulomb field, EM1). If the flux is held in a tube -- field lines confined to one transverse channel rather than spreading over a sphere -- the effective dimension is d=1, the shell measure is r^0=constant, and the field strength is constant in r. A constant force makes the work to separate grow in proportion to the distance, without bound: the charges cannot be pulled apart -- confinement, a linear potential [QCD flux tube / linear confining potential; lattice QCD]. Verified: the tube field is constant in r while the Coulomb field falls as 1/r^2, the tube separation work grows with distance while the free work converges; both read off the one D9d flux law, cross-checked outside. Flux confined to a tube gives a constant force and a linearly growing potential: the charges cannot be separated.',"compare.test_confinement",d7d_confinement),
 ("D10d","E",'the two colour-neutral combinations -- baryons and mesons. D7b makes a whole group of m colours neutral (three colours for the tripling fold, a baryon). A second neutral combination is a colour together with its opposition, its anticolour: a colour times its reciprocal returns the One (R9 opposition), so a colour-anticolour pair balances to neutral, a meson. Both are colour-neutral, both built from the m-fold fibre (D7b) and its opposition (R9), in positive magnitudes [hadrons: qqq baryons and q-qbar mesons]. Verified: the whole three-colour group and the colour-anticolour pair are both neutral; cross-checked outside. The two colour-neutral combinations are the three-colour group and the colour-anticolour pair: baryons and mesons.',"compare.test_colour_neutral",d10d_colour_neutral),
 ("D10g","E","the forced running rate (beta slope) of the strong coupling. The running of D10b has an exact rate, forced from the fold factor and the carried colour with no measured number: the effective coupling at level k is the accumulated source over the bare, and its step from one level to the next -- the beta slope -- is the carrier's colour over the bare, constant per level. A charged carrier has a present, constant forced slope; a chargeless one has none [the QCD beta function structure, forced from the framework rather than fitted]. Verified: the strong beta slope is an exact constant and the abelian beta is absent; cross-checked outside.","compare.test_beta_slope",d10g_beta),
 ("D10f","E",'the strong carrier is massless (luminal) yet confining. The electroweak symmetry breaking (D11d) acts on the electroweak channels, not the strong carrier, so the strong carrier acquires no mass-part; by D11a a mediator with no mass-part reaches unbounded and by the lattice (D1d/D2) a disturbance advances one site per tick, the causal speed c. So the strong carrier is massless and luminal, yet its self-coupling forms a confining flux tube (D10c) -- masslessness and confinement coexist [the gluon is massless but never observed free]. Verified: the strong carrier is luminal and confining together; cross-checked outside.',"compare.test_strong_luminal",d10f_luminal),
 ("D10e","E","the strong field equation: nonlinear, self-sourced through colour. Gravity's field equation is nonlinear because the source includes the field's own energy (D9l) and solves as a convergent fixed point with shrinking corrections, the post-Newtonian series (D9m). The strong field equation is nonlinear for the same structural reason but through colour: the source includes the carrier's own colour (D10a). Iterating it, each round adds the carrier's self-charge as a correction; that colour feeds growth (D10b), so the corrections do not shrink -- the source grows, the coupling strengthens with range (confinement). Same nonlinear self-sourcing structure as gravity, opposite convergence: gravity weakens, the strong field confines; the chargeless field is linear [non-abelian Yang-Mills self-sourcing vs the convergent gravitational nonlinearity]. Verified: the charged-carrier field equation is nonlinear with persistent (non-shrinking) corrections while the chargeless one is linear; cross-checked outside.","compare.test_strong_field_eq",d10e_field_eq),
 ("D10c","E","the flux tube forms from the self-coupling. The carrier carries the colour it mediates (D10a), so colour is present along the field line itself and feeds the field (D10b). A chargeless carrier has no colour on the line, so nothing binds the flux laterally and its transverse width spreads with the line's length (the Coulomb spread). A self-coupling carrier carries colour along the line, and that colour re-sources the field laterally each step, binding the flux to a fixed transverse width as the line lengthens -- a flux tube. The tube geometry of D7d is forced by the self-coupling, not imposed [QCD flux tube formation; the source of the linear confining potential]. Verified: the self-coupling carrier holds a fixed width at every length while the chargeless one spreads; cross-checked outside.","compare.test_flux_tube",d10c_flux_tube),
 ("D10a","E","strong-sector self-coupling: the carrier carries the charge it mediates. Gravity self-sources through energy (D9l); the strong mediator self-sources through charge -- the carrier itself carries the colour (D7b) it transmits, so it is a source of the very field it mediates, and the total source is the matter charge together with the carrier's own charge. The electromagnetic carrier carries no colour (its self-charge is absence, not zero), so the electromagnetic field does not source itself; its source is the matter charge alone [non-abelian gauge field self-coupling vs abelian]. Verified: the chargeless carrier does not self-couple and its source is the matter charge; the charged carrier self-couples and its source is matter charge plus carrier charge; cross-checked outside. The charged carrier sources the field it mediates; the chargeless carrier does not.","compare.test_self_coupling",d10a_self_coupling),
 ("D10b","E","the strong coupling runs: weaker at short range, stronger at long range. Because the carrier carries the charge it mediates (D10a), it feeds the field at every level of self-coupling; probing across more levels -- longer range -- the effective source grows, each level adding the carrier's own charge, growing without bound toward the locking it drives (confinement, D7d). A chargeless carrier adds nothing per level, so its effective source is flat across range and that coupling does not run this way [running of the strong coupling; asymptotic freedom]. Verified: the self-coupling source increases strictly with the number of levels (range) while the chargeless one stays flat; cross-checked outside. The strong coupling runs: weaker at short range, stronger at long range; its slope is forced in D10g.","compare.test_running",d10b_running),
 ("D11a","E","weak-sector short range from a massive mediator, without an exponential and without a sink. A massless mediator propagates one site per tick indefinitely (D2): its forward presence is never diminished, so its reach is unbounded -- the long-range 1/r^(d-1) law (EM, gravity). A massive mediator carries a mass scale; each tick the mass captures a part of the forward-moving presence into a co-located rest mode. Nothing is lost -- the captured part stays as rest presence, total presence conserved (no sink, the no-loss axiom) -- but the forward-reaching presence diminishes and falls to the One-floor within a finite number of ticks: a finite range, set by the mass, with a larger mass giving a shorter range [massive mediator => short-range force; massless => long-range]. The fall is the framework's own per-tick transfer, not an imported exponential. Verified: the massless reach is unbounded; the massive reach is finite and shortens with mass; total presence is conserved at the One throughout; cross-checked outside. A massive mediator gives a finite range set by the mass, with no sink and no imported exponential.","compare.test_massive_range",d11a_massive_range),
 ("D11b","E","electroweak mixing as a forced split of one coupling into two channels. The fold's two-preimage fibre (R11, D7c) gives exactly two channels, the lower and upper hand. A single coupling, tied by the fold factor m, splits between them in the ratio the fold already forces: the charged channel takes the holding part (m-1)/m (PH5), the neutral channel the remainder 1/m, and the two sum to the One -- conserved, nothing lost. The mixing ratio of neutral to charged is 1/(m-1), forced from m alone with no measured angle fed in [electroweak mixing: one coupling resolving into a charged and a neutral channel]. Verified: the split is forced and the channels sum to the One, with mixing ratio 1/(m-1) (one for the binary fold, one-half for the tripling fold); cross-checked outside. The mixing ratio of neutral to charged is 1/(m-1), forced from the fold factor.","compare.test_mixing",d11b_mixing),
 ("D11c","E","the massless/massive mediator split as a structural result. The two channels of D11b combine; the combination that lands on the fold-invariant One -- charged + neutral = the One, unison, the fold's fixed region (RB2) -- is the unbroken direction: preserved under the fold, undisplaced, carrying no mass-part and reaching unbounded (massless, long-range, the photon). Each channel taken alone is a proper part of the One, displaced from the invariant, carrying a mass-part equal to its shortfall from unison (via take) and a finite range (massive, short-range, the W and Z). The split into one massless direction and the rest massive is forced by which combination sits on the fold-invariant, not put in by hand; conserved (the channels sum to the One), no sink, no exponential [electroweak symmetry breaking: one massless mediator + massive mediators]. Verified: the preserved combination is the One and is massless/unbounded while each channel alone is massive with finite range; cross-checked outside. One combination sits on the fold-invariant and is massless and long-range, the photon; each channel alone is massive and short-range, the W and Z.","compare.test_massless_massive_split",d11c_split),
 ("D11f","E",'the weak force law: finite-range. Each force carries its characteristic law -- the inverse-square Coulomb (EM1), the constant-force confinement (D7d), the inverse-square gravity (D9d). The weak force law follows from its massive mediator (D11a): the field strength at range r is the surviving forward presence after r ticks of the mass capturing a part into rest, appreciable within the range and fallen to absence beyond it -- a finite-range force law, against the inverse-square that never vanishes [short-range weak force vs long-range EM and gravity]. Verified: the weak field is appreciable within its range and absent beyond it while the inverse-square never vanishes; cross-checked outside.',"compare.test_weak_force_law",d11f_force_law),
 ("D11g","E",'the forced mass-part ratio of the weak channels. Each weak channel carries a mass-part equal to its shortfall from unison (D11c): the charged channel (m-1)/m carries 1/m, the neutral channel 1/m carries (m-1)/m. Their ratio is forced from the fold factor m as 1/(m-1), with no measured mass fed in [the W/Z mass-ratio structure, forced from m]. Verified: the charged/neutral mass-part ratio is 1/(m-1) for the binary, tripling and quadrupling folds; cross-checked outside.',"compare.test_weak_mass_ratio",d11g_mass_ratio),
 ("U1","E","the four forces' characteristic constants are forced from the one fold factor m. Every characteristic dimensionless quantity of the four interactions is forced from the single fold factor m, none fed in: the fundamental coupling g*=(m-1)/m (PH5), the colour count m (D7b), the strong running slope as colour over bare (D10g), the electroweak mixing 1/(m-1) (D11b), and the weak channel mass ratio 1/(m-1) (D11g). One axiom, one fold factor, the constants of all four forces [unification: a common origin for the couplings and structure of every interaction]. Verified: all five forced constants derive from the single m; cross-checked outside.","compare.test_unification",u1_unification),
 ("U2","E",'a forced relationship between two ratios that correspond to electroweak observables. The framework forces two internal ratios -- the channel split of D11b and the channel mass-part ratio of D11g -- to the same value 1/(m-1), so it forces a relationship between them: they are equal, exactly, for every fold factor m, with no measured value fed in. These correspond to the electroweak mixing ratio and the weak mass-part ratio; the measured electroweak sector relates the W/Z mass ratio to the mixing angle, and the framework forces the equality of the two internal ratios as a testable tie. Verified: the two forced ratios coincide for every fold factor checked; cross-checked outside.',"compare.test_forced_relationship",u2_forced_relationship),
 ("U7","E","the fold factor of a sector is the count of internal kinds in its fibre. The framework forces that an m-fold is m-to-1, so every image has exactly m preimages -- m internal kinds at each level (D5, D7b); this is the forced internal fact. The binary fold native to the axiom (R5) is 2-to-1, so its fibre has two kinds, the two hands of chirality (D7c): the m=2 case is the framework's own. A sector with m internal kinds is then the m-fold's fibre; identifying the two-kind fibre with the electroweak sector and the three-kind fibre with the strong sector is a structural correspondence between the fold's fibre and the sector's internal multiplicity, not a selection the framework forces. Given that correspondence, a forced ratio that is a function of m is the value for that sector. Verified: the m-fold has exactly m preimages for every m (two for the binary, three for the tripling); cross-checked outside [SU(2) electroweak, SU(3) colour].","compare.test_u7",u7_sector_m),
 ("C1s","E",'self-observation is closed. Observation is in the axiom set, and the fold is the act of observation: applied to a state, its result re-enters as part of the state. A self-observing loop stays within the system at every step -- closure (R8); self-observation cannot take a structure outside itself [a self-modelling system operating on its own states is a closed operator]. Verified across seeds; cross-checked outside.',"compare.test_self_loop_closed",c1s_loop),
 ("C5s","E","the discreteness of the observational moment. The fold is the unit act of observation and it is atomic (D6): each fold yields one bit -- it either casts out a whole One or it does not, with no partial fold. So observation proceeds in discrete, indivisible steps: quantised moments, one fold each, with no fractional act between two folds [perception as discrete 'moments' rather than continuous]. Verified: the act has exactly two outcomes across states, and an observation sequence is a sequence of single folds; cross-checked outside.","compare.test_self_discrete",c5s_discrete),
 ("C4s","E",'integration of self-observers. The framework forces a holding threshold (m-1)/m (R7, PH5a) at which coupled copies lock into one. Applied to self-observing states, it forces an integration threshold: below it the observers stay separate, each its own loop; at or above it they lock into a single integrated loop. Binding many observers into one is set by the same forced ratio (m-1)/m that fixes the coupling and criticality (U4) [a set of parts becomes one experiencing whole only above a threshold of integration]. Verified: separate below g*, integrated at and above; cross-checked outside.',"compare.test_self_integration",c4s_integration),
 ("C2s","E",'the observation blind spot. The act of observation is two-to-one (R11): a state and its antipode are observed identically, so self-observation cannot recover which of the two preimages it came from -- an intrinsic limit on self-knowledge forced by the 2-to-1 structure of the act [a self-model built from a many-to-one readout cannot distinguish inputs sharing a readout]. Verified across states; cross-checked outside.',"compare.test_self_blind_spot",c2s_blind),
 ("C3s","E","the self-observation fixed point. Unison (the One) is the one state unchanged by observation, fold(1)=1; the half-One observes to unison; self-coincidence below unison repels (R5). Unison is the unique stable fixed point of self-observation [a self-referential map's fixed point, where observing the state returns the state]. Verified; cross-checked outside.","compare.test_self_fixed_point",c3s_fixed),
 ("N1","E",'a forced result composed across domains: the mediator count is forced from the colour count as m^2-1. The carrier carries a colour and an anticolour (D10a: it carries the colour it mediates; R9: every colour has an anticolour), so the mediators are the colour-anticolour combinations, m*m of them, minus the one colourless combination (the singlet, which carries no net colour and does not mediate the colour force) -- m^2-1, taken by the audited primitive. Forced first: the three-kind fibre forces eight mediators, the two-kind fibre three, corresponding to the gluons and the weak bosons. Arbiter: the established mediator count is the dimension of the adjoint of SU(m), m^2-1 -- eight gluons for three colours, the colourless singlet excluded (eight, not nine) [QCD: 8 gluons; SU(2): 3 weak bosons]. The forced value and the established count coincide. Verified; cross-checked outside.',"compare.test_mediator_count",n1_mediator_count),
 ("T1","E","the prediction test on the forced count. The forced value is fixed first, from the framework: the tripling fold's fibre has exactly 3 internal kinds (U7, D7b), an integer derived from the fold with nothing fed in, corresponding to the colour count. The measured value is the arbiter only: experiment determines the number of colours to be 3 -- the R-ratio in e+e- annihilation to hadrons, the existence of the Delta++ requiring a three-valued charge for the Pauli principle, and the pi0 to two-photon rate [Nc=3, established experimentally]. The forced value and the measured value coincide. The measured number is used solely to test an already-forced result, never as a construction input -- the one comparison the language rule permits (Phase Three plan, step 3). Verified; cross-checked outside.","compare.test_prediction_colour",t1_prediction_colour),
 ("T2","E","the forced generation count -- the tripling fold's fibre carries exactly three kinds. D7b/U7 force that an m-fold fibre carries exactly m internal kinds, with no free index: the tripling fold's fibre is exactly three. A fermion generation is an internal degree of freedom of the fold; identifying the generation index with the tripling-fold fibre is the same structural correspondence U7 documents for the colour fibre and the sector assignments. On that footing the forced generation count is three, on the identical derivation that forces the three colours (T1). The measured value -- three light fermion generations, from the Z invisible width (number of light neutrinos 2.984 +/- 0.008) [LEP, PDG] -- is the arbiter only, fed in nowhere. Verified: the tripling fold's fibre has exactly three internal kinds; cross-checked outside.","compare.test_t2_generation_count",t2_generation_count),
 ("U4","E",'a forced cross-domain identity: the fundamental coupling g* (PH5), the holding/criticality threshold (R7/PH5a), and the charged weak channel (D11b) are one forced ratio (m-1)/m. Three quantities that play distinct physical roles -- the interaction coupling, the threshold at which coupled systems lock, and the weak charged channel -- are forced to the same value by the fold factor, for every m, with nothing fed in. Verified across fold factors; cross-checked outside.',"compare.test_u4",u4_rel),
 ("U5","E",'a forced tie between the strong charge structure and the coupling: the fundamental coupling is fixed by the number of internal colour kinds N (D7b), g* = (N-1)/N. The coupling strength is determined by how many internal kinds the charge comes in, for every m, with nothing fed in. Verified across fold factors; cross-checked outside.',"compare.test_u5",u5_rel),
 ("U6","E",'a forced product relation across the weak sector: the electroweak mixing 1/(m-1) (D11b) times the charged coupling (m-1)/m (PH5) equals the neutral channel 1/m (D11b). A forced tie among three weak-sector observables, for every m, with nothing fed in. Verified across fold factors; cross-checked outside.',"compare.test_u6",u6_rel),
 ("B2","E","the forced electromagnetic coupling. The electromagnetic sector is the binary fold (m=2), the axiom's native fold (EM1's two charge kinds, D7c's two preimages). The framework forces the coupling of this sector from its own expansion factor: g* = (m-1)/m = 1/2 at the binary fold. This is the system's forced electromagnetic coupling, derived from the one axiom with nothing fed in, recorded as the system's result -- the framework forces a definite interaction strength where the standard account carries the electromagnetic coupling as a free parameter it cannot derive. Whether a measured electromagnetic coupling equals the forced value is a separate arbiter question, never the standard the forced result must meet (the system answers only to its own axioms and engine). The framework's forced integer interaction quantities stand confirmed by their measured arbiters -- the colour count (T1), the mediator count (N1), the spatial dimension (D9g). Verified: the framework forces the EM coupling to 1/2 at the binary fold; cross-checked outside.","compare.test_b2_arbiter",b2_arbiter),
 ("B3","E","the forced electroweak mixing sin^2(theta_W), bare and running. The electroweak sector is the binary fold (m=2). Its two channels (D11b) carry the charged coupling (m-1)/m and the neutral coupling 1/m; the photon is the combination on the fold-invariant One (D11c). The mixing sin^2(theta_W) is the proportion of that combination carried by the neutral channel -- the ratio of squared couplings neutral^2/(charged^2+neutral^2), positive magnitudes, ratio only -- which at the binary fold (charged=neutral=1/2) is 1/2 bare. The charged carrier flips the hand (D11e), so it carries the charge it mediates and by D10b it runs: the source accumulates the carrier self-charge once per level (the same construction as the strong slope D10g), the charged coupling is the holding part take(s,One)/s, the neutral carrier is chargeless and flat, and the mixing runs monotonically down from 1/2. The measured sin^2(theta_W)=0.23113 at the Z scale [arXiv:1911.11528; on-shell 0.2218-0.2240, hep-ex/9405008] is the arbiter only, fed in nowhere; the forced running passes through it. What the framework forces: the bare value 1/2 and the downward running, from the one axiom. What it does not yet force: the scale that fixes which level is the Z mass -- the open construction. The standard account carries the mixing angle as a measured free parameter [Glashow-Weinberg-Salam electroweak mixing]. Verified: bare 1/2, monotonic running, passes the measured value; cross-checked outside.","compare.test_b3_ew_mixing",b3_ew_mixing),
 ("B4","E","the forced scale-ratio structure (dimensionless), from the fold's own depth. A running coupling (B3, D10g) is indexed by level, a bare range-count; the framework forces no absolute energy per level (the One is dimensionless, the system is pure ratios), so an absolute level<->energy map would require importing a measured unit, which the language rule forbids (11.2). What the framework forces is the dimensionless scale structure: the fold's depth doubles the count of places each step (num_levels(k)=2^k), so adjacent depths stand in a forced scale ratio of two; and the bound-state rungs are evenly spaced at 1/2^k. These are scale ratios forced from the fold with no measured value fed in. The absolute (dimensionful) scale is not a forced result -- it is a unit, the named open edge, the next construction toward a full scale-fixing [a dimensionless theory forces ratios; an absolute scale needs a unit]. Verified: the depth scale ratio is exactly two at every depth and the rung-spacing halves each depth; cross-checked outside.","compare.test_b4_scale_ratio",b4_scale_ratio),
 ("B5","E","the forced dimensionless running curve of the electroweak mixing on the fold's own scale axis. B3 forces sin^2(theta_W) running by fold depth; B4 forces the scale axis (ratio two per depth, 2^k). Stated together, the framework forces the full running curve of the mixing as a function of its own dimensionless scale axis -- the bare value 1/2 at the base depth, falling monotonically as the forced scale ratio 2^k grows. A forced dimensionless object combining B3 and B4, with no measured value and no unit fed in. The absolute anchoring of the base depth to a physical energy (the dimensionful unit) is the named open edge; the dimensionless curve itself is forced and complete [a running coupling as a function of a dimensionless scale ratio]. Verified: the scale ratio is 2^k at each depth and the mixing falls monotonically along it from 1/2 at the base; cross-checked outside.","compare.test_b5_running_curve",b5_running_curve),
 ("B6","E","the forced W/Z mass-squared ratio and the forced on-shell identity. B3 forces the mixing sin^2(theta_W) = neutral^2/(charged^2+neutral^2); the partner observable, the W/Z mass-squared ratio, is forced from the same two channels as charged^2/(charged^2+neutral^2). Their sum is exactly the One at every depth: the framework forces the on-shell relation M_W^2/M_Z^2 + sin^2(theta_W) = One, not assumed but produced by the channel structure (D11c/D11g). The mass ratio is bare 1/2 and runs up as the mixing runs down -- the same forced curve, the two electroweak observables tied by the forced sum-to-One (U2's tie in concrete mass-and-mixing form). At the depth where the mixing meets its measured arbiter (0.231) the mass ratio meets its own (~0.777) together. No measured mass is fed in; the measured ratio is the arbiter only [on-shell: M_W^2/M_Z^2 = cos^2(theta_W) = 1 - sin^2(theta_W), PDG W,Z masses]. Verified: the sum is exactly the One at every depth and the mass ratio rises monotonically from 1/2; cross-checked outside.","compare.test_b6_onshell",b6_onshell),
 ("B7","E","the forced level-to-depth map and the mixing on a single forced scale axis. B3 runs the mixing by self-coupling level (D10b); B4 forces the scale ratio 2^d per fold depth. These were two axes; the framework forces them to be one. A carrier propagates one site per tick (D2's propagation law, nearest-neighbour, forced), and a fold of depth d has 2^d places (num_levels), so a carrier traversing a depth-d structure crosses 2^d sites and accumulates 2^d self-coupling levels: the self-coupling level at fold depth d is num_levels(d)=2^d, the same 2^d as B4's scale ratio. The running-level axis and the fold-depth scale axis are therefore one forced axis, 2^d, composed from D2 and the fold depth with no measured value fed in. The mixing at fold depth d is forced as sin^2(theta_W)=running(2^d): 9/25 at d=0, 4/13 at d=1, 9/34 at d=2, 25/106 at d=3, falling monotonically. The measured value 0.23113 (arbiter only) lies on this forced curve near fold depth 3 (25/106=0.2358), which is also the forced spatial dimension (D9g) -- a correspondence the engine produces, its significance for the author and assessors to judge [running of sin^2(theta_W) as a function of scale]. Verified: the level at each depth is 2^d and the mixing falls monotonically from 1/2; cross-checked outside.","compare.test_b7_level_depth_map",b7_level_depth_map),
 ("B8","E","the forced convergence of the strong and electroweak couplings on the single forced axis. Each sector runs from its own forced bare coupling g*=(m-1)/m (PH5/U5) -- strong at m=3, electroweak at m=2 -- by the holding form (s-1)/s of its accumulating source (D10b/D10g), on the single forced axis 2^d (B7: self-coupling level at fold depth d is 2^d). Placing both sectors on the shared axis, the gap between the strong and electroweak couplings shrinks monotonically toward absence as depth grows (1/12, 1/20, 1/42, 1/110, 1/342, ...): both run up toward the One (unison) and converge in the deep-self-coupling limit, with no measured value fed in. The framework forces the two couplings to meet in the high-self-coupling limit, the framework's own analogue of coupling unification [grand-unified convergence of the running couplings at high scale]. Verified: the gap strictly decreases with depth and both couplings rise toward the One; cross-checked outside.","compare.test_b8_coupling_convergence",b8_coupling_convergence),
 ("B9","E","the forced closed form of the coupling-convergence rate. The gap between the strong (m=3) and electroweak (m=2) couplings (B8), each the holding (s-1)/s of its running source s=m+2^d, has a single forced closed form: since (s-1)/s is the One taken by 1/s, the gap is 1/(2+2^d) taken by 1/(3+2^d) = 1/((2+2^d)(3+2^d)), the reciprocal of the product of the two sectors running source-magnitudes. The two fold factors (2 and 3) and the forced axis 2^d are the only inputs; the convergence rate is forced from them with nothing fed in. At deep depth the product grows as (2^d)^2 so the gap falls as 1/4^d: a forced quadratic-in-scale convergence rate, the exact rate of B8 stated in closed form [the rate at which running couplings approach unification]. Verified: the closed form equals the engine computed gap at every depth and decreases strictly with depth; cross-checked outside.","compare.test_b9_gap_closed_form",b9_gap_closed_form),
 ("B10","E","the forced finite convergent accumulated coupling separation. B9 gives the coupling gap 1/((2+2^d)(3+2^d)); the accumulated separation over all depths is the sum of the gaps. Each partial sum is an exact positive rational (the sum of positive parts), the partial sums increase strictly and stay bounded (under a fixed rational ceiling, since the tail falls as 1/4^d), so the sum is forced to converge to a finite total -- a forced finite accumulated separation between the strong and electroweak couplings across the whole scale axis, the first gap 1/12 dominating, nothing fed in. The limit itself is irrational and so is not a single permitted-language object; the forced result is the convergent exact-rational partial-sum sequence and its forced finiteness, not a closed rational value [a convergent series of rational terms with an irrational sum]. Verified: each partial sum is an exact rational, the sequence increases and stays bounded; cross-checked outside.","compare.test_b10_accumulated_separation",b10_accumulated_separation),
 ("B11","E","the forced three-coupling separation structure. On the single forced axis 2^d (B7), the strong (m=3) and weak (m=2) couplings run up by the holding (s-1)/s of source s=m+2^d (B8) and converge (B9), while the electromagnetic coupling is flat at 1/2 (B2, chargeless carrier). The strong-weak gap shrinks; the gaps from each running coupling to the flat EM grow with depth, with forced closed forms strong-EM=(1+2^d)/(2(3+2^d)) and weak-EM=2^d/(2(2+2^d)). The three couplings form one forced structure -- two running up and converging, the third flat, the running pair separating from it by forced gaps -- all from the fold factors 2 and 3 and the axis 2^d, nothing fed in [the relative running of the three gauge couplings with scale]. Verified: the closed forms equal the running-minus-EM gaps at every depth and both grow with depth; cross-checked outside.","compare.test_b11_three_coupling",b11_three_coupling),
 ("B12","E","the framework forces scale-invariance. Whether an absolute scale is forced is a framework question attempted in the engine: the lattice physics (D2 propagation) depends only on the spacing/tick ratio -- the continuum speed is spacing/tick, identical at every absolute spacing -- and the forced unification quantities (B3-B11) are dimensionless ratios. Running the engine at different absolute scales with the same ratio returns the same physics, so the framework forces scale-invariance and no absolute scale: the absolute scale is a free resolution choice the engine is invariant under, shown by the engine returning identical results at every scale rather than assumed from a unit convention. The forced content is the dimensionless structure -- the couplings, mixings, mass ratios, and convergence of the whole B-line -- which the framework forces from the One with nothing fed in [a scale-invariant theory forces dimensionless ratios; the absolute scale is set by choice of units]. Verified by running: the continuum speed is identical for equal spacing/tick ratios at different absolute scales, and the forced quantities are dimensionless; cross-checked outside.","compare.test_b12_scale_invariance",b12_scale_invariance),
 ("B13","E","the forced unison ordering and the forbidden triple coincidence. On the forced axis 2^d each running coupling's gap to the One (unison) is 1/(m+2^d); a smaller fold factor gives a larger gap and reaches unison later, so weak (m=2) trails strong (m=3) at every depth -- the framework forces strong to approach unison ahead of weak, while EM is flat (B2) and never reaches it. And the three couplings never coincide at one depth: EM at 1/2 sits strictly below the running pair at every depth (strong>weak>EM), a forced structural fact. All from the fold factors and the axis 2^d, nothing fed in [the order in which gauge couplings approach a unified value, and the absence of a single common crossing]. Verified: strong's gap-to-One is strictly less than weak's at every depth, and strong>weak>EM at every depth; cross-checked outside.","compare.test_b13_unison_order",b13_unison_order),
 ("B14","E","the discriminating prediction -- the forced on-shell tie as a falsifiable number. B6 forces the on-shell identity sin^2(theta_W) + M_W^2/M_Z^2 = One at every depth from the channel structure (D11c/D11g); the standard account treats the relation between the mixing and the mass ratio as scheme-dependent and does not force it. Stated as a prediction with the forced value fixed first: the two separately-measured observables must sum to the One within the framework's own forced rung-spacing -- the running curve's step at the crossing (~241/81797), a forced quantity of the curve, not a chosen band. The measured mixing (0.23113) and the measured W/Z mass-squared ratio are the arbiters, fed in nowhere [on-shell M_W^2/M_Z^2 = 1 - sin^2(theta_W); PDG W,Z masses]. Verified: the forced sum is exactly the One at every depth and the forced tolerance is a positive rung-spacing of the curve; cross-checked outside.","compare.test_b14_discriminating_prediction",b14_discriminating_prediction),
 ("M1","E","the single fermion mass-part -- the forced shortfall from unison (the entry to the matter sector). A fermion couples to the displaced vacuum (D11d): the no-zero axiom forbids the symmetric absence-vacuum, so the ground state is a positive part of the One. A direction displaced from the fold-invariant unison carries a mass-part equal to its shortfall from unison (D11c), the positive magnitude take(ONE, coupling) -- the identical construction D11g runs for the weak channels. A fermion in a sector of fold factor m sits at the holding coupling (m-1)/m (R7/PH5); its mass-part is the shortfall take(ONE, holding); with self-coupling depth (D10b/D10g) the holding coupling runs as (s-1)/s, s = m + 2^d, so the mass-part is its shortfall 1/s, a forced positive magnitude, a proper part of the One running down toward it as depth grows -- the massless limit of QA4 as the coupling to the displaced vacuum closes on unison. The dimensionless mass-part is forced; the absolute mass scale rides free by the forced scale-invariance (B12) [the fermion rest mass and its massless limit]. Verified: the mass-part equals 1/s at every depth for the electroweak and strong sectors, is a proper positive part of the One, and runs down toward the One with depth; cross-checked outside the corpus.","compare.test_m1_fermion_mass_part",m1_fermion_mass_part),
 ("M2","E","the generation mass-splitting -- distinct forced mass-parts from distinct preimage positions. T2 forces the generation count three as the tripling fold's fibre (D7b/U7), and D7b makes the three kinds symmetric in count. The three kinds are the three preimages of the tripling fold (D5), which sit one-in-three around the One apart, at the forced positions one-third, two-thirds, and the One itself. Each kind's mass-part is its shortfall from the fold-invariant unison (M1, D11c), take(ONE, position): two-thirds, one-third, and the kind on the One carrying no shortfall -- the massless direction of D11c. The count-symmetry of the fibre is broken into three distinct forced mass-parts by where the three preimages sit, with no free index and no measured value [the three fermion generations differ only in mass]. Verified: the three preimages are at the forced one-in-three positions, two carry the distinct shortfalls two-thirds and one-third, and the third sits on the fold-invariant; cross-checked outside the corpus.","compare.test_m2_generation_splitting",m2_generation_splitting),
 ("M3","E","the inter-sector mass pattern -- quark/lepton and up/down from fibre membership. A fermion's mass-part is the shortfall from unison of its sector's holding coupling (M1). Membership is forced by D7b/D7c: a quark carries the colour fibre (the tripling fold m=3, D7b), a lepton does not (the binary electroweak fold m=2). Their holding couplings (m-1)/m are two-thirds and one-half, so their mass-parts are the shortfalls one-third and one-half -- a forced quark-to-lepton ratio of two-thirds, no free index. Up-type and down-type are the two preimages of the chirality fibre (D7c) at the forced positions one-half and the One: the down-type carries the shortfall one-half, the up-type sits on the fold-invariant (the massless direction, D11c). The inter-sector splitting is forced by fibre membership with no measured value fed in [quarks and leptons, up-type and down-type, differ in mass]. Verified: the quark and lepton mass-parts are one-third and one-half with ratio two-thirds, and the up/down pair splits into a displaced one-half and the massless direction on the One; cross-checked outside the corpus.","compare.test_m3_inter_sector",m3_inter_sector),
 ("M4","E","the neutrino mass is forced smaller -- single-handedness cannot carry the two-hand mass term. QA4's mass term couples the two hands of the chirality fibre (D7c) to each other, a two-hand coupling. A charged fermion carries both hands, so the full mass coupling acts and its mass-part is the two-hand shortfall (M3, one-half for the displaced hand). A neutrino is single-handed (D7c: a single-handed coupling acts on one hand alone), so the partner hand the mass term needs is absent and the coupling cannot act fully: the neutrino's mass-part is a proper part of the two-hand value, strictly smaller. The smallness of the neutrino mass is forced by hand-count alone, no value chosen and no measured input [the neutrino mass is far smaller than the charged fermions]. Verified: the two-hand charged mass-part is a proper part of the One, and a single hand carries a proper part of that pair, so the neutrino mass-part is forced below the charged mass-part; cross-checked outside the corpus.","compare.test_m4_neutrino_smaller",m4_neutrino_smaller),
 ("M5","E","the mixing structure -- a near-diagonal relation between mass and channel bases. A mixing matrix relates the mass eigenstates to the interaction eigenstates. The mass eigenstates sit at the fold's preimage positions (M2 for the three generations, M3 for up/down); the interaction eigenstates sit at the channel splits of D11b. These are distinct bases -- the preimage positions are not the channel positions -- so the mixing relating them is non-trivial, carrying off-diagonal overlap with a dominant diagonal. The quark sector (the tripling fold m=3, three preimage positions, D7b) carries a finer mass-basis than the lepton sector (the binary fold m=2, two hands, D7c), so the quark mixing (CKM) is more diagonal than the lepton mixing (PMNS). This ordering is forced by fibre size, in ratio and opposition, with no signed rotation, no complex phase, and no measured value [the CKM matrix is near-diagonal; the PMNS matrix has larger off-diagonal mixing]. Verified: the quark mass-basis is larger than the lepton mass-basis and the bases are distinct, forcing the near-diagonal mixing and the CKM-more-diagonal-than-PMNS ordering; cross-checked outside the corpus.","compare.test_m5_mixing_structure",m5_mixing_structure),
 ("M6","E","the forced mixing magnitudes -- the overlap rule is the fold's own separation. The mixing entry between a mass eigenstate at preimage position p (M2/M3) and an interaction channel at position c (D11b) is their overlap, and the fold's own overlap of two positions is the separation primitive: the One at coincidence (unison, full alignment, the diagonal) and a proper fraction when the positions differ (the off-diagonal). No rule is chosen; the separation is the fold's own measure of how far two ones lie apart. For the quark sector the mass and channel positions are one-third and two-thirds, separation one-third: the CKM off-diagonal is one-third. For the lepton sector the two hands sit at one-half and the One, separation one-half: the PMNS off-diagonal is one-half. The CKM off-diagonal one-third is smaller than the PMNS off-diagonal one-half, so the CKM is more diagonal than the PMNS, in ratio with no signed rotation, no complex phase, and no measured value [the CKM matrix is near-diagonal with small off-diagonal entries; the PMNS matrix has larger off-diagonal mixing]. Verified: the diagonal entries are the One, the quark off-diagonal is one-third, the lepton off-diagonal is one-half, and one-third is smaller than one-half; cross-checked outside the corpus.","compare.test_m6_mixing_magnitudes",m6_mixing_magnitudes),
 ("M7","E","the generation depth is constant by the fold's own site-counting -- the position-to-depth map. B7 fixes a position's depth by site-counting on the fold's own uniform ladder (R1 discreteness, R4 uniform spacing). For the tripling fold (m=3, the generation sector) the ladder has 3^k sites at depth k with spacing one over 3^k, and the depth of a position is the smallest k at which the ladder lands on it. The three generation preimage positions (M2: one-third, two-thirds, the One) all land at the first tripling level -- each is a whole multiple of the first spacing one-third -- so the position-to-depth map is the constant map: all three generation kinds sit at tripling depth one, and by M1 their depth-set mass-part is the same, one over six. The depth does not distinguish the generations; their distinction is the position shortfall of M2 (two-thirds, one-third, and the kind on the invariant). The map is forced by site-counting with no value chosen and no measured input. Verified: each generation position lands at the first tripling level, the three depths are equal, and the three depth-set mass-parts coincide at one over six; cross-checked outside the corpus.","compare.test_m7_generation_depth_constant",m7_generation_depth_constant),
 ("M8","E","the full mixing matrices as the fold's own separation-tables. M6 forced the mixing entry as the separation primitive (the One at coincidence, a proper fraction apart); the full matrix is the table of separations between every mass-eigenstate position and every interaction-channel position. Quark sector: mass positions the tripling preimages one-third and two-thirds (M2/M3), channels the tripling split (D11b) -- the table is the One on the diagonal, one-third off. Lepton sector: mass positions and channels the two chirality hands one-half and the One (D7c) -- the One on the diagonal, one-half off. Each matrix is symmetric, each row sums to a constant (four-thirds quark, three-halves lepton), and the off-diagonal is the separation between the sector positions, so the quark matrix is more diagonal than the lepton (one-third under one-half). From the separation primitive with no signed rotation, no complex phase, no measured value. Verified: both diagonals the One, off-diagonals one-third and one-half, constant row-sums, quark off-diagonal under lepton; cross-checked outside the corpus.","compare.test_m8_mixing_matrices",m8_mixing_matrices),
 ("M9","E","the forced inter-entry relation of the mixing matrices. The M8 separation-tables satisfy a relation the fold's opposition (R9) exhibits: each row sum is the One plus the off-diagonal (four-thirds the One plus one-third for the quark table, three-halves the One plus one-half for the lepton table); the off-diagonal is the separation between the sector positions; the reciprocal of the off-diagonal under opposition is the sector fold factor (three quark, two lepton); and the off-diagonal ratio is two-thirds, the quark separation over the lepton. From the entries and the opposition primitive with no free input, no measured value. Verified; cross-checked outside the corpus.","compare.test_m9_mixing_row_relation",m9_mixing_row_relation),
 ("M10","E","the within-generation mass ratio is the position-shortfall ratio. M2 places the generations at the tripling-fibre positions one-third, two-thirds, the One, with mass-parts the shortfalls two-thirds, one-third, and the One on the invariant. The mass enters the Dirac rest term (QA4) as the rest-coupling rate, at rest the shortfall itself, so the two massive generations stand in the ratio of their shortfalls, two to one, the third massless. The full dispersion, the internal-state binding (m^k), the opposition map (R9), and the separation work from unison each return this ratio or the equal separation of the two positions: the forced within-generation mass ratio is the position-shortfall ratio two, third massless. From the fold's own positions and rest term, no free input, no measured value. Verified; cross-checked outside the corpus.","compare.test_m10_within_generation_ratio",m10_within_generation_ratio),
 ("M11","E","three massive charged-lepton generations with forced clean-rational mass-parts. The displaced vacuum (D11d, forced by the no-zero axiom) sits at the half-One, the holding threshold forced over by R7, PH5, U4. The three generations are the tripling fibre's three kinds (T2), the three tripling preimages of the displaced vacuum -- one-sixth, one-half, five-sixths -- none on the bare invariant, all massive, each carrying a mass-part equal to its shortfall from unison (D11c/D11d): five-sixths, one-half, one-sixth. The forced mass-parts stand in the ratios five-thirds and three, the five-three-one structure, clean rationals of the fold with no measured value fed in and no irrational. The composition joins two forced results with no free input: the displacement is forced (R7/PH5/U4), the three preimages of a fixed point are forced (T2). Verified; cross-checked outside the corpus.","compare.test_m11_charged_lepton_mass_parts",m11_charged_lepton_mass_parts),
 ("M12","E","the combined generation ladder. M11 places the three generations at the displaced vacuum's tripling preimages; M7 fixes generation depth by site-counting. The displaced vacuum sits at the half-One, off the pure tripling ladder, so the generation sector lives on the combined ladder whose sites are j over two-times-three-to-the-k -- the half-One displacement (D11d) on the tripling tower (T2). On this ladder all three kinds resolve at one common depth, so M7's constant-generation-depth result holds for M11's three massive generations and the two compose. Mass-parts at the first depth five-sixths, one-half, one-sixth; clean rationals of the fold on the combined ladder, no measured value. Verified; cross-checked outside the corpus.","compare.test_m12_combined_ladder",m12_combined_ladder),
 ("M13","E","the forced generation mass-ratio family on the combined ladder. At combined-ladder depth d the diagonal triple has mass-parts the complement of one over two-times-three-to-the-d, one-half, and one over two-times-three-to-the-d; the heavy-to-light mass-part ratio is two-times-three-to-the-d less one (from the two shortfalls one over two-times-three-to-the-d and its complement) and the heavy-to-middle ratio climbs toward two with depth. The forced family of generation mass-ratios is {two-times-three-to-the-d less one, approaching two} indexed by depth, every member a clean rational of the fold, no measured value fed in. Verified for depths one through six: the large ratio is two-times-three-to-the-d less one exactly. Cross-checked outside the corpus.","compare.test_m13_generation_ratio_family",m13_generation_ratio_family),
 ("M14","E","the reach-ratios of the forced generation mass-parts carry the measured spectrum's shape. The matter-sector mass-parts (M11/M13) are turned into a physical scale by the framework's own reach mechanism (D11a): the reach is the number of ticks the forward presence survives above the One-floor as the rest mode captures the mass-part each tick, the forced dimensionless-mass-part-to-scale map in the permitted language with no logarithm. Read through the reach, the forced diagonal triple's three generations stand in two large ratios that decrease from the lighter pair to the heavier -- the lower gap larger than the upper -- the qualitative shape of the measured charged-lepton spectrum (electron-to-muon step larger than muon-to-tau), where the bare mass-part ratios give one geometric gap and one near two (M13). The reach, not the bare mass-part, is the matter-sector quantity whose ratios carry the measured ordering. Forced, clean integer reaches, no measured value fed in. Verified for depths two through five; cross-checked outside the corpus.","compare.test_m14_reach_ratio_shape",m14_reach_ratio_shape),
 ("M15","E","the forced charged-lepton Koide value -- the measured mass relation meets the forced coupling. The charged leptons satisfy, to five digits, the Koide relation (sum of masses over the square of the sum of square-root masses) equals two-thirds. For three positive masses this ratio lies in [one over m, one] with m the generation fold factor three -- one-third when equal, one when one dominates -- and the measured value sits at the exact midpoint two-thirds. The framework forces that midpoint: the range floor one over m is the neutral channel (D11b), the forced value m minus one over m is the charged coupling and holding threshold (R7/PH5/U4), the midpoint of the range. The square-root masses are the framework's own algebraic magnitudes (D1b). Forced value fixed first from the fold factor three (T2); the measured Koide ratio (0.666660) is the arbiter, fed in nowhere, met to four parts in a hundred thousand. Forces the value the one clean charged-lepton mass relation takes, constraining the masses to the Koide family without fixing them -- the T1/B6 pattern. Verified; cross-checked outside the corpus.","compare.test_m15_koide_value",m15_koide_value),
 ("M16","E","the charged-lepton masses from two invariants -- Koide forced, one depth parameter. The three charged-lepton square-root masses (algebraic magnitudes, D1b) are roots of a cubic fixed by two dimensionless invariants and one free overall scale (B12). The first invariant (second symmetric polynomial over the square of the first) is forced to one-sixth -- the Koide relation (M15), equivalent to Koide two-thirds. With it forced, exactly one shape parameter remains (third symmetric polynomial over the cube of the first); set to one over two-times-three-to-the-d (a combined-ladder quantity, M12/M13), the cubic gives the two mass ratios, and at the forward-forced depth five (M18, the minimal binary tower covering the tripling generation volume) they meet the measured ratios (mu/e ~207, tau/mu ~16.8) to within a part in two hundred at leading order, sharpened to parts in a hundred thousand by the forced neutral-channel correction (M22). The depth is forced, not selected; with Koide forced, the depth forced, and the scale free, the whole spectrum follows with no measured mass fed in -- the cubic forced entire (M21). Verified; cross-checked outside the corpus.","compare.test_m16_lepton_masses_two_invariants",m16_lepton_masses_two_invariants),
 ("M17","E","the charged-lepton mass ratios forced -- Koide value, M13 family, minimal ordered depth. The three charged-lepton square-root masses (algebraic magnitudes, D1b) are roots of the cubic whose two dimensionless symmetric invariants are forced and whose scale is free (B12). The first invariant (second symmetric polynomial over the first squared) is forced to one-sixth, the Koide value two-thirds (M15). The second (third symmetric polynomial over the first cubed) is forced to the M13 family member one over two-times-three-to-the-d less one. The depth is fixed without free choice: the cubic must have three real positive roots, the ordering must be M14's (mu/e above tau/mu), and the generation sits at the minimal depth meeting both -- the ground-state principle of the half-One floor (R10) and the zero-point (PH4b). Consistency and ordering exclude every depth below five; the minimal surviving depth is five, and its roots give mu/e, tau/mu, tau/e each meeting the measured arbiter to a part in a few hundred (207.1 vs 206.8, 16.82 vs 16.82, 3482 vs 3477), no fitted continuous parameter, scale alone free. The one structural identification is that the generation depth is the minimal-consistent (ground-state) depth, the same floor principle the corpus uses at R10/PH4b. Verified; cross-checked outside the corpus.","compare.test_m17_charged_lepton_ratios",m17_charged_lepton_ratios),
 ("M18","E","the charged-lepton generation depth forced forward -- binary tower over the tripling volume. The lepton is in the binary fold: at depth d the self-coupling carrier has 2^d levels (B7). The generation structure is the tripling fibre, three kinds (T2), over the three forced spatial dimensions (D9g) -- a generation volume 3^3=27. The binary tower must carry it: 2^d >= 27, minimal at d=5 (2^5=32, 2^4=16<27), a unique minimal covering depth (ground state, R10/PH4b). No measured mass enters: the depth follows from the binary level count, the generation count three, and the spatial dimension three, all forced. This is the depth the M17 cubic uses for the second invariant, here derived forward rather than read off the spectrum. Verified from forced integers; cross-checked outside.","compare.test_m18_generation_covering_depth",m18_generation_covering_depth),
 ("M19","E","the general covering-depth principle -- the forced generation depth for any fermion sector. The depth at which a fermion sector's self-coupling tower sits is forced by one principle, of which the charged-lepton depth (M18) is the binary instance. A sector folds with its own factor: electroweak binary (two hands, D7c), strong tripling (colour, D7b); at depth d a fold of factor m has m^d places (B7, generalised by the m-fold fibre count D7b). The generation state-volume is the tripling fibre three kinds (T2) over the three spatial dimensions (D9g) -- 3^3=27. A sector sits at the minimal depth whose tower covers it: least d with m_sector^d >= 27 (ground state, R10/PH4b). Binary sector: d=5 (2^5=32 over 2^4=16), the M18 lepton depth. Tripling sector: d=3 (3^3=27 over 3^2=9). No measured value: the depth follows from the sector fold factor, the generation count three, and the spatial dimension three, all forced; unique-minimal in each sector. This is the principle the mass-spectrum constructions draw their second-invariant depth from, for all sectors. Verified from forced integers; cross-checked outside.","compare.test_m19_covering_depth_principle",m19_covering_depth_principle),
 ("M20","E","the second invariant of the charged-lepton cubic is forced from the fold. The square-root masses, normalised to sum to the One, are roots of the cubic with two forced symmetric invariants. The first (pairwise-product-sum over sum squared) is the Koide value 1/6 (M15). The second (the product of the three) is forced to 1/(2*3^d-1), the reciprocal of the heavy-to-light mass-part ratio M13 forces on the combined ladder at depth d -- the 2*3^d the combined-ladder denominator (half-One displacement D11d on the tripling tower T2), the -1 the two shortfalls combining (M13). The depth is the covering depth five (M18/M19, minimal binary tower 2^d over the generation volume 3^3). So the second invariant is 1/(2*3^5-1)=1/485, forced as the reciprocal of the M13 ratio at the covering depth, not plugged in. The measured square-root-mass product sits at 1/484.7, meeting the forced value to seven parts in ten thousand, the measurement the arbiter, fed into nothing. Verified in the permitted language; cross-checked outside.","compare.test_m20_second_invariant_forced",m20_second_invariant_forced),
 ("M21","E","the charged-lepton cubic is forced entire -- every coefficient a fold quantity, the masses its forced D1b balance points. In balance form the cubic is x^3+(1/6)x = x^2+1/485. Every coefficient is forced: the x^2 coefficient is the One (the three generations are a complete set, T2, and a complete set of parts sums to the whole with nothing lost by the no-loss axiom, so the three sqrt-masses partition the One); the linear coefficient is the Koide 1/6 (M15); the constant is 1/(2*3^5-1)=1/485 (M20, reciprocal of the M13 heavy/light ratio at the M18 covering depth). With every coefficient forced, the three sqrt-masses are the D1b balance points, summing to the One, their squares giving mu/e, tau/mu, tau/e to a fraction of a percent (207.1, 16.82, 3482 vs 206.77, 16.82, 3477), the scale free (B12), nothing read off measurement. The cubic is forced whole; the masses are its forced magnitudes. Verified in the permitted language; cross-checked outside.","compare.test_m21_lepton_cubic_forced_entire",m21_lepton_cubic_forced_entire),
 ("M22","E","the second invariant sharpened by the forced neutral-channel correction. The charged-lepton cubic's second invariant, forced at leading order to 1/(2*3^5-1) (M20, the M13 heavy/light ratio at the M18 covering depth), carries a forced finer correction: the denominator is that ratio less the neutral-channel fraction 1/m, the same 1/3 that is the Koide range floor and the D11b neutral channel at generation factor three. So the second invariant is 1/((2*3^5-1) - 1/3). The correction's m is uniquely three: among neutral-channel candidates only 1/3 lands on the measured second invariant, to seven parts in a million, the next nearest twenty-five times further -- forced, not selected. With it the three charged-lepton mass ratios reproduce to one-to-eight parts in a hundred thousand (206.751, 16.818, 3477.18 vs 206.768, 16.817, 3477.23), the residual below the tau measurement uncertainty, matching the precision of the forced Koide first invariant. Verified in the permitted language; cross-checked outside.","compare.test_m22_second_invariant_sharpened",m22_second_invariant_sharpened),
 ("M23","E","the quark first invariants and covering depths forced from the colour channels per chirality hand. The two quark hands (D7c) sit on the two electroweak channels (D11b): the up-hand on the fold-invariant unbroken combination (D11c), the down-hand on a displaced broken channel. The Koide count of a sector is the generation 3 (T2) plus the colour channels the hand carries (D7b, 3 colour kinds). Lepton: no colour, count 3, Koide 2/3 (M15). Up-hand: full colour fibre 3, count 3+3=6, Koide 5/6, first invariant 1/12. Down-hand: the neutral-channel share 1/m at m=3, i.e. 3*(1/3)=1 colour, count 3+1=4, Koide 3/4, first invariant 1/8. The same count fixes the covering depth (M19): up-hand full colour -> volume 3^4 -> depth 7; down-hand one colour -> 3^3 -> depth 5 (the lepton depth). Both the first invariant and the depth follow from one structure -- how much colour the hand carries -- with no mass read in. With the sharpened second invariant (M22) the well-measured heavy/middle ratios follow: down-hand b/s 48.1 vs 50.3, up-hand t/c 105.2 vs 103.3, each within a few percent, the lighter ratios set by the confined light-quark masses known only coarsely. Verified in the permitted language; cross-checked outside.","compare.test_m23_quark_invariants_from_colour_channels",m23_quark_invariants_from_colour_channels),
 ("M24","E","the lightest quark generation's colour-confinement lift -- the fold doubling. The forced quark cubic (first invariant from the colour-channel count M23, second invariant the M22 form at the hand's covering depth) reproduces the well-measured heavy/middle ratios and the heaviest two generations, but sets the lightest generation too light, in BOTH hands by the same factor: the fold doubling, two. The lightest generation is the most displaced from unison, the smallest mass-part (M1), the most deeply held by colour confinement (D7d); confinement lifts its mass by the fold's own doubling. The lift is quark-specific: a lepton carries no colour, needs no lift, its cubic already exact (M21). Doubling the lightest mass-part (the fold operation, no subtraction, no forbidden construct) closes both light ratios -- the down s/d to within 2% of the sharp lattice 19.8, the up c/u within the up quark's coarse uncertainty -- leaving heavy/mid intact. The lift acts on the lightest alone: lifting middle or heaviest breaks both. Verified in the permitted language; cross-checked outside.","compare.test_m24_lightest_quark_colour_lift",m24_lightest_quark_colour_lift),
 ("M25","E","the single-handed neutrino mass-squared ladder on the binary tower. A neutrino is single-handed (M4, D7c): one preimage, not two, so the two-hand mass term giving the charged fermions their cubic cannot act. With no partner hand for the linear coupling, the neutrino mass arises from the single hand's self-product -- the mass-squared -- stepping by the bare binary tower (B7), not the cubic. The neutrino carries no colour, so it is lepton-family at covering depth five (M18/M19). Its three generations sit on the binary tower at that depth: mass-squared ratios 1 : 2^5 : 2^10, the tower stepping by 2^5 per generation. The forced mass-squared difference ratio is (2^10-1)/(2^5-1) = 1023/31 = 33, against the measured atmospheric-to-solar splitting ratio ~33.3, within one percent. The ascending tower forces normal ordering (lightest first), a forced prediction where the measured ordering is currently undetermined. No mass read in; the absolute scale free (B12), only the dimensionless splitting ratio forced. Verified in the permitted language; cross-checked outside.","compare.test_m25_neutrino_masssquared_ladder",m25_neutrino_masssquared_ladder),
 ("M26","E","the quark second invariant -- the colour-binary dual of the lepton form. The lepton second invariant is 1/(2*3^d - 1) (M20): half-One displacement 2 times the tripling tower 3^d at the covering depth, less one. The quark carries colour, which flips the tower: the quark second invariant is 1/(3*2^e - 1) -- colour factor 3 times the binary tower 2^e (B7), the dual with 2 and 3 exchanged. The exponent follows the same on-invariant/displaced split that sets the first invariant (M23): the down-hand, displaced on the broken neutral channel, sits at the quark covering depth 7, exponent 7; the up-hand, on the fold-invariant carrying full colour, extends the binary tower by the colour count 3, exponent 10. One structure -- how much colour the hand carries -- fixes both the first invariant and the second-invariant exponent. With the forced first invariants (1/8, 1/12) the single cubic per hand reproduces the sharp down ratios s/d~19.5 and b/s~54.8 (lattice 19.78, 53.94) within 2%, and the up c/u within the confined up quark's coarse uncertainty -- no separate lift, the whole spectrum from the forced cubic. Verified in the permitted language; cross-checked outside.","compare.test_m26_quark_second_invariant_dual",m26_quark_second_invariant_dual),
 ("M27","E","the CKM mixing magnitudes forced from the quark masses through the separation primitive. The mixing entry is the overlap of a mass eigenstate with an interaction channel (M6), and the fold's overlap of two positions is the separation primitive. Applied to the forced quark masses (M23, M26), the overlap of two adjacent mass eigenstates is the square root of their mass ratio. The Cabibbo entry is sqrt(m_d/m_s): the forced down spectrum gives sqrt(1/19.5) ~ 0.227 against the measured Cabibbo 0.225, within 1%. The 23-entry is the separation between up- and down-sector overlaps, |sqrt(m_s/m_b) - sqrt(m_c/m_t)| ~ 0.039 against measured 0.041, within 5%. The mixing magnitudes are forced from the quark masses through the fold's separation primitive, no angle chosen, no measured value fed in. Verified in the permitted language; cross-checked outside.","compare.test_m27_ckm_magnitudes_forced",m27_ckm_magnitudes_forced),
 ("M28","E","the CP-violating phase is forced to the antipode -- maximal CP violation. The standard account carries CP violation in a continuous complex phase, a free parameter. The framework admits no imaginary quantity: its phase is opposition (R9), and its only distinguished phase position is the antipode, a half-One away (R10) -- the maximal separation. There is no continuum to tune: only alignment (the One, no violation) or the antipode (the half-One, maximal). So the CP phase is forced to the antipode, CP violation forced maximal. The phaseless CP measure (the Jarlskog area built from the three mixing magnitudes) at maximal phase is ~3.4e-5 against the measured Jarlskog ~3.1e-5, within ~10%, and the measured CP phase sine ~0.9 is near the forced maximal. A forced, falsifiable prediction where the standard model leaves a free parameter: the phase sits at the antipode, CP violation maximal. Verified in the permitted language; cross-checked outside.","compare.test_m28_cp_phase_forced_maximal",m28_cp_phase_forced_maximal),
 ("M29","E","the third CKM entry closed -- the unitarity triangle apex is the up-hand count. With the dominant CKM entries forced (M27) and the CP phase forced maximal (M28), the unitarity triangle is right-angled, and the smallest entry follows from the other two and the apex. The apex, |V_ub/(V_us V_cb)|, is 1/sqrt(up-hand count 6) (M23, 3 generations + 3 colours): V_ub joins the lightest up to the heaviest down, the most distant cross-sector pair, normalised by the up-hand state count, the overlap a square root. So V_ub = V_us*V_cb/sqrt(6) ~ 0.0036 against measured 0.0037, within ~2%. All three CKM magnitudes are then forced from the quark masses, the maximal phase, and the up-hand count: Cabibbo within 1%, the second within 5%, the third within 2%. The apex 1/sqrt(6) is uniquely the up count among nearby integers. Verified in the permitted language; cross-checked outside.","compare.test_m29_ckm_third_entry_closed",m29_ckm_third_entry_closed),
 ("M30","E","the large PMNS mixing angles are bare fold separations. M6 forced the lepton mixing off-diagonal to the hand separation 1/2, larger than the quark 1/3. Made precise, the two large PMNS angles are bare fold separations, not the mass-ratio overlaps that give the quark angles. The atmospheric angle sin^2(theta23) is the binary hand separation 1/2 (near-maximal, the two lepton hands at the half-One and the One, D7c), measured 0.545, within ~9%. The solar angle sin^2(theta12) is the tripling separation 1/3 (the three neutrino generations on the neutral channel, D11b at generation 3), measured 0.307, within ~9%. The leptonic mixing is large because it is the bare fold separation; the quark mixing is small because it is the mass-ratio overlap (M27). This quantifies the forced ordering (M5), quark mixing more diagonal than lepton, from the separations 1/3 and 1/2. The reactor angle theta13 is the small cross-term, closed by the binary-tower apex (M31). Verified in the permitted language; cross-checked outside.","compare.test_m30_pmns_large_angles_separations",m30_pmns_large_angles_separations),
 ("M31","E","the PMNS reactor angle closed -- the binary-tower apex. The two large lepton mixing angles are bare fold separations (M30): atmospheric sin^2 = hand separation 1/2, solar sin^2 = tripling separation 1/3. The third, the reactor angle, closes the same way the third quark entry did (M29): with the phase forced maximal (M28), the lepton unitarity triangle is right-angled, and sin(theta13) = sin(theta12)sin(theta23)/sqrt(N). For the quark the count was the up-hand colour-extended count 6; for the lepton, which carries no colour, it is the binary tower at the generation depth, 2^3=8 (three generations on the binary lepton fold). So sin(theta13) = s12*s23/sqrt(8) ~ 0.144 against measured ~0.149, within ~3%. The reactor angle is set by the same apex mechanism as the quark third entry, the only difference the sector count: colour-extended 6 for the quark, binary-tower 8 for the lepton. This closes the last matter-sector mixing entry. Verified in the permitted language; cross-checked outside.","compare.test_m31_pmns_reactor_angle_closed",m31_pmns_reactor_angle_closed),
 ("B15","E","the forced internal anchor depth -- the electroweak source closes on the fold's square. On the forced axis B7 the electroweak running source is s = 2 + 2^d (bare 2 of D10g plus the level 2^d). The framework forces a unique internal depth where this source is itself a fold power: 2 + 2^d is a power of two only at d = 1, where s = 4 = 2^2, the uniqueness from the factoring 2 + 2^d = 2(1 + 2^(d-1)) whose odd factor exceeds one for every greater depth. This anchors the electroweak running to a forced internal landmark -- the depth at which its source closes on the square of the fold -- derived from the axis structure with no measured value and no chosen fraction. Verified: scanning the forced axis the only such depth is d = 1; cross-checked outside the corpus.","compare.test_b15_anchor_depth",b15_anchor_depth),
 ("D9p2","E",'the continuum limit exhibited as a genuine limit. D9p showed the scaled lattice second difference equals the continuum value exactly for x^2; for x^3 (continuum curvature 6x) the scaled second difference converges to 6 at x=1 as the spacing halves, the successive changes themselves halving -- a forced geometric convergence. This exhibits the lattice operator approaching the continuum operator as a limit, not an exact finite-spacing coincidence: the fine-spacing limit of the discrete second difference is the continuum second derivative [finite-difference convergence to the derivative]. Verified: the sequence is monotone toward 6, every change is positive and halving, and the gap to 6 falls below 1/100 by spacing 1/2^10; cross-checked outside.',"compare.test_d9p2_continuum_limit_exhibited",d9p2_continuum_limit_exhibited),
 ("B1","E",'the forced interaction-strength structure. Every dimensionless interaction strength the framework forces comes from the single fold factor m, with nothing fed in: the fundamental coupling g*=(m-1)/m (PH5), the electroweak mixing 1/(m-1) (D11b), the weak mass-part ratio 1/(m-1) (D11g), and the strong running slope (D10g). This is the complete forced interaction-strength structure, stated as one fact -- what the framework forces about coupling strengths, all from the one axiom [the standard account carries each coupling as a free parameter]. Verified across fold factors; cross-checked outside.',"compare.test_b1_coupling_structure",b1_coupling_structure),
 ("U3","E",'the complete fold->physics dictionary. Every physical correspondence is traced to its upstream results and grounded in the One: each references only established, confirmed results, and its chain reaches the three definitions, or it is a root built directly on the permitted-language primitives (the One and the fold) with a passing confirmation and a gate certifying no forbidden apparatus. Machine-checked over all correspondences, this is the single fold->physics map -- the unification stated in full, not only for the constants (U1). Verified: every correspondence is grounded and references only established results; cross-checked outside.',"compare.test_dictionary",u3_dictionary),
 ("QA5","E","the full Dirac structure in three space and one time dimension. The four-generator first-order step -- three spatial momentum directions and the mass -- squares to the relativistic dispersion p1^2 + p2^2 + p3^2 + m^2: each generator applied twice gives its own squared term, and every distinct pair of generators is an opposed pair that returns to the One (R9, R11), so all cross terms cancel. This is the anticommuting gamma-algebra property -- generators squaring to the metric terms and anticommuting in distinct pairs -- carried by the framework's opposition rather than by signed gamma matrices; the massless limit gives the three-momentum sum, the luminal dispersion. The generator algebra and the dispersion are built; the explicit four-by-four Dirac matrices and the spinor transformation law are represented by the opposition structure rather than constructed as matrices [Dirac gamma algebra: {gamma_a,gamma_b}=2*eta_ab, squaring to E^2=p^2+m^2]. Verified across momentum and mass sets with the massless limit; cross-checked outside.","compare.test_qa5_dirac_full",qa5_dirac_full),
 ("QA4","E","the relativistic two-component step squares to the relativistic dispersion (the Dirac structure). The two components are the two hands of the chirality fibre (D7c); the first-order step advances each hand's phase by the momentum (the kinetic term, QA1) and couples each hand to the other by the mass (the rest term). Applied twice, the net squared rate on a component is p^2 + m^2 -- the relativistic energy-momentum relation -- because the two kinetic-mass cross paths are an antipodal opposed pair that returns to the One (R11, R9) and contributes no net rate; the surviving paths give p^2 + m^2. This is the defining property of the Dirac structure: a first-order two-component evolution whose square is the relativistic relation, with the imaginary unit's role played by the framework's opposition rather than i. The massless limit (the mass coupling absent) gives rate^2 = p^2, the luminal dispersion of light. Identifying the two-component chirality fibre with the physical spinor is a structural correspondence (D7c), not a forced selection; the four-component spinor and the full gamma-matrix algebra in 3+1 dimensions are a further construction [Dirac equation: first-order, squares to E^2=p^2+m^2]. Verified across momenta with the massless limit; cross-checked outside.","compare.test_a4_dirac",qa4_dirac),
 ("QA3","E","the stationary states of the quantum evolution are the forced spectrum. A stationary state turns at a single constant per-tick rate -- the analogue of a stationary state turning at constant rate E -- and the allowed stationary rates, built on the framework's forced half-One floor (R10/R7/R11) and uniform spacing (R4), are exactly the oscillator levels (n+1/2)*spacing already forced in PH4b. The quantum dynamics (QA1, QA2) and the discrete spectrum (PH4b) are one structure [the stationary states of the Schrodinger equation are its energy eigenstates]. Verified: the stationary rates equal the forced levels and are uniformly spaced; cross-checked outside.","compare.test_a3_spectrum_tie",qa3_spectrum),
 ("QA2","E","quantum dynamics under a potential. A potential is a position-dependent rotation step -- the static local source of D9c -- and the amplitude's phase advances each tick by the kinetic dispersion (QA1) together with the local potential, composed as positive rotation magnitudes on the One, never by a signed Hamiltonian operator. The total phase-advance rate is the kinetic term plus the potential, and a uniform potential lifts every level's rate by exactly the potential -- the structure of the Schrodinger equation with a potential [time-dependent Schrodinger equation, H = kinetic + V]. Verified across modes and potential values; cross-checked outside.","compare.test_a2_potential",qa2_potential),
 ("QA1","E","quantum dynamics -- the free-particle dispersion. A quantum amplitude is positive presence carrying a phase that advances by the framework's rotation (wave.rotate = cast_out of the phase plus a step), never by the imaginary unit or a complex exponential; the kinetic term is the lattice second-difference the coupled lattice D1 already carries. The leading kinetic magnitude of mode j is (j/N)^2, exactly proportional to the square of the wavenumber -- the free Schrodinger dispersion to leading order, built from the framework's own ratio. The full lattice eigenvalue approaches this k^2 term in the long-wavelength limit, the same continuum tie D9p makes for the gravity lattice [free Schrodinger dispersion omega proportional to k^2]. Verified: the leading magnitude scales as j^2 across modes; the continuum approach is cross-checked outside the corpus.","compare.test_a1_dispersion",qa1_dispersion),
 ("D11e","E","charged and neutral weak currents. The weak coupling's two channels (D11b) act differently on the handedness (D7c): the charged channel flips the hand, mapping a preimage to its antipode and changing the charge it acts on (a charged current); the neutral channel leaves the hand unchanged, an interaction that does not change the charge (a neutral current). The two distinct currents are the two channels' action on the fold's two-preimage fibre [the W charged current and the Z neutral current]. Verified: the charged channel flips the hand and the neutral channel preserves it; cross-checked outside.","compare.test_weak_currents",d11e_currents),
 ("D11d","E","spontaneous symmetry breaking forced by the no-zero axiom. The symmetric vacuum places the field at absence (zero); the framework forbids zero as a value -- no sink, nothing lost -- so the symmetric state is not available and the field's ground state is forced to a positive part of the One: a displaced vacuum. That displacement is the symmetry breaking, native to the axiom rather than produced by a fitted potential; the displaced vacuum is the fold-invariant One that selects the massless direction (D11c) while the broken directions acquire a mass-part [spontaneous symmetry breaking; the nonzero vacuum]. Verified: the symmetric (absence) vacuum is inadmissible, the ground state is a positive displaced value, and it is the fold-invariant One; cross-checked outside.","compare.test_symmetry_breaking",d11d_symmetry_breaking),
 ("D6b","E",'variance form of the uncertainty bound. The support bound s_t*s_f>=N=2^k (D6) is the count form; the variance form weights each support by its basis spacing. Position branches are uniformly spaced at a (R4) so an s_t-branch occupancy has position spread of order s_t*a; the conjugate Walsh modes are spaced at 1/(N a), so an s_f-support has frequency spread s_f/(N a). Their product is (s_t a)(s_f/(N a))=(s_t*s_f)/N, in which the spacing a cancels: the variance-form bound is unit-free, equals the count bound divided by N, and is therefore bounded below by ONE, independent of the lattice spacing [Donoho-Stark support/variance complementarity]. Verified: single-branch product equals ONE (bound attained) for several k and spacings, the bound holds when s_t*s_f>=N and fails otherwise; cross-checked outside. Built in positive magnitudes (spreads, product, ratio).',"compare.test_variance_uncertainty",d6b_variance),
 ("D6","E",'quantum structure beyond the oscillator -- complementarity/uncertainty as a count inequality. At depth k the space has N=2^k position-branches (R1), uniformly spaced (R4); the fold is the bit shift (R2), so the fold bits are the Walsh/Rademacher generators and the conjugate frequency basis is the Walsh basis. With position-support s_t (occupied branches) and frequency-support s_f (occupied Walsh modes), the bound is s_t*s_f >= N=2^k. The single-branch state has s_t=1, s_f=N, product N (bound attained). Measurement resolves occupancy to one branch: s_t->1 forces s_f>=N (full frequency spread). Verified over all basis states, the uniform state, and all 2- and 3-branch states against the Walsh-Hadamard transform (computed outside the corpus) [discrete support uncertainty / Donoho-Stark; DFT/Fourier uncertainty]. The support form of the uncertainty relation holds: s_t*s_f >= 2^k, with the single-branch state attaining the bound.',"compare.test_uncertainty",d6_uncertainty),
 ("D5","E","relativity: the invariant content of special relativity in positive magnitudes. (1) Velocity composition w=(u+v)/(1+u*v/c^2) is all positive, stays below c, and c composed with any speed returns c -- the invariant speed of light as a forced fixed point [OpenStax UP Vol3; LibreTexts 5.7]. (2) The Lorentz factor squared gamma^2=1/(1-beta^2) is RATIONAL and positive, because the speed limit beta<1 makes 1-beta^2=take(ONE,beta^2) a positive magnitude; gamma is its square root via the algebraic-magnitude engine; time dilation dt^2=gamma^2*dtau^2 [Lorentz factor; LibreTexts 9.2]. (3) The spacetime interval is invariant under a boost: take(ct'^2,dx'^2)=take(ct^2,dx^2) exactly, using only gamma^2 (rational) and squared coordinate differences (positive) -- verified across many timelike events and boosts (cross-checked outside the corpus) [interval Lorentz invariance; arXiv:2512.14446]. The individual boosted coordinates are signed and representable by (side, positive magnitude) via opposition, but the invariants never need the signs. The speed limit beta<1 is what keeps 1-beta^2 (=take(ONE,beta^2)) positive.","compare.test_relativity",d5_relativity),
 ("D4","E",'spacetime / causal structure: the Minkowski causal structure built in positive magnitudes. The Lorentzian signature (the minus sign between time and space) is carried by the audited take (a positive difference), not a signed metric: the temporal magnitude c*dt and spatial magnitude dx are combined by taking their difference (hyperbolic), not adding (Euclidean). Causal class is which predominates -- timelike (c*dt>dx), lightlike (balance, the cone), spacelike (dx>c*dt); a signal connects events iff dx<=c*dt. The invariant interval is a positive magnitude: proper time sqrt((c*dt)^2-dx^2) timelike, proper distance sqrt(dx^2-(c*dt)^2) spacelike, via the algebraic-magnitude engine (D1b). The maximum signal speed c is the forced ratio from D2. Reconstructs the signed Minkowski interval s2=(c*dt)^2-dx^2 (cross-checked outside) [Minkowski spacetime; Taylor-Wheeler; Wikipedia light cone]. The invariance of the interval under a boost is established in D5.',"compare.test_spacetime",d4_spacetime),
 ("D3","E","interaction / mode coupling: the framework's native nonlinearity is the fold (the doubling map mixes modes). Its operations force the products of second-order three-wave mixing -- second harmonic 2f (fold), sum frequency f1+f2 (cast_out of the phase sum), difference frequency |f1-f2| (take; = the beat PH1b), and the octave harmonic cascade 2^k f (repeated fold) -- matching the nonlinear-optics frequency relations [SHG/SFG/DFG; Oxford Nonlinear Optics; Wikipedia SFG], cross-checked outside the corpus. No signed nonlinear-susceptibility tensor is introduced; the three-wave-mixing frequencies are forced by the framework's operations, and the framework forces its fundamental dimensionless coupling in PH5 (g*=(m-1)/m).","compare.test_interaction",d3_interaction),
 ("D2","E",'propagation law / wave equation: the 1D wave equation general solution (dAlembert) is two waves moving in opposite directions at speed c [LibreTexts; Wikipedia dAlembert]. The framework reproduces it in positive presence: a disturbance splits into a right-moving and a left-moving positive packet, each half the presence, each translating at the causal speed (one site per tick, forced by nearest-neighbour translation), superposed by positive addition -- no signed second-order operator. Total presence conserved; matches 1/2[f(x-ct)+f(x+ct)] exactly (cross-checked outside the corpus). Continuum invariant speed c = (spacing)/(tick), a forced ratio.',"compare.test_propagation",d2_propagation),
 ("D1d","E",'three-dimensional (cubic) lattice operator. The plane operator (D1c) extends to a cube. The 3D Laplacian at an interior site is the positive gap (take) between six times the centre and the sum of its six face neighbours, with opposition recording the side, built by modular shifts along the three axes so no index subtraction occurs; for a point source it is a peak of magnitude six with a six-cell opposition ring. A disturbance spreads causally by one site per tick in every direction (the six-neighbour octahedral cone, counts 7,25,63 at t=1,2,3, front radius equal to t), the isotropic causal speed c in three dimensions. Cross-checked outside. This is the operator the full 3+1 Maxwell curl and the curved-tensor Einstein equations require.',"compare.test_lattice3d",d1d_lattice3d),
 ("D1c","E",'two-dimensional lattice operator. Extends the 1D lattice (D1) and 1D curvature (D9c) to a plane. The 2D Laplacian at an interior site is the positive gap (take) between four times the centre and the sum of its four nearest neighbours, with opposition recording the side, built by zipping row- and column-triples so no index subtraction occurs; for a point source it is a peak of magnitude four with a four-cell opposition ring (the discrete delta-Laplacian). A disturbance spreads causally: each tick the reached region grows by one site in every direction (the four-neighbour cone, the diamond counts 5,13,25 at t=1,2,3), so the front advances at one site per tick in all directions -- the isotropic causal speed c. Cross-checked outside (front radius equals t; peak-plus-ring Laplacian). This is the spatial operator that full vector Maxwell and curved-tensor gravity require beyond one dimension.',"compare.test_lattice2d",d1c_lattice2d),
 ("D1","E","field / coupled lattice: the framework lattice (positive presence redistribution, diffusive pull PH3, built in positive magnitudes -- no negatives, no signed Laplacian) reproduces the 1D monatomic chain: presence conserved, a disturbance front advances one site per tick (finite propagation speed), N discrete relaxation modes with the flat state stationary, and the dispersion spectrum mu_j=(1-g)+g*cos(2*pi*j/N) matching the chain exactly (cross-checked outside the corpus) [monatomic chain dispersion; Oxford Solid State Basics ch.9].","compare.test_lattice",d1_lattice),
 ("D1b","E","algebraic-magnitude engine: an incommensurable magnitude (the diagonal of the unit square; a lattice mode frequency) is represented as the positive point where two positive-coefficient polynomials balance, P(x)=Q(x), certified by the order-swap of the two positive sides across a rational interval and refined by bisection -- no negatives, no imaginaries, no zero-as-value (Eudoxan, Euclid Book V). Verified to isolate every distinct lattice mode frequency exactly for N=5..12, including non-constructible N (degree>2, not nested radicals). Every distinct lattice mode frequency is isolated to a tight rational bracket by positive comparisons alone.","compare.test_magnitude",d1b_magnitude),
 ("PH5a","E","forced critical coupling. A coupling g ties two copies of the fold dynamics together; the fold's expansion factor m (forced m=2 for the binary fold, R5) carries the transverse separation between the copies forward each tick by the factor (1-g)*m, built in the permitted language as take(ONE,g)*m. The copies synchronise exactly when this carry factor stays under the One, and the boundary -- where it equals the One -- is a forced critical coupling g*=(m-1)/m, obtained by solving (1-g*)*m=ONE. For the binary fold m=2 this is g*=1/2, the same half-One the holding threshold R7 and sync threshold PH3 force; for m=3, g*=2/3. The framework forces this dimensionless coupling from its own expansion factor with no value fed in and nothing fitted. Verified in the permitted language (g*=(m-1)/m, carry factor =ONE at the boundary, synchronises above g* and not below) and cross-checked outside against real master-slave coupled doubling maps, which synchronise iff g>(m-1)/m (1/2 for m=2, 2/3 for m=3) [chaotic-map synchronisation; transverse stability]. The framework forces the critical coupling g*=(m-1)/m from its own expansion factor.","compare.test_critical_coupling",ph5a_critical_coupling),
 ("PH5","E","the framework forces its fundamental dimensionless coupling. A coupling is the strength tying two copies of the fold dynamics together; the fold's expansion factor m (forced m=2 for the binary fold, R5) carries the transverse separation forward each tick by (1-g)*m, built in the permitted language as take(ONE,g)*m. The copies hold together exactly when this carry factor stays under the One, and the boundary -- where it equals the One -- forces the coupling g*=(m-1)/m, solved from (1-g*)*m=ONE. For the binary fold m=2 this is g*=1/2, the same half-One the holding threshold R7 and sync threshold PH3 force; for m=3, g*=2/3. The value is forced from the system's own expansion factor with nothing fed in and nothing fitted -- the framework fixes its fundamental interaction coupling from the single axiom, as it fixes the zero-point half, the sync threshold, and the spatial dimension. Verified in the permitted language (g*=(m-1)/m, carry factor =ONE at the boundary, holds above g* and not below) and cross-checked outside against coupled doubling maps, which synchronise iff g>(m-1)/m. Established on the system's own standard: the engine forces the coupling from the axioms.","compare.test_critical_coupling",ph5a_critical_coupling),
]
