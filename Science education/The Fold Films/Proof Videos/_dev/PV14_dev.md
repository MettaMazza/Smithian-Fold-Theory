# PV14 dev — "The Rope That Won't Break" (strong force / confinement; pairs Ep 15)

*(Dev clutter + post description copy here. Script file = clean spoken prose only.)*

## Truth gate (re-run 2026-06-17)
| Element | Detail | Anchor |
|---|---|---|
| Confinement (d=1 tube) | work to separate **grows**: near 1/8, far 1/4 | `verify_strong_confinement(1/8,1/4,10)` `proof.py:2651` |
| Deconfinement (d=3 Coulomb) | work to separate **shrinks**: near 4, far 2; flux conserved = ONE | same |
| Constant-width tube | massless carrier (speed 1) yet confining; tube width **½** constant; abelian width grows 1, 2 | `verify_strong_luminal(8)` `proof.py:2946` |
| Self-coupling | carrier carries the charge it mediates: matter 1 + carrier 2 = **total 3** (photon = 1) | `verify_strong_self_coupling` `proof.py:3208` |
| Colour-neutral wholes | baryon (three colours → ONE) and meson (colour–anticolour pair) only | `verify_colour_neutral(3)` `proof.py:2801` |
| Colour count 3 | forced elsewhere, NOT assumed here | `verify_colour_prediction` `proof.py:3904` |
| Trace to One | `verify_value`; zero free parameters | — |

**Framing guard:** the *structure* (tube-vs-Coulomb inequality; constant width; self-coupling source 3; only neutral combos free) is forward-forced; the *match* to observed confinement is the external read. The "pull → pair production → two tubes" is standard physics, stated straight. NO postdiction/ranking, NO caveat. The "consensus observes it but has no first-principles derivation in 50 years" contrast is accurate and played straight (not preachy).

## Gates
- **Truth gate ☑** — confinement vs deconfinement inequalities (`verify_strong_confinement`); constant-width tube ½ (`verify_strong_luminal`); self-coupling total source 3 (`verify_strong_self_coupling`); colour-neutral wholes (`verify_colour_neutral(3)`); colour-3 forced elsewhere; forward-forced; zero free parameters.
- **Proof-register gate ☑** — technical; spread-vs-rope contrast; the self-grabbing carrier mechanism; only-wholes-walk-free; the can't-take-one snap; anchors named; AI-image disclaimer near close; CTA → *The Unfolding Adventures*; description = repo + Zenodo. `voice_gate.py` → pass.

## Post description copy (NOT spoken)
> You will never see a free quark — confinement. The fold gives the mechanism. A 3D Coulomb field spreads and weakens (1/r²): separating two charges costs LESS the farther you go (`verify_strong_confinement`, d=3: 4 then 2). The strong field doesn't spread — its flux is a 1D tube of constant width ½ (`verify_strong_luminal`), so the work to separate GROWS with distance (1/8 then 1/4): infinite energy to extract one. Why the tube? The carrier carries the charge it mediates — matter 1 + carrier 2 = total source 3 vs the photon's 1 (`verify_strong_self_coupling`) — so the field grabs itself into a rope. Only colour-neutral wholes walk free: three colours summing to the One (baryon) or a colour–anticolour pair (meson) (`verify_colour_neutral`). Pull hard enough and the tube makes a new pair — two tubes, never a lone quark. Zero free parameters; colour-count 3 forced elsewhere.
>
> • Code: https://github.com/MettaMazza/Smithian-Fold-Theory — run `verify_strong_confinement` and `verify_strong_self_coupling`.
> • Papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
>
> The story version → *The Unfolding Adventures.*

## Runtime
~830 words ≈ ~5 min (technical pace). Clean spoken-prose file confirmed.
