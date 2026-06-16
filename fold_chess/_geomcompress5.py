"""Does the five-piece value factor through a small set of fold-geometric
invariants? Partition positions by an exact fold-geometric invariant vector
(distances via the fold's take, line control via the fold's slider logic,
symmetric in the two identical rooks). Measure, exactly: how many distinct
invariant-classes appear, and what fraction of positions sit in classes that
carry a SINGLE value (pure). High purity + sub-exponential class count = the
value is compactly determined by geometry. No fitting, no thresholds."""
import sys, os, time, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_chess5 import (NSTATES5, decode5, is_legal5,
                         white_in_check5, black_in_check5)
from fold_chess4 import _slider_attacks
from fold_chess import _ROOK_RAYS, _QUEEN_RAYS

HERE = os.path.dirname(os.path.abspath(__file__))
KIND = np.memmap(os.path.join(HERE, "kqkrr_kind.bin"), dtype=np.uint8, mode="r")
U, D, W, L = 0, 1, 2, 3


def cheb(a, b):
    return max(abs((a >> 3) - (b >> 3)), abs((a & 7) - (b & 7)))


def edge(s):
    r, f = s >> 3, s & 7
    return min(r, 7 - r, f, 7 - f)


def corner(s):
    r, f = s >> 3, s & 7
    return max(min(r, 7 - r), min(f, 7 - f))   # 0 only at the four corners


def q_hits(wq, tgt, occ):
    return tgt in _slider_attacks(wq, _QUEEN_RAYS, occ, None)


def r_hits(rsq, tgt, occ):
    return tgt in _slider_attacks(rsq, _ROOK_RAYS, occ, None)


def invariant(idx):
    wk, wq, r1, r2, bk, stm = decode5(idx)
    occ = {wk, wq, r1, r2, bk}
    wchk = 1 if white_in_check5(wk, wq, r1, r2, bk) else 0
    bchk = 1 if black_in_check5(wk, wq, r1, r2, bk) else 0
    kkd = cheb(wk, bk)
    bke = edge(bk)
    bkc = 0 if corner(bk) == 0 else (1 if corner(bk) <= 1 else 2)
    qbd = cheb(wq, bk)
    qr = (1 if q_hits(wq, r1, occ - {r1}) else 0) + (1 if q_hits(wq, r2, occ - {r2}) else 0)
    rq = (1 if r_hits(r1, wq, occ - {wq}) else 0) + (1 if r_hits(r2, wq, occ - {wq}) else 0)
    conn = 1 if r_hits(r1, r2, occ - {r2}) else 0
    rbk = min(cheb(r1, bk), cheb(r2, bk))           # rook nearest black king
    rwk = min(cheb(r1, wk), cheb(r2, wk))
    # pack into one int64 key (each field small)
    fields = [stm, wchk, bchk, kkd, min(bke, 3), bkc, min(qbd, 7), qr, rq, conn,
              min(rbk, 7), min(rwk, 7)]
    key = 0
    for v in fields:
        key = key * 9 + (v + 1)
    return key


if __name__ == "__main__":
    NSAMP = int(sys.argv[1]) if len(sys.argv) > 1 else 8000000
    rng = random.Random(20260615)
    t = time.time()
    keys = np.empty(NSAMP, dtype=np.int64)
    vals = np.empty(NSAMP, dtype=np.uint8)
    got = 0
    while got < NSAMP:
        idx = rng.randrange(NSTATES5)
        k = KIND[idx]
        if k == U:
            continue
        wk, wq, r1, r2, bk, stm = decode5(idx)
        if not is_legal5(wk, wq, r1, r2, bk, stm):
            continue
        keys[got] = invariant(idx)
        vals[got] = k
        got += 1
        if got % 1000000 == 0:
            print("  sampled %d/%d  %.0fs" % (got, NSAMP, time.time() - t), flush=True)

    order = np.argsort(keys, kind="stable")
    ks = keys[order]; vs = vals[order]
    bounds = np.flatnonzero(np.diff(ks)) + 1
    starts = np.concatenate(([0], bounds))
    ends = np.concatenate((bounds, [NSAMP]))
    nclass = starts.size
    pure_pos = 0
    pure_cls = 0
    for s, e in zip(starts.tolist(), ends.tolist()):
        seg = vs[s:e]
        if seg.min() == seg.max():
            pure_pos += (e - s)
            pure_cls += 1
    print("\nGEOM-COMPRESS (5pc, sample=%d)" % NSAMP, flush=True)
    print("  distinct invariant-classes: %d" % nclass, flush=True)
    print("  classes that are value-pure: %d (%.2f%%)" % (pure_cls, 100.0 * pure_cls / nclass), flush=True)
    print("  positions in pure classes:   %d (%.4f%%)" % (pure_pos, 100.0 * pure_pos / NSAMP), flush=True)
    print("GEOM-COMPRESS DONE %.0fs" % (time.time() - t), flush=True)
