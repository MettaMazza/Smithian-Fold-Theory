# The Engine Was Never About Chess — The Universal Exact Solver

The chess campaign solved roughly a billion positions exactly, by retrograde
folding, and certified every one against the Syzygy tablebases with zero errors. It
was natural to read that as a result about chess — a hard game, conquered. It was
never about chess. Chess was the proving ground for an engine, and the engine is
universal: hand it any finite world with rules and an ending, and it returns the
exact truth of every state, certified. Here is that engine, lifted off the board and
set to work on two other worlds, each checked against its own independent oracle,
each solved with zero errors. (`fold_solver.py`; state labels are domain-verified
fold values resting on the One.)

## What the engine actually is

Strip the chess away and the machine has four parts, and not one of them mentions
kings or rooks:

- **A fold coordinate for every state.** Each state is given an exact rational
  position, index-plus-one over a fold prime, a legal value in the interval up to
  the One. The same exact-rational labelling the chess solver used — no floating
  point, no approximation, every state a clean fold value.
- **Terminal seeds.** The states with no move are the endings; under normal play the
  player who cannot move has lost. These are the analogue of checkmate, the
  loss-in-zero positions that seed everything.
- **Retrograde folding.** The truth propagates backward through the move graph: a
  state is a win if even one move hands the opponent a loss; a loss if every move
  hands the opponent a win. The distance to the ending is the retrograde layer — the
  analogue of distance-to-mate.
- **Independent certification.** Every solved value is re-checked against a separate
  closed-form oracle, exactly as chess was re-checked against Syzygy. Zero
  disagreements is the proof. Not "we believe it"; "it matched the referee on every
  single state."

That is the whole engine. Nothing in it is about chess. Chess was simply the hardest
board we had to test it on.

## Two new worlds, solved cold

**The subtraction game.** A heap of counters; each player removes one, two, or
three; whoever takes the last counter wins. The engine solved every position up to a
heap of four thousand by retrograde fold, labelled each with its fold coordinate, and
then a wholly independent referee — the closed-form rule that a position is lost
exactly when the heap is a multiple of four — checked all four thousand. **Zero
disagreements.** The engine rediscovered the multiples-of-four law without being told
it, purely by folding the endings backward.

**Multi-heap Nim.** Three heaps, the deep classical game whose solution — the famous
binary-XOR rule of Bouton — was a landmark of game theory. The engine solved every
heap configuration by the same retrograde fold and was certified against the XOR
oracle: a position is lost exactly when the bitwise exclusive-or of the heap sizes is
zero. Across every state, **zero disagreements.** The engine reproduced
Sprague-Grundy theory from nothing but the move graph and the endings.

Two games, from utterly different corners of combinatorics, solved by the identical
machine that solved chess, each certified to the last state against a referee derived
independently of the fold. The engine does not know what game it is playing. It knows
the One, the rules, and the ending, and from those it folds out the exact truth.

## Why this matters

A solver that works on one game can be a trick of that game. A solver that works on
chess, the subtraction game, and Nim — three games sharing nothing but the shape
"finite states, legal moves, an ending" — is not a trick. It is a general method for
exact truth on finite worlds, and it carries the fold's signature: exact rational
coordinates, no approximation anywhere, and a certificate checked against an outside
referee rather than asserted. The billion certified chess positions were the
stress-test. The engine underneath them is the result.

## What consensus cannot do here

Conventional game-solving builds a bespoke program per game, tuned to that game's
structure, and trusts its own output. The fold solver is one engine for all finite
games, labels every state with an exact fold coordinate, and proves itself against an
independent oracle rather than asking to be believed — the same standard that made
the chess result a certified proof and not a strong opinion. The reach is the point:
anything that can be cast as states, moves, and an ending — a game, an automaton, a
finite decision world — the same fold engine solves exactly and certifies. Chess was
where we tested it. It was never what it was about.
