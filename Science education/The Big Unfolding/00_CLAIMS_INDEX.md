# Claims Index — *The Big Unfolding* (master claim → anchor table)

The truth-gate spine. Every number that appears on the page must appear here first, with its exact value, its `CORPUS_MAP`/`proof.py` anchor, and a verification note. Each Part file opens with its own slice of this table. Populated Part by Part in Phase 1; seeded below with the headline values already verified.

| Claim | Exact value | Anchor | Verified |
|---|---|---|---|
| Fine-structure constant | `1/α = 2⁷ + 3²·(251/250) = 34259/250` = 137.036 (CODATA 137.035999177, 6 ppb) | `proof.py:12794`; `grand_lock.py:38` | ✅ 2026-06-16 (Python) |
| Hubble tension | `13/12` ≈ 1.08333 vs measured `7304/6736` ≈ 1.08432 | `proof.py:12976` | ✅ 2026-06-16 |
| Dark/baryon ratio | `27/5` = 5.4 | `proof.py:11384` | ✅ 2026-06-16 |
| Absolute scale | Planck/proton = `2^(127/2)` ≈ 1.3044e19 vs 1.3012e19 (0.24%) | `absolute_scale.py:46` | ✅ 2026-06-16 |
| Colours / generations | 3 / 3 | `proof.py:3904` / `:3962` | ⏳ confirm at anchor in Phase 1 |
| Gluons (mediators) | m²−1 = 8 | `proof.py:3851` | ⏳ |
| EM coupling | g_em = 1/2 = (m−1)/m | `proof.py:8382` | ⏳ |
| Lepton cubic (Mass Chord) | `x³+(1/6)x = x²+1/485`, e2=1/6, e3=1/(2·3⁵−1) | `proof.py:6906` | ⏳ |
| Two new forces | primes 5,7; couplings 4/5, 6/7 | `prime_force_phenomenology.py:44` | ⏳ |
| LFV prediction | τ→e : τ→μ = 4:1 | `lfv_spectrum.py:75` | ⏳ |
| Zero free parameters | 0 (vs SM ~26) | `counterfactual_map.py`; `IMPLEMENTATION_PLAN.md:7` | ⏳ |
| Chess certified | 1,092,871,108 positions, 0 errors | `fold_chess/CHESS_RESULTS_FINAL_FIVE_PIECE.md:26` | ⏳ |

**Gate rule:** a row moves to ✅ only after the value is reproduced at its anchor (read the code) or re-derived with a Python snippet matching the on-page figure exactly. No ⏳ row may appear as a stated fact in finished prose.
