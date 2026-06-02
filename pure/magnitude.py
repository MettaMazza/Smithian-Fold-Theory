"""Algebraic magnitudes, in the permitted language. A magnitude that is not a ratio of whole
numbers — the diagonal of the unit square, a lattice mode frequency — is the positive point
where two positive-magnitude polynomials balance. No negatives, no imaginaries, no zero-as-value:
a defining relation P(x) = Q(x) with P, Q positive-coefficient polynomials, isolated to the
unique balance point in a rational interval where the two sides swap order. This is the Eudoxan
treatment of incommensurable magnitudes (Euclid Book V), carried into computation.

A polynomial is written as (whole, terms): an optional positive constant `whole` (the part with no
factor of x) together with `terms`, a map {power: positive coefficient} over powers of at least one.
An absent part is simply not present — `whole` is None when there is no constant, `terms` is empty
when there is no variable part. No power is ever written as the exponent zero and no coefficient is
ever written as the value zero (no zero-as-value, §8). The constant whole c is (c, {}); the square
x^2 is (None, {2: ONE})."""
from fractions import Fraction
from ratio import ONE

def peval(poly, x):
    # poly is (whole, terms); sum the present parts, starting the running total from the first
    # present part (never seeded with zero, cf. count.py).
    whole, terms = poly
    parts = []
    if whole is not None:
        parts.append(whole)
    for pw, c in terms.items():
        parts.append(c * (x ** pw))
    acc = parts[0]
    for p in parts[1:]:
        acc = acc + p
    return acc

def order(P, Q, x):
    # which positive side is the greater at x: True if P(x) <= Q(x)
    return peval(P, x) <= peval(Q, x)

def certifies(P, Q, lo, hi):
    # the two positive sides swap order across [lo,hi] -> they balance at a point between
    return order(P, Q, lo) != order(P, Q, hi)

def refine(P, Q, lo, hi, steps):
    # bisection, keeping the half where the sides still swap order; intervals shrink to the
    # balance point. Positive midpoints throughout.
    for _ in range(steps):
        mid = (lo + hi) * Fraction(1, 2)
        if certifies(P, Q, lo, mid):
            hi = mid
        else:
            lo = mid
    return lo, hi

class Magnitude:
    """A positive algebraic magnitude: the balance point of P and Q isolated in [lo,hi].
    P and Q are polynomials (whole, terms) in the form described above."""
    def __init__(self, P, Q, lo, hi):
        assert certifies(P, Q, lo, hi), "interval does not isolate a balance point"
        self.P, self.Q, self.lo, self.hi = P, Q, lo, hi
    def tighten(self, steps):
        self.lo, self.hi = refine(self.P, self.Q, self.lo, self.hi, steps)
        return self
    def brackets(self):
        return self.lo, self.hi
    def above(self, r):       # is the magnitude above the rational r?
        self.tighten(40)
        return self.lo > r if self.lo > r or self.hi < r else certifies(self.P,self.Q,r,self.hi)

# the square-root relation x^2 = c, as positive polynomials: P = x^2 (None,{2:ONE}), Q = c (c,{})
def sqrt_relation(c):
    return ((None, {2: ONE}), (c, {}))

if __name__=="__main__":
    # the diagonal-of-the-unit-square magnitude: x*x = 2, i.e. balance x^2 (=P) with 2 (=Q)
    P, Q = sqrt_relation(Fraction(2))
    root2 = Magnitude(P, Q, Fraction(1), Fraction(2))
    lo,hi = root2.tighten(30).brackets()
    print(f"sqrt(2) isolated in [{float(lo):.6f}, {float(hi):.6f}]  (true {2**0.5:.6f})")
