# The framework DOES anchor a scale: D11d forces the symmetry-breaking scale to be the displaced
# vacuum = the fold-invariant One. The bare mixing 1/2 sits AT that breaking scale (depth 0). The
# running carries it away as depth grows. Attempt: does the framework force the depth at which the
# mixing is MEASURED, by its own structure -- i.e. is there a forced number of levels between the
# breaking scale (vacuum) and the observation scale?
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

# The framework's mass-parts (D11g): charged mass-part 1/m, neutral mass-part (m-1)/m at m=2 -> both 1/2.
# The W/Z masses ARE these mass-parts. The observation scale of sin^2(theta_W) IS the Z mass scale.
# In the framework the Z mass-part is a fixed fraction of the vacuum (the One). So the depth of
# observation is set by how many running levels correspond to the ratio (Z mass)/(vacuum scale).
# The framework forces the vacuum = One and the Z mass-part = a forced fraction. Read that fraction
# and whether it picks a depth.
print("D11d: symmetry-breaking scale = displaced vacuum = the fold-invariant One (depth 0).")
print("D11g forced mass-parts at m=2: charged=1/2, neutral=1/2 (the W and Z mass-parts as fractions of One).")
print()
# the Z is the neutral-channel-derived massive mediator (D11c); its mass-part fraction of the vacuum:
print("The Z mass-part as a fraction of the vacuum (One):", F(1,2))
print()
# does a forced depth correspond to the Z mass relative to the vacuum, via B4's scale ratio 2^k?
# scale at depth k = vacuum / 2^k (B4: factor 2 per depth, running toward shorter scales as depth grows
# -- OR vacuum * 2^k). The Z mass-part is 1/2 of the vacuum = vacuum / 2 = depth k where 2^k = 2 => k=1.
print("B4 forced scale ratio: 2 per depth. Z mass-part = 1/2 of vacuum = vacuum/2 = the scale at depth k")
print("where 2^k = 2, i.e. k=1. So the framework's OWN mass structure places the Z scale at depth 1.")
print()
s2_at_depth1 = Co.forced_sin2_theta_w_running(1)
print(f"Forced sin^2(theta_W) at depth 1 (the framework's Z scale) = {s2_at_depth1} = {float(s2_at_depth1):.4f}")
print(f"Measured sin^2(theta_W) at Z scale (arbiter only) = 0.23113")
print()
print("READING: if the framework's mass structure forces the Z scale at depth 1, the forced mixing there")
print("is 9/25 = 0.36, NOT 0.231. So THAT anchoring does not land at measurement. The depth-1 anchor is")
print("forced by the 1/2 mass-part fraction; it gives 0.36. This is a forced number (0.36 at the framework's")
print("own Z-scale depth), reported as the engine gives it -- not 0.231. The mass-structure anchor is built")
print("and it forces depth 1; the value there is 0.36. Whether the running rate or the anchor needs a")
print("different framework construct to land at 0.231 is the next reachable piece: the running RATE.")
