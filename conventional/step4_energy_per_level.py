# Reachable reduction (12.1) before any wall: can energy-per-level be BUILT from the framework's
# own constructs, not imported? The framework has: lattice spacing/tick (speed c, D2); fold depth k
# giving 2^k places; the level-spacing of bound states (correspondence.level_spacing). Attempt: is a
# scale forced by the fold's own depth-doubling, so that level k carries a forced RATIO of scales?
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

print("Framework constructs that carry a scale-like quantity, read from the engine:")
# level spacing of bound states (PH4): the rungs are evenly spaced; their spacing is a forced ratio
for k in range(1,6):
    try:
        ls = Co.level_spacing(k)
        print(f"  level_spacing(k={k}) = {ls}")
    except Exception as e:
        print(f"  level_spacing(k={k}) error: {e}")
print()
# the fold's depth-doubling: each depth k has 2^k places. A scale RATIO between depths is 2^k forced.
print("Fold depth-doubling: places at depth k = 2^k (forced). Ratio of scales between adjacent depths = 2.")
print("  This IS a framework-forced scale ratio (a factor of 2 per depth) -- BUT it is a ratio, not an")
print("  absolute energy. The running needs an ABSOLUTE scale to say 'level k = the Z energy'.")
print()
print("READING (engine):")
print("  The framework forces scale RATIOS (2 per fold depth; the even rung-spacing of PH4) but NO")
print("  ABSOLUTE energy -- because the One is dimensionless and the whole system is built in pure")
print("  ratios. An absolute energy scale (eV, GeV) is a UNIT, and 11.2 forbids importing a unit value.")
print("  So the framework forces the mixing's running CURVE in level (dimensionless) and forces scale")
print("  RATIOS between levels, but an absolute level<->Z-mass identification needs a measured unit and")
print("  is therefore NOT a forced result. This is the true edge, reached by attempting the reduction:")
print("  the dimensionless running is forced; the absolute scale is dimensionful and not the framework's")
print("  to force without importing a unit. The reachable piece (the dimensionless running + forced")
print("  scale-ratios) is BUILT; the dimensionful absolute scale is the named edge, not a built result.")
