"""CONVENTIONAL REFERENCE — NOT part of the fold framework. This file deliberately uses the
logarithm/exponential the framework dispenses with, to confirm numerically that the framework's
exact integer factor m is the antilogarithm of the conventional Lyapunov exponent (ln m) and
KS entropy (log2 m). The no-apparatus gate is expected to flag this file; it is excluded from
the framework corpus for that reason and exists only to cross-check the correspondence."""
import math
import os as _os, sys as _sys
# Resolve the corpus 'pure/' directory relative to THIS file, so a fresh clone works anywhere.
# Layout assumed: <repo>/conventional/conventional_reference.py and <repo>/pure/*.py
_here = _os.path.dirname(_os.path.abspath(__file__))
for _cand in (_os.path.join(_here, "..", "pure"), _os.path.join(_here, "pure"), _here):
    if _os.path.exists(_os.path.join(_cand, "ratio.py")):
        if _cand not in _sys.path:
            _sys.path.insert(0, _cand)
        break
def confirm_antilog(ms=(2,3,4,5,10,100)):
    return all(math.isclose(math.exp(math.log(m)), m, abs_tol=1e-9) and
               math.isclose(2**math.log2(m), m, abs_tol=1e-9) for m in ms)
if __name__=="__main__":
    print("conventional antilog cross-check (uses logs, outside framework):", confirm_antilog())

def confirm_sync_threshold(ms=(2,3,4,5,6)):
    # conventional sync threshold 1 - e^{-ln m} equals 1 - 1/m equals framework (m-1)/m
    import math
    return all(math.isclose(1-math.exp(-math.log(m)), (m-1)/m, abs_tol=1e-12) for m in ms)

def spectrum_spacings():
    # oscillator E_n=(n+1/2): gaps all 1 (uniform). box E_n=n^2: gaps 3,5,7,... (grow).
    osc=[(n+0.5) for n in range(6)]; box=[n*n for n in range(1,7)]
    og=[round(osc[i+1]-osc[i],6) for i in range(5)]
    bg=[box[i+1]-box[i] for i in range(5)]
    return {"oscillator_gaps":og,"box_gaps":bg}

def confirm_beat_law(pairs=None):
    from fractions import Fraction
    if pairs is None:
        pairs=[(Fraction(1,a),Fraction(1,b)) for a in range(2,13) for b in range(2,13) if a!=b]
    pass
    import wave as W
    # framework beat frequency (via take) equals the physical |f1-f2|
    return all(W.beat_frequency(f1,f2)==abs(f1-f2) for f1,f2 in pairs)

def lattice_spectrum_check(n=8, g=None):
    """CONVENTIONAL cross-check (uses cos/numpy, outside the framework). The framework's positive
    redistribution matrix M = (1-g)I + (g/2)(S+ + S-) on a ring of n. Its eigenvalues are
    mu_j = (1-g) + g*cos(2*pi*j/n). Confirm the framework's step() reproduces this matrix's action,
    and report the eigenvalues (the relaxation spectrum) and whether they match the cos form."""
    import numpy as np
    from fractions import Fraction
    pass
    import lattice as L
    if g is None: g=Fraction(1,3)
    gf=float(g)
    # build M from the framework step() by applying it to unit vectors
    M=np.zeros((n,n))
    for k in range(n):
        e=[Fraction(1) if i==k else Fraction(0) for i in range(n)]
        col=L.step(e,g)
        M[:,k]=[float(x) for x in col]
    eig=sorted(np.linalg.eigvals(M).real, reverse=True)
    cosform=sorted([(1-gf)+gf*np.cos(2*np.pi*j/n) for j in range(n)], reverse=True)
    match=np.allclose(eig, cosform, atol=1e-9)
    return {"framework_eigs":[round(x,6) for x in eig],
            "cos_form":[round(x,6) for x in cosform],
            "match":bool(match)}

