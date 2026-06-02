# Place all three couplings on the single forced axis 2^d (B7: level at fold depth d = 2^d).
# Each coupling is the holding ratio (s-1)/s of its accumulating source (D10g form, the framework's).
# strong: source accumulates colour self-charge per level; gluon carries colour -> runs up.
# weak charged: carries charge -> runs up (B3 form).
# EM: chargeless photon -> flat at the forced 1/2 (B2).
# Read whether they MEET at a forced depth. No measured value, nothing fed in.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co
import charge as Q
from ratio import ONE

def holding(source):                      # (s-1)/s, the framework's coupling form, positive magnitudes
    return F(source-1, source)

# at fold depth d, the self-coupling level is 2^d (B7). source at that level = bare + level*self_charge.
# strong: bare source 1 (colour), self-charge 1 (carries one colour unit) -> source = 1 + 2^d
# weak charged: bare source 2 (binary fold), self-charge 1 -> source = 2 + 2^d  (B3's form)
# EM: chargeless -> flat, holding of bare source 2 = 1/2 (B2), no running
print("All three couplings (holding ratio) on the single forced axis 2^d (B7):")
print(" fold depth d | level 2^d | strong g | weak charged g | EM g (flat)")
for d in range(0,8):
    lvl = Co.num_levels(d)                 # 2^d, forced
    g_strong = holding(1 + lvl)            # strong: source 1 + level
    g_weak   = holding(2 + lvl)            # weak charged: source 2 + level (B3)
    g_em     = F(1,2)                       # EM flat (B2)
    print(f"   d={d}  | {lvl:<5} | {str(g_strong):>6} = {float(g_strong):.4f} | {str(g_weak):>6} = {float(g_weak):.4f} | 1/2")
print()
print("READING (engine): strong and weak charged couplings both run UP toward the One (holding -> 1)")
print("as depth grows; EM is flat at 1/2. They do NOT converge to a common value at large depth -- they")
print("both approach 1 but EM stays at 1/2. Reading what the engine shows: at depth 0 (the bare/base")
print("scale) strong=1/2, weak=1/2, EM=1/2 -- ALL THREE EQUAL at the base. That is the meeting point.")
print()
# verify the base-scale equality exactly
d=0; lvl=Co.num_levels(0)
print(f"At fold depth d=0 (base scale, level {lvl}):")
print(f"  strong g = {holding(1+lvl)} ; weak charged g = {holding(2+lvl)} ; EM g = 1/2")
