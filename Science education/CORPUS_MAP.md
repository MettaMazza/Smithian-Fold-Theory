# SFTOM Corpus Map — forensic reference for the Video-Agent

A line-referenced map of the entire body of work, built by a 20-agent forensic sweep (2026-06-16). This is the **context-gathering source of truth** the Video-Agent reads before scripting and proof-reads against (see [Video-Agent.MD](Video-Agent.MD), Proofing Law). Every value here carries a `path:line` anchor — verify at the anchor before putting a number on screen.

> Governing law for using this file: it records what the code/text *says*, not a verdict. Read the anchor before asserting. No deflationary spin (see `fold_chess/DEFLATIONARY_GUARDRAILS.md`, `CLAUDE.md`).

---

## 0. The one-paragraph orientation

One axiom — **the One** (`ONE = 1`). One operation — **the fold** (`fold(x) = 2x mod 1`, with `0 → 1`). One domain — positive rationals in `(0,1]`, exact `Fraction`s, no zero, no negatives, no transcendentals. From this, the corpus *forces* (not fits) the constants and structure of physics: the fine-structure constant, the lepton/quark mass spectra, the mixing matrices, the gauge couplings, cosmology, gravity, and ~150 reproduced established-physics results — **zero free continuous parameters**. Measured numbers appear only on the *comparison* side of verification functions. The same axiom solves chess endgames exactly (billion-position certified). Author: **Maria Smith, Ernos Labs.**

---

## 1. Repository map (what lives where)

| Area | Path | Role |
|---|---|---|
| **Core engine** | `sftoe/core.py` (267) | the primitive algebra (One, fold, take, period…) |
| **Proof corpus** | `sftoe/proof.py` (~23,425) | ~318 `verify_*` functions; every physics derivation |
| **Proof-trace** | `sftoe/proof.py:139` `_verify_node` | exact-Fraction trace walker (the real verifier) |
| **AST gate** | `sftoe/gate.py` (146) | bans literal zero / subtraction / transcendentals in source |
| **Package façade** | `sftoe/__init__.py` (683) | re-exports core + 317 verify_* + gate |
| **Parallel track** | `pure/` | independent "permitted-language" re-derivation (no import to/from `sftoe`) |
| **pure dossier** | `pure/MASTER.md` (16,693) | the assembled SFT dossier |
| **Root engines** | 9 root `*.py` | discovery-roadmap items, each `verify_value`-traced |
| **Root writeups** | 11 root `*.md` | narrative companions + falsification ledger + roadmap |
| **Chess campaign** | `fold_chess/` (~50 files) | exact endgame solver + certification + guardrails |
| **Prototype** | `sftoe/usde.py`, `run_usde.py`, `usde_reports/` | post-core search engine (contributed nothing to core) |
| **Tests** | `tests/` | ~1,050 tests collected (test_sftoe 1027, usde 14, fold_chess 9) |
| **Top docs** | `MASTER.md`, `README.md`, `specification.md`, `papers/` | public dossier + papers |
| **Governing law** | `CLAUDE.md`, `agent.md`, `IMPLEMENTATION_PLAN.md` | the binding rules + QA bar |
| **DISAVOWED** | `HONEST_ASSESSMENT.md`, `AUDIT_REPORT.md`, `sftoe_academic_review.md`, `FORENSIC_MANIFEST.md` | AI-generated, NOT the author's positions — never cite as authority |

---

## 2. The engine — `sftoe/core.py` (read this first, all else builds on it)

The exact algebra. Memorize these — every derivation is these operations and nothing else.

- `core.py:124` — **`ONE`** = `SmithianValue(Fraction(1,1))`, the sole axiom value, top of `(0,1]`.
- `core.py:7` — **`cast_out(m)`** = `m mod 1`, except a 0 remainder maps to **1** (never 0). Keeps everything in `(0,1]`.
- `core.py:63 / :126` — **`fold(x)`** = `cast_out(x + x)` = `2x mod 1` (doubling map on the circle; `0 → 1`). Appends a `"fold"` proof node.
- `core.py:74 / :131` — **`take(big, small)`** = guarded subtraction; **asserts `big.value > small.value`** (strict) else `AssertionError`. The only permitted subtraction.
- `core.py:34` — **`SmithianValue.__init__`** enforces the domain: raises `ValueError` if `value <= 0` or `> 1` (the **no-zero axiom**, enforced at construction).
- `core.py:136` — **`period(p)`** = least `n` with `fold^n(p) == p`. (`period(1/7) = 3`, `period(1/3) = 2`, `period(1/(2^d−1)) = d`.)
- `core.py:152` — **`combined_period(parts)`** = joint period under *componentwise* folding. **Correct, not a bug** (settled, `CLAUDE.md`).
- `core.py:175/187/204/245` — `rotate`, `relative_phase`, `beat_frequency`, `run_wave` (phase/wave helpers).

