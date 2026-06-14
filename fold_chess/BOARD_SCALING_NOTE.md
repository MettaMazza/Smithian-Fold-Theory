# Board-completion ambition

The goal of this campaign is to solve as much of the chessboard as possible —
not a fixed target, but as far as the method will carry: possibly ten pieces
or more. We do not yet know how far that is. The honest position is that we
cannot know until we try, and we are trying.

## Why ten-plus is even on the table

The new algorithmic developments are what make the ambition real rather than
fantasy:

- **Certified retrograde pipeline.** Each ending is solved exactly in the
  fold's own arithmetic and certified against external Syzygy ground truth,
  with internal symmetry referees (mirror, rook-swap) over the whole space.
- **Sparse fold-spectrum structure.** The value field is overwhelmingly
  sparse in the fold's Walsh basis, and the sparse approximate form
  **generalizes from a fragment** — a few thousand coefficients trained on a
  5% sample rank win-vs-loss on the withheld 95% at AUC ~0.998 at four
  pieces, and that does not degrade across the material step (3 -> 4). The
  exact-lossless form does NOT stay compact as material grows; the approximate
  side does, and the approximate side is what a ten-piece plan rests on.
- **Query-access recovery.** Recovering the dominant structure by querying,
  rather than holding the whole index space, is proven by AUC; the remaining
  open piece is making it sublinear in queries (it currently recovers
  perfectly but still touches most of the cube). That efficiency is the gate
  beyond roughly six pieces.

## Progress

- **Done — 4 pieces, fully certified:** KQK, KRK, KQKR, KRRK —
  **42,391,244 positions checked vs Syzygy, 42,391,244 agreements, 0 errors.**
- **In progress — 5 pieces:** KQKRR (white K+Q vs black K+two rooks),
  2^31 = 2,147,483,648 raw states. Movegen referee and move/un-move duality
  both passed (0 diffs); the full retrograde solve is running, to be
  certified against the KRRvKQ Syzygy table over every legal position.

Five is the next rung. Ten-plus is the direction. We find out by climbing.
