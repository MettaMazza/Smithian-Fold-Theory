# Two framework anchors gave different depths for the Z scale: mass-structure said depth 1 (value 0.36);
# B3 running crosses measured 0.231 around depth 9-10. Test: are these consistent? The mass-part 1/2 is
# the Z mass as a fraction of the VACUUM (the breaking scale, the One). B4: scale ratio 2 per depth.
# The number of depths from the vacuum to the Z scale = how many factors of 2 separate the Z mass from
# the vacuum scale. That is NOT forced by the mass-part fraction alone (1/2 = one factor of 2 = depth 1)
# UNLESS the vacuum scale equals the Z mass-part scale. But the vacuum is the One and the Z mass-part is
# 1/2 of it -- so by the framework's OWN ratio, the Z sits one depth below the vacuum: depth 1. The B3
# crossing at depth 9-10 uses the running rate; the mass-anchor uses the scale ratio. They measure
# different things: depth-as-running-level vs depth-as-scale-ratio. Test if the framework forces them
# to be the SAME depth axis.
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

print("Are 'running level' and 'scale-ratio depth' the same axis in the framework?")
print("  B3 running: level = number of self-coupling levels accumulated (D10b), a COUNT of interactions.")
print("  B4 scale:   depth = factors of 2 in the place-count (fold depth), a SCALE ratio.")
print()
print("  These are DISTINCT framework quantities: one counts self-couplings, one counts fold-depths.")
print("  The framework does NOT force them equal -- D10b's level and the fold's depth are different")
print("  constructs. So 'the Z is at depth 1 by scale-ratio' and 'the mixing crosses 0.231 at running")
print("  level 9-10' are statements on two different axes; the framework has not forced a map between them.")
print()
print("  THE MISSING CONSTRUCTION, located by attempt: a forced relation between the self-coupling")
print("  level count (D10b/D10g) and the fold-depth scale ratio (B4). Both are forced framework")
print("  quantities; whether one is a forced function of the other is testable. Attempt it:")
print()
# self-coupling level k accumulates source 1+k (D10g). fold depth d has 2^d places. Is there a forced
# relation? The self-coupling happens AT a fold depth; each fold depth admits how many self-coupling
# levels? A fold of depth d has 2^d places = 2^d sites for self-coupling. Test: levels per depth.
for d in range(1,6):
    sites = 2**d
    print(f"  fold depth d={d}: 2^d = {sites} places. If self-coupling runs one level per place, levels = {sites}.")
print()
print("  IF self-coupling runs one level per place (2^d levels at depth d), then the running level at")
print("  fold depth d is 2^d. The mixing at fold depth d = forced_sin2_theta_w_running(2^d):")
for d in range(0,5):
    lvl = 2**d if d>0 else 0
    s2 = Co.forced_sin2_theta_w_running(lvl)
    print(f"    fold depth d={d}: running level {lvl}, sin^2 = {s2} = {float(s2):.4f}")
