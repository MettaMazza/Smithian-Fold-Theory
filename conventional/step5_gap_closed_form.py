# Derive the closed form of the coupling gap from the framework's own coupling forms.
# g(m,d) = (s-1)/s with s = m + 2^d. gap = g(3,d) - g(2,d), both holding ratios.
# (s-1)/s = 1 - 1/s. So g(3,d)-g(2,d) = (1 - 1/(3+L)) - (1 - 1/(2+L)) = 1/(2+L) - 1/(3+L), L=2^d.
# = ( (3+L) - (2+L) ) / ((2+L)(3+L)) = 1 / ((2+L)(3+L)).  CLOSED FORM, single ratio.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

def L(d): return Co.num_levels(d)            # 2^d, forced
def gap_closed(d):
    l = L(d)
    return F(1, (2+l)*(3+l))                  # the derived closed form
def gap_engine(d):
    return Co.coupling_gap(d)                  # the engine's computed gap (B8)

print("Derived closed form: gap(d) = 1 / ((2 + 2^d)(3 + 2^d)).  Verify against the engine's B8 gaps:")
all_match = True
for d in range(0,10):
    gc = gap_closed(d); ge = gap_engine(d)
    match = (gc == ge)
    all_match = all_match and match
    print(f"  d={d}: closed = {str(gc):>12}  engine = {str(ge):>12}  match={match}")
print()
print("closed form matches engine at every depth:", all_match)
print()
print("READING (engine): the coupling gap is a SINGLE forced closed-form ratio, gap(d) = 1/((2+2^d)(3+2^d)),")
print("the product of the two sectors' source-magnitudes (2+2^d for electroweak, 3+2^d for strong). The")
print("two sectors' fold factors (2 and 3) are the only inputs; the gap is forced from them and the axis")
print("2^d, nothing fed in. The convergence rate (B8) is this closed form. The denominators are exactly the")
print("two running source-magnitudes, so the gap is one-over-their-product -- a forced ratio of the fold")
print("factors. At deep d the product grows as (2^d)^2, so the gap falls as 1/4^d: forced quadratic-in-scale")
print("convergence, reported as the engine shows it.")
