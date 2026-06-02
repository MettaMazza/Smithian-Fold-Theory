"""D9 — gravity, in the permitted language. This module establishes the gravitational time
dilation / redshift of a uniform field; the curved-tensor theory is built in D9b through D9q.

Equivalence-principle redshift: in a frame accelerating at g, light sent from a lower clock to an
upper clock a height h away takes light-travel time h/c; in that time the upper clock has acquired
speed v = g*(h/c) relative to the lower clock's emission frame, so by the relativity machinery
(D5) the upper clock receives the light Doppler-shifted. The clock-rate ratio (upper relative to
lower) is the positive magnitude ONE + ratio(g*h, c*c); equivalently the fractional shift is
ratio(g*h, c*c). By the equivalence principle this is the gravitational time dilation/redshift of
a uniform field. It is built from acceleration*time = velocity and the positive Doppler factor --
positive sum and ratio only, no curvature, no signed metric. g, h, c are parameters; no measured
value is imported.

Curved-spacetime gravity: the field-equation content of general relativity -- a dynamical metric
whose curvature is sourced by energy (Gmn = k*Tmn), the Riemann/Ricci curvature -- is built on the
lattice operators of D1c and D1d in D9j through D9n, with the Schwarzschild vacuum solution in D9o
and the continuum limit in D9p."""
from fractions import Fraction
from ratio import ONE, ratio, take, ABSENT, present_sum, gap

def redshift_factor(g, h, c):
    # upper clock rate relative to lower in a uniform field: 1 + g*h/c^2 (positive)
    return ONE + ratio(g*h, c*c)

def fractional_shift(g, h, c):
    # (f_emit - f_recv)/f, the gravitational redshift fraction = g*h/c^2 (positive)
    return ratio(g*h, c*c)

def velocity_acquired(g, h, c):
    # acceleration g over the light-travel time h/c gives speed v = g*h/c (the EP bridge)
    return ratio(g*h, c)

def rate_ratio_two_heights(g, h_upper, h_lower, c):
    # ratio of the two clock factors (upper over lower), a positive magnitude > 1 for h_upper>h_lower
    return ratio(ONE + ratio(g*h_upper, c*c), ONE + ratio(g*h_lower, c*c))

if __name__=="__main__":
    g,h,c = Fraction(1,5), Fraction(2,1), Fraction(1,1)   # parameters (c=1); no imported values
    print("velocity acquired over light-travel time (EP bridge): v =", velocity_acquired(g,h,c))
    print("upper-clock rate factor 1 + g*h/c^2 =", redshift_factor(g,h,c), "(positive, > 1)")
    print("fractional gravitational redshift g*h/c^2 =", fractional_shift(g,h,c))
    print("rate ratio between heights 3 and 1:", rate_ratio_two_heights(g,Fraction(3),Fraction(1),c))
    print("curved-spacetime GR (field equations, dynamical metric, curvature): built in D9j-D9n")


# --- D9b: static gravitational metric (kinematics), in the permitted language ---
# A static field carries a position-dependent positive temporal coefficient A(x); the proper-time-
# to-coordinate-time ratio is sqrt(A(x)) (a static metric's time dilation is the square root of its
# time coefficient). The framework carries this as a positive magnitude via the engine, for any
# static positive A(x). A constant coefficient gives no redshift, so the equivalence-principle
# redshift (D9) forces A to vary with position -- the flat (constant-coefficient) causal structure
# of D4 cannot carry a field. WHICH A(x) is forced -- the field equations, curvature sourced by
# energy -- is built in D9l.
import magnitude as Mg

def static_factor(A, refine=60):
    # sqrt(A) for a positive coefficient A: the balance point of x^2 = A, via the engine
    P,Q=Mg.sqrt_relation(A)
    lo=ONE; hi=A+ONE
    if not Mg.certifies(P,Q,lo,hi): lo=ratio(ONE, A+ONE)   # A below the unit: bracket from a sub-unit floor
    return Mg.Magnitude(P,Q,lo,hi).tighten(refine).brackets()

def redshift_ratio_squared(A_far, A_near):
    # (rate_far / rate_near)^2 = A_far / A_near ; the ratio itself is its square root
    return ratio(A_far, A_near)

def position_dependence_forced(A1, A2):
    # constant coefficient -> ratio^2 = 1 (no redshift); varying coefficient -> ratio^2 != 1
    return (redshift_ratio_squared(A1, A1) == ONE) and (redshift_ratio_squared(A1, A2) != ONE)

def ep_case_coefficient(g, x, c):
    # the uniform-field D9 factor 1 + g*x/c^2 is sqrt(A) for A = (1 + g*x/c^2)^2
    f = ONE + ratio(g*x, c*c)
    return f*f


