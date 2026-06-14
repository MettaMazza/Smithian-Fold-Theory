"""Fixes #2 and #4: per-packing fortress scores on the DIRECT draw-field
instrument (voiding the hitchhiker-based packing verdicts), plus
prevalence-free AUC at matched fractions for the 'complexity premium'."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace
from fold_solve4 import solve4
from fold_chess4 import NSTATES4, decode4
from fold_chess import solve, NSTATES

def f_(s): return s % 8
def r_(s): return s // 8
def sq(f, r): return (r % 8) * 8 + (f % 8)
def shear(s): return sq(f_(s), r_(s) + f_(s))

def auc_and_recall(recon_at, legal, draws, n):
    ranked = sorted(legal, key=lambda i: -recon_at(i))
    dset = set(draws)
    nD = len(draws); nO = len(legal) - nD
    ranksum = 0
    hit = 0
    for pos, i in enumerate(ranked):
        if i in dset:
            ranksum += pos + 1
            if pos < nD: hit += 1
    auc = 1 - (ranksum - nD*(nD+1)/2) / (nD*nO)
    return auc, hit/nD

if __name__ == "__main__":
    # 3-piece aligned AUC baselines (for #4)
    for piece in ("Q", "R"):
        res = solve(piece=piece, console=False)
        kind = res["kind"]
        legal = [i for i in range(NSTATES) if kind[i] != "U"]
        draws = [i for i in legal if kind[i] == "D"]
        f = [0]*NSTATES
        for i in legal: f[i] = 1 if kind[i] == "D" else -1
        spec = wht_inplace(f[:])
        order = sorted(range(NSTATES), key=lambda i: -abs(spec[i]))
        k = max(1, int(NSTATES*3.9e-3))
        trunc = [0]*NSTATES
        for i in order[:k]: trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        auc, rec = auc_and_recall(lambda i: recon[i], legal, draws, NSTATES)
        print(f"AUC K{piece}K aligned (frac 3.9e-3): AUC={auc:.4f} recall@|D|={100*rec:.1f}%")

    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    PACKINGS = [
        ("aligned", lambda wk,wq,br,bk: (wk,wq,br,bk)),
        ("bk rel wq, br rel wq", lambda wk,wq,br,bk: (wk, wq,
            sq(f_(br)-f_(wq), r_(br)-r_(wq)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq)))),
        ("rook rel own king", lambda wk,wq,br,bk: (wk, wq,
            sq(f_(br)-f_(bk), r_(br)-r_(bk)), bk)),
        ("shear + bk,br rel wq", lambda wk,wq,br,bk: (shear(wk), shear(wq),
            sq(f_(br)-f_(wq), r_(br)-r_(wq)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq)))),
    ]
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
            pos[i] = j
            legal.append(i)
            if kk == D:
                g[j] = 1; draws.append(i)
            else:
                g[j] = -1
        spec = wht_inplace(g[:])
        order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
        k = max(1, int(NSTATES4*3.9e-3))
        trunc = [0]*NSTATES4
        for i in order[:k]: trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        auc, rec = auc_and_recall(lambda i: recon[pos[i]], legal, draws, NSTATES4)
        print(f"KQKR DIRECT {name}: AUC={auc:.4f} recall@|D|={100*rec:.1f}%")
    print("REGRADE COMPLETE")
