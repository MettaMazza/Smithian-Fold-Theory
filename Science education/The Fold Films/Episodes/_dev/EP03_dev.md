# EP03 dev notes — "Mate in a Billion" (idea #2; was "The Chess Heist")

*(Dev clutter only. Episode file is clean prose. Title evolved from "The Chess Heist" → "Mate in a Billion" when the episode was rebuilt from a desk-bound heist into a surreal on-the-board adventure, 2026-06-16.)*

## Fold payload (truth gate — verified 2026-06-16)
| Element | Detail | Anchor |
|---|---|---|
| Core result | the One + the fold solve chess **endgames** exactly, certified vs independent Syzygy tablebases | `fold_chess/CHESS_RESULTS_FINAL_FIVE_PIECE.md` |
| Headline figure | **1,092,871,108 positions checked vs independent ground truth, 1,092,871,108 agreements, ZERO errors** | `:26-27` |
| Five-piece | **1,054,075,064** legal positions solved exactly, zero errors | `:56,64` |
| Fortresses | **382,468,048** drawn fortresses correctly identified (the "hold-out" beat) | `:66` |
| Universal solver | same engine solves **Nim** (Bouton's XOR) + a third game, zero disagreements — impartial games ARE the fold's binary/carry-free arithmetic | `fold_theorems5.py`; results doc Nim section |
| **Truth-gate guard** | reality: *full* chess is unsolved; what's solved = **endgame tablebases**. The episode is explicitly an **endgame** ("you don't have to solve all of chess to solve the bit you're standing in") — never claims full chess solved. | — |
| On screen | the *numbers* land as gut-punches; no equations | — |

## Episode arc (template + surreal fold-world, REBUILT 2026-06-16 to Maria's beat)
1. **Everyday open:** night after the 137 win; the crew playing **Nim** (matchsticks) by the fire; Danny's lost 11× to Errol.
2. **The why:** Danny — *"is there just a right move, always? could you KNOW the perfect move every time? has anyone ever solved a game?"*
3. **The shutdown:** Team Tenure swoops; the Dean — *chess can't be solved, more positions than atoms, "a computer larger than creation," put the matchsticks away.* **BUT post-137 the crew don't back down** — the Gardener, flat: *"we counted the number your whole temple can't explain. Last Tuesday. I think we'll manage a board game, pet."*
4. **Tenure shrinks them (the surreal adventure):** the Dean, furious at the cheek, snaps his fingers and **shrinks the crew to pawn-size onto a giant live board** — a lethal endgame — *"solve it from down there. Lose, and you don't go home."*
5. **The board + conflict (every rule a true fold fact):** the fold **knows the true value of every position** (won/lost/drawn, exact) → perfect play; the winning move is always the *boring* one (Nadia calls it, Errol has the nerve to trust it). **Internal/group:** Maria tries a flash move, nearly gets them killed, Matthew hauls her back (*"the fold's telling you the answer — for once take the boring move!"*) → her arc: right means doing the unspectacular true thing. **The fortress:** forced where they can't win, the fold finds an unbreakable **drawn fortress** (382M of them) and they hole up while the Dean sweats. One-way / no take-backs raises stakes.
6. **Mate / resolution:** Errol sees the forced mate; fold-perfect play topples the Dean's king; they snap back to **full size**, alive. Off-board, the treasure stated plain: the fold computes the exact truth of every endgame position, **a billion+ checked vs the world's own tables, zero errors**, + Nim + a third game — the one shape under all of them — all checkable by anyone.
7. **Close on the gowns:** the Dean *"this proves nothing, raises serious questions,"* grovel to Consensus, blast off; **Priya** watched them win on pure trust-the-truth and it moved her (defection deepens); the **watcher** beat (*something minding them on the board*); CTA → PV02; close.

## Fold-world laws used (truth gate — every surreal rule maps to a real fold fact)
| In-world (surreal) | Real fold fact | Anchor |
|---|---|---|
| shrunk onto a lethal endgame; "solve the bit you're in" | endgame tablebases (few pieces) are solved; full chess is not | `CHESS_RESULTS_FINAL_FIVE_PIECE.md` |
| every position has a fixed true value (won/lost/drawn) → perfect play | exact solved values, 1.09bn checked vs Syzygy, 0 errors | `:26-27`, `fold_solve5.py` |
| the unbreakable fortress they hide in | 382,468,048 drawn fortresses, exactly identified | `:66` |
| can't un-move; only forward | the fold is one-way / irreversible | `proof.py:11569` |
| Danny's matchsticks (Nim) solved by the same shape | impartial games = nim-values = XOR = the fold's binary arithmetic | `fold_theorems5.py` |

## Dialogue (new rule — every quote attributed: who + how)
All quotes carry the speaker and manner so the single-voice audio render is never ambiguous: *Danny, slapping the dirt* / *Errol, lifting one matchstick without hurry* / *the Gardener, flat as a paving slab* / *Matthew shouted (the only time all series he raises his voice)* / *Errol… said the second full sentence he'd said all night.* Checked: no bare floating quotes.

## Runtime
~2,528 words → ~15 min at brisk pace (expanded 2026-06-16 to the full-15 rule with the open-lane gauntlet beat + the fuller fortress siege). Clean prose file confirmed. Word→runtime is production-dependent.

## Gates
- **Truth gate ☑** — figures verified vs the certified record; framed as **endgames** (no over-claim of full chess); every surreal board-law maps to a real fold fact (table above); maths off the page.
- **Voice-as-law gate ☑** — narrator = the One, fireside, direct-to-you; **every quote attributed who+how** (new rule); template arc (everyday → why → shutdown → they-don't-back-down → shrink → board adventure → mate → close on gowns); real internal/group conflict (Maria's flash-move row = her arc); strong swearing earned; contempt only on Team Tenure; **Priya** defection deepens; watcher hinted never found; AI-image disclaimer open+close; sign-off.

## New canon (→ CANON_LOG on lock)
- The chess proof is canon: a billion+ endgame positions, zero errors vs independent tables; same engine solves Nim + a third game.
- **Maria's arc beat:** the menace learns to take the *boring, true* move over the flashy one (Matthew the one who lands it).
- **Post-137 confidence** is now canon: the crew no longer shrink from Team Tenure on sight.
- **Team Tenure escalate to outright (cartoon) violence** (shrinking, the murder-board) — and still lose; can't gatekeep a self-verifying result.
- **Priya** moved by watching the crew win on trust-the-truth — defection arc advanced.

## Motifs used
the grovel to Consensus · the Parameter / "typed in by hand" (light) · the blast-off · "why does nobody like us" · credentials gatekeeping · the watcher beat · the sign-off · autofiction open/close.

## Fresh (single-use this ep)
Nim by the fire / Danny's losing streak; shrunk-to-pawn-size on a live murder-board; "solve it from down there"; the boring-move-is-the-winning-move; the fortress hold-out / the Dean sweating; the felled-chimney king; "I think we'll manage a board game, pet."
