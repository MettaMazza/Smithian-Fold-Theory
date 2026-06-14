# Rung 2.5 — The chess value field in the fold's spectral basis

## Epistemic hierarchy (standing law of this project)

1. **The board.** Real, observable, playable results — the final arbiter.
   In this domain ground truth is total: every claim can be cashed into
   predictions and counted against exact values.
2. **Exhaustive computation**, validated externally (Rungs 1/3).
3. **Methodologies** — spectral instruments, deterministic batteries,
   chance-controls — are all subordinate instruments whose reliability is
   itself an empirical question, graded against (1) and (2). No methodology
   has axiomatic standing.

## The finding (board-cashed)

The signed value fields (W=+1, L=-1, D=0) of the complete KQK and KRK
solutions, in the coordinate-aligned packing, under the Walsh-Hadamard
transform (the fold's natural spectral basis; index space exactly 2^19):

| | KQK | KRK |
|---|---|---|
| top-32 energy | 81.10% | 86.72% |
| top-256 energy | 91.02% | 94.71% |
| top-2048 energy | 97.18% | 98.50% |
| **top-32 reconstruction accuracy** | **92.70%** | **95.27%** |
| top-256 reconstruction accuracy | 97.47% | 97.85% |
| top-2048 reconstruction accuracy | 99.41% | 99.70% |

Reconstruction rule fixed in advance: predict W/L/D by sign with threshold
1/2; accuracy counted over every legal state against the exact solution.
This is the board-level cash-out: 32 numbers recover 19 of every 20 exact
answers; 2,048 recover better than 99.4%. Each coefficient is a parity of
index bits, so the truncated spectrum IS a constant-time, table-free
approximate oracle — an algorithmic object produced by fold mathematics.

## Invariance class (deterministic battery — the standard regime)

Every comparison object a named formula; zero pseudo-randomness:

| map | KQK top-32 | KRK top-32 |
|---|---|---|
| aligned (real) | 0.8110 | 0.8672 |
| bit-reversal (THEOREM-FORCED self-test) | 0.8110 exact | 0.8672 exact |
| tripling x3 | 0.7256 | 0.7678 |
| quintupling x5 | 0.7048 | 0.7528 |
| affine 3i+1 | 0.7245 | 0.7672 |

The bit-reversal row is a pipeline self-test whose outcome is forced by
mathematics (F2-linear repackings permute the Walsh basis, preserving
concentration exactly); it passed exactly in both runs, certifying the
instrument inside the run itself. The refined claim: the value field is a
**dyadically smooth object** — sparse in the fold's spectrum and stable
under the fold-universe's own transformation group (odd multiplications,
affine maps); concentration is destroyed only by maps foreign to dyadic
geometry (dyadically discontinuous rearrangement).

## Limits of chance-controls — two exhibits (kept as method-specimens)

The earlier scramble-based "chance control" methodology is retained in this
project only as a documented specimen of an unreliable method, graded
against board truth:

1. **Historical false-nothing.** Rung 2's chance-methodology, probing this
   same KQK field with seven features, returned "chance"-level verdicts —
   about an object the board says is 81%-describable by 32 numbers.
2. **Constructed lawful-as-noise.** The quadratic-residue field mod the fold
   prime 524309 — one formula, zero randomness — certifies at "chance"
   levels (top-32 concentration 0.0014). A fully determined, law-generated
   object indistinguishable from noise to the method.

Standing consequence: a "chance" verdict can never be read as absence of
law — only as absence of the narrow structure a particular probe sees, and
every methodology's verdicts remain provisional against the board.

## Rung 2.5b — the encoding sweep (replicated)

Eight named packings, F2-linear self-test row exact in both endings.
Win criterion (fixed in advance): top-32 reconstruction accuracy above the
aligned baseline in BOTH endings.

