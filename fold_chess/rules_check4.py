"""EXTERNAL READ (rules referee) — phase 3a gate for fold_chess4.

Compares the 4-piece KQKR state model and move generation against
python-chess on a large seeded random sample BEFORE any solving happens:
  1. legality verdicts (mine vs board.is_valid()),
  2. the EXACT set of legal (from, to) moves for every mutually legal state.
External instrument; not subject to fold source conventions.
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess

from fold_chess4 import NSTATES4, decode4, is_legal4, moves4, BTM

SEED = 20260612


def board4(wk, wq, br, bk, stm):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    b.set_piece_at(wq, chess.Piece(chess.QUEEN, chess.WHITE))
    b.set_piece_at(br, chess.Piece(chess.ROOK, chess.BLACK))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b


def run(n_sample=300000):
    rng = random.Random(SEED)
    t = time.time()
    legality_diffs = move_diffs = both_legal = checked = 0
    examples = []
    for _ in range(n_sample):
        idx = rng.randrange(NSTATES4)
        wk, wq, br, bk, stm = decode4(idx)
        if len({wk, wq, br, bk}) != 4:
            continue
        checked += 1
        b = board4(wk, wq, br, bk, stm)
        mine_legal = is_legal4(wk, wq, br, bk, stm)
        theirs_legal = b.is_valid()
        if mine_legal != theirs_legal:
            legality_diffs += 1
            if len(examples) < 8:
                examples.append(("LEGALITY", b.fen(), mine_legal, theirs_legal))
            continue
        if not mine_legal:
            continue
        both_legal += 1
        mine_moves = sorted(moves4(idx))
        theirs_moves = sorted((m.from_square, m.to_square) for m in b.legal_moves)
        if mine_moves != theirs_moves:
            move_diffs += 1
            if len(examples) < 8:
                missing = [m for m in theirs_moves if m not in mine_moves]
                extra = [m for m in mine_moves if m not in theirs_moves]
                examples.append(("MOVES", b.fen(), missing, extra))
    print("RULES REFEREE — KQKR movegen vs python-chess:")
    print("  sampled states (distinct squares): %d" % checked)
    print("  legality disagreements:            %d" % legality_diffs)
    print("  mutually legal states compared:    %d" % both_legal)
    print("  move-set disagreements:            %d" % move_diffs)
    print("  elapsed: %.1fs" % (time.time() - t))
    for e in examples:
        print("   ", e)
    return legality_diffs + move_diffs


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
    sys.exit(1 if run(n) else 0)
