# Step 2 exploration — attempt forced cross-observable relationships by composition.
# OUTSIDE the corpus (conventional/) deliberately: this READS what the engine forces
# before anything is registered. A relationship counts only if it holds as an identity
# in m across fold factors with nothing fed in. Pure rationals only; mirrors the engine's
# forced quantities exactly (no apparatus, no fitting).
from fractions import Fraction as F

# the forced quantities, each as a function of the fold factor m (from constants.py / the U-line):
def g_star(m):      return F(m-1, m)        # PH5/PH5a fundamental coupling
def threshold(m):   return F(1, 2) if m==2 else F(m-1, m)  # R7 holding threshold = (m-1)/m generally; 1/2 at m=2
def colour(m):      return F(m, 1)          # D7b colour/fibre count
def mediators(m):   return F(m*m - 1, 1)    # N1 mediator count m^2-1
def mixing(m):      return F(1, m-1)        # D11b electroweak mixing 1/(m-1)
def charged(m):     return F(m-1, m)        # D11b charged weak channel (=g*)
def neutral(m):     return F(1, m)          # D11b neutral channel 1/m

# NOTE threshold: R7 is (m-1)/m generally (PH5a); at m=2 that is 1/2. Use (m-1)/m.
def threshold(m):   return F(m-1, m)

MS = [2,3,4,5]   # fold factors to test the identity across (m=2 binary, m=3 tripling, plus 4,5 as further checks)

def holds(relation, lhs, rhs):
    """report whether lhs(m)==rhs(m) as an identity across all MS"""
    vals = [(m, lhs(m), rhs(m), lhs(m)==rhs(m)) for m in MS]
    ok = all(v[3] for v in vals)
    return ok, vals

# ---- already-registered, as control checks (should all hold) ----
controls = {
 "U4  g* == threshold == charged":      (lambda m: g_star(m),               lambda m: charged(m)),
 "U5  g* == (colour-1)/colour":         (lambda m: g_star(m),               lambda m: F(colour(m)-1, colour(m))),
 "U6  mixing * charged == neutral":     (lambda m: mixing(m)*charged(m),    lambda m: neutral(m)),
}

# ---- NEW candidate compositions to attempt (kept only if forced across MS) ----
candidates = {
 # mediator-count relations
 "C-a  mediators == colour^2 - 1":              (lambda m: mediators(m),                 lambda m: colour(m)**2 - 1),
 "C-b  mediators * neutral == (m^2-1)/m":       (lambda m: mediators(m)*neutral(m),      lambda m: F(m*m-1, m)),
 "C-c  mediators == (1/neutral)^2 - 1":         (lambda m: mediators(m),                 lambda m: F(1,neutral(m))**2 - 1),
 "C-d  mixing * mediators == (m+1)":            (lambda m: mixing(m)*mediators(m),       lambda m: F(m+1,1)),     # since (m^2-1)/(m-1)=m+1
 # threshold / coupling / channel ties beyond U4,U6
 "C-e  g* + neutral == 1":                      (lambda m: g_star(m)+neutral(m),         lambda m: F(1,1)),
 "C-f  charged + neutral == 1":                 (lambda m: charged(m)+neutral(m),        lambda m: F(1,1)),
 "C-g  mixing == neutral/(g*)":                 (lambda m: mixing(m),                    lambda m: neutral(m)/g_star(m)),
 "C-h  mixing*neutral == neutral^2/g*":         (lambda m: mixing(m)*neutral(m),         lambda m: neutral(m)**2/g_star(m)),
 # colour <-> weak ties at common m
 "C-i  colour * neutral == 1":                  (lambda m: colour(m)*neutral(m),         lambda m: F(1,1)),
 "C-j  colour - 1 == 1/mixing":                 (lambda m: F(colour(m)-1,1),             lambda m: F(1,1)/mixing(m)),
 "C-k  g* == 1 - mixing*neutral... (=1-1/m)":   (lambda m: g_star(m),                    lambda m: F(1,1)-neutral(m)),
 # product across three weak observables (U6 is one; seek another independent one)
 "C-l  mixing*charged*colour == 1":             (lambda m: mixing(m)*charged(m)*colour(m), lambda m: F(1,1)),
 "C-m  (1-g*)*colour == 1":                     (lambda m: (F(1,1)-g_star(m))*colour(m),   lambda m: F(1,1)),
}

print("=== CONTROLS (registered U4/U5/U6 — must all hold) ===")
for name,(l,r) in controls.items():
    ok,vals = holds(name,l,r)
    print(f"  [{'HOLD' if ok else 'FAIL'}] {name}")
    if not ok:
        for m,lv,rv,o in vals:
            if not o: print(f"        m={m}: {lv} != {rv}")

print()
print("=== NEW CANDIDATES (forced across m=2,3,4,5 ?) ===")
forced=[]; notforced=[]
for name,(l,r) in candidates.items():
    ok,vals = holds(name,l,r)
    print(f"  [{'FORCED' if ok else 'not-forced'}] {name}")
    if ok: forced.append(name)
    else:
        notforced.append(name)
        # show the first m where it breaks, for honesty
        for m,lv,rv,o in vals:
            if not o:
                print(f"        breaks at m={m}: {lv} != {rv}"); break

print()
print(f"FORCED (hold as identities in m): {len(forced)}")
for f_ in forced: print("   ", f_)
print(f"NOT-FORCED: {len(notforced)}")

print()
print("=== INDEPENDENCE TEST: is each forced candidate just a rearrangement of registered results? ===")
print("Registered facts the U-line/D11b/N1 already fix, as forms in m:")
print("  g* = charged = (m-1)/m   [PH5]")
print("  neutral = 1/m            [D11b]   mixing = 1/(m-1)  [D11b]")
print("  colour = m               [D7b]    mediators = m^2-1 [N1]")
print("  U4: g*=charged   U5: g*=(colour-1)/colour   U6: mixing*charged=neutral")
print()
# A candidate is NON-INDEPENDENT if it is a pure algebraic consequence of the six forms above.
# Since all six are fixed functions of m, EVERY true relation among them is such a consequence.
# So the honest statement is: independence cannot come from algebra (all are functions of one m);
# it can only come from whether the relation ties observables the standard account leaves free.
# Report that structural fact, do not manufacture independence.
note = """
READING (reported, not adjudicated):
- All quantities are fixed functions of the single fold factor m. Therefore every algebraic
  identity among them holds automatically once the forms are fixed; holding-across-m is necessary
  but does NOT make a relation an independent result.
- Of the 13 forced identities, 12 are rearrangements of already-registered results
  (N1: C-a,C-c; D11b channel partition: C-e,C-f,C-k; U5: C-i,C-m; U6: C-g,C-h; D11b forms: C-j; trivial product: C-b).
- 1 is an algebraically non-obvious factorization: C-d  mixing * mediators = m+1,
  i.e. (m^2-1)/(m-1) = m+1 -- ties the mediator count and the mixing to the integer m+1.
  Whether C-d is a DISTINCT observable-relationship worth registering, or merely the factorization
  of m^2-1, is the author's/assessors' call (GUIDANCE 9.1). The engine forces it; that is the reading.
"""
print(note)
