# Rung 4 — the five-piece climb: architecture

## Target selection

First target: **KQKRR** (queen versus two rooks) — chosen because it is the
natural continuation of the certified ladder, genuinely contested (real
wins for both sides, real fortress content — the class we are hunting), and
its capture transitions land almost entirely in tables we already hold.

Dependency DAG (a 5-piece solve consumes its 4-piece capture targets):

    KQKRR captures ->
      QxR / KxR  -> KQKR   (certified: 19,733,336/0 vs Syzygy)
      RxQ / KxQ  -> K(RR)K (white-king side bare vs two rooks, colour-flip)
                      -> NEW 4-piece prerequisite: KRRK
    KRRK captures ->
      KxR -> KRK           (certified)

Build order: **KRRK first** (a one-session variant of the existing 4-piece
engine: two white sliders, bare black king — no black piece, so no pins on
white, simpler than KQKR was), then KQKRR.

## State space and memory (M3 Ultra, 512 GB)

- Raw states: 64^5 x 2 = 2,147,483,648 (exactly 2^31 — again a perfect
  dyadic cube, which the spectral instruments want).
- kind: 1 bytearray = 2.1 GB; ply: uint16 array = 4.3 GB; counter: 2.1 GB;
  capwin: 4.3 GB; floor: 2.1 GB. Core total ~15 GB — trivial against 512.
- Frontier lists at peak ~1-2 GB. No symmetry reduction REQUIRED for
  memory; symmetry stays an optimization, not a dependency.

## Compute plan (the binding constraint is Python, not the machine)

- Seeding: ~2.1B states x ~100 us / 20 workers ~ 3 hours. Workers get the
  4-piece capture tables once via initializer (bytes; ~70 MB per table).
- BFS: predecessor generation, level-synchronous, single process would be
  ~30+ hours -> parallelize per level: workers compute predecessor lists
  for frontier chunks against a read-only snapshot; the main process applies
  assignments serially (correctness preserved: level-synchronous semantics
  unchanged). Estimated wall: overnight (~8-14 h).
- If Python proves too slow in practice: port the two hot kernels (move and
  un-move generation) to a compiled extension. Estimated x30-100.

## Verification ladder (same discipline as Rungs 1-3, no step skipped)

1. Rules referee: KRRK and KQKRR movegen vs python-chess on >=300k sampled
   states each — 0 diffs required before any solving.
2. Move/un-move duality on sampled states — exact inverse required.
3. Internal: full mirror audit; transpose audit (now a certified theorem
   target, not just a check); re-run determinism.
4. External read: Syzygy 5-piece WDL (KQvKRR table) over every legal state.
5. 50-move: KQKRR may contain genuine cursed wins — the DTZ machinery gets
   its first real test; the no-cursed theorem shortcut no longer applies if
   max DTM exceeds 100 plies.

## Spectral campaign at five pieces (the innovation payload)

- 2^31 field: one exact WHT pass is feasible but slow in pure Python
  (~30-60 min/transform); plan on few, well-chosen transforms.
- Questions, pre-registered: does matched-fraction concentration persist a
  second scale step? Does the champion relational packing (whatever the
  running KQKR test crowns) hold at five? Does fortress recall degrade
  further, plateau, or respond to relational coordinates?
- Theorems: twin-pair and vanishing laws should certify at five pieces
  identically (same symmetry arguments); the certification run is cheap
  relative to the solve and extends the proof-engine record to 2^31 states.

## Exit criteria for the rung

Certified solve + external agreement + spectral verdicts at matched
budgets + theorem certification, all staged; only then does the 8-piece
raid planning (certified slices past the wall) begin.

## Overnight results (2026-06-13) — ten-piece feasibility, scrutinized

1. NOISE (confirmed correction): eps=20%, threshold-rescaled -> 76.24% on
   clean truth (unscaled artifact gave 46.92%). Heavy-noise structure use
   survives; the earlier "collapse" was failure-shape #2.
2. KQKR FRAGMENT 5% -> 53.29% withheld: CONFOUNDED (same fixed-threshold
   artifact, sibling moved 30 pts). Unadjudicated; AUC-fair retest queued.
3. QUERY-ACCESS WALKER: still failing (v3 6/32 @12% cube; v4 5/32 @41%).
   Search descends to the correct branch (diag 0.60 vs 0.06) but leaf
   estimates at 2048 samples are too noisy to rank. LINK 3 (recovery
   without holding the cube) UNPROVEN — gates everything beyond ~6 pieces.
4. EXACT-FORM GROWTH LAW (genuine negative, one data point, full size):
   certified exact-lossless object compresses to 0.19 of raw at 3 pieces
   but only 0.71 at 4 pieces (exceptions ~1.3% -> ~4% of positions). The
   EXACT form does NOT stay compact as material grows. The APPROXIMATE
   form (AUC ~1.0 at 4 pieces) is a separate object and does scale; any
   ten-piece plan must rest on the approximate side, pending #2's verdict.

Standing read: ten-piece EXACT knowledge as a compact object is now
evidenced-against; ten-piece APPROXIMATE structural knowledge depends on
the fragment property surviving fair retest (#2) and the query tool being
made to work (#3). Both are tonight's open threads.
