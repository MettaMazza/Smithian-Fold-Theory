"""B2 — rational harmonics, in the permitted language. A part with odd denominator is
purely periodic under the fold; two such parts run together return to their joint start
after the least common multiple of their periods. Macro-pattern (a beat) from interlocking
exact cycles — no continuous curve, no pi. Periods are counts (scaffolding), not magnitudes."""
from fractions import Fraction
from ratio import fold

def period(p, cap=100000):
    cur=fold(p); n=1
    while cur != p:
        cur=fold(cur); n+=1
        if n>cap: return None
    return n

def combined_period(parts, cap=1000000):
    start=tuple(parts)
    cur=tuple(fold(x) for x in start); n=1
    while cur != start:
        cur=tuple(fold(x) for x in cur); n+=1
        if n>cap: return None
    return n

def gcd(a,b):
    while b: a,b=b, a%b
    return a
def lcm(a,b): return a*b//gcd(a,b)

if __name__=="__main__":
    print("single-part periods under the fold (odd denominator => purely periodic):")
    for p in (Fraction(1,3),Fraction(1,5),Fraction(1,7),Fraction(1,9),Fraction(1,11)):
        print(f"  {p}: period {period(p)}")
    print("\ntwo parts together: combined period vs lcm of the two periods:")
    for a,b in ((Fraction(1,3),Fraction(1,5)),(Fraction(1,7),Fraction(1,5)),(Fraction(1,7),Fraction(1,9))):
        pa,pb=period(a),period(b); cp=combined_period([a,b])
        print(f"  {a} (per {pa}) with {b} (per {pb}): combined {cp}, lcm {lcm(pa,pb)}, equal {cp==lcm(pa,pb)}")
