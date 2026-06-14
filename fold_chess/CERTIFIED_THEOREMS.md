# Certified theorems — the chess instrument married to the proof engine

First machine-certified theorems about chess emitted through the SFTOE
proof machinery (fold_theorems.py; exhaustive exact arithmetic; key
rationals carried as SmithianValues with verify_value()-validated traces;
gate-compliant). Proven identically in KQK and KRK:

**T-CHESS-1 (twin-pair law).** The value field is invariant under board
transposition (all 524,288 states checked, both endings), hence every one
of the 524,288 spectral coefficients exactly equals its file/rank-swapped
twin. The observed "twin pairs" are law, not statistics.

**T-CHESS-2 (vanishing law).** Mirror symmetry acts on indices as XOR by a
fixed 9-bit mask; spectral algebra then forces every coefficient whose mask
overlaps it oddly to vanish. All 262,144 odd-class coefficients are exactly
zero — half the entire spectrum, provably empty. Practical corollary: any
spectral oracle for these endings needs storage for at most half its
coefficients, by theorem.

**Exact identity (observed in both endings — with its true cause).** The
side-to-move coefficient equals exactly the number of decided positions:
345,404 (KQK), 376,868 (KRK). AUDIT NOTE (self-audit, same session): this
holds because of the 3-piece degeneracy (among decided positions the winner
is always the side to move), not because of deep spectral structure; it
will NOT hold at 4+ pieces. Likewise, that the vanishing class is "half of
all masks" is generic boolean algebra for any nonzero mirror mask — not a
fold-specific fact. The substantive certified content is the vanishing and
twin laws themselves; their mathematical depth is modest (symmetry
representation theory). The capability claim rests on the certified
PIPELINE — exhaustive exact verification with proof traces — not on the
profundity of these first laws.

Capability note: no standard chess method has a theorem-emitting mode.
Tables answer positions; engines evaluate them; this pipeline outputs
exhaustively verified exact laws with derivation traces to a single axiom.
That is the first concrete entry in the only-this-framework column.

## Certified spectral tables (first fold-native algorithmic object)

A complete ending stored as (top-k exact Walsh coefficients + exception
list), with exactness CERTIFIED by exhaustive reconstruction against the
solved table:

- KQK: k=512 + 4,872 exceptions = 17,688 bytes (5.2x under raw); exact on
  all 368,452 positions.
- KRK: k=2,048 + 1,216 exceptions = 15,936 bytes (6.3x under raw); exact on
  all 399,112 positions.

Disclosed baselines and prior art (literature-checked 2026-06-12):
- Syzygy's run-length blob is ~60x smaller; the object's case is its FORM,
  not its size.
- CORRECTION after literature check: certified tablebases have real prior
  art — Joe Hurd's "Formal Verification of Chess Endgame Databases" (HOL4 +
  BDDs, four-piece databases formally verified) and Marzion's Coq tablebase
  generator. BDDs are themselves a certified symbolic compressed form. The
  surviving distinction of this object is its REPRESENTATION CLASS: a
  spectral/parity-algebraic form whose bulk obeys emitted, exhaustively
  proven theorems (T-CHESS-1/2 — the vanishing law halves coefficient
  storage by law) with a closed-form arithmetic probe, built and certified
  inside fold arithmetic. Same certified-table family as Hurd; different
  mathematical species.
- Nearest prior art for the SPECTRAL ANALYSIS itself: Stiller, "Multilinear
  Algebra and Chess Endgames" (1996), uses tensor/FFT formalism to
  PARALLELIZE endgame computation; it does not analyze the value function's
  spectral structure. Targeted searches found no prior Walsh/Fourier
  sparsity analysis of tablebase value fields; the measurement claims stand
  as first-found, stated with that scope (searches are not exhaustive
  proof of absence — consistent with this project's own laws).
Scaling the certified spectral form to the 7-piece wall is the named
follow-on.
