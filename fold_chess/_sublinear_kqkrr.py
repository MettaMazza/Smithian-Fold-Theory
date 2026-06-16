"""The real breakthrough test: sublinear aliasing recovery against the SOLVED
five-piece field (KQKRR, 2^31). Measures the only two numbers that matter:
fraction of the cube queried, and withheld W/L AUC of the reconstruction."""
import sys, os, time, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_sublinear import recover, reconstruct_score, auc
from fold_chess5 import NSTATES5

KIND = np.memmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kqkrr_kind.bin"),
                 dtype=np.uint8, mode="r")
U, D, W, L = 0, 1, 2, 3
N = 31
queried = np.zeros(NSTATES5, dtype=bool)


def query_batch(idx_arr):
    ii = idx_arr.astype(np.int64)
    queried[ii] = True
    k = KIND[ii]
    return np.where(k == W, 1.0, np.where(k == L, -1.0, 0.0))


if __name__ == "__main__":
    b = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    rounds = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    topk = int(sys.argv[3]) if len(sys.argv) > 3 else 8000
    rng = random.Random(20260615)
    cols = lambda r: [rng.randrange(1, 1 << N) for _ in range(b)]
    t = time.time()
    print("recovering (n=%d b=%d rounds=%d topk=%d)..." % (N, b, rounds, topk), flush=True)
    found = recover(query_batch, N, b, rounds, topk, cols)
    nq = int(queried.sum())
    print("recovered %d coeffs | queried %d = %.4f%% of cube | %.0fs"
          % (len(found), nq, 100.0 * nq / NSTATES5, time.time() - t), flush=True)

    # withheld evaluation set: decided positions NOT queried
    need = 200000
    samp = []
    rs = random.Random(7)
    while len(samp) < need:
        idx = rs.randrange(NSTATES5)
        if queried[idx]:
            continue
        k = KIND[idx]
        if k == W or k == L:
            samp.append(idx)
    samp = np.array(samp, dtype=np.int64)
    labels = np.where(KIND[samp] == W, 1, -1)
    scores = reconstruct_score(found, samp)
    a = auc(scores, labels)
    print("WITHHELD W/L AUC = %.5f  (n_eval=%d, W=%d L=%d) | %.0fs"
          % (a, samp.size, int((labels == 1).sum()), int((labels == -1).sum()), time.time() - t),
          flush=True)
    print("SUBLINEAR-KQKRR: queried %.4f%% of cube, withheld AUC %.5f" % (100.0 * nq / NSTATES5, a))
