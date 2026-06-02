"""D4 — spacetime / causal structure, in the permitted language. The Lorentzian signature (the
minus sign between time and space) is not a negative here: it is the instruction to combine the
temporal magnitude (c*dt) and the spatial magnitude (dx) by TAKING their difference, not by
ADDING them (an Euclidean sum). The causal class is which positive magnitude predominates:
  time predominates (c*dt > dx)  -> timelike   (events can be causally connected)
  they balance     (c*dt = dx)   -> lightlike  (the light cone, the causal boundary)
  space predominates (dx > c*dt)  -> spacelike  (no signal can connect them)
The invariant interval is then a positive magnitude: the proper time sqrt((c*dt)^2 - dx^2) for
timelike, the proper distance sqrt(dx^2 - (c*dt)^2) for spacelike -- the positive difference of
the two squared magnitudes (the audited take), square-rooted via the algebraic-magnitude engine.
The maximum signal speed c is the forced ratio from D2 (one site per tick). Invariance of the
interval under a change of frame (boost) is the next part, D5."""
from fractions import Fraction
from ratio import ONE, take, ratio
import magnitude as Mg

def causal_class(dt, dx, c):
    ct = c*dt
    if ct > dx: return "timelike"
    if ct == dx: return "lightlike"
    return "spacelike"

def interval_square(dt, dx, c):
    # the positive squared interval: the larger squared magnitude with the smaller taken away.
    ct2 = (c*dt)*(c*dt); dx2 = dx*dx
    if ct2 > dx2: return ("timelike_proper_time2", take(ct2, dx2))
    if ct2 == dx2: return ("lightlike", ONE)        # balance: the two magnitudes coincide
    return ("spacelike_proper_distance2", take(dx2, ct2))

def interval(dt, dx, c, refine=60):
    # the interval as a positive magnitude: sqrt of the positive squared interval, via the engine
    kind, m2 = interval_square(dt, dx, c)
    if kind=="lightlike":
        return ("lightlike", None)                   # the cone: the magnitudes balance (no interval)
    # sqrt(m2): balance point of x^2 = m2, via the magnitude engine's square-root relation.
    # the proper time/distance is a positive magnitude; its bracket runs from the One-floor (the
    # smallest whole, the unit) up to m2+ONE, both strictly positive.
    P,Q=Mg.sqrt_relation(m2)
    lo=ONE; hi=m2+ONE
    if not Mg.certifies(P,Q,lo,hi):                  # m2 below the unit: bracket from a sub-unit floor
        lo=ratio(ONE, m2+ONE)
    mag=Mg.Magnitude(P,Q,lo,hi).tighten(refine)
    return (kind, mag.brackets())

def reachable(dt, dx, c):
    # can a signal connect events separated by (dt, dx)? iff dx <= c*dt (inside/on the cone)
    return dx <= c*dt

if __name__=="__main__":
    c=ONE
    for dt,dx in [(Fraction(2),Fraction(1)),(Fraction(1),Fraction(1)),(Fraction(1),Fraction(2))]:
        cls=causal_class(dt,dx,c); ks=interval_square(dt,dx,c)
        print(f"dt={dt} dx={dx}: {cls}; squared interval {ks[0]} = {ks[1]}; reachable={reachable(dt,dx,c)}")
    # a timelike interval's proper time as an algebraic magnitude
    kind,br=interval(Fraction(2),Fraction(1),ONE)
    print(f"timelike proper-time^2=3 -> proper time isolated in [{float(br[0]):.6f},{float(br[1]):.6f}] (true {3**0.5:.6f})")
