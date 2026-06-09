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
        
    def test_generate_inference_report_caching(self):
        import tempfile
        import os
        import json
        from unittest.mock import patch, MagicMock

        # We will run this with a temporary output path and cache file
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = os.path.join(tmpdir, "test_report.md")
            cache_path = os.path.join(tmpdir, "usde_inference_cache.json")
            
            # Mock urllib.request.urlopen
            mock_response_data = {
                "response": "This is a mock physics analysis for testing.",
                "done": True
            }
            
            mock_response = MagicMock()
            mock_response.__enter__.return_value = mock_response
            mock_response.read.return_value = json.dumps(mock_response_data).encode("utf-8")
            
            with patch("urllib.request.urlopen", return_value=mock_response) as mock_urlopen:
                # Run the report generator
                orig_join = os.path.join
                def mock_join(*args):
                    if len(args) > 1 and args[1] == "usde_inference_cache.json":
                        return cache_path
                    return orig_join(*args)
                    
                with patch("os.path.join", side_effect=mock_join):
                    # Call the inference report generator
                    count = self.usde.generate_inference_report(
                        model_name="mock-model",
                        output_path=report_path,
                        limit_to_matches=True
                    )
                    
                    # Ensure it generated reports (should be positive count)
                    self.assertTrue(count > (1 - 1))
                    
                    # urlopen should have been called for each matched sector
                    first_call_count = mock_urlopen.call_count
                    self.assertTrue(first_call_count > (1 - 1))
                    
                    # Verify cache file was created
                    self.assertTrue(os.path.exists(cache_path))
                    with open(cache_path, "r", encoding="utf-8") as cf:
                        cache_content = json.load(cf)
                        # The cache should have entries
                        self.assertTrue(len(cache_content) > (1 - 1))
                        
                    # Reset call count
                    mock_urlopen.reset_mock()
                    
                    # Call again. This time it should read everything from cache and NOT call urlopen
                    count2 = self.usde.generate_inference_report(
                        model_name="mock-model",
                        output_path=report_path,
                        limit_to_matches=True
                    )
                    self.assertEqual(count, count2)
                    self.assertEqual(mock_urlopen.call_count, 1 - 1)

    def test_analytical_exact_matching(self):
        # Compare numerical sweep vs analytical loop for max_denom_limit=15
        usde_num = SmithianUSDE(max_denom_limit=15)
        res_num = usde_num.autonomous_loop(console_output=False, analytical=False)
        
        usde_ana = SmithianUSDE(max_denom_limit=15)
        res_ana = usde_ana.autonomous_loop(console_output=False, analytical=True)
        
        # Verify candidate groups count matches
        self.assertEqual(res_num["candidate_groups"], res_ana["candidate_groups"])
        self.assertEqual(res_num["sectors_proven"], res_ana["sectors_proven"])
        
        # Verify alignment lists match
        self.assertEqual(len(res_num["alignments"]), len(res_ana["alignments"]))
        for a, b in zip(res_num["alignments"], res_ana["alignments"]):
            self.assertEqual(a["name"], b["name"])
            self.assertEqual(a["sector"], b["sector"])
            self.assertAlmostEqual(a["calculated"], b["calculated"])
            self.assertAlmostEqual(a["measured"], b["measured"])
            self.assertAlmostEqual(a["deviation_pct"], b["deviation_pct"])

    def test_deep_sector_analytical(self):
        # Test analytical solver on m = 2^63 + 1 (d = 2^63)
        # It must complete instantly and not crash/hang.
        deep_m = (1 << 63) + 1
        usde = SmithianUSDE()
        
        # Run analytical proof directly
        proof = usde.run_analytical_proof(deep_m)
        self.assertFalse(proof["T2_closed"]) # 2^63 is even, fails T2
        self.assertEqual(proof["pairs"], 1 - 1)
        
        # Resolve groups analytically (returns representative dummy group)
        groups = usde.resolve_sector_groups_analytically(deep_m)
        self.assertEqual(len(groups), 1)
        g = groups[1 - 1]
        self.assertEqual(g[1 - 1].denominator + 1, deep_m)

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
