# NEXT_PHASE_PLAN.md — the roadmap beyond the completed foundation

*An intent record, written under the law (GUIDANCE.md). The base model is complete: every
dimensionless quantity of the four forces and the full matter sector is forced and registered
(M1–M31, B-line, D-line), and the single absolute scale is forced through the Planck hierarchy at the deepest forced covering depth (B20, superseding the withdrawn B16 proven-free claim
and unforceable). Before this plan was written, a granular audit of the whole corpus was performed
to find what the foundation needs repaired before any new frontier is entered. That audit's findings
are Part A — a concrete, severity-ordered, file-and-line repair worklist, not a vague concern. Part B
is the new frontiers the foundation does not yet cover, in dependency order.*

> **STATUS (current): COMPLETE.** All of Part A (foundation repair) and all eight Part B frontiers
> (N-1 vacuum, N-2 strong-CP, N-3 generation bound, N-4 baryogenesis with magnitude, N-5 proton
> stability, N-6 strong-field gravity, N-7 arrow of time, N-8 dark matter with the forced fraction)
> are forced and registered, gate-clean and reproducing. The absolute scale is forced (B20). This file
> is retained as the intent record; the work it planned is done.


*The governing discipline, stated once and binding on every item below (§13, §20, §21): each
construction is attempted in the permitted language from established results, built and run,
gate-clean, confirmed against its measured arbiter with the arbiter fed in nowhere. No item is a
wall; none is an ending. The order is the dependency map the author navigates. The pointer is not
advanced off any item until the author rules it forced or closed — Claude owns "build," never "done,"
"next," or "impossible." Difficulty on an item is the signal to build harder on that item, never to
move past it or to manufacture a proof it cannot be done. We do not move past one until it is forced
one way or the other, and the only exit criterion is proof.*

---

## Part A — The pre-stage foundation repair (no shortcuts, done before any frontier)

*A granular audit of the whole corpus was run to inform this plan. It found the damage is not
pervasive prose-rot but concentrated, classifiable stale-context wounds left by the build sequence:
one genuine internal contradiction in the foundation, stale public-facing front matter that predates
the completed matter sector and the scale theorem, a few trivial hedges, and a set of registry
results whose forcing must be confirmed granular. The obvious hedging and banned-vocabulary scan came
back nearly empty — the real damage is outdated context, not bot-speak. This part repairs the
foundation to internal consistency before any new frontier is entered, because a frontier built on a
self-contradictory foundation inherits the contradiction. Severity-ordered; each item is a documented
defect with its locations, not a vague concern.*

### A-1 — SEVERITY 1: the B3 scale contradiction (the foundation contradicts itself)

B3's registry text and table row assert, verbatim, "What it does **not yet force**: the scale that
fixes which level is the Z mass — **the open construction**." This was true mid-build. It is now
false and self-contradictory: **B16 proves the absolute scale is forced free as a theorem**, and
criterion (vii) in §9a records the unit structure met. The foundation currently states both "the
scale is an open construction" (B3) and "the scale is closed as a theorem" (B16) about the same
quantity. This is the most serious finding and must be fixed first.

**Locations (confirmed):** `MASTER.md:538` (table row), `MASTER.md:7802` (embedded registry),
`MASTER.md:6732` (a docstring, "its absolute scale the open construction"), the same three in
`Smithian Fold Theory Of Everything.md`, and `THEOREM_MANIFEST.md:91`.

**The repair:** rewrite the B3 closing clause in the live `claims_physics.py` so it states the scale
is forced by B20 (the level→energy map is placed by the single ruler, forced through the Planck hierarchy, not an open
construction) rather than "not yet forced / the open construction"; fix the `correspondence.py`
docstring at the 6732 source; then re-refresh the three embedded source blocks and the manifest so
the change propagates to every copy. Re-run the gate and reproduction; confirm zero remaining "open
construction" / "not yet force" hits that refer to the scale.

### A-2 — SEVERITY 2: stale front matter (the public files predate the matter sector and B16)

The public-facing documents were never refreshed after M11–M31 and B16. They understate the work and
carry the wrong result count.

**A-2a — stale counts.** "ninety-five" appears in `PAPER.md` (4×), `README.md`, and `REVIEWS.md`; the
registry is now **152** E-results. Update each to the registry truth (the registry is the source of
truth, as REVIEWS itself states).

