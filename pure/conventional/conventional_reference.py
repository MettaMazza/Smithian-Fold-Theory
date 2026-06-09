import math
import itertools
from fractions import Fraction

def hadamard(n):
    if n == 1:
        return [[1]]
    h = hadamard(n // 2)
    out = []
    for row in h:
        out.append(row + row)
    for row in h:
        out.append(row + [-x for x in row])
    return out

def walsh_uncertainty(k):
    N = 2**k
    H = hadamard(N)
    supports = set()
    for bits in itertools.product([0, 1], repeat=N):
        if sum(bits) == 0:
            continue
        # Compute the signed Walsh/Hadamard transform: y = H * bits
        y = [sum(H[i][j] * bits[j] for j in range(N)) for i in range(N)]
        st = sum(bits)
        sf = sum(1 for val in y if val != 0)
        supports.add((Fraction(st), Fraction(sf)))
    single = (Fraction(1), Fraction(N))
    return sorted(list(supports)), single
