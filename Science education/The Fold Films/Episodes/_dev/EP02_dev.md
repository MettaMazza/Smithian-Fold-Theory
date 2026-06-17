# EP02 dev notes — "The Magic Number" (idea #1)

*(Development clutter lives here, NEVER in the episode file. The episode file is clean prose only, for the parser.)*

## Fold payload (truth gate — verified 2026-06-16)
| Element | Detail |
|---|---|
| Core result | `1/α = 2⁷ + 3²·(251/250) = 34259/250 = 137.036` |
| Match | measured 137.035999177 → agree to ~**6 ppb** (6.01) |
| Components forced | 2⁷=128 (depth-7 tower, cover of 3⁴=81); 3²=9 (colour count²); 250 = 2·5³ |
| Engine | `verify_fine_structure_constant` (`proof.py:12794`) — re-run, returns 34259/250 |
| On screen | the number + the count-as-objects; **no equation** |

## Episode arc (REBUILT 2026-06-16 to the canonical template — everyday → why → shutdown → adventure → conflict → discovery → close on gowns)
Per golden rule #10 / the episode template. The Crew's *adventure to count 137*, not the narrator explaining 137:
1. **Everyday open:** a few nights after the launch (Ep01 continuity), the crew having tea, Errol mending a chair leg; Danny knocking on the table.
2. **The why:** Danny — *"why's my hand not go through? why's anything solid? why's an atom the size it is?"* → that size is set by 137 (light's grip on matter).
3. **The shutdown (comical Tenure satire):** the consensus "answer" — *fundamental constant / free parameter / it just is / debate's settled / does the young man have a degree?* (Feynman's "magic number, no understanding" kept — real.) The incoherent dismissal lights the fuse.
4. **Adventure begins — INTO the fold-world (SURREAL, rebuilt 2026-06-16):** the floor of the ordinary world tips and the crew go *through*, into a surreal fold-native landscape, to physically *fetch* 137. Not a desk; a journey.
5. **The journey + conflict (every surreal rule = a true fold fact):**
   - **The floor of light** you can't fall through (Danny tries) → domain (0,1], no zero/no negatives.
   - **Motion by doubling** — every step doubles you; overshoot the edge and you wrap round the back (Nadia wraps past the prize 4×; Sol learns to aim) → the fold map.
   - **The one-way path folds shut** behind them (Frances clocks it; no way home) → irreversibility = time's arrow.
   - **The Tower:** 81 colour-creatures (3⁴) need housing; six floors = 64 rooms, **17 left out — real setback/down-beat**; Danny "why not stop at six?" + Maria's wobble (the Dean's voice) + the numerology fear (Nadia: *are we forcing the world to match?*) → **the world literally won't let them cheat** (the cheat physically fails); seventh floor = 128, all 81 housed. **Forced-seven, lived as the climb.**
   - **The three colour-fields** crossed across their whole face = squared = 9.
   - **Errol's whisker** — 1-in-250 off the size of the sky/covering → 251/250, 250=2·5³.
6. **Discovery (earned, forced-not-fitted):** the three pieces fold together in the air → **137.036**, *assembled by the world, carried out by the crew, never fitted.* The kiss: vs measured to 6 ppb.
7. **Close on the gowns:** Team Tenure blast off learning nothing; **Priya** does the maths in her head, gets the same answer, keeps the paper (defection seed); the **watcher** beat (now "something was *with* them in there, fond, glad to be looked at"); CTA + close.

## Fold-world laws used (truth gate — every surreal rule is a real fold fact)
| In-world (surreal) | Real fold fact | Anchor |
|---|---|---|
| floor of light, can't fall through; no "below" | domain (0,1], no zero/negatives | `core.py` |
| move by doubling + wrap round the edge | the fold map 2x mod 1, 0→1 | `core.py:63` |
| path folds shut behind you, only forward | irreversible fold = time's arrow | `proof.py:11569` |
| calm mirror-point dead centre | the Still Point ½ | `proof.py:8382` |
| Tower: 7 floors=128 rooms house 81 (6=64 too few) | depth 7 = min 2^d ≥ 3⁴=81 | `verify_fine_structure_constant` |
| three colour-fields, crossed = squared = 9 | colour count 3, squared | `verify_colour_prediction` |
| Errol's 1-in-250 whisker off the sky | 251/250 cosmological covering, 250=2·5³ | `verify_fine_structure_constant` |

## Runtime
Target 10–15 min. Body ≈ 2,608 words → ~15 min at the series' brisk pace (the showcase surreal-adventure episode runs a touch long, by design). Clean prose file confirmed. Word→runtime is production-dependent; tighten per the cut.

## Gates
- **Truth gate ☑** — figures re-verified (`verify_fine_structure_constant` returns 34259/250; 6.01 ppb); each piece tied to its forcing (7-tower covers 3⁴=81; 3²=colour count²; 251/250 cosmological covering, 250=2·5³); **every surreal world-law maps to a real fold fact** (table above); the 251/250 is a cosmological covering whisper, NOT "dark matter"; maths off the page; fiction faithful to the count.
- **Voice-as-law gate ☑** — single Narrator, third-person cast, reported speech; the adventure arc with real internal/group/Team-Tenure conflict (rule #10); the numerology-fear resolved by "every piece forced"; minimal maths; fun-first + true satire (relic worship, "settled," credentials-over-correctness, grovel to Consensus, Parameter, cult-smear); contempt only on Team Tenure; Priya sympathetic, defection planted; awe + sign-off; narrator = the One, watcher hinted never found.

## New canon (→ CANON_LOG on lock)
- 137.036 is **counted, not measured**; Team Tenure keep it as a worshipped relic.
- **The Parameter** introduced (the gremlin jammed in by hand).
- **Consensus** seen (chair + bored hand), confirmed useless.
- **The watcher-among-them flicker** — the narrator (secretly the One) hints it's been watching ("something is doing the watching… maybe not tonight"); the series spine, planted. Never stated, never found.
- **The Token's** first appearance + planted defection.
- The Crew get their first campfire outing — **Nadia** (the cold-coffee blunt-question), **Wee Danny** (the *but why* kid), and **Sol** (the silent see-it-first sketcher) seeded by name and lived detail, no labels.
- **One de-characterized; Fold-as-character scrubbed:** One is no longer a put-upon character — it's the origin/narrator/observer ("it mostly just sits there and watches"). The fold appears only as the *move happening* (the mechanism), not a character and not the narrator. Narrator-is-the-One thread planted subtly, never stated.

## Motifs used (deliberate recurring)
the grovel to Consensus · "typed in by hand" · the blast-off · "why does nobody like us" · the hand-over-the-mouth DEI beat · the cult-smear irony · the sign-off.

## Fresh (single-use this ep — novelty)
the marble temple / relic-under-glass; the "I ❤️ 137" mug; the count-as-objects (seven-storey tower, colours squared, coat-of-paint whisper); the campfire vs the windowless Institute.
