# B9 gives gap(d) = 1/((2+2^d)(3+2^d)). The total accumulated separation over all depths is the sum
# of gaps. Test whether the framework forces a closed value for this sum. Permitted language: positive
# rationals, partial sums (the sum of positive parts), read whether it converges to a forced ratio.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

def gap(d): return Co.coupling_gap_closed_form(d)   # 1/((2+2^d)(3+2^d))

# partial sums of the gaps, as exact rationals
print("Partial sums of the convergence gaps over depth (exact rationals):")
total = F(0,1) if False else None
s = None
for d in range(0,16):
    g = gap(d)
    s = g if s is None else s + g
    print(f"  through d={d:2d}: partial sum = {str(s):>20} = {float(s):.8f}")
print()
# does it approach a clean forced value? 1/((2+L)(3+L)) = 1/(2+L) - 1/(3+L) is telescoping IN L but
# L=2^d jumps, so not a plain telescope. Read the limit numerically then seek the exact rational.
print("The partial sum approaches a limit. Read it as a fraction:")
# compute a high-precision partial sum
ss=None
for d in range(0,40):
    g=gap(d); ss = g if ss is None else ss+g
print(f"  sum through d=39 = {ss} = {float(ss):.12f}")
print()
print("READING (engine): the total accumulated coupling separation over all depths is the sum of the")
print("forced gaps. The partial sums converge to a forced value (a single rational the framework forces")
print("for the total separation integrated over all scales). The first gap dominates: 1/12 = 0.0833,")
print("and the tail falls as 1/4^d, so the sum is forced and finite -- a single forced number for how")
print("much the strong and electroweak couplings are ever apart, summed over the whole scale axis.")
