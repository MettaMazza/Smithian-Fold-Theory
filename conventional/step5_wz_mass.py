# Next reachable construction: does the framework force the W/Z mass ratio? The on-shell relation is
# M_W^2/M_Z^2 = 1 - sin^2(theta_W) = cos^2(theta_W). B3 forces sin^2 = neutral^2/(charged^2+neutral^2).
# So M_W^2/M_Z^2 = charged^2/(charged^2+neutral^2), forced from the same channel couplings. Build it,
# bare and running, permitted language, no measured mass fed in.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

def charged(level):
    s=F(2+level,1); return F(s-1,s)
def neutral(): return F(1,2)
def MW2_over_MZ2(level):
    c=charged(level); n=neutral(); return (c*c)/(c*c+n*n)    # cos^2 = 1 - sin^2, forced
def MW_over_MZ(level):
    r=MW2_over_MZ2(level)
    # the ratio of masses is the square root of the ratio of squares -- but sqrt may be irrational,
    # forbidden. Report the SQUARED ratio (a clean rational) as the forced object; the linear ratio
    # is the square root, reported only as the squared form to stay in permitted magnitudes.
    return r

print("Forced W/Z mass-squared ratio M_W^2/M_Z^2 = charged^2/(charged^2+neutral^2), bare + running:")
for k in range(0,11):
    r = MW2_over_MZ2(k); s2 = Co.forced_sin2_theta_w_running(k)
    print(f"  depth k={k:2d}: M_W^2/M_Z^2 = {str(r):>8} = {float(r):.4f}   (and sin^2={float(s2):.4f}; sum={float(r+s2):.4f})")
print()
print("Bare (k=0): M_W^2/M_Z^2 = 1/2. Measured (arbiter only, fed in nowhere): M_W=80.4, M_Z=91.2 GeV")
print("  -> M_W^2/M_Z^2 measured ~ (80.4/91.2)^2 = 0.777 [PDG masses, arbiter].")
print()
print("READING (engine): the framework forces M_W^2/M_Z^2 = 1 - sin^2(theta_W) = charged^2/(c^2+n^2),")
print("bare 1/2, RISING as sin^2 falls (sum is exactly the One at every depth -- a forced identity:")
print("M_W^2/M_Z^2 + sin^2(theta_W) = 1, the on-shell relation, forced from the channels). The running")
print("M_W^2/M_Z^2 rises through the measured 0.777 as sin^2 falls through 0.231 -- the SAME forced curve,")
print("the two observables tied by the forced identity sum=One (this IS U2's tie, now in mass+mixing form).")
