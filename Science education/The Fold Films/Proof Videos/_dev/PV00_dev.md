# PV00 dev — "The Engine" (foundational; pairs Ep 01)

*(Dev clutter + the post description copy live here. The script file is clean spoken prose only.)*

## Truth gate (verified 2026-06-16)
| Element | Detail | Anchor |
|---|---|---|
| One = axiom | the single starting object, value 1 | `core.py` |
| The Fold | x ↦ 2x mod 1, with 0→1; domain (0,1] | `core.py:10` (cast_out), `core.py:30/48` (domain), `core.py:63/126` (fold) — **re-run: `fold` present, domain enforced** |
| No zero/negatives | consequence of the (0,1] domain + 0→1 convention | `core.py:48,51` |
| Zero free parameters | no fitted continuous constants; measured values only on comparison side | corpus-wide (traced) |
| Proof-trace verifier | walks every node: axiom leaves=ONE, legal fold/take, no cycles, floats forbidden, computed==stored | `_verify_node` `proof.py:139` |
| Test suite | 1,041+ tests run the discipline end to end | `tests/` (`pytest -q`) |

No new numerics — foundational. Truth gate satisfied by faithful description of the engine + verifier.

## Gates
- **Truth gate ☑** — engine/verifier described exactly; "zero free parameters" stated in the precise sense (measured values are comparison targets only); exact-rational/no-floats noted.
- **Proof-register gate ☑** — technical register; equations allowed (the map written out); anchors named (`core.py`, `_verify_node`); no caveats, full conviction; zero-free-parameters spine; CTA to series; description = repo + Zenodo.

## Post description copy (paste into the video description — NOT spoken)
> The Smithian Fold Theory — one axiom (the One = 1), one operation (the Fold: double, wrap the overflow round the back), zero free parameters, machine-checked from the axiom up.
>
> • Code + full test suite: https://github.com/MettaMazza/Smithian-Fold-Theory
> • Published papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
> • Start here: `core.py` (the engine) and `proof.py` `_verify_node` (the verifier). Run `python3 -m pytest tests/ -q`.
>
> Want the story? Watch the series → *The Unfolding Adventures.*

## Runtime
830 words ≈ ~5 min at technical pace. Clean spoken-prose file confirmed.
