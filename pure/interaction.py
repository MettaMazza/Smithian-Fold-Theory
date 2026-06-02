"""D3 — interaction / mode coupling, in the permitted language. A linear wave keeps each mode
separate; interaction (nonlinearity) couples modes and generates new frequencies. The framework's
native nonlinearity is the fold (the doubling map): folding a wave's phase doubles its frequency
(second harmonic). Combining two waves' phases gives the sum frequency (cast out the One of the
phase sum) and the difference frequency (the take). These are exactly the products of second-order
three-wave mixing: 2f (SHG), f1+f2 (SFG), |f1-f2| (DFG). All by the framework's own operations;
no signed nonlinear susceptibility tensor is introduced. The frequencies are forced; the coupling
strength (efficiency) is a separate parameter, not a forced constant."""
from fractions import Fraction
from ratio import ONE, cast_out, take

def second_harmonic(f):
    # the fold doubles the phase, so a wave at f becomes a wave at 2f
    return cast_out(f + f)            # frequency doubling (SHG), positive

def sum_frequency(f1, f2):
    return cast_out(f1 + f2)          # f1 + f2 on the One (SFG)

def difference_frequency(f1, f2):
    if f1==f2: return ONE             # identical inputs: no difference tone
    return take(f1, f2) if f1>f2 else take(f2, f1)   # |f1 - f2| (DFG, = the beat)

def harmonic_cascade(f, k):
    # repeated folding: f, 2f, 4f, ..., 2^k f -- the octave ladder, forced powers of two
    out=[f]; cur=f
    for _ in range(k):
        cur=cast_out(cur+cur); out.append(cur)
    return out

if __name__=="__main__":
    f1,f2=Fraction(1,5),Fraction(1,7)
    print(f"second harmonic of {f1}: {second_harmonic(f1)}")
    print(f"sum frequency {f1}+{f2}: {sum_frequency(f1,f2)}")
    print(f"difference frequency of {f1},{f2}: {difference_frequency(f1,f2)}")
    print(f"harmonic cascade of 1/16 (octaves): {[str(x) for x in harmonic_cascade(Fraction(1,16),3)]}")
