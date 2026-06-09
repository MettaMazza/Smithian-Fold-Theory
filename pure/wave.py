"""Wave / rotation dynamic, in the permitted language. A wave is a phase advancing by a fixed
part of the One each tick: phase <- cast_out(phase + step). This is rotation on the One, built
from addition and casting-out — the same primitives as the fold, a different motion (the fold
doubles; a wave translates). Two waves of steps f1, f2 have a relative phase that advances by
the gap between their steps each tick; that gap is the beat frequency. No negatives, no trig."""
from fractions import Fraction
from ratio import ONE, cast_out, take, separation

def rotate(phase, step):
    return cast_out(phase + step)                 # advance a phase by a fixed part

def relative_phase(p1, p2):
    # p1 seen from p2 on the circle of the One = (p1 minus p2) the positive way, via take
    if p2==ONE: return p1
    return cast_out(p1 + take(ONE, p2))

def beat_frequency(f1, f2):
    # the gap between the two step-rates = how fast the relative phase turns
    if f1==f2: return ONE                          # unison: no beat
    return take(f1, f2) if f1>f2 else take(f2, f1)

def relative_advance(rel):
    # the relative phase advances by one constant step each tick; return that step (positive,
    # around the circle) if constant, else None. The step is the beat frequency up to direction.
    pairs=list(zip(rel, rel[1:]))
    if not pairs: return None
    step0=relative_phase(pairs[0][1], pairs[0][0])
    for x,y in pairs:
        if relative_phase(y,x)!=step0: return None
    return step0

def run(f1, f2, ticks, p1=None, p2=None):
    p1 = f1 if p1 is None else p1
    p2 = f2 if p2 is None else p2
    rel=[]
    for _ in range(ticks):
        p1=rotate(p1,f1); p2=rotate(p2,f2); rel.append(relative_phase(p1,p2))
    return rel

if __name__=="__main__":
    f1,f2=Fraction(1,5),Fraction(1,7)
    bf=beat_frequency(f1,f2)
    rel=run(f1,f2,10)
    print(f"two waves step {f1}, {f2}: beat frequency (step gap) = {bf}")
    print("relative phase over ticks:", [str(r) for r in rel])
    # the relative phase advances by exactly the beat frequency each tick:
    step=relative_advance(rel)
    same_rate = step==bf or step==cast_out(take(ONE,bf))
    print(f"relative phase advances by one constant step {step}; this is the beat frequency (up to direction): {same_rate}")
