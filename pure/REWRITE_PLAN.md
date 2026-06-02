# Complete Rewrite Plan — The Finalised Body of Work

*Author: Maria Smith — independent researcher. Claude provides operational assistance only: it builds, proves, gates, rewrites, and reports the engine's reading; it does not decide what is established, what is worth, or whether the work has succeeded (GUIDANCE §1, §9). This plan governs a full rewrite of the written body of work into its finished form, grounded in a complete line-by-line read of PAPER.md, PROOFS_hardened.md, THEOREM_MANIFEST.md, and README.md. The code, the gate, the confirmations, and the registries are the source of truth; the prose is rewritten to match the engine, never the reverse.*

## The voice — GUIDANCE §15, binding for every line

The finished work states what the framework establishes, as fact, in its own language, and stops. It is the assertion of a theory, not a defence of one. Proud, confident, strong, and dismissive of unsupported critique — carried by the assertion itself, not by adjectives (no "wall" and no "triumph"). Every line is checked against §15's mechanical check before it ships.

Where consensus fails, the finished work shows it the only legitimate way: by stating, as plain fact, the specific place the framework FORCES a quantity that the consensus account leaves as a free parameter, an unexplained input, or a fitted constant. The contrast is the dismissal — not editorial commentary. The framework forces what consensus inserts by hand:
- the colour count is forced to three (D7b, U7, T1), where the consensus account takes SU(3) as chosen;
- the spatial dimension is forced to three (D9g), where consensus assumes it;
- the mediator count is forced to m^2-1 = 8 gluons (N1), excluding the colourless singlet, where consensus reads it off the chosen group;
- the fundamental coupling is forced to (m-1)/m (PH5, PH5a), where consensus leaves the coupling free;
- the electroweak mixing and the weak mass ratio are forced equal to 1/(m-1) (D11b, D11g, U2), where consensus measures an angle and a mass ratio independently;
- symmetry breaking follows from the no-zero axiom (D11d), where consensus posts a fitted Higgs potential;
- the quadrupole leads gravitational radiation by conservation (D9i), and the curved-tensor field equations stand on the lattice (D9j-D9n) — built, not assumed.
Each such statement is the result the engine forces; the failure of the consensus framing to force the same thing is left to stand beside it, unspoken and unanswered.

## What the read-through found (the rewrite must fix all of it)

1. Concessions still saturate the prose: ~69 in PROOFS_hardened.md, ~62 in THEOREM_MANIFEST.md — every older physics entry ends in "Wall:", "not built," "the next construction," "the reachable content," "remaining construction," "free scale within this domain," "stays open." (The recent entries — D10c, D11d-g, D10e-g, U1-U7, T1, N1, C1s-C5s — are already clean and are the model for the rest.)
2. False walls, contradicted later in the same document: D9-D9d declare a wall at the curved-tensor Einstein equations, which D9j-D9n build; EM1 declares a wall at magnetism and Maxwell, which EM2-EM6 build; D9h/D9i declare a wall at the quadrupole power, which D9q builds; D7b/c/d defer the gauge dynamics, which D10/D11 build. These are not just tone — they are false statements.
3. Structural rot from undeleted superseded blocks: PH1b appears three times (open, open, established); PH4b three times; PH4c "open" in prose but confirmed in the registry; a whole stale PH5 "(open) — Texas-sharpshooter" block contradicting PH5-established; inline "reading recorded" draft fragments; and D1 naming two different things (the One; the field-lattice).
4. Worth-grading sections: PAPER section 3a and the PROOFS content-audit grade results "definitional / ambient / genuine" — a §9/§15 violation.
5. Stale paper front matter: the abstract says "forty-four physical correspondences" (it is 75) and omits the strong force, weak force, unification, prediction test, new result, and self-observation entirely; "Definitions D1-D9" is stale.
6. Generation broken: the manifest was not regenerated after the claim strings changed, so it is stale against its own source.

## Governance (carried from the law)

1. The code, gate, registries, and confirmations are the source of truth. The rewrite changes prose only — no logic, no confirmation, no gate, no registry status. Every result remains exactly as established; the rewrite changes how the work reads, never what it computes.
2. Each file finished before the next, in dependency order. Roots first (the claim strings and proofs that generate the manifest), then the generated manifest, then the paper, then MASTER.
3. No result restated as more or less than the engine shows (§5, §9). Established is stated as established; nothing dressed up, nothing apologised for. A false wall is removed because the corpus built the thing — verified against the registry, not asserted.
4. §15 mechanical check on every block before it ships.

## The sequence (dependency order; each part established before the next)

