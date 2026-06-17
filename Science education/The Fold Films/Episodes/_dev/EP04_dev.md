# EP04 dev notes — "The Edge of the Map" (idea #3 — two new forces)

*(Dev clutter only. Episode file is clean prose. Pairs with PV03 — Two New Forces.)*

## Fold payload (truth gate — re-run 2026-06-16, `prime_force_phenomenology.py`)
| Element | Detail | Anchor |
|---|---|---|
| Forces = prime sectors | known 2 (electroweak), 3 (strong); **new 5, 7**; seal at 7 | `derive_ladder_bound()` → realized {2,3,5,7}, bound 7, no force at 11 |
| Carrier count = p²−1 | 3→**8 gluons (real anchor)**; 5→**24**; 7→**48** | `derive_mediators_and_colours()` |
| Colours = p | 3, then **5**, then **7** | same |
| Coupling (p−1)/p | strong 2/3; new **4/5**, **6/7** (fiercer up the ladder) | `derive_couplings()` |
| Confining | both new forces confine → hidden (charges never come out free) | `derive_carrier()` (confining width ½) |
| The seal | **no force at 11** — four families, never a fifth | `derive_ladder_bound()` |

**Truth-gate guard:** the two new forces are the **same forward forced derivation as every other corpus result** — they simply target a quantity the labs haven't catalogued yet (NEVER call any corpus result a "postdiction/retrodiction" — all are blind forward derivations; this is a standing instruction). The episode presents them as forced/derived (no hedge) and explains *why unseen* (confinement). The 8-gluon count is the real, known anchor the rule nails first.

## Episode arc (template + surreal fold-world)
1. **Everyday open:** after the chessboard; Errol's fridge magnet, Danny feeling two magnets push against nothing.
2. **The why:** Danny — *"how many forces are there? why four? what if there's ones we can't feel? how would you know you'd found them all?"*
3. **The shutdown:** the Dean — *"we have found them all. Four. The search is complete… because we would have SEEN it"* (confidence, not argument) + the credentials jab. **Crew don't back down** (post-137/chess): the Gardener — *"right. Let's go and count them ourselves."*
4. **Adventure — into the country of families:** the fold-world laid out as a rising land of family-regions, each with its own *grip.*
5. **The journey + conflict:**
   - **2-family** (electroweak, 3 carriers), then **3-family** (strong): 3 colours, Nadia counts **8** carriers, Errol names the rule — *"three, squared, take one"* — the known gluon count → the rule keeps going. The strong region **confines** (clamps them in; they fight out) — confinement made physical.
   - Past the gowns' "edge": the **5-family** (5 colours, **24** carriers, grip 4/5, confining → Frances: *"it's not missing, it's hiding"*) and the **7-family** (7 colours, **48** carriers, grip 6/7, confining harder). Two new hidden forces.
   - **Internal/group:** Danny (and Maria) want a *fifth* — the romance of more; Danny runs up the slope toward an 11-family.
6. **The edge / discovery:** the land just **ends** — a clean drop, no 11-region. Errol: *"that's the lot. It stops at seven."* Maria's arc beat: she wanted a fifth as much as anyone, but makes herself say the true thing over the thrilling one — *"we don't get to want it into existence — that's their game. It's four. And that edge is the most beautiful thing we've found all year."*
7. **Close on the gowns:** the Dean flip-flops (*"we found them all"* → *"obviously infinitely many"*) — wrong in both directions in one breath; grovel to Consensus; **Priya** checks 24 against the 8 gluons, holds the paper a little longer now (defection deepens); blast off; the **watcher** beat (*something counted along the whole way, fond of "four and no more"*); CTA → PV03; close.

## Fold-world laws used (truth gate — every surreal rule is a real fold fact)
| In-world (surreal) | Real fold fact | Anchor |
|---|---|---|
| country of family-regions, each with its own "grip" | forces indexed by prime sector; coupling (p−1)/p | `derive_couplings()` |
| count the carriers in a region = colours² − 1 (8, 24, 48) | carrier count p²−1 (3→8 gluons known) | `derive_mediators_and_colours()` |
| regions clamp you in / hide their charges | confinement; confining carriers | `derive_carrier()` |
| past the known edge: a 5-region and a 7-region | sectors 5,7 are forces (B-7N) | `prime_force_phenomenology.py` |
| the land ends — a void where 11 should be | ladder sealed at 7, no force at 11 | `derive_ladder_bound()` |

## Dialogue (every quote attributed: who + how)
*Danny, grinning, pressing the two magnets together* / *Errol, taking his magnet back* / *the Dean, spreading his hands* (warmth = most dangerous version) / *the Gardener, low, to the crew, not to him* / *Nadia, jaw near the floor* / *Frances, walking through it stunned* / *Errol… the second thing he'd said all trip* / *Maria, who wanted it just as bad.* No bare quotes.

## Runtime
~2,427 words → ~15 min at brisk pace (expanded 2026-06-16: the terrain/doubling-travel beat, the electroweak open, the 5-family near-trap, the 7-family worse-grip + Errol's seal-clue). Clean prose file confirmed. Word→runtime is production-dependent.

## Gates
- **Truth gate ☑** — figures re-run; 8 gluons = the known anchor; p²−1 → 24, 48; seal at 7 (no force at 11); new forces framed as a forced *prediction* with the confinement reason they're unseen; every surreal world-law maps to a real fold fact (table); maths off the page.
- **Voice-as-law gate ☑** — narrator = the One, fireside, direct-to-you; **every quote attributed who+how**; template arc (everyday → why → shutdown → don't-back-down → into the fold-world → conflict → discovery → close on gowns); surreal-but-lawful adventure with ups/downs (confinement traps, the romance-of-more vs the seal); Maria's arc (truth over the thrilling thing); Priya defection deepens; watcher hinted never found; AI-image disclaimer open+close; sign-off.

## New canon (→ CANON_LOG on lock)
- **Two new forces are canon:** sectors 5 (5 colours, 24 carriers, 4/5) and 7 (7 colours, 48 carriers, 6/7), confining/hidden; the ladder **seals at 7** (no force at 11) — four families, never a fifth.
- The carrier rule **p²−1** is canon (nailed the 8 gluons).
- **Maria's arc:** refuses to "want a thing into existence" — truth over the thrilling story (the anti-Tenure virtue).
- **Priya** holds the paper longer now — defection advancing.

## Motifs used
the grovel to Consensus · the blast-off · "why does nobody like us" · credentials gatekeeping · the watcher beat · the sign-off · autofiction open/close · the Dean flip-flopping/wrong-in-both-directions.

## Fresh (single-use this ep)
the fridge magnet open; the "country of families" with per-region grip; counting carriers as creatures (8/24/48); "three, squared, take one"; the confinement-clamp you fight out of; running off the literal edge of the map; "a universe that knows exactly when to stop."
