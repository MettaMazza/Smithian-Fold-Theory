"""Corrected scaling: peeling recovery (query cost tracks coefficient count)
across KQK -> KQKR -> KQKRR, re-extrapolated to 10 pieces."""
import sys, os, time, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_sublinear_peel import recover_peel
from fold_sublinear import reconstruct_score, auc

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = 0.90
ROUNDS = 5


def sweep(name, p, n, sgn, legal, b_list):
    NST = 1 << n
    queried = np.zeros(NST, dtype=bool)

    def qb(idx):
        ii = idx.astype(np.int64)
        queried[ii] = True
        return sgn[ii].astype(np.float64)

    rs = random.Random(7)
    samp = []
    while len(samp) < min(40000, legal // 4):
        i = rs.randrange(NST)
        if sgn[i] != 0:
            samp.append(i)
    samp = np.array(samp, dtype=np.int64)
    lab = np.where(sgn[samp] > 0, 1, -1)
    hit = None
    for b in b_list:
        queried[:] = False
        rng = random.Random(1234 + b)
        cols = lambda r: [rng.randrange(1, NST) for _ in range(b)]
        found = recover_peel(qb, n, b, ROUNDS, cols)
        nq = int(queried.sum())
        keep = ~queried[samp]
        a = auc(reconstruct_score(found, samp[keep]), lab[keep])
        frac = 100.0 * nq / legal
        print("  %-6s p=%d n=%d b=%-3d coeffs=%-8d q=%-10d %%legal=%9.4f AUC=%.4f"
              % (name, p, n, b, len(found), nq, frac, a), flush=True)
        if a >= TARGET and hit is None:
            hit = (p, n, b, nq, frac, a)
    return hit


if __name__ == "__main__":
    t0 = time.time()
    pts = []
    from fold_chess import solve
    code = {"W": 1, "L": -1}
    r3 = solve(piece="Q", console=False)
    sgn3 = np.array([code.get(k, 0) for k in r3["kind"]], dtype=np.int8)
    legal3 = sum(1 for k in r3["kind"] if k in ("W", "L", "D"))
    print("KQK built %.0fs" % (time.time() - t0), flush=True)
    h = sweep("KQK", 3, 19, sgn3, legal3, [6, 8, 10, 12]);  pts += [h] if h else []

    from fold_solve4 import solve4
    k4 = np.frombuffer(bytes(solve4(console=False)["kind"]), dtype=np.uint8)
    sgn4 = np.where(k4 == 2, 1, np.where(k4 == 3, -1, 0)).astype(np.int8)
    legal4 = int((k4 != 0).sum())
    print("KQKR built %.0fs" % (time.time() - t0), flush=True)
    h = sweep("KQKR", 4, 25, sgn4, legal4, [10, 12, 14, 16]); pts += [h] if h else []

    k5 = np.memmap(os.path.join(HERE, "kqkrr_kind.bin"), dtype=np.uint8, mode="r")
    sgn5 = np.where(k5 == 2, 1, np.where(k5 == 3, -1, 0)).astype(np.int8)
    print("KQKRR mapped %.0fs" % (time.time() - t0), flush=True)
    h = sweep("KQKRR", 5, 31, sgn5, 1054075064, [13, 15, 16, 17, 18]); pts += [h] if h else []

    print("\nPEEL B-FOR-AUC>=%.2f:" % TARGET, flush=True)
    for p, n, b, nq, frac, a in pts:
        print("  p=%d n=%d b=%d q=%d %%legal=%.5f AUC=%.4f" % (p, n, b, nq, frac, a), flush=True)
    if len(pts) >= 2:
        ps = np.array([x[0] for x in pts], float); bs = np.array([x[2] for x in pts], float)
        s, b0 = np.polyfit(ps, bs, 1)
        print("\nb(p) ~ %.3f*p + %.3f" % (s, b0), flush=True)
        for p10 in (6, 7, 8, 9, 10):
            n10 = 6 * p10 + 1; b10 = s * p10 + b0
            q10 = (n10 + 1) * (2 ** b10) * ROUNDS
            print("  PROJECT p=%d: n=%d b=%.1f q~%.3e %%legal~%.3e"
                  % (p10, n10, b10, q10, 100.0 * q10 / ((2 ** n10) * 0.49)), flush=True)
    print("PEEL SCALING DONE", flush=True)
