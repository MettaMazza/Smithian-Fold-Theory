# Build sin^2(theta_W) from D11c's forced structure, permitted language only: positive
# magnitudes, ratio/division, the One. NO negatives, NO zero-as-value, NO trig, NO complex.
# D11c (forced): the photon is the combination on the fold-invariant One. The two channels
# carry magnitudes charged=(m-1)/m and neutral=1/m, summing to the One. sin^2(theta_W) is the
# fraction of the photon (the One-combination) carried by the NEUTRAL channel's coupling weight.
#
# In the permitted language the mixing is a PROPORTION: each channel contributes a coupling-
# weight, and the photon (the unbroken One-direction) is built from both. The weight a channel
# contributes to the One-combination is its magnitude. sin^2(theta_W) = neutral-weight as a
# fraction of the total weight that builds the photon. The total weight is NOT the raw sum
# (m-1)/m + 1/m = 1 (that is the magnitude sum); it is the sum of the SQUARED couplings, because
# the photon couples through each channel by that channel's coupling and the invariant combination
# weights each channel by its own coupling (D11c: each channel projects onto the One by its own part).
from fractions import Fraction as F

def charged(m): return F(m-1, m)   # the charged-channel coupling weight (PH5/D11b)
def neutral(m): return F(1, m)      # the neutral-channel coupling weight (D11b)

print("Build sin^2(theta_W) = neutral^2 / (charged^2 + neutral^2)  -- the proportion of the")
print("invariant One-combination carried through the neutral channel, ratio of squared couplings,")
print("all positive magnitudes, no apparatus:")
for m in (2,3,4,5):
    c, n = charged(m), neutral(m)
    s2 = (n*n) / (c*c + n*n)        # ratio of positive magnitudes; the photon projection
    print(f"  m={m}: charged={c} neutral={n}  ->  sin^2(theta_W) = {n*n}/({c*c}+{n*n}) = {s2} = {float(s2):.4f}")
print()
print("At the electroweak fold m=2:")
m=2; c,n=charged(m),neutral(m); s2=(n*n)/(c*c+n*n)
print(f"  sin^2(theta_W) forced = {s2} = {float(s2):.4f}")
print(f"  measured (on-shell, hep-ex/9405008): 0.2218..0.2240 ; (Z-pole, 1911.11528): 0.23113")
print()
# also test the alternative: tan^2 form (neutral/charged)^2, the standard Weinberg relation shape
print("Cross-form: tan^2(theta_W) = (neutral/charged)^2, sin^2 = t/(1+t):")
for m in (2,3,4):
    c,n=charged(m),neutral(m); t=(n/c)*(n/c); s2=t/(1+t)
    print(f"  m={m}: tan^2={t}  sin^2 = {s2} = {float(s2):.4f}")
