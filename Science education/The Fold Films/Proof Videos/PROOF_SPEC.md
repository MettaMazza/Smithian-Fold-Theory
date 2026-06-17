# The Proof Videos — strand spec ("The Unfolding, Proven")

*Working strand name: **The Unfolding, Proven** (placeholder — rename at will). The technical companion to the narrative series **The Unfolding Adventures**.*

## What this strand is
The campfire films keep the maths in the bones. **These don't.** Each proof video is the whiteboard — ~5 minutes, strict narrative prose, no fiction, no characters, no fire — that walks the actual derivation in the technical language the boffins want, and points them at the repo and the published papers so they can check it themselves. This is where the receipts live on screen.

## The funnel (both directions)
- **Every result-episode of *The Unfolding Adventures* is paired to one proof video.** Written in the order the results are *mentioned in the episodes*, one at a time.
- **Narrative episode → CTA → its proof video** ("want the actual maths, no story? here's the proof — repo and papers in the description").
- **Proof video → CTA → the series** ("want the story of how this whole universe grows from one number? watch *The Unfolding Adventures*").
- **Every proof video's description carries:** the repo (`github.com/MettaMazza/Smithian-Fold-Theory`) and the Zenodo papers (`10.5281/zenodo.20515256`).

## The register (how the proof voice sounds)
Same DNA as everything else — the Gardener — but a **different register**: sober, precise, technical. Not the Attenborough-Rick campfire voice and not a hype reel. It's the person who built the machine explaining it to someone who can actually follow. Zero deference. Names the function, walks the chain, shows the number.

