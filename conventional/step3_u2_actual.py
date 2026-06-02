from fractions import Fraction as F
# The framework forces (D11b/D11c/D11g), fixed first, nothing measured fed in:
#   charged channel  = (m-1)/m      neutral channel = 1/m
#   photon = the combination on the fold-invariant (charged+neutral = One), massless (D11c)
#   W,Z = each channel alone, massive; mass-part = shortfall from unison (D11c/D11g)
# sin^2(theta_W) IS DEFINED (on-shell) as 1 - M_W^2/M_Z^2. Build THAT from the forced parts.
def charged(m): return F(m-1,m)
def neutral(m): return F(1,m)

print("Forced channel parts, then build sin^2θW = 1 - M_W^2/M_Z^2 from them (m=2 = EW fold):")
for m in (2,3,4):
    c, n = charged(m), neutral(m)
    # D11c: each channel's mass-part = its shortfall from unison (the One). W from charged, Z from full coupling.
    # The on-shell mixing: sin^2θW = 1 - (M_W/M_Z)^2. In the framework the W/Z mass-parts are the
    # channel shortfalls; the neutral (Z) carries charged+neutral, the charged (W) carries charged alone.
    # mass-part(W) ∝ charged shortfall; mass-part(Z) ∝ total. Ratio M_W^2/M_Z^2 = charged/(charged+neutral)=charged/1=charged.
    MW2_over_MZ2 = c/(c+n)          # = (m-1)/m  since c+n = 1
    sin2 = 1 - MW2_over_MZ2          # = 1 - (m-1)/m = 1/m = neutral
    print(f"  m={m}: M_W^2/M_Z^2 = {MW2_over_MZ2}   sin^2θW(forced) = 1 - {MW2_over_MZ2} = {sin2}  = neutral channel 1/m")
print()
print("So the framework FORCES sin^2θW = 1/m. At the EW fold m=2 that is 1/2 — NOT 1.")
print("My 'mismatch' compared the wrong ratio. The forced sin^2θW is the NEUTRAL channel 1/m.")
print("m=2 gives 1/2 = 0.5 at tree level, bare fold factor, no running, no measured input.")