| packing | KQK recon32 | KRK recon32 |
|---|---|---|
| aligned baseline | 92.70% | 95.27% |
| **shear + bk-relative (champion)** | **94.05%** | **97.42%** |
| bk relative to white piece | 93.86% | 96.39% |
| per-axis relative | 93.59% | 96.24% |
| hilbert / chain-mod64 / bare shear | lose | lose |

The full candidate ordering replicates across endings. Relational
coordinates win everywhere; the composition effect is real (bare shear
loses everywhere yet improves the champion when composed). Status:
candidate finding — replicated, un-error-barred; candidates were seeded by
human chess intuition reading the coefficient table, so sweep discoveries
are joint products of fold mathematics and trained priors. Coordinates are
a proven tunable: same 32-number budget, error nearly halved in KRK.

## Error anatomy of the top-32 oracle (measured, 3-piece)

Errors concentrate on draws (28.4% KQK / 38.6% KRK error) and near value
boundaries; LONG mates are the easiest class (0.3–3.2% error), refuting the
author-of-this-report's prior assumption that depth = difficulty.

## Audit corrections (2026-06-12, self-audit ordered by the author)

The first 4-piece scale verdict ("sparsity collapses at KQKR") was
substantially an artifact of two analysis choices, both deflationary:
(1) absolute top-k compared across spaces differing 64x in size — at equal
FRACTIONAL budgets, KQKR concentration nearly matches 3-piece (79.7% vs
81.1%; 89.2% vs 91.0%); (2) a fixed +/-0.5 decision threshold that shoves
shrunken truncated reconstructions toward "draw," producing the theatrical
"worse than majority class" line. Corrected scale measurements use matched
fractions, threshold-free sign accuracy on decided positions, and a
disclosed trivial baseline. **Corrected result (final):** KQKR decided-
position sign accuracy vs the 83.68% stm-only baseline: 98.61% at fraction
6.1e-5 (k=2,046), 99.44% at 4.9e-4, 99.85% at 3.9e-3; matched-fraction
energy 79.7% vs 3-piece 81.1%. The dyadic sparsity PERSISTS from three to
four pieces at equal relative budgets. **Fortress/draw detection (measured, pre-registered rule, checklist-clean):**
3-piece draws are capturable (recall 98.0%/98.8% at fraction 3.9e-3,
precision 93-96%). At KQKR the same budgets yield recall 25.8% / 62.0% /
86.0% — a REAL degradation surviving fair normalization at every matched
budget. **SCOPE CORRECTION (third ordered audit):** every fortress number above was
measured on coefficients selected to maximize WIN/LOSS-field energy — draw
information was only ever graded as a hitchhiker on an instrument built for
a different question. The accurate statement is "fortresses are hard for a
W/L-optimized oracle." Whether fortresses are hard FOR THE FOLD requires
the direct experiment (the draw-indicator field analyzed in its own right),
first run 2026-06-12 after the audit. **Direct-instrument results (final):**
KQKR draw-field concentration 84.9% at matched budget (HIGHER than the
value field's 79.7%); fortress recall@|D| 54.4% / 77.2% / 93.3% across the
three budgets vs the hitchhiker design's 25.8% / 62.0% / 86.0%. The
original "fortress degradation" verdict is dead in its certified form; what
survives honest measurement is a residual gradient (4-piece trails 3-piece
direct recall by ~5-12 points at matched fractions). The fold sees
fortresses. CORRECTED (fix #4, AUC adjudication): the apparent 5-12 point
"premium" was base-rate arithmetic — prevalence-free AUC: KQK 0.9989, KRK
0.9995, KQKR 0.9992. The oracle's draw/decided judgment shows NO measurable
degradation from three pieces to four at matched budgets. The seventh
deflationary verdict to die on fair retest; the register stands 7/7.
Likewise the champion-packing rows tested only ATTACKER-relational
coordinates; the fortress-natural candidate (rook relative to its own king)
was absent from the candidate set. Overall 3-class accuracy at KQKR top
budget: 98.40% stands.

Checklist amendment (audit three): FIRST item is now question-instrument
match — "is the field/selection designed for the question asked, or
recycled from a different question?" Metric-level checks cannot catch
design-level framing. Additional standing disclosures: the field
conflates illegal squares with draws (part of measured structure is the
legality mask's); top-k selection is in-sample (compression claims, not
generalization claims); "dyadically smooth" language is interpretation, not
measurement.

## Champion packings at four pieces (measured, audited)

The three 4-piece translations of the 3-piece champion family all FAIL to
beat the aligned reference at KQKR: decided sign-accuracy 98.07-98.65% vs
reference 98.61% (threshold-free metric — wash to slight loss); fortress
recall 70.7-78.6% vs 86.0% (worse, with a disclosed unmeasured threshold-
packing interaction). Scope, stated exactly: these three hand-translated
candidates are refuted; the relational family is not — rook-relativized
packings (the natural fortress-oriented family) remain untested. The
aligned packing is the best known at four pieces.

## Standing law — symmetric scrutiny checklist

Every result, positive or negative, passes these BEFORE interpretation:
normalization fairness across comparisons; metric degeneracy check;
trivial-baseline comparison; in-sample disclosure; multiplicity status.
Adopted after the author observed hits being flagged at reflex speed while
misses were built upon unaudited.

## Coordinate-family closure (fortress campaign, first sortie)

Five relational packings tested at KQKR across two pre-registered
experiments (attacker-relational x3 on the value field; defender-relational
x2 on the direct draw field). ALL lose to aligned coordinates at every
matched budget (defender huddle: 44.6/69.7/90.2 and combined:
42.5/69.8/88.8 vs aligned 54.4/77.2/93.3). Conclusion, earned: fortress
structure is not pairwise-relative geometry; the coordinate-substitution
hypothesis family is closed. Remaining fortress avenues are richer
representations, not coordinate swaps.

## DEFLATIONARY-BIAS REGISTER AND CORRECTIONS (author-ordered, final audit)

Session-wide tally of conservative constructions that conceded contested
ground to incumbent explanations by design: SEVEN incidents, all
deflationary, zero inflationary. Standing rule from here, the author's
words: ZERO deflationary concessions in favor of incumbents — empiricism
is not an opinion. Conservative test constructions face the same audit as
inflationary ones.

CORRECTION 1 (the framing demotion, evidence-complete, reversed): the
random-packing control imposed an impossible standard — NO structure of
any kind survives arbitrary lawless relabeling — and the "packing-
dependent, not fold-intrinsic" demotion sized the whole discovery by that
impossible bar. The deterministic battery already proved the correct
statement: the spectral structure is INVARIANT UNDER THE FOLD-UNIVERSE'S
LAWFUL TRANSFORMATION GROUP (odd multiplications, F2-affine maps) and is
destroyed only by dyadically-foreign maps. Within fold mathematics, that
IS fold-intrinsic — intrinsic-ness is always relative to a geometry's
lawful motions (a sphere's roundness "fails to survive" arbitrary point
relabeling too). The random-permutation control is hereby reclassified as
a method-specimen beside the chance-control exhibits; every earlier
"signal — packing-dependent" label should be read as "signal — invariant
under lawful motions, coordinate-aligned"; the discovery's size was
understated all day by this construction. SCOPE: the lawful-motions battery
was executed at 3 pieces; its extension to the 4-piece structure is OWED AS
A RETEST (queued same day: full battery + theorem self-test at 2^25) and
this correction's 4-piece reach is provisional until that run reports.

CORRECTION 2 (champion transfer, statistically re-adjudicated): decided-
accuracy differences were declared ties/losses with no error model. With
~19.0M decided positions the paired-bound standard error is <0.004 points;
therefore "bk rel wq, br rel wq" at 98.65% vs aligned 98.61% was a
STATISTICALLY SIGNIFICANT WIN on the decided metric, wrongly reported as
"no win." Fortress-side verdicts in that test used the superseded
hitchhiker instrument and are void pending the direct-instrument re-grade
(launched; results recorded when complete).

CORRECTION 3 and 4: adjudicators run/launched same day — exact-core scale
artifact check (Grundy campaign doc) and prevalence-controlled AUC for the
fortress "complexity premium" (this doc, when complete).

## Final fair-instrument packing table, KQKR (direct draw-field, AUC)

aligned 0.9992 (recall 93.3%) | rook-rel-own-king 0.9981 (90.2%) |
bk,br-rel-wq 0.9975 (89.1%) | shear-composite 0.9941 (84.4%).
All rows pass the guardrail construction-audit; all stand. Combined with
the corrected decided-side result (bk,br-rel-wq wins +0.04, >10 sigma):
AT THIS SINGLE BUDGET the four tested candidates trail aligned on the
fortress side. SCOPE DEMOTION (author-ordered scrutiny of the last
standing negative): a one-budget verdict conflates concentration speed
with judgment ceiling, and four candidates do not exhaust "relational."
AUC-vs-budget curves queued; the verdict is provisional until the curves
report. The candidate's decided-side win (+0.04, >10 sigma) stands.

## Fragment and noise certification (the sampling regime opens)

Pre-registered suite, KQK, deterministic position selection, graded
against held-out truth only:

FRAGMENTS (see rho of positions, graded ONLY on the withheld):
  rho=1%:  withheld acc 81.03% (ceiling 92.71, majority 54.5); 17/32 coeffs
  rho=5%:  withheld acc 92.19% — 99.4% of ceiling quality from 5% of data
  rho=20%: withheld acc 92.69% = ceiling (tie); 31/32 coeffs
NOISE (eps of values flipped, graded on clean truth):
  structure identification: 31/32, 31/32, 29/32 of the true top
  coefficients at eps = 1%, 5%, 20% — at eps=20% that is ~15,000x beyond
  chance overlap (expected 0.002 of 32): near-perfect structure recovery
  with a fifth of the input wrong.
  Accuracy at eps=20% (46.9%) is FLAGGED, not accepted: fixed-threshold
  shrinkage artifact (failure shape #2); threshold-rescaled adjudication
  queued before any "collapses under heavy noise" conclusion exists.

Meaning, at tested size: complete answer spaces are not required to
extract their structure — five percent recovers essentially everything,
at 2^19 scale, one ending. Scale-up (KQKR fragments) queued. Combined
with noise-tolerant structure identification, this defines the realistic
wall-raid design: SAMPLE positions beyond the tablebase frontier, evaluate
each imperfectly (engine/search = noisy oracle), extract structure from
the noisy fragment — the lens tolerates both conditions jointly tested.

## Curve adjudication of the final negative (complete)

Full AUC-vs-budget curves, four budgets, three packings: aligned reaches
1.00000 at k=2^20; defender-relational 0.99999; attacker-relational
0.99997. No crossing at any measured budget; gaps shrink monotonically
(0.014 -> 0.00001-0.00003). FINAL FORM of the one surviving negative:
all tested coordinates achieve near-perfect fortress separation at large
budgets; aligned concentrates fastest. A convergence-speed difference,
not a capability difference. Register final: eight verdicts scrutinized —
seven dissolved or reversed, one survived at ~1/1000 of its apparent
original size.

## Owed retests (complete)

2^25 deterministic battery: self-test EXACT at scale; lawful-motion
retention 63% at four pieces (0.504/0.797) vs 89% at three (0.726/0.811),
both ~25x+ above floor. Fold-intrinsic confirmed at both scales; invariance
strength is scale-dependent — new datum, recorded without spin either way.
Paired McNemar, candidate-1 vs aligned, decided positions: z = 19.3 in the
candidate's favor — the "no win" verdict refuted at the strictest standard.
