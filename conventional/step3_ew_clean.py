# Clean electroweak running, built exactly as D10b/D10g: the source accumulates the carrier's
# self-charge once per level; the coupling is the holding part (s-1)/s of the source (the same
# (m-1)/m form PH5 forces). Monotonic from level 0, no artefact. Permitted language: positive
# magnitudes, ratio/division, the One. The neutral carrier is chargeless (D11e: preserves the hand)
# so its coupling is flat. sin^2 = neutral^2/(charged^2+neutral^2).
from fractions import Fraction as F
ONE = F(1,1)

# bare source at the electroweak fold m=2: the matter charge is the One; the charged carrier's
# self-charge is the bare charged coupling's source-unit. Build source = One + (level)*self.
# The bare charged coupling is (m-1)/m = 1/2, which is the holding part of source=2 (since (2-1)/2=1/2).
# So the bare source is 2. Each running level the charged carrier adds its self-charge (its colour),
# which for the binary fold is the One (one charge kind carried). Source_k = 2 + k.
def charged_coupling(level):
    s = F(2 + level, 1)          # source accumulates One per level (self-charge of the carrier)
    return F(s - 1, s)            # holding part (s-1)/s -- the same form as (m-1)/m, monotonic up
neutral = F(1, 2)                 # chargeless carrier: flat across range (D11e)

print("Clean EW running (m=2), monotonic from level 0, built as D10g (holding part of accumulating source):")
prev = None
mono = True
for level in range(0, 20):
    c = charged_coupling(level)
    s2 = (neutral*neutral) / (c*c + neutral*neutral)
    flag = ""
    if prev is not None and s2 > prev: mono = False; flag = "  <-- NON-MONOTONIC"
    prev = s2
    if level <= 12 or abs(float(s2)-0.231) < 0.02:
        print(f"  level={level:2d}: charged={c}={float(c):.4f}  sin^2={s2}={float(s2):.4f}{flag}")
print()
print("monotonic decreasing from level 0:", mono)
print()
# where does it cross the measured band? report the level, do NOT fit.
print("measured arbiter (never fed in): sin^2(theta_W) = 0.23113 at Z scale [1911.11528];")
print("on-shell 0.2218-0.2240 [hep-ex/9405008]. Report which level the forced running passes it:")
for level in range(0, 40):
    c = charged_coupling(level)
    s2 = float((neutral*neutral) / (c*c + neutral*neutral))
    if s2 <= 0.2311:
        cprev = charged_coupling(level-1)
        s2prev = float((neutral*neutral)/(cprev*cprev+neutral*neutral))
        print(f"  forced running passes 0.2311 between level {level-1} (sin^2={s2prev:.4f}) and level {level} (sin^2={s2:.4f})")
        break
