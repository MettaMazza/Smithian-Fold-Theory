# The Lepton-Flavour-Violation Spectrum — The Fold's Forced Prediction

When a muon turns into an electron, or a tau into a muon, the lepton's flavour
changes — a process the Standard Model permits but about which it predicts almost
nothing. Whether these flavour-violating transitions ever happen, and in what
relative proportions, is left open: the Standard Model has no rule for the rates.
The fold has a rule, and it is exact. The three lepton generations sit at fixed
fold positions — standing modes — and a flavour-changing transition has an
amplitude set by the *separation* between those positions, so its rate goes as
that separation squared. From this, the entire spectrum of relative rates is
forced. (`lfv_spectrum.py`, every value traced to the One.)

## The structure

The three lepton generations occupy the standing modes of the five-fold:

| Generation | Channel position | Mass-part |
|---|---|---|
| electron | 1/4 | 1/6 |
| muon | 1/2 | 1/2 |
| tau | 3/4 | 5/6 |

A flavour-violating transition between two generations has an amplitude equal to
the separation between their channels (the fold's `take`), and a rate equal to
that separation squared:

| Transition | Step | Separation (amplitude) | Rate-weight |
|---|---|---|---|
| muon → electron | 2 → 1, adjacent | 1/4 | 1/16 |
| tau → muon | 3 → 2, adjacent | 1/4 | 1/16 |
| tau → electron | 3 → 1, two-step | 1/2 | 1/4 |

The adjacent separations are equal (both 1/4) and the two-step separation is
exactly their sum (1/2) — a forced relation, not a fit.

## The sharp, falsifiable prediction

The cleanest test sits inside the tau, because the tau can violate flavour in two
ways — toward the electron or toward the muon — and when the parent is the same,
the mass and the phase space cancel completely, leaving the ratio **purely fold**:

**The fold predicts lepton-flavour-violating tau decays favour the electron
channel over the muon channel by exactly four to one.**

The tau-to-electron transition is a two-step separation (1/2); the tau-to-muon is
adjacent (1/4); the rate goes as the square, so the ratio is (1/2 ÷ 1/4)² = 4. No
mass enters — both daughters are light, both come from the same tau — so this is a
clean, parameter-free number. When lepton-flavour-violating tau decays are finally
observed, the electron-flavour channels must outnumber the muon-flavour channels
four to one, or the fold is wrong. The Standard Model says nothing here; the fold
writes the answer down in advance.

## The adjacent equality

A second forced statement: the muon-to-electron transition and the tau-to-muon
transition are *both* single-step, adjacent separations, so they share the
identical generation amplitude. Their separation-normalized rates are equal. Any
difference in their physical rates comes purely from the mass and phase-space
weighting — which the fold also supplies, from the same mass-parts that fix the
lepton masses. There is no independent freedom anywhere in the spectrum.

## The full physical structure

Weighting each transition by its parent mass-part gives the fold's complete
forced structure for the physical rates:

| Transition | rate-weight × parent mass-part | = |
|---|---|---|
| muon → electron | 1/16 × 1/2 | 1/32 |
| tau → muon | 1/16 × 5/6 | 5/96 |
| tau → electron | 1/4 × 5/6 | 5/24 |

Every number traces to the One through the fold; not one is fitted, and the same
mass-parts that fix these weights are the ones that fix the lepton masses
themselves — so the LFV spectrum is locked to the mass spectrum, the same grand
lock that binds the rest of the constants.

## What consensus cannot do here

The Standard Model has no generative structure for flavour, so it cannot predict
the ratio of one lepton-flavour-violating channel to another — every such rate is
an independent unknown until measured, and most are simply parametrized away. The
fold forces the entire pattern from the geometry of where the generations sit: the
four-to-one tau preference, the adjacency equality, the mass-weighting, all from
the standing modes and the separations between them. This is a clean,
near-term-testable prediction in a place the Standard Model is silent — the kind
of forward statement only a theory with a generative root can make. The
experiments are searching for these decays now. The fold has already told them
what the ratios will be.
