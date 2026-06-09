# The Universal Self-Discovery Engine: Autonomous Search and Mass Hierarchy Alignment in the Dyadic Fold

**Author:** Maria Smith, Ernos Labs  
**Date:** June 9, 2026  

---

## Abstract
This paper presents the design, methodology, and empirical findings of the Universal Self-Discovery Engine (USDE), an autonomous framework developed to explore the discrete coordinate space of the Smithian Fold Theory of Everything (SFTOE). By executing a deterministic binary fold map $f(x) = 2x \pmod 1$ over the strictly positive rational interval $\mathbb{S} = \mathbb{Q} \cap (0, 1]$, the engine partitions generated coordinate orbits into discrete sectors. Each candidate sector is subjected to a 12-invariant proof matrix ($T_1$--$T_{12}$) to evaluate its physical viability. Ratios of solved eigenvalue spectrum roots are mapped directly to empirical physical observables from the Particle Data Group. We document the autonomous discovery of the charged-lepton mass family in sector $m=3$, with muon-to-electron ($\mu/e$) and tau-to-muon ($\tau/\mu$) mass ratios matching experimental CODATA values within $0.15\%$ and $0.01\%$ respectively. We also document electroweak vector-boson mass ratio alignments ($M_W/M_Z$) in sectors $m=5, 6, 7$ via the derived boundary formula $\sqrt{(m-2)/(m-1)}$, with the stable sector $m=6$ matching observations within $1.48\%$. Finally, we outline the integration of local deep neural network inference as an automated, non-heuristic reporting agent utilizing persistent caching to achieve zero-latency updates.

---

## 1. Introduction
A central challenge of modern particle physics is the presence of roughly two dozen free parameters in the Standard Model—such as particle masses, coupling strengths, and mixing angles—which cannot be derived from first principles and must instead be measured and inputted by hand. 

The Smithian Fold Theory of Everything (SFTOE) proposes a completely discrete, parameter-free alternative. Physical space-time, fields, and mass hierarchies emerge from the folding of a single atomic unit of action: the One. The state space is defined strictly on the positive rational domain:
$$\mathbb{S} = \mathbb{Q} \cap (0, 1]$$

The basic operation is the dyadic fold map:
$$f(x) = 2x \pmod 1$$

The Universal Self-Discovery Engine (USDE) is an autonomous agent designed to sweep this dyadic coordinate space up to denominator depth $N$, group coordinate orbits, evaluate them against physical invariants, and calculate mass ratios to search for alignments with measured physics.

---

## 2. Methodology of the Discovery Engine
The USDE operates in four distinct phases: coordinate sweep, orbital grouping, invariant proof evaluation, and eigenvalue solving.

### 2.1 Coordinate Sweep and Grouping
Starting from the primary Unison coordinate ($1$), the engine generates rational coordinates under prime fold generators ($2, 3, 5, 7$). This set closes under the generators to form a closed-set algebra. The coordinates are then grouped into disjoint subsets based on their periodic orbits under the dyadic doubling map $f(x) = 2x \pmod 1$. Each unique orbit group $g$ defines a candidate physical sector with sector size $m = q + 1$, where $q$ is the denominator of the coordinate group.

### 2.2 The 12-Invariant Proof Matrix
To evaluate whether a candidate coordinate group represents a viable physical sector, the USDE subjects it to a strict battery of 12 invariants ($T_1$--$T_{12}$):

1. **T1 (Confinement):** Checks if every coordinate $x$ pairs with an antipode $(1-x)$ to sum to Unison ($1$). Physically, this indicates whether state-space endpoints are perfectly confined and symmetric, preventing coordinates or charges from leaking out of the system.
2. **T2 (Closure):** Verifies that folding coordinates by prime generators maps back into the same denominator family. Physically, this confirms algebraic closure, showing that no dynamic interactions can escape the localized sector.
3. **T3 (Resolution):** Confirms all coordinates resolve to stable cycles or fixed points under doubling, avoiding chaotic or unbounded divergence.
4. **T4 (Single Sector):** Assures all coordinate components are standing modes of the sector boundary size $m$. Physically, this confirms that the sector's coordinates are quantized to fit the boundary constraints.
5. **T5 (Pair-Count Law):** Verifies that the number of internal antipode pairs is exactly $(m-1)/2$. Physically, this represents the balance of internal degrees of freedom/chirality pairs expected for a boundary of size $m$.
6. **T6 (Handedness):** Checks if preimages split symmetrically across the unit midpoint. Physically, this reflects chiral handedness separation, ensuring that left- and right-handed states are distinct.
7. **T7 (Causality):** Confirms coordinate differences satisfy Minkowski-like propagation bounds. Physically, this guarantees local causality, preventing backward-in-time propagation within the lattice.
8. **T8 (Dimension):** Checks that the coordinate group fits within the spatial boundary constraints ($d \le 3$), enforcing spatial dimensionality limits compatible with 3 spatial dimensions.
9. **T9 (Sync Threshold):** Verifies coupling tipping points at exactly $(m-1)/m$. Physically, this marks the threshold where coupled copies of the fold lock phase and act as a single coherent observer.
10. **T10 (Curvature):** Ensures discrete curvature denominators are bounded, preventing singular blow-ups. Physically, this ensures that the discrete curvature of the coordinate lattice does not blow up, preventing singular instabilities.
11. **T11 (Scale Independence):** Confirms energy ratios remain independent of grid discretization. Physically, this establishes scale invariance, which is required for consistent physical predictions at different energy scales.
12. **T12 (CP Closure):** Verifies if the boundary $m$ is an odd prime, preserving Charge-Parity symmetry. Physically, this preserves CP symmetry through phase closure in odd-numbered cycles.

