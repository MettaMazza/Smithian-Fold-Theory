"""Query-access sparse recovery — the beyond-the-cube tool.

Finds large fold-spectrum coefficients WITHOUT holding the index space.
Correct KM-style identity: for masks m whose low w bits equal p,
  sum of c_m^2  =  E[ f(xh|xl) * f(xh|xl') * (-1)^popcount(p & (xl^xl')) ]
over samples sharing high bits xh and varying low bits xl, xl'.
Heavy prefixes split, light ones prune. Memory O(samples), independent of
space size. Deterministic sampling (no PRNG). Graded against full-cube
truth at KQK before larger use.
"""
import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import solve, NSTATES
from fold_spectrum import wht_inplace

Z = 1 - 1
B = 19
from fold_chess import find_fold_prime
_P = find_fold_prime(NSTATES)
_e = (_P - 1) // 2


def _chi_key(x, shifts):
    """Weil-flat multi-bit key from quadratic characters at disjoint shifts:
    flat AND near-independent across disjoint shift families."""
    k = Z
    for s in shifts:
        v = (x + s) % _P
        if v == Z:
            v = 1
        k = (k << 1) | (1 if pow(v, _e, _P) == 1 else Z)
    return k


SH_H = [101 + 7 * j for j in range(20)]      # high-part stream
SH_L = [4001 + 11 * j for j in range(20)]    # low stream
SH_L2 = [9001 + 13 * j for j in range(20)]   # low-prime stream


def recover(query, n_samples, tau_energy, tau_coeff, max_found=64):
    cache = {}
    def q(x):
        if x not in cache:
            cache[x] = query(x)
        return cache[x]

    def subtree_energy(w, p):
        lowmask = (1 << w) - 1
        tot = Z
        for k in range(n_samples):
            xh = _chi_key(3 * k + 1, SH_H) % (NSTATES >> w)
            xl = _chi_key(3 * k + 1, SH_L) & lowmask
            xl2 = _chi_key(3 * k + 1, SH_L2) & lowmask
            x = (xh << w) | xl
            y = (xh << w) | xl2
            par = bin(p & (xl ^ xl2)).count("1") % 2
            s = q(x) * q(y)
            tot += s if par == Z else -s
        return tot / n_samples

    def coeff_est(m, leaf_mult=16):
        tot = Z
        for k in range(n_samples * leaf_mult):
            x = _chi_key(5 * k + 2, SH_H + SH_L[:5]) % NSTATES
            par = bin(x & m).count("1") % 2
            v = q(x)
            tot += v if par == Z else -v
        return tot / n_samples

    import heapq
    e0 = subtree_energy(1, Z)
    e1 = subtree_energy(1, 1)
    print("  diag level-1 energies: p=0 -> %.4f | p=1 -> %.4f" % (e0, e1))
    frontier = [((Z - 1) * e0, 1, Z), ((Z - 1) * e1, 1, 1)]
    heapq.heapify(frontier)
    found = []
    expansions = Z
    while frontier and expansions < 6000:
        negE, w, p = heapq.heappop(frontier)
        if w == B:
            c = coeff_est(p)
            if abs(c) >= tau_coeff:
                found.append((p, c))
            continue
        expansions += 1
        for child in (p, p | (1 << w)):
            en = subtree_energy(w + 1, child) if w + 1 < B else tau_energy + abs(coeff_est(child))
            if en >= tau_energy:
                heapq.heappush(frontier, ((Z - 1) * en, w + 1, child))
    print("  diag expansions: %d | leaves kept: %d" % (expansions, len(found)))
    found.sort(key=lambda t: -abs(t[1]))
    return found[:max_found]


if __name__ == "__main__":
    res = solve(piece="Q", console=False)
    kind = res["kind"]
    f = [Z] * NSTATES
    for i in range(NSTATES):
        if kind[i] == "W":
            f[i] = 1
        elif kind[i] == "L":
            f[i] = Z - 1
    seen = set()
    nq = [Z]
    def query(i):
        if i not in seen:
            seen.add(i)
            nq[Z] += 1
        return f[i]

    spec = wht_inplace(f[:])
    order = sorted(range(NSTATES), key=lambda i: -abs(spec[i]))
    truth32 = set(order[:32])

    found = recover(query, n_samples=8192, tau_energy=0.002, tau_coeff=0.04)
    got32 = set(m for m, c in found[:32])
    print("QUERY-ACCESS RECOVERY vs full-cube truth (KQK):")
    print("  distinct positions queried: %d (%.2f%% of cube)" % (nq[Z], 100 * nq[Z] / NSTATES))
    print("  recovered: %d masks | overlap with true top-32: %d/32"
          % (len(found), len(got32 & truth32)))
    print("QUERY RECOVERY GRADE COMPLETE")
