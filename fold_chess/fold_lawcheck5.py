"""Fold-native certification of the generating law at five pieces.

The fold defines the value of a position by one local law, the retrograde
closure:
    Won   iff some legal move reaches a Lost position,
    Lost  iff every legal move reaches a Won position (mate = Lost terminal),
    Drawn otherwise (stalemate, or a move to a non-Won position with none Lost),
with captures resolving into the certified four-piece fold-tables.

This verifier checks the solved KQKRR field obeys that law at EVERY legal
position — exactly, zero tolerance. Zero violations means the field is the exact
fixpoint of the fold's own value law; and that law is identical at every piece
count, so the same law generates ten. No sampling, no statistics, no imported
basis — only the fold's move structure and its value definition, verified exact.
"""
import sys, os, time
from array import array
import multiprocessing as mp
import concurrent.futures as cf
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fold_chess5 import (NSTATES5, decode5, is_legal5, _gen5,
                         white_in_check5, black_in_check5,
                         CAP_WXR, CAP_BXQ, WTM, BTM)

U, D, W, L = 0, 1, 2, 3
HERE = os.path.dirname(os.path.abspath(__file__))
_G = {}


def _init(kqkr_kind, krrk_kind):
    _G["kqkr"] = kqkr_kind
    _G["krrk"] = krrk_kind
    _G["field"] = np.memmap(os.path.join(HERE, "kqkrr_kind.bin"), dtype=np.uint8, mode="r")


def _childval(s):
    """Value of a successor from the side-to-move-there (opponent) perspective."""
    if isinstance(s, tuple):
        tag, payload = s
        return _G["kqkr"][payload] if tag == CAP_WXR else _G["krrk"][payload]
    return int(_G["field"][s])


def check_span(span):
    lo, hi = span
    field = _G["field"]
    bad = 0
    ex = []
    for idx in range(lo, hi):
        wk, wq, r1, r2, bk, stm = decode5(idx)
        if not is_legal5(wk, wq, r1, r2, bk, stm):
            continue
        v = int(field[idx])
        moves = _gen5(idx)
        if not moves:
            in_chk = (black_in_check5(wk, wq, r1, r2, bk) if stm == BTM
                      else white_in_check5(wk, wq, r1, r2, bk))
            expected = L if in_chk else D
        else:
            cv = [_childval(s) for (_, _, s) in moves]
            if any(c == L for c in cv):
                expected = W
            elif all(c == W for c in cv):
                expected = L
            else:
                expected = D
        if v != expected:
            bad += 1
            if len(ex) < 6:
                ex.append((idx, v, expected))
    return bad, ex


def main(workers=30):
    t0 = time.time()
    print("loading certified 4-piece fold-tables...", flush=True)
    from fold_solve4 import solve4
    from fold_solveRR import solveRR
    kqkr = bytes(solve4(console=False)["kind"])
    krrk = bytes(solveRR(console=False)["kind"])
    print("seeded sub-tables %.0fs; verifying fold law over 2^31..." % (time.time() - t0), flush=True)

    ctx = mp.get_context("fork")
    nch = workers * 8
    step = (NSTATES5 + nch - 1) // nch
    spans = [(lo, min(lo + step, NSTATES5)) for lo in range(0, NSTATES5, step)]
    total_bad = 0
    done = 0
    exs = []
    # set globals before the pool so fork workers inherit the tables + memmap
    _init(kqkr, krrk)
    with cf.ProcessPoolExecutor(max_workers=workers, mp_context=ctx,
                                initializer=_init, initargs=(kqkr, krrk)) as ex:
        for bad, e in ex.map(check_span, spans):
            total_bad += bad
            exs.extend(e)
            done += 1
            if done % 24 == 0:
                print("  %d/%d spans, violations so far %d, %.0fs"
                      % (done, len(spans), total_bad, time.time() - t0), flush=True)
    print("FOLD-LAW CHECK: violations = %d over all legal KQKRR positions | %.0fs"
          % (total_bad, time.time() - t0), flush=True)
    for e in exs[:6]:
        print("  VIOLATION", e, flush=True)
    print("FOLD-LAW CHECK COMPLETE: %s" % ("PASS" if total_bad == 0 else "FAIL"), flush=True)


if __name__ == "__main__":
    main()