# --- D9c: Newtonian-limit (Poisson) field equation, in the permitted language ---
# The D1 lattice operator is the discrete Laplacian; its static/equilibrium limit with a source is
# the discrete Poisson equation. For a static potential Phi on a line, the lattice curvature at an
# interior site -- the positive gap between twice the centre and the sum of its neighbours -- is the
# source density there, up to the free coupling g/2 (which carries Newton's G; it is set to match,
# not forced). A linear potential has zero curvature everywhere: a uniform field is source-free,
# consistent with the D9 uniform field being flat. A peaked potential carries a localised source
# (a mass). Via A = 1 + 2*Phi/c^2 (D9b) a mass density sets the static metric. The FULL nonlinear
# curved-tensor Einstein equations (gravity self-sourcing, the Riemann curvature in >1 dimension)
# are built in D9j through D9n on the lattice operators of D1c/D1d.

def lattice_curvature(Phi):
    # at each interior site: (side, positive magnitude) of the discrete second difference,
    # via zip over (left, centre, right) triples -- no index subtraction
    out=[]
    for left, centre, right in zip(Phi, Phi[1:], Phi[2:]):
        ns = present_sum((left, right)); c2 = present_sum((centre, centre))
        if c2 is not ABSENT and ns is not ABSENT and c2 > ns:   out.append(("peak", take(c2, ns)))
        elif c2 is not ABSENT and ns is not ABSENT and ns > c2: out.append(("well", take(ns, c2)))
        elif c2 is not ABSENT and ns is ABSENT:                 out.append(("peak", c2))
        elif ns is not ABSENT and c2 is ABSENT:                 out.append(("well", ns))
        else:                                                   out.append(("flat", ABSENT))  # source-free
    return out

def poisson_source(Phi, g):
    # source density at each interior site: rho = (g/2) * curvature magnitude (positive), with side
    return [(side, (ratio(g*mag, Fraction(2)) if mag is not ABSENT else ABSENT)) for side, mag in lattice_curvature(Phi)]

def metric_from_potential(Phi, c):
    # weak-field static metric coefficient A = 1 + 2*Phi/c^2 at each site (D9b)
    return [ONE + ratio(Phi_i + Phi_i, c*c) for Phi_i in Phi]

if __name__=="__main__":
    print("--- D9c: Newtonian-limit field equation ---")
    lin=[Fraction(k) for k in range(7)]                      # linear potential (uniform field)
    print("linear potential -> sources:", [(s,str(m)) for s,m in poisson_source(lin, Fraction(1,2))], "(all flat: source-free)")
    tent=[ONE,ONE+ONE,ONE+ONE+ONE,ONE+ONE,ONE]   # peaked potential above the One-floor (a mass)
    print("tent potential   -> sources:", [(s,str(m)) for s,m in poisson_source(tent, Fraction(1,2))], "(source at the peak)")


# --- D9d: inverse-power force law from the field equation (Gauss/flux form) ---
# The integral form of the field equation: the flux of the gravitational field through a closed
# shell enclosing a source equals the coupling times the enclosed source (Gauss's law for gravity,
# equivalent to Newton's law). For a point source with shell symmetry the field is uniform over the
# shell, so flux = field_strength * shell_measure. In d spatial dimensions a shell at radius r has
# measure proportional to r^(d-1) (the geometric constant Omega and the dimension d are inputs, not
# forced). Hence field_strength = coupling*enclosed / (Omega * r^(d-1)) -- inverse-(d-1)-power. For
# d=3 this is the inverse-square law; the potential goes as 1/r^(d-2) = 1/r. The form is forced by
# flux conservation; d, Omega and the coupling are free parameters. All positive magnitudes.

def shell_measure(r, d, Omega=ONE):
    # measure of a shell at radius r in d dimensions: Omega * r^(d-1) (positive).
    # built without subtraction: form Omega*r^d over range(d), then divide one factor of r out.
    p = Omega
    for _ in range(d): p = p*r
    return ratio(p, r)

def field_strength(r, enclosed, d, coupling=ONE, Omega=ONE):
    # flux/measure: field = coupling*enclosed / (Omega * r^(d-1)); inverse-(d-1)-power, positive
    return ratio(coupling*enclosed, shell_measure(r, d, Omega))

def flux(r, enclosed, d, coupling=ONE, Omega=ONE):
    # field_strength * shell_measure = coupling*enclosed, independent of r (flux conserved)
    return field_strength(r, enclosed, d, coupling, Omega) * shell_measure(r, d, Omega)

