"""Owed retests: (A) deterministic battery at KQKR (2^25) — lawful mixers
plus theorem-forced bit-reversal self-test, validating the fold-intrinsic
claim AT THE SCALE IT WAS EXTENDED TO; (B) true paired McNemar for
candidate-1 vs aligned on decided positions."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_spectrum import wht_inplace, concentration
from fold_solve4 import solve4
from fold_chess4 import NSTATES4, decode4

def f_(s): return s % 8
def r_(s): return s // 8
def sq(f, r): return (r % 8) * 8 + (f % 8)
B = 25

def bitrev(i):
    r = 0
    for _ in range(B):
        r = (r << 1) | (i & 1); i >>= 1
    return r

if __name__ == "__main__":
    r4 = solve4(console=False)
    K4 = r4["kind"]; U,D,W,L = 0,1,2,3
    f = [0]*NSTATES4
    for i in range(NSTATES4):
        if K4[i] == W: f[i] = 1
        elif K4[i] == L: f[i] = -1

    print("(A) DETERMINISTIC BATTERY AT KQKR (2^25):")
    MAPS = [("aligned", lambda i: i),
            ("bit-reversal SELF-TEST (theorem: exact equality)", bitrev),
            ("tripling x3", lambda i: (3*i) % NSTATES4),
            ("affine 3i+1", lambda i: (3*i+1) % NSTATES4)]
    for name, sg in MAPS:
        g = [0]*NSTATES4
        for i in range(NSTATES4):
            v = f[i]
            if v: g[sg(i)] = v
        c = concentration(wht_inplace(g), [2046, 130862])
        print("  %-46s top2046=%.4f top130862=%.4f" % (name, c[2046], c[130862]))

    print("(B) TRUE PAIRED McNEMAR — candidate-1 vs aligned, decided positions:")
    def predict(mp):
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
        order = sorted(range(NSTATES4), key=lambda i: -abs(spec[i]))
        trunc = [0]*NSTATES4
        for i in order[:2046]: trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        return pos, recon
    posA, reconA = predict(lambda wk,wq,br,bk: (wk,wq,br,bk))
    posB, reconB = predict(lambda wk,wq,br,bk: (wk, wq,
        sq(f_(br)-f_(wq), r_(br)-r_(wq)), sq(f_(bk)-f_(wq), r_(bk)-r_(wq))))
    a_only = b_only = 0
    for i in posA:
        k = K4[i]
        if k == D: continue
        truth = 1 if k == W else -1
        okA = (reconA[posA[i]] > 0) == (truth > 0)
        okB = (reconB[posB[i]] > 0) == (truth > 0)
        if okA and not okB: a_only += 1
        elif okB and not okA: b_only += 1
    print("  aligned-only correct: %d | candidate-only correct: %d" % (a_only, b_only))
    diff = b_only - a_only
    import math as _m  # noqa: stdlib arithmetic for the z-score only
    z = diff / max((a_only + b_only) ** 0.5, 1)
    print("  McNemar z = %.1f (|z|>3 decisive; positive favors candidate-1)" % z)
    print("OWED RETESTS COMPLETE")
