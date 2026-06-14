"""Draw/fortress detection by the spectral oracle — pre-registered rule:
predict D iff |recon| < tau, tau = half the median |recon| over legal states
(formula-fixed, scale-adaptive, untuned). Report recall/precision on the
draw class at matched budgets; trivial baseline = never-predict-draw."""
import sys, os, statistics
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace
from fold_chess import solve, NSTATES
from fold_solve4 import solve4
from fold_chess4 import NSTATES4

def report(tag, field, legal, isW, isL, isD, N, fracs):
    spec = wht_inplace(field[:])
    order = sorted(range(N), key=lambda i: -abs(spec[i]))
    nd = sum(1 for i in legal if isD(i))
    print(f"{tag}: legal={len(legal)} draws={nd} ({100*nd/len(legal):.2f}%) | never-predict-draw recall=0%")
    for fr in fracs:
        k = max(1, int(N * fr))
        trunc = [0] * N
        for i in order[:k]:
            trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        mags = sorted(abs(recon[i]) for i in legal)
        tau = mags[len(mags)//2] / 2
        tp = fp = fn = corr = 0
        for i in legal:
            predD = abs(recon[i]) < tau
            trueD = isD(i)
            if predD and trueD: tp += 1
            elif predD: fp += 1
            elif trueD: fn += 1
            if predD == trueD and (trueD or (recon[i] > 0) == isW(i)):
                corr += 1
        rec = 100*tp/max(tp+fn,1); prec = 100*tp/max(tp+fp,1)
        print(f"  frac={fr:.1e} (k={k}): draw recall={rec:.1f}% precision={prec:.1f}% | 3-class acc={100*corr/len(legal):.2f}%")

FRACS = [6.1e-5, 4.9e-4, 3.9e-3]

if __name__ == "__main__":
    for piece in ("Q", "R"):
        res = solve(piece=piece, console=False)
        kk = res["kind"]
        legal = [i for i in range(NSTATES) if kk[i] != "U"]
        f = [0]*NSTATES
        for i in legal:
            if kk[i] == "W": f[i] = 1
            elif kk[i] == "L": f[i] = -1
        report(f"K{piece}K", f, legal,
               lambda i, kk=kk: kk[i]=="W", lambda i, kk=kk: kk[i]=="L",
               lambda i, kk=kk: kk[i]=="D", NSTATES, FRACS)
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    legal4 = [i for i in range(NSTATES4) if K4[i] != U]
    g = [0]*NSTATES4
    for i in legal4:
        if K4[i] == W: g[i] = 1
        elif K4[i] == L: g[i] = -1
    report("KQKR", g, legal4,
           lambda i: K4[i]==W, lambda i: K4[i]==L, lambda i: K4[i]==D,
           NSTATES4, FRACS)
    print("DRAW DETECTION COMPLETE")