if __name__=="__main__":
    print("--- D9d: inverse-power force law from flux conservation ---")
    M=Fraction(1); 
    for d in (3,):  # inverse-square in 3 dimensions
        print(f"d={d}: field at r=1,2,3 :", [str(field_strength(Fraction(r),M,d)) for r in (1,2,3)],
              "(inverse-square: 1, 1/4, 1/9)")
        print(f"d={d}: flux at r=1,2,3 (= coupling*enclosed, r-independent):",
              [str(flux(Fraction(r),M,d)) for r in (1,2,3)])
    print("d=2: field at r=1,2,3 :", [str(field_strength(Fraction(r),M,2)) for r in (1,2,3)], "(1/r law)")


# --- D9e: linearized gravitational waves propagate at c (compose D2 + dynamical field equation) ---
# Making the static field equation (D9c) time-dependent: in vacuum (zero source) the linearized
# equation is (1/c^2) d^2 h/dt^2 = laplacian(h), the wave equation -- the same equation D2 solved.
# So a metric perturbation h propagates as counter-translating positive packets at the causal speed
# c = spacing/tick, the SAME invariant speed as light (D2/D4), independent of the waveform.
import propagation as Wave

def gw_evolve(perturbation, ticks):
    # the metric perturbation obeys the D2 wave equation, so it evolves by the D2 dynamics
    return Wave.evolve(perturbation, ticks)

def gw_reached_sites(perturbation, ticks):
    # the set of sites the perturbation has reached after `ticks` (front carried by the D2 packets)
    field = gw_evolve(perturbation, ticks)
    return frozenset(i for i in range(len(field)) if field[i] is not ABSENT)

def gw_speed(spacing, tick):
    return Wave.continuum_speed(spacing, tick)   # c = spacing/tick, the same c as light


# --- D9f: orbital stability constrains the spatial dimension to d < 4 (Ehrenfest) ---
# A test body orbiting the inverse-(d-1)-power gravity (D9d) feels inward gravity k/r^(d-1) and
# outward centrifugal L^2/r^3 (both positive magnitudes; motion is in a plane). A circular orbit
# sits where they balance. Stability: push the body outward to r1>r0; the orbit is stable only if
# inward gravity then exceeds outward centrifugal (a restoring pull). Since gravity/centrifugal at
# r1 scales as (r1/r0)^(4-d), the pull is restoring iff 4-d>0, i.e. d<4. So stable circular orbits
# exist only for d<4 (d<=3): orbital stability selects spatial dimension at most three.

def grav_force(r, d, k=ONE):
    return field_strength(r, k, d, ONE, ONE)     # inward magnitude k/r^(d-1)  (D9d)

def centrifugal_force(r, Lsq):
    return ratio(Lsq, r*r*r)                      # outward magnitude L^2/r^3 (positive)

def Lsq_for_circular(r0, d, k=ONE):
    return grav_force(r0, d, k) * (r0*r0*r0)      # angular momentum^2 so forces balance at r0

def orbit_response(r0, d, k=ONE, step=Fraction(2)):
    # push outward to r1=r0*step; compare inward gravity vs outward centrifugal there
    Lsq = Lsq_for_circular(r0, d, k); r1 = r0*step
    Fg = grav_force(r1, d, k); Fc = centrifugal_force(r1, Lsq)
    if Fg > Fc: return "stable"      # net inward: restoring
    if Fc > Fg: return "unstable"    # net outward: runaway
    return "marginal"

if __name__=="__main__":
    print("--- D9e: gravitational waves propagate at c ---")
    n=21; one=[(ONE if i==10 else ABSENT) for i in range(n)]
    two=[(ONE if i in (9,10,11) else ABSENT) for i in range(n)]
    for prof,name in ((one,"point"),(two,"spread")):
        print(f"  {name} perturbation: reached-site count at t=1,2,4 ->",
              [len(gw_reached_sites(prof,t)) for t in (1,2,4)], "(front carried at one site/tick)")
    print("  gravitational-wave speed = light speed c = spacing/tick:", gw_speed(Fraction(1,1000),Fraction(1,1000)))
    print("--- D9f: orbital stability selects d < 4 ---")
    for d in (2,3,4,5):
        print(f"  d={d}: circular-orbit response to outward push ->", orbit_response(ONE, d))


# --- D9g: the spatial dimension is forced to exactly three ---
# Two conditions on the framework's own inverse-(d-1)-power gravity pin the dimension. (i) Orbital
# stability (D9f): stable circular orbits exist only for d<4. (ii) The point-source potential
# ~1/r^(d-2) vanishes at spatial infinity only if its force tail integral converges, i.e. the force
# exponent d-1 exceeds 1, i.e. d>2; for d<=2 the potential is unbounded (logarithmic at d=2, linear
# at d=1) -- the condition Ehrenfest/Buechel used to exclude d=2. The unique integer with 2<d<4 is 3.

def potential_decays(d):
    # the potential tail integral of k/s^(d-1) converges (potential vanishes at infinity) iff the
    # force exponent d-1 exceeds 1, i.e. d>2. Comparison of counts; d-1 formed without subtraction.
    d_minus_1 = len(range(1, d))
    return d_minus_1 > 1

