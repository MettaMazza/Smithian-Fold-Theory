"""B4 — modulation, in the permitted language. Two interlocking rational streams folded
together: over their beat period the separation between them rises and falls. Near the
half-One they are opposed (the antipode/opposition state); near unison they are together.
This separation-modulation is the system's own beat pattern — reported as what the system
produces, NOT a claim about physical interference. Separations are exact rationals; the
sequence is exact and periodic with the beat period."""
from fractions import Fraction
from ratio import ONE, fold, separation
import beats as B
QUARTER=Fraction(1,4); HALF=Fraction(1,2)

def separation_sequence(a, b, steps):
    xs=[]; ca,cb=a,b
    for _ in range(steps):
        xs.append(separation(ca,cb)); ca,cb=fold(ca),fold(cb)
    return xs

def profile(a, b):
    """Over one beat period, the separation sequence and how many steps are 'together'
       (separation up to the quarter-One) versus 'opposed' (separation past the quarter,
       toward the half-One antipode)."""
    L=B.combined_period([a,b])
    seq=separation_sequence(a,b,L)
    together=sum(1 for s in seq if s<=QUARTER)
    opposed=sum(1 for s in seq if s>QUARTER)
    return L, seq, together, opposed

def is_periodic_with_beat(a, b):
    """THM check: the separation sequence repeats with the combined (beat) period."""
    L=B.combined_period([a,b])
    one=separation_sequence(a,b,L)
    two=separation_sequence(a,b,L+L)
    return two[:L]==one and two[L:]==one

if __name__=="__main__":
    for a,b in ((Fraction(1,7),Fraction(1,5)),(Fraction(1,9),Fraction(1,5)),(Fraction(1,11),Fraction(1,7))):
        L,seq,tog,opp=profile(a,b)
        print(f"{a} with {b}: beat period {L}")
        print(f"  separation sequence: {[str(s) for s in seq]}")
        print(f"  steps together (<=1/4): {tog}   opposed (>1/4): {opp}")
        print(f"  sequence periodic with the beat period: {is_periodic_with_beat(a,b)}")
        print()
