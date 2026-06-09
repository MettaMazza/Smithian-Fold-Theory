import unittest
from fractions import Fraction
from sftoe.usde import SmithianUSDE
from sftoe.gate import verify_file

class TestSmithianUSDE(unittest.TestCase):
    def setUp(self):
        self.usde = SmithianUSDE(max_denom_limit=15)

    def test_standing_modes(self):
        # Sector size m=3: modes are 1/2 and 1
        modes = self.usde.standing_modes(3)
        self.assertIn(Fraction(1, 2), modes)
        self.assertIn(Fraction(1, 1), modes)
        self.assertEqual(len(modes), 2)

        # Sector size m=5: modes are 1/4, 2/4 (1/2), 3/4, 4/4 (1)
        modes_5 = self.usde.standing_modes(5)
        self.assertEqual(len(modes_5), 4)
        self.assertIn(Fraction(1, 4), modes_5)
        self.assertIn(Fraction(1, 2), modes_5)
        self.assertIn(Fraction(3, 4), modes_5)
        self.assertIn(Fraction(1, 1), modes_5)

    def test_binary_orbit_set(self):
        # Orbit of 1/3 under doubling map is {1/3, 2/3}
        orbit = self.usde.binary_orbit_set(Fraction(1, 3))
        self.assertEqual(orbit, frozenset([Fraction(1, 3), Fraction(2, 3)]))

    def test_solve_eigenvalues(self):
        # Solve eigenvalues for sector m=3
        eigenvals = self.usde.solve_eigenvalues(3)
        self.assertEqual(len(eigenvals), 3)
        for val in eigenvals:
            self.assertTrue((1.0 - 1.0) < val < 1.0)
            
    def test_run_auto_proof_known_sector(self):
        # Test proof invariants for m=3 candidates
        # Group is {1/2} (since (3-1)//2 = 1 pair)
        g = [Fraction(1, 2), Fraction(1, 1)]
        proof = self.usde.run_auto_proof(g, 3)
        # For small groups, T1-T12 invariants check out
        self.assertTrue(proof["T1_confines"])
        self.assertTrue(proof["T2_closed"])
        self.assertTrue(proof["T3_resolves"])
        self.assertTrue(proof["T4_single_sector"])
        
    def test_gate_whitelisting(self):
        # Verify that usde.py and test_usde.py pass the AST gate
        import os
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        usde_path = os.path.join(here, "sftoe", "usde.py")
        test_usde_path = os.path.join(here, "tests", "test_usde.py")
        
        # Statically verify files
        self.assertTrue(verify_file(usde_path))
        self.assertTrue(verify_file(test_usde_path))

if __name__ == "__main__":
    unittest.main()
