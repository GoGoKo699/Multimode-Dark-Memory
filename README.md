# Multimode Dark Memory

How much unknown quantum information can an ensemble store when a vacuum reservoir sees only a few independent spatial radiation patterns?

For $`N`$ two-level emitters with an arbitrary supplied rank-$`r`$ matrix of collective lowering profiles, the common dark space satisfies

```math
\dim\mathcal K_G\ge
\left\lceil\frac{2^N}{\binom{N+r}{r}}\right\rceil.
```

The worst-profile **dark-code redundancy** has order $`r\log(N/r)`$ for $`1\le r=o(N)`$. Every such profile sequence therefore permits $`N-o(N)`$ logical qubits. Uneven couplings and a growing number of profiles are allowed; permutation symmetry is not required.

**[Read the science](science/README.md)** · [Exact theorem and proof](science/rank-law.md) · [Four-emitter stored qubit](science/examples.md) · [Reproduce the checks](verification/README.md)

## What is established

| Result | Guarantee and scope |
|---|---|
| Finite dark-space bound | Uniform over every supplied complex profile matrix; a commuting-nilpotent dimension argument. |
| Matching redundancy order | Disjoint collective-decay groups supply a worst-profile example with the same order, up to constants. This optimizes the common-kernel code class. |
| Exact passive vacuum storage | The full rotating-wave light–matter interaction vanishes on the code tensor reservoir vacuum. No bath Markov approximation is needed. |
| Stationary code | Selecting one excitation sector costs at most another $`\log_2(N+1)`$ qubits and removes logical free-precession phases. |
| Paid endpoint compilation | For fixed $`r`$, or $`r=o(\log N)`$, logarithmic blocks give rate one with polynomial classical and circuit cost for exact rational coupling data. |
| Precision accounting | Endpoint synthesis error has a time-uniform bound under the exact model. Coupling-calibration error has a separate, time-dependent bound. |

The protected input may be entangled with an inaccessible reference. All physical emitters, including initialized redundancy, are counted. No quantum bypass, measurement, reset or active control carries the input during storage.

## The physical mechanism

Each radiation pattern couples through a lowering operator

```math
L_a=\sum_{j=1}^{N}G_{aj}\sigma_j^-.
```

A state in $`\bigcap_a\ker L_a`$ cannot create a reservoir excitation through any of the supplied patterns. The reverse interaction annihilates the vacuum. The same code works for arbitrarily many oscillator frequencies and time-dependent mixing within that fixed spatial span. The [model](science/model.md) states the complete Hamiltonian and reference-sensitive storage interface.

Standard DFS criteria and the single-mode high-rate count are inherited. The [comparison](references/related-work.md) separates those foundations from the uniform growing-rank resource law, its worst-profile scaling and its block implementation.

## Read by question

| Interest | Route |
|---|---|
| Physical setup and input promises | [Model](science/model.md) → [scope](science/limitations.md) |
| Complete analytical proof | [Rank law](science/rank-law.md) → [encoding and precision](science/encoding-and-precision.md) |
| A concrete encoded state | [Worked qubit](science/examples.md) → [finite verification](verification/README.md) |
| Attribution and novelty boundary | [Related work](references/related-work.md) → [source register](references/source-register.md) |

[llms.txt](llms.txt) maps scientific questions to authoritative pages.

## Reproduce

```bash
python -m pip install -r verification/requirements.txt
python verification/check_dark_rank.py
python verification/compile_toy.py
python verification/check_vacuum.py
```

Outputs go to `build/`. The [verification guide](verification/README.md) distinguishes exact finite kernel checks, normalized-Choi diagnostics, full vacuum Hamiltonian checks and the analytical general theorems. No elementary-gate compiler, experimental calibration procedure or diamond-norm SDP is run by these scripts.

## Scope

The core model assumes a common emitter frequency, an initially vacuum reservoir and excitation-conserving rotating-wave coupling through the supplied span. Generic frequency disorder, counterrotating interactions, thermal photons and independent local noise can invalidate the dark code. General sublinear rank gives an existence guarantee; the polynomial compiler covers only its stated slower-rank regime. The result is not unrestricted passive-capacity optimality or unconditional free-space protection. See [limitations](science/limitations.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## Citation and reuse

Cite this repository with its inspected commit; [CITATION.cff](CITATION.cff) supplies metadata. The existing [MIT license](LICENSE) applies to the repository's original content. Referenced publications retain their own rights.