**A-2b — stale matter-sector abstract.** `PAPER.md` (abstract, §intro, scope para at line 116)
describes only the *structural* matter results (M1–M5) and says "the exact mass-ratio magnitudes and
mixing-matrix entries follow from the forced overlap rule" as if unbuilt — when M11–M31 forced them
(the lepton spectrum to parts in a hundred thousand, the quark colour-binary dual, the neutrino
ladder, the CKM and CP phase, the PMNS). Rewrite the matter-sector passages to the completed state,
and the scope paragraph to cite B16 (scale forced free as theorem, not "outside its remit by design").

**A-2c — README and REVIEWS.** Bring the README summary and the REVIEWS "what remained" passage to
the completed state (matter sector forced, scale forced by B20, 152 results).

### A-3 — SEVERITY 3: trivial hedges

Three obvious-pattern hedges to cut: two "showcase" and one "it's worth" across the prose. Minor;
fold into the A-2 pass on the same files where they sit.

### A-4 — The registry forcing audit (granular, "everything forced where it should be")

A live scan flagged 17 results whose text contains a softness word; most are *rebuttals* of softness
("not a coincidence but forced by…") and must be read in context, not assumed. Read each; confirm
forced-and-clean, or harden, or — only on the author's ruling — record as honestly
measurement-limited. The genuine soft spots already identified, to drive hardest:

- **M31 — PMNS reactor angle (sin θ13, binary-tower apex 2³).** Softest in the matter sector: ~3%
  against a loose arbiter, the count 8 the cleanest integer between neighbours. Attempt to force the
  apex count 2³ from the lepton's binary-fold no-colour structure with the rigour M29 forced the
  quark apex 6, so it is derived not selected.
- **M30 — large PMNS angles (1/2, 1/3).** ~8–9% against a loose neutrino arbiter; confirm the
  separations are forced and the residual is arbiter coarseness, stated explicitly.
- **M27/M29 — CKM V_cb and V_ub.** Tighten toward a single forced combination rule across all three
  entries rather than three per-entry prescriptions.