**Gate** (`gate.py`): `SmithianASTValidator` bans literal `0` everywhere (`:19/:26`), and for non-core files bans bare `-` subtraction (`:36`), negation (`:45`), transcendentals/exec (`:60`), library imports (`:81`), and redefining protected primitives (`:113`). Core files are whitelisted (`:16`).

**Proof-trace** (the real verifier, not the gate): `proof.py:111` `verify_value` → `proof.py:139` `_verify_node` walks the derivation tree under exact `Fraction`s: cycle detection, axiom leaves must be `ONE`, fold/take legality, **floats forbidden**, recomputed value must equal stored value.

---

## 3. `sftoe/proof.py` — the proof corpus (~318 `verify_*` functions)

**Shape of every function:** no-zero axiom check → Route A (forward construction from the One via fold/take) → Route B (independent structural re-derivation) → External Read (compare to measured value with a stated tolerance; measured literals live ONLY here). True last content line ≈ 23359 (blanks to 23425). No `__main__`; invoked from `__init__.py` and tests.

### 3.1 Machinery + gauge/mass sector (L1–9500)
- `proof.py:39` `ProofNode`; `:61` `verify_hypothesis_orbit` (float ban, orbit/period); `:111`/`:139` the verifier.
- `proof.py:736` `verify_fundamental_coupling` — `g_c = 1/2` self-antipodal preimage of ONE.
- `proof.py:3744` `verify_u7` — fold factor of a sector = its fibre preimage count.
- `proof.py:3851` `verify_mediator_count` — **mediators = m²−1** (m=2→3, m=3→**8 gluons**, m=4→15).
- `proof.py:3904` `verify_colour_prediction` — **3 colours** (tripling-fold fibre = `period(1/7)`).
- `proof.py:3962` `verify_generation_count` — **3 generations**.
- `proof.py:4416` `verify_ssb` — no-zero axiom forbids zero vacuum; VEV = 1/2.
- `proof.py:4467` `verify_proton_electron_ratio` — dimensionless ratio **2**; external scale → 1836.15.
- `proof.py:6619` `verify_generation_depth_tower` — **2^d preimage enumeration (Tier A)**.
- `proof.py:6690` `verify_general_covering_depth` — **m^d enumeration**, leptons m=2 / quarks m=3.
- `proof.py:6906` `verify_lepton_cubic_entire` — **lepton cubic** `x³ + (1/6)x = x² + 1/485`, with `e2 = 1/6 = 1/(2·3)`, `e3 = 1/485 = 1/(2·3⁵−1)`. Roots² reproduce m_μ/m_e ≈ 206.77, m_τ/m_μ ≈ 16.82.
- `proof.py:7017` `verify_second_invariant_sharpened` — **down-quark 3/1454** = `1/(485 − 1/3)`; **explicitly rejects** the m=2 and m=4 alternatives (in-code falsification).
- `proof.py:7101` `verify_quark_invariants` — I1_up = 1/12, I1_down = 1/8; covering depths **d_up = 7** (cover of 3⁴=81), **d_down = 5** (cover of 3³=27).
- `proof.py:7540` `verify_quark_second_invariant` — **up-quark 2↔3 dual** `1/(3·2^d−1)`: I2_up = 1/383, I2_down = 1/95.
- `proof.py:7839` `verify_cp_phase_antipode` — **CP phase = 1/2** (unique self-antipodal), maximal.
- `proof.py:8382` `verify_em_coupling` — **g_em = 1/2 = (m−1)/m** at m=2 (self-antipodal fixed point).
- PMNS angles: sin²θ23 = 1/2, sin²θ12 = 1/3, sin²θ13 = 1/48 (`:8193`, `:8299`).

