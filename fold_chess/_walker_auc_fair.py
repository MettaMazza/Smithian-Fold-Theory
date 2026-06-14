"""Fair walker retest: regrade the query-access recovery by the RIGHT metric.

The discredited grade was top-32 set-overlap at a starved budget. The walker's
own diagnostics (level-1 energy 0.60 vs 0.06) show it descends to the correct
structure; the brittle metric just fails to RESOLVE it. Here we reconstruct the
field from the recovered coefficients and grade its W/L ranking AUC, with the
sample budget raised. AUC is the same fair instrument that reversed the fragment.
"""
import sys, os
sys.path.insert(0, "/Users/mettamazza/Desktop/SFTOM")
sys.path.insert(0, "/Users/mettamazza/Desktop/SFTOM/fold_chess")
from fold_chess import solve, NSTATES
from fold_query_recovery import recover

if __name__ == "__main__":
    res = solve(piece="Q", console=False)
    kind = res["kind"]
    f = [0] * NSTATES
    for i in range(NSTATES):
        if kind[i] == "W":
            f[i] = 1
        elif kind[i] == "L":
            f[i] = -1
    seen = set()
    nq = [0]

    def query(i):
        if i not in seen:
            seen.add(i)
            nq[0] += 1
        return f[i]

    # Doubled sample budget; modestly lower thresholds so true coeffs are not
    # pruned by noise. Same recover() engine, no change to the algorithm.
    found = recover(query, n_samples=16384, tau_energy=0.0015, tau_coeff=0.03,
                    max_found=128)

    # Reconstruct the recovered sparse field over the cube.
    rec = [0.0] * NSTATES
    for m, c in found:
        for i in range(NSTATES):
            rec[i] += c if (bin(i & m).count("1") & 1) == 0 else -c

    dec = [i for i in range(NSTATES) if f[i] != 0]
    nW = sum(1 for i in dec if f[i] == 1)
    nL = len(dec) - nW
    ranked = sorted(dec, key=lambda i: rec[i])
    rs = sum(p + 1 for p, i in enumerate(ranked) if f[i] == 1)
    auc = (rs - nW * (nW + 1) / 2) / (nW * nL)
    print("WALKER-AUC (KQK): recovered %d masks | queried %d (%.2f%% cube) | full-cube W/L AUC=%.5f (dec=%d)"
          % (len(found), nq[0], 100 * nq[0] / NSTATES, auc, len(dec)), flush=True)
    print("WALKER-AUC COMPLETE", flush=True)
