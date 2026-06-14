# Grundy's Game campaign — the fold in its native territory

Impartial games ARE dyadic mathematics (nim-values = xor = carry-free
base-2; the fold = the shift on base-2 digits). Target: the famous open
problem — is Grundy's Game's value sequence eventually periodic?
(Berlekamp-Conway-Guy conjecture; 2^35 values computed, no period found.)
The field's only tool is compute-further; ours is structural analysis in
the game's own arithmetic.

## Instrument calibration (theorem-forced, passed exactly)

Nim's losing set is an F2-linear subspace, so its fold-spectrum must be
supported EXACTLY on the dual subspace with uniform magnitudes — predicted
before computation, verified exactly in three configurations (2x8-bit,
2x9-bit, 3x6-bit heaps). The author's original Nim spacings (5 = 2^2+1,
257 = 2^8+1) are the 1-D shadow of this law, now certified in full.

## Portrait of Grundy's Game (n < 16384, OEIS A002188, 20001 terms held)

Four instrument iterations, each prior reference design KILLED by its own
numbers (documented: unbalanced-DC confound; odd-multiplier reference
self-structured; prefix-packed reference self-structured). Final (v4):
off-DC energy, density-matched multi-shift Weil-flat sampler references.

Result: STRATIFIED DYADIC ANATOMY — top-16 off-DC exceedance over flat
floor rises monotonically with bit significance: x1.7 (bit0) -> x3 (bits
1-2) -> x8-10 (bits 3-5) -> x17.0 (bit6). Neither noise-shaped nor
period-shaped.

## Status after the decisive tests (run same day)

DRIFT TEST RESULT: the dramatic portrait was MOSTLY DRIFT. Against
drift-matched references (per-block density matching, 16 blocks) the
exceedances collapse from x8-17 to x1.1-1.9. The instrument killed its own
most striking picture within the hour — by design.

SURVIVING RESIDUAL (hypothesis-grade, NOT finding-grade): x1.1-1.9 over
drift-matched floors on every plane in BOTH disjoint 8192-windows (8/8
cells direction-consistent). Single-reference cells — within possible
reference variability. To promote or kill: reference-spread floors (many
shift constants), more windows, deeper data (Flammenkamp reaches 2^35).

Campaign verdict so far: instrument certified in native territory on
theorem-forced answers; first sortie at the open problem returned
"mostly drift, faint replicated residual." Normal prospecting. The
periodicity question remains untouched; the residual is the live thread.

## THE MOTIF (end of first night — finding-candidate, true size stated)

The high bits of Grundy's Game values couple preferentially to masks
containing n's FULL PARITY-TRIPLE (n mod 8) together with its 16s-place
bit. Evidence chain, every step pre-stated relative to its test:
- beyond smooth drift x1.4-1.9 on all high planes;
- exact core mask {n-bits 9,4,2,1,0} in top-16 of 3/4 internal windows
  (per-window chance 0.39%; joint ~6e-8); absent only in the earliest,
  pre-asymptotic window;
- OUT-OF-SAMPLE (n in [16384,18432), never touched): family signature in
  7/16 top masks vs 1.0 expected (p ~ 2e-5); exact core ABSENT in the one fresh window —
  CORRECTED same day: at that window scale the core is intermittent even
  in-sample (3/8 windows), so one fresh absence distinguishes nothing
  (p=0.625 under the in-sample rate). Exact-core persistence is UNTESTED
  out-of-sample, not failed. The family-level confirmation (7/16 vs 1.0
  expected, p~2e-5) is the standing fresh-data result.
Mechanism note (unproven, motivating): the unequal-split rule is parity-
sensitive (even n forbids the equal split), making arithmetic-of-n
structure mechanistically plausible rather than numerological.

Provenance note: an earlier per-block drift test BURIED this signal by
conceding all coarse structure to the null (over-conservative reference);
the author ordered the re-examination that recovered it. Lesson logged:
over-conservative references are a bias with the same rank as inflation.

## Promotion path to a notable result
1. Flammenkamp-scale data (2^35 terms) — out-of-sample at massive depth.
2. Formal significance treatment (family-rule look-elsewhere accounting).
3. Mechanism: derive the motif from the unequal-split rule inside the fold
   corpus — predicted structure would complete discovery into theorem.
4. Connection to the periodicity question itself: does the motif constrain
   or contradict eventual periodicity?
