# PROOFS (permitted language) — every theorem from the One, ratio and division only

Primitive: the One is unity; a position is a part of the One, an exact ratio in (0, 1]; the fold doubles a part and casts out the One; the relation between two ones is their ratio. No negative, no zero, no imaginary, no sine — only ratio, proportion, doubling, and casting-out. Each theorem carries the id its claim holds in claims_pure.py.

**R1 (Q4) — the One unfolds to 2^k positions.** Each fold either casts out the One or does not: two outcomes per fold. After k folds the distinct outcome-strings number 2·2·…·2 = 2^k, and each fixes a distinct part of the One to k folds. ∎

**R2 (Q5) — one part revealed per fold; exact reassembly.** Doubling a part moves its leading sub-part across the half-One exactly when that bit is present; casting out the One removes it and shifts the rest up. The bit read at fold i is the i-th part of the One in the position; summing the present parts one-in-2^i reassembles the original exactly (shown: 11/16 → bits 1,0,1,1 → 1/2+1/8+1/16 = 11/16). ∎

**R3 (Q6) — count and measure are one quantity.** A position fixed to k folds is one of 2^k equal faces; each face is the part one-in-2^k of the One. So count = 2^k, measure = one-in-2^k, and count·measure = 2^k·(1/2^k) = the One. The two are the same fold-depth k read two ways. ∎

**R4 (Q7) — the monad is fold-fixed.** Take the whole in M equal parts. Doubling sends the M parts onto M/2 positions, each reached by exactly two of the original parts; the images are equally spaced (gap two-in-M = one-in-(M/2)). So an even division folds to an even division — the evenly-divided whole is returned to itself. ∎

**R5 (Q8) — self-perception repels.** Two ones a fold apart: each doubles, so the part between them doubles. Near unison (separation a small part) the separation multiplies by the fold factor m ≥ 2 each fold, growing away from unison. Exact self-coincidence is therefore a repelling state; any part between two ones grows under folding. ∎ (Shown: separation 1/1000 → 1/500, ratio 2.)

**R6 (Q9) — relative views telescope and commute.** A one seen from another's frame is the proportion observed:observer. Composing two views multiplies the proportions: (c:b)·(b:a) = c:a. Composition is multiplication of ratios, which is associative and commutative; relative position telescopes. (The non-commuting found earlier was a property of the complex-affine representation, not of the system in ratio terms.) ∎

**R7 (Q10) — the holding threshold is (m−1)/m; there is no π.** Two coupled ones: each fold multiplies their separation by the fold factor m (R5), and the pull keeps the fraction (one minus g) of it, giving separation factor m·(one minus g) per fold. The separation does not grow exactly when m·(one minus g) ≤ the One, i.e. when g ≥ (m−1)/m. So holding begins at the ratio (m−1)/m — the half-One for the doubling fold, two-in-three for the tripling fold, and so on. No π enters: π appeared earlier only through the sine-and-radian apparatus, which the permitted language does not use. ∎

**R8 (Q11) — domain closure.** The objects the fold generates are: parts of the One, even divisions, bit-streams, fold-depths, tuples of parts, and proportions. The fold maps each into the domain — a part to a part (double-and-cast-out stays in (0,1]); an even division to an even division (R4); a bit-stream to its shift (R2); a depth k to k+1; a tuple coordinatewise to a tuple; a proportion to a proportion. Nothing the fold produces lies outside the domain: the system is closed under its own operation, hence all-encompassing of everything it generates. ∎

---
Every theorem is derived from the One using ratio and division only, and quantified where it ranges (all k, all M, all m, all dimensions). Definitions Q1–Q3 owe no proof. Confirmations in claims_pure.py reproduce each exactly; they are confirmation, not the proof.

**R9 (Q12) — opposition of relations returns the One.** The opposite of a relation r is its reciprocal, the proportion one-to-r. Combining a relation with its opposite is multiplying them: r · (1/r) = 1, the One. The balance of opposed relations is therefore the One — the multiplicative identity standing exactly where additive zero stands in a signed system, but as unity, so nothing is lost. Holds for every relation r. ∎

**R10 (Q13) — opposition of positions is the half-One.** The opposite of a position p is its antipode, the position a half-One away (p with the half-One added, the One cast out). The separation between a position and its antipode, taken the short way, is the half-One — the maximal separation on the whole. Two equal influences so placed have no net direction; their resultant is the centre, the One itself. Cancellation is a return to the One, not annihilation to zero. Holds for every position p. ∎

---
## Emergence theorems (Part B)

**RB1 (E1) — interlocking cycles return at the lcm.** A part with odd denominator is purely periodic under the fold, with some period L (the number of folds to return). Two such parts a, b with periods L_a, L_b run together as a pair; the pair returns to its joint start exactly when both have returned, i.e. after a number of folds divisible by both L_a and L_b. The least such is the least common multiple lcm(L_a, L_b). So the joint cycle — the beat — has period lcm(L_a, L_b), built from the interlocking of two exact rational rhythms, with no continuous curve. ∎

**RB2 (E2) — the power-of-two lattice collapses to the One.** Every part i/2^k is dyadic: its bit-stream terminates, so after at most k folds the casting-out brings it to the One and it stays there. A lattice of such parts therefore folds into the single region containing the One. (This is an exact edge, distinct from the odd-denominator lattices, whose orbits stay periodic and spread.) ∎

**RB3 (E5) — the separation-modulation is periodic with the beat period.** Two parts a, b each purely periodic under the fold return jointly after the beat period L = lcm of their periods (RB1). The separation between them at each step is a function of the joint state; since the joint state repeats every L folds, the separation sequence repeats every L folds. So the modulation — the rise and fall of their separation between unison and the half-One — is exactly periodic with the beat period. ∎
