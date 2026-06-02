# Settle C-d: is (mixing * mediator-count = m+1) DISTINCT from the registered set,
# by the same standard U4/U5/U6 were registered under -- does it tie observables the
# STANDARD ACCOUNT leaves independent? Mechanical, framework-first (16.1), no consensus as judge.
from fractions import Fraction as F

def mixing(m):    return F(1, m-1)     # D11b  electroweak mixing
def mediators(m): return F(m*m-1, 1)   # N1    mediator count
def colour(m):    return F(m, 1)       # D7b
def g_star(m):    return F(m-1, m)      # PH5
def neutral(m):   return F(1, m)        # D11b

print("=== what C-d states, framework-first ===")
for m in (2,3,4,5):
    print(f"  m={m}:  mixing({m}) * mediators({m}) = {mixing(m)} * {mediators(m)} = {mixing(m)*mediators(m)}   ; m+1 = {m+1}")
print()

print("=== is C-d entailed by an ALREADY-registered relationship? ===")
# N1 already registers mediators = m^2 - 1. mixing = 1/(m-1) is the D11b form.
# mixing * mediators = (m^2-1)/(m-1) = (m-1)(m+1)/(m-1) = m+1. This is pure factorization of N1's
# own value divided by the D11b mixing form -- no NEW tie; it is N1 expressed over the mixing.
# Compare: U6 (mixing*charged=neutral) ties THREE DISTINCT channel observables (mixing, charged,
# neutral) none of which is defined as a function the others trivially factor into.
print("  C-d  = mediators / (1/mixing) = (m^2-1)/(m-1) = m+1   -- this is N1's value factored by (m-1).")
print("  It re-expresses N1 (mediators=m^2-1) using the mixing form 1/(m-1); it introduces no observable")
print("  that N1 and D11b do not already fix. The integer m+1 is the cofactor of the factorization,")
print("  not a separately-forced observable.")
print()
print("  Contrast U6: mixing*charged=neutral ties three channel observables, none the factorization of another.")
print()
print("=== READING (reported, not adjudicated) ===")
print("  C-d is forced (holds across m) but is N1 re-expressed over the mixing form -- NOT a distinct")
print("  observable-relationship by the standard U4-U6 were registered under. Registering it would be")
print("  the inflation 5/9.5 forbids. Reported as: forced, and a restatement of N1. Not registered.")