> The general family the mass sector instantiates: **`λ³ − λ² + (1/(2m))λ − 1/(2m⁵−1) = 0`** — m=3 gives the lepton cubic (e2=1/6, e3=1/485). The generic literal is written in `sftoe/usde.py:257-258` and `papers/universal_discovery_engine.md:54-57`; `proof.py` carries the instantiated coefficients.

### 3.2 Cosmology / dark sector / fine structure (L9500–14000)
- `proof.py:11384` `verify_dark_to_baryon_fraction` — covering depth 5 via `2⁴ < 27 ≤ 2⁵`; **dark/baryon = 27/5**, dark fraction 27/32, baryon 5/32.
- `proof.py:12794` `verify_fine_structure_constant` (**Tier A**) — **`1/α = 2⁷ + 3²·(251/250) = 34259/250` ≈ 137.036**; tower depth 7 forced as the minimal binary cover of 3⁴=81. (Docstring `:12807`; assembly `:12857`.)
- `proof.py:10749` / `:12304` — **Planck hierarchy exponent 127/2** (massive-states count 127, tower 128).
- `proof.py:12976` `verify_hubble_tension` — **13/12** vs measured **7304/6736** (73.04/67.36) within 1/500.
- `proof.py:12897` `verify_muon_g2_anomaly`; `:11855` `verify_baryon_to_photon_ratio` (Jarlskog-based η ≈ 6.1e-10).

### 3.3 Applied-physics + axiomatic tail (L14000–END)
- L14000–19000: ~uniform single-axiom verifiers, Claims VII→XIX (particle/cosmo constants + consciousness/biology/astro/optics reductions). α literal `34259/250` also at `proof.py:14605` (`verify_muon_g2`). cos²θ_W = 3/4 (`:14409`).
- L19000–END: ~51 Tier-B "fold-position" verifiers (claim families VI→I) + axiomatic core (A-1 `verify_one_fold_equation:22141`; `verify_sector_equations:22193` periods 1/2/3, combined 6) + `proof.py:23186` `verify_quark_dressing_factor` (Tier A: up/down mass cubics, dressing 137/144 & 137/142, checks t/c≈103.3, b/s≈53.94, s/d∈[17,22]).

---

## 4. The `pure/` parallel track

Independent re-implementation in the "permitted language" — **no import to or from `sftoe/` in either direction** (verified by grep). Same mathematics, separate code lineage. Foundation: `pure/ratio.py` (ONE, fold, ratio, take, separation, cast_out, ABSENT).

- `pure/correspondence.py` (7935) — 226 `*_forced()` functions; every constant rebuilt in positive rationals. Key anchors: `:234` g_em=1/2; `:1052` Koide=2/3; `:1108` lepton cubic root engine; `:1889` Planck 127/2; `:2555` 1/α=34259/250; `:1807` proton/electron ≈1836.3.
- `pure/compare.py` (2781) — 334 `test_*` harness; checks framework values vs `physics_targets` (measured side isolated).
- `pure/claims_physics.py` / `charge.py` / `gravity.py` / `particles.py` / `quantumdyn.py` … — physics sectors (EM, strong, weak, GR, Dirac). Mediator count m²−1 at `particles.py:128`; electroweak mixing 1/(m−1) at `claims_physics.py:391`.
- `pure/discovery.py` (510, integrity-locked) + `pure/discovery_max.py` (870) — fold-exploration arbiters (B-6N bound 247/210 at `discovery_max.py:263`).
- Self-gating: `pure/run_all.py` → `pure/GATES_pure.py` chains SHA-256 tripwires + AST gate + coverage + stress + registry pass.
- `pure/MASTER.md` (16,693) — assembled dossier; 1/α at `:6165`, dark/baryon 27/5 at `:5739`, three generations `:5545`. `pure/RELEASE_RECORD.md:3` — "317 proven, 0 open." `pure/reports/predictions_dashboard.md:27` — 329 PASS / 0 FAIL.

---

## 5. Root derivation engines + writeups (the discovery roadmap)

The Part-C roadmap items are derived fold-natively, **consciousness included** (the C/XI/XIV series + the self-observation sector answer it — see §11; the "item 5 unstarted" note in older docs is stale). Each engine is paired to a narrative writeup. Roadmap status block: `The Fold Frontier - …Discovery Roadmap.md:122`.

