"""Scale-FAIR comparison: equal fractional budgets, threshold-free metric
(sign accuracy on W/L states only), 3-piece vs 4-piece."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace
from fold_chess import solve, NSTATES
from fold_solve4 import solve4
from fold_chess4 import NSTATES4

def signacc(field, kind_w, kind_l, N, fracs):
    spec = wht_inplace(field[:])
    order = sorted(range(N), key=lambda i: -abs(spec[i]))
    out = {}
    for fr in fracs:
        k = max(1, int(N * fr))
        trunc = [0] * N
        for i in order[:k]:
            trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        right = tot = 0
        for i in kind_w:
            tot += 1
            if recon[i] > 0: right += 1
        for i in kind_l:
            tot += 1
            if recon[i] < 0: right += 1
        out[fr] = (k, right, tot)
    return out

FRACS = [6.1e-5, 4.9e-4, 3.9e-3]

res = solve(piece="Q", console=False)
kk = res["kind"]
f = [0]*NSTATES
W3 = [i for i in range(NSTATES) if kk[i] == "W"]
L3 = [i for i in range(NSTATES) if kk[i] == "L"]
for i in W3: f[i] = 1
for i in L3: f[i] = -1
for fr, (k, r, t) in signacc(f, W3, L3, NSTATES, FRACS).items():
    print(f"KQK  frac={fr:.1e} (k={k}): sign-acc on W/L = {r}/{t} = {100*r/t:.2f}%")

r4 = solve4(console=False)
K4 = r4["kind"]
U,D,W,L = 0,1,2,3
g = [0]*NSTATES4
W4 = [i for i in range(NSTATES4) if K4[i] == W]
L4 = [i for i in range(NSTATES4) if K4[i] == L]
for i in W4: g[i] = 1
for i in L4: g[i] = -1
for fr, (k, r, t) in signacc(g, W4, L4, NSTATES4, FRACS).items():
    print(f"KQKR frac={fr:.1e} (k={k}): sign-acc on W/L = {r}/{t} = {100*r/t:.2f}%")
print("SCALE-FAIR COMPLETE")
