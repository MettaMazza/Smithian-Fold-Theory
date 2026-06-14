"""Fair growth retest: does the APPROXIMATE sparse object's generalization
degrade as material grows? Same fragment protocol that scored 0.998 at 4pc
(5% chi-key train -> withheld W/L AUC, top-k sparse), run across material at
MATCHED sparse FRACTION: KQK/KRK (3pc, cube 2^19) vs KQKR (4pc, cube 2^25).

This replaces the discredited 'lossless-fraction-of-raw' growth metric with
the right object (approximate) and the fair metric (withheld ranking AUC).
"""
import sys
sys.path.insert(0, "/Users/mettamazza/Desktop/SFTOM")
sys.path.insert(0, "/Users/mettamazza/Desktop/SFTOM/fold_chess")
from fold_spectrum import wht_inplace
from fold_chess import solve, NSTATES, find_fold_prime
from fold_solve4 import solve4
from fold_chess4 import NSTATES4

FRACS = (6.1e-5, 3.9e-3)   # matches the two 4pc operating points, fraction-wise


def frag_auc(N, truth, legal, P, label):
    e = (P - 1) // 2

    def chi(x):
        v = x % P
        if v == 0:
            v = 1
        return 1 if pow(v, e, P) == 1 else 0

    keys = {}
    for i in legal:
        k = 0
        for s in range(20):
            k = (k << 1) | chi(i + 1 + s * 5003)
        keys[i] = k
    order = sorted(legal, key=lambda i: keys[i])
    samp = set(order[:int(0.05 * len(legal))])
    wh = [i for i in legal if i not in samp]
    g = [0] * N
    for i in samp:
        g[i] = truth[i]
    spec = wht_inplace(g)
    o = sorted(range(N), key=lambda i: -abs(spec[i]))
    dec = [i for i in wh if truth[i] != 0]
    nW = sum(1 for i in dec if truth[i] == 1)
    nL = len(dec) - nW
    for fr in FRACS:
        kb = max(1, int(N * fr))
        tr = [0] * N
        for i in o[:kb]:
            tr[i] = spec[i]
        rec = wht_inplace(tr)
        ranked = sorted(dec, key=lambda i: rec[i])
        rs = sum(p + 1 for p, i in enumerate(ranked) if truth[i] == 1)
        auc = (rs - nW * (nW + 1) / 2) / (nW * nL)
        print("GROWTH-FAIR %s N=%d frac=%.2e k=%d: withheld W/L AUC=%.5f (n_wh=%d dec=%d)"
              % (label, N, fr, kb, auc, len(wh), len(dec)), flush=True)


if __name__ == "__main__":
    P3 = find_fold_prime(NSTATES)
    P4 = find_fold_prime(NSTATES4)

    for piece, lab in (("Q", "KQK-3pc"), ("R", "KRK-3pc")):
        res = solve(piece=piece, console=False)
        kind = res["kind"]
        truth = [0] * NSTATES
        legal = []
        for i in range(NSTATES):
            k = kind[i]
            if k == "W":
                truth[i] = 1
                legal.append(i)
            elif k == "L":
                truth[i] = -1
                legal.append(i)
            elif k == "D":
                legal.append(i)
        frag_auc(NSTATES, truth, legal, P3, lab)

    r4 = solve4(console=False)
    K = r4["kind"]
    U, D, W, L = 0, 1, 2, 3
    truth4 = [0] * NSTATES4
    legal4 = []
    for i in range(NSTATES4):
        k = K[i]
        if k == U:
            continue
        legal4.append(i)
        truth4[i] = 1 if k == W else (-1 if k == L else 0)
    frag_auc(NSTATES4, truth4, legal4, P4, "KQKR-4pc")
    print("GROWTH-FAIR COMPLETE", flush=True)
