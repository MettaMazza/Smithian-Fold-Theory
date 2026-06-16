"""Sublinear sparse-Walsh recovery — the breakthrough engine.

The wall: exact tablebases die because you must hold/enumerate the whole cube.
The escape: the value field is sparse in the fold's Walsh basis, so recover the
heavy coefficients by ALIASING — query the field on a small random subspace,
take the small Walsh transform, and the 2^n coefficients fold into 2^b buckets.
Heavy coefficients light up as heavy buckets; unit-shift queries read off the
index of the lone heavy coefficient in each bucket. Total queries ~ (n+1)*2^b
per round — a tiny, board-independent fraction of the 2^n cube.

Math (Walsh-Hadamard, indices in {0,1}^n):
  sample on subspace x = M.j  (M is n-by-b binary, j in {0,1}^b)
  U[m] = WHT_b(f[M.j])[m] = (2^b/2^n) * sum_{k : M^T k = m} F[k]
  shift by e_i:  U_i[m] = U[m] * (-1)^{k*_i}  for a lone-heavy bucket k*
  => bit i of the recovered coefficient = sign(U_i[m]) != sign(U[m]).

Success metric, honest and unfudgeable: (1) fraction of the cube queried,
(2) withheld W/L AUC of the reconstructed field. Sublinear queries + high AUC
on positions never seen = the gate to ten-plus pieces is open.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _fwht(a):
    """In-place fast Walsh-Hadamard transform (natural order)."""
    n = a.size
    h = 1
    while h < n:
        a2 = a.reshape(-1, 2 * h)
        x = a2[:, :h].copy()
        y = a2[:, h:].copy()
        a2[:, :h] = x + y
        a2[:, h:] = x - y
        h *= 2
    return a


def _subspace_points(cols, b):
    """All 2^b points x = M.j for j in 0..2^b-1, as a uint64 array.
    cols: list of b column masks (each an n-bit int). Vectorized subset-XOR."""
    N = 1 << b
    j = np.arange(N, dtype=np.uint64)
    x = np.zeros(N, dtype=np.uint64)
    for i in range(b):
        bit = ((j >> np.uint64(i)) & np.uint64(1)).astype(np.uint64)
        x ^= np.uint64(cols[i]) * bit
    return x


def recover(query_batch, n, b, rounds, topk, rng_cols, queried_mark=None):
    """Recover heavy Walsh coefficients by aliasing.
      query_batch(idx_array) -> float array of f at those indices (and marks them).
      n: index bit-width, b: subspace dim, rounds: independent M matrices,
      topk: heavy buckets kept per round, rng_cols: callable -> b random n-bit cols.
    Returns dict {k: averaged coefficient value}."""
    found = {}
    for r in range(rounds):
        cols = rng_cols(r)
        xb = _subspace_points(cols, b)                  # base subspace points
        U0 = _fwht(query_batch(xb).astype(np.float64))
        # unit-shift transforms, one per index bit
        Ui = np.empty((n, xb.size), dtype=np.float64)
        for i in range(n):
            Ui[i] = _fwht(query_batch(xb ^ np.uint64(1 << i)).astype(np.float64))
        # heavy buckets
        order = np.argsort(-np.abs(U0))[:topk]
        s0 = np.sign(U0)
        for m in order:
            if U0[m] == 0:
                continue
            k = 0
            for i in range(n):
                if np.sign(Ui[i, m]) != s0[m]:
                    k |= (1 << i)
            v = U0[m]
            if k in found:
                found[k] = (found[k] + v) / 2.0
            else:
                found[k] = v
    return found


def reconstruct_score(found, idxs):
    """Score = sum_k val * (-1)^<k,idx> over recovered coeffs, for each idx.
    (Overall scale irrelevant for AUC.)"""
    ks = np.array(list(found.keys()), dtype=np.uint64)
    vs = np.array(list(found.values()), dtype=np.float64)
    out = np.zeros(idxs.size, dtype=np.float64)
    idxs = idxs.astype(np.uint64)
    for kk, vv in zip(ks, vs):
        par = np.zeros(idxs.size, dtype=np.int64)
        anded = idxs & np.uint64(kk)
        x = anded.copy()
        while x.any():
            par ^= (x & np.uint64(1)).astype(np.int64)
            x >>= np.uint64(1)
        out += vv * np.where(par == 0, 1.0, -1.0)
    return out


def auc(scores, labels):
    """W/L AUC via rank-sum. labels: +1 win, -1 loss."""
    W = labels == 1
    L = labels == -1
    nW, nL = int(W.sum()), int(L.sum())
    if nW == 0 or nL == 0:
        return float("nan")
    order = np.argsort(scores, kind="stable")
    ranks = np.empty(scores.size, dtype=np.float64)
    ranks[order] = np.arange(1, scores.size + 1)
    rs = float(ranks[W].sum())
    return (rs - nW * (nW + 1) / 2) / (nW * nL)


# ----------------------------------------------------------------- self-test
def _selftest():
    """Plant K random heavy Walsh coefficients in an n-bit field, recover them
    by aliasing, confirm sublinear queries and correct recovery."""
    import random
    rnd = random.Random(20260615)
    n, K = 24, 200
    planted = {}
    while len(planted) < K:
        k = rnd.randrange(1, 1 << n)
        planted[k] = rnd.choice([-3.0, -2.0, -1.0, 1.0, 2.0, 3.0])

    def f(idx):
        # f[idx] = sum_k c_k (-1)^<k,idx>   (the inverse WHT of a sparse spectrum)
        out = np.zeros(idx.size, dtype=np.float64)
        idx = idx.astype(np.uint64)
        for kk, cc in planted.items():
            par = np.zeros(idx.size, dtype=np.int64)
            x = (idx & np.uint64(kk)).copy()
            while x.any():
                par ^= (x & np.uint64(1)).astype(np.int64)
                x >>= np.uint64(1)
            out += cc * np.where(par == 0, 1.0, -1.0)
        return out

    seen = set()
    nq = [0]

    def qb(idx_arr):
        for v in idx_arr.tolist():
            if v not in seen:
                seen.add(v)
                nq[0] += 1
        return f(idx_arr)

    def cols(r):
        return [rnd.randrange(1, 1 << n) for _ in range(b)]

    b = 12
    t = time.time()
    found = recover(qb, n, b, rounds=3, topk=400, rng_cols=cols)
    hits = sum(1 for k in planted if k in found)
    print("SELFTEST n=%d planted=%d recovered=%d correct=%d/%d | queries=%d (%.3f%% of 2^%d) | %.1fs"
          % (n, K, len(found), hits, K, nq[0], 100 * nq[0] / (1 << n), n, time.time() - t))
    print("SELFTEST:", "PASS" if hits >= int(0.9 * K) else "FAIL")


if __name__ == "__main__":
    _selftest()
