"""D6 — quantum structure beyond the oscillator, in the permitted language. At depth k the state
space has N = 2^k position-branches (R1), uniformly spaced (R4). The fold is the bit shift (R2),
so the fold's bit functions are the Walsh/Rademacher generators: the conjugate (frequency) basis
of the branch basis is the Walsh basis. Position-support s_t = count of occupied branches;
frequency-support s_f = count of occupied Walsh modes. The complementarity bound is a count
inequality:  s_t * s_f  >=  N = 2^k. The most localized state -- occupancy on one branch (s_t=1)
-- has frequency-support s_f = N (the full Walsh comb), so its product equals N (the bound is
attained). Measurement resolves occupancy to one branch: s_t -> 1 forces s_f >= N (maximal
frequency spread). The Walsh transform itself carries signs and is computed outside the corpus;
the framework's claim is the integer inequality on the supports."""
from fractions import Fraction
from ratio import ONE, ratio

def dimension(k):
    n=ONE
    for _ in range(k): n=n+n        # 2^k by doubling (the fold's branch count, R1)
    return n

def support_product(s_t, s_f):
    return s_t*s_f                  # count of occupied branches times count of occupied modes

def satisfies_uncertainty(s_t, s_f, k):
    return support_product(s_t, s_f) >= dimension(k)     # s_t * s_f >= 2^k

def measurement_forces_frequency_support(k):
    # occupancy resolved to one branch (s_t=1): the bound forces s_f >= 2^k
    return dimension(k)

def min_uncertainty_product(k):
    # the single-branch state: s_t=1, s_f=2^k, product = 2^k (bound attained)
    return dimension(k)

if __name__=="__main__":
    for k in (1,2,3,4):
        N=dimension(k)
        print(f"depth k={k}: N=2^k={N}; bound s_t*s_f>={N}; single branch s_t=1 forces s_f>={N} (product={support_product(ONE,N)})")
    print("complementarity: localising position (s_t small) forces frequency spread (s_f large), product >= N")


# --- D6b: variance form of the uncertainty bound ---
# The support bound s_t*s_f >= N=2^k (above) is the count form. The variance form weights each by
# the spacings of its basis. Position branches are uniformly spaced at a (R4); the conjugate Walsh
# modes are spaced at 1/(N a) over the period. A spread occupying s branches has a position spread
# of order (s * a); a frequency-support s_f has a frequency spread of order s_f /(N a). The product
# of the spreads is (s_t * a) * (s_f /(N a)) = (s_t * s_f)/N >= 1: the spacings a cancel, so the
# variance-form bound is unit-free and equals the count bound divided by N -- bounded below by ONE,
# independent of the lattice spacing. Built in positive magnitudes (spreads, products, ratio).

def position_spread(s_t, a):
    return s_t * a                          # spread of an s_t-branch occupancy at spacing a

def frequency_spread(s_f, a, k):
    return ratio(s_f, dimension(k) * a)     # spread in the conjugate Walsh basis (spacing 1/(N a))

def spread_product(s_t, s_f, a, k):
    # (s_t a)(s_f/(N a)) = (s_t s_f)/N : the spacing a cancels, unit-free
    return ratio(position_spread(s_t, a) * frequency_spread(s_f, a, k), ONE)

def variance_bound_holds(s_t, s_f, a, k):
    # the spread product is >= ONE exactly when the count product s_t*s_f >= N
    return spread_product(s_t, s_f, a, k) >= ONE

if __name__=="__main__":
    print("--- D6b: variance form (spacing-independent) ---")
    for k in (1,2,3):
        N=dimension(k)
        for a in (Fraction(1,1), Fraction(1,7), Fraction(5,3)):
            sp=spread_product(ONE, N, a, k)        # single branch: s_t=1, s_f=N
            print(f"  k={k} a={a}: single-branch spread product = {sp} (== ONE, bound attained, a cancels)")
        print(f"  k={k}: holds for s_t=1,s_f=N:", variance_bound_holds(ONE,N,Fraction(2,9),k),
              "| violated for s_t=1,s_f=1:", not variance_bound_holds(ONE,ONE,Fraction(2,9),k))