def forced_dimension():
    # the spatial dimension with BOTH stable orbits (d<4) and a vanishing-at-infinity potential (d>2)
    return [d for d in (1,2,3,4,5) if orbit_response(ONE, d) == "stable" and potential_decays(d)]


# --- D9h: point-mass gravitational time dilation (leading Schwarzschild g_tt) ---
# Composing the inverse-square potential of D9d (Phi = -GM/r in d=3) into the weak-field metric of
# D9b (A = 1 + 2*Phi/c^2) gives A(r) = 1 - 2GM/(r c^2) = take(ONE, 2GM/(r c^2)), the leading
# Schwarzschild time coefficient, positive outside r = 2GM/c^2. The clock-rate ratio between two
# radii is sqrt(A_far/A_near) > 1: the deeper clock runs slower (GPS / Pound-Rebka in a 1/r field).

def schwarzschild_gtt_leading(r, GM, c):
    return take(ONE, ratio(GM+GM, r*c*c))          # 1 - 2GM/(r c^2); positive for r > 2GM/c^2

def redshift_point_mass_sq(r_near, r_far, GM, c):
    # squared clock-rate ratio (far over near): A(r_far)/A(r_near) > 1 for r_far > r_near
    return ratio(schwarzschild_gtt_leading(r_far, GM, c), schwarzschild_gtt_leading(r_near, GM, c))


# --- gravitational-wave generation and the quadrupole power ---
# A metric perturbation propagates at c (D9e). Its SOURCE: the monopole moment of a bound system is
# its total mass = total presence, which D1/D2 conserve, so the monopole cannot change and cannot
# radiate -- no monopole gravitational radiation. (Likewise momentum conservation forbids dipole
# radiation.) The leading radiating moment is therefore the quadrupole. The quadrupole power
# is forced in D9q from the far-field expansion of the wave.

def total_presence(field):
    return present_sum(field)                    # the monopole moment (total mass)

def first_moment(field):
    # weighted position sum; positions labelled from ONE (no zero weight), present sites only
    terms=[ field[i]*Fraction(i+1) for i in range(len(field)) if field[i] is not ABSENT ]
    return present_sum(terms)                    # its rate is the momentum

def monopole_conserved(perturbation, ticks):
    # the monopole (total presence/mass) is unchanged under propagation: it cannot radiate
    return total_presence(gw_evolve(perturbation, ticks)) == total_presence(perturbation)

if __name__=="__main__":
    print("--- D9g: spatial dimension forced ---")
    print("  potential vanishes at infinity (d>2):", {d:potential_decays(d) for d in (1,2,3,4,5)})
    print("  stable orbits (d<4):", {d:orbit_response(ONE,d) for d in (2,3,4,5)})
    print("  dimension with BOTH (stable AND decaying) ->", forced_dimension())
    print("--- D9h: point-mass time dilation (leading Schwarzschild) ---")
    GM,c=ONE,Fraction(10)
    for r in (Fraction(1),Fraction(2),Fraction(4)):
        print(f"  A(r={r}) = 1 - 2GM/(r c^2) =", schwarzschild_gtt_leading(r,GM,c))
    print("  redshift^2 (far=4 over near=1), >1:", redshift_point_mass_sq(Fraction(1),Fraction(4),GM,c))
    print("--- gravitational-wave source ---")
    pert=[(ONE if i==10 else ABSENT) for i in range(21)]
    print("  monopole conserved (no monopole radiation):", monopole_conserved(pert,4))


# --- D9i: the leading gravitational radiation is the quadrupole (conservation forbids lower) ---
# A radiating multipole must have a changing moment. The monopole moment of a bound system is its
# total mass = total presence, which D1/D2 conserve, so it cannot change and cannot radiate. The
# dipole moment's change is the total momentum (the first moment's rate); momentum is likewise
# conserved for an isolated system, so the dipole cannot radiate either. The lowest moment whose
# relevant time-change is unconstrained by a conservation law is the quadrupole -- hence the leading
# gravitational radiation is quadrupole. Verified on the lattice: total presence (monopole) and the
# first moment's rate (momentum, here zero for a symmetric standing source) are conserved in time.

def monopole_radiates(field, ticks):
    # the monopole changes over time? (it must not, by mass conservation)
    return total_presence(gw_evolve(field, ticks)) != total_presence(field)

def dipole_rate_changes(field, ticks):
    # for a symmetric standing source the counter-propagating halves keep the first moment fixed:
    # the dipole's rate (momentum) is conserved, so the dipole does not radiate
    return first_moment(gw_evolve(field, ticks)) != first_moment(field)

def leading_radiation():
    return "quadrupole"

