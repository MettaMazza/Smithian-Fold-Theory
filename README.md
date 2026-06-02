# Smithian Fold Theory

**Author:** Maria Smith — independent researcher.

This directory (`pure/`) is the system, in the author's language: one axiom (the One),
no negatives, no zero, no imaginaries, ratio and division only. The static gate
(`no_apparatus_gate.py`) enforces that the corpus contains none of the forbidden apparatus —
no imaginary or complex quantity, no negative, no zero used as a value, no subtraction outside
the audited casting-out primitives, and no sine or cosine.

## What is here
- `ratio.py` — the One, the fold (double and cast out the One), ratio, separation, the audited
  removal primitives. Absence (an empty site, a flat curvature, a coincidence) is carried
  structurally, never as the value zero.
- foundation modules — `count`, `measure`, `monad`, `geometry`, `coupling`, `opposition`, `closure`.
- emergence modules — `beats`, `density`, `aggregate`, `modulation`.
- physics modules — `magnitude`, `lattice`, `propagation`, `interaction`, `spacetime`,
  `relativity`, `quantum`, `particles`, `constants`, `gravity`, `charge`, and the
  `correspondence` / `compare` layer.
- claim registries — `claims_pure.py`, `claims_emergence.py`, `claims_physics.py`
  (each entry tagged DEF, THM, OBS, or E).
- `PROOFS_hardened.md` — definitions and proofs.
- `no_apparatus_gate.py` — the language gate (AST-based); `gate_integrity.py` — its tripwire.
- `coverage_pure.py`, `stress_pure.py`, `fold_system_pure.py`, `GATES_pure.py` — coverage,
  exact-arithmetic scale tests, one-pass derivation, master gate.
- `manifest.py` / `THEOREM_MANIFEST.md` — claim to proof to confirmation map.
- `run_all.py` — one-command reproduction.
- `PAPER.md` — the paper.

The parent directory holds an earlier development that modelled the same dynamics in the
complex plane with negatives and signed operations. That development is superseded and is not
the system; a model built in the forbidden apparatus is not the author's system, and the gate
here enforces that the finalized corpus contains none of it.

## Reproduce
```
python3 run_all.py
```
This is green only when no forbidden apparatus appears anywhere, every theorem has a proof and a
passing exact confirmation, every observation is labelled and confirmed, every physical
correspondence is confirmed, the scale tests pass to the environment ceiling, and the one-pass
derivation reports all theorems proven.

## The system
Three definitions; fifteen theorems, each proved from the One using ratio and division only and
confirmed by exact rational computation; four measured observations; and ninety-five physical
correspondences, each derived in the framework and reproducing — or forcing — a physical
relationship in the permitted language. The four fundamental interactions are built in the one
language and unified: every characteristic constant is forced from the single fold factor m. The
electroweak mixing is forced bare and runs by the framework's own mechanism through its measured
value; the W/Z mass ratio and the on-shell relation are forced from the channel structure; and the
strong and electroweak couplings are forced to converge on a single scale axis at a closed-form
rate. The constants that appear are plain ratios — the holding threshold (m-1)/m, opposition as the
reciprocal and the half-One, the forced coupling (m-1)/m — with no transcendental. The framework
forces only dimensionless ratios and is scale-invariant. The language constraint is enforced
mechanically and the development reproduces from a single command.
