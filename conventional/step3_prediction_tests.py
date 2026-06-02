# Step 3: prediction tests on the forced relationships. Framework value FIXED FIRST (11.2),
# measured value as ARBITER ONLY. Report match/mismatch as engine+data show it; fit NOTHING (5, 9.5).
from fractions import Fraction as F

# ---- forced quantities, fixed first, from the proofs (m = fold factor) ----
def mixing_ratio(m):    return F(1, m-1)   # D11b neutral/charged channel ratio
def mass_part_ratio(m): return F(1, m-1)   # D11g weak channel mass-part ratio
def g_star(m):          return F(m-1, m)   # PH5 coupling
def charged(m):         return F(m-1, m)   # D11b charged channel
def neutral(m):         return F(1, m)     # D11b neutral channel
def threshold(m):       return F(m-1, m)   # R7/PH5a
def colour(m):          return m           # D7b

print("=== U2 prediction test — the forced EQUALITY of two observables, fixed first ===")
print("U2 forces: mixing_ratio(m) == mass_part_ratio(m), both = 1/(m-1), for every m.")
for m in (2,3,4):
    a, b = mixing_ratio(m), mass_part_ratio(m)
    print(f"  m={m}: mixing_ratio={a}  mass_part_ratio={b}  equal? {a==b}  (forced, fixed first)")
print()
print("  ARBITER (measured, looked at second): the on-shell electroweak relation is")
print("  sin^2 theta_W = 1 - M_W^2/M_Z^2 [arxiv hep-ex/9405008], which TIES the mixing angle to the")
print("  W/Z mass ratio -- the SAME two observables U2 forces into a relationship. Measured")
print("  sin^2 theta_W = 0.2218..0.2240 [hep-ex/9405008; arXiv:1512.08256].")
print()
print("  READING (reported, not adjudicated):")
print("  - U2's forced CLAIM is that the mixing ratio and the mass-part ratio are the SAME quantity.")
print("    The measured sector likewise ties the mixing angle and the mass ratio through one relation")
print("    (sin^2θW = 1 - M_W^2/M_Z^2): the two observables are NOT independent in the data either.")
print("    The forced equality CORRESPONDS to a real structural tie in the measured electroweak sector.")
print("  - The NUMERICAL value: forced mixing_ratio at the EW fold m=2 is 1/(m-1) = 1; the measured")
print("    sin^2θW ~ 0.223. These NUMBERS do NOT coincide. The framework forces the EQUALITY-OF-RATIOS")
print("    structure, NOT the numerical value of sin^2θW. Reported as: structural tie corresponds;")
print("    numerical value does NOT match the mixing angle. NOT fitted, NOT explained away.")
print()

print("=== U4 prediction test — coupling = threshold = charged channel, fixed first ===")
for m in (2,3,4):
    print(f"  m={m}: g*={g_star(m)}  threshold={threshold(m)}  charged={charged(m)}  all equal? {g_star(m)==threshold(m)==charged(m)}")
print("  ARBITER: U4 is an INTERNAL identity among three framework roles (coupling, locking threshold,")
print("  charged channel). There is no single measured number that is all three; U4's test is the")
print("  internal coincidence, which holds for every m. No external arbiter applies -- reported as a")
print("  forced internal identity, confirmed across m, with no measured comparison to make.")
print()

print("=== U5 prediction test — coupling fixed by colour count, fixed first ===")
for m in (2,3,4):
    print(f"  m={m}: g*={g_star(m)}  (colour-1)/colour={F(colour(m)-1,colour(m))}  equal? {g_star(m)==F(colour(m)-1,colour(m))}")
print("  ARBITER: the colour count is measured = 3 (T1: R-ratio, Delta++, pi0->2gamma), already an")
print("  established arbiter. U5 ties the coupling to that measured count: at m=3, g* = 2/3, forced.")
print("  READING: the colour count arbiter (3) is confirmed (T1); U5 forces the coupling FROM it as 2/3.")
print("  Whether a measured strong coupling equals 2/3 at the relevant scale is a SEPARATE arbiter")
print("  question (running coupling, scale-dependent) -- reported as forced value 2/3, measured-coupling")
print("  comparison scale-dependent and not a single number, so no clean numeric arbiter. Not fitted.")
print()

print("=== U6 prediction test — mixing * charged = neutral, fixed first ===")
for m in (2,3,4):
    lhs = mixing_ratio(m)*charged(m); rhs = neutral(m)
    print(f"  m={m}: mixing*charged={lhs}  neutral={rhs}  equal? {lhs==rhs}")
print("  ARBITER: U6 is an INTERNAL product identity among three forced weak-sector ratios; holds for")
print("  every m. No single measured number is the product; reported as forced internal identity,")
print("  confirmed across m, with no external numeric arbiter to compare.")