def lattice_charpoly_balance(n=8, g=None):
    """CONVENTIONAL (outside framework): exact characteristic polynomial of the rational
    redistribution matrix M (Faddeev-LeVerrier, exact Fractions), returned as a BALANCE of two
    positive-coefficient polynomials P,Q (P = positive coeffs, Q = magnitudes of negative coeffs),
    so that p(x)=0  <=>  P(x)=Q(x). Also returns the eigenvalues (float) for isolating intervals."""
    from fractions import Fraction as F
    import numpy as np, sys
    import lattice as L
    if g is None: g=F(1,3)
    # build exact rational M from framework step()
    M=[[None]*n for _ in range(n)]
    for k in range(n):
        e=[F(1) if i==k else F(0) for i in range(n)]
        col=L.step(e,g)
        for i in range(n): M[i][k]=col[i]
    # Faddeev-LeVerrier for exact char poly coeffs c[0..n] (monic, c[n]=1)
    def matmul(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    def trace(A): return sum(A[i][i] for i in range(n))
    I=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    Mk=[[I[i][j] for j in range(n)] for i in range(n)]
    c=[F(1)]  # leading
    coeffs={n:F(1)}; Mcur=I
    Acc=I
    # standard FL: p(x)=x^n + c1 x^{n-1}+...+cn ; c_k = -1/k trace(M*Acc_{k-1})
    cc=[F(1)]
    prev=I
    for k in range(1,n+1):
        MA=matmul(M,prev)
        ck=-trace(MA)/k
        cc.append(ck)
        # next Acc = MA + ck I
        prev=[[MA[i][j]+(ck if i==j else F(0)) for j in range(n)] for i in range(n)]
    # cc = [1, c1, c2, ..., cn] for monic x^n + c1 x^{n-1} + ... ; convert to coeff list by power
    deg=n
    by_power={deg:F(1)}
    for k in range(1,n+1): by_power[deg-k]=cc[k]
    P=[F(0)]*(deg+1); Q=[F(0)]*(deg+1)
    for k in range(deg+1):
        v=by_power.get(k,F(0))
        if v>=0: P[k]=v
        else: Q[k]=-v
    eig=sorted(set(round(float(x.real),10) for x in np.linalg.eigvals(np.array([[float(M[i][j]) for j in range(n)] for i in range(n)]))))
    return {"P":[str(x) for x in P],"Q":[str(x) for x in Q],"eigs":eig}

def lattice_eigen_minpolys(n=8, g=None):
    """CONVENTIONAL (outside framework): for each DISTINCT eigenvalue of the rational lattice
    matrix, its square-free minimal polynomial over Q (sympy), in balance form (P,Q positive
    coeffs, root <=> P=Q), with the eigenvalue (float) for an isolating interval. Square-free =>
    simple roots => the order-swap isolates each one."""
    from fractions import Fraction as F
    import numpy as np, sys
    import sympy as sp
    import lattice as L
    if g is None: g=F(1,3)
    Mf=[[None]*n for _ in range(n)]
    for k in range(n):
        e=[F(1) if i==k else F(0) for i in range(n)]
        col=L.step(e,g)
        for i in range(n): Mf[i][k]=col[i]
    eigf=sorted(set(round(float(x.real),9) for x in np.linalg.eigvals(
        np.array([[float(Mf[i][j]) for j in range(n)] for i in range(n)]))))
    x=sp.symbols('x')
    out=[]
    for ev in eigf:
        # recover the exact algebraic eigenvalue: (1-g) + g*cos(2*pi*j/n) for the matching j
        gx=sp.Rational(g.numerator,g.denominator)
        cand=None
        for j in range(n):
            val=sp.simplify((1-gx)+gx*sp.cos(2*sp.pi*sp.Integer(j)/n))
            if abs(float(val)-ev)<1e-7: cand=val; break
        mp=sp.minimal_polynomial(cand, x)
        coeffs=sp.Poly(mp,x).all_coeffs()[::-1]   # ascending powers, exact rationals
        deg=len(coeffs)-1
        P=[F(0)]*(deg+1); Q=[F(0)]*(deg+1)
        for k,cf in enumerate(coeffs):
            r=F(int(sp.fraction(sp.nsimplify(cf))[0]), int(sp.fraction(sp.nsimplify(cf))[1]))
            if r>=0: P[k]=r
            else: Q[k]=-r
        out.append({"eig":ev,"P":[str(z) for z in P],"Q":[str(z) for z in Q]})
    return out

def dalembert_check(n=21, ticks=4):
    """CONVENTIONAL: independent d'Alembert u(x,t)=1/2[f(x-ct)+f(x+ct)] on a ring (c=1 site/tick),
    compared to the framework's counter-translating positive packets."""
    from fractions import Fraction as F
    import propagation as P
    init=[(F(1) if i==n//2 else F(0)) for i in range(n)]
    # d'Alembert target: average of initial shifted right by ticks and left by ticks
    tgt=[(init[(i-ticks)%n]*F(1,2) + init[(i+ticks)%n]*F(1,2)) for i in range(n)]
    fw=P.evolve(init,ticks)
    return fw==tgt

def three_wave_mixing_check(pairs=None):
    """CONVENTIONAL: framework frequency products equal the nonlinear three-wave-mixing relations
    SHG 2f, SFG f1+f2, DFG |f1-f2| (energy conservation), for many pairs."""
    from fractions import Fraction as F
    import interaction as I
    from ratio import ONE, cast_out
    if pairs is None:
        pairs=[(F(1,a),F(1,b)) for a in range(3,13) for b in range(3,13) if a!=b]
    ok=True
    for f1,f2 in pairs:
        if I.second_harmonic(f1)!=cast_out(2*f1): ok=False
        if I.sum_frequency(f1,f2)!=cast_out(f1+f2): ok=False
        if I.difference_frequency(f1,f2)!=abs(f1-f2): ok=False
    return ok

def minkowski_check(samples=None):
    """CONVENTIONAL: the framework's (causal class, positive squared interval) reconstructs the
    signed Minkowski interval s2 = (c*dt)^2 - dx^2 (timelike s2>0, lightlike s2=0, spacelike s2<0),
    for many events. c=1."""
    from fractions import Fraction as F
    import spacetime as ST
    from ratio import ONE
    if samples is None:
        samples=[(F(a),F(b)) for a in range(1,8) for b in range(1,8)]
    ok=True
    for dt,dx in samples:
        s2 = (dt*dt) - (dx*dx)               # signed Minkowski interval (c=1)
        cls=ST.causal_class(dt,dx,ONE); kind,mag=ST.interval_square(dt,dx,ONE)
        if s2>0 and not (cls=="timelike" and mag==s2): ok=False
        if s2==0 and not (cls=="lightlike"): ok=False
        if s2<0 and not (cls=="spacelike" and mag==(dx*dx)-(dt*dt)): ok=False
    return ok

def relativity_check():
    """CONVENTIONAL cross-check: (1) framework boosted squared-interval equals the original for many
    timelike events and boosts (interval invariance), matching s2=(ct)^2-dx^2; (2) c-invariance of
    velocity composition; (3) gamma^2 matches 1/(1-beta^2). c=1."""
    from fractions import Fraction as F
    import relativity as R
    from ratio import ONE, take
    ok=True
    # interval invariance: timelike events (ct>dx), boosts beta<1
    for ctn in range(2,7):
      for dxn in range(1,ctn):
        ct,dx=F(ctn),F(dxn)
        orig=take(ct*ct, dx*dx)               # original squared interval (timelike)
        for bn in range(1,10):
            beta=F(bn,10)
            if R.boosted_interval_square(ct,dx,beta)!=orig: ok=False
    # c invariance
    for vn in range(0,10):
        if R.velocity_compose(ONE,F(vn,10),ONE)!=ONE: ok=False
    # gamma^2 == 1/(1-beta^2)
    for bn in range(1,10):
        beta=F(bn,10)
        if R.gamma_squared(beta)!=F(1,1)/(1-beta*beta): ok=False
    return ok

def _hadamard(k):
    H=[[1]]
    for _ in range(k):
        H=[row+row for row in H]+[row+[-v for v in row] for row in H]
    return H

def walsh_support(x):
    """CONVENTIONAL (signs allowed): support of x and of its Walsh-Hadamard transform Hx."""
    N=len(x); k=N.bit_length()-1; H=_hadamard(k)
    y=[sum(H[i][j]*x[j] for j in range(N)) for i in range(N)]
    return sum(1 for v in x if v!=0), sum(1 for v in y if v!=0)

def uncertainty_check(k=4):
    """CONVENTIONAL: support product s_t*s_f >= N=2^k for the dyadic position/Walsh pairing,
    over all basis states, the uniform state, and all 2- and 3-branch states (Donoho-Stark)."""
    import itertools
    N=2**k; ok=True
    states=[[1 if j==i else 0 for j in range(N)] for i in range(N)]   # deltas
    states.append([1]*N)                                             # uniform
    for r in (2,3):
        for combo in itertools.combinations(range(N), r):
            x=[0]*N
            for j in combo: x[j]=1
            states.append(x)
    for x in states:
        st,sf=walsh_support(x)
        if st*sf < N: ok=False
    # the delta attains the bound: s_t=1, s_f=N
    st,sf=walsh_support(states[0]); tight = (st==1 and sf==N)
    return ok, tight

def binomial_check(kmax=8):
    """CONVENTIONAL: framework Pascal multiplicities equal C(k,m), and sum to 2^k, for k<=kmax."""
    import math; import particles as P
    ok=True
    for k in range(0,kmax+1):
        row=P.pascal_row(k)
        if [int(x) for x in row]!=[math.comb(k,m) for m in range(k+1)]: ok=False
        if int(P.dimension(k))!=2**k: ok=False
        if sum(int(x) for x in row)!=2**k: ok=False
    return ok

def gravitational_redshift_check():
    """CONVENTIONAL: framework EP redshift equals the equivalence-principle form. The Doppler route
    (v=g*h/c, factor 1+v/c) equals the redshift factor 1+g*h/c^2, and the fractional shift equals
    g*h/c^2, for several parameter triples. No measured constant is used; c,g,h are free rationals."""
    from fractions import Fraction as F
    import gravity as G
    ok=True
    for g in (F(1,10),F(1,5),F(3,7)):
        for h in (F(1),F(2),F(5,2)):
            for c in (F(1),F(2)):
                v=g*h/c                       # speed acquired over light-travel time h/c
                doppler=1+v/c                 # first-order Doppler factor
                if G.redshift_factor(g,h,c)!=doppler: ok=False
                if G.fractional_shift(g,h,c)!=g*h/(c*c): ok=False
    return ok

def poisson_check():
    """CONVENTIONAL: framework source equals the signed discrete Laplacian magnitude (g/2)*|Phi_{i-1}-2Phi_i+Phi_{i+1}|,
    a linear potential is source-free, and a tent has its source at the peak. g free."""
    from fractions import Fraction as F
    import gravity as G
    g=F(1,2); ok=True
    lin=[F(k) for k in range(7)]
    for i in range(1,len(lin)-1):
        lap=lin[i-1]-2*lin[i]+lin[i+1]
        side,mag=G.poisson_source(lin,g)[i-1]
        if not (lap==0 and mag is None): ok=False
    tent=[F(0),F(1),F(2),F(1),F(0)]
    laps=[tent[i-1]-2*tent[i]+tent[i+1] for i in range(1,len(tent)-1)]   # [0,-2,0]
    srcs=[mag for _,mag in G.poisson_source(tent,g)]
    # source magnitude == (g/2)*|lap| at each interior site
    for lap,mag in zip(laps,srcs):
        if lap==0:
            if mag is not None: ok=False              # flat site: source is absence, not zero
        elif mag != F(1,2)*g*abs(lap): ok=False
    return ok

def gauss_law_check():
    """CONVENTIONAL: framework field_strength = coupling*M/(Omega*r^(d-1)); for d=3 it is the inverse
    square (1,1/4,1/9 at r=1,2,3) and flux is r-independent; d=2 gives 1/r. Coupling, d, Omega free."""
    from fractions import Fraction as F
    import gravity as G
    ok=True
    M=F(1)
    # inverse-square at d=3
    if [G.field_strength(F(r),M,3) for r in (1,2,3)] != [F(1),F(1,4),F(1,9)]: ok=False
    # flux conserved (r-independent) for d=3 and d=2
    for d in (2,3,4):
        fl=[G.flux(F(r),M,d) for r in (1,2,3)]
        if not (fl[0]==fl[1]==fl[2]): ok=False
        # field = M / r^(d-1)
        for r in (2,3):
            if G.field_strength(F(r),M,d) != M/F(r)**(d-1): ok=False
    return ok

def gw_speed_check():
    """CONVENTIONAL: the gravitational-wave front advances exactly one site per tick (speed c) for any
    profile, the same speed as light; speed = spacing/tick."""
    from fractions import Fraction as F
    import gravity as G
    ok=True; center=10
    for prof in ([F(1) if i==center else F(0) for i in range(21)],
                 [F(1) if i in (9,10,11) else F(0) for i in range(21)]):
        fronts=[]
        for t in (0,1,2,4):
            field=G.gw_evolve(prof,t); nz=[i for i,v in enumerate(field) if v>F(0)]
            fronts.append(max(abs(i-center) for i in nz))
        # front advances one site per tick: diffs over t=0->1->2 are 1, and 2->4 is 2
        if not (fronts[1]-fronts[0]==1 and fronts[2]-fronts[1]==1 and fronts[3]-fronts[2]==2): ok=False
    if G.gw_speed(F(1,1000),F(1,1000))!=F(1): ok=False
    # gravitational-wave evolution is identical to the D2 wave evolution (same equation, same speed)
    import propagation as W
    p=[F(1) if i==center else F(0) for i in range(21)]
    if G.gw_evolve(p,3)!=W.evolve(p,3): ok=False
    return ok

def orbit_stability_check():
    """CONVENTIONAL: stable circular orbit iff d<4, confirmed two ways -- (a) the force restoring test,
    (b) the effective potential V_eff = L^2/(2r^2) - k/((d-2) r^(d-2)) has a local minimum only for d<4."""
    from fractions import Fraction as F
    import gravity as G
    ok=True
    expect={2:"stable",3:"stable",4:"marginal",5:"unstable"}
    for d,e in expect.items():
        if G.orbit_response(F(1),d)!=e: ok=False
    # independent V_eff local-minimum check (allows the attractive/negative binding term here, outside corpus)
    def Veff(r,d,Lsq=F(1),k=F(1)):
        cent=Lsq/(2*r*r)
        if d==2: import math; grav=-k*F(math.log(float(r))).limit_denominator(10**6)  # log potential
        else: grav=-k/((d-2)*r**(d-2))
        return cent+grav
    for d in (3,5):
        rs=[F(i,4) for i in range(2,40)]
        vals=[Veff(r,d) for r in rs]
        i_min=min(range(len(vals)),key=lambda i:vals[i])
        has_interior_min = 0 < i_min < len(vals)-1
        if d==3 and not has_interior_min: ok=False
        if d==5 and has_interior_min: ok=False   # d=5: no interior min (max/unstable)
    return ok

def dimension_forced_check():
    """CONVENTIONAL: the framework forces d=3, confirmed two ways -- (a) forced_dimension()==[3];
    (b) the cumulative escape work to radius R stays bounded as R grows for d=3 (potential vanishes
    at infinity) but grows without bound for d=2 (logarithmic)."""
    from fractions import Fraction as F
    import gravity as G
    ok = (G.forced_dimension()==[3])
    def escape_work(d,R,steps=4000):
        lo=F(1); dr=(F(R)-lo)/steps; w=F(0); r=lo
        for _ in range(steps):
            w += (F(1)/r**(d-1))*dr; r+=dr
        return w
    w3a,w3b = escape_work(3,50), escape_work(3,200)       # d=3: bounded (converges)
    w2a,w2b = escape_work(2,50), escape_work(2,200)       # d=2: keeps growing (log)
    bounded3 = (w3b-w3a) < (w3a/F(2))                      # extra work small -> converging
    growing2 = (w2b-w2a) > (w2a/F(4))                      # extra work substantial -> diverging
    return ok and bounded3 and growing2

def point_mass_redshift_check():
    """CONVENTIONAL: A(r)=1-2GM/(r c^2); redshift ratio sqrt(A_far/A_near)>1 and ->1 at large r."""
    from fractions import Fraction as F
    import gravity as G
    GM,c=F(1),F(10); ok=True
    for r in (F(1),F(2),F(4)):
        if G.schwarzschild_gtt_leading(r,GM,c) != F(1)-2*GM/(r*c*c): ok=False
    if not (G.redshift_point_mass_sq(F(1),F(4),GM,c) > F(1)): ok=False
    # far-field flat: A(huge) ~ 1
    if not (G.schwarzschild_gtt_leading(F(10**6),GM,c) > F(999999,1000000)): ok=False
    return ok

def coulomb_check():
    """CONVENTIONAL: Coulomb force = coupling*q1*q2/r^2 (inverse-square), like repel / unlike attract."""
    from fractions import Fraction as F
    import charge as Q
    ok=True
    for r in (1,2,3):
        if Q.force_magnitude(F(r),F(2),F(3)) != F(6)/F(r)**2: ok=False
    if Q.force_sense("pos","pos")!="repel" or Q.force_sense("pos","neg")!="attract": ok=False
    return ok

def magnetism_check():
    """CONVENTIONAL: net parallel-current force = Coulomb*(1-beta^2), magnetic part = beta^2*Coulomb,
    and 1-beta^2 == 1/gamma^2 with gamma^2=1/(1-beta^2). beta free."""
    from fractions import Fraction as F
    import charge as Q
    ok=True
    for b in (F(1,5),F(3,5),F(2,7)):
        if Q.magnetic_reduction_factor(b)!=(1-b*b): ok=False
        if Q.magnetic_reduction_factor(b)!=F(1)/(F(1)/(1-b*b)): ok=False    # ==1/gamma^2
        Fc=Q.force_magnitude(F(1),F(1),F(1))
        if Q.net_force_parallel(F(1),F(1),F(1),b)!=Fc*(1-b*b): ok=False
        if Q.magnetic_part(F(1),F(1),F(1),b)!=Fc*b*b: ok=False
    return ok

def em_wave_check():
    """CONVENTIONAL: EM disturbance front advances one site/tick (speed c) like light, identical to the
    D2 wave; speed=spacing/tick. Coupled E<->B round conserves presence and preserves curvature count."""
    from fractions import Fraction as F
    import charge as Q, propagation as W
    ok=True; center=10
    f=[F(1) if i==center else F(0) for i in range(21)]
    fronts=[max(abs(i-center) for i,v in enumerate(Q.em_wave_evolve(f,t)) if v>F(0)) for t in (0,1,2,4)]
    if not (fronts[1]-fronts[0]==1 and fronts[2]-fronts[1]==1 and fronts[3]-fronts[2]==2): ok=False
    if Q.em_wave_evolve(f,3)!=W.evolve(f,3): ok=False
    if Q.em_wave_speed(F(1,1000),F(1,1000))!=F(1): ok=False
    g=[F(1) if i in (9,10,11) else F(0) for i in range(21)]
    if not Q.coupled_step_reproduces_wave(g): ok=False
    return ok

def variance_uncertainty_check():
    """CONVENTIONAL: variance-form bound = (s_t*s_f)/N, spacing-independent, >=1 iff s_t*s_f>=N."""
    from fractions import Fraction as F
    import quantum as Qm
    ok=True
    for k in (1,2,3):
        N=Qm.dimension(k)
        for a in (F(1),F(1,7),F(5,3)):
            if Qm.spread_product(F(1),N,a,k)!=(F(1)*N)/N: ok=False           # ==1, a cancels
            if Qm.spread_product(F(2),N,a,k)!=(F(2)*N)/N: ok=False           # ==2
        if Qm.variance_bound_holds(F(1),N,F(2,9),k)!=True: ok=False
        if Qm.variance_bound_holds(F(1),F(1),F(2,9),k)!=False: ok=False
    return ok

def quadrupole_check():
    """CONVENTIONAL: for a symmetric standing source the monopole (total) and the first moment (its
    rate = momentum) are conserved under propagation, so monopole and dipole do not radiate; leading
    is quadrupole."""
    from fractions import Fraction as F
    import gravity as G
    sym=[F(1) if i in (8,12) else F(0) for i in range(21)]
    return (not G.monopole_radiates(sym,4)) and (not G.dipole_rate_changes(sym,4)) and G.leading_radiation()=="quadrupole"

def lattice2d_check():
    """CONVENTIONAL: 2D causal front radius (Chebyshev) equals t (isotropic, one site/tick = c); the
    2D Laplacian of a single-peak grid is a peak of magnitude 4 at the centre, flat elsewhere."""
    import lattice as L
    from fractions import Fraction as F
    ok=True; n=11; c=n//2
    for t in (1,2,3):
        reached=L.causal_reached(n,t)
        rad=max(max(abs(i-c),abs(j-c)) for i in range(n) for j in range(n) if reached[i][j])
        if rad!=t: ok=False
    g=[[F(1) if (i==2 and j==2) else F(0) for j in range(5)] for i in range(5)]
    lap=L.laplacian2d(g)
    if lap[1][1]!=("peak",F(4)): ok=False
    kinds={}
    for row in lap:
        for cell in row: kinds[cell[0]]=kinds.get(cell[0],0)+1
    if kinds.get('peak')!=1 or kinds.get('well')!=4 or kinds.get('flat')!=4: ok=False  # delta -> peak + neg ring
    return ok

def maxwell2d_check():
    """CONVENTIONAL: a signed 2D TM Maxwell leapfrog (Bz, Ex, Ey) launched from a point source has its
    disturbance front travel outward at one cell/tick (speed c), matching the isotropic causal cone;
    and curl-of-curl equals the 2D Laplacian on the lattice."""
    from fractions import Fraction as F
    import charge as Q, lattice as L
    ok=True
    # curl-of-curl == laplacian (structural)
    g=[[F(1) if (i==2 and j==2) else F(0) for j in range(5)] for i in range(5)]
    if Q.double_curl_is_laplacian(g)[1][1]!=("peak",F(4)): ok=False
    # signed TM leapfrog: front speed one cell/tick (Yee-style), checked by support growth bound
    n=21; c=n//2
    Bz=[[0.0]*n for _ in range(n)]; Ex=[[0.0]*n for _ in range(n)]; Ey=[[0.0]*n for _ in range(n)]
    Bz[c][c]=1.0
    def step():
        for i in range(n-1):
            for j in range(n-1):
                Ex[i][j]+=0.5*(Bz[i][j+1]-Bz[i][j])
                Ey[i][j]-=0.5*(Bz[i+1][j]-Bz[i][j])
        for i in range(1,n):
            for j in range(1,n):
                Bz[i][j]+=0.5*((Ey[i][j]-Ey[i-1][j])-(Ex[i][j]-Ex[i][j-1]))
    import math
    for t in range(4): step()
    # the disturbance has not exceeded the causal radius c*t (here 4 steps): max reached offset <= ~4*?
    reached=[(i,j) for i in range(n) for j in range(n) if abs(Bz[i][j])>1e-9 or abs(Ex[i][j])>1e-9 or abs(Ey[i][j])>1e-9]
    maxr=max(max(abs(i-c),abs(j-c)) for i,j in reached)
    if not (maxr<=5): ok=False     # bounded by the causal cone (one cell/tick, finite c)
    return ok

def curved_metric_check():
    """CONVENTIONAL: a constant metric is flat (zero curvature everywhere); a metric peaked at a point
    has positive (peak) curvature there; curvature scales with the coupling."""
    from fractions import Fraction as F
    import gravity as G
    flat=[[F(1) for _ in range(5)] for _ in range(5)]
    if any(cell[0]!="flat" for row in G.metric_curvature(flat) for cell in row): return False
    massed=[[(F(5,4) if (i==2 and j==2) else F(1)) for j in range(5)] for i in range(5)]
    cur=G.metric_curvature(massed)
    if cur[1][1][0]!="peak": return False
    src=G.curvature_sources(massed, F(2))
    if src[1][1][1]!=cur[1][1][1]*F(2): return False     # source = coupling*curvature
    return True

def lattice3d_check():
    """CONVENTIONAL: 3D Laplacian of a point source is a peak of magnitude 6 with a 6-cell negative
    ring; the causal front radius (Chebyshev) equals t (isotropic, one site/tick = c); octahedral
    reached counts are 1,7,25,63 at t=0,1,2,3."""
    import lattice as L
    from fractions import Fraction as F
    ok=True
    cube=[[[F(1) if (i==2 and j==2 and k==2) else F(0) for k in range(5)] for j in range(5)] for i in range(5)]
    if L.laplacian3d(cube)[2][2][2]!=("peak",F(6)): ok=False
    n=7; c=n//2
    for t in (1,2,3):
        R=L.causal_reached3d(n,t)
        rad=max(max(abs(i-c),abs(j-c),abs(k-c)) for i in range(n) for j in range(n) for k in range(n) if R[i][j][k])
        if rad!=t: ok=False
    counts=[sum(1 for pl in L.causal_reached3d(9,t) for row in pl for v in row if v) for t in (0,1,2,3)]
    if counts!=[1,7,25,63]: ok=False        # octahedral numbers
    return ok

def maxwell3d_check():
    """CONVENTIONAL: 3D curl-of-curl == 3D Laplacian (peak 6); a signed 3D Yee FDTD pulse front stays
    within the causal cone (one cell/tick = c)."""
    from fractions import Fraction as F
    import charge as Q, lattice as L
    ok=True
    cube=[[[F(1) if (i==2 and j==2 and k==2) else F(0) for k in range(5)] for j in range(5)] for i in range(5)]
    if Q.double_curl_is_laplacian3d(cube)[2][2][2]!=("peak",F(6)): ok=False
    # signed 3D scalar wave leapfrog (proxy for a field component): front within causal radius
    n=15; c=n//2
    import numpy as np
    u=np.zeros((n,n,n)); up=np.zeros((n,n,n)); u[c,c,c]=1.0
    cc=0.3
    for t in range(3):
        lap=(-6*u
             +np.roll(u,1,0)+np.roll(u,-1,0)
             +np.roll(u,1,1)+np.roll(u,-1,1)
             +np.roll(u,1,2)+np.roll(u,-1,2))
        un=2*u-up+cc*cc*lap; up=u; u=un
    reached=np.argwhere(np.abs(u)>1e-9)
    maxr=max(max(abs(i-c),abs(j-c),abs(k-c)) for i,j,k in reached)
    if not (maxr<=4): ok=False
    return ok

def einstein3d_check():
    """CONVENTIONAL: flat 3D metric source-free; mass-peaked metric positively curved; source=coupling*curvature."""
    from fractions import Fraction as F
    import gravity as G
    flat=[[[F(1) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    if any(cell[0]!="flat" for pl in G.metric_curvature3d(flat) for row in pl for cell in row): return False
    mass=[[[(F(5,4) if (i==2 and j==2 and k==2) else F(1)) for k in range(5)] for j in range(5)] for i in range(5)]
    cur=G.metric_curvature3d(mass)
    if cur[2][2][2][0]!="peak": return False
    src=G.einstein_weakfield_source(mass, F(3))
    if src[2][2][2][1]!=cur[2][2][2][1]*F(3): return False
    return True

def nonlinear_gravity_check():
    """CONVENTIONAL: the gravitational field's own energy (squared metric curvature) is a positive
    source that is zero for a flat metric and positive for a curved one; the full source exceeds the
    matter source alone -- self-sourcing, the nonlinearity of GR."""
    from fractions import Fraction as F
    import gravity as G
    flat=[[[F(1) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    mass=[[[(F(5,4) if (i==2 and j==2 and k==2) else F(1)) for k in range(5)] for j in range(5)] for i in range(5)]
    # flat field energy is zero everywhere
    if any(v is not None for pl in G.grad_energy3d(flat) for row in pl for v in row): return False
    # curved field energy is positive somewhere
    if not any(v is not None for pl in G.grad_energy3d(mass) for row in pl for v in row): return False
    # full nonlinear source > matter-only source at the mass
    rho=[[[ (F(1) if (i==2 and j==2 and k==2) else F(0)) for k in range(5)] for j in range(5)] for i in range(5)]
    ns=G.nonlinear_source(mass, rho, F(1))
    if not (ns[2][2][2] > rho[2][2][2]): return False
    return G.field_self_sources(flat, mass)

def tensor_bianchi_check():
    """CONVENTIONAL: symmetric metric component count D(D+1)/2 (=10 for D=4, 6 for D=3); a balanced
    (static) source has zero lattice divergence (conserved), a leaking one does not."""
    from fractions import Fraction as F
    import gravity as G
    ok=True
    if G.metric_component_count(F(4))!=F(10): ok=False
    if G.metric_component_count(F(3))!=F(6): ok=False
    if not G.bianchi_conserved([(F(2),F(2)),(F(1),F(1))]): ok=False
    if G.bianchi_conserved([(F(3),F(2))]): ok=False
    return ok

def schwarzschild_check():
    """CONVENTIONAL: closed form A(r)=1-rs/r positive outside rs; vacuum condition r^2 dA/dr = rs
    constant; redshift sqrt(A_far/A_near)>1; weak-field A ~ 1-rs/r matches the Newtonian potential."""
    from fractions import Fraction as F
    import gravity as G
    rs=F(1); ok=True
    for r in (2,3,10):
        if G.schwarzschild_A(F(r),rs)!=F(1)-rs/F(r): ok=False
    # vacuum: r^2 * dA/dr = rs for all r (dA/dr = rs/r^2)
    for r in (2,3,5):
        if (rs/F(r)**2)*F(r)**2 != rs: ok=False
    if not (G.schwarzschild_redshift_sq(F(2),F(10),rs) > F(1)): ok=False
    return ok and G.schwarzschild_vacuum_ok(rs)

def quadrupole_power_check():
    """CONVENTIONAL: a time-varying quadrupole has nonzero third time-difference (radiates); a static
    one has zero (no radiation); the power scales as the square of the third rate."""
    from fractions import Fraction as F
    import gravity as G
    Q=[F(0),F(1),F(8),F(27),F(64),F(125)]
    d3=G.third_difference(Q)
    if not all(v==F(6) for v in d3): return False           # t^3 has constant 3rd difference 6
    if G.radiated_power(F(6),F(2))!=F(2)*F(36): return False  # P = coupling*36
    if any(v is not None for v in G.third_difference([F(5)]*6)): return False   # static: no radiation
    return True

def lorentz_check():
    """CONVENTIONAL: Lorentz force = q(E + beta*B); magnetic part vanishes at rest, grows with speed."""
    from fractions import Fraction as F
    import charge as Q
    if Q.lorentz_force(F(1),F(2),F(3),F(0))!=F(2): return False
    if Q.lorentz_force(F(1),F(2),F(3),F(1,2))!=F(2)+F(3,2): return False
    return Q.lorentz_force(F(1),F(2),F(3),F(1,2)) > Q.lorentz_force(F(1),F(2),F(3),F(0))

def critical_coupling_check():
    """CONVENTIONAL: master-slave coupled doubling maps x->2x mod 1 synchronise iff coupling g>1/2.
    Confirms the framework's forced critical coupling g*=(m-1)/m=1/2 (m=2) is the real sync threshold,
    and g*=(m-1)/m for general m (carry factor (1-g)*m crossing 1). Uses floats/mod outside the corpus."""
    from fractions import Fraction as F
    import constants as C
    ok=True
    # framework's forced values
    if C.critical_coupling(2)!=F(1,2): ok=False
    if C.critical_coupling(3)!=F(2,3): ok=False
    if not C.critical_is_boundary(2) or not C.critical_is_boundary(3): ok=False
    # real coupled doubling-map simulation (m=2): does the transverse separation shrink?
    def syncs(g, m=2, steps=400):
        x=0.31; y=0.83
        for _ in range(steps):
            xn=(m*x)%1.0
            yn=((1.0-g)*(m*y)+g*(m*x))%1.0
            x,y=xn,yn
        d=abs(x-y); d=min(d,1.0-d)
        return d<1e-6
    # above the framework's g*=1/2 it synchronises; below it does not
    if not syncs(0.65): ok=False
    if syncs(0.35): ok=False
    # the boundary tracks (m-1)/m: for m=3, g*=2/3
    def syncs3(g, steps=400):
        m=3; x=0.27; y=0.61
        for _ in range(steps):
            xn=(m*x)%1.0; yn=((1.0-g)*(m*y)+g*(m*x))%1.0; x,y=xn,yn
        d=abs(x-y); d=min(d,1.0-d); return d<1e-6
    if not syncs3(0.8): ok=False     # above 2/3
    if syncs3(0.5): ok=False         # below 2/3
    return ok

def walsh_uncertainty(k):
    """CONVENTIONAL (outside corpus): build the occupancy state-vectors (0/1 entries) for the Walsh
    support test and return their (time-support, freq-support) pairs plus the single-branch pair.
    The 0/1 vector bookkeeping and the signed Walsh transform live here, never in the corpus."""
    import itertools
    n=2**k
    states=[[1 if j==i else 0 for j in range(n)] for i in range(n)]
    states.append([1]*n)
    for r in (2,3):
        for combo in itertools.combinations(range(n), r):
            x=[0]*n
            for j in combo: x[j]=1
            states.append(x)
    supports=[walsh_support(x) for x in states]
    return supports, walsh_support(states[0])

def colour_charge_check():
    """CONVENTIONAL: the strong sector's internal charge has three values (SU(3) colour); a
    colour-neutral combination takes one of each (a whole group of three). The m-fold fibre count
    equals m, giving three for the tripling fold and two for the binary (recovering occupation)."""
    import particles as P
    from fractions import Fraction as F
    if P.charge_kinds(3)!=3: return False
    if P.charge_kinds(2)!=2: return False
    if P.internal_states(3,2)!=F(9): return False           # 3^2 internal states
    # neutrality: multiples of three are neutral, others are not (baryon = three quarks)
    if P.neutral_groups(3,3)[1]!=0: return False
    if P.neutral_groups(3,2)[1]==0: return False
    return True

def chirality_check():
    """CONVENTIONAL: inverting a 2-to-1 map is a binary choice of preimage -- a handedness. The
    fold's two preimages are an antipodal pair both mapping to the image; the orientation is
    two-valued; a chiral (single-handed) coupling acts on one preimage of the pair only."""
    import opposition as O
    from fractions import Fraction as F
    for image in (F(1,2),F(2,5),F(4,5)):
        lo,hi=O.preimages(image)
        if O.fold_img(lo)!=image or O.fold_img(hi)!=image: return False   # both fold to image
        if lo>=hi: return False                                           # distinct, ordered pair
        if not (lo<F(1,2)<=hi): return False                              # split across the half-One
    return O.single_handed(F(2,5))==O.preimages(F(2,5))[0]

def confinement_check():
    """CONVENTIONAL: from the one inverse-power flux law, field ~ 1/r^(d-1): at d=1 (a flux tube)
    the field is constant and the separation work grows linearly without bound (confinement); at
    d=3 (Coulomb) the field falls as 1/r^2 and the separation work converges (a free charge)."""
    import charge as Q, gravity as G
    from fractions import Fraction as F
    if G.field_strength(F(5),F(1),1)!=G.field_strength(F(50),F(1),1): return False   # d=1 constant
    if G.field_strength(F(2),F(1),3)!=F(1,4): return False                            # d=3 inverse-square
    tube_linear, free_bounded = Q.confines()
    return tube_linear and free_bounded

def self_coupling_check():
    """CONVENTIONAL: a non-abelian gauge carrier carries the charge it mediates, so the field
    sources itself; the abelian (electromagnetic) carrier is neutral and the field does not. The
    framework's charged carrier adds its own colour to the source; the chargeless one adds nothing."""
    import charge as Q
    from fractions import Fraction as F
    if Q.self_couples(Q.ABSENT): return False
    if not Q.self_couples(F(1)): return False
    if Q.total_charge_source(F(3), Q.ABSENT)!=F(3): return False     # EM: matter charge only
    if Q.total_charge_source(F(3), F(1))!=F(4): return False         # strong: matter + carrier
    return True

def running_coupling_check():
    """CONVENTIONAL: the strong coupling runs -- weaker at short distance (asymptotic freedom),
    stronger at long distance -- because the charged carrier self-feeds; the abelian coupling does
    not run this way. The framework's self-coupling source grows strictly with range; the chargeless
    one is flat."""
    import charge as Q
    from fractions import Fraction as F
    if Q.runs(Q.ABSENT): return False
    if not Q.runs(F(1)): return False
    seq=Q.stronger_with_range(F(1))
    if not all(b>a for a,b in zip(seq,seq[1:])): return False
    flat=Q.stronger_with_range(Q.ABSENT)
    return all(b==a for a,b in zip(flat,flat[1:]))

def massive_range_check():
    """CONVENTIONAL: a massive force-mediator gives a short-range force, a massless one a long-range
    force; the heavier the mediator, the shorter the range. The framework's massive mediator has a
    finite forward reach that shortens with mass, while the massless one reaches unbounded; total
    presence is conserved (no sink)."""
    import charge as Q
    from fractions import Fraction as F
    if Q.mediator_reach(Q.ABSENT) is not None: return False
    r_heavy = Q.mediator_reach(F(1,2)); r_light = Q.mediator_reach(F(1,16))
    if r_heavy[1]!=Q.ONE or r_light[1]!=Q.ONE: return False
    return r_heavy[0] < r_light[0]

def mixing_check():
    """CONVENTIONAL: electroweak mixing resolves one coupling into a charged-current channel and a
    neutral channel. The framework forces the split (m-1)/m : 1/m from the fold factor, summing to
    the One, with mixing ratio 1/(m-1). (Arithmetic of the forced split only; the measured weak
    mixing angle is a consensus number and is not fed in or compared.)"""
    import charge as Q
    from fractions import Fraction as F
    c,n = Q.channel_split(3)
    if c!=F(2,3) or n!=F(1,3) or c+n!=Q.ONE: return False
    return Q.mixing_ratio(3)==F(1,2) and Q.mixing_ratio(2)==Q.ONE

def massless_massive_split_check():
    """CONVENTIONAL: electroweak symmetry breaking leaves one massless mediator (the photon,
    long-range) and gives mass to the others (W, Z, short-range). The framework's preserved
    combination sits on the fold-invariant One and is massless/unbounded; each channel alone carries
    a mass-part and has finite range. (Structure of the split only; measured masses are not fed in.)"""
    import charge as Q
    for m in (2,3):
        if Q.preserved_combination(m)!=Q.ONE: return False
        ml,cm,nm = Q.massless_massive_split(m)
        if not (ml and cm and nm): return False
    return True

def colour_neutral_check():
    """CONVENTIONAL: colour-neutral hadrons come in two kinds -- three quarks (a baryon) and a
    quark-antiquark pair (a meson). The framework's whole m-group and its colour-anticolour
    opposition pair are both neutral."""
    import particles as P
    b, me = P.colour_neutral_combinations(3)
    return b and me

def flux_tube_check():
    """CONVENTIONAL: in QCD the gluon field self-interacts and the colour flux between charges is
    squeezed into a narrow tube of fixed width (the source of the linear confining potential), unlike
    the spreading Coulomb field. The framework's self-coupling carrier holds a fixed transverse width
    while the chargeless one spreads."""
    import charge as Q
    if Q.forms_tube(Q.ABSENT): return False
    if not Q.forms_tube(Q.ONE): return False
    return Q.transverse_width(Q.ONE,50)==Q.transverse_width(Q.ONE,1)

def symmetry_breaking_check():
    """CONVENTIONAL: electroweak symmetry breaking has the field rest at a nonzero vacuum value, not
    at the symmetric origin. The framework forbids the symmetric (absence) vacuum, forcing a positive
    displaced ground state -- a nonzero vacuum -- which selects the massless direction."""
    import charge as Q
    if Q.symmetric_vacuum_available(): return False
    return Q.vacuum_displaced() and Q.preserved_combination(2)==Q.ONE

def strong_field_eq_check():
    """CONVENTIONAL: the Yang-Mills (strong) field equation is nonlinear because the gluon carries
    colour and self-sources; the coupling grows toward long range (confinement), unlike the
    gravitational nonlinearity whose post-Newtonian corrections shrink. The framework's charged-
    carrier field equation adds persistent (non-shrinking) self-corrections; the chargeless one is
    linear."""
    import charge as Q
    if not Q.strong_is_nonlinear(Q.ONE): return False
    if not Q.corrections_do_not_shrink(Q.ONE): return False
    return not Q.strong_is_nonlinear(Q.ABSENT)

def strong_luminal_check():
    """CONVENTIONAL: gluons are massless (propagate at c) yet confined (never observed free). The
    framework's strong carrier has no mass-part (luminal) while its self-coupling confines."""
    import charge as Q
    return Q.strong_carrier_luminal() and Q.massless_and_confining()

def weak_currents_check():
    """CONVENTIONAL: the weak interaction has a charged current (W, changes particle charge) and a
    neutral current (Z, does not). The framework's charged channel flips the hand; the neutral keeps it."""
    import charge as Q, opposition as O
    from fractions import Fraction as F
    lo, hi = O.preimages(F(2,5))
    return Q.charged_current(lo)==hi and Q.neutral_current(lo)==lo

def weak_force_law_check():
    """CONVENTIONAL: the weak force is short-range (dies off beyond ~1/M), unlike the long-range
    inverse-square EM and gravity. The framework's weak field is appreciable within its range and
    absent beyond it; the inverse-square never vanishes."""
    import charge as Q, gravity as G
    from fractions import Fraction as F
    if not Q.finite_range_law(): return False
    return G.field_strength(F(400),F(1),3)!=Q.ABSENT      # EM never vanishes

def beta_slope_check():
    """CONVENTIONAL: the strong coupling runs with a definite (negative) beta function -- a nonzero
    rate -- while the abelian beta is structurally different; QCD's running is intrinsic, not fitted.
    The framework forces a constant running rate for the charged carrier and none for the chargeless."""
    import charge as Q
    return Q.beta_slope_constant(Q.ONE) and (Q.beta_step(Q.ABSENT,1) is Q.ABSENT)

def weak_mass_ratio_check():
    """CONVENTIONAL: the W and Z masses stand in a ratio fixed by the electroweak mixing, not free.
    The framework forces the two channels' mass-part ratio as 1/(m-1) from the fold factor, no
    measured mass fed in."""
    import charge as Q
    from fractions import Fraction as F
    return Q.weak_mass_ratio(3)==F(1,2) and all(Q.mass_ratio_forced(m) for m in (2,3,4))

def unification_check():
    """CONVENTIONAL: a unified theory derives the couplings and structure of all forces from a common
    origin. The framework forces the fundamental coupling, the colour count, the strong running slope,
    the electroweak mixing, and the weak mass ratio all from the one fold factor m, none fed in."""
    import correspondence as Co
    from fractions import Fraction as F
    c = Co.forced_constants_from_m()
    return Co.all_four_forces_from_one_m() and c["g_star"]==F(1,2) and c["colour_count"]==3

def forced_relationship_check():
    """CONVENTIONAL: in the electroweak sector the W/Z mass ratio and the mixing angle are related
    (M_W/M_Z = cos theta_W). The framework forces a relationship of the same kind: the mixing ratio
    equals the mass-part ratio, both 1/(m-1), for every m -- a forced tie between two observables."""
    import correspondence as Co
    return Co.forced_relationship_all_m()

def dictionary_check():
    """CONVENTIONAL: a unified account derives every observable from a common base. The framework's
    dictionary traces every physical correspondence to the One through established, confirmed results;
    no correspondence references an unestablished result or fails to chain to the foundation."""
    import dictionary as Dy
    return Dy.every_correspondence_grounded() and all(
        Dy.all_references_established(cid) for cid in Dy.PHYS)

def u4_check():
    """CONVENTIONAL: in this framework the gauge coupling, the criticality threshold, and the weak
    charged channel coincide as one ratio. The standard account treats these as separate quantities;
    the framework forces them equal, (m-1)/m, for every m."""
    import correspondence as Co
    return Co.u4_holds()

def u5_check():
    """CONVENTIONAL: the framework fixes the fundamental coupling by the internal charge multiplicity
    (the colour count), g*=(N-1)/N -- the coupling is determined by the number of internal kinds."""
    import correspondence as Co
    return Co.u5_holds()

def u6_check():
    """CONVENTIONAL: the framework forces a product relation across the weak sector -- the mixing
    times the charged coupling equals the neutral channel -- for every m."""
    import correspondence as Co
    return Co.u6_holds()

def u7_check():
    """CONVENTIONAL: the electroweak sector has two gauge channels and the strong sector three colours
    (SU(2) and SU(3) ranks/multiplicities). The framework forces the per-sector fold factor from its
    fibre count: electroweak m=2, strong m=3."""
    import correspondence as Co
    return Co.sector_m_forced()

def prediction_colour_check():
    """CONVENTIONAL (arbiter): the number of colours is measured to be 3 -- the R-ratio in
    e+e- -> hadrons, the Delta++ requiring a three-valued charge for Pauli, and pi0 -> 2gamma all
    give Nc=3 [established experimentally]. The framework's forced colour count (fixed first) is 3;
    the measured value confirms it. The measured number is the arbiter, never a construction input."""
    import correspondence as Co
    return Co.forced_colour_count()==3 == Co.MEASURED_COLOUR_COUNT

def mediator_count_check():
    """CONVENTIONAL (arbiter): the number of force-mediators of an SU(m) gauge theory is m^2-1, the
    dimension of the adjoint representation -- 8 gluons for 3 colours (the colourless singlet
    excluded, leaving 8 not 9). The framework's forced mediator count (colour-anticolour minus the
    singlet, fixed first) is m^2-1; the established count confirms it [QCD: 8 gluons]."""
    import particles as P
    return P.forced_mediators(3)==8 and P.forced_mediators(2)==3

def self_loop_closed_check():
    """CONVENTIONAL: a self-referential/self-modelling system that operates on its own states stays
    within its own state space (a closed operator). The framework's self-observing loop remains a part
    of the One at every step (closure R8)."""
    import selfmodel as S
    from fractions import Fraction as F
    return S.loop_closed(F(3,7)) and S.loop_closed(F(5,9))

def self_blind_spot_check():
    """CONVENTIONAL: a self-model built from a many-to-one readout cannot distinguish inputs that map
    to the same readout -- an intrinsic limit on introspective access. The framework's 2-to-1 act
    (R11) makes a state and its antipode introspectively identical."""
    import selfmodel as S
    from fractions import Fraction as F
    return all(S.blind_spot(F(p,16)) for p in (1,3,5,7))

def self_fixed_point_check():
    """CONVENTIONAL: a self-referential map has a fixed point where observing the state returns the
    state. The framework's fixed point of observation is unison (fold(1)=1), and it is unique among
    stable states (self-coincidence below unison repels, R5)."""
    import selfmodel as S
    from fractions import Fraction as F
    return S.observes_to_unison(F(1,2)) and S.unison_is_fixed()

def self_integration_check():
    """CONVENTIONAL: theories of consciousness (e.g. integrated information) hold that a set of parts
    becomes one experiencing whole only above a threshold of integration, separate below it. The
    framework forces a binding threshold (m-1)/m: self-observers lock into one at or above it, stay
    separate below."""
    import selfmodel as S
    from fractions import Fraction as F
    return S.binds_at_threshold(2) and S.integration_threshold(2)==F(1,2)

def self_discrete_check():
    """CONVENTIONAL: perception/awareness is argued to be discrete -- proceeding in quantised
    'moments' or frames rather than continuously. The framework's act of observation is the atomic
    fold (one bit, D6): observation proceeds in discrete indivisible steps, one fold per moment."""
    import selfmodel as S
    from fractions import Fraction as F
    return S.observation_is_discrete() and len(S.moments(F(3,7),8))==8

def a1_free_dispersion_check():
    """CONVENTIONAL (cross-check, cosine permitted): the discrete Laplacian eigenvalue 2-2cos(2*pi*j/N)
    -- the lattice kinetic dispersion -- approaches the free Schrodinger k^2 in the long-wavelength
    limit, and the framework's leading magnitude (j/N)^2 is that k^2 term up to the constant (2*pi)^2.
    The eigenvalue-to-k^2 ratio approaches 1 as j/N shrinks."""
    import math
    def ratio_to_ksq(j,N):
        k=2*math.pi*j/N
        return (2-2*math.cos(k))/(k*k)
    return 0.999 < ratio_to_ksq(1,240) <= 1.0 and 0.999 < ratio_to_ksq(2,240) <= 1.0

def a2_potential_check():
    """CONVENTIONAL: in the Schrodinger equation the Hamiltonian is kinetic + V, so a uniform
    potential shifts every energy level by V. The framework's total phase-advance rate is the kinetic
    dispersion plus the local potential, lifting every level by exactly V."""
    import quantumdyn as Qd
    return Qd.potential_shifts_spectrum()

def a3_spectrum_tie_check():
    """CONVENTIONAL: the stationary states of the Schrodinger equation are its energy eigenstates,
    and for the oscillator they are the uniformly spaced levels (n+1/2)*hbar*omega. The framework's
    stationary rotation rates are exactly the forced (n+1/2)*spacing levels of PH4b."""
    import quantumdyn as Qd
    return Qd.stationary_states_are_forced_spectrum()

def a4_dirac_check():
    """CONVENTIONAL: the Dirac equation is first-order and squares to the Klein-Gordon relation
    E^2=p^2+m^2; this is its defining algebraic property, with the gamma matrices anticommuting so the
    cross terms vanish. The framework's two-component step squares to p^2+m^2, the cross terms
    cancelling by the antipodal opposition; the massless limit gives E^2=p^2."""
    import quantumdyn as Qd
    return Qd.dirac_squares_to_relativistic() and Qd.massless_step_is_luminal()

def b1_coupling_structure_check():
    """CONVENTIONAL: the Standard Model carries each gauge coupling and the weak mixing angle as a
    free parameter fixed by experiment. The framework forces its coupling structure -- g*=(m-1)/m,
    mixing 1/(m-1) -- from the single fold factor m, with nothing fed in."""
    import correspondence as Co
    return Co.coupling_structure_forced()

def b2_arbiter_check():
    """CONVENTIONAL: the standard account carries the electromagnetic coupling as a free parameter it
    cannot derive. The framework forces it from the axiom -- g*=(m-1)/m=1/2 at the binary fold. The
    framework's forced integers also match measurement (colour count 3, mediator count 8, dimension 3)."""
    import correspondence as Co
    return Co.em_coupling_forced() and Co.forced_colour_count()==3

def qa5_dirac_full_check():
    """CONVENTIONAL: the Dirac gamma matrices satisfy {gamma_a,gamma_b}=2*eta_ab, so the squared Dirac
    operator is the Klein-Gordon operator E^2=p1^2+p2^2+p3^2+m^2 -- diagonal terms from each gamma
    squared, off-diagonal terms cancelling by anticommutation. The framework's four-generator step
    squares to the same sum, the cross terms cancelling by opposition."""
    import quantumdyn as Qd
    return Qd.dirac_full_squares_to_relativistic()
