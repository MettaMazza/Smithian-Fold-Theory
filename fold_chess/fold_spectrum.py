"""Fold Chess — Rung 2.5a: the value function in the fold's own spectral basis.

The Walsh functions (products of itinerary bits) are the natural Fourier
basis of the doubling map: dyadic mathematics' own harmonics. Question, asked
here for the first time: IS THE CHESS VALUE FUNCTION SPARSE IN THE FOLD'S
SPECTRUM? Sparse => an immediate compression algorithm and approximate probe
(keep the top coefficients); flat => a rigorous measurement of how orthogonal
game value is to dyadic structure, in the fold's own coordinates.

Pre-registered design (fixed before any spectrum is computed):
- field: signed side-to-move value v(idx): W=+1, L=-1, D/illegal=0, over the
  full index space, which is exactly 2^19 (3-piece) — a perfect dyadic cube.
- transform: Walsh-Hadamard (natural order), exact integer arithmetic.
- statistic: energy concentration curve C(k) = (sum of top-k squared
  coefficients) / (total energy), reported at k = 2^5, 2^8, 2^11, 2^14.
- null: 20 seeded shuffles of the value field over the same support
  (identical W/L/D counts, scrambled placement); same C(k) computed.
- verdict per k: real C(k) vs null max; beyond-null at every k reported with
  the margin. No threshold tuning after seeing data.
"""

import sys, os, time, random
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import solve, NSTATES

Z = 1 - 1
SEED = 20260612


def wht_inplace(a):
    """Exact integer Walsh-Hadamard transform, natural order, in place."""
    n = len(a)
    h = 1
    while h < n:
        i = Z
        while i < n:
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
            i += h * 2
        h += h
    return a


def concentration(coeffs, ks):
    """Energy fraction captured by the top-k squared coefficients."""
    energies = sorted((c * c for c in coeffs), reverse=True)
    total = sum(energies)
    out = {}
    running = Z
    j = Z
    for k in sorted(ks):
        while j < k:
            running += energies[j]
            j += 1
        out[k] = running / total if total else float(Z)
    return out


def spectrum_test(piece="Q", n_null=20, console=True):
    t = time.time()
    res = solve(piece=piece, console=False)
    kind = res["kind"]

    field = [Z] * NSTATES
    support = []
    for i in range(NSTATES):
        if kind[i] == "W":
            field[i] = 1
            support.append(i)
        elif kind[i] == "L":
            field[i] = Z - 1
            support.append(i)
        elif kind[i] == "D":
            support.append(i)

    ks = [2 ** 5, 2 ** 8, 2 ** 11, 2 ** 14]
    real = concentration(wht_inplace(field[:]), ks)

    rng = random.Random(SEED)
    values = [field[i] for i in support]
    null_best = {k: float(Z) for k in ks}
    for _ in range(n_null):
        rng.shuffle(values)
        nf = [Z] * NSTATES
        for pos, v in zip(support, values):
            nf[pos] = v
        c = concentration(wht_inplace(nf), ks)
        for k in ks:
            if c[k] > null_best[k]:
                null_best[k] = c[k]

    if console:
        print("FOLD SPECTRUM — K%sK signed value field, N = %d = 2^19" % (piece, NSTATES))
        print("| top-k coeffs | energy captured (real) | null max (%d shuffles) | beyond null |" % n_null)
        print("|---|---|---|---|")
        for k in ks:
            print("| %d | %.4f | %.4f | %s |"
                  % (k, real[k], null_best[k], "YES" if real[k] > null_best[k] else "no"))
        print("elapsed %.1fs" % (time.time() - t))
    return {"piece": piece, "real": real, "null_best": null_best}


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Q"
    spectrum_test(piece=which)