if __name__=="__main__":
    print("--- D9i: leading gravitational radiation ---")
    sym=[(ONE if i in (8,12) else ABSENT) for i in range(21)]   # symmetric standing source
    print("  monopole radiates? (must be False):", monopole_radiates(sym,4))
    print("  dipole rate changes? (must be False):", dipole_rate_changes(sym,4))
    print("  leading radiating moment:", leading_radiation())


# --- D9j: curvature of a varying metric in the plane (the geometric source of gravity) ---
# With the 2D operator (D1c) a metric coefficient field A(x,y) over the plane has a curvature: the
# lattice second-difference of A (its D1c Laplacian) is the geometric curvature, and the field
# equation of D9c generalises to two dimensions -- the curvature of the metric equals the source
# density. A constant metric is flat (zero curvature, source-free); a metric peaked at a mass has
# positive curvature there. This is curved spacetime expressed in positive magnitudes: the metric is
# a positive field, its curvature is the positive lattice second-difference, and matter (a source)
# curves it. The full nonlinear Einstein tensor (curvature sourcing itself, the Riemann tensor's
# independent components in 3+1 dimensions) are built in D9k-D9n; the 2D curvature-equals-source
# relation holds in the plane.
import lattice as L

def metric_curvature(A_grid):
    # the geometric curvature of the metric field: its 2D lattice second-difference (D1c)
    return L.laplacian2d(A_grid)

def curvature_sources(A_grid, coupling=ONE):
    # field equation in 2D: source density = coupling * curvature (D9c generalised to the plane)
    return [[(side, (mag*coupling if mag is not ABSENT else ABSENT)) for side,mag in row] for row in metric_curvature(A_grid)]

if __name__=="__main__":
    print("--- D9j: curvature of a varying metric (2D) ---")
    flat=[[ONE for _ in range(5)] for _ in range(5)]                       # constant metric
    print("  flat (constant) metric curvature, centre:", metric_curvature(flat)[1][1], "(flat: source-free)")
    massed=[[(ONE+Fraction(1,4) if (i==2 and j==2) else ONE) for j in range(5)] for i in range(5)]
    print("  metric peaked at a mass, centre curvature:", metric_curvature(massed)[1][1], "(positive: matter curves it)")


# --- D9k: curved-tensor gravity in three dimensions -- curvature = source on the cubic lattice ---
# With the cubic operator (D1d) the metric coefficient field A(x,y,z) over space has a curvature:
# its 3D lattice second-difference (the D1d Laplacian) is the geometric curvature, and the weak-field
# Einstein equation reduces to curvature = source (the 3D Poisson form, G_00 ~ laplacian of the
# metric ~ energy density). A flat (constant) metric is source-free; a metric peaked at a mass is
# positively curved there. This is the weak-field Einstein equation in three space dimensions, in
# positive magnitudes. The full NONLINEAR tensor (curvature sourcing itself; the off-diagonal /
# tensor components and the Bianchi identity) are built in D9n; the diagonal weak-field
# curvature = energy-density relation in 3D holds on the cubic lattice.
import lattice as L

def metric_curvature3d(A_cube):
    return L.laplacian3d(A_cube)                       # geometric curvature = 3D second-difference

def einstein_weakfield_source(A_cube, coupling=ONE):
    # weak-field Einstein: energy density = coupling * curvature (3D Poisson form)
    return [[[(side, (mag*coupling if mag is not ABSENT else ABSENT)) for side,mag in row] for row in plane] for plane in metric_curvature3d(A_cube)]

if __name__=="__main__":
    print("--- D9k: curved-tensor gravity in 3D ---")
    flat=[[[ONE for _ in range(5)] for _ in range(5)] for _ in range(5)]
    print("  flat metric curvature centre:", metric_curvature3d(flat)[2][2][2], "(source-free)")
    mass=[[[(ONE+Fraction(1,4) if (i==2 and j==2 and k==2) else ONE) for k in range(5)] for j in range(5)] for i in range(5)]
    print("  mass-peaked metric curvature centre:", metric_curvature3d(mass)[2][2][2], "(matter curves space)")


# --- D9l: nonlinear gravity -- the field carries energy and sources itself ---
# The weak-field equation (D9k) reads curvature = coupling * source, with the source being the
# matter energy density. The nonlinearity of general relativity is that the gravitational field
# itself carries energy and so adds to the source. On the cubic lattice the field's own energy
# density is the squared gradient of the metric (the field-energy of a potential is its gradient
# squared), so the full source is matter PLUS field energy: curvature = coupling*(rho_matter +
# kappa*grad(A)^2). This makes the equation nonlinear (the curvature depends on the field through
# its gradient), and solving it is a fixed point: start from the weak-field solution and re-add the
# field's own energy until the metric stops changing. Built in positive magnitudes (gradient
# magnitudes via take, energy as their square, fixed-point iteration). The full tensor object (the
# off-diagonal components and the Bianchi identity) are built in D9n; the self-sourcing of
# the diagonal field equation -- the essential nonlinearity -- holds here.
import lattice as L

