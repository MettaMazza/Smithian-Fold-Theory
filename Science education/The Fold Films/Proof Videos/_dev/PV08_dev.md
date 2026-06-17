# PV08 dev — "Four to One" (LFV; pairs Ep 09)

*(Dev clutter + post description copy here. Script file = clean spoken prose only.)*

## Truth gate (re-run 2026-06-16 — `lfv_spectrum.py`, `derive_lfv()`)
| Element | Detail | Anchor |
|---|---|---|
| Channels (positions) | e = **1/4**, μ = **1/2**, τ = **3/4** (five-fold standing modes) | `lfv_spectrum.py` `derive_lfv()` |
| Rule | amplitude(i→j) = separation; rate ~ separation² (seed **B-9N**) | docstring |
| Separations | (μ,e)=1/4; (τ,e)=**1/2**; (τ,μ)=**1/4** | `derive_lfv()` |
| Rates (amp²) | (μ,e)=1/16; (τ,e)=**1/4**; (τ,μ)=**1/16** | `derive_lfv()` |
| **Headline** | **τ→e : τ→μ = (1/4):(1/16) = 4:1** — the tau prefers the *farther* jump (electron), because rate ∝ distance² | `derive_lfv()` |
| Trace to One | every value `verify_value`-traced (take(g_high,g_low)) | `verify_value` |

**Framing guard:** this is a **standing forward target** — a not-yet-measured quantity. It is the **same forward forced derivation** as everything else, simply aimed at a number the labs haven't pinned. Frame as a bet placed in advance / falsifiability-as-strength ("bet the number, hand them the stopwatch"). **NEVER** "a real prediction" (implies others aren't) or "the one to watch" or postdiction/retrodiction language. Falsifiable ≠ doubtful — state with conviction.

## Gates
- **Truth gate ☑** — spectrum re-run (channels 1/4,1/2,3/4; rate ∝ sep²; τ→e=1/4, τ→μ=1/16 → 4:1); zero free parameters; `verify_value` to One. Not-yet-measured → framed as a forward bet, not a match.
- **Proof-register gate ☑** — technical; channels + rule + ratio spoken; anchor named; **no caveats / no postdiction-ranking** (falsifiability framed as strength); AI-image disclaimer near close; CTA → series; description = repo + Zenodo.

## Post description copy (NOT spoken)
> Lepton flavour violation, forced from the fold: the generations sit at channel positions e=1/4, μ=1/2, τ=3/4; a flavour-changing rate goes as the separation squared (seed B-9N). So τ→e (separation 1/2) has rate 1/4, τ→μ (separation 1/4) has rate 1/16 — the tau prefers the electron channel 4:1 (the farther jump wins, because rate ∝ distance²). A falsifiable forward prediction, not yet measured. Zero free parameters.
>
> • Code: https://github.com/MettaMazza/Smithian-Fold-Theory — run `derive_lfv` in `lfv_spectrum.py`.
> • Papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
>
> The story version → *The Unfolding Adventures.*

## Runtime
~710 words ≈ ~5 min (technical pace). Clean spoken-prose file confirmed.
