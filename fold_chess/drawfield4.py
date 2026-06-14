"""Direct draw-field spectrum at KQKR — the corrected fortress experiment."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace, concentration
from fold_solve4 import solve4
from fold_chess4 import NSTATES4

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    f = [0]*NSTATES4
    draws = []
    legal = []
    for i in range(NSTATES4):
        k = K4[i]
        if k == U: continue
        legal.append(i)
        if k == D:
            f[i] = 1
            draws.append(i)
        else:
            f[i] = -1
    spec = wht_inplace(f[:])
    c = concentration(spec, [2046, 16441, 130862])
    print("DRAW-FIELD KQKR: conc", {k: round(v,4) for k,v in c.items()})
    order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
    dset = set(draws)
    for k in (2046, 16441, 130862):
        trunc = [0]*NSTATES4
        for i in order[:k]: trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        ranked = sorted(legal, key=lambda i: -recon[i])[:len(draws)]
        hit = len(set(ranked) & dset)
        print(f"  top-{k}: fortress recall@|D| = {hit}/{len(draws)} = {100*hit/len(draws):.1f}%  (hitchhiker design scored: 25.8/62.0/86.0)")
    print("DRAWFIELD4 COMPLETE")
