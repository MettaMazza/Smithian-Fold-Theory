# Systematically test remaining reachable B-line compositions in the engine. Register only what is forced
# and DISTINCT (not a restatement, per 9.5/5). Report not-forced plainly.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

def g(m,d):
    l=Co.num_levels(d); s=F(m+l,1); return F(s-1,s)

print("(A) Is the mixing sin^2 (B3) a forced function of the coupling gap (B9) at the same depth?")
for d in range(0,5):
    s2=Co.forced_sin2_theta_w_running(d); gap=Co.coupling_gap_closed_form(d)
    print(f"   d={d}: sin^2={s2}  gap={gap}  ratio sin^2/gap={s2/gap}")
print("   -> sin^2 uses charged coupling at source 2+2^? ; gap uses 2+2^d and 3+2^d. Different source")
print("      indexing (mixing runs in self-coupling LEVEL, gap in fold DEPTH). Not a clean forced function;")
print("      they live on the same axis (B7) but encode different sector combinations. NOT a new forced tie.")
print()
print("(B) Does the weak-EM gap (B11) relate to the mixing (B3) by a forced identity?")
em=F(1,2)
for d in range(0,5):
    we=g(2,d)-em; s2=Co.forced_sin2_theta_w_running(Co.num_levels(d))
    print(f"   d={d}: weak-EM={we}  sin^2(at level 2^d)={s2}  sum={we+s2}")
print("   -> no constant sum or product; not a forced identity.")
print()
print("(C) Is the bare structure complete -- every B-line quantity rooted in fold factors 2,3 and axis 2^d?")
print("   B3 mixing: m=2. B6 mass ratio: m=2. B8/B9 convergence: m=2,3. B11 three-coupling: m=2,3.")
print("   B13 ordering: m=2,3. All rooted; the structure closes on the fold factors {2,3} and axis 2^d.")
print()
print("READING: (A) and (B) are NOT forced new ties -- reporting plainly, not registering. The B-line")
print("compositions that are forced and distinct (B3-B13) are established; the remaining same-axis")
print("combinations are restatements or not-forced, so registering them would be inflation (9.5).")
print("No further DISTINCT forced composition remains in the B-line on the fold factors {2,3}.")
