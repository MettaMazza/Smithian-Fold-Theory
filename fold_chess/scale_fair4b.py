"""KQKR scale-fair, threshold-free, with trivial-baseline disclosure."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace
from fold_solve4 import solve4
from fold_chess4 import NSTATES4

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]
    U, D, W, L = 0, 1, 2, 3
    g = [0] * NSTATES4
    W4, L4 = [], []
    for i in range(NSTATES4):
        if K4[i] == W:
            g[i] = 1; W4.append(i)
        elif K4[i] == L:
            g[i] = -1; L4.append(i)
    # trivial baseline: predict mover-wins iff white to move (stm bit = idx%2 == 0 means WTM)
    triv = sum(1 for i in W4 if i % 2 == 0) + sum(1 for i in L4 if i % 2 == 1)
    tot = len(W4) + len(L4)
    print(f"KQKR TRIVIAL BASELINE (stm-only): {triv}/{tot} = {100*triv/tot:.2f}%")
    spec = wht_inplace(g[:])
    order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
    for fr in [6.1e-5, 4.9e-4, 3.9e-3]:
        k = max(1, int(NSTATES4 * fr))
        trunc = [0] * NSTATES4
        for i in order[:k]:
            trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        right = sum(1 for i in W4 if recon[i] > 0) + sum(1 for i in L4 if recon[i] < 0)
        print(f"KQKR frac={fr:.1e} (k={k}): sign-acc on W/L = {right}/{tot} = {100*right/tot:.2f}%")
    print("FAIR4B COMPLETE")
