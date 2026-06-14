"""Rung 2.5 scale test: spectrum + reconstruction of the full KQKR field (2^25).
Run as a file (multiprocessing spawn requires an importable __main__)."""
import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace, concentration
from fold_solve4 import solve4
from fold_chess4 import NSTATES4

Z = 1 - 1
U, D, W, L = Z, 1, 2, 3

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]
    g = [Z] * NSTATES4
    legal4 = []
    for i in range(NSTATES4):
        k = K4[i]
        if k == W:
            g[i] = 1
            legal4.append(i)
        elif k == L:
            g[i] = Z - 1
            legal4.append(i)
        elif k == D:
            legal4.append(i)
    spec4 = wht_inplace(g[:])
    ks = [32, 256, 2048, 16384]
    c = concentration(spec4, ks)
    print("KQKR SPECTRUM:", {k: round(c[k], 4) for k in ks})
    order4 = sorted(range(NSTATES4), key=lambda i: -abs(spec4[i]))
    for k in (32, 2048):
        trunc = [Z] * NSTATES4
        for i in order4[:k]:
            trunc[i] = spec4[i]
        recon = wht_inplace(trunc)
        right = Z
        for i in legal4:
            r = recon[i] * 2
            pred = 1 if r > NSTATES4 else (Z - 1 if r < -NSTATES4 else Z)
            truth = 1 if K4[i] == W else (Z - 1 if K4[i] == L else Z)
            if pred == truth:
                right += 1
        print("KQKR RECON top-%d: %d/%d = %.2f%%" % (k, right, len(legal4), 100 * right / len(legal4)))
    print("SCALE TEST COMPLETE")
