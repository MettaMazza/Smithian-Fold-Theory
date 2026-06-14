"""EXTERNAL READ (Route B) — Syzygy WDL validation for KQKRR, parallelized.

Reads the solved kqkrr_kind.bin (written by fold_solve5) via memmap and probes
the certified KRRvKQ Syzygy table for every legal position, across all cores.
Compares on the WDL SIGN (win/draw/loss): our W matches Syzygy {win, cursed
win} = {2, 1}; our L matches {loss, blessed loss} = {-2, -1}; our D matches 0.
This is the WDL-without-50-move comparison our DTM solve computes — the same
certification standard used at every prior rung. Statically-valid-but-
unreachable double-check states are excluded from probing (disclosed
convention, identical to KRRK).
"""
import sys, os, time
import concurrent.futures as cf
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess
import chess.syzygy
from fold_chess5 import NSTATES5, decode5, BTM

U, D, W, L = 0, 1, 2, 3
KIND_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kqkrr_kind.bin")
SYZYGY_DIR = "/tmp/syzygy"
UNREACH = chess.STATUS_TOO_MANY_CHECKERS | chess.STATUS_IMPOSSIBLE_CHECK

_G = {}


def _init():
    _G["tb"] = chess.syzygy.open_tablebase(SYZYGY_DIR)
    _G["kind"] = np.memmap(KIND_PATH, dtype=np.uint8, mode="r")


def _board(wk, wq, r1, r2, bk, stm):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    b.set_piece_at(wq, chess.Piece(chess.QUEEN, chess.WHITE))
    b.set_piece_at(r1, chess.Piece(chess.ROOK, chess.BLACK))
    b.set_piece_at(r2, chess.Piece(chess.ROOK, chess.BLACK))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b


def read_span(span):
    lo, hi = span
    tb = _G["tb"]
    kind = _G["kind"]
    agree = disagree = checked = skipped = 0
    ex = []
    for idx in range(lo, hi):
        k = kind[idx]
        if k == U:
            continue
        wk, wq, r1, r2, bk, stm = decode5(idx)
        b = _board(wk, wq, r1, r2, bk, stm)
        if b.status() & UNREACH:
            skipped += 1
            continue
        checked += 1
        theirs = tb.probe_wdl(b)
        ours_win = (k == W)
        ours_loss = (k == L)
        ours_draw = (k == D)
        ok = ((ours_win and theirs > 0) or (ours_loss and theirs < 0)
              or (ours_draw and theirs == 0))
        if ok:
            agree += 1
        else:
            disagree += 1
            if len(ex) < 6:
                ex.append((b.fen(), int(k), int(theirs)))
    return agree, disagree, checked, skipped, ex


if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    t = time.time()
    nchunks = workers * 8
    step = (NSTATES5 + nchunks - 1) // nchunks
    spans = [(lo, min(lo + step, NSTATES5)) for lo in range(0, NSTATES5, step)]
    A = Dg = C = S = 0
    ex_all = []
    with cf.ProcessPoolExecutor(max_workers=workers, initializer=_init) as exr:
        done = 0
        for agree, disagree, checked, skipped, ex in exr.map(read_span, spans):
            A += agree; Dg += disagree; C += checked; S += skipped
            ex_all.extend(ex)
            done += 1
            print("  span %d/%d done: cum agree %d / disagree %d / checked %d, %.0fs"
                  % (done, len(spans), A, Dg, C, time.time() - t), flush=True)
    print("EXTERNAL READ — Syzygy WDL diff, KQKRR:")
    print("  checked: %d | agreements: %d | disagreements: %d | unreachable skipped: %d | %.0fs"
          % (C, A, Dg, S, time.time() - t))
    for e in ex_all[:6]:
        print("   DISAGREE", e)
    print("EXTERNAL READ COMPLETE: %s" % ("PASS" if Dg == 0 else "FAIL"))
