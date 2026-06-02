# The forced level<->depth map: carrier crosses one site per tick (D2), depth d has 2^d places
# (num_levels), so self-coupling levels at fold depth d = 2^d. Compose with B3 running and B4 scale.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

print("Forced map (D2 propagation o fold depth): self-coupling level at fold depth d = 2^d.")
print("B4: the scale at fold depth d stands in ratio 2^d to the base. So scale-ratio and level both = 2^d:")
print("the two axes ARE the same axis, 2^d, forced -- the map I wrongly declared absent.")
print()
print("Mixing at each forced fold depth d (running level 2^d):")
for d in range(0,7):
    lvl = Co.num_levels(d)            # 2^d, forced
    s2 = Co.forced_sin2_theta_w_running(lvl)
    scale_ratio = Co.num_levels(d)    # 2^d
    print(f"  fold depth d={d}: scale ratio x{scale_ratio:<4} self-coupling level {lvl:<4} sin^2(theta_W) = {str(s2):>10} = {float(s2):.4f}")
print()
print("measured sin^2(theta_W) = 0.23113 at Z scale (arbiter only).")
print()
# the framework's mass structure forces the Z at the depth where the Z mass-part (1/2 of vacuum) sits:
# scale ratio = 2 => 2^d = 2 => d=1. At d=1, level=2^1=2, sin^2 = running(2):
d_Z = 1
lvl_Z = Co.num_levels(d_Z)
s2_Z = Co.forced_sin2_theta_w_running(lvl_Z)
print(f"Framework's forced Z depth d=1 (mass-part 1/2 = scale ratio 2): level {lvl_Z}, sin^2 = {s2_Z} = {float(s2_Z):.4f}")
