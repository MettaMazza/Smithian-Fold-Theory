# Rung 2 Report — Fold-structural features vs game value (KQK, KRK)

**Design, fixed before any data:** 7 fold-native features of the state numerator;
exact mutual information with solved W/L/D values; seeded label-permutation null
(final run: 500 permutations); Bonferroni look-elsewhere over all 7 features;
significance threshold p_global < 0.05; random-packing control to localize any
signal; replication across both endings required for any cross-ending claim.
Criterion identical between the 50-null and 500-null runs — only measurement
resolution changed (50 nulls bottom out at raw p = 0.020, which cannot clear
0.05 after x7 correction; 500 nulls resolve to 0.002, which can).

## KQK (368,452 states, 364 mates, P = 524309)

| feature | MI bits (real) | null p (raw) | null p (x7) | MI bits (random packing) | verdict |
|---|---|---|---|---|---|
| itinerary_ones | 0.0004 | 0.002 | 0.014 | 0.0001 | signal — packing-dependent |
| residue_mod3 | 0.0000 | 0.627 | 1.000 | 0.0000 | chance |
| residue_mod7 | 0.0000 | 1.000 | 1.000 | 0.0000 | chance |
| residue_mod31 | 0.0000 | 1.000 | 1.000 | 0.0002 | chance |
| residue_mod127 | 0.0004 | 0.934 | 1.000 | 0.0004 | chance |
| orbit_balance | 0.0001 | 0.002 | 0.014 | 0.0000 | signal — packing-dependent |
| mate_distance_decile | 0.0012 | 0.002 | 0.014 | 0.0000 | signal — packing-dependent |

## KRK (399,112 states, 216 mates, P = 524309)

| feature | MI bits (real) | null p (raw) | null p (x7) | MI bits (random packing) | verdict |
|---|---|---|---|---|---|
| itinerary_ones | 0.0005 | 0.002 | 0.014 | 0.0001 | signal — packing-dependent |
| residue_mod3 | 0.0000 | 0.583 | 1.000 | 0.0000 | chance |
| residue_mod7 | 0.0000 | 1.000 | 1.000 | 0.0000 | chance |
| residue_mod31 | 0.0000 | 1.000 | 1.000 | 0.0001 | chance |
| residue_mod127 | 0.0003 | 1.000 | 1.000 | 0.0004 | chance |
| orbit_balance | 0.0001 | 0.002 | 0.014 | 0.0000 | signal — packing-dependent |
| mate_distance_decile | 0.0005 | 0.002 | 0.014 | 0.0000 | signal — packing-dependent |

## Findings

1. Three features carry statistically real signal, replicated in both endings
   at the fixed corrected threshold. Effect sizes are minuscule: at most
   0.0012 bits of the ~1.58 bits per label (< 0.1%).
2. The random-packing control annihilates all three. The signal therefore
   lives in the interaction between the structured position->numerator packing
   (whose low bits encode board coordinates) and fold-arithmetic functions of
   the numerator — per the pre-registered interpretation rule, a statement
   about the (encoding, fold) pair, not about fold dynamics knowing chess.
3. No fold-intrinsic structure in game values was found at this rung: nothing
   survives the packing control, and the Mersenne-tower residues are dead.
4. What would change this verdict at higher rungs or future sweeps: a feature
   that (a) survives random packing, or (b) carries effect size at the
   percent-of-label scale. Neither occurred here.

Prior-work features (Mersenne orbit periods, P-position spacings, orbit sums)
are reserved for a follow-up investigation under identical controls, at the
author's direction, with this run kept clean as the baseline.
