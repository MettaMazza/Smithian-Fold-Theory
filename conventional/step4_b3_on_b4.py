# Chain: re-express B3's running against B4's forced scale-ratio (factor 2 per fold depth). If level k
# corresponds to fold depth k, the scale at depth k stands in ratio 2^k to the base -- a forced,
# dimensionless scale axis. State B3's running on THAT axis. No measured value, no unit.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

print("B3 running re-expressed on B4's forced dimensionless scale axis (scale ratio 2 per depth):")
print(" depth k | scale-ratio to base (2^k) | sin^2(theta_W) forced")
for k in range(0, 12):
    scale_ratio = 2**k                       # B4: forced factor 2 per depth, dimensionless
    s2 = Co.forced_sin2_theta_w_running(k)
    print(f"   k={k:2d} | x{scale_ratio:<5d} | {str(s2):>8} = {float(s2):.4f}")
print()
print("READING (engine): the framework forces the FULL running curve of sin^2(theta_W) as a function of")
print("its own dimensionless scale axis (the fold-depth scale ratio 2^k) -- the bare value 1/2 at the")
print("base depth, falling monotonically as depth/scale-ratio grows. This is B3 stated on B4's forced")
print("scale structure: a forced dimensionless running curve. The ONE thing still not forced is the")
print("absolute anchoring of the base depth to a physical energy (the unit), which 11.2 bars importing.")
print("The forced object is complete as a dimensionless curve; the dimensionful anchor is the open edge.")
