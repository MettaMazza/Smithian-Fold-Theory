"""GATE/scale: push each permitted-language identity to the environment ceiling in exact
rational arithmetic (no float, so no precision window). Record the largest scale reached
with zero failures."""
import sys, time
from fractions import Fraction
from ratio import ONE, take, whole_parts, separation, fold
import count as C, measure as Me, monad as Mo, geometry as G, coupling as Cp
fails=[]; budget=6.0

t0=time.time(); k=4000
while time.time()-t0<budget:
    if Me.count(k)*Me.face(k)!=ONE: fails.append(("measure",k)); break
    k+=4000
print(f"  count*measure = One (exact): k reached {k}")

t0=time.time(); kb=2000
while time.time()-t0<budget:
    # a part with kb ones below the point: sum of one-in-2^i for i=1..kb (no subtraction)
    r=None
    for i in range(1, kb+1):
        c=whole_parts(i); r = c if r is None else r + c
    if C.reconstruct(C.unfold(r,kb))!=r: fails.append(("unfold",kb)); break
    kb+=2000
print(f"  unfold & exact reassembly: bit-length reached {kb}")

t0=time.time(); M=4
while time.time()-t0<budget and M<200000:
    M*=2
    g=Mo.gaps(Mo.folded_distinct(M))
    if not all(x==g[0] for x in g): fails.append(("monad",M)); break
print(f"  even division folds to even division: M reached {M}")

t0=time.time(); m=1
while time.time()-t0<budget and m<200000:
    m+=1
    # threshold (m-1)/m = One - 1/m, formed via take; the per-fold factor m*(One - g*) = One
    gstar = take(ONE, Fraction(1,m))
    if gstar*m != take(Fraction(m), ONE):     # m*(m-1)/m must equal m-1
        fails.append(("threshold",m)); break
print(f"  holding threshold (m-1)/m exact: m reached {m}")

import opposition as Op
t0=time.time(); bitsz=2000
while time.time()-t0<budget:
    r=Fraction(2**bitsz+1, 2**bitsz+3)      # a proportion with large numerator/denominator
    if Op.reciprocal(r)*r != ONE: fails.append(("reciprocal",bitsz)); break
    bitsz+=2000
print(f"  reciprocal(r)*r = One (exact): numerator/denominator bit-size reached {bitsz}")

t0=time.time(); dep=2000; half=Fraction(1,2)
while time.time()-t0<budget:
    # a deep dyadic part: sum of one-in-2^i for i=1..dep, then one more fold down (halved)
    pp=None
    for i in range(1, dep+1):
        c=whole_parts(i+1); pp = c if pp is None else pp + c
    if separation(pp, Op.antipode(pp))!=half: fails.append(("antipode",dep)); break
    dep+=2000
print(f"  separation(p, antipode(p)) = half-One (exact): depth reached {dep}")

import opposition as _Op
t0=time.time(); fb=2000
while time.time()-t0<budget:
    pp=Fraction(2**fb+1, 2**(fb+2))
    if fold(pp)!=fold(_Op.antipode(pp)) or _Op.antipode(_Op.antipode(pp))!=pp:
        fails.append(("fold_fiber",fb)); break
    fb+=2000
print(f"  fold(p)=fold(antipode(p)) & antipode involution (exact): depth reached {fb}")

print(f"\nstress_pure: {'CLEAN' if not fails else 'FAIL '+str(fails)}  (zero failures to the ceilings above)")
if fails: sys.exit(1)   # clean run exits cleanly