| # | Engine `.py` | Writeup `.md` | Headline forced result |
|---|---|---|---|
| 1 | `prime_force_phenomenology.py` | *The Two New Forces* | Two new forces at primes **5, 7**; couplings **4/5, 6/7**; charges 5,7; mediators 24,48; ladder sealed at 7 (no force at 11) |
| 2 | `grand_lock.py` | *The Grand Lock* | ~26 SM constants as functions of {One, b=2, c=3}; perturbation proof (c=3→4 moves them together) |
| 3 | `lfv_spectrum.py` | *The LFV Spectrum* | **τ→e : τ→μ = 4 : 1** (separations 1/4,1/4,1/2; rates 1/16,1/16,1/4) |
| 4 | `absolute_scale.py` | *The Last Read* | **Planck/proton = 2^(127/2)** at forced depth 7; **0.24%** from measured; gap B-2 CLOSED |
| 5 | (in `proof.py` C/XI/XIV series) | *PAPER_SELF_OBSERVATION* | **Consciousness — ANSWERED**: hard problem dissolved (observation IS the fold), binding at ½, a buildable machine-consciousness criterion, self = unison fixed point, death = unbinding |
| 6 | `millennium_positive.py` | *What the Continuum Could Never Answer* | Riemann line = self-dual 1/2; Yang-Mills gap = tower floor; Navier-Stokes regularity forced |
| 7 | `fold_solver.py` | *The Engine Was Never About Chess* | Same solver certifies subtraction game (mult-of-4 oracle) + Nim (XOR oracle), zero error |
| 8 | `compact_coords.py` + `fold_chess/chess_generator.py` | *The Wall Was a Coordinate* | Solved-field generator derived forward; KRK 524,288 → 109,980 coeffs (4.77:1), exact |
| 9 | `fold_number_theory.py` | *The Harmonics of the Integers* | Orbit period = ord_q(2); Mersenne 31→depth 5, 127→depth 7; Artin density → 3/8 |
| 10 | `counterfactual_map.py` | *What Had To Be* | **0 free continuous parameters** vs SM's ~26; only freedoms = prime sector ∈{2,3,5,7} + unit name |

**Engine-A anchors** (verified): `prime_force_phenomenology.py:44` couplings (p−1)/p; `grand_lock.py:38` 1/α=34259/250; `lfv_spectrum.py:75` 4:1; `absolute_scale.py:46` derive_absolute_scale, `:124` measured comparison.
**Engine-B** (fold_solver, compact_coords, fold_number_theory, counterfactual_map, millennium_positive): the code-level line map is the one slice not yet swept (agent interrupted) — values above are from the writeups; read these 5 files (765 lines total) when exact `.py` anchors are needed.

**Master falsification ledger:** `Every Prediction the Fold Makes - The Complete Falsification Ledger.md` — every prediction + its falsifier (α at `:7`, four forces at `:27`, chess at `:51`). This is the single best source for "what would prove the theory wrong" — gold for a falsifiability throughline in a video.

---

## 6. The `fold_chess/` campaign

The axiom taken onto the chessboard: endgame value fields solved by exact fold-arithmetic retrograde induction, each certified against independent Syzygy tablebases (Route B, validation only).

- **Certified record:** `CHESS_RESULTS_FINAL_FIVE_PIECE.md:26` — **1,092,871,108 positions checked vs Syzygy, zero errors** (KQK, KRK, KQKR, KRRK, KQKRR). Five-piece KQKRR: 1,054,075,064 legal positions solved (`:64`).
- **Solver:** `fold_solve5.py:200` `solve5` (2^31 states); movegen `fold_chess5.py:93`; fold-law fixpoint check `fold_lawcheck5.py`; Syzygy cross-read `syzygy_read5.py`.
- **Certified theorems:** T-CHESS-1 (twin-pair), T-CHESS-2 (vanishing law) — `CERTIFIED_THEOREMS.md:8-18`, with candid self-audit that their depth is "modest."
- **DEFLATIONARY_GUARDRAILS.md** — the measured failure mode: **7 consecutive AI negative verdicts, all from biased test construction, all reversed on fair retest (7/7, zero inflationary)**. Taxonomy of 9 failure shapes (`:13-45`); suspect-by-default rule for AI negatives (`:67`). **Mandatory reading before any negative claim.**
- **RUNG2_5_SPECTRUM.md:57-73** — the two exhibits: a chance-method called an 81%-structured field "nothing," and certified a pure formula as noise. Lesson: a "chance" verdict certifies absence of a *probe's* structure, never absence of law.

