# The three couplings on the single forced axis 2^d: strong (m=3, runs), weak (m=2, runs), EM (flat 1/2).
# B8/B9 gave strong-weak. Now the separations involving EM (the flat one). Read the forced structure.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

def g(m,d):
    l=Co.num_levels(d); s=F(m+l,1); return F(s-1,s)   # running holding (s-1)/s
def g_em(): return F(1,2)                              # EM flat (B2)

print("Three couplings on axis 2^d, and separations from flat EM (1/2):")
print(" d | strong(m3) | weak(m2) | EM | strong-EM gap | weak-EM gap")
for d in range(0,8):
    gs=g(3,d); gw=g(2,d); ge=g_em()
    se = gs-ge if gs>ge else ge-gs
    we = gw-ge if gw>ge else ge-gw
    print(f" {d} | {str(gs):>7} | {str(gw):>6} | 1/2 | {str(se):>8} | {str(we):>8}")
print()
# closed forms for the EM gaps: g(m,d)-1/2 = (s-1)/s - 1/2 = (2(s-1)-s)/(2s) = (s-2)/(2s), s=m+2^d.
# strong-EM: (3+2^d-2)/(2(3+2^d)) = (1+2^d)/(2(3+2^d)).  weak-EM: (2+2^d-2)/(2(2+2^d)) = 2^d/(2(2+2^d)).
print("Closed forms (derived): strong-EM = (1+2^d)/(2(3+2^d)) ; weak-EM = 2^d/(2(2+2^d)). Verify:")
allok=True
for d in range(0,8):
    l=Co.num_levels(d)
    se_cf=F(1+l,2*(3+l)); we_cf=F(l,2*(2+l))
    gs=g(3,d); gw=g(2,d); ge=g_em()
    se=gs-ge if gs>ge else ge-gs; we=gw-ge if gw>ge else ge-gw
    ok=(se_cf==se and we_cf==we); allok=allok and ok
    print(f"  d={d}: strong-EM {se_cf}=={se} ; weak-EM {we_cf}=={we}  ok={ok}")
print("all closed forms match:", allok)
print()
print("READING (engine): EM is flat at 1/2; strong and weak run UP away from it, so the strong-EM and")
print("weak-EM gaps GROW with depth (toward 1/2 as the running couplings approach the One), opposite to")
print("the strong-weak gap which shrinks (B9). The three couplings form a forced structure: two running")
print("up and converging with each other (B8/B9), the third flat, the running pair separating from the")
print("flat one by forced closed-form gaps (1+2^d)/(2(3+2^d)) and 2^d/(2(2+2^d)). All forced from the fold")
print("factors 2,3 and the axis 2^d, nothing fed in.")
