# Multimode Dark Memory

How much unknown quantum information can an ensemble store when a vacuum reservoir sees only a few independent spatial radiation patterns?

For $`N`$ two-level emitters with an arbitrary supplied rank-$`r`$ matrix of collective lowering profiles, the common dark space satisfies

```math
\dim\mathcal K_G\ge
\left\lceil\frac{2^N}{\binom{N+r}{r}}\right\rceil.
```

The worst-profile **dark-code redundancy** has order $`r\log(N/r)`$ for $`1\le r=o(N)`$. Every such profile sequence therefore permits $`N-o(N)`$ logical qubits. Uneven couplings and a growing number of profiles are allowed; permutation symmetry is not required.

**[Read the science](science/README.md)** · [Learn the argument](learning/README.md) · [30 milestones](learning/milestones.md) · [Four-emitter stored qubit](science/examples.md) · [Reproduce the checks](verification/README.md)

## Write, hold and read

1. **Compile the blocks.** Supply the exact complex-rational lowering profiles and an endpoint error budget. Partition the emitters into logarithmic-size blocks. Within each excitation sector, stack the restricted lowering matrices and compute their [common nullspace](science/encoding-and-precision.md#3-exact-classical-linear-algebra). Pick the sector with the largest dark dimension in each block and keep the largest power of two of its orthonormal basis states. Complete the chosen encoding columns to a block unitary and [compile it](science/encoding-and-precision.md#4-from-block-matrices-to-circuits) into CNOTs and single-qubit rotations.
2. **Write and hold.** Initialize the redundancy emitters for each block and put the leftover emitters in their ground states. Apply each block encoder to its part of the unknown input and the initialized emitters. Start storage with the reservoir in vacuum. During storage the emitters share one transition frequency and undergo the specified excitation-preserving rotating-wave interaction through the supplied spatial span. The code has a fixed total excitation number, so its free evolution gives a common phase. The physical emitters carry the state throughout the hold without measurement, reset or control.
3. **Read.** Apply the inverse block circuits and return the logical register, including its correlations with any reference. Release the initialized redundancy and unused emitters. Decoding uses no measurement, flag or classical outcome processing.

The [compilation theorem](science/encoding-and-precision.md#1-endpoint-compilation-theorem) counts all emitters, classical arithmetic, gate synthesis and precision. It gives polynomial endpoints with rate tending to one at fixed rank or rank growing slower than the logarithm of emitter count. The broader rank theorem gives a dark-space dimension for every sublinear rank. The synthesis error bound is uniform in hold time under the exact supplied dynamics. [Coefficient error](science/encoding-and-precision.md#6-wrong-coefficients-are-a-different-error-source) has its own time-dependent bound. [Four-emitter example](science/examples.md)

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

## Learn the argument

The [learning route](learning/README.md) starts with the stored-qubit example and connects protected-subspace physics to the counting theorem and paid encoder. Its single educational anchor is Daniel A. Lidar's DFS review, [arXiv:1208.5791v3](https://arxiv.org/abs/1208.5791v3), 24 October 2013. The [source bridge](learning/anchor-and-bridge.md) translates the review's assumptions and notation; the [30-milestone map](learning/milestones.md) follows the project's background and contribution through to its resource and evidence limits.

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
