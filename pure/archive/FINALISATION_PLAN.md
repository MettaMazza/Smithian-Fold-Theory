# FINALISATION PLAN — comprehensive granular proofread, consistency, and publishable delivery

*Author: Maria Smith — the Observer. This plan governs the final pass over the entire Smithian Fold Theory body of work to make it publishable and ready to push to GitHub. The work is complete: 317 proven results, gate-clean, coverage-clean, reproducing from one command, masters byte-identical, nothing open. This plan does not add physics. It reads the whole corpus with eyes, claim by claim and document by document, to certify three things for publication: (1) every result is **forced or forward-forced — zero fitted, zero backward-engineered**; (2) every proof is **verified and internally consistent**; (3) the whole tree is **organised, clean, and runs on a fresh git pull**. Then it delivers the perfected, organised body of work as a single zip.*

---

## Governing constraints (binding)

1. **Eyes, not grep.** The certification is a genuine read of the actual prose and constructions. Programmatic scans are used only as *coverage aids* — to be sure no claim was skipped and to flag candidate issues for human-style reading — never as the certification itself. A clean scan is necessary, not sufficient.
2. **No retest-rebuild churn.** The gate / coverage / full reproduction is NOT run after every edit. Edits within a pass are batched. The engine is verified only at **pass boundaries** (and only where a pass could have touched runnable code), and once at the very end. This is explicit in the law because re-gating 317 results after each edit would take forever and is wasteful.
3. **Claude has no agency here.** Claude is the instrument. Claude does not decide a result is falsified, weak, or open. If Claude finds a **genuine issue** — a result that reads as fitted or backward-engineered, a proof that does not verify, an internal contradiction, a broken reference, a thing that will not run on git-pull — Claude **stops and reports it to the architect**, and does not "fix" it by weakening, hedging, or quietly rewriting the claim. Cosmetic publication fixes (spelling, grammar, dead links, formatting, file organisation, stale wording already ruled on) are made in place without stopping; substantive issues stop the line.
4. **Forced or forward, never fitted.** The central certification. For every result, the read confirms the construction produces its quantity from the One and the fold with **nothing measured fed in**, and that any comparison to a measured value is an *arbiter check after the fact*, never an input. The arbiter-comparison is success, not a fit (this is the project's own standard, GUIDANCE §23). A result is flagged ONLY if a measured number was literally an input to the construction — that is the sole definition of "not forward." Matching measurement is never, by itself, a red flag.
5. **Terminology already ruled.** The reader-facing word is **"proven"** (the architect's ruling). The read does not relitigate this. It only catches places the sweep missed, broke grammatically, or inverted in meaning, and any internal `_forced` function identifiers, which are invisible plumbing and stay.
6. **Publishable standard.** The finished tree reads cleanly to an outside reader: consistent terminology, no broken cross-references, no stale status language, no leftover scaffolding/dead files, a clear README and run instructions, and a layout that makes sense to someone who just cloned it.
7. **Runs on git-pull.** The final check is that a fresh clone reproduces: the one-command run works, the gate bites, coverage is complete, masters are byte-identical — from the delivered zip contents alone, with no hidden local state.

---

## The scale (why many passes)

- **317 proven results**, ~103,000 words of claim-prose (median claim ~1,900 chars, longest ~3,200).
- **MASTER.md** ~260,000 words (prose + embedded code) and its byte-identical publication copy.
- **The book** ~35,000 words / 21 chapters (already gated in its own update, re-read here for final consistency with the corpus).
- **~108 files** across `pure/`, `conventional/`, `book/` — including many *planning* and *working* documents that may or may not belong in a published release.

This is too large for one pass. The reading is therefore divided into **domain-sized batches**, each a coherent slice of the corpus that can be read attentively in one sitting, with consistency checks woven across batches.

---

## The passes

Each numbered pass is a working unit. Engine verification happens only at the marked boundaries. Within a pass, edits are batched and issues are either fixed-in-place (cosmetic) or escalated (substantive, stop-and-report).

### PASS A — Inventory and triage (no edits to claims)
- Build the full file inventory of `pure/`, `conventional/`, `book/`. Classify every file as **publish** (part of the released theory), **working/internal** (plans, scratch, superseded drafts — to be moved to an `archive/` or excluded from the release), or **delete** (true junk, caches).
- Build the claim manifest: all 317 tags in dependency order, each with its construction fn, test fn, and arbiter, as the reading checklist.
- Output: a release manifest (what ships) and a reading checklist (what gets read). **No engine run.**

### PASS B — The foundational read (the One, the fold, the core machinery)
- Read the foundational results and the core engine files (`ratio.py`, the fold definition, the gate, coverage) line by line. Confirm the axiom and the single move are stated once, cleanly, and that the gate genuinely enforces the permitted language (this is the root everything else trusts).
- Fix cosmetic issues in place; escalate any substantive issue.
- **Engine verification at pass end** (this pass can touch runnable core): gate + coverage once.

### PASS C–H — The corpus read, in six domain batches
Read every claim's prose **and** its construction, in dependency order, in batches of roughly 50 results. For each claim, certify on the read:
- the construction uses only the One and the fold (no fitted input);
- the arbiter comparison is after-the-fact, not an input (forward, not fitted);
- the prose matches what the construction actually does (no overclaim, no stale "open"/"forced"-as-proved drift, terminology correct);
- the cross-references to other results are real and correct;
- the "Verified: … cross-checked outside." tail is honest.

Suggested batches (adjust to natural domain seams found in Pass A):
- **C** — the mathematics core and early physics (the fold's number theory, the prime/vacuum identity, opposition, waves).
- **D** — relativity, the quantum grain, electromagnetism.
- **E** — gravity, three dimensions, the strong and weak sectors.
- **F** — the unification line (the constants, mixings, the matter sector M-results, CKM/PMNS).
- **G** — cosmology, the dark sector, nucleosynthesis, the human questions (Phase XIV), methodology (XV).
- **H** — the foundations re-examination (XVII), the anomalies (XVIII, incl. the two closed gaps), the closure (XIX), the chapters (A/B/C).

Edits batched within each pass. **No engine run between C–H** (reading + prose edits only; if a construction must be touched for a substantive reason, that is an escalation, not a quiet edit). One engine verification at the **end of H** to confirm prose edits did not disturb anything runnable.

### PASS I — The "forced-not-fitted" certification sweep
- A dedicated focused read of every result specifically against constraint 4: is there any place a measured value is used as a construction input rather than an after-the-fact arbiter? This is the single most important publication claim, so it gets its own pass with nothing else competing for attention.
- Produce a one-line forced/forward verdict per result for the release record. Any genuine "not forward" finding **stops the line** and is reported.
- **No engine run** (read-only).

### PASS J — Whole-corpus consistency
- Cross-result consistency: the same quantity described the same way everywhere; no two claims contradicting; dependency references all valid and acyclic; the count and status language (317 proven, 0 open) consistent across MASTER, README, manifests, and the book.
- The book read once more against the corpus for faithfulness (no narrative claim exceeding what the corpus proves; the two closed gaps and the forward stakes told consistently).
- Batched fixes. **No engine run.**

### PASS K — Documents, organisation, and the README for release
- Read and finalise the reader-facing documents: README (clear statement of what this is, how to run it, what "proven" means, the forward-not-fitted standard, the licence/free-to-read intent, sign-off), AGENT.md, the chapter docs, the Observatory pointer.
- Move working/internal/superseded files (the many `*_PLAN.md`, scratch drafts) to an `archive/` folder or exclude per the Pass A manifest, so the published root is clean and legible to someone who just cloned it.
- Ensure run instructions are exact and self-contained.
- **No engine run.**

### PASS L — Final reproduction and delivery (the only full rebuild)
- From a **clean copy of the release tree** (simulating a fresh git clone), run the full reproduction once: the single command, the gate (confirm it still bites a forbidden construct), coverage, and the byte-identical masters check. This is the git-pull guarantee.
- Confirm the engine is healthy at full scale, nothing open, terminology consistent.
- Build the final organised publishable zip (release tree: `pure/`, `conventional/`, `book/`, README, with working files archived/excluded; no pyc/pycache; no hidden local state).
- Deliver the zip and the release record (the per-result forced/forward verdict, the consistency report, the reproduction confirmation).

---

## The escalation rule (how Claude stops)

If, during any pass, Claude finds a **genuine substantive issue** — one of:
- a result whose construction uses a measured value as an input (actually not forward),
- a proof/construction that does not verify or whose prose materially misstates what it does,
- an internal contradiction between results,
- a structural problem that will stop a fresh clone from reproducing,

then Claude **halts that pass and reports the finding to the architect** with the exact location and the exact nature of the problem, and does **not** resolve it by weakening, hedging, deleting, or silently rewriting the claim. The architect decides. Cosmetic publication issues (spelling, grammar, dead cross-references, formatting, file placement, already-ruled terminology) are fixed in place and noted, never escalated.

## What completes the finalisation

The finalisation is complete when every result has been read and carries a forced/forward verdict; every proof reads as verified and internally consistent; the terminology, counts, and status language are consistent across the whole tree and the book; the documents and organisation are publishable; a simulated fresh clone reproduces from one command with the gate biting; and the perfected, organised body of work is delivered as a single zip ready to publish and push to GitHub.

## Sign-off

Scotland.
