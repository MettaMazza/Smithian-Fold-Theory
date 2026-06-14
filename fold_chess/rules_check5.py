"""Rules referee for KQKRR movegen vs python-chess (external instrument).

Same convention as KRRK: with two identical black rooks the static state space
contains double-check positions that are valid chess but unreachable in any
game. python-chess flags these via TOO_MANY_CHECKERS / IMPOSSIBLE_CHECK; we
compare STATIC legality (status minus the unreachability flags) and still
compare full move sets on unreachable-but-valid states. Zero static diffs and
zero move diffs are required before the solver is permitted to run.
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess
from fold_chess5 import NSTATES5, decode5, is_legal5, moves5, BTM

SEED = 20260612
UNREACH = chess.STATUS_TOO_MANY_CHECKERS | chess.STATUS_IMPOSSIBLE_CHECK


def board(wk, wq, r1, r2, bk, stm):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    b.set_piece_at(wq, chess.Piece(chess.QUEEN, chess.WHITE))
    b.set_piece_at(r1, chess.Piece(chess.ROOK, chess.BLACK))
    b.set_piece_at(r2, chess.Piece(chess.ROOK, chess.BLACK))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    rng = random.Random(SEED)
    leg_diff = mov_diff = checked = unreach = 0
    ex = []
    t = time.time()
    for _ in range(N):
        idx = rng.randrange(NSTATES5)
        wk, wq, r1, r2, bk, stm = decode5(idx)
        if len({wk, wq, r1, r2, bk}) != 5:
            continue
        checked += 1
        b = board(wk, wq, r1, r2, bk, stm)
        status = b.status()
        valid_static = (status & ~UNREACH) == 0
        mine_legal = is_legal5(wk, wq, r1, r2, bk, stm)
        if status & UNREACH:
            unreach += 1
        if mine_legal != valid_static:
            leg_diff += 1
            if len(ex) < 10:
                ex.append(("LEGAL", b.fen(), "mine=%s theirs=%s status=%d"
                           % (mine_legal, valid_static, status)))
            continue
        if mine_legal and valid_static:
            mine = set(moves5(idx))
            theirs = set((m.from_square, m.to_square) for m in b.legal_moves)
            if mine != theirs:
                mov_diff += 1
                if len(ex) < 10:
                    ex.append(("MOVES", b.fen(), "mine-theirs=%s theirs-mine=%s"
                               % (sorted(mine - theirs), sorted(theirs - mine))))
    print("RULES REFEREE KQKRR vs python-chess:")
    print("  checked %d | legality diffs %d | move diffs %d | unreachable flagged %d | %.1fs"
          % (checked, leg_diff, mov_diff, unreach, time.time() - t))
    for e in ex:
        print("  DIFF", e)
    print("RULES REFEREE COMPLETE: %s"
          % ("PASS" if leg_diff == 0 and mov_diff == 0 else "FAIL"))
