# EP09 dev notes — "Four to One" (idea #9 — the 4:1 LFV prediction)

*(Dev clutter only. Episode file is clean prose. Pairs with PV08 — Four to One.)*

## Fold payload (truth gate — re-run 2026-06-16, `lfv_spectrum.py`)
| Element | Detail | Anchor |
|---|---|---|
| Channels | e=1/4, μ=1/2, τ=3/4; rate ∝ separation² (B-9N) | `derive_lfv()` |
| Headline | **τ→e : τ→μ = 4:1** (rates 1/4 vs 1/16; τ prefers the farther jump) | `derive_lfv()` |
| Full spectrum | (μ,e) 1/16; (τ,e) 1/4; (τ,μ) 1/16 | `derive_lfv()` |

**Framing guard:** a **standing forward target** (not yet measured) — same forward forced derivation as the rest, aimed at an uncatalogued number. Frame as a falsifiable **bet placed in advance** (hand them the stopwatch); falsifiability = strength. **NEVER** postdiction/retrodiction, "real prediction," or ranking above other results.

## Episode arc (template + surreal fold-world)
1. **Everyday open:** a betting game by the fire (Nadia cleaning Danny out at coins); Danny — *"nobody can call a thing before it happens, you just got lucky."* The Gardener — *"if you know the rule the thing runs on, you can call it stone dead before it happens."*
2. **The why:** Danny (joining it to the chord) — *"the tau changes into the lighter ones — which does it pick, electron or muon? and can you call it, in advance, for definite?"*
3. **The shutdown:** the Dean — *"we would never be so reckless as to PREDICT a ratio… we measure, then explain why it was always going to be that"* (the never-commit / measure-then-postdict posture) + amateur jab. Crew don't back down: the Gardener — *"that's a bookie who only takes bets after the race. We'll call it. In advance."*
4. **Adventure — onto the channels:** three glowing channels at 1/4 (e), 1/2 (μ), 3/4 (τ); the tau fizzing on the high channel, about to jump; Sol reads the world's rule — *"rate of a jump goes as the distance. Squared."*
5. **The bet + the far leap (discovery, counterintuitive):** the Gardener calls for bets — Danny (and Nadia, Errol) bet the **near** hop (muon, "it's closer"); the Gardener works the rule and bets the **far** leap (electron: twice the distance, squared = 4× the rate). They watch & count — τ→electron wins **4:1**. Danny loses (the far jump wins because rate ∝ distance²).
6. **The wager to the world:** not yet measured → the Gardener writes **FOUR TO ONE** in the dirt, *in advance, no take-backs*, and hands the world the stopwatch — the opposite of measure-then-explain. **Maria's arc:** the courage to bet a falsifiable number in public.
7. **Close on the gowns:** they're *frightened*, not angry — a public number can be *wrong* in public (*"they've left themselves nowhere to hide!"* — missing that that's the point); *"On The Inadvisability Of Specific Claims"*; grovel to Consensus; blast off; **Priya** writes FOUR TO ONE, feels the wish *to be allowed to be wrong out loud* (defection advancing — strongest yet); the **watcher** beat (something kept count, "known the odds since before there were channels"); CTA → PV08; close.

## Fold-world laws used (truth gate — every surreal rule is a real fold fact)
| In-world (surreal) | Real fold fact | Anchor |
|---|---|---|
| three channels at 1/4, 1/2, 3/4 | generation standing-mode positions | `derive_lfv()` |
| flavour-change = a jump between channels | lepton flavour violation | docstring |
| jump-rate goes as distance, squared | rate ∝ separation² (B-9N) | `derive_lfv()` |
| tau prefers the FAR leap (electron) 4:1 | τ→e:τ→μ = (1/2)²:(1/4)² = 1/4:1/16 = 4:1 | `derive_lfv()` |

## Dialogue (every quote attributed: who + how)
*Danny, scowling at the coin in Nadia's hand* / *the Gardener, not even looking up* / *the Dean, recoiling as though slapped* / *the Gardener, flat, standing up* / *Sol, going still, reading it off the air* / *Danny, going straight in (learned nothing from the coins)* / *Sol, quietly delighted* / *the Dean, pale.* No bare quotes.

## Runtime
~2,514 words → ~15 min at brisk pace (expanded 2026-06-16: the coin-game open + "you can't call it", the fizzing tau + the rule-rewards-distance strangeness, the whole-crew-bets-near beat, the far-leap surprise with faces falling, Danny's turnaround "you actually called it", the weight of the public wager). Clean prose file confirmed.

## Gates
- **Truth gate ☑** — spectrum re-run; channels 1/4,1/2,3/4; rate ∝ sep²; 4:1; not-yet-measured → framed as a forward bet (no match claimed); every surreal world-law maps to a real fold fact (table); **no postdiction/ranking, no hedge** (falsifiability = strength, stated with conviction); maths off the page.
- **Voice-as-law gate ☑** — narrator = the One, fireside, direct-to-you; **every quote attributed who+how**; template arc (everyday → why → shutdown → don't-back-down → channels → the bet/far-leap conflict → wager-to-the-world → close on gowns); surreal-but-lawful; **the never-commit-vs-bet-in-advance satire** (fair critique of consensus unfalsifiability; does NOT touch the fold's forward derivations); Maria's arc (bet the number, hand over the stopwatch); Priya defection advances furthest yet (the wish to be allowed to be wrong out loud); watcher hinted never found; AI-image disclaimer open+close; sign-off.

## New canon (→ CANON_LOG on lock)
- The LFV spectrum is canon: channels 1/4,1/2,3/4; rate ∝ separation²; τ→e:τ→μ = 4:1 (a standing forward bet, not yet measured).
- **The "bet the number in advance, hand them the stopwatch" ethos** is canon for the Crew — explicitly contrasted with Team Tenure's measure-then-explain / never-commit posture.
- **Priya's defection advances furthest yet:** the wish to be allowed to be wrong out loud.
- **Maria's arc beat:** the courage to commit a falsifiable number in public.

## Motifs used
the grovel to Consensus · the blast-off · "why does nobody like us" · credentials gatekeeping · the watcher beat · the sign-off · autofiction open/close.

## Fresh (single-use this ep)
the coin-betting game / "you just got lucky"; the three jumping-channels; "rate goes as distance, squared"; the far-leap-wins surprise; FOUR TO ONE written in the dirt; "a bookie who only takes bets after the race"; "the wish to be allowed to be wrong out loud."
