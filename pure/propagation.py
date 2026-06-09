"""D2 — propagation law, in the permitted language. The 1D wave equation's general solution
(d'Alembert) is two waves moving in opposite directions at speed c. Built here in positive
presence: a disturbance splits into a right-moving and a left-moving positive packet (each half
the presence), each translating at the causal lattice speed (one site per tick), superposed by
positive addition. No signed second-order operator, no negative displacement, no zero: a site that
carries no presence is absent (ABSENT), not the value zero. The maximum signal speed is one site
per tick, forced by nearest-neighbour translation; in the continuum limit the invariant propagation
speed is the ratio c = (spacing)/(tick)."""
from fractions import Fraction
from ratio import ONE, ABSENT, present_sum

def translate_right(profile):
    n=len(profile); idx=list(range(n)); back=len(profile[1:])   # = n-1, no subtraction
    return [profile[(i+back)%n] for i in idx]                   # shift profile right by one

def translate_left(profile):
    n=len(profile); idx=list(range(n))
    return [profile[(i+1)%n] for i in idx]                      # shift profile left by one

def half(profile):
    # split present presence in two; an absent site stays absent (no presence to split)
    return [ (c*Fraction(1,2) if c is not ABSENT else ABSENT) for c in profile]

def evolve(initial, ticks):
    """d'Alembert in positive presence: right-mover + left-mover, each half, translated `ticks`.
       Superposition adds the present packets; a site reached by neither stays absent."""
    r=half(initial); l=half(initial)
    for _ in range(ticks):
        r=translate_right(r); l=translate_left(l)
    return [ present_sum((a,b)) for a,b in zip(r,l) ]           # positive superposition

def total(profile):
    return present_sum(profile)

def front_distance(initial, ticks):
    """half-width of the reached region after `ticks`: the right-mover and left-mover each carry
       the front one site per tick, so the reached support spans 2*ticks+1 sites about the source.
       Measured by support size (count of present sites), no signed index arithmetic."""
    field=evolve(initial,ticks)
    reached=sum(1 for c in field if c is not ABSENT)
    # support size grows as 2*ticks+1 until the two fronts meet; half-width = ticks
    return reached

def continuum_speed(spacing, tick):
    return spacing / tick                                      # c = a/tau, the invariant ratio

if __name__=="__main__":
    n=21
    init=[ (ONE if i==10 else ABSENT) for i in range(n)]
    for t in (1,2,3,5):
        print(f"t={t}: reached-support size = {front_distance(init,t)}  (= 2t+1 => {2*t+1})  total={total(evolve(init,t))}")
    print("continuum invariant speed c = spacing/tick (ratio):", continuum_speed(Fraction(1,1000),Fraction(1,1000)))
