# Attempt GENUINELY cross-domain ties: connect gravity's forced dimension d=3 and the
# inverse-(d-1) exponent to the gauge-sector fold factor m. These come from DIFFERENT
# constructions (orbital stability / potential boundedness vs fold-factor algebra), so any
# relation between them is NOT automatic -- that is the test of independence.
from fractions import Fraction as F

d_forced   = 3                 # D9g: spatial dimension forced to three
exponent   = lambda d: d-1     # gravity field law inverse-(d-1)
m_em       = 2                 # B2: EM sector is the binary fold m=2
m_strong   = 3                 # strong sector tripling fold m=3
def colour(m):    return m
def mediators(m): return m*m-1
def g_star(m):    return F(m-1,m)

print("=== cross-domain candidates: do gravity's d and the gauge m coincide or relate by force? ===")
# Candidate G-a: the strong fold factor equals the forced spatial dimension (both 3)?
print(f"  G-a  strong fold factor m_strong = {m_strong} ; forced spatial dimension d = {d_forced}  -> equal? {m_strong==d_forced}")
print("        READING: numerically both are 3, BUT m_strong=3 is the colour-count identification (U7),")
print("        and d=3 is forced by orbital stability+potential boundedness (D9f/D9g). They are forced by")
print("        INDEPENDENT constructions. Coincidence of value is NOT a forced relationship between them")
print("        unless a single construction forces both. The engine does NOT derive d from m or m from d.")
print()
# Candidate G-b: is the gravity exponent (d-1) tied to the EM fold factor?
print(f"  G-b  gravity exponent (d-1) at d=3 = {exponent(3)} ; EM fold factor m_em = {m_em}  -> equal? {exponent(3)==m_em}")
print("        READING: both equal 2, again by independent constructions (geometry of a shell vs the binary")
print("        fold). No single construction forces the equality; it is a value-coincidence, not a forced tie.")
print()
print("=== HONEST CONCLUSION (reported, not adjudicated) ===")
print("  No GENUINELY independent cross-domain relationship is forced: the only cross-domain coincidences")
print("  (m_strong=3=d ; d-1=2=m_em) are equalities of VALUE between quantities forced by SEPARATE")
print("  constructions, not relationships a single construction forces. By the standard U4-U6 were")
print("  registered under (one construction forcing a tie among observables), these do NOT qualify.")
print("  To claim them would be to fit a coincidence into a relationship -- 5/9.5 forbids it.")
print("  The U-line is therefore complete at U1,U2,U4,U5,U6 (with U3 dictionary, U7 fibre-count):")
print("  no further INDEPENDENT forced cross-observable relationship is produced by composition.")
