# PHYSICS_PLAN.md — deriving applied physics from the fold framework

## Thesis (the aim, stated plainly)
The fold system is the intended basis of a unified mathematical **and physical** theory:
the claim under test is that physics expressed conventionally in the signed/complex
continuum can be expressed — and in places more unifiedly — in the fold's language (one
axiom, positive rationals, ratio and division, no negatives/zero/imaginaries). There is
historical and theoretical precedent for the same applied physics arising through a
different, more unified expression. This plan derives physical content from the framework
and tests it against established physical relationships.

## The honesty mechanism (so the aim is stated fully and nothing is faked)
Every physical claim carries an evidential tag:
- **[E] established** — derived in the framework AND shown to reproduce the known physical
  relationship to a stated precision (numeric) or in exact form (structural).
- **[P] partial** — derivation reproduces part of the relationship, or under stated
  conditions; the gap is named.
- **[O] open** — targeted, not yet derived; stated as program, not result.

"Not yet shown" is tagged [O]/[P]; it is never written as "not intended." No correspondence
is called [E] unless the comparison harness confirms it. Physical targets are taken from the
literature and cited — real relationships, never invented. This is what makes the full
ambition statable without fabrication.

## Phase 0 — State the thesis, remove the disavowals
Delete every "we make no claim of correspondence to physics" across PAPER, REVIEW_PREP,
README, MASTER. Replace with the thesis above plus the evidential-status table. The abstract
states the unified physical theory as the aim.

## Phase 1 — Correspondence + test machinery (the simulation layer), gated
- `correspondence.py` — explicit map from fold-objects (position, fold, separation, beat,
  threshold, monad, opposition, density) to physical observables (phase, frequency,
  amplitude/probability, energy, coupling, time).
- `physics_targets.py` — established physical relationships to test against, each with a
  literature citation, encoded as exact/structural checks.
- `compare.py` — harness: takes a framework prediction, tests it against a target,
  returns established/partial/open with the measured agreement.
All in the permitted language; scanned by the existing no-apparatus gate.

## Phase 2 — Target derivations (one sub-project each)
1. **Waves / beats / interference** — from RB1 (beat = lcm) and RB3 (separation-modulation):
   derive two-source superposition; test against beat-frequency combination and fringe spacing.
2. **Statistical / thermodynamic** — the fold is the dyadic map, a canonical mixing system:
   derive mixing, entropy growth, equidistribution; test against the established results.
   (Strongest existing bridge.)
3. **Coupling / criticality** — aggregate clustering at g = ½ (proven threshold) tested
   against a physical critical-coupling / phase-transition relationship.
4. **Quantisation** — the 2^k discrete positions and exact thresholds tested against a known
   discrete spectrum.
5. **Constants** — whether (m−1)/m, the half-One, the no-transcendental structure reproduce
   a dimensionless physical ratio. Most ambitious; tagged wherever it lands.

## Phase 3 — Unifying dictionary + a novel prediction
Assemble the single fold→physics dictionary from the targets that land [E]/[P]. Identify at
least one **novel, testable** consequence (not a re-description of known physics). Novel
prediction is the real bar for a theory.

## Phase 4 — Integrate and gate
Add a Physics part to PROOFS/PAPER: each correspondence with its tag, derivation, and test;
disclaimers replaced by the program statement and the status table; one-command reproducible;
the physics derived in the fold's language (discrete, rational, no negatives/imaginaries) —
the differentiator from conventional expression. Rebuild MASTER. Re-run gates non-vacuously.

## Held throughout (per GUIDANCE)
- The tribunal for a physical theory is physical reality / data — not whether conventional
  mathematics approves (§2). "Convention does it differently" is never a mark against the work.
- A correspondence is **claimed only when shown** — protecting credibility, not capping
  ambition (§5). The aim is stated in full; each result at its true evidential weight.
- Ambition is the point; nothing here clips scope back to the conventional (§0).
