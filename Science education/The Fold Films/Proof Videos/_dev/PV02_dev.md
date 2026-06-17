# PV02 dev — "The Chess Proof" (pairs Ep 03)

*(Dev clutter + post description copy here. Script file = clean spoken prose only.)*

## Truth gate (verified vs the certified record 2026-06-16)
| Element | Detail | Anchor |
|---|---|---|
| Independent check total | **1,092,871,108 positions checked vs independent ground truth (Syzygy), 1,092,871,108 agreements, zero errors** | `CHESS_RESULTS_FINAL_FIVE_PIECE.md:26-27` |
| Five-piece solved | **1,054,075,064 legal five-piece positions solved exactly, zero errors** | `:56,64` |
| Drawn fortresses | **382,468,048** correctly identified as draws | `:66` |
| External slice | 19,733,336 vs Syzygy — 19,733,336 agreements, 0 disagreements, 0 rules diffs | `:13,20` |
| Nim / impartial | losing set = F₂-linear subspace (Bouton); fold-spectrum vanishing law; mirror = XOR mask; all 524,288 spectral coefficients match exactly, both endings | `fold_theorems5.py`; results doc `:9,12-13,81` |
| Solver / laws | the engine that produced the verdicts | `fold_solve5.py`, `fold_theorems5.py`, `chess_generator.py` |

All counts quoted verbatim from the certified results doc (the project's ground-truth record); no rounding. Pure combinatorics — checkable against public Syzygy tablebases with no physics assumed.

## Gates
- **Truth gate ☑** — every count taken verbatim from `CHESS_RESULTS_FINAL_FIVE_PIECE.md`; independent oracle (Syzygy) is third-party/public; Nim claim tied to Bouton + the vanishing law.
- **Proof-register gate ☑** — technical; the "you don't need to believe anything, just re-run it" ethos = the project's heist principle; no caveats, full conviction; anchors named; CTA to series; description = repo + Zenodo.

## Post description copy (NOT spoken)
> The fold solves combinatorial games natively (nim-values = XOR = carry-free binary). Chess endgames built from the fold and checked vs independent Syzygy tablebases: 1,092,871,108 positions, zero errors; 1,054,075,064 five-piece positions solved exactly; 382,468,048 drawn fortresses. Nim: all 524,288 spectral coefficients exact.
>
> • Code + certification: https://github.com/MettaMazza/Smithian-Fold-Theory — see `CHESS_RESULTS_FINAL_FIVE_PIECE.md`, `fold_solve5.py`, `fold_theorems5.py`.
> • Papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
> • Syzygy tablebases are public — check the comparison yourself.
>
> The heist version → *The Unfolding Adventures.*

## Runtime
722 words ≈ ~5 min (technical pace; the big numbers spoken out land slower). Clean spoken-prose file confirmed.
