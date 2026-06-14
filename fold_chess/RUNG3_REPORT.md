# Rung 3 Report — KQKR solved and certified

Queen versus rook: the first rung with bidirectional checks, pins, capture
transitions across material boundaries (into the certified 3-piece tables),
and genuine drawn fortresses.

## Pipeline (each gate passed before the next opened)

1. **Rules referee (phase 3a):** 272,652 sampled states vs python-chess —
   0 legality disagreements; 176,420 mutually legal states compared
   move-for-move — 0 move-set disagreements.
2. **Move/un-move duality:** predecessors and successors proven exact
   inverses on 2,311 sampled states — 0 exceptions.
3. **Solve (phase 3b):** 19,733,336 legal states; parallel seeding + level-
   synchronous predecessor BFS; capture values resolved in the certified
   3-piece tables. 614 s on 8 workers.
4. **Internal referees:** full-space mirror audit — 0 violations; solve
   reproduced identically on re-run.
5. **External read (phase 3c):** Syzygy WDL diff over every position —
   **19,733,336 / 19,733,336 agreements, 0 disagreements, 0 rules diffs.**

## Results

- W 11,953,856 / L 7,079,816 / D 699,664 (of which 411,768 drawn cycles —
  the fortress class), 13,420 checkmates.
- Longest win: 69 plies (mate in 35).
- 50-move rule: max win 69 <= 100 plies, so cursed wins are impossible at
  this rung by theorem; the external read independently confirms (any
  Syzygy cursed value would have surfaced as a WDL diff).

## Cumulative external record (consensus track)

KQK 368,452 + KRK 399,112 + KQKR 19,733,336 =
**20,500,900 positions checked, 20,500,900 agreements, 0 errors.**

## Addendum — KRRK certified (prerequisite for the five-piece climb)

KRRK: 21,985,768 legal states solved in 451s. Internal referees: rook-swap
invariance exhaustive over all states — 0 violations; mirror audit — 0.
External read: 21,890,344 comparable positions vs Syzygy — 21,890,344
agreements, 0 disagreements (95,424 statically-valid-but-unreachable
double-check states excluded from probing, a convention disclosed in
rules_checkRR.py; their movegen was still verified move-for-move).

Provenance note: the first certification log contained an unexplained
second result block in a foreign format (same verdict). Per the
direction-blind provenance rule, the read was re-run to a fresh exclusive
log and reproduced the authored result digit-for-digit. Both blocks
preserved in the session record; conclusion earned by reproduction.

## Cumulative external record (final, four endings)

KQK 368,452 + KRK 399,112 + KQKR 19,733,336 + KRRK 21,890,344 =
**42,391,244 positions checked, 42,391,244 agreements, 0 errors.**