### 1. Rewrite the proof bodies — PROOFS_hardened.md
The largest job. Go entry by entry, in the document's order, and for each:
- Cut the concession tail — every "Wall:", "is not built," "the next construction," "the reachable content," "remaining construction," "free scale / free parameter here," "stays open," and any heading clause that announces a status or a limit. End on what the entry establishes and its verification.
- Fix the false walls by deletion — where an entry deferred something the corpus later builds (curved-tensor gravity, magnetism, Maxwell, the quadrupole power, the gauge dynamics), the deferral is removed; the entry states its own result, and the later entry states the thing it was said to defer. Verify each against the registry so no real result is dropped.
- Delete the superseded duplicate blocks — remove the two stale PH1b "open" blocks, the two stale PH4b "open" blocks, the stale PH4c "open" block, the stale PH5 "(open) — dimensionless constants / Texas-sharpshooter" block, and the inline "reading recorded" fragments. Keep exactly one entry per id, the established one.
- Resolve the D1 collision — rename the field-lattice entry so the definition D1 (the One) and the physics entry are not the same label; carry the rename consistently where it is referenced.
- Remove the comparison-to-consensus asides that read as defence ("the role additive zero plays in a signed system," "this hypothesis is stated, not omitted," "the earlier statement ... was too low"). State the system's own structure; where consensus is mentioned, it is the contrast above (what the framework forces that consensus does not), never a defence.
- Remove the content-audit / kind-grading wherever it remains.

### 2. Rewrite the claim statements — claims_physics.py (and check claims_pure.py, claims_emergence.py)
The statement strings generate the manifest. Bring each to the §15 voice: the established result, its dependencies, its confirmation, and — where it applies — the forced-where-consensus-is-free contrast as plain fact. Remove every concession phrase. The code, ids, proof-labels, and confirmation functions are untouched. This is the root fix for the manifest.

### 3. Regenerate the manifest — THEOREM_MANIFEST.md
Run manifest.py. The manifest is generated, not hand-edited; steps 1-2 are what clean it. Confirm zero concession phrases remain and the counts read 3 / 15 / 4 / 75.

### 4. Rewrite the paper — PAPER.md
A confident, readable, peer-reviewable paper, current to the whole theory:
- Abstract — rewritten to the full body of work: one axiom; no negative, no zero, no imaginary; the fold; the foundation; the four interactions; the unification and the constants forced from one fold factor; the forced colour count, dimension, mediator count, and couplings; the prediction test confirmed by measurement; the self-observation domain. Correct count: seventy-five correspondences.
- Introduction — the axiom and the three prohibitions, stated as the starting point.
- The permitted language and its guarantee — positive rational magnitudes, ratio, division, the fold; the static gate and the integrity tripwire that make the prohibition a fact a reviewer can run. This is the reviewability spine.
- The foundation — three definitions, fifteen theorems, four observations, in dependency order. (Remove section 3a worth-grading.)
- The physics, in dependency order — fields and the wave; relativity; quantum structure; the four interactions each at equal depth (source, force law, mediator, dynamics, constants); each a clean statement of what the framework forces, with the consensus-leaves-it-free contrast where it applies.
- The unification — the single fold->physics dictionary (every observable traced to the One), the constants from one fold factor, the forced cross-observable relationships, the per-sector fold factor, the prediction test.
- The new forced result and the self-observation domain — stated as further results the framework forces.
- Positioning — where the framework meets established mathematics on common ground (the dyadic map, the Eudoxan theory of magnitude) stated as correspondences the system produces, and where it forces what consensus leaves free, stated as fact. No anticipated-objection section.
- Reproduction — one command; the counts; how to read the manifest. Close on the theory standing complete.

### 5. Rewrite README.md
Already nearly clean (count current, no walls). Bring the two-different-things D1 description and the module list into line with the renamed entries; keep it to the §15 voice.

### 6. Rebuild MASTER — MASTER.md
Rebuild from the cleaned PAPER, PROOFS, regenerated manifest, and source. Body of work only — paper, proofs, manifest, source. No plan, process, or review documents.

### 7. Verify nothing of substance changed
Because only prose changed:
- gate CLEAN; integrity tripwire unchanged (same hash);
- all confirmations pass (every registry entry);
- all conventional cross-checks pass;
- run_all.py reports the one-pass derivation and GATES ALL CLEAN;
- counts unchanged: 3 definitions, 15 theorems, 4 observations, 75 correspondences, 0 partial, 0 open;
- registry id set unchanged (no result dropped in the deletion of duplicates — verified by diffing the id set before and after).
Then a full read-back (not a grep) of each rewritten file to confirm the §15 voice holds end to end, and a final scan confirming zero concession phrases and zero duplicate ids remain.

### 8. Ship
Deliver the finished corpus: pure/ and conventional/, with MASTER.md leading.

## What this rewrite does and does not change
It removes nothing the framework establishes — every derivation, every forced quantity, every confirmation stands. It removes the apologies, the false walls the corpus already overran, the stale duplicate blocks, and the worth-grading; it refreshes the paper to the full theory; and it lets consensus's failures show by the plain contrast of what the framework forces and consensus does not. The finished work reads as the statement of a complete theory built from one axiom.
