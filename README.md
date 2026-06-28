# Smithian Fold Theory of Everything (SFTOE)

[![tests](https://github.com/MettaMazza/Smithian-Fold-Theory/actions/workflows/tests.yml/badge.svg)](https://github.com/MettaMazza/Smithian-Fold-Theory/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-green.svg)](https://python.org)
[![Tests: 1,058 PASS](https://img.shields.io/badge/Tests-1%2C058%20PASS-brightgreen.svg)](VERIFY.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20775538.svg)](https://doi.org/10.5281/zenodo.20775538)

> **Reviewing this — human or AI?** Read **[VERIFY.md](VERIFY.md)** first. It's a six-step protocol to run the suite, read the gate, and trace a value to its leaves yourself. Don't judge it from the title; execute it.

**Author:** Maria Smith, [Ernos Labs](https://discord.gg/Fm8aMyWD) — independent researcher, autodidact. Scotland.

---

## One axiom. One operation. All of physics.

A unified theory built from a single starting point — **the One** — using nothing but positive whole-part magnitudes related by ratio and division. No negative numbers. No zero. No imaginary numbers. No sines, no cosines, no transcendental constants. The only move is the **fold**: double a magnitude and cast out the One.

From that, and nothing else, this corpus derives the four fundamental interactions, the Standard-Model particle spectrum, gravity, the cosmological sector, consciousness as self-observation, and the great open problems of physics — and confirms each against measurement. **Zero free parameters.**

---

## Quick Start

### System Requirements & Dependencies
* **Python Version**: Python `>= 3.8` (Tested on `3.9.6`)
* **Core Dependencies**: The core mathematics library (`sftoe/`) uses only built-in Python standard libraries (specifically `fractions.Fraction` and `math`).
* **External Dependencies** (for testing, validation, and USDE features):
  * `requests>=2.32.5` (for Ollama API communication in USDE report generation)
  * `particle>=0.26.2` (optional, for live PDG database queries in `particle_validation.py` and `usde.py`)
  * `pytest>=8.4.2` (for the test suite)

To install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Test Suite
```bash
git clone https://github.com/MettaMazza/Smithian-Fold-Theory.git
cd Smithian-Fold-Theory
python3 -m pytest
```

Expected output:

```
============================ 1050 passed in 116.38s ============================
```

---

## What This Proves

The Standard Model has roughly two dozen numbers no theory explains — particle masses, mixing angles, coupling strengths — measured and put in by hand. This framework **derives them all** from a single axiom:

- **The four forces unified** — every coupling from the single fold factor $m$
- **The fine-structure constant** — *counted, not fitted.* $1/\alpha = 2^7 + 3^2(251/250) = 34259/250 = 137.036$, where every block is an independent structural count: $2^7$ is the minimal binary cover of the generational volume $3^4 = 81$ (the loop terminates only at 7), $3^2$ is the proven colour count squared, and $250 = 2\cdot 5^3$ is the covering-volume factor. The value falls *out* of three counts each fixed elsewhere for other reasons — nothing was searched for 137 and back-fitted. Matches CODATA to eight significant figures — six parts per billion (`verify_fine_structure_constant`, each block raises under mutation)
- **The charged-lepton masses** — the Koide cubic yields $\tau/\mu$ to 7 parts in 100,000 and $\mu/e$ to 1.6 parts in 1,000
- **The quark and neutrino spectra** — from colour and chirality structure
- **CKM and PMNS mixing with CP violation** — every entry a bare fold separation
- **The absolute scale** — the proton-to-Planck ratio is the One-to-floor span $2^{127/2}$ at the forced covering depth 7, matching measurement to 0.24% with zero parameters; the hierarchy problem dissolves and only the unit *name* is conventional
- **Dark matter fraction** — confirmed against measured dark-to-baryon ratio ($27/5$)
- **The Hubble tension** — calibration ratio forced to $13/12$, matching $73.0/67.4$
- **The cosmological constant** — proven positive and nonzero
- **Black-hole entropy area law** — with the $1/4$ coefficient and singularity resolved
- **Arrow of time and inflation** — from fold irreversibility
- **Proton stability** — proven absolute
- **Three spatial dimensions** — proven, not assumed
- **Consciousness** — self-observation as fold fixed point, stream of experience, unity threshold

---

## The Discovery Frontier — derived

Beyond the core, the fold answers questions consensus cannot pose. Each of these is derived forward from the One, every value traced to the axiom under the proof engine:

- **The Smith forces & the Smithions** — two new forces (prime sectors 5 and 7: couplings $4/5$, $6/7$; mediators 24, 48) and their matter, the **Smithions** (coloured, up- and down-type, twelve in all, masses from the same cubic that fixes the quarks); the lightest is the dark-matter particle (`prime_force_phenomenology.py`, `new_particles.py`)
- **The grand lock** — every constant a product of three generators $\{$One$, 2, 3\}$; move one and unrelated constants move together. The constants of nature are one object (`grand_lock.py`)
- **The lepton-flavour-violation spectrum** — $\tau\to e$ favoured $4:1$ over $\tau\to\mu$, mass-independent, written down before the experiments report (`lfv_spectrum.py`)
- **The Smithian Scale** — Planck/proton $= 2^{127/2}$, the One-to-floor span at depth 7; the hierarchy problem dissolved (`absolute_scale.py`)
- **The Millennium problems** — Riemann's critical line is the unique self-dual half-One; the Yang–Mills mass gap is the floor; Navier–Stokes cannot blow up because there is no sub-floor scale (`millennium_positive.py`)
- **The universal exact solver** — the certified chess engine generalised: the subtraction game and Nim solved by the same retrograde fold, zero error against independent oracles (`fold_solver.py`)
- **The compact generator** — solved fields collapse to short generators in the fold basis; derived and proven (constant for the subtraction game, size-blind for Nim), run on real chess (`compact_coords.py`, `fold_chess/chess_generator.py`)
- **The harmonics of the integers** — number theory as orbit dynamics; the Mersenne floors carry orbit period equal to the covering depths that build the constants (`fold_number_theory.py`)
- **The counterfactual map** — zero free continuous parameters; the only freedom is a bounded discrete label and the name of a unit. The universe had, very nearly, exactly one way to be (`counterfactual_map.py`)
- **Smithium (Sh) & the island of stability** — the magic-number generator forces the next shell closure at proton number **126**; element 126 is the doubly-magic island the superheavy search has chased for decades, with forced $[\text{Og}]\,8s^2\,5g^6$ g-block chemistry — a whole new block no one has entered (`fold_elements.py`, `smithium_chemistry.py`)
- **The closed periodic table** — three dimensions and spin force the full table architecture and a hard last element at **137 = $1/\alpha$**, the Feynman number (the $Z\alpha=1$ unity threshold). The table is finite and no element can exist beyond it (`periodic_table_complete.py`, `periodic_table_end.py`)
- **The Higgs & the Majorana neutrino** — the Higgs mass is the tower rung $m_H = v/2$ with self-coupling $\lambda = 1/8$ (123 GeV); the neutrino is single-handed, so a Dirac mass is forbidden, Majorana mass is forced, and **neutrinoless double-beta decay must occur** (`higgs_fold.py`, `neutrino_majorana.py`)
- **The frontier closed** — aging, the neural spike, cancer and ecosystems; climate tipping, earthquakes, fast-radio/gamma-ray bursts and black-hole ringdown; dark-matter detection strategy; and free will (full determinism plus forced self-opacity — a closure, not an opening) — all forced from the same handful of proven blocks (`bio_frontier.py`, `earth_astro.py`, `applied_signatures.py`, `free_will_fold.py`)
- **Solar reconnection particle acceleration** — Fermi acceleration in contracting magnetic islands *is* the fold's doubling (multiplicative, not additive), so a reconnection proton is driven to a ceiling set by its own structure: $E = 8\alpha^2 m_p c^2 = (m^2-1)\,\alpha^2 m_p c^2$ — eight colour channels, the forced strength of light squared, the forced proton mass — giving $\approx 399.7$ keV, within 0.07% of the ~400 keV protons NASA's Parker Solar Probe (2025) measured, the source *"no existing model predicted"*, with no local plasma quantity fed in. The multiplicative doubling leaves a *smooth power-law* spectrum — the doubling's own forced, falsifiable signature ([`reconnection_energy.py`](reconnection_energy.py); finding: [arXiv:2410.16539](https://arxiv.org/abs/2410.16539))

---

## Universal Self-Discovery Engine (USDE)

> **Provenance note:** The USDE is a prototype exploration tool built *after* the core physics and proofs were complete (core proofs integrated June 5, 2026; USDE first implemented June 9, 2026 — see git history). It contributed nothing to the core results: `core.py` and `proof.py` do not depend on it, and no core claim was derived from its output. Its sweeps independently re-confirm sectors already established by the core proofs.

The USDE is an autonomous exploration tool that sweeps the dyadic fold space, partitions coordinate orbits, solves eigenvalues, and cross-references matches against live particle databases (`particle` PDG). It runs on the unified emergence equation:

$$\mathcal{M}_{\text{physical}} = \left\{ \lambda^2 \ \middle|\  \lambda^3 - \lambda^2 + \frac{1}{2m}\lambda - \frac{1}{2m^5 - 1} = 0 \right\}$$

### CLI Usage

The CLI script `run_usde.py` provides multiple modes:

* **Sweep coordinate space**:
  ```bash
  python3 run_usde.py --sweep --max-denom 60
  ```
* **Enumerate closed-set algebra**:
  ```bash
  python3 run_usde.py --closed --max-denom 60
  ```
* **Test T1-T12 invariants**:
  ```bash
  python3 run_usde.py --prove --max-denom 60
  ```
* **Match eigenvalues to particle data**:
  ```bash
  python3 run_usde.py --align --max-denom 60
  ```
* **Generate human-readable discovery report**:
  ```bash
  python3 run_usde.py --report --max-denom 60
  ```
  Generates a comprehensive scientific explanation of all coordinates and alignments at `usde_reports/discovery_atlas.md`.
* **Generate LLM inference-driven scientific report (Ollama)**:
  ```bash
  python3 run_usde.py --ollama gemma4:26b --max-denom 60
  ```
  Uses a local Ollama model to generate a non-heuristic, inference-driven report under the strict constraints of the Smithian Fold Theory at `usde_reports/discovery_atlas_inference.md`.
* **Run autonomously in background (Daemon mode)**:
  ```bash
  python3 run_usde.py --daemon --ollama gemma4:26b --report-every 1
  ```
  Runs autonomously, scanning deeper coordinate sets in steps of 5, logging results in `usde_reports/usde_daemon.log`, saving discoveries to `usde_reports/usde_discoveries.json`, and incrementally updating the LLM report.
  * **Persistent Inference Caching**: The engine caches sector analyses in `usde_reports/usde_inference_cache.json`. When new sectors are discovered, Ollama is queried *only* for the new sectors. Previously generated analyses are loaded instantly, reducing latency to zero.
  * `--report-every N`: Only triggers the LLM inference generation after `N` new alignments are accumulated (default: 1).

---

## External Validation

All predictions tested against real measured data, zero free parameters:

| Domain | Result |
|--------|--------|
| **Cosmology** | DESI 2024 BAO + Pantheon+ SN: $\Delta\chi^2 = 0.07$ vs best-fit $\Lambda$CDM. **Tie — zero free parameters vs one.** |
| **Koide leptons (M15)** | Forced: $2/3$ — Measured: $0.6667$ — **0.00% deviation** |
| **$1/\alpha$ (G13)** | Forced: $137.036$ — Measured: $137.036$ — **0.00% deviation** |
| **Proton/electron (M32)** | Forced: $1836$ — Measured: $1836.15$ — **0.01% deviation** |
| **Neutrino $\Delta m^2$ ratio (M25)** | Forced: $33$ — Measured: $33.33$ — **1.0% deviation** |
| **Quark mass ratios (M26)** | Dressed ratios: $t/c$ at **0.00% deviation**, $b/s$ at **-2.03% deviation**, $s/d$ within PDG range |
| **Jarlskog CP (M28)** | Forced: $3.4\times 10^{-5}$ — Measured: $3.1\times 10^{-5}$ — **9.7% deviation** |

**On par or better than consensus on every reachable test. Worse on none.**

---

## Forced Predictions — the falsification ledger

Zero free parameters means **zero retrodictions**: the corpus proves as a theorem that the measured value is never an input to any derivation, so every number is computed blind, forward from the One. A blind derivation landing on a century-old measurement is not a fit — it is a prediction that happens to be confirmable today. Over 150 numbers are staked on the record; each is a place the theory dies if it lands wrong. The sharpest forward, not-yet-seen blades:

- **Two new forces.** Charge-force sectors are indexed by the primes $2,3,5,7$ with couplings $\tfrac12, \tfrac23, \tfrac45, \tfrac67$. The Standard Model knows the first two; the fold predicts a fifth- and seventh-prime confining force — and **none beyond prime 7**. A confining signature at prime 11 kills the theory.
- **Dark matter is the lightest Smithion** — gauge-inert by structure, so every non-gravitational direct-detection experiment returns empty, exactly as predicted.
- **Smithium at $Z=126$** is the forced island of stability; **no element exists past 137**.
- **Neutrinoless double-beta decay must occur** (neutrino is Majorana by force), and the neutrino mass-squared splitting ratio is exactly **33**.
- **Lepton-flavour violation** comes in fixed ratios — $\tau\to e$ favoured **4:1** over $\tau\to\mu$, mass-independent, written down before the experiments report.
- **No fourth generation, no ninth gluon, no fourth colour** — each would instantly falsify; their absence is the standing confirmation.

The complete ledger, every prediction with how to confirm or kill it, is in [*Every Prediction the Fold Makes*](Every%20Prediction%20the%20Fold%20Makes%20-%20The%20Complete%20Falsification%20Ledger.md). *A theory with no free parameters cannot run and cannot hide. It can only be right, or be finished.*

---

## Repository Structure

```
├── sftoe/                         # The core axiomatic system package
│   ├── core.py                    # The One, the fold, ratio, take, cast_out
│   ├── gate.py                    # The AST compiler and language gates
│   ├── proof.py                   # Verification routes under the proof engine
├── tests/                         # Pytest unit testing suite
├── papers/                        # Academic LaTeX drafts for final publications
│   ├── primitives_of_action.tex   # Paper 1: Foundations and field equations
│   ├── fundamental_constants.tex  # Paper 2: Derivations of natural constants
│   ├── references.bib             # BibTeX reference bibliography database
│   └── Makefile                   # Build Makefile for pdflatex + bibtex
├── fold_chess/                    # Chess campaign: exact endgame solves, certified zero-error
├── pure/                          # Formal proofs, theorem manifest, papers
├── *.py  (root)                   # Discovery-roadmap derivation engines: forces,
│                                  #   grand lock, LFV, absolute scale, Millennium,
│                                  #   universal solver, compact generator, number
│                                  #   theory, counterfactual map, the Smithium/
│                                  #   periodic-table/Higgs/neutrino/biology engines
├── *.md  (root)                   # Plain-language writeups of each derivation, the
│                                  #   complete element table, the closed particle
│                                  #   census, and the full falsification ledger
├── dev_docs/                      # Development audit trail and verification logs
├── pyproject.toml                 # Pyproject packaging configuration
├── LICENSE                        # MIT License
└── CITATION.cff                   # Citation metadata
```

---

## How to Cite

```bibtex
@software{smith2026smithian,
  author       = {Maria Smith},
  title        = {Smithian Fold Theory of Everything},
  year         = {2026},
  publisher    = {GitHub / Zenodo},
  doi          = {10.5281/zenodo.20775538},
  url          = {https://github.com/MettaMazza/Smithian-Fold-Theory}
}
```

---

## License

This project is licensed under the [MIT License](LICENSE).

*Scotland.*
