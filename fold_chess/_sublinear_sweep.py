"""Sublinear recovery on the solved KQKRR field — done properly.
Multiple seeds (reproducibility), fixed withheld eval set, null baseline,
both denominators. Prints raw numbers only."""
import sys, os, time, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_sublinear import recover, reconstruct_score, auc
from fold_chess5 import NSTATES5

HERE = os.path.dirname(os.path.abspath(__file__))
KIND = np.memmap(os.path.join(HERE, "kqkrr_kind.bin"), dtype=np.uint8, mode="r")
U, D, W, L = 0, 1, 2, 3
N = 31
LEGAL = 1054075064
queried = np.zeros(NSTATES5, dtype=bool)


def query_batch(idx_arr):
    ii = idx_arr.astype(np.int64)
    queried[ii] = True
    k = KIND[ii]
    return np.where(k == W, 1.0, np.where(k == L, -1.0, 0.0))


def build_eval(n_eval, seed):
    rs = random.Random(seed)
    samp = []
    while len(samp) < n_eval:
        idx = rs.randrange(NSTATES5)
        k = KIND[idx]
        if k == W or k == L:
            samp.append(idx)
    samp = np.array(samp, dtype=np.int64)
    lab = np.where(KIND[samp] == W, 1, -1)
    return samp, lab


if __name__ == "__main__":
    t0 = time.time()
    EVAL, LAB = build_eval(120000, seed=99)
    print("fixed eval set: %d decided (W=%d L=%d)"
          % (EVAL.size, int((LAB == 1).sum()), int((LAB == -1).sum())), flush=True)

    # null baseline: random scores
    rng0 = np.random.default_rng(0)
    print("NULL  random-score AUC = %.5f" % auc(rng0.standard_normal(EVAL.size), LAB), flush=True)
    print("%-6s %-5s %-6s %10s %9s %9s %9s" %
          ("b", "rnds", "seed", "coeffs", "%cube", "%legal", "AUC"), flush=True)

    runs = [(16, 4, 11), (16, 4, 22), (18, 4, 11), (18, 4, 22), (20, 3, 11)]
    for b, rounds, seed in runs:
        queried[:] = False
        rng = random.Random(seed)
        cols = lambda r: [rng.randrange(1, 1 << N) for _ in range(b)]
        topk = max(8000, (1 << b) // 8)
        found = recover(query_batch, N, b, rounds, topk, cols)
        nq = int(queried.sum())
        keep = ~queried[EVAL]                         # exclude any eval pos that got queried
        ev, lb = EVAL[keep], LAB[keep]
        a = auc(reconstruct_score(found, ev), lb)
        print("%-6d %-5d %-6d %10d %9.4f %9.4f %9.5f  (%.0fs)" %
              (b, rounds, seed, len(found), 100.0 * nq / NSTATES5,
               100.0 * nq / LEGAL, a, time.time() - t0), flush=True)
    print("SWEEP DONE", flush=True)
