# EP13 dev notes — "The Mirror and the Hinge" (antimatter / why something not nothing / CP) — Arc One

*(Dev clutter only. Episode file is clean prose. Pairs with PV12. ARC ONE — "Bigger Than the Number," episode 3. See [STORYBOARD_AND_ARCS.md](../../STORYBOARD_AND_ARCS.md).)*

## Fold payload (truth gate — re-run 2026-06-17)
| Element | Detail | Anchor |
|---|---|---|
| The Mirror | `take(ONE, x) = 1 − x`; a value + its Mirror sum to exactly ONE (1/3 + 2/3 = 1) | `proof.py` take; `verify_cp_phase_antipode` |
| Annihilation = folding home | matter + antimatter = a value and its Mirror folding back to the One they summed to | (Mirror identity) |
| Why something survived | complete annihilation = sum reaching **zero**; zero forbidden → No-Zero floor leaves a residue, proven nonzero = ½ | `verify_baryon_asymmetry_nonzero` |
| The hinge (CP) | CP-violating phase = the Still Point ½, the unique self-antipode (its own Mirror), maximal | `verify_cp_phase_antipode` |
| Jarlskog | fold 3.13×10⁻⁵ vs measured 3.08×10⁻⁵ (≈1 part in 70) | `verify_cp_phase_antipode` |
| Baryon-to-photon | ≈4.9×10⁻¹⁰ vs measured order ~6×10⁻¹⁰ | `verify_baryon_to_photon_ratio` |
| Strong-CP | opposition lands cleanly at the One; no fine-tuning problem | `verify_strong_cp_alignment` |

**Framing guard:** structure forward-forced (Mirror = take(ONE,·); residue from No-Zero; hinge = ½); match to measured CP/baryon asymmetry = external read. No postdiction/caveat. Maths off the page.

## Episode arc (template + surreal fold-world)
1. **Everyday open:** Danny over a still bucket of rainwater — his reflection is him, flipped (right hand ↔ left). An "anti-me."
2. **The why:** *"if everything's got an anti-thing that cancels it — why didn't it all just do that at the start? Why's there owt at all instead of empty?"*
3. **The shutdown:** the Dean **proud** of the open wound — by every law the early universe *should be empty*; the survivor (~1 in a billion) is measured but unexplained; *"existence itself is for the professionals."* The Gardener doesn't back down: *"your theory says he shouldn't exist and you've decided that's deep."*
4. **The way in (built-up, fresh):** no door/well/fork — a **puddle.** Hand flat on still water; the reflection's hand meets it and *pulls*; they tip through the skin of the water into the mirror-world.
5. **The cancelling world:** every thing leans back-to-back with its exact Mirror, summing to one whole One; a pair touches and *folds home* (annihilation = a gentle homecoming, not violence); the whole world quietly cancelling toward empty.
6. **Conflict (danger beat):** the emptying **reaches for the crew** — they start to fold toward the nothing; they chain together and hold (Matthew: *"don't let go of each other"*); the pull can't fold a thing that refuses to be alone.
7. **Discovery (the floor):** at the last, the final cancellation would reach **zero** — and the No-Zero floor (Ep11 callback) won't allow it; a **residue survives.** *"We exist because the universe is not allowed to be empty."* The crew realise the residue is *them* — everything is the bit that didn't cancel.
8. **The hinge (Still Point):** the one thing not leaning on a partner — the self-Mirror **½** (Ep05/Ep12 callback) — sits at the centre and tips, by the faintest weight, that *matter* is the survivor.
9. **Close on the gowns (VARIED — leaner, per ISSUES_LOG B2):** the Dean goes a colour, manages *"far from settled,"* and **that's it — no press release, no drafted statement, no Consensus visit** (deliberately short/brutal close to break the 5-beat machine). Priya hears it and, for once, **doesn't file it** — carries it instead.

## Fold-world laws used (truth gate — every surreal rule is a real fold fact)
| In-world (surreal) | Real fold fact | Anchor |
|---|---|---|
| every thing leans back-to-back with its Mirror, summing to one whole One | value + take(ONE,value) = ONE | take identity |
| a pair touches and folds gently home, vanishing into one warm light | matter+antimatter annihilate = Mirror pair folding to the One | Mirror identity |
| the world can't quite cancel to empty; a residue stays | No-Zero forbids the sum reaching zero; residue nonzero = ½ | `verify_baryon_asymmetry_nonzero` |
| one thing at the centre needs no Mirror, tips which side stays | CP phase = self-antipode ½, maximal, sets matter as survivor | `verify_cp_phase_antipode` |