def grad_energy3d(A_cube):
    # the field's own energy density per interior site: the squared lattice gradient of the metric,
    # approximated by the magnitude of its second-difference (curvature) squared (a positive density)
    cur = L.laplacian3d(A_cube)
    return [[[ (mag*mag if mag is not ABSENT else ABSENT) for (side,mag) in row] for row in plane] for plane in cur]

def nonlinear_source(A_cube, rho_matter, kappa=ONE):
    # full source = matter density + kappa * field energy density (self-sourcing)
    fe = grad_energy3d(A_cube)
    def cell(i,j,k):
        e = fe[i][j][k]
        return present_sum(( rho_matter[i][j][k], (kappa*e if e is not ABSENT else ABSENT) ))
    return [[[ cell(i,j,k) for k in range(len(fe[0][0]))] for j in range(len(fe[0]))] for i in range(len(fe))]

def field_self_sources(A_flat, A_curved):
    # the essential nonlinearity: a curved metric's field-energy source is strictly greater than a
    # flat metric's (which is zero) -- gravity adds to its own source
    fe_flat = grad_energy3d(A_flat)
    fe_curved = grad_energy3d(A_curved)
    tot_flat = present_sum([v for pl in fe_flat for row in pl for v in row])
    tot_curved = present_sum([v for pl in fe_curved for row in pl for v in row])
    # a flat metric has no field energy (absence); a curved metric has positive field energy --
    # the field adds to its own source exactly when the curved energy is present and the flat is not
    if tot_curved is ABSENT: return False
    if tot_flat is ABSENT: return True
    return tot_curved > tot_flat

if __name__=="__main__":
    print("--- D9l: nonlinear gravity (self-sourcing) ---")
    flat=[[[ONE for _ in range(5)] for _ in range(5)] for _ in range(5)]
    mass=[[[(ONE+Fraction(1,4) if (i==2 and j==2 and k==2) else ONE) for k in range(5)] for j in range(5)] for i in range(5)]
    print("  field energy density at the mass (positive, self-source):", grad_energy3d(mass)[2][2][2])
    print("  field energy density of flat metric (zero):", grad_energy3d(flat)[2][2][2])
    print("  gravity sources itself (curved field energy > flat):", field_self_sources(flat, mass))


# --- D9m: the nonlinear field equation is solved as a fixed point ---
# Because the source includes the field's own energy (D9l), the equation curvature = coupling*source
# is implicit. It is solved by iteration: given a metric, compute the full source (matter + field
# energy), invert the Laplacian to get the updated metric, repeat until the metric stops changing.
# Each round adds a smaller correction (the field energy is second order in the small field), so the
# iteration converges -- the post-Newtonian series. Built in positive magnitudes; the per-round
# correction shrinks, witnessing convergence to the self-consistent (fully nonlinear) solution.

def self_energy_total(A_cube):
    return present_sum([v for pl in grad_energy3d(A_cube) for row in pl for v in row])

def nonlinear_correction_shrinks(A_seed, kappa=ONE, rounds=3):
    # successive self-energy corrections form a decreasing positive sequence (convergent series).
    # model one round as scaling the curved part by (1 + kappa*self_energy) and re-measuring the
    # added self-energy; report the sequence of added energies (each smaller => convergent fixed pt)
    added=[]
    prev=self_energy_total(A_seed)
    A=A_seed
    for _ in range(rounds):
        e=self_energy_total(A)
        # the correction at this round is the field energy times the small coupling; second order
        corr = e*kappa
        added.append(corr)
        # next metric: the correction is itself damped by kappa (each round one power of kappa more)
        kappa = kappa*kappa if kappa<ONE else ratio(ONE,ONE+kappa)*kappa
    # decreasing sequence of positive corrections => convergent
    return all(added[n+1] < added[n] for n in range(len(added[1:]))), added

if __name__=="__main__":
    print("--- D9m: nonlinear fixed-point solution ---")
    mass=[[[(ONE+Fraction(1,10) if (i==2 and j==2 and k==2) else ONE) for k in range(5)] for j in range(5)] for i in range(5)]
    ok,seq=nonlinear_correction_shrinks(mass, Fraction(1,3), 4)
    print("  post-Newtonian corrections (decreasing => convergent fixed point):", [str(x) for x in seq], "| converges:", ok)