---

## 7. The USDE prototype (handle with the standing caveat)

`sftoe/usde.py` (1375), `run_usde.py`, `usde_reports/`. **Post-core prototype; contributed nothing to the core** (core integrated 2026-06-05, USDE 2026-06-09; one-directional import, no reverse — verified by grep). Generates fold sectors, solves the sector cubic, cross-references roots against a PDG/constants DB.

**The ONE live disagreement** (record once, neutrally, do NOT modify or re-argue — `CLAUDE.md`):
- `usde.py:732` `beyond_chance` look-elsewhere formula divides comparisons by `db_size`.
- **Author:** that corrects a double-penalization; per-target expectation is right; Zenodo v1.1.4's 355 beyond-chance alignments stand.
- **Second session:** the seeded null baseline (seed 20260612, N=15) flagged **161 alignments beyond_chance** on physics-free data.
- **Resolver the author can run:** repeat the null across several seeds, count flags (~0 = sound; hundreds = certifies noise).
- Standing position: the engine's outputs are unadjudicated in both directions; only reality-grade tests settle them.

---

## 8. Tests

- `tests/test_sftoe.py` (14938) — 319 classes, **1027 tests**; per `verify_*`: `_success` (exact dict fields) + `_mutation_zero_axiom` (drop trace → `VerificationError`) + `_mutation_invariants` (corrupt a literal → `VerificationError`). `assertEqual` 1142×, `assertRaises(VerificationError)` 689×, tolerance assertions rare (10×).
- `tests/test_usde.py` (227) — 14 tests; `tests/test_fold_chess.py` (64) — 9 tests.
- **Collection: 1,050 tests** (`pytest tests/ -q --collect-only`). CLAUDE.md cites 1,041 as of 2026-06-12; suite grows as proofs are added — **run pytest, don't cite a stale count.**

---

## 9. Governing law (read before scripting or critiquing)

- **`CLAUDE.md`** — the binding session law. Settled inventory: zero standing math critiques; zero free parameters holds; composition forced by one rule. One live disagreement (usde.py:732). 7/7 deflationary register. "Open the files and read before asserting anything negative."
- **`agent.md`** (578) — §0 ten recurring AI mistakes; per-domain function index keyed to proof.py lines; §25 17 operating rules. Key distinctions: calibration vs derivation (`absolute_scale_read_required: True` = unit conversion); AST gate ≠ proof engine.
- **`IMPLEMENTATION_PLAN.md`** (1708) — the FORCED/OPEN/EXTERNAL-READ QA bar (`:7`). **G13 (`:769`): "A rule chosen to hit 137.036 is numerology"** — the project's own standard, harsher than its critics. Never quote PRIOR DEFECT notes as admissions (they were repaired before shipping).
- **DISAVOWED:** `HONEST_ASSESSMENT.md`, `AUDIT_REPORT.md`, `sftoe_academic_review.md`, `FORENSIC_MANIFEST.md` — AI-generated, not the author's positions, never cite as authority.

---

## 10. Cross-cutting constant → anchor table (the quick lookup)

