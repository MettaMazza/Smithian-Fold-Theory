"""EXTERNAL READ (Route B) — Syzygy validation harness for fold_chess.

This file is comparison-side instrumentation, the chess analogue of
particle_validation.py reading PDG/CODATA: it takes the fold solver's
completed values and diffs them, position by position, against the Syzygy
tablebases (an independent external computation). Nothing here feeds any
derivation. Any disagreement is adjudicated by hand on the board.

Not subject to fold source conventions (external instrument), exactly as
particle_validation.py is not.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess
import chess.syzygy

from fold_chess import solve, decode, BTM

PIECE_SYMBOL = {"Q": chess.QUEEN, "R": chess.ROOK}


def board_from_state(wk, wp, bk, stm, piece):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    b.set_piece_at(wp, chess.Piece(PIECE_SYMBOL[piece], chess.WHITE))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b


def run_diff(piece="Q", tb_path="/tmp/syzygy", res=None):
    if res is None:
        res = solve(piece=piece, console=True)
    kind, ply, wdl5 = res["kind"], res["ply"], res["wdl5"]

    # my five-valued result -> Syzygy WDL integer (side-to-move perspective)
    to_wdl = {"win": 2, "cursed_win": 1, "draw": 0, "blessed_loss": -1, "loss": -2}

    t = time.time()
    agree = disagree = checked = rules_diff = 0
    examples = []
    with chess.syzygy.open_tablebase(tb_path) as tb:
        for idx in range(len(kind)):
            if kind[idx] == "U":
                continue
            wk, wp, bk, stm = decode(idx)
            b = board_from_state(wk, wp, bk, stm, piece)
            if not b.is_valid():
                rules_diff += 1          # I call it legal, python-chess does not
                continue
            checked += 1
            mine = to_wdl[wdl5(idx)]
            theirs = tb.probe_wdl(b)
            if mine == theirs:
                agree += 1
            else:
                disagree += 1
                if len(examples) < 10:
                    examples.append((b.fen(), mine, theirs, kind[idx], ply[idx]))

    print("EXTERNAL READ — Syzygy WDL diff, K%sK:" % piece)
    print("  positions checked: %d" % checked)
    print("  agreements:        %d" % agree)
    print("  disagreements:     %d" % disagree)
    print("  rules-legality diffs (mine legal, python-chess invalid): %d" % rules_diff)
    print("  elapsed: %.1fs" % (time.time() - t))
    for fen, m, th, k, p in examples:
        print("    DISAGREE %s | mine=%d (kind=%s ply=%d) syzygy=%d" % (fen, m, k, p, th))
    return {"checked": checked, "agree": agree, "disagree": disagree,
            "rules_diff": rules_diff, "examples": examples}


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Q"
    run_diff(piece=which)
