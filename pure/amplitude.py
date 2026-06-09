"""Amplitude / occupancy layer, in the permitted language. Amplitude is presence: a positive
magnitude (a count of arrivals, or a part of the One) at a position. Superposition combines
presence by positive addition — never by signed cancellation. Interference is expressed as
density contrast: constructive where presence compounds, a gap where presence stays sparse
(relations returning toward the One), not a negative. No negatives, no zero-as-sink: an empty
region is absence of count, the bookkeeping floor, not a magnitude."""
from fractions import Fraction
from ratio import ONE, fold, take, separation

def orbit(p, n):
    pts=[]; c=p
    for _ in range(n): pts.append(c); c=fold(c)
    return pts

def occupancy(points, regions):
    idxs=[ int(p*regions) % regions for p in points ]
    return [ sum(1 for ix in idxs if ix==r) for r in range(regions) ]   # tally per region (no zero seed)

def superpose(occA, occB):
    return [a+b for a,b in zip(occA, occB)]          # positive combination, no cancellation

def total_presence(occ):
    return sum(occ)                                   # total of the region tallies

def closeness(a, b):
    # amplitude of two sources as one positive magnitude: high (-> the One) in phase,
    # low (-> the half-One) in anti-phase. closeness = the One with the separation removed.
    if a==b: return ONE
    return take(ONE, separation(a, b))

def envelope(a, b, n):
    out=[]; ca,cb=a,b
    for _ in range(n):
        out.append(closeness(ca,cb)); ca,cb=fold(ca),fold(cb)
    return out

if __name__=="__main__":
    A=occupancy(orbit(Fraction(1,7),24),12)
    B=occupancy(orbit(Fraction(1,5),24),12)
    S=superpose(A,B)
    print("source A occupancy:", A)
    print("source B occupancy:", B)
    print("superposed:        ", S)
    print(f"total A={total_presence(A)} + total B={total_presence(B)} == total S={total_presence(S)}: {total_presence(A)+total_presence(B)==total_presence(S)}")
    print(f"interference contrast: max {max(S)} (constructive)  min {min(S)} (gap)")
    print("\nbeat envelope (closeness over folds, 1/7 & 1/5):", [str(x) for x in envelope(Fraction(1,7),Fraction(1,5),12)])
