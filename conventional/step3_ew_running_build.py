# Build the electroweak running by the SAME construction as D10b/D10g (charge.py), permitted
# language only: accumulated source = matter + carrier self-charge once per level, effective
# coupling = that over bare, all positive magnitudes, ratio/division, the One. No apparatus.
import sys; sys.path.insert(0, 'pure')
from fractions import Fraction as F

ONE = F(1,1)
def accumulated_source(matter, self_charge, levels):
    s = matter
    for _ in range(levels): s = s + self_charge   # positive addition, once per level
    return s
def effective_coupling(matter, self_charge, level):
    return accumulated_source(matter, self_charge, level) / matter   # ratio of positive magnitudes

# The weak charged carrier carries the charge it mediates. Its self-charge is the charged-channel
# coupling itself, (m-1)/m, at the electroweak fold m=2 -> 1/2. The neutral carrier preserves the
# hand: chargeless, does NOT run (absence). So as range grows, the charged coupling grows, the
# neutral does not, and the channels -- equal at the bare level (both 1/2) -- SEPARATE.
m = 2
charged0 = F(m-1, m)   # bare charged coupling = 1/2
neutral0 = F(1, m)     # bare neutral coupling = 1/2, chargeless: constant

print("Electroweak fold m=2. Bare: charged=neutral=1/2 -> sin^2 = 1/2. Now RUN by D10b construction:")
print("charged self-charge feeds each level; neutral chargeless (flat). sin^2 = neutral^2/(charged^2+neutral^2):")
print()
self_charge = charged0   # the charged carrier's self-charge
for level in range(0, 9):
    if level == 0:
        c = charged0
    else:
        # effective charged coupling grows; but a COUPLING cannot exceed the One (no value past whole).
        # The framework caps at the One: the accumulated source over bare, but the COUPLING is the
        # holding part (source-1)/source -> stays a proper part of the One. Use g=(s-? ) NO: build
        # the coupling as the framework's holding ratio of the accumulated source.
        s = accumulated_source(ONE, self_charge, level)   # accumulated source, matter=One
        c = F(s - 1, s) if s > 1 else charged0             # holding part (m-1)/m generalised: (s-1)/s
    n = neutral0                                            # neutral flat (chargeless)
    s2 = (n*n) / (c*c + n*n)
    print(f"  level={level}: charged={c}={float(c):.4f}  neutral={n}  sin^2(theta_W)={s2}={float(s2):.4f}")
print()
print("measured sin^2(theta_W) at Z scale = 0.23113 [1911.11528]; on-shell 0.2218-0.2240 [hep-ex/9405008]")