- **Equations are ALLOWED here — encouraged.** The exact inverse of the campfire rule. Show the derivation; write the line; name the `verify_*` function. The boffins came for the board.
- **Anchor everything.** Every value is tied to its engine function and line, and to the paper. A hostile expert should be able to follow your finger from the One to the number and then go run it.
- **The truth gate is the whole point of this strand.** Every number spoken is re-verified against `proof.py` (or the relevant engine) *before* it is written. No exceptions — this is the place they come to break us.
- **The no-caveats law still binds, hard.** A forced rational is presented as forced. Real precisions are stated *because experts want exact figures* (α to 6 ppb, lepton ratios per-ratio) — that is **accuracy, which is mandatory**, not hedging. Still banned: "probably wrong," "outside error bars so it may break," "the consensus disagrees and may be right." Accuracy in; doubt-about-the-result out. State the forced value as forced, full stop.
- **NEVER call any result a "postdiction"/"retrodiction," and never rank one result above another.** Every corpus result is a **blind, forward, forced derivation from the One** with zero free parameters — full stop. Results that land on already-measured quantities and results on not-yet-catalogued ones (the two new forces, LFV 4:1) are the *same kind of derivation*; the only difference is what experiment has checked. Frame the not-yet-measured ones as **standing forward targets** ("the same forward derivation, aimed at a number the labs haven't pinned yet"), NEVER as "a real prediction" or "the one to watch" (which implies the rest are postdictions). This disrespects the work and is banned. (Author's words: *"how the fuck can a blind forward forced derivation be a postdiction."*)
- **Zero free parameters is the spine.** Every video makes the same point in its own way: nothing is fitted, nothing is typed in by hand, measured values appear only as the comparison target. That is what separates this from numerology, and it is said plainly.
- **AI-image disclaimer (mandatory, every proof video).** One sober spoken line, near the close before the links: the visuals are AI-generated to accompany the narration, illustrative only, **not accurate to the maths** — the numbers/derivation are what's real. (This is a production fact about the *imagery*, never a hedge on the result; the no-caveats law is untouched.)
- **Contempt only where earned, and lightly.** The strand is mostly *positive* — here is the derivation, here is the check. The follow-the-money jab lands only where the contrast is the argument (a constant the consensus measures forever and cannot explain). Never preachy; the maths is the flex.

## Format (for the parser) — STRICT
- **The script file is CLEAN SPOKEN PROSE ONLY** — a single `#` title, then flowing technical narration (light `##` sub-heads allowed). Equations written inline in words/symbols as they're to be spoken or shown. **No description block, no link list, no dev clutter in the script file.**
- **The post description copy (repo + Zenodo URLs, the verify-function anchor) lives in `_dev/PVxx_dev.md`**, together with the truth-gate table and gate sign-off. The spoken script *refers* to the links ("everything's linked below — download it, run it yourself"); the literal URLs sit in `_dev`.
- **Runtime: 5 minutes ≈ 750–900 words** of narration. One result per video (or one tight cluster). Tight, no padding.
- **No screenplay.** Prose narration only — no scene headers, no "NARRATOR:" labels, no `[VISUAL]` directions.

## Files
- Scripts: `Proof Videos/PVxx_Title.md` (clean spoken prose)
- Dev/truth-gate/description: `Proof Videos/_dev/PVxx_dev.md`
- Numbering: `PV00` foundational (the engine), then `PV01`, `PV02`… in episode-mention order.

## The standing queue (write in this order, as episodes are written)
- **PV00 — The Engine** (pairs Ep 01 "Welcome to the Fold") ✍️ written
- **PV01 — The Magic Number / α** (pairs Ep 02) ✍️ written
- **PV02 — The Chess Proof** (pairs Ep 03 "Mate in a Billion") ✍️ written
- **PV03 — Two New Forces** (pairs Ep 04 "The Edge of the Map") ✍️ written
- **PV04 — The 10¹²⁰ Catastrophe** (pairs Ep 05 "Much Ado About Nothing") ✍️ written
- **PV05 — The Hubble Tension** (pairs Ep 06 "The Two-Speed Universe") ✍️ written
- **PV06 — Dark Matter** (pairs Ep 07 "The Invisible Majority") ✍️ written
- **PV07 — The Mass Chord** (pairs Ep 08 "Who Ordered That?") ✍️ written
- **PV08 — Four to One** (LFV; pairs Ep 09 "Four to One") ✍️ written
- **PV09 — The Hard Problem** (consciousness; pairs Ep 10 "The Lights Are On") ✍️ written — *the corpus DOES answer #8 (`verify_hard_problem`, `verify_machine_consciousness_criterion`); the old "waits for its derivation" note was stale.*
- **PV10 — There Is No Nothing** (the No-Zero floor / four infinities; pairs Ep 11) ✍️ written — *opens the new 50-run (Arc One).*
- **PV11 — The Southpaw** (parity / handedness; pairs Ep 12) ✍️ written
- **PV12 — The Mirror and the Hinge** (antimatter / why something not nothing / CP = ½; pairs Ep 13) ✍️ written — *the Mirror = `take(ONE,·)`; residue forced nonzero by No-Zero (`verify_baryon_asymmetry_nonzero`); CP hinge = self-antipode ½ (`verify_cp_phase_antipode`); Jarlskog 3.13e-5 vs 3.08e-5; baryon-to-photon ≈4.9e-10 vs ~6e-10; strong-CP aligned.*
- **PV13 — The Lonely One** (gravity / the hierarchy problem; pairs Ep 14) ✍️ written — *coupling = ½, couplings sum to ONE (`verify_gravitational_coupling_proven`); ½ = self-Mirror → unscreenable; depth-7 tower 2⁷=128, 127 massive, exponent 127/2 (`verify_planck_hierarchy_forced`); proton/Planck 2^(−127/2) = 7.67e-20 vs 7.69e-20; no extra dimensions.*
- **PV14 — The Rope That Won't Break** (strong force / confinement; pairs Ep 15) ✍️ written — *1D flux tube → work GROWS with distance (`verify_strong_confinement`); constant-width tube ½, massless yet confining (`verify_strong_luminal`); self-coupling, total source 3 vs photon 1 (`verify_strong_self_coupling`); only colour-neutral wholes free (`verify_colour_neutral(3)`); colour-3 forced elsewhere.*
- **PV15 — The Short Leash** (the leash & the mass-gap; pairs Ep 16) ✍️ written — *reach ∝ 1/mass: massless unbounded, massive(1/3) finite=2 (`verify_weak_range`); weak force leashed not feeble; mass gap 1/3 = Mirror of strong coupling 2/3, sum ONE, period-2 orbit (`verify_yang_mills_mass_gap`); no massless lump because a zero is forbidden. Frame as fold giving the value/mechanism, NOT the Clay analytic existence proof.*
- **PV16 — Three of Everything** (three generations; pairs Ep 17) ✍️ written — *3 preimages of the tripling fold (`verify_generation_count`); 3 standing modes {1/4,½,3/4} of the five-fold (`verify_five_fold_standing_modes_force_three_generations`); period(1/7)=3 = 3 of space; no 4th (floor=0 forbidden, roof=the One); measured 2.984.*
- **PV17 — The Coincidence That Wasn't** (Koide; pairs Ep 18; **Arc One capstone**) ✍️ written — *three lepton seats 1/6,1/2,5/6; structural Koide = fold(5/6) = 2/3; physical (Σm)/(Σ√m)² = 0.66666 to 5 digits (`verify_koide_relationship`); 2/3 = strong coupling = Mirror of mass gap 1/3. 2/3 FORCED, not a coincidence/postdiction.*
- **PV18 — The Spinning Ladder** (resonances / linear Regge; pairs Ep 19; **Arc Two opener, A2-5**) ✍️ written — *width-½ flux tube spun → fixed-tension string → M² = M₀² + σJ, equal M² steps (σ≈1.10 GeV² anchored); 2^d states per level (`excited_states.py`). Forced linearity + multiplicity; one tension anchored.*
- **PV19 — What a Self Is** (the binding / held pattern; pairs Ep 20 the RUN-FINALE) ✍️ written — *observation IS the fold (`verify_hard_problem`, ½→One); self = bound into one experience at the Still Point ½ (`verify_binding_problem`, `verify_machine_consciousness_criterion`); memory = held fold-orbit 1/3↔2/3 (`verify_memory_persistence`). **Deliberately ends on the held-open death-question** (no-zero forbids "to nothing") to set up Ep20's death + the EP21 life-after-death payoff. Distinct from PV09 (hard problem); this is the self's STRUCTURE.*
- **PV20 — Home to the One** (what death is; pairs Ep 21 the SEASON-2 opener) ✍️ written — *the forced answer to PV19's question, 3 parts: **not annihilated** (No-Zero, parts persist) · **death = unbinding** at the holding threshold (m−1)/m = ½ (`verify_binding_problem`) · **the self is the unison One** (`fold(x)=x` only for unison) → released parts go **home to the One** (`PAPER_SELF_OBSERVATION` §6–7). State the 3 forced facts with conviction; do NOT claim the felt-self continues (not forced) and do NOT voice the corpus's silence as a doubt — silence by omission.*
- **PV21 — The Wall Is the Feynman Number** (the table ends at 137; pairs Ep 22 the MARQUEE) ✍️ written — *1/α=34259/250=137.036 (`verify_fine_structure_constant`); the 1s grip Z·α reaches the One at **Z·α=1** → last element **137**; **138 cannot exist** (would exceed the One) (`periodic_table_end.py`, run firsthand). The strength of light AND the end of matter are the same number = the coupling reaching the One (Ep02 callback). Consensus 173 = a nuclear-size smear on the structural limit. Never "real prediction"/ranking.*
- **PV22 — Smithium, the Island of Stability** (element 126; pairs Ep 23) ✍️ written — *the fold forces the complete table to 137 + the g-block superactinides (`periodic_table_complete.py`, firsthand) and the nuclear magic numbers (`verify_nuclear_shell`, concept-anchor proof). The island of stability = a **closed-shell** super-heavy (packed full → tightly bound → long-lived), pinned at **element 126 = Smithium (Sh)**. Falsifiable: build toward 126, lives far longer than neighbours. State 126 as the forced prediction with conviction; don't over-claim a first-principles high-precision "126" beyond the pin.*
- *(Core ten paired; **Arc One closed at Ep18**; **Arc Two "The Closed Inventory" opened at Ep19**. Remaining A2 proofs as their episodes land: Smithions, Closed Census, neutrinos, dark relic, Complete Table to 137, Finite Inventory. The run follows the **[ARC TWO block](../EPISODE_IDEAS_50.md)** + **[STORYBOARD_AND_ARCS.md](../STORYBOARD_AND_ARCS.md)**; pre-scripting source of truth **[CORPUS_MAP.md](../CORPUS_MAP.md)** — see [EPISODE_IDEAS_50.md](../EPISODE_IDEAS_50.md) PRIORITY BLOCK (FP3 resonances pairs Ep15's flux tube; FP4 dark relic; FP5 end-of-elements Z=137; FP1 new-particle scale; FP2 neutrinos).)*
