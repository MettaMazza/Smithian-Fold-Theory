"""KQKR fragment test (real file: multiprocessing-safe) + threshold-rescaled
noise retest + 4-piece certified-table growth point. The three owed runs."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace
from fold_solve4 import solve4
from fold_chess4 import NSTATES4
from fold_chess import solve, NSTATES, find_fold_prime

if __name__ == "__main__":
    # ---------- A. KQKR fragment (rho ~ 5% deterministic)
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    legal = [i for i in range(NSTATES4) if K4[i] != U]
    f = [0]*NSTATES4; truth = {}
    for i in legal:
        v = 1 if K4[i]==W else (-1 if K4[i]==L else 0)
        f[i] = v; truth[i] = v
    sel = lambda i: ((i*2654435761 + 17) % NSTATES4) < NSTATES4//20   # 5%
    g = [0]*NSTATES4
    ns = 0
    for i in legal:
        if sel(i): g[i] = f[i]; ns += 1
    spec = wht_inplace(g)
    order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
    trunc = [0]*NSTATES4
    for i in order[:2046]: trunc[i] = spec[i]
    recon = wht_inplace(trunc)
    scale = len(legal)/ns
    wh = [i for i in legal if not sel(i)]
    right = sum(1 for i in wh if ((recon[i]*2*scale > NSTATES4) and truth[i]==1) or ((recon[i]*2*scale < -NSTATES4) and truth[i]==-1) or ((abs(recon[i]*2*scale) <= NSTATES4) and truth[i]==0))
    print("KQKR FRAGMENT rho=5%%: withheld acc %.2f%% (full-data ceiling ~?)" % (100*right/len(wh)))

    # ---------- B. threshold-rescaled noise retest (KQK, eps=20%)
    res = solve(piece="Q", console=False)
    kind = res["kind"]
    leg3 = [i for i in range(NSTATES) if kind[i] != "U"]
    f3 = [0]*NSTATES; t3 = {}
    for i in leg3:
        v = 1 if kind[i]=="W" else (-1 if kind[i]=="L" else 0)
        f3[i] = v; t3[i] = v
    P = find_fold_prime(NSTATES); e=(P-1)//2
    flat = sorted(leg3, key=lambda i: ((i*40503+7) % NSTATES))
    eps = 0.20
    g3 = f3[:]
    for i in flat[:int(len(leg3)*eps)]:
        g3[i] = -g3[i] if g3[i] else 1
    spec3 = wht_inplace(g3)
    order3 = sorted(range(NSTATES), key=lambda i: -abs(spec3[i]))
    trunc3 = [0]*NSTATES
    for i in order3[:32]: trunc3[i] = spec3[i]
    recon3 = wht_inplace(trunc3)
    resc = 1.0/(1-2*eps)               # amplitude correction for sign-flips
    right3 = sum(1 for i in leg3 if ((recon3[i]*2*resc > NSTATES) and t3[i]==1) or ((recon3[i]*2*resc < -NSTATES) and t3[i]==-1) or ((abs(recon3[i]*2*resc) <= NSTATES) and t3[i]==0))
    print("NOISE eps=20%% RESCALED threshold: acc on clean truth %.2f%% (unscaled gave 46.92)" % (100*right3/len(leg3)))

    # ---------- C. growth-law point: KQKR certified table size
    spec4 = wht_inplace(f[:])
    order4 = sorted(range(NSTATES4), key=lambda i: -abs(spec4[i]))
    best = None
    for k in (512, 2048, 8192, 32768):
        trunc4 = [0]*NSTATES4
        for i in order4[:k]: trunc4[i] = spec4[i]
        rc = wht_inplace(trunc4)
        exc = sum(1 for i in legal if not (((rc[i]*2 > NSTATES4) and truth[i]==1) or ((rc[i]*2 < -NSTATES4) and truth[i]==-1) or ((abs(rc[i]*2) <= NSTATES4) and truth[i]==0)))
        size = k*7 + exc*4
        print("CERT KQKR k=%d: exceptions=%d size=%dB" % (k, exc, size))
        if best is None or size < best[0]: best = (size, k, exc)
    print("CERT KQKR BEST: %dB (k=%d, exc=%d) | raw=%dB | 3-piece points: 17688B/15936B" % (best[0], best[1], best[2], 2*len(legal)//8))
    print("OWED RUNS COMPLETE")
