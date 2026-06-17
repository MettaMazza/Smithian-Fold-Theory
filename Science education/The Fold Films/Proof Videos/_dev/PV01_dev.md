# PV01 dev — "The Magic Number / α" (pairs Ep 02)

*(Dev clutter + post description copy here. Script file = clean spoken prose only.)*

## Truth gate (re-run 2026-06-16)
| Element | Detail | Anchor |
|---|---|---|
| Core result | 1/α = 2⁷ + 3²·(251/250) = **34259/250 = 137.036** | `verify_fine_structure_constant` `proof.py:12794` — **re-run returns `Fraction(34259, 250)`** |
| Arithmetic | 2⁷=128; 3²·251/250 = 2259/250 = 9.036; 128+9.036 = 137.036; 128=32000/250 → +2259/250 = 34259/250 ✓ | (checked by hand + engine) |
| Match | measured 137.035999177 → **6.01 ppb** (re-run: 6.00572…) | CODATA |
| 2⁷ block | depth-7 binary tower = minimal cover of 3⁴=81 (2⁶=64<81≤128=2⁷) | same principle as covering depth 5 in `verify_dark_to_baryon_fraction` |
| 3² block | colour count (3) squared = surface; the 3 is the tripling-fold fibre, preimages constructed | `verify_colour_prediction` `proof.py:3904` |
| 251/250 block | cosmological covering-volume dilation; 250 = 2·5³ (prime families 2,5) | `verify_fine_structure_constant` |
| Zero free params | 137.035999177 appears only as comparison target, never input | (traced) |

## Gates
- **Truth gate ☑** — engine re-run, returns 34259/250; ppb recomputed (6.01); each block tied to its own derivation; no measured value on the input side.
- **Proof-register gate ☑** — technical; equation written out and spoken; every block anchored; no caveats (precision stated as accuracy, not hedge); zero-free-parameters spine; follows-the-money jab earned ("measure the mystery harder"); CTA to series; description = repo + Zenodo.

## Post description copy (NOT spoken)
> 1/α = 2⁷ + 3²·(251/250) = 34259/250 = 137.036 — derived exactly from the fold, agreeing with measured 137.035999177 to 6 parts per billion. Zero free parameters.
>
> • Code: https://github.com/MettaMazza/Smithian-Fold-Theory — run `verify_fine_structure_constant` in `proof.py`.
> • Papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
>
> The story version → *The Unfolding Adventures.*

## Runtime
737 words ≈ ~5 min (technical pace, plus the on-screen equation beats). Clean spoken-prose file confirmed.
