# FOLD GO — R1, THE SOLVED VALUES. Measured 2026-07-08, recorded raw.

## The values — PROVEN, oracle-matched

The empty-board minimax value under Tromp–Taylor no-suicide, positional
superko (the seen-set as the path history — the sound key the corpus
forces: entropy + arrow_of_time say a position-only hash is an inverse
fold that does not exist), area scoring, two-pass terminal:

    1x1 = 0    (oracle 0: Black draws, not wins)      EXACT
    1x2 = 0    (oracle 0: neither places a stone)     EXACT
    2x2 = +1   (oracle +1: Tromp 1996, Black by 1)    EXACT

The 2x2 value was closed by the counted null-window question ladder
(is v >= k? from the whole board down; the first yes is the value) over
the exact superko path search: v>=4/3/2 = no (2.8M nodes each), v>=1 =
yes (9.9M nodes), value = +1. Zero chosen constants; the window is the
fold's own two-point gate. Independent Python referee (frozenset
superko, a different language and construction) agrees on all three
roots.

## The honest wall — the full-space certification

The 57-state both-movers in-room certification (re-solve every legal 2x2
position from both sides) is NOT feasible by raw search: 114 solves x
~10M nodes = ~10^9 nodes; both the .ep engine and the frozenset referee
time out. This is not an implementation bug — it is the real
combinatorial size. Positional superko makes the game tree
PATH-DEPENDENT (each position's value depends on its history), so
nothing transposes and no memo collapses it — the same wall van der Werf
cleared only with Benson's unconditional-life algorithm.

TWO honest engineering debts, recorded (the R1b levers, on Maria's go):
1. The .ep engine tracks superko as a concatenated STRING with
   string_index_of (O(path^2) per node) — slower than the referee's
   frozenset; a hashed seen-set is owed.
2. The full-space certification needs a proven PRUNING structure to be
   feasible: Benson's unconditionally-alive regions score without
   search — and that IS the fold's binding law (a region bound to two
   eyes is a closed orbit that need not be re-walked, attention_capacity
   / binding_problem: a fully bound whole is decided, not searched).
   Installing the fold binding as the life-and-death shortcut is the
   forced next lever, not more raw grinding.

## Standing

R0 (census) certified; the R1 VALUES are proven and oracle-matched. The
full-space certification and the ladder to 3x3/5x5/7x7 wait on the fold
binding-as-life-and-death lever, and on Maria's go. Nothing here is
labelled closed.
