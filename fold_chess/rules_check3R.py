"""Rules referee for KRRRK movegen vs python-chess. Three identical rooks give
double/triple-check positions that are statically valid but unreachable; we
compare static legality (status minus the unreachability flags) and full move
sets, requiring zero diffs before the solver runs."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chess
from fold_chess3R import NSTATES_3R, decode3R, is_legal3R, moves3R, BTM

UNREACH = chess.STATUS_TOO_MANY_CHECKERS | chess.STATUS_IMPOSSIBLE_CHECK


def board(wk, r1, r2, r3, bk, stm):
    b = chess.Board(None)
    b.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
    for r in (r1, r2, r3):
        b.set_piece_at(r, chess.Piece(chess.ROOK, chess.WHITE))
    b.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
    b.turn = chess.WHITE if stm != BTM else chess.BLACK
    return b


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    rng = random.Random(20260612)
    leg = mov = checked = unreach = 0
    ex = []
    t = time.time()
    for _ in range(N):
        idx = rng.randrange(NSTATES_3R)
        wk, r1, r2, r3, bk, stm = decode3R(idx)
        if len({wk, r1, r2, r3, bk}) != 5:
            continue
        checked += 1
        b = board(wk, r1, r2, r3, bk, stm)
        st = b.status()
        valid = (st & ~UNREACH) == 0
        mine = is_legal3R(wk, r1, r2, r3, bk, stm)
        if st & UNREACH:
            unreach += 1
        if mine != valid:
            leg += 1
            if len(ex) < 8:
                ex.append(("LEGAL", b.fen(), "mine=%s theirs=%s st=%d" % (mine, valid, st)))
            continue
        if mine and valid:
            a = set(moves3R(idx))
            c = set((m.from_square, m.to_square) for m in b.legal_moves)
            if a != c:
                mov += 1
                if len(ex) < 8:
                    ex.append(("MOVES", b.fen(), "mine-theirs=%s theirs-mine=%s"
                               % (sorted(a - c), sorted(c - a))))
    print("RULES REFEREE KRRRK: checked %d | legality diffs %d | move diffs %d | unreachable %d | %.1fs"
          % (checked, leg, mov, unreach, time.time() - t))
    for e in ex:
        print("  DIFF", e)
    print("RULES REFEREE KRRRK: %s" % ("PASS" if leg == 0 and mov == 0 else "FAIL"))