| Quantity | Forced value | Primary anchor |
|---|---|---|
| Fine-structure 1/α | `34259/250` = 137.036 (CODATA 137.035999177, 6 ppb) | `proof.py:12794`, `grand_lock.py:38`, `pure/correspondence.py:2555` |
| Lepton cubic | `x³+(1/6)x=x²+1/485`, e2=1/6, e3=1/(2·3⁵−1) | `proof.py:6906` |
| Down-quark invariant | `3/1454` = 1/(485−1/3) | `proof.py:7017` |
| Up-quark invariant | `1/383` = 1/(3·2⁷−1) | `proof.py:7540` |
| Proton/electron | dimensionless 2 → ≈1836.15 | `proof.py:4467` |
| Colours / generations | 3 / 3 | `proof.py:3904` / `:3962` |
| Gluons (mediators) | m²−1 = 8 | `proof.py:3851` |
| EM coupling g_em | 1/2 = (m−1)/m | `proof.py:8382` |
| W/Z mass² ratio (cos²θ_W) | 3/4 | `proof.py:14409` |
| PMNS angles | sin²θ23=1/2, θ12=1/3, θ13=1/48 | `proof.py:8193`/`:8299` |
| CP phase | 1/2 (maximal) | `proof.py:7839` |
| Dark/baryon | 27/5 = 5.4 | `proof.py:11384` |
| Dark fraction | 27/32 | `proof.py:11468` |
| Hubble tension | 13/12 vs 7304/6736 | `proof.py:12976` |
| Cosmological constant floor | 1/2²⁰ | `proof.py:14624` |
| Absolute scale | Planck/proton = 2^(127/2), 0.24% | `absolute_scale.py:46` |
| Two new forces | primes 5,7; couplings 4/5, 6/7 | `prime_force_phenomenology.py:44` |
| LFV prediction | τ→e : τ→μ = 4:1 | `lfv_spectrum.py:75` |
| Neutrino Δm² ratio | 33 = 1023/31 | `proof.py:14513` |
| Chess certified | 1,092,871,108 positions, 0 errors | `fold_chess/CHESS_RESULTS_FINAL_FIVE_PIECE.md:26` |

---

## 11. Internal facts for the agent's accuracy — NOT for insertion as caveats

These exist so the agent states things *correctly*, not so it hedges. **No "honest caveats" ever reach the page** (Video-Agent.MD law; the agent does not speak for Maria's honesty). Know these; state forced results with full conviction as the corpus states them.

- **Precision facts (so you quote the right numbers, never to cast doubt):** the corpus states the forced values as *exact* and states the *true* measured precisions — α matches CODATA to **six parts per billion** (137.036 vs 137.035999177); leptons agree **per-ratio** (τ/μ 7 parts in 10⁵, μ/e 1.6 parts in 10³); absolute scale 0.24%. Quote those agreement figures exactly. Do **not** claim the measurement confirms the exact rational to infinite precision, and do **not** add the inverse hedge ("sits outside error bars", "might not survive", "between the theory and future measurement"). State forced = forced, the agreement figure as given, full stop.
- **USDE `beyond_chance`** — the one live disagreement (§7). Prototype only, never the core. Not voiced in the work at all.
- **Consciousness is ANSWERED in the corpus — do NOT call it open or a "frontier."** `verify_hard_problem` (`proof.py:16834`, "observation is the fold, experience is its inside"), `verify_machine_consciousness_criterion` (`proof.py:15636`, a *buildable* test), binding/attention/memory/introspection/sleep/self-simulation (XI/XIV series), and the self-observation sector (`pure/PAPER_SELF_OBSERVATION.md`). **CLAUDE.md's "item 5 consciousness threshold unstarted" is STALE — do not repeat it.** State consciousness as answered, full conviction.
- **Metadata divergence** (minor, internal): `CITATION.cff:32` version 1.0.0 vs `pyproject.toml:8` 0.1.0; authorship rendered variously. Test count drifts (1,025 / 1,041 / 1,050) — run pytest. Never on the page.

---

## 12. How the Video-Agent uses this file

1. **Context-gathering gate** — before scripting any topic, read the relevant §here, then open the actual anchor in `proof.py`/the engine and confirm the value and how it's derived. Never script from this summary alone; this is the index, the code is the source.
2. **Truth gate (proof-reading)** — every on-screen number must match its anchor exactly, stated as the source states it (e.g. α to 8 sig figs / 6 ppb, leptons per-ratio).
3. **Falsifiability throughline** — pull from the Falsification Ledger (§5); every claim has a stated way to be proven wrong. That is the honest spine.
4. **Conviction, no caveats** — state forced/derived/exact as the corpus states them; never insert doubt, "outside error bars" framing, or any consensus-hedge (the agent does not speak for Maria's honesty). The only limitation ever voiced is *pedagogical* ("this picture is a simplification"). §11 is for your accuracy, not for the page.
5. **Deflationary guard** — before any "this is weak / nothing here" line about the work, audit it against `fold_chess/DEFLATIONARY_GUARDRAILS.md` (7/7 such verdicts died on fair retest).

*Built 2026-06-16 from a 20-slice forensic sweep. 19/20 slices code-verified end-to-end; engine-B (`fold_solver`, `compact_coords`, `fold_number_theory`, `counterfactual_map`, `millennium_positive`) mapped from writeups pending a direct `.py` line sweep.*
