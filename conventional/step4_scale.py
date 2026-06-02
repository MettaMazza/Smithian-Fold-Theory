# Scale-fixing attempt, sovereign (no measured energy fed in). Level is a bare range-count in the
# corpus; the framework forces NO energy-per-level. So a scale-fixing can only be: does the framework
# single out a LEVEL by its own structure, at which the mixing takes a framework-distinguished value?
# Test framework-internal marks, NOT the measured 0.231.
from fractions import Fraction as F
ONE = F(1,1)
def charged(level):
    s = F(2+level,1); return F(s-1,s)        # holding part of accumulating source
def neutral(): return F(1,2)
def sin2(level):
    c=charged(level); n=neutral(); return (n*n)/(c*c+n*n)

print("Framework-distinguished values the running might be pinned to (no measured input):")
print("  the half 1/2, the third 1/3, the quarter 1/4, the fifth 1/5 -- fold-native fractions.")
print()
for target,nm in [(F(1,2),'1/2'),(F(1,3),'1/3'),(F(1,4),'1/4'),(F(1,5),'1/5')]:
    hit = [k for k in range(40) if sin2(k)==target]
    print(f"  sin^2 = {nm}: forced exactly at level(s) {hit if hit else 'NONE (never exactly equals)'}")
print()
print("READING (engine, not adjudication):")
print("  The running passes THROUGH fold-native fractions but the framework does not force a level to")
print("  BE the electroweak scale: 'level' carries no forced energy, and no internal mark says 'this")
print("  level is where the measurement is taken'. The scale-fixing is NOT forced by the current corpus.")
print("  To attach level to the Z energy would require feeding in a measured mass -- 11.2 forbids it.")
print()
print("  What the framework forces, exactly: sin^2 = 1/2 bare, running monotonically down through the")
print("  fold-native fractions. What it does NOT force: an energy per level. The scale-fixing is a")
print("  WALL located precisely here -- the missing construction is an energy-per-level (a forced map")
print("  from range-count to physical scale), which the corpus does not supply and which cannot be")
print("  built by importing the Z mass. It is the next construction toward building, named at its edge.")
