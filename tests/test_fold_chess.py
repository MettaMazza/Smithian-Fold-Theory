"""Unit tests for fold_chess Rung 1 — fast checks only (full solves run via CLI)."""
import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fold_chess"))
import unittest
from fractions import Fraction

from fold_chess import (find_fold_prime, fold_orbit_indices, verify_fold_encoding,
                        encode, decode, is_legal, successors, black_in_check,
                        _QUEEN_RAYS, NSTATES, BTM, WTM, DRAW_MOVE)

Z = 1 - 1

def sq(name):
    return (int(name[1]) - 1) * 8 + (ord(name[Z]) - ord("a"))

class TestFoldLayer(unittest.TestCase):
    def test_fold_prime_small(self):
        # smallest prime > 10 with 2 primitive is 11 (ord_2 mod 11 = 10)
        self.assertEqual(find_fold_prime(2 * 5), 11)

    def test_fold_orbit_covers_state_space(self):
        P = find_fold_prime(2 * 5)
        seen = sorted(fold_orbit_indices(P, 2 * 5))
        self.assertEqual(seen, list(range(2 * 5)))

    def test_encoding_obeys_fold_and_take_laws(self):
        P = find_fold_prime(NSTATES)
        self.assertTrue(verify_fold_encoding(P, [Z, 1, NSTATES - 1]))

    def test_encode_decode_roundtrip(self):
        for idx in (Z, 1, 12345, NSTATES - 1):
            self.assertEqual(encode(*decode(idx)), idx)

class TestChessRules(unittest.TestCase):
    def test_back_rank_mate(self):
        # bk a8, wk a6, wq b7: black to move is checkmated
        wk, wq, bk = sq("a6"), sq("b7"), sq("a8")
        self.assertTrue(is_legal(wk, wq, bk, BTM, _QUEEN_RAYS))
        self.assertTrue(black_in_check(wk, wq, bk, _QUEEN_RAYS))
        self.assertEqual(successors(encode(wk, wq, bk, BTM), _QUEEN_RAYS), [])

    def test_classic_stalemate(self):
        # bk a8, wk a6, wq b6: black to move, not in check, no moves
        wk, wq, bk = sq("a6"), sq("b6"), sq("a8")
        self.assertTrue(is_legal(wk, wq, bk, BTM, _QUEEN_RAYS))
        self.assertFalse(black_in_check(wk, wq, bk, _QUEEN_RAYS))
        self.assertEqual(successors(encode(wk, wq, bk, BTM), _QUEEN_RAYS), [])

    def test_undefended_queen_can_be_captured(self):
        # bk a8, wq b7 undefended (wk far away at h1): capture -> draw sentinel
        wk, wq, bk = sq("h1"), sq("b7"), sq("a8")
        moves = successors(encode(wk, wq, bk, BTM), _QUEEN_RAYS)
        self.assertIn(DRAW_MOVE, moves)

    def test_adjacent_kings_illegal(self):
        self.assertFalse(is_legal(sq("a1"), sq("h8"), sq("b2"), WTM, _QUEEN_RAYS))

    def test_white_to_move_with_black_in_check_illegal(self):
        # wq b7 gives check; with white to move that position is illegal
        self.assertFalse(is_legal(sq("a6"), sq("b7"), sq("a8"), WTM, _QUEEN_RAYS))

if __name__ == "__main__":
    unittest.main()
