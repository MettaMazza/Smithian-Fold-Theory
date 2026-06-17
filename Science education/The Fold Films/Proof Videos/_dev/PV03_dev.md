# PV03 dev — "Two New Forces" (pairs Ep 04)

*(Dev clutter + post description copy here. Script file = clean spoken prose only.)*

## Truth gate (re-run 2026-06-16 — `prime_force_phenomenology.py`)
| Element | Detail | Anchor |
|---|---|---|
| Forces = prime sectors | known: 2 (electroweak), 3 (strong); **predicted: 5, 7**; criterion = corpus claim **B-7N** | `prime_force_phenomenology.py` docstring |
| Carrier count = p²−1 | 2→3, **3→8 (the gluons — real-world anchor)**, **5→24, 7→48** | `derive_mediators_and_colours()` → `{2:(2,3),3:(3,8),5:(5,24),7:(7,48)}` |
| Charge/colour count = p | 5 charges (sector 5), 7 charges (sector 7) | same |
| Coupling g_p=(p−1)/p (shortfall 1/p) | 1/2, 2/3, **4/5, 6/7** | `derive_couplings()` → `{2:(1/2,1/2),3:(2/3,1/3),5:(4/5,1/5),7:(6/7,1/7)}` |
| Confinement (p−1)/2 antipodal pairs | 5→**2 pairs**, 7→**3 pairs** | `derive_confinement()` → `{2:1/2,3:1,5:2,7:3}` |
| Running g_p(d)=take(ONE,1/(p+2^d))→ONE; beta-slope p−1 | slope 5→**4**, 7→**6** | `derive_running()` |
| Carriers | massless, unbounded reach, **confining** (width ½) | `derive_carrier()` |
| Bound states | mesons + baryons charge-neutral (5 and 7) | `derive_bound_states()` |
| **The seal** | realized sectors **{2,3,5,7}**, bound **7**, **no force at 11** | `derive_ladder_bound()` → `{'realized_sectors':[2,3,5,7],'bound':7,'no_force_at':11}` |
| Trace to One | every value `verify_value`-traced to the One | `verify_value` |
| Cross-checks | weak range / colour count in the main corpus | `verify_weak_range` `proof.py:3318`, `verify_colour_prediction` `proof.py:3904` |

**The anchor that earns it:** p²−1 gives sector 3 → **8 = the measured gluon count** (known, undisputed) *before* the same formula is run forward to 24 and 48. Why unseen: both new forces **confine** (like the strong force) → charges hidden in neutral bound states. **These are the same forward forced derivation as everything else in the corpus** — they simply target quantities the labs haven't catalogued yet (NEVER frame any corpus result as a "postdiction/retrodiction" — all are blind forward derivations). A real fifth gauge force would falsify the seal.

## Gates
- **Truth gate ☑** — all figures re-run from `prime_force_phenomenology.py`; the 8-gluon anchor is the known check; the seal (no force at 11) stated; zero free parameters (p is the only label); `verify_value` to the One.
- **Proof-register gate ☑** — technical; equations (p²−1, (p−1)/p, beta-slope p−1) written/spoken; anchors named; no caveats (prediction stated as forced; falsifiability stated as strength, not doubt); AI-image disclaimer near close; CTA → series; description = repo + Zenodo.

## Post description copy (NOT spoken)
> The fold indexes the fundamental forces by prime sector. Known: sector 2 (electroweak, 3 carriers), sector 3 (strong, 8 gluons = 3²−1). Predicted: sector 5 (5 charges, 24 carriers, coupling 4/5) and sector 7 (7 charges, 48 carriers, coupling 6/7) — two new confining forces — and the ladder seals at 7 (no force at 11). Zero free parameters.
>
> • Code: https://github.com/MettaMazza/Smithian-Fold-Theory — run `prime_force_phenomenology.py`.
> • Papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
>
> The story version → *The Unfolding Adventures.*

## Runtime
~821 words ≈ ~5 min (technical pace; the per-sector numbers land slower). Clean spoken-prose file confirmed.
