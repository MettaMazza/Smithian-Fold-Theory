"""Certified spectral theorems at five pieces (2^31), via numpy fast-WHT.

Recreates the Rung 2.5 / CERTIFIED_THEOREMS payload one piece higher:
  - T-CHESS-2 (vanishing law): the value field is invariant under horizontal
    mirror, which on the index is XOR by a fixed mask M (file bits of all five
    squares). Walsh algebra then forces every coefficient c_w with
    popcount(w & M) odd to vanish exactly. Certified by exhaustive check.
  - Energy concentration C(k) of the value field in the fold's Walsh basis,
    at k = 2^5, 2^8, ..., 2^20 — the sparsity measurement, one scale up.
The field-level mirror and rook-swap symmetries are already certified
exhaustively inside fold_solve5; this exhibits their spectral consequence.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_chess5 import NSTATES5

KIND_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kqkrr_kind.bin")
U, D, W, L = 0, 1, 2, 3

# horizontal-mirror index mask: file bits (low 3) of each 6-bit square field.
# layout: bit0=stm; bk@1..6, r2@7..12, r1@13..18, wq@19..24, wk@25..30
M_HORIZ = (7 << 1) | (7 << 7) | (7 << 13) | (7 << 19) | (7 << 25)


def fwht_inplace(a):
    """In-place fast Walsh-Hadamard transform (natural order), numpy int64."""
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


if __name__ == "__main__":
    t = time.time()
    kind = np.memmap(KIND_PATH, dtype=np.uint8, mode="r")
    print("building signed value field over %d cells..." % NSTATES5, flush=True)
    f = np.zeros(NSTATES5, dtype=np.int64)
    f[kind == W] = 1
    f[kind == L] = -1
    decided = int((kind == W).sum() + (kind == L).sum())
    print("  decided (W or L) = %d ; %.0fs" % (decided, time.time() - t), flush=True)

    print("running fast Walsh-Hadamard transform (2^31)...", flush=True)
    spec = fwht_inplace(f)              # f is overwritten with coefficients
    print("  WHT done, %.0fs" % (time.time() - t), flush=True)

    # ---- T-CHESS-2 vanishing law: c_w == 0 whenever popcount(w & M) is odd
    print("certifying vanishing law (mask=%d)..." % M_HORIZ, flush=True)
    viol = 0
    vanish_total = 0
    CH = 1 << 26
    for base in range(0, NSTATES5, CH):
        end = min(base + CH, NSTATES5)
        w = np.arange(base, end, dtype=np.int64)
        par = np.zeros(end - base, dtype=np.int64)
        m = w & M_HORIZ
        # popcount parity of m
        x = m.copy()
        while x.any():
            par ^= (x & 1)
            x >>= 1
        odd = par == 1
        vanish_total += int(odd.sum())
        seg = spec[base:end]
        viol += int((seg[odd] != 0).sum())
    print("  vanishing-class coefficients: %d | nonzero among them (violations): %d"
          % (vanish_total, viol), flush=True)

    # ---- energy concentration C(k)
    print("computing energy concentration...", flush=True)
    sq = spec.astype(np.float64)
    sq *= sq
    total = float(sq.sum())
    # top-k energy via partial sort on magnitudes (work on a copy of squares)
    ks = [2 ** e for e in (5, 8, 11, 14, 17, 20)]
    order_top = np.argpartition(sq, NSTATES5 - max(ks))[NSTATES5 - max(ks):]
    top_sorted = np.sort(sq[order_top])[::-1]
    cum = np.cumsum(top_sorted)
    print("ENERGY CONCENTRATION C(k) (fraction of total energy):", flush=True)
    for k in ks:
        ck = cum[k - 1] / total if total else 0.0
        print("  C(2^%d = %d) = %.5f" % (k.bit_length() - 1, k, ck), flush=True)

    print("THEOREMS5: vanishing_violations=%d (PASS=%s) | decided=%d | %.0fs"
          % (viol, viol == 0, decided, time.time() - t), flush=True)
    print("THEOREMS5 COMPLETE")
