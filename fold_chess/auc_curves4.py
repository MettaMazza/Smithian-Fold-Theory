"""Scrutiny of the last standing negative: AUC-vs-budget curves.
Single-budget verdicts conflate concentration speed with judgment ceiling;
the curves adjudicate. Aligned vs the two best relational candidates,
four budgets each."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace
from fold_solve4 import solve4
from fold_chess4 import NSTATES4, decode4

def f_(s): return s % 8
def r_(s): return s // 8
def sq(f, r): return (r % 8) * 8 + (f % 8)

PACKINGS = [
    ("aligned", lambda wk,wq,br,bk: (wk,wq,br,bk)),
    ("rook rel own king", lambda wk,wq,br,bk: (wk, wq, sq(f_(br)-f_(bk), r_(br)-r_(bk)), bk)),
    ("bk,br rel wq", lambda wk,wq,br,bk: (wk, wq, sq(f_(br)-f_(wq), r_(br)-r_(wq)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq)))),
]
BUDGETS = [2046, 16441, 130862, 1048576]

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    for name, mp in PACKINGS:
        g = [0]*NSTATES4
        pos = {}
        legal = []; draws = []
        for i in range(NSTATES4):
            kk = K4[i]
            if kk == U: continue
            wk,wq,br,bk,stm = decode4(i)
            a,b,c,d = mp(wk,wq,br,bk)
            j = (((a*64+b)*64+c)*64+d)*2 + stm
            pos[i] = j; legal.append(i)
            if kk == D: g[j] = 1; draws.append(i)
            else: g[j] = -1
        spec = wht_inplace(g[:])
        order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
        dset = set(draws); nD = len(draws); nO = len(legal) - nD
        for kbud in BUDGETS:
            trunc = [0]*NSTATES4
            for i in order[:kbud]: trunc[i] = spec[i]
            recon = wht_inplace(trunc)
            ranked = sorted(legal, key=lambda i: -recon[pos[i]])
            ranksum = sum(p+1 for p, i in enumerate(ranked) if i in dset)
            auc = 1 - (ranksum - nD*(nD+1)/2)/(nD*nO)
            print(f"CURVE {name} k={kbud}: AUC={auc:.5f}")
    print("CURVES COMPLETE")
