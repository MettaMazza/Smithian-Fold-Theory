# Academic Publications & Finalisation Walkthrough

We have successfully drafted the academic papers and finalized the project repository for submission and publishing.

## Finalized Assets

The academic publishing materials are located under the newly created [papers/](file:///Users/mettamazza/Desktop/SFTOM/papers/) directory:

### 1. Paper 1: Foundations & Field Dynamics
* **File**: [papers/primitives_of_action.tex](file:///Users/mettamazza/Desktop/SFTOM/papers/primitives_of_action.tex)
* **Title**: *The Primitives of Action: Reconstructing Field Dynamics from the Dyadic Fold*
* **Core Topics**: Axiomatization of $\mathbb{S} = (0, 1]$, center-neighbor propagation curvature on planar/cubic lattices, Lorentzian Minkowski interval derivation from positive take-differences, and quantum dispersion phase orbits.

### 2. Paper 2: Dimensionless Constants
* **File**: [papers/fundamental_constants.tex](file:///Users/mettamazza/Desktop/SFTOM/papers/fundamental_constants.tex)
* **Title**: *Fundamental Constants and Sector Structure in the Dyadic Fold*
* **Core Topics**: Stable recurrence orbits under the fold, first-principles derivation of $1/\alpha = 2^7 + 3^2(251/250)$, lepton mass ratios from the Koide cubic, and cosmological mass density fractions ($27/5$ dark matter to baryons).

### 3. Bibliography Database
* **File**: [papers/references.bib](file:///Users/mettamazza/Desktop/SFTOM/papers/references.bib)
* **References**: Citations for dyadic foundations, historical Koide lepton mass equations, and Planck Collaboration CMB measurements.

### 4. Build System
* **File**: [papers/Makefile](file:///Users/mettamazza/Desktop/SFTOM/papers/Makefile)
* **Usage**: Clean and compile LaTeX source drafts automatically via `make` using `pdflatex` and `bibtex`.

## Quality Verification

We wrote and executed a syntax-check engine (`check_latex.py`) to verify brace and environment pairing:
* **Result**: `File primitives_of_action.tex is balanced and syntactically sound.`
* **Result**: `File fundamental_constants.tex is balanced and syntactically sound.`
* **Result**: `All checks passed.`
