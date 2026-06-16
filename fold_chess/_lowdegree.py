"""Fold-native generativity test: is the chess value field LOW-DEGREE in the
fold's itinerary (Walsh) basis, and does the degree stay bounded as pieces grow?

Exact integer Walsh-Hadamard spectrum (values in {-1,0,+1} -> integer coeffs,
no floats in the transform). For each coefficient, its ORDER is the number of
interacting itinerary bits = popcount of its index. We report how much of the
total energy sits at each order. If the field is low-degree (energy in order<=d)
and d does not grow with pieces, the heavy coefficients number ~ C(n,d) ~ n^d
(polynomial), so they can be enumerated and solved for at any scale, generatively
— no sampling of the field. Fold's own basis; exact arithmetic; no fitting."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_theorems5 import fwht_inplace

HERE = os.path.dirname(os.path.abspath(__file__))


def energy_by_order(spec, n):
    """spec: int64 exact Walsh coefficients. Returns energy summed by popcount(index)."""
    eo = np.zeros(n + 1, dtype=np.float64)
    CH = 1 << 24
    N = spec.size
    for base in range(0, N, CH):
        end = min(base + CH, N)
        idx = np.arange(base, end, dtype=np.uint64)
        pc = np.zeros(end - base, dtype=np.int64)
        x = idx.copy()
        while x.any():
            pc += (x & np.uint64(1)).astype(np.int64)
            x >>= np.uint64(1)
        e = spec[base:end].astype(np.float64) ** 2
        eo += np.bincount(pc, weights=e, minlength=n + 1)[:n + 1]
    return eo


def report(name, p, n, sgn):
    t = time.time()
    f = sgn.astype(np.int64)            # exact integer field
    spec = fwht_inplace(f)              # exact integer Walsh spectrum
    eo = energy_by_order(spec, n)
    tot = eo.sum()
    cum = np.cumsum(eo) / tot
    # count of coefficients available up to each order: sum C(n,i)
    from math import comb
    print("\n%s  p=%d  n=%d   (energy by interaction-order)" % (name, p, n), flush=True)
    run = 0
    for d in range(0, min(n, 8) + 1):
        ncoef = sum(comb(n, i) for i in range(d + 1))
        print("   order<=%d : cum-energy=%.6f   candidate-coeffs=C(n,<=%d)=%d"
              % (d, cum[d], d, ncoef), flush=True)
        if cum[d] >= 0.999 and run == 0:
            run = d
    print("   >=99.9%% energy by order %d  | %.0fs" % (run, time.time() - t), flush=True)
    return run


if __name__ == "__main__":
    degs = {}
    from fold_chess import solve
    r3 = solve(piece="Q", console=False)
    code = {"W": 1, "L": -1}
    sgn3 = np.array([code.get(k, 0) for k in r3["kind"]], dtype=np.int8)
    degs[3] = report("KQK", 3, 19, sgn3)

    from fold_solve4 import solve4
    k4 = np.frombuffer(bytes(solve4(console=False)["kind"]), dtype=np.uint8)
    sgn4 = np.where(k4 == 2, 1, np.where(k4 == 3, -1, 0)).astype(np.int8)
    degs[4] = report("KQKR", 4, 25, sgn4)

    k5 = np.memmap(os.path.join(HERE, "kqkrr_kind.bin"), dtype=np.uint8, mode="r")
    sgn5 = np.where(k5 == 2, 1, np.where(k5 == 3, -1, 0)).astype(np.int8)
    degs[5] = report("KQKRR", 5, 31, sgn5)

    print("\nDEGREE for 99.9%% energy:  3pc=%d  4pc=%d  5pc=%d" % (degs[3], degs[4], degs[5]), flush=True)
    print("LOWDEGREE DONE", flush=True)
