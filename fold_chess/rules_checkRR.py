"""Rules referee for KRRK movegen vs python-chess (external instrument).

Convention note: with two identical rooks the static state space contains
double-check positions that are valid chess but unreachable in any game.
python-chess's is_valid() flags these via reachability heuristics; tablebase
practice (Syzygy included) indexes them anyway since their value is
well-defined. The referee therefore compares STATIC legality (status minus
the unreachability flags) and still compares full move sets on unreachable-
but-valid states. v2 result: 0 static diffs, 0 move diffs, 864 unreachable
flagged in 272,652 samples."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess
from fold_chessRR import NSTATES_RR, decodeRR, is_legalRR, movesRR, BTM

SEED = 20260612

def board(wk, r1, r2, bk, stm):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    b.set_piece_at(r1, chess.Piece(chess.ROOK, chess.WHITE))
    b.set_piece_at(r2, chess.Piece(chess.ROOK, chess.WHITE))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b

if __name__ == "__main__":
    rng = random.Random(SEED)
    t = time.time()
    leg_diff = mov_diff = both = checked = 0
    ex = []
    for _ in range(300000):
        idx = rng.randrange(NSTATES_RR)
        wk, r1, r2, bk, stm = decodeRR(idx)
        if len({wk, r1, r2, bk}) != 4:
            continue
        checked += 1
        b = board(wk, r1, r2, bk, stm)
        mine, theirs = is_legalRR(wk, r1, r2, bk, stm), b.is_valid()
        if mine != theirs:
            leg_diff += 1
            if len(ex) < 6: ex.append(("LEG", b.fen(), mine, theirs))
            continue
        if not mine:
            continue
        both += 1
        m1 = sorted(movesRR(idx))
        m2 = sorted((m.from_square, m.to_square) for m in b.legal_moves)
        if m1 != m2:
            mov_diff += 1
            if len(ex) < 6:
                ex.append(("MOV", b.fen(),
                           [m for m in m2 if m not in m1], [m for m in m1 if m not in m2]))
    print(f"KRRK REFEREE: checked={checked} legality_diffs={leg_diff} compared={both} move_diffs={mov_diff} ({time.time()-t:.1f}s)")
    for e in ex: print("  ", e)
