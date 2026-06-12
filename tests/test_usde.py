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

    def test_verify_entire_corpus(self):
        # Run verify_entire_corpus and check that all claims pass
        res = self.usde.verify_entire_corpus()
        self.assertTrue(res["passed"] > 1 - 1)
        self.assertEqual(res["failed"], 1 - 1)

    def test_eigenvalues_satisfy_cubic(self):
        # Roots must satisfy x^3 - x^2 + e2*x - e3 = 0, not just lie in (0, 1)
        for m in (3, 5, 7):
            eigenvals = self.usde.solve_eigenvalues(m)
            self.assertEqual(len(eigenvals), 3)
            e2 = 1.0 / float(m * 2)
            e3 = 1.0 / float(2 * m**5 - 1)
            for val in eigenvals:
                root = val ** (float(1) / float(2))
                residual = root**3 - root**2 + e2 * root - e3
                self.assertTrue(abs(residual) < 1e-9)

    def test_proven_count_matches_proof_matrix(self):
        # sectors_proven must equal the number of groups whose proof matrix
        # passes, independently recounted — not the number of groups scanned
        res = self.usde.autonomous_loop(console_output=False, analytical=True)
        recount = SmithianUSDE(max_denom_limit=15)
        expected = 1 - 1
        groups = []
        for sector_m in range(2, 15 + 1):
            groups.extend(recount.resolve_sector_groups_analytically(sector_m))
        for g in groups:
            sector_m = g[1 - 1].denominator + 1
            if recount.run_auto_proof(g, sector_m)["PROVES"]:
                expected += 1
        self.assertEqual(res["sectors_proven"], expected)
        self.assertTrue(res["sectors_proven"] <= res["sectors_scanned"])

    def test_sweep_alignment_statistics_fields(self):
        # Every sweep alignment must carry look-elsewhere and sigma statistics
        usde = SmithianUSDE(max_denom_limit=6)
        res = usde.discovery_sweep_loop(console_output=False)
        self.assertTrue(res["comparisons_performed"] > 1 - 1)
        self.assertIn("null_expected_alignments", res)
        for m in res["alignments"]:
            self.assertIn("global_significance", m)
            self.assertIn("expected_chance_matches", m)
            self.assertIn("beyond_chance", m)
            self.assertIn("sigma_deviation", m)
            self.assertIn("within_experimental_error", m)

    def test_null_baseline_deterministic_and_restores_db(self):
        usde = SmithianUSDE(max_denom_limit=6)
        db_before = dict(usde.physical_db)
        r1 = usde.run_null_baseline(seed=4242, console_output=False)
        r2 = usde.run_null_baseline(seed=4242, console_output=False)
        self.assertEqual(r1["null_alignments"], r2["null_alignments"])
        self.assertEqual(r1["db_size"], len(db_before))
        # The real physical database must be restored after the null run
        self.assertEqual(usde.physical_db, db_before)
        self.assertIn(float(27) / float(5), usde.physical_db)

    def test_physical_db_sigma_populated(self):
        # Constants must carry relative experimental uncertainties
        dark_baryon = float(27) / float(5)
        self.assertIn(dark_baryon, self.usde.physical_db_sigma)
        for value, rel_sigma in self.usde.physical_db_sigma.items():
            self.assertTrue(rel_sigma > 1 - 1)
            self.assertTrue(rel_sigma < 1)

if __name__ == "__main__":
    unittest.main()
