"""EXTERNAL READ (Route B) — Syzygy validation for KRRK."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess, chess.syzygy
from fold_chessRR import NSTATES_RR, decodeRR, BTM

if __name__ == "__main__":
    from fold_solveRR import solveRR
    res = solveRR(console=False)
    kind = res["kind"]
    U, D, W, L = 0, 1, 2, 3
    to_wdl = {W: 2, D: 0, L: -2}
    t = time.time()
    agree = disagree = checked = skipped_unreachable = 0
    ex = []
    UNREACH = chess.STATUS_TOO_MANY_CHECKERS | chess.STATUS_IMPOSSIBLE_CHECK
    with chess.syzygy.open_tablebase("/tmp/syzygy") as tb:
        for idx in range(NSTATES_RR):
            k = kind[idx]
            if k == U: continue
            wk, r1, r2, bk, stm = decodeRR(idx)
            b = chess.Board(None)
            b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
            b.set_piece_at(r1, chess.Piece(chess.ROOK, chess.WHITE))
            b.set_piece_at(r2, chess.Piece(chess.ROOK, chess.WHITE))
            b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
            b.turn = chess.WHITE if stm != BTM else chess.BLACK
            status = b.status()
            if status & UNREACH:
                skipped_unreachable += 1   # Syzygy probing of unreachable double-checks is undefined
                continue
            checked += 1
            mine = to_wdl[k]
            theirs = tb.probe_wdl(b)
            if mine == theirs: agree += 1
            else:
                disagree += 1
                if len(ex) < 8: ex.append((b.fen(), mine, theirs))
    print("EXTERNAL READ — Syzygy WDL diff, KRRK:")
    print("  checked: %d | agreements: %d | disagreements: %d | unreachable skipped: %d | %.1fs"
          % (checked, agree, disagree, skipped_unreachable, time.time() - t))
    for e in ex: print("   DISAGREE", e)