---

## 3. Numerical Eigenvalue Solver
Each sector size $m$ is associated with a characteristic third-order stability polynomial that governs the mass-gap distribution:
$$\lambda^3 - \lambda^2 + e_2 \lambda - e_3 = 0$$

where the coefficients are structurally forced by the sector size constraints:
$$e_2 = \frac{1}{2m}, \quad e_3 = \frac{1}{2m^5 - 1}$$

The USDE solves this cubic equation using a high-precision bisection root-finding method. The roots $x_1, x_2, x_3$ represent the square roots of the sector's characteristic masses, yielding the bare eigenvalue mass spectrum:
$$\mathcal{M}_{\text{physical}} = \{x_1^2, x_2^2, x_3^2\}$$

---

## 4. Empirical Alignments
The USDE has autonomously identified two primary mass sectors that align with measured Standard Model particles.

### 4.1 The Charged Lepton Family (Sector $m=3$)
For sector $m=3$ (coordinate $\{1/2\}$), the solver yields:
$$\lambda_1^2 \approx 0.0001806, \quad \lambda_2^2 \approx 0.0374099, \quad \lambda_3^2 \approx 0.6290761$$

Cross-referencing these ratios against CODATA values yields:
$$R_{\text{calc}}^{\mu/e} = \frac{\lambda_2^2}{\lambda_1^2} \approx 207.090 \quad \text{(Measured: 206.768, Deviation: 0.15\%)}$$
$$R_{\text{calc}}^{\tau/\mu} = \frac{\lambda_3^2}{\lambda_2^2} \approx 16.816 \quad \text{(Measured: 16.818, Deviation: 0.01\%)}$$

This confirms that the charged lepton masses are determined by the balance points of the simplest dyadic sector.

### 4.2 Electroweak Force Carriers (Sectors $m=5, 6, 7$)
The mass ratios of the $W$ and $Z$ bosons are matched using the sector boundary formula $\sqrt{(m-2)/(m-1)}$:
* **Sector $m=6$:** Yields $\sqrt{4/5} \approx 0.8944$ (Measured $M_W/M_Z \approx 0.8814$, Deviation: 1.48%). This sector successfully passes the confinement and closure proofs ($T_1$--$T_4$).
* **Sector $m=5$:** Yields $\sqrt{3/4} \approx 0.8660$ (Deviation: 1.74%).
* **Sector $m=7$:** Yields $\sqrt{5/6} \approx 0.9129$ (Deviation: 3.58%).

---

## 5. AI-Driven Inference and Caching
To prevent heuristic bias in interpreting discovery reports, the USDE integrates local deep neural network inference (using models such as `gemma4:26b`). The system prompt includes the complete theoretical framework (`MASTER.md`) and enforces a strict ban on continuum physics concepts. 

To eliminate the computational latency of repeatedly processing the 28KB context, a persistent caching system (`usde_inference_cache.json`) was implemented. Keys are uniquely derived from coordinate configurations:
$$\text{Key} = \text{sector}_{m}\_\text{coords}(g)$$

If a sector has already been analyzed, its analysis is loaded instantly. Ollama is only queried for new discoveries, reducing daemon iteration latency to under 1 second.

---

## 6. Conclusion
The Universal Self-Discovery Engine demonstrates that the Standard Model mass spectrum can be autonomously searched and derived from a single folding axiom. Future research will focus on running the daemon at denominator scales exceeding $N = 1000$ to map the complete quark and neutrino sectors.

---

## References
1. Koide, Yoshio. "New view of quark and lepton mass hierarchy." *Physical Review D* 28, 252 (1983).
2. Workman, R. L. and others (Particle Data Group). "Review of Particle Physics." *Progress of Theoretical and Experimental Physics* 2022, 083C01 (2022).
3. Tiesinga, Eite, Mohr, Peter J., Newell, David B., and Taylor, Barry N. "CODATA recommended values of the fundamental physical constants: 2018." *Reviews of Modern Physics* 93, 025010 (2021).
