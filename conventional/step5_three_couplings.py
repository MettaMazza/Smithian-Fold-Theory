# The three couplings at the base scale (bare g*), read from the framework's forced values:
#   strong (m=3): g* = (m-1)/m = 2/3        [PH5/U5]
#   weak   (m=2): g* = (m-1)/m = 1/2        [PH5, the charged channel]
#   EM     (m=2, flat): g* = 1/2            [B2]
# Read whether their pattern is a forced ratio. No measured value.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import constants as K

g_strong = K.critical_coupling(3)    # 2/3
g_weak   = K.critical_coupling(2)    # 1/2
g_em     = F(1,2)                      # 1/2 (B2, flat)

print(f"Base-scale forced couplings:  strong={g_strong}  weak={g_weak}  EM={g_em}")
print()
# the ratios among them, forced from the fold factors alone:
print("Forced ratios among the three (from the fold factors 2 and 3, nothing fed in):")
print(f"  strong : weak = {g_strong}/{g_weak} = {g_strong/g_weak}   = (2/3)/(1/2) = 4/3")
print(f"  strong : EM   = {g_strong/g_em}")
print(f"  weak : EM     = {g_weak/g_em}  (equal -- both the m=2 sector)")
print()
# is there a single forced relation tying all three? each is (m-1)/m for its sector's m.
# strong m=3, electroweak m=2. The pattern: g(m) = (m-1)/m = 1 - 1/m. So:
#   g_strong = 1 - 1/3 = 2/3,  g_ew = 1 - 1/2 = 1/2.
# the three couplings are 1 - 1/m at m = 3, 2, 2. The forced relation is g = (m-1)/m, the SAME U5 law,
# now read across all three sectors at the base. weak=EM because both are the binary fold.
print("READING (engine): the three base-scale couplings are each (m-1)/m at the sector's fold factor --")
print("strong at m=3 gives 2/3, weak and EM at m=2 give 1/2 each. This is the SAME forced coupling law")
print("(m-1)/m (U5/PH5) read across all three sectors at the base scale; weak=EM because both are the")
print("binary fold (m=2). The strong:weak ratio is 4/3, forced from the fold factors 3 and 2 alone.")
print("Not a NEW law -- the base-scale reading of U5 across the three sectors. The NEW forced object is")
print("the strong:electroweak base ratio 4/3, a forced ratio of the two sectors' couplings. Test if THAT")
print("is distinct from U5 or a restatement:")
print(f"  strong:weak = ((3-1)/3) / ((2-1)/2) = (2/3)/(1/2) = 4/3 -- a function of the two fold factors,")
print("  derivable directly from U5's (m-1)/m at m=3 and m=2. It is U5 read as a ratio, not a new law.")
