"""EXTERNAL READ (Route B) — Syzygy validation harness for the 4-piece KQKR
solution. Comparison-side instrument, exactly as syzygy_read.py at Rung 1:
nothing here feeds any derivation; disagreements are adjudicated by hand.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess
import chess.syzygy

from fold_chess4 import NSTATES4, decode4, BTM

U, D, W, L = 0, 1, 2, 3


def board4(wk, wq, br, bk, stm):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    b.set_piece_at(wq, chess.Piece(chess.QUEEN, chess.WHITE))
    b.set_piece_at(br, chess.Piece(chess.ROOK, chess.BLACK))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b


def run_diff4(kind, ply, no_cursed, tb_path="/tmp/syzygy"):
    """kind/ply: solver output arrays. Maps my values to Syzygy WDL from the
    side-to-move perspective: W->2, D->0, L->-2 (cursed/blessed impossible at
    this rung iff no_cursed, which this diff itself independently tests —
    a Syzygy ±1 anywhere I claim ±2 would surface as a disagreement)."""
    to_wdl = {W: 2, D: 0, L: -2}
    t = time.time()
    agree = disagree = checked = rules_diff = 0
    examples = []
    with chess.syzygy.open_tablebase(tb_path) as tb:
        for idx in range(NSTATES4):
            k = kind[idx]
            if k == U:
                continue
            wk, wq, br, bk, stm = decode4(idx)
            b = board4(wk, wq, br, bk, stm)
            if not b.is_valid():
                rules_diff += 1
                continue
            checked += 1
            mine = to_wdl[k]
            theirs = tb.probe_wdl(b)
            if mine == theirs:
                agree += 1
            else:
                disagree += 1
                if len(examples) < 10:
                    examples.append((b.fen(), mine, theirs, k, ply[idx]))
    print("EXTERNAL READ — Syzygy WDL diff, KQKR:")
    print("  positions checked: %d" % checked)
    print("  agreements:        %d" % agree)
    print("  disagreements:     %d" % disagree)
    print("  rules-legality diffs: %d" % rules_diff)
    print("  elapsed: %.1fs" % (time.time() - t))
    for e in examples:
        print("    DISAGREE", e)
    return {"checked": checked, "agree": agree, "disagree": disagree,
            "rules_diff": rules_diff}


if __name__ == "__main__":
    from fold_solve4 import solve4
    res = solve4(console=True)
    run_diff4(res["kind"], res["ply"], res["no_cursed_theorem"])
