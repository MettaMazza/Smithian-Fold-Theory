"""coupling, identity, and the holding threshold, in the permitted language. Two ones
fold (separation multiplies by the fold factor m) and are pulled toward unison (the gap
is kept to a fraction of itself). Holding = the separation does not grow. The threshold
is derived as a ratio; there is no pi here — pi was an artifact of the angle apparatus."""
from fractions import Fraction
from ratio import ONE, take

def sep_step(s, m, g):
    """One folded step of the separation between two coupled ones: multiply by the fold
       factor m (the repel), then keep the fraction (One minus g) of it (the pull toward
       unison). (One minus g) is formed with the take primitive, never a bare minus."""
    grown = s * m
    kept_fraction = take(ONE, g)        # = One - g, strictly positive for g in (0,1)
    return grown * kept_fraction

def holds(m, g, start=Fraction(1,1000), folds=60):
    s=start
    for _ in range(folds):
        s = sep_step(s, m, g)
    return s <= start                   # separation did not grow => held

def threshold(m):
    """Smallest g (as a ratio) at which holding begins, found by exact bisection on
       rationals. Reported as the ratio the system gives."""
    lo, hi = Fraction(1,10**6), ONE
    # holding begins where m*(One-g) <= One, i.e. g >= (m-1)/m. Confirm by search:
    for _ in range(40):
        mid=(lo+hi)/2
        if holds(m, mid): hi=mid
        else: lo=mid
    return hi

if __name__=="__main__":
    print("holding threshold g* by fold factor m (pure ratio; no pi):")
    for m in (2,3,4,5):
        t=threshold(m)
        predicted=take(ONE, Fraction(1,m))     # (m-1)/m = One - 1/m
        print(f"  m={m}: g* ~ {float(t):.5f}   (m-1)/m = {predicted} = {float(predicted):.5f}")
