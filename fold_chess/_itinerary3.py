"""Step 1+2 at 3 pieces: the value field's structure in the FOLD's coordinates
(itinerary of (i+1)/P under the doubling map), exact, compared to the raw-index
coordinates the corpus and I used before.

For position i the fold-state is (i+1)/P. Its itinerary bit at step t is
b_t(i) = [ (i+1)*2^t mod P > P/2 ]  (the t-th binary digit of (i+1)/P under
doubling). chi_t = (-1)^{b_t}. These are the fold's own harmonics.

We compute, exactly, the correlation of the value with each order-1 and order-2
fold-harmonic, and the same in raw-index bits, and compare which coordinate
system carries the value at low order. Integers only; no thresholds, no fitting."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import solve, NSTATES, find_fold_prime

if __name__ == "__main__":
    t0 = time.time()
    P = find_fold_prime(NSTATES)
    n = NSTATES.bit_length() - 1               # 19
    r = solve(piece="Q", console=False)
    f = np.array([1 if k == "W" else (-1 if k == "L" else 0) for k in r["kind"]], dtype=np.int64)
    dec = int((f != 0).sum())
    print("KQK: states=%d decided=%d P=%d n=%d  %.0fs" % (NSTATES, dec, P, n, time.time() - t0), flush=True)

    # fold itinerary harmonics
    M = 40
    res = (np.arange(NSTATES, dtype=np.int64) + 1) % P
    chi_it = np.empty((M, NSTATES), dtype=np.int8)
    half = P // 2
    for t in range(M):
        chi_it[t] = np.where(res > half, -1, 1)
        res = (res * 2) % P
    # raw index harmonics
    idx = np.arange(NSTATES, dtype=np.int64)
    chi_raw = np.empty((n, NSTATES), dtype=np.int8)
    for t in range(n):
        chi_raw[t] = np.where(((idx >> t) & 1) == 1, -1, 1)

    def order1(chis):
        c = chis.astype(np.int64) @ f          # sum_i f*chi_t
        return np.abs(c) / dec                  # |correlation| in [0,1]

    def order2(chis):
        K = chis.shape[0]
        best = 0.0
        big = 0
        for a in range(K):
            ca = chis[a].astype(np.int64) * f
            for b in range(a + 1, K):
                v = abs(int(ca @ chis[b].astype(np.int64))) / dec
                if v > best:
                    best = v
                if v > 0.30:
                    big += 1
        return best, big

    o1_it = order1(chi_it); o1_raw = order1(chi_raw)
    o2_it_max, o2_it_big = order2(chi_it)
    o2_raw_max, o2_raw_big = order2(chi_raw)

    print("\nORDER-1 max |corr|:   itinerary=%.4f   raw-index=%.4f" % (o1_it.max(), o1_raw.max()), flush=True)
    print("ORDER-1 #(|corr|>0.30): itinerary=%d   raw-index=%d"
          % (int((o1_it > 0.30).sum()), int((o1_raw > 0.30).sum())), flush=True)
    print("ORDER-2 max |corr|:   itinerary=%.4f   raw-index=%.4f" % (o2_it_max, o2_raw_max), flush=True)
    print("ORDER-2 #(|corr|>0.30): itinerary=%d   raw-index=%d" % (o2_it_big, o2_raw_big), flush=True)
    print("ITINERARY3 DONE %.0fs" % (time.time() - t0), flush=True)
