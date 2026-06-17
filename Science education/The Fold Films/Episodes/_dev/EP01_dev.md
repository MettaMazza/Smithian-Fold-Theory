# EP01 dev notes — "Welcome to the Fold" (world-building pilot)

*(Development clutter lives here, NEVER in the episode file. The episode file is clean prose only, for the parser.)*

## Purpose
The pilot (everything else shifted up one). A world-build/launch episode — the **exception** to the adventure-arc rule (golden rule #10): it cracks no single constant; the *world* is the payload.

## Structure (REBUILT 2026-06-16 to the canonical template, scaled to launch the series)
Per golden rule #10 — the pilot runs the **same engine** (everyday → why → Tenure shutdown → adventure → … → close on gowns), with the shutdown doubling as the scathing consensus-world tour and the "adventure" being the founding of the whole mission:
1. **Everyday open:** an ordinary night at the fire — Errol's kettle on a stone, Nadia's cold coffee, Sol drawing in the soot, Frances on the edge of the warmth, Maria poking the fire, Matthew watching her; Wee Danny flat on his back looking up. We meet everyone through behaviour (show, not tell).
2. **The (biggest) why:** Danny — *"where does it all come from? why's anything the size it is? why's there stuff instead of nothing?"*
3. **The shutdown = the scathing tour:** they ask the experts; Team Tenure's "answer" is the savaging of the consensus world — measuring mystery-numbers to 12 places & explaining none; *free parameters = typed in by hand and we don't know*; *who let you in*; Consensus the bored hand; the graveyard (Semmelweis / Wegener / Marshall / Shechtman); consensus = headcount, never proof.
4. **The adventure begins:** being told the biggest why is "none of his business" galvanizes the Gardener — *if they won't and can't tell him, we'll work it out ourselves, from scratch, no permission.* The founding of the mission.
5. **The foundations = the first surreal glimpse of the fold-world:** framed not as a chalkboard but as a *place* — the Gardener takes the first step *in* and we get a taste of the surreal-but-lawful world the series adventures into (floor of light you can't fall through, motion by doubling-and-wrapping, the one-way path, the mirror Still Point, the four families/never a fifth). Establishes that **answers are fetched from inside that world, not told** — and tees up Ep02 ("starting tomorrow, with the magic number"). The radical bet: one seed, one move, **no dials**; the gowns can't read it because reading it defunds them.
6. **The ones who'll read it:** the crew named & lived (Maria/Gardener, Matthew [academic→army dropout], Nadia, Sol, Errol, Wee Danny, Frances); each an archetype of the academically disenfranchised.
7. **Close on the gowns:** the Institute laughs it off, checks with Consensus, goes back to measuring — unaware they've been lit under. The buried thread: **in the act of observing, the Crew are the One folding — unaware**; watcher beat; CTA + close.

A world-build/launch episode: names and lives BOTH camps, savages the consensus world, lays the foundations, sets up the war. No single headline constant — the *world* is the payload.

## Fold payload (truth gate — all established world-canon, no new numerics)
| Element | Detail | Anchor |
|---|---|---|
| One | the single starting being | `core.py:124` |
| The move (fold) | double, wrap overflow round the back (2x mod 1, 0→1); the **move/mechanism** — not a character, not the narrator | `core.py:63` |
| The One | the origin **and the narrator/observer** (not a character); accompanies the Crew as the act of observation, never found | `core.py:124` |
| The floor | no Nothing — no zero, no negatives; domain (0,1]; why nothing crashes to 0/∞ | `core.py:34` |
| One-way fold = time's arrow | two parents → one child, irreversible | `proof.py:11569` |
| The Still Point | ½, self-mirror, folds home to One in one step | `proof.py:8382` |
| Prime families | 2,3,5,7 are the forces; never a fifth | `prime_force_phenomenology.py` |
| Zero free parameters | "no dials, nobody typed anything in" — the series' spine claim | (corpus-wide) |
| History (real, documented) | Semmelweis (handwashing, died in asylum); Wegener (continental drift ridiculed→vindicated); Marshall & Warren (H. pylori ulcers, self-experiment, Nobel 2005); Shechtman (quasicrystals "impossible," told to leave, Nobel 2011) | SATIRE_BANK "core irony of Consensus" |

All facts are established canon or documented history — nothing here needs an engine re-run; the truth gate is satisfied by faithful depiction.

## Runtime
~2,422 words incl. top/tail disclaimers. Target 10–15 min; lands ~14 at the brisk pace. Clean-prose file confirmed (no tables/dev clutter in the episode). Word→runtime is production-dependent.

## Gates
- **Truth gate ☑** — laws depicted faithfully (the move/fold = the mechanism, the floor, one-way time, Still Point, four families, zero dials; One = origin/narrator/observer); history accurate; maths off the page (zero equations); fiction faithful to the corpus.
- **Voice-as-law gate ☑** — single Narrator; cast third-person, reported speech; narrator talks straight to YOU (frame), in-story characters never turn to camera; minimal maths; fun-first + true satire (consensus = headcount-not-proof, the graveyard, gowns/grovel, tokenism on Priya = on the men never her, no-dials); contempt only on Team Tenure; Priya sympathetic + defection planted; awe; autofiction open/close; swearing earned ("bellends," "get knotted," "monkey brain").

## New canon (→ CANON_LOG on lock)
- The world's laws fixed as story-canon (One = origin/narrator/observer; the move/fold = the mechanism; the floor, Still Point, four families, one-way time, zero dials).
- **The Crew named & lived:** Maria (the Gardener, self-taught anti-hero), Matthew (the tether), Nadia (cold-coffee blunt-question), Sol (silent see-it-first sketcher), Errol (dropped-spanner toolmaker), Wee Danny (the *but why* kid), Frances (ex-Tenure, flinches at "tenure").
- **Team Tenure named:** the Dean (leader), Crispin (sycophant), Priya (sharpest & most ignored — defection planted), Rupert (optics/PR), + Consensus (the unseen boss, "a chair, a bored wave").
- The consensus-graveyard history is canon backdrop.
- **The series-spine thread planted, never stated:** the narrator is secretly the **One** — present as the act of observation, the watcher among them — hinted ("don't worry about who's actually talking… or why it talks about the start like it was *there*… I was the start of it"), never confirmed, never found.

## Motifs used (deliberate recurring)
the no-dials / "nobody typed anything in" · the grovel to Consensus · consensus = headcount-not-proof · the cold white building vs the fire · the Gardener · the autofiction open/close · "go and check it yourself."

## Fresh (single-use this ep — novelty, retire after)
the no-plughole floor · un-ring a bell / un-say the thing to your nan · sharp as a smashed bottle · dry as month-old toast · dropped-spanner (Errol's signature — may recur AS his motif) · "an ego with a man somewhere inside it" · Crispin laughing half a second early · the prop-on-a-stand spin-to-camera · the graveyard with the carved stones · "a barman who's stopped serving you" (the no-fifth-force gag).
