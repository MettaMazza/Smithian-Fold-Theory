"""Innovation route, 5-piece datapoint: does the sparse fold-spectrum fragment
generalization survive a SECOND material step (4 -> 5)?

Same protocol that scored AUC 0.998 at four pieces (5% chi-key train ->
withheld W/L AUC, sparse top-k of the fold's Walsh basis), now at KQKRR
(2^31). Reads the solved field, selects a 5% fragment by the same Weil-flat
quadratic-character key (vectorized via a precomputed character table),
transforms the fragment with the numpy fast-WHT, keeps the top-k coefficients
at matched sparse FRACTIONS, and grades the reconstruction's ranking on the
withheld 95% by AUC. Compare against the 4-piece operating points
(frac 6.1e-5 -> 0.998 ; frac 3.9e-3 -> 0.963).
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_chess5 import NSTATES5
from fold_chess import find_fold_prime
from fold_theorems5 import fwht_inplace

KIND_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kqkrr_kind.bin")
U, D, W, L = 0, 1, 2, 3
FRACS = (6.1e-5, 3.9e-3)
NBITS = 20
SHIFT = 5003


def char_table(P):
    """chi_table[r] = 1 if r (or 1 if r==0) is a quadratic residue mod P else 0,
    for r in 0..P-1, computed in memory-bounded chunks (uint64 modpow)."""
    e = (P - 1) // 2
    tab = np.empty(P, dtype=np.uint8)
    CH = 1 << 24
    for base in range(0, P, CH):
        end = min(base + CH, P)
        b = np.arange(base, end, dtype=np.uint64)
        b[b == 0] = 1
        # modular exponentiation b^e mod P, square-and-multiply, uint64-safe
        res = np.ones(end - base, dtype=np.uint64)
        ee = e
        bb = b.copy()
        while ee:
            if ee & 1:
                res = (res * bb) % P
            ee >>= 1
            if ee:
                bb = (bb * bb) % P
        tab[base:end] = (res == 1).astype(np.uint8)
    return tab


if __name__ == "__main__":
    t = time.time()
    P = find_fold_prime(NSTATES5)
    kind = np.memmap(KIND_PATH, dtype=np.uint8, mode="r")
    legal = np.flatnonzero(kind != U)
    print("legal=%d ; building character table (P=%d)... %.0fs"
          % (legal.size, P, time.time() - t), flush=True)
    chi = char_table(P)
    print("  chi table ready, %.0fs" % (time.time() - t), flush=True)

    # 20-bit Weil-flat key per legal index (vectorized table gathers)
    print("computing fragment keys...", flush=True)
    keys = np.zeros(legal.size, dtype=np.uint32)
    base = (legal.astype(np.int64) + 1)
    for s in range(NBITS):
        r = (base + s * SHIFT) % P
        keys = (keys << np.uint32(1)) | chi[r].astype(np.uint32)
    order = np.argsort(keys, kind="stable")
    nsamp = int(0.05 * legal.size)
    samp_idx = legal[order[:nsamp]]
    wh_idx = legal[order[nsamp:]]
    del keys, order, base
    print("  sample=%d withheld=%d ; %.0fs" % (samp_idx.size, wh_idx.size, time.time() - t),
          flush=True)

    # truth for the withheld decided set
    kw = kind[wh_idx]
    dec_mask = (kw == W) | (kw == L)
    wh_dec = wh_idx[dec_mask]
    wh_truth = np.where(kind[wh_dec] == W, 1, -1).astype(np.int8)
    nW = int((wh_truth == 1).sum())
    nL = int((wh_truth == -1).sum())
    print("  withheld decided=%d (W=%d L=%d) ; %.0fs"
          % (wh_dec.size, nW, nL, time.time() - t), flush=True)

    # build the 5% sample field over the full cube, transform once
    f = np.zeros(NSTATES5, dtype=np.int64)
    sv = kind[samp_idx]
    f[samp_idx[sv == W]] = 1
    f[samp_idx[sv == L]] = -1
    print("running fast-WHT on the fragment field... %.0fs" % (time.time() - t), flush=True)
    spec = fwht_inplace(f)
    mag = np.abs(spec)
    print("  WHT done; ranking coefficients... %.0fs" % (time.time() - t), flush=True)

    for fr in FRACS:
        kb = max(1, int(NSTATES5 * fr))
        topk = np.argpartition(mag, NSTATES5 - kb)[NSTATES5 - kb:]
        tr = np.zeros(NSTATES5, dtype=np.int64)
        tr[topk] = spec[topk]
        rec = fwht_inplace(tr)              # reconstruct (overwrites tr)
        score = rec[wh_dec].astype(np.float64)
        # AUC via rank-sum (Mann-Whitney)
        ssort = np.argsort(score, kind="stable")
        ranks = np.empty(score.size, dtype=np.float64)
        ranks[ssort] = np.arange(1, score.size + 1)
        rs = float(ranks[wh_truth == 1].sum())
        auc = (rs - nW * (nW + 1) / 2) / (nW * nL)
        print("FRAG-AUC5 frac=%.2e k=%d: withheld W/L AUC=%.5f (n_wh=%d dec=%d) %.0fs"
              % (fr, kb, auc, wh_idx.size, wh_dec.size, time.time() - t), flush=True)
    print("FRAG-AUC5 COMPLETE", flush=True)