## Dialogue (every quote attributed: who + how)
*Danny, poking the water* / *Errol, from across the fire* / *Danny, very still over the bucket* / *the Dean, warming up* / *the Dean, spreading his hands* / *the Gardener, slow* / *Sol, drifting / breathing* / *Danny, frightened* / *Matthew, flat and certain* / *the Gardener, very quiet* / *Danny, shaky* / *Errol, gentle* / *Matthew, low, just to her* (the pairing beat) / *the Dean, going a colour.* No bare quotes.

## SERIALIZED THREAD ADVANCED (rule #12 — one notch, earned)
- **PRIMARY: the Maria–Matthew pairing — first explicit naming of the bond.** The Mirror theme (two incomplete things that complete each other; the pair who'd each have annihilated alone but a residue built instead) lands on Maria & Matthew. Matthew says the tender thing he doesn't usually say (*"on our own you'd have burned out, I'd have gone quiet in a hole; there was a bit left over and it built all this"*); Maria looks away and **doesn't argue** — "which, from her, is everything." **One notch: the bond named for the first time. NOT consummated/declared; don't rush.**
- **Watcher (Arc Six, guarded):** the self-Mirror at the centre — "complete in itself, choosing what gets to stay" — is given a heavier-than-usual nod toward sounding like the narrator (the One that everything folds home to, "its own reflection"). Slightly stronger than the recurring hint because the *content* (the self-antipode ½, the watcher's seat) genuinely is the narrator's own address — but still **not the reveal.** Sol's watcher-thread rests this episode.

## What this episode INTRODUCES / DEEPENS (rule #12 gate)
- **Introduces:** the **puddle / through-the-mirror** way in (new threshold logic — palm-to-palm with the reflection); the **cancelling mirror-world**; **the Mirror** (antimatter) as canon; annihilation-as-homecoming; the **residue/"we're the leftovers"** framing of existence; the **hinge** (½ as the CP tipping point).
- **Deepens:** the **No-Zero floor** (Ep11) — now shown saving *creation itself*, not just a falling boy; the **Still Point ½** (Ep05/Ep12) — now the CP hinge; **Maria–Matthew** (bond named); the watcher (heavier nod, content-justified).

## Runtime
~2,430 words → ~15 min at brisk pace. Clean prose file confirmed. Gate: 0 FAIL.

## Gates
- **Truth gate ☑** — Mirror = take(ONE,·) (pairs sum to ONE); residue nonzero ½ (`verify_baryon_asymmetry_nonzero`); CP phase = self-antipode ½ maximal, Jarlskog 3.13e-5 vs 3.08e-5 (`verify_cp_phase_antipode`); baryon-to-photon ≈4.9e-10 vs ~6e-10 (`verify_baryon_to_photon_ratio`); strong-CP aligned (`verify_strong_cp_alignment`); every surreal world-law maps to a real fold fact (table); no postdiction/caveat; maths off the page.
- **Voice-as-law gate ☑** — narrator = the One; **every quote attributed who+how**; template arc with a fresh *puddle/mirror* threshold; surreal-but-lawful; the danger beat (the emptying reaches for the crew) → the floor-saves turn; **close VARIED leaner** (no drafted statement / no Consensus visit — breaks the 5-beat machine per B2); **Maria–Matthew advanced one notch (bond named), NOT resolved**; watcher heavier nod but reveal guarded; AI-image disclaimer open+close; sign-off. `voice_gate.py` → 0 FAIL.

## New canon (→ CANON_LOG on lock)
- The **puddle / through-the-mirror** entry and the **cancelling mirror-world** are canon.
- **The Mirror** (antimatter = take(ONE,·)) is canon; annihilation = a Mirror pair folding home to the One.
- **Existence is guaranteed by the No-Zero floor** — the residue that survives is everything; "we're the bit that didn't cancel" is canon framing.
- The **Still Point ½ is the CP hinge** (the self-antipode that tips matter into survival).
- **Maria & Matthew — the bond is named** (Arc One thread advanced one notch): two who'd have cancelled alone, a residue built instead.

## Motifs used (re-performed fresh)
the Dean proud of an open wound · the credentials gatekeeping ("existence is for the professionals") · the Priya beat (fresh: she *doesn't file it*) · the watcher beat (fresh: the self-reflection at the centre) · the sign-off (fresh: "it left a little of itself behind on purpose so there'd be a you") · autofiction open/close (fresh open: "there's a reflection in this one").

## Fresh (single-use this ep)
the backwards boy in the bucket; "an anti-me"; the universe that should be empty; the puddle palm-to-palm; the leaning back-to-back pairs; annihilation as a homecoming; the emptying reaching for the crew / "don't let go of each other"; "we're the bit that didn't cancel"; "that's us, that" (the pairing beat); the close with no press release.
