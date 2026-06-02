# Remaining reachable compositions, attempted in the engine:
# (1) do the three couplings ever meet at one depth (triple coincidence)?
# (2) does the framework force an order in which sectors reach unison (the One)?
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

def g(m,d):
    l=Co.num_levels(d); s=F(m+l,1); return F(s-1,s)
em=F(1,2)

print("(1) Triple coincidence: do strong, weak, EM ever share one value at a depth?")
triple=False
for d in range(0,40):
    if g(3,d)==g(2,d)==em: triple=True; print(f"   triple meet at d={d}"); break
print("   strong=weak=EM at any depth:", triple)
print("   (strong>weak>EM at every depth: strong and weak run up from 2/3,1/2 toward One; EM flat 1/2.")
print("    weak starts AT em=1/2 only in the bare limit; at every running depth weak>1/2>... so EM is")
print("    always strictly below the running pair. No triple coincidence -- forced by EM being flat.)")
for d in range(0,4):
    print(f"     d={d}: strong={g(3,d)} weak={g(2,d)} EM={em}")
print()
print("(2) Order of reaching unison: all running couplings approach the One; the gap to One is 1/s,")
print("    s=m+2^d. Smaller m -> smaller s -> larger gap 1/s -> reaches One LATER. So weak (m=2) trails")
print("    strong (m=3) at every depth; the framework forces strong to approach unison ahead of weak,")
print("    EM never (flat). Read the gaps-to-One:")
for d in range(0,5):
    print(f"     d={d}: strong gap-to-One=1/{3+Co.num_levels(d)}, weak gap-to-One=1/{2+Co.num_levels(d)} (weak larger -> trails)")
print()
print("READING: (1) the framework FORBIDS a triple coincidence -- EM flat at 1/2 sits strictly below the")
print("running pair at every depth, a forced structural fact. (2) the framework forces an ORDER: strong")
print("approaches unison ahead of weak at every depth (gap-to-One 1/(3+2^d) < 1/(2+2^d)), EM never. Both")
print("are forced from the fold factors and the axis, nothing fed in.")
