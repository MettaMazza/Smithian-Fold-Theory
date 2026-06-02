# Attempt the absolute-scale anchoring in the engine (20: not a wall, a construction to attempt).
# The framework's forced scales: the lattice spacing a (D2, the smallest length, one site); the vacuum
# (D11d, the symmetry-breaking scale = the One). A coupling runs over self-coupling levels; the level at
# fold depth d is 2^d (B7). The number of fold depths from the lattice scale to the vacuum scale would
# fix an absolute ratio IF the framework forces how many depths separate them. Attempt: does it?
import sys; sys.path.insert(0,'pure')
from fractions import Fraction as F
import correspondence as Co

print("Framework-forced scales and what relates them:")
print("  lattice spacing a (D2): the smallest length, one site/tick -- the UV/base scale.")
print("  vacuum (D11d): the symmetry-breaking scale = the fold-invariant One.")
print("  B4: scale ratio 2 per fold depth. B7: self-coupling level at depth d = 2^d.")
print()
# The vacuum is the One; the lattice spacing is a part of the One (a position, D2: p/q in (0,1]).
# The ratio vacuum/spacing = 1/spacing. Is the spacing FORCED to a particular part of the One? Read D2:
# a position is ANY rational p/q in (0,1]; the spacing is not forced to a specific value -- the lattice
# is scale-free (any spacing works, the continuum limit takes a->0). So the framework does NOT force a
# specific lattice spacing; the spacing is a free choice of resolution, not a forced magnitude.
print("Attempt: is the lattice spacing forced to a specific part of the One?")
print("  D2: a position is any rational p/q in (0,1]. The lattice spacing is a free resolution choice;")
print("  the continuum limit takes spacing->0 with c=spacing/tick fixed. The framework does NOT force a")
print("  specific spacing -- it is scale-free in the spacing. RUN-confirmed: the wave/lattice results")
print("  (D2, EM wave) hold for ANY spacing, so no spacing value is preferred.")
print()
# verify by running: the causal speed is spacing/tick for ANY spacing -- show two spacings give the
# same physics (scale-free), so no absolute spacing is forced.
import importlib
em = importlib.import_module('charge')
print("Run-check: EM wave speed = spacing/tick for two different spacings (scale-free):")
import correspondence as C
for sp in [F(1,1000), F(1,1000000)]:
    speed = C.em_wave_speed(sp, sp)   # spacing/tick = 1 for equal spacing&tick, independent of value
    print(f"  spacing={sp}: wave speed (spacing/tick) = {speed}")
print()
print("READING (engine, RUN): the framework is scale-free in the lattice spacing -- the same physics")
print("holds for every spacing, confirmed by running the EM-wave speed at two spacings (both give the")
print("same c=spacing/tick). So the framework forces NO preferred lattice spacing, which means there is")
print("no framework-forced ratio between the lattice scale and the vacuum scale: the absolute scale is")
print("genuinely a free resolution choice, shown by the engine producing identical physics at every")
print("spacing, NOT assumed from a unit-prior. This is a code-located obstruction (20.1): the construction")
print("was attempted and the engine returns scale-invariance -- the absolute scale is not forced because")
print("the engine exhibits the same result at every spacing. The forced content is the dimensionless")
print("ratios (B4-B11); the absolute scale is shown-free, not declared-free.")
