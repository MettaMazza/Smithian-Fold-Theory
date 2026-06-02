# Rebuild: each sector runs from its OWN forced bare coupling g*=(m-1)/m (PH5/U5), strong at m=3,
# electroweak at m=2. Place both on the single forced axis 2^d (B7) and read whether they meet.
# Each runs by the holding form of its accumulating source; bare source set so holding = g* at level 0.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

# bare g* = (m-1)/m. holding(s)=(s-1)/s = g* when s = m. So bare source = m (the fold factor itself).
# running: source accumulates self-charge (the One) per self-coupling level. level at depth d = 2^d (B7).
def g_running(m, d):
    lvl = Co.num_levels(d)          # 2^d forced
    s = F(m + lvl, 1)              # bare source m (gives g*=(m-1)/m) + one per level
    return F(s-1, s)

print("Each sector from its own forced bare coupling g*=(m-1)/m, on the single forced axis 2^d:")
print(" depth d | level | strong (m=3) | electroweak (m=2)")
for d in range(0,8):
    lvl=Co.num_levels(d)
    gs=g_running(3,d); ge=g_running(2,d)
    print(f"   d={d}  | {lvl:<4} | {str(gs):>7} = {float(gs):.4f} | {str(ge):>7} = {float(ge):.4f}")
print()
# do they meet? strong bare 2/3, ew bare 1/2. both run up toward 1. difference shrinks. read it.
print("READING (engine): strong starts 2/3, electroweak starts 1/2; both run up toward the One as depth")
print("grows, the gap between them shrinking monotonically. Read the gap (strong - ew via take, positive):")
for d in range(0,10):
    gs=g_running(3,d); ge=g_running(2,d)
    gap = gs - ge if gs>ge else ge-gs
    print(f"   d={d}: gap = {gap} = {float(gap):.5f}")
print()
print("The gap shrinks toward absence as depth grows -- the couplings CONVERGE at deep levels (high")
print("self-coupling, the framework's high-energy limit). They meet in the limit, not at a finite forced")
print("depth: asymptotic convergence to the One. Reported as the engine shows it, nothing fed in.")
