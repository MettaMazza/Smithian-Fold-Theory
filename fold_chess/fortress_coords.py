"""Fortress-native coordinates on the DIRECT draw-field instrument at KQKR.
The audit-flagged untested hypothesis: a fortress is a DEFENDER structure,
so encode the rook relative to its own king. Numbers to beat (aligned
direct instrument): recall@|D| 54.4 / 77.2 / 93.3 at the matched budgets."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace, concentration
from fold_solve4 import solve4
from fold_chess4 import NSTATES4, decode4

def f_(s): return s % 8
def r_(s): return s // 8
def sq(f, r): return (r % 8) * 8 + (f % 8)

PACKINGS = [
    ("aligned (reference)", lambda wk,wq,br,bk: (wk,wq,br,bk)),
    ("rook rel own king (defender huddle)", lambda wk,wq,br,bk:
        (wk, wq, sq(f_(br)-f_(bk), r_(br)-r_(bk)), bk)),
    ("defender pair rel queen, rook rel bk", lambda wk,wq,br,bk:
        (wk, wq, sq(f_(br)-f_(bk), r_(br)-r_(bk)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq)))),
]

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    print("FORTRESS COORDS — direct draw-field, KQKR. Beat: 54.4/77.2/93.3")
    for name, mp in PACKINGS:
        g = [0]*NSTATES4
        pos = {}
        draws = []
        legal = []
        for i in range(NSTATES4):
            k = K4[i]
            if k == U: continue
            wk,wq,br,bk,stm = decode4(i)
            a,b,c,d = mp(wk,wq,br,bk)
            j = (((a*64+b)*64+c)*64+d)*2 + stm
            pos[i] = j
            legal.append(i)
            if k == D:
                g[j] = 1
                draws.append(i)
            else:
                g[j] = -1
        spec = wht_inplace(g[:])
        order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
        dset = set(draws)
        row = []
        for k in (2046, 16441, 130862):
            trunc = [0]*NSTATES4
            for i in order[:k]: trunc[i] = spec[i]
            recon = wht_inplace(trunc)
            ranked = sorted(legal, key=lambda i: -recon[pos[i]])[:len(draws)]
            row.append(100*len(set(ranked) & dset)/len(draws))
        print("  %-40s recall@|D| = %.1f / %.1f / %.1f" % (name, *row))
    print("FORTRESS COORDS COMPLETE")
