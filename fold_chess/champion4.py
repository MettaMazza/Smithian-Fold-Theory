"""Champion relational packings applied to KQKR: does the sweep's winner
restore/raise sparsity at 4 pieces, and does it see fortresses better?
Metrics per packing (checklist): matched-fraction concentration, decided
sign-accuracy (baseline: stm-only 83.68%), draw recall/precision at the top
budget (baseline: never-predict-draw = 0% recall)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace, concentration
from fold_solve4 import solve4
from fold_chess4 import NSTATES4, decode4

def f_(s): return s % 8
def r_(s): return s // 8
def sq(f, r): return (r % 8) * 8 + (f % 8)
def shear(s): return sq(f_(s), r_(s) + f_(s))

PACKINGS = [
    ("aligned (reference)", lambda wk,wq,br,bk: (wk,wq,br,bk)),
    ("bk rel wq, br rel wq", lambda wk,wq,br,bk: (wk, wq,
        sq(f_(br)-f_(wq), r_(br)-r_(wq)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq)))),
    ("chain relative", lambda wk,wq,br,bk: (wk,
        sq(f_(wq)-f_(wk), r_(wq)-r_(wk)), sq(f_(br)-f_(wq), r_(br)-r_(wq)),
        sq(f_(bk)-f_(br), r_(bk)-r_(br)))),
    ("shear + bk,br rel wq (3pc champion analogue)", lambda wk,wq,br,bk: (shear(wk), shear(wq),
        sq(f_(br)-f_(wq), r_(br)-r_(wq)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq)))),
]

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    print("KQKR CHAMPION TEST — baselines: decided stm-only 83.68%, draw recall 0%")
    for name, mp in PACKINGS:
        g = [0]*NSTATES4
        pos = {}
        for i in range(NSTATES4):
            k = K4[i]
            if k == U: continue
            wk,wq,br,bk,stm = decode4(i)
            a,b,c,d = mp(wk,wq,br,bk)
            j = (((a*64+b)*64+c)*64+d)*2 + stm
            pos[i] = j
            if k == W: g[j] = 1
            elif k == L: g[j] = -1
        spec = wht_inplace(g[:])
        conc = concentration(spec, [2046, 130862])
        order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
        # decided sign-acc at matched small fraction
        trunc = [0]*NSTATES4
        for i in order[:2046]: trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        rs = tot = 0
        for i, j in pos.items():
            if K4[i] == W: tot += 1; rs += recon[j] > 0
            elif K4[i] == L: tot += 1; rs += recon[j] < 0
        # draw metrics at top budget
        trunc2 = [0]*NSTATES4
        for i in order[:130862]: trunc2[i] = spec[i]
        recon2 = wht_inplace(trunc2)
        mags = sorted(abs(recon2[j]) for j in pos.values())
        tau = mags[len(mags)//2] / 2
        tp = fp = fn = 0
        for i, j in pos.items():
            predD = abs(recon2[j]) < tau
            trueD = K4[i] == D
            if predD and trueD: tp += 1
            elif predD: fp += 1
            elif trueD: fn += 1
        print("  %-44s conc2046=%.4f | decided=%.2f%% | drawR=%.1f%% drawP=%.1f%%"
              % (name, conc[2046], 100*rs/tot, 100*tp/max(tp+fn,1), 100*tp/max(tp+fp,1)))
    print("CHAMPION TEST COMPLETE")
