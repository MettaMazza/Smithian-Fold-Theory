"""Peeling sparse-Walsh recovery — fixes the collision flaw.

Small bucket count B, several random hashes. A bucket holding exactly one heavy
coefficient (detected: |U_shift| == |U_base| for every unit shift) is recovered
and SUBTRACTED from every bucket in every round, which turns colliding buckets
into lone ones; iterate. Query cost = (n+1)*B*rounds with B ~ O(k), so it tracks
the COEFFICIENT count, not the field size. No new queries during peeling."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_sublinear import _fwht, _subspace_points, reconstruct_score, auc


def _parity(arr):
    x = arr.copy()
    p = np.zeros(arr.shape, dtype=np.uint64)
    while x.any():
        p ^= (x & np.uint64(1))
        x >>= np.uint64(1)
    return p


def _buckets(cols, ks, b):
    m = np.zeros(ks.shape, dtype=np.int64)
    for j in range(b):
        m |= (_parity(ks & np.uint64(cols[j])).astype(np.int64) << j)
    return m


def recover_peel(query_batch, n, b, rounds, rng_cols, tol=0.30, max_iter=40):
    B = 1 << b
    rd = []
    for r in range(rounds):
        cols = rng_cols(r)
        xb = _subspace_points(cols, b)
        U0 = _fwht(query_batch(xb).astype(np.float64))
        Ui = np.empty((n, B), dtype=np.float64)
        for i in range(n):
            Ui[i] = _fwht(query_batch(xb ^ np.uint64(1 << i)).astype(np.float64))
        rd.append([cols, U0, Ui])
    allabs = np.concatenate([np.abs(x[1]) for x in rd])
    thresh = 3.0 * np.median(allabs) + 1e-9
    found = {}
    for _ in range(max_iter):
        new = {}
        for cols, U0, Ui in rd:
            a0 = np.abs(U0)
            consistent = np.ones(B, dtype=bool)
            for i in range(n):
                consistent &= (np.abs(np.abs(Ui[i]) - a0) <= tol * a0 + 1e-9)
            lone = consistent & (a0 > thresh)
            idx = np.flatnonzero(lone)
            if idx.size == 0:
                continue
            s0 = np.sign(U0[idx])
            ks = np.zeros(idx.size, dtype=np.uint64)
            for i in range(n):
                ks |= ((np.sign(Ui[i][idx]) != s0).astype(np.uint64) << np.uint64(i))
            for kk, vv in zip(ks.tolist(), U0[idx].tolist()):
                if kk not in found and kk not in new:
                    new[kk] = vv
        if not new:
            break
        nk = np.array(list(new.keys()), dtype=np.uint64)
        nv = np.array(list(new.values()), dtype=np.float64)
        for cols, U0, Ui in rd:
            mb = _buckets(cols, nk, b)
            np.subtract.at(U0, mb, nv)
            for i in range(n):
                si = np.where(((nk >> np.uint64(i)) & np.uint64(1)) == 0, 1.0, -1.0)
                np.subtract.at(Ui[i], mb, nv * si)
        found.update(new)
    return found


def _selftest():
    import random
    rnd = random.Random(20260615)
    n, K, b = 24, 2000, 12
    planted = {}
    while len(planted) < K:
        planted[rnd.randrange(1, 1 << n)] = rnd.choice([-3., -2., -1., 1., 2., 3.])
    parr = np.array(list(planted.keys()), dtype=np.uint64)
    pval = np.array(list(planted.values()), dtype=np.float64)

    def f(idx):
        idx = idx.astype(np.uint64)
        out = np.zeros(idx.size)
        for kk, cc in zip(parr.tolist(), pval.tolist()):
            out += cc * np.where(_parity(idx & np.uint64(kk)) == 0, 1.0, -1.0)
        return out

    seen = set(); nq = [0]

    def qb(a):
        for v in a.tolist():
            if v not in seen:
                seen.add(v); nq[0] += 1
        return f(a)

    cols = lambda r: [rnd.randrange(1, 1 << n) for _ in range(b)]
    t = time.time()
    found = recover_peel(qb, n, b, rounds=5, rng_cols=cols)
    hit = sum(1 for k in planted if k in found)
    print("PEEL SELFTEST n=%d K=%d b=%d: recovered=%d correct=%d/%d | queries=%d (%.3f%% of 2^%d) | %.1fs"
          % (n, K, b, len(found), hit, K, nq[0], 100 * nq[0] / (1 << n), n, time.time() - t))
    print("PEEL SELFTEST:", "PASS" if hit >= int(0.95 * K) else "FAIL")


if __name__ == "__main__":
    _selftest()
