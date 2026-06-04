# Implementation Plan: Academic Finalisation & Publishing

This plan outlines the steps to draft, organize, compile, and prepare the academic publications for the **Smithian Fold Theory of Everything (SFTOE)**.

---

## User Review Required

> [!IMPORTANT]
> The academic papers will be drafted in LaTeX format. We need to align on preprint style and journal targets to ensure proper formatting and bibliography styles.

## Open Questions

> [!WARNING]
> 1. **LaTeX Document Class**: Should we use standard `article` with a modern design layout, or the official `revtex4-2` style (typically used for APS journals like Physical Review Letters / Physical Review D)?
> 2. **Submission Target**: Are we prioritizing an arXiv preprint layout first, or targeting specific journals (e.g., *JHEP*, *Foundations of Physics*, *PRD*) directly?

---

## Proposed Changes

We will create a dedicated `papers/` directory to house the LaTeX source files, bibliography, and build automation.

### Directory Restructuring

#### [NEW] [primitives_of_action.tex](file:///Users/mettamazza/Desktop/SFTOM/papers/primitives_of_action.tex)
* **Title**: *The Primitives of Action: Reconstructing Field Dynamics from the Dyadic Fold*
* **Content Outline**:
  - **Abstract**: Reconstructing physical fields, Lorentzian space-time intervals, and quantum dispersion on a strictly positive rational domain $(0, 1]$ using a single unit of action and a doubling map.
  - **Section I: The Dyadic Domain**: Axiomatic definition of the domain $\mathbb{S}$, the no-zero constraint, the fold operator, and the take separation operator.
  - **Section II: Curvature and Lattice Propagation**: Planar and cubic lattice models, center-neighbor ratio propagation, and the definition of discrete curvature.
  - **Section III: Causal Structures & Minkowski Metrics**: Reconstructing the Lorentzian interval via positive take separation bounds on rational grids.
  - **Section IV: Quantum Dispersion & Wave Packets**: Phase rotations modeled without complex numbers, showing wave-packet dispersion limits and stability.

#### [NEW] [fundamental_constants.tex](file:///Users/mettamazza/Desktop/SFTOM/papers/fundamental_constants.tex)
* **Title**: *Fundamental Constants and Sector Structure in the Dyadic Fold*
* **Content Outline**:
  - **Abstract**: Derivation of dimensionless physical constants (fine-structure constant, Koide mass relations, cosmological fractions) as exact periodic and algebraic orbits under the dyadic fold map.
  - **Section I: Interaction Strengths as Periodic Orbits**: Explaining the recurrence theorems of rational orbits under folding.
  - **Section II: The Fine-Structure Constant**: The first-principles derivation of $1/\alpha = 2^7 + 3^2(251/250) = 137.036$ from binary depth 7, color count, and covering volume.
  - **Section III: The Lepton Mass Sector**: Solving the Koide cubic equation exactly over the rational domain, mapping to the masses of $e, \mu, \tau$.
  - **Section IV: Cosmological Bounds**: Deriving the dark-to-baryon mass density fraction ($27/5$) and vacuum energy density constraints.

#### [NEW] [references.bib](file:///Users/mettamazza/Desktop/SFTOM/papers/references.bib)
* Academic references, including foundations of discrete space-time, Koide mass relation history, fine-structure measurements, and cosmological parameters.

#### [NEW] [Makefile](file:///Users/mettamazza/Desktop/SFTOM/papers/Makefile)
* Automation script to compile the LaTeX manuscripts to PDF (`pdflatex` + `bibtex`).

---

## Verification Plan

### Automated Verification
- Build and compile the papers using the `Makefile` with `pdflatex` to ensure zero compilation warnings or bad boxes.
- Verify all cross-references, equations, and bibliography citations resolve correctly.

### Manual Verification
- Ask the user to review the generated PDF manuscripts to ensure readability, professional formatting, and clarity.
