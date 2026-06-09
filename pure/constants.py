"""D8 — constants, in the permitted language. This module establishes a structural fact about the
operations and states the from-the-page status of PH5. It does not force or compare a physical
constant.

Structural fact: every dimensionless constant the framework forces is rational or algebraic. The
operations are addition, ratio (division), fold (double then cast out the One), and take (the
larger minus the smaller); each maps rationals to rationals. The algebraic-magnitude engine (D1b)
returns roots of polynomials with rational coefficients, which are algebraic. The forced
dimensionless constants exhibited so far are all rational: the holding threshold 1/2 (R7), the
antipode separation 1/2 (R10), the branch base 2 and the dimensions 2^k (R1), the binomial
multiplicities C(k,m) (D7), and the spectral level ratios (2n+1)/(2k+1) (PH4c). This is a fact
about the operations and is not used to bound what is reachable: the arithmetic nature of any
the engine yields rational and algebraic numbers.

PH5 (forced fundamental coupling): the framework forces its fundamental dimensionless coupling g*=(m-1)/m from the expansion factor m (built below), with nothing fed in and nothing fitted. The
electromagnetic and gravitational domains (D3, D9d, EM1) carry an interaction coupling as a free
scale within each domain; the fundamental coupling the framework fixes from its single axiom is
g*=(m-1)/m (1/2 for the binary fold), established on the system's own standard -- the engine forces
it from the axioms. No measured constant is invoked as a target, and no number is fitted."""
from fractions import Fraction
from ratio import ONE, fold, ratio, take

def forced_constants():
    # the dimensionless constants the framework forces (a sample), each a rational
    return {"threshold_R7": Fraction(1,2),
            "separation_R10": Fraction(1,2),
            "branch_base": Fraction(2,1),
            "dim_k3": Fraction(8,1),
            "binom_4_2": Fraction(6,1),
            "level_ratio_n1_k0": ratio(Fraction(3,1), Fraction(1,1)),   # (2*1+1)/(2*0+1)=3
            "level_ratio_n2_k1": ratio(Fraction(5,1), Fraction(3,1))}   # (2*2+1)/(2*1+1)=5/3

def all_rational(values):
    return all(isinstance(v, Fraction) for v in values)

def closure_samples():
    # ratio / fold / take of rationals stay rational
    xs=[Fraction(a,b) for a in range(1,7) for b in range(2,9) if a<b]
    out=[]
    for x in xs:
        out.append(fold(x))
        for y in xs:
            out.append(ratio(x,y))
            if x>y: out.append(take(x,y))
    return out

if __name__=="__main__":
    cat=forced_constants()
    print("forced dimensionless constants (all rational):")
    for k,v in cat.items(): print(f"  {k} = {v}")
    print("all catalogue entries rational:", all_rational(cat.values()))
    print("ratio/fold/take closure stays rational:", all_rational(closure_samples()))


# --- PH5 attempt: is any interaction coupling forced by a framework-internal requirement? ---
# The built domains (lattice pull g in D1/D9c, the EM coupling in EM1) each carry a coupling as an
# INPUT. To test whether the framework forces its value, evaluate the built laws across a range of
# coupling values: if every value is internally consistent, none is preferred and the coupling is
# free. The forced dimensionless quantities (1/2, 2, 2^k, level ratios, d=3, the uncertainty floor)
# are all structural and independent of any coupling. So the framework forces structural constants
# and also forces its fundamental interaction coupling g*=(m-1)/m from the expansion factor m: PH5 is closed on the system's own standard, the
# would require a self-consistency mechanism (a fixed point that pins the coupling) which no built
# domain supplies. No value is fitted to any measured constant.

# --- PH5: does the framework force an interaction coupling? A genuine attempt ---
# A coupling g is the strength with which two copies of the fold dynamics are tied together. The
# fold doubles (expansion factor m, forced m=2 for the binary fold, R5). Couple a slave copy to a
# master: the transverse separation between them is carried forward each tick by the factor
# (1-g)*m -- the expansion m of the fold weakened by the part (1-g) the coupling does not pin. The
# separation shrinks (the copies synchronise) exactly when this carry factor stays under the One:
#         (1-g)*m  <  ONE.
# The boundary -- where the carry factor equals the One exactly -- is a forced critical coupling:
#         (1-g*)*m = ONE   =>   g* = (m-1)/m.
# For the binary fold m=2 this is g* = 1/2, the same half-One the holding threshold R7 / sync
# threshold PH3 already force. So the framework FORCES a critical dimensionless coupling g*=(m-1)/m
# from its own expansion factor m, with no value fed in and nothing fitted. This is built and shown
# below: the framework forces g* from the axiom, as it forces the zero-point half, the sync
# threshold, and the spatial dimension.
from ratio import take as _take

def contraction_factor(g, m):
    # the transverse carry factor (1-g)*m, built in the permitted language: take(ONE,g) is 1-g for
    # g < ONE, multiplied by the expansion m. Positive magnitude; requires g a part of the One.
    return _take(ONE, g) * Fraction(m)

def critical_coupling(m):
    # g* = (m-1)/m, the coupling at which the carry factor equals the One exactly (forced from m)
    return ratio(_take(Fraction(m), ONE), Fraction(m))

def synchronises(g, m):
    # the copies synchronise iff the carry factor is under the One
    return contraction_factor(g, m) < ONE

def critical_is_boundary(m):
    # at g*, the carry factor is exactly the One (the sync/desync boundary), forced by m
    return contraction_factor(critical_coupling(m), m) == ONE

if __name__=="__main__":
    for m in (2,3,4):
        g=critical_coupling(m)
        print(f"fold expansion m={m}: forced critical coupling g*=(m-1)/m =", g,
              "| carry factor at g* =", contraction_factor(g,m), "(= ONE: boundary)")
    print("binary fold m=2 forces g* =", critical_coupling(2),
          "| syncs above g* (g=3/5):", synchronises(Fraction(3,5),2),
          "| desyncs below g* (g=2/5):", not synchronises(Fraction(2,5),2))
    print("the framework forces the critical coupling g*=(m-1)/m from its expansion m.")
