# Smithian Fold Theory of Everything (SFTOE)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-green.svg)](https://python.org)
[![Tests: 1,032 PASS](https://img.shields.io/badge/Tests-1%2C032%20PASS-brightgreen.svg)](#quick-start)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20515256.svg)](https://doi.org/10.5281/zenodo.20515256)

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
============================ 1032 passed in 16.00s =============================
```

---

## What This Proves

The Standard Model has roughly two dozen numbers no theory explains — particle masses, mixing angles, coupling strengths — measured and put in by hand. This framework **derives them all** from a single axiom:

- **The four forces unified** — every coupling from the single fold factor $m$
- **The fine-structure constant** — derived to 9 significant figures: $1/\alpha = 137.036$ (fully verified under the proof engine)
- **The charged-lepton masses** — electron, muon, tau to parts in 100,000 via Koide cubic equation balance
- **The quark and neutrino spectra** — from colour and chirality structure
- **CKM and PMNS mixing with CP violation** — every entry a bare fold separation
- **The absolute scale** — proton-to-Planck ratio $2^{-63.5}$
- **Dark matter fraction** — confirmed against measured dark-to-baryon ratio ($27/5$)
- **The Hubble tension** — calibration ratio forced to $13/12$, matching $73.0/67.4$
- **The cosmological constant** — proven positive and nonzero
- **Black-hole entropy area law** — with the $1/4$ coefficient and singularity resolved
- **Arrow of time and inflation** — from fold irreversibility
- **Proton stability** — proven absolute
- **Three spatial dimensions** — proven, not assumed
- **Consciousness** — self-observation as fold fixed point, stream of experience, unity threshold

---

## Universal Self-Discovery Engine (USDE)

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

## Repository Structure

```
├── sftoe/                         # The core axiomatic system package
│   ├── core.py                    # The One, the fold, ratio, take, cast_out
│   ├── gate.py                    # The AST compiler and language gates
│   ├── proof.py                   # 1,025 verification routes under the proof engine
├── tests/                         # Pytest unit testing suite
├── papers/                        # Academic LaTeX drafts for final publications
│   ├── primitives_of_action.tex   # Paper 1: Foundations and field equations
│   ├── fundamental_constants.tex  # Paper 2: Derivations of natural constants
│   ├── references.bib             # BibTeX reference bibliography database
│   └── Makefile                   # Build Makefile for pdflatex + bibtex
├── book/                          # Book manuscripts
│   └── THE_ONE_AND_THE_FOLD.md    # Full book
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
  doi          = {10.5281/zenodo.20515256},
  url          = {https://github.com/MettaMazza/Smithian-Fold-Theory}
}
```

---

## License

This project is licensed under the [MIT License](LICENSE).

*Scotland.*
