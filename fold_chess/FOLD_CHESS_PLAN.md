# Fold Chess — Discovery Engine Plan

Solve chess one material rung at a time, exclusively inside the fold's mathematical laws,
until we hit the limit — and map where, and why, the limit sits. Every result verified
against ground truth (Syzygy tablebases for ≤7 pieces): a referee with no priors.

## Fold-law adherence rules (binding on all code in this directory)

1. **Domain.** Every chess state is a rational in S = Q ∩ (0, 1]: state = (index + 1)/P
   with P prime and 2 a primitive root mod P, so the doubling fold acts transitively on
   the nonzero residues. The fold on states IS multiplication by two on numerators mod P —
   numerator arithmetic is exact image of fold arithmetic, used for speed without leaving
   the law.
2. **No zero.** No literal zero characters in code (corpus convention: one_val - one_val
   where an additive identity is unavoidable). No state maps to zero: indices shift by one.
3. **Operations.** fold (double, cast out the One) and take (guarded subtraction,
   greater-from-lesser forbidden) are the only primitive moves on state rationals.
   Interface values are SmithianValue instances; verify_value() validates sampled
   derivations every run.
4. **No transcendental imports.** No math module, no floats in any proof-bearing path.
5. **Gate.** fold_chess.py passes sftoe.gate.verify_code under the same conditions as
   usde.py.

## Rungs

- **Rung 1 (this build): KQK and KRK, complete.** Enumerate every legal state along the
  fold orbit of 1/P, solve by retrograde induction (mate / stalemate / capture-to-draw
  terminals, backward distance-to-mate), self-check internal invariants (colour/mirror
  symmetry counts, fixpoint stability).
- **Rung 1 verification:** position-by-position agreement with Syzygy WDL/DTZ via
  python-chess — all positions, not samples. Deliverable: "N positions, N agreements."
- **Rung 2: discovery layer.** Sweep fold-structural features (orbit period classes under
  varying P, orbit sums, residue classes, take-distance to nearest mate state) as
  predictors of game value, scored against ground truth with seeded null controls and
  look-elsewhere correction — the USDE methodology, ported. A validated fold invariant
  that predicts value = a compression of the tablebase = the seed of a new algorithm.
  A null result = knowledge of where structure is not.
- **Rung 3: climb.** KP K, then 4-piece, then 5-piece. Measure memory/time at each rung
  on this machine. The rung where it bites is the limit, found honestly — and any
  validated Rung-2 invariant gets its chance to move it.

## Honesty protocol

- **Syzygy is the external read (Route B), exactly as CODATA/PDG are for the physics
  corpus: an independent measurement used for validation only.** It is never an input
  to any derivation, and it is not "truth" — any disagreement between the fold solver
  and Syzygy is adjudicated by hand on the board, the only real authority. ("Beats
  Stockfish" is theater: any perfect table converts won positions against anything.
  Agreement on ALL positions is the certificate.)
- Internal (prior-free) referees run first: full board-symmetry audit over all states,
  dual-prime double-solve (two different fold orbits must give identical values —
  enumeration-order independence), hand-checkable spot positions.
- **The 50-move rule is modeled from Rung 1 onward**: the solver tracks distance-to-
  zeroing (DTZ) alongside distance-to-mate and reports five-valued results (win /
  cursed win / draw / blessed loss / loss), because beyond three pieces some wins
  require more than 100 plies between zeroing moves and are draws under the rule.
  At three pieces the cursed/blessed counts are asserted, not assumed, to be zero.
- The rules of chess (FIDE) are the one irreducible external object: the fold solves
  the game, it does not define it.
- Every claimed regularity must beat seeded nulls after look-elsewhere correction.
- Limits get reported with the same precision as successes.
