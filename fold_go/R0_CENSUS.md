# R0 -- THE CENSUS. Measured 2026-07-07, first compile, first run.

The rules substrate (constants/fold_go.ep, Tromp-Taylor position
legality as counted connectivity) certified by exact enumeration
before any play is built on it -- the chess campaign's perft
discipline on Go's soil.

## Engine counts vs the published Tromp oracle (halting law armed)

    1x1 = 1            oracle 1            EXACT
    2x2 = 57           oracle 57           EXACT
    3x3 = 12675        oracle 12675        EXACT
    4x4 = 24318165     oracle 24318165     EXACT

All 43,046,721 candidate colourings of 4x4 enumerated; full run 47s.
Any mismatch exits 1 (forced_to_be) -- the run passed through the gate.

## Independent referee (tools/go_census_referee.py)

A second implementation, different language, different construction
(sets/itertools vs odometer/flat lists), agreeing on every board
INCLUDING rectangles the oracle does not list:

    1x1=1  1x2=5  2x2=57  2x3=489  3x3=12675   engine == referee
    (referee additionally: 1x3=15)

ZERO disagreements anywhere. R0's pre-registered bar ("zero
disagreements or the engine does not proceed") is met; R1 (the solved
class: 2x2 and 3x3 complete, in-room certified) enters on the
author's go.