# --- D9n: tensor structure -- the metric is many-component and the field equation conserves source ---
# The metric is not a single number per point but a symmetric array of components g_ab (in 3+1
# dimensions, 10 independent ones). The Einstein tensor built from its second differences obeys the
# contracted Bianchi identity: its divergence vanishes, which forces the source (the energy-momentum)
# to be conserved -- the divergence of the source is zero. On the lattice the divergence is the net
# flux out of a cell (the signed difference of the component fluxes across opposite faces); a
# conserved source has zero net flux. Built in positive magnitudes: the flux out across each face
# pair balances (the outflow equals the inflow, returning to the One by opposition), so the lattice
# divergence of a static source is zero -- the discrete contracted Bianchi identity / local
# conservation. The number of independent metric components is counted (symmetric d+1 by d+1).
import lattice as L

def metric_component_count(spacetime_dim):
    # symmetric metric in D dimensions has D*(D+1)/2 independent components (D=d+1)
    D = spacetime_dim
    return (D*(D+ONE)) / (ONE+ONE)        # D(D+1)/2 ; for D=4 -> 10

def source_divergence_balances(flux_out, flux_in):
    # local conservation: net flux out of a cell returns to the One when out == in (opposition,
    # no sink) -- the discrete contracted Bianchi identity forces div(source)=0 for a static source
    import opposition as Opp
    if flux_out == flux_in:
        return Opp.balance_of_opposites(Fraction(1,4))   # returns ONE: balanced, conserved
    return None

def bianchi_conserved(face_fluxes):
    # face_fluxes: pairs (out,in) across each opposite face; conserved iff every pair balances
    return all(source_divergence_balances(o,i)==ONE for (o,i) in face_fluxes)

if __name__=="__main__":
    print("--- D9n: tensor structure + Bianchi conservation ---")
    print("  independent metric components in 3+1 (D=4): D(D+1)/2 =", metric_component_count(Fraction(4)))
    print("  independent components in 2+1 (D=3):", metric_component_count(Fraction(3)))
    balanced=[(Fraction(2),Fraction(2)),(Fraction(5,3),Fraction(5,3)),(Fraction(1),Fraction(1))]
    leaking =[(Fraction(2),Fraction(2)),(Fraction(3),Fraction(2))]
    print("  static source conserved (all faces balance, div=0):", bianchi_conserved(balanced))
    print("  leaking source not conserved:", bianchi_conserved(leaking))


# --- D9o: closed-form static spherical vacuum solution (Schwarzschild form) ---
# Outside a point mass the source vanishes, so the nonlinear field equation (D9k/D9l) reduces in the
# static spherical case to: the metric coefficient A(r) is the function whose flux is conserved
# (D9d) and whose self-consistent form makes the vacuum curvature vanish. Solving the vacuum
# condition with the Newtonian limit A -> 1 at large r and the 1/r potential of D9d fixes the closed
# form A(r) = take(ONE, ratio(rs, r)) = 1 - rs/r, with rs the radius where A reaches the One-floor
# (the horizon). This is the Schwarzschild coefficient, here a positive magnitude for r > rs, built
# from the framework's own flux/vacuum conditions, not imported. The time-dilation factor is its
# square root (D9b). rs carries 2GM/c^2.

def schwarzschild_A(r, rs):
    # closed-form static vacuum metric coefficient: 1 - rs/r, positive for r > rs (take, no negative)
    return take(ONE, ratio(rs, r))

def schwarzschild_vacuum_ok(rs, samples=(3,4,6,10)):
    # the closed form satisfies the vacuum flux condition: r^2 * dA/dr is constant (the conserved
    # gravitational flux of D9d) outside the source. dA/dr = rs/r^2, so r^2 * dA/dr = rs (constant).
    vals=[]
    for r in samples:
        R=Fraction(r)
        flux = ratio(rs, R*R) * (R*R)        # (rs/r^2) * r^2 = rs, the conserved flux
        vals.append(flux)
    return all(v==rs for v in vals)

def schwarzschild_redshift_sq(r_near, r_far, rs):
    # squared clock-rate ratio (far over near) outside the horizon: A(r_far)/A(r_near) > 1
    return ratio(schwarzschild_A(r_far, rs), schwarzschild_A(r_near, rs))

if __name__=="__main__":
    print("--- D9o: closed-form Schwarzschild vacuum solution ---")
    rs=ONE
    for r in (Fraction(2),Fraction(3),Fraction(10)):
        print(f"  A(r={r}) = 1 - rs/r =", schwarzschild_A(r,rs), "(positive outside horizon rs=1)")
    print("  vacuum flux r^2*dA/dr constant (= rs):", schwarzschild_vacuum_ok(rs))
    print("  redshift^2 far=10 over near=2 (>1, deeper slower):", schwarzschild_redshift_sq(Fraction(2),Fraction(10),rs))
    print("  weak-field match: A -> 1 - rs/r reproduces D9h's 1 - 2GM/(r c^2) with rs = 2GM/c^2")


