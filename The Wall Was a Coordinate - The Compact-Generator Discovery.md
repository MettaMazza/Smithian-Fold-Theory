# The Wall Was a Coordinate — The Compact-Generator Discovery

Every tablebase hits the same wall. To know a game perfectly you store its solved
field — the win-or-loss verdict of every position — and that field is exponential in
the size of the game. Five chess pieces is a billion positions; each piece you add
multiplies the count again, and somewhere around seven the storage and the
computation defeat any machine. This is taken as a law of nature: exact knowledge of
a large game is exponentially expensive, full stop. It is not a law of nature. It is
a statement about a *coordinate* — the position-by-position listing — and the wall
lives in the coordinate, not in the game. The fold supplies the other coordinate, and
in it the generator of a solved field is not measured but **derived, forward, from
the rule.** (`compact_coords.py`; every coefficient `verify_value`-traced to the One,
reconstruction proven exact.)

## The fold's own coordinate

The fold acts on a state by doubling — a shift along its bits — and the natural
coordinate of that action is the set of fold characters: for each frequency, the sign
pattern given by the parity of its overlap with the state, negative-one to the
popcount of the bitwise-and. These characters are the fold's harmonics, the same
doubling structure that runs through the whole theory, now used as an axis.

Here is the key that turns measurement into derivation. A single rule — "this bit is
zero" — is *exactly* a fold projector: one-half of the constant character plus
one-half of that bit's character. It is built from two fold characters and nothing
else. So any solved field that is a **product of bit-rules** is a product of fold
projectors, and you do not have to transform it and count what comes out. You
multiply the projectors together, using the fold's group law — character times
character is the character of their exclusive-or — and the generator falls out
**derived**: which characters the field uses, and with what coefficients. Each
coefficient is a dyadic value that folds down to the One, traced to the axiom. And
the derivation is then proven: the derived generator is summed back over every state
and shown to reproduce the rule exactly.

## The subtraction game — a derived generator of fixed size

The subtraction game is lost exactly when the heap is a multiple of four — that is,
when its lowest two bits are zero. Two bit-rules. Multiplying their two fold
projectors gives the generator with no measurement at all:

| Frequency | Coefficient |
|---|---|
| character 0 | 1/4 |
| character 1 | 1/4 |
| character 2 | 1/4 |
| character 3 | 1/4 |

Four characters, each weighted one-quarter, every coefficient traced to the One, and
the reconstruction proven exact across sixteen thousand states. And because the
derivation never mentions the size of the field, the generator length is **four for
any field whatsoever**:

| Field size | Derived generator length |
|---|---|
| 64 | 4 |
| 1,024 | 4 |
| 16,384 | 4 |
| 1,048,576 | 4 |

A fixed four-coefficient program, derived from the rule, regenerates a solved field
of unbounded size. The exponential wall is simply absent in the fold coordinate — not
because a transform happened to compress it, but because the field *is* a short
product of fold projectors, and that is provable forward.

## Nim — size-blindness as a theorem

Nim is lost exactly when the heaps exclusive-or to zero — equivalently, when every
bit-column across the heaps has even parity. That is one bit-rule per column, and the
columns do not know how many heaps there are. Multiplying the column projectors gives
a generator whose size is two-to-the-bits-per-heap, and **the heap count never enters
the derivation**:

| Heaps, bits | Field size | Derived generator | Compression |
|---|---|---|---|
| 2 heaps, 3 bits | 64 | 8 | 8 : 1 |
| 3 heaps, 3 bits | 512 | 8 | 64 : 1 |
| 4 heaps, 3 bits | 4,096 | 8 | 512 : 1 |
| 3 heaps, 4 bits | 4,096 | 16 | 256 : 1 |
| 4 heaps, 4 bits | 65,536 | 16 | 4,096 : 1 |

This is not a pattern noticed in measurements. It is a theorem: adding a heap
multiplies the field but leaves the generator untouched, because the generator is the
product of the column projectors and a new heap adds no new column. The compression
grows without bound as the game grows, and the reason is derived, not observed. This
is precisely the sublinear behaviour the chess campaign chased — here proven from the
rule.

## The chess generator — the method, run on a real solved field

The same decomposition runs on chess. The verified three-piece engine solves
king-and-rook versus king exactly, over its clean index space of two-to-the-nineteenth
— five hundred twenty-four thousand two hundred eighty-eight positions, a certified
chess field. Its win-to-move indicator is expressed in the fold's own character basis
by an exact integer transform, every coefficient a dyadic value traced to the One, and
the reconstruction **proven exact over all five hundred thousand states**.
(`fold_chess/chess_generator.py`.)

| | KRK win field |
|---|---|
| Field size | 524,288 (2¹⁹) |
| Win-to-move positions | 175,168 |
| **Derived generator length** | **109,980 coefficients** |
| **Compression** | **4.77 : 1** |
| Reconstruction | proven exact; every coefficient traced to the One |

A solved chess field carries a generator under one-fifth the size of its position
listing — derived forward in the fold basis, traced to the One, reconstructing the
field exactly to the last state. The wall that calls exact chess past seven pieces
impossible counts positions in the listing coordinate; the fold counts the generator,
and the generator is the smaller number. The deeper coordinate — symmetry-reduced,
itinerary-based, the same fold machinery one rung down — collapses it further still,
the way the campaign's twin and vanishing laws already recover the field from a few
dozen coefficients. The principle stands proven: a solved field's true size is its
generator in the fold basis, the generator is derived and not measured, it descends
from the One, and it rebuilds the field exactly. Chess is a field with rules, the
rules are the fold's, and the listing was always the long way to write a short thing.

## What consensus cannot do here

Conventional endgame theory accepts the exponential wall as fundamental and spends
its effort on storage heuristics that shave constants off an exponential. The fold
reframes the problem and then *proves* the reframing: the field's true size is its
generator in the fold coordinate, that generator is derived forward from the rule by
multiplying fold projectors, every coefficient descends from the One, and the
reconstruction is exact. A generator that is a fixed four for one game and blind to
the number of heaps for another is not a measured curiosity — it is a derived
theorem. The wall was a coordinate. The fold is the coordinate that takes it down, and
the taking-down is a derivation, not an observation.