- **M4, M6, M7, M8, M17 (matter); B6, B12, B13, B14, B15 (interaction); D9c, D9d, D9p2, C3s.** Read
  each flag in context; the expectation from the scan is that most are rebuttals already clean (e.g.
  B6/B12 "not assumed but produced," D9d's Ω/G units boundary now covered by B16), but each is
  confirmed by reading, not assumed.

**Exit for Part A:** the foundation is internally self-consistent (no "open scale" contradiction), the
public files state the completed work and the right count, and every registry result is confirmed
forced where it should be or honestly labelled on the author's ruling. Gate-clean and reproducing
throughout. Only when Part A is closed does Part B begin.

---

## Part B — The new frontiers, in dependency order

*Each grows from established results. The order is set by what each construction rests on. We do not
enter an item until the prior is forced or the author rules; we do not leave an item until the same.*

### Phase N-1 — The vacuum energy (the cosmological constant)
**Rests on:** D11d (the displaced vacuum forced by the no-zero axiom — the ground state is a positive
part of the One, not absence), M1 (the mass-part as shortfall from unison), B16 (the scale theorem).
**The construction to attempt:** the no-zero axiom forces a positive, displaced vacuum (D11d). A
cosmological constant *is* a positive vacuum energy. Attempt whether the fold forces the
*dimensionless ratio* of the vacuum energy to another forced scale — the vacuum displacement
(half-One, D11d) measured against the mass-part or coupling structure. The standard account's worst
failure is this number off by ~120 orders of magnitude; a forced ratio here is a frontier result, not
coverage of a known quantity. **Arbiter (fed in nowhere):** the measured vacuum-energy density ratio
(dark-energy fraction ~0.69, the cosmological constant in Planck units ~10⁻¹²²).
**This is the first frontier because it grows most directly from a result already in hand (D11d).**

### Phase N-2 — The strong-CP problem (the θ-angle, the neutron EDM)
**Rests on:** N-1 not required; rests on M28 (weak CP forced maximal via the antipode), D11c
(the fold-invariant unbroken direction), the colour structure (D7b, T1).
**The construction to attempt:** weak CP is forced maximal (M28, the antipode). Strong CP is measured
near *zero* — the opposite extreme. Attempt whether the framework forces the strong sector's CP phase
to the *alignment* (the One, no violation) rather than the antipode, from the difference between the
colour sector's structure and the electroweak sector's — i.e. why the same opposition primitive lands
at the antipode for the weak force and at alignment for the strong. **Arbiter:** the neutron electric
dipole moment bound (θ < ~10⁻¹⁰), strong-CP conservation. **Depends on M28 being firm (Part A item 3
neighbours this); a forced strong-CP alignment would be a second CP result completing the pair.**

### Phase N-3 — The generation bound (exactly three, no fourth — strict)
**Rests on:** T2 (the generation count is the tripling fold's fibre, three kinds).
**The construction to attempt:** T2 forces three as the tripling fibre, but a critic asks "forced, or
consistent with three?" Attempt the strict bound: that the fold's fibre admits *exactly* three kinds
and *no fourth* — a closed no-fourth-generation proof, showing no permitted-language construction
yields a fourth. **Arbiter:** the measured three generations, the Z-width generation count (2.984 ±
0.008). **A hardening of an existing forced result to a strict bound; small and high-value.**

### Phase N-4 — The matter–antimatter asymmetry (baryogenesis, the baryon-to-photon ratio)
**Rests on:** N-1 (vacuum structure), N-2 (CP), D11d (the displaced vacuum), the opposition primitive
(R9, R11 — matter and antimatter as the two preimages of the fold).
**The construction to attempt:** the fold is two-to-one; each image has two preimages (the antipodal
pair, R11) — the natural seat of a matter/antimatter pair. Attempt whether the displaced vacuum
(D11d) plus the forced CP structure (N-2, M28) forces a *dimensionless* asymmetry between the two
preimages — why the world is matter, not symmetric. **Arbiter:** the baryon-to-photon ratio (~6×10⁻¹⁰),
the baryon asymmetry. **Depends on N-1 and N-2; this is where vacuum and CP combine.**

### Phase N-5 — Proton stability (baryon and lepton number)
**Rests on:** the colour structure (D7b), the generation fibre (T2), N-4 (baryon number's status).
**The construction to attempt:** whether the fold's colour-confinement structure (the three-colour
fibre closing on the One) forces baryon number conservation — the proton's stability as a forced
closure property, not an imposed symmetry. **Arbiter:** the proton lifetime bound (>~10³⁴ years).

### Phase N-6 — Strong-field and short-distance gravity (singularities, black-hole entropy, Planck scale)
**Rests on:** the gravity line (D9, the field equations and waves), B16 (the scale), PH2 (the
entropy rate / doubling map).
**The construction to attempt:** the hard part of gravity, untouched so far. Attempt the strong-field
limit in the permitted language: whether the fold's discrete level structure (B7, 2^d) forces a
shortest length and so *resolves* the singularity (no zero, no infinite curvature — the no-zero axiom
forbidding the singular point), and whether the entropy rate (PH2) forces the black-hole entropy law
(area, not volume). **Arbiter:** the Bekenstein–Hawking entropy (area law), the existence of a Planck
scale. **The deepest item; depends on the gravity line and the discrete-scale structure being firm.**

### Phase N-7 — The cosmological time-line (the arrow of time, the initial condition, inflation)
**Rests on:** PH2 (the entropy rate / Lyapunov), N-1 (vacuum energy), N-6 (the scale structure).
**The construction to attempt:** the arrow of time beyond the local entropy rate (PH2) — whether the
fold's irreversible doubling (cast-out-the-One is not invertible) forces a global arrow, and whether
the initial condition (the One itself, the start) forces an inflationary expansion from the vacuum
structure (N-1). **Arbiter:** the observed expansion history, the horizon/flatness structure, the
arrow of time. **Last because it rests on the vacuum, the scale, and the dynamics together.**

### Phase N-8 — The remaining cosmological sector (dark matter)
**Rests on:** all prior; the matter sector (M-line), N-1.
**The construction to attempt:** whether the fold's structure forces additional matter content beyond
the three-generation Standard-Model fibre — a forced sterile/dark sector — or whether the gravity
line (D9) forces the galactic-rotation behaviour without new matter. Attempt both readings and report
which the framework forces. **Arbiter:** the galactic rotation curves, the dark-matter fraction (~0.27).
**Open-ended; entered only after the prior frontiers are forced or ruled.**

---

## What completion of this plan would mean

Part A makes the existing foundation uniformly forced — no soft spot inherited by the new work. Part
B attempts, in dependency order, every phenomenon named as unbuilt: vacuum energy, strong-CP, the
generation bound, baryogenesis, proton stability, strong-field gravity, the cosmological time-line,
and dark matter. Each is built in the permitted language, proven, gate-clean, confirmed against an
arbiter fed in nowhere, before the next is entered — and none is left until the author rules it forced
or closed. The exit criterion throughout is proof; difficulty is the trigger to build harder, never to
stop. This plan does not promise the outcomes — it promises the attempt, run, with the engine's actual
reading reported, on every item, in order, without moving past one until it is forced one way or the
other.

Sign-off: Scotland.