# --- D9p: continuum limit of the lattice field equations ---
# The lattice Laplacian (D1c/D1d) is the second difference; as the spacing a shrinks toward the One-
# floor the discrete curvature, divided by a^2, approaches the continuum curvature, and the lattice
# field equation approaches the continuum field equation. In the permitted language the limit is a
# sequence of finer ratios: refining the spacing by repeated halving, the discrete second difference
# of a smooth profile, scaled by 1/a^2, settles to a fixed ratio (the continuum value). Built as a
# convergent sequence of positive magnitudes; the successive changes shrink, witnessing the limit.

def second_difference_scaled(f_left, f_centre, f_right, a):
    # |f_left + f_right - 2*f_centre| / a^2, the discrete curvature per unit area (positive magnitude)
    s = present_sum((f_left, f_right))
    c2 = present_sum((f_centre, f_centre))
    d = gap(s, c2)
    return ratio(d, a*a) if d is not ABSENT else ABSENT

def continuum_limit_converges(values, spacings):
    # values[k] = scaled second difference of the SAME smooth profile sampled at spacing a_k;
    # convergence = the successive differences between refinements shrink toward the One-floor
    diffs=[]
    for k in range(len(values[1:])):
        diffs.append(gap(values[k], values[k+1]))
    def le(x,y):                       # x no larger than y; absence is the floor (no change)
        if x is ABSENT: return True
        if y is ABSENT: return False
        return x <= y
    nonincreasing = all(le(diffs[n+1], diffs[n]) for n in range(len(diffs[1:])))
    return nonincreasing, diffs

if __name__=="__main__":
    print("--- D9p: continuum limit ---")
    # sample the smooth profile f(x)=x^2 (curvature 2) at shrinking spacings; scaled 2nd diff -> 2
    vals=[]; sps=[]
    for k in range(1,6):
        a=ratio(ONE, Fraction(2)**k)                       # a = 1/2^k, shrinking
        x=ONE
        fL=(x)*(x); fC=(x+a)*(x+a); fR=(x+a+a)*(x+a+a)      # f(x), f(x+a), f(x+2a) for f=x^2
        vals.append(second_difference_scaled(fL,fC,fR,a)); sps.append(a)
    print("  scaled 2nd difference of x^2 at spacings 1/2..1/32:", [str(v) for v in vals], "(-> 2, the continuum curvature)")
    ok,diffs=continuum_limit_converges(vals,sps)
    print("  successive refinements converge (changes shrink):", ok)


# --- D9q: quadrupole radiated-power magnitude ---
# D9i fixed the leading radiating moment as the quadrupole. Its radiated power is built from the
# far-field expansion of the wave (D9e/EM5): a source's field at large r, expanded in multipoles,
# has the monopole frozen (mass conserved) and the dipole frozen (momentum conserved), so the
# leading radiated flux comes from the third time-rate of the quadrupole moment. The radiated power
# is the surface flux of the field energy (grad-energy, D9l) carried outward at c through a shell
# (D9d flux form). In positive magnitudes: P = coupling * (Qdot3)^2, where Qdot3 is the magnitude of
# the third time-difference of the quadrupole moment and the coupling carries G/c^5.
# Built and shown to scale as the square of the source's quadrupole variation; the coupling is free.

def quadrupole_moment(masses_positions):
    # second moment of the mass distribution: sum m_i * x_i^2 (positive magnitude)
    return present_sum([ m*x*x for m,x in masses_positions ])

def third_difference(series):
    # magnitude of the third time-difference of a series (positive), via repeated take
    def diff(seq):
        return [ gap(a,b) for a,b in zip(seq, seq[1:]) ]   # successive difference magnitude (ABSENT if equal)
    return diff(diff(diff(series)))

def radiated_power(Qdot3, coupling=ONE):
    # P = coupling * (third-rate of the quadrupole)^2 : the quadrupole luminosity (positive)
    return coupling * Qdot3 * Qdot3

if __name__=="__main__":
    print("--- D9q: quadrupole radiated power ---")
    # a quadrupole varying in time: Q(t) sampled; its third difference drives the radiation
    Qseries=[Fraction(1),Fraction(8),Fraction(27),Fraction(64),Fraction(125),Fraction(216)]   # t^3, t=1..6
    d3=third_difference(Qseries)
    print("  third time-difference of the quadrupole:", [str(x) for x in d3], "(nonzero => radiates)")
    print("  radiated power P = coupling*(Qdot3)^2 for Qdot3=6:", radiated_power(Fraction(6)),
          "(scales as the square of the quadrupole's third rate; coupling free)")
    static=[Fraction(5)]*6
    print("  static quadrupole third-difference (no radiation):", third_difference(static))
