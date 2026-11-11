# From decoherence-free subspaces to multimode dark memory

[Learning route](README.md) · [Milestones](milestones.md) · [Scientific account](../science/README.md)

The selected educational anchor is **Daniel A. Lidar, _Review of Decoherence Free Subspaces, Noiseless Subsystems, and Dynamical Decoupling_, arXiv:1208.5791v3, 24 October 2013**. Use the [version record](https://arxiv.org/abs/1208.5791v3) and [versioned PDF](https://arxiv.org/pdf/1208.5791v3). All page numbers below count the PDF's first page as page 1.

The review supplies the language of protected subspaces, Hamiltonian invariance and coding rate. The repository supplies the simultaneous lowering-constraint bound, its physical vacuum model, worst-profile redundancy and endpoint construction. These roles are different: a general DFS criterion identifies when a proposed code is protected; it does not by itself count the codewords available for arbitrary inhomogeneous profiles.

## 1. Begin with a stored qubit

Read the [four-emitter example](../science/examples.md#1-encode-an-arbitrary-qubit). Its two profiles are the rows of

```math
G=\begin{pmatrix}1&1&1&1\\1&2&3&4\end{pmatrix}.
```

In the one-excitation sector, an amplitude vector $`u=(u_1,u_2,u_3,u_4)`$ is dark when

```math
u_1+u_2+u_3+u_4=0,
\qquad
u_1+2u_2+3u_3+4u_4=0.
```

The example gives two orthonormal solutions, so both constraints vanish on every encoded superposition. The stored object is an unknown qubit, including its correlations with a reference. The next question is why this cancellation protects it in the full emitter–reservoir dynamics. The anchor's distinction between a protected subspace and its surrounding Hilbert space is the starting point for that explanation.

## 2. Exact reading locations in the anchor

| Anchor location | Foundation to take forward | Translation needed here |
|---|---|---|
| II.B, PDF pp. 2–3, Eqs. (4)–(10) | Collective dephasing gives a common phase within a fixed-weight subspace; rate is logarithmic code dimension divided by physical-qubit count. | Our noise is collective lowering. A fixed excitation sector removes free-precession phases, but its darkness requires additional linear constraints. |
| II.C, PDF p. 3, Eqs. (11)–(14) | Kraus operators restricted to a protected subspace share one unitary action, up to scalar factors. | The repository proves the reduced channel's action by first treating the complete vacuum Hamiltonian. |
| II.D, PDF pp. 4–5, Eqs. (19)–(21), Hamiltonian Theorem 1 | Common interaction-operator eigenvalues and a system Hamiltonian that preserves the subspace yield unitary reduced evolution. | The present microscopic protection uses a specified vacuum bath state; its raising and lowering operators need not satisfy that bath-independent criterion. |
| IV.E, PDF p. 15, Eqs. (86)–(90) | High-rate encoding already exists for the review's collective-decoherence DFS. | That example counts spin-singlet states under collective SU(2) noise. It is not the lowering-only dark-space count. |
| V.A, beginning on PDF p. 16; Theorem 2 and Eqs. (99)–(100) on p. 17 | An adjoint-closed unital noise algebra decomposes into noiseless and gauge factors. | The repository bounds common-kernel subspace codes. Its commuting lowering algebra is not adjoint-closed, and its theorem does not optimize all noiseless subsystems. |

The review labels a result “Theorem 1” in both II.C and II.D. The section and equation numbers above identify which statement is intended.

## 3. Translate the notation and assumptions

| Review notation | Project notation and meaning |
|---|---|
| System $`S`$ and bath $`B`$ | The $`N`$ emitters and the bosonic reservoir. |
| Good subspace $`\mathcal H_G`$ | A selected code inside $`\mathcal K_G=\bigcap_a\ker L_a`$. |
| Interaction $`\sum_\alpha S_\alpha\otimes B_\alpha`$ | Rotating-wave terms containing both $`L_a`$ and $`L_a^\dagger`$, paired with reservoir creation and annihilation operators. |
| System Hamiltonian $`H_S`$ | $`H_A=\omega\mathsf N`$ and any explicitly allowed code-preserving addition. |
| Code dimension $`d_N`$ and rate $`r_N`$ | $`d=\dim\mathcal K_G`$ gives $`q=\lfloor\log_2d\rfloor`$ whole logical qubits and rate $`q/N`$. In this project $`r`$ instead denotes profile rank. |

The decisive physical step is checked on the joint emitter–bath space. For $`|\psi\rangle\in\mathcal K_G`$,

```math
a_\lambda^\dagger L_a
\bigl(|\psi\rangle\otimes|\mathrm{vac}\rangle\bigr)=0,
\qquad
L_a^\dagger a_\lambda
\bigl(|\psi\rangle\otimes|\mathrm{vac}\rangle\bigr)=0.
```

The first term vanishes on the code; the second vanishes on the vacuum. There is no requirement that $`L_a^\dagger|\psi\rangle=0`$. Consequently one must not insert only the lowering operators into the anchor's bath-independent Hamiltonian criterion and declare that criterion proved.

The [storage model](../science/model.md#3-exact-vacuum-invariance) also requires vacuum-preserving reservoir dynamics and a system Hamiltonian that preserves the code. The identity $`[\mathsf N,L_a]=-L_a`$ ensures that $`\omega\mathsf N`$ preserves the common kernel. A general code undergoes known free precession, which recovery can reverse. A [fixed-excitation subcode](../science/rank-law.md#3-a-stationary-code) acquires only a global phase and admits one decoder for every storage duration. Thermal occupation, an incompatible Hamiltonian, or a new spatial profile requires additional analysis.

## 4. The steps supplied by this project

**Simultaneous constraints at arbitrary profile rank.** Single-excitation cancellation explains the opening example. The many-excitation theorem must account for spin saturation and the compatibility of several constraints. The lowering operators commute, and any product of total degree greater than $`N`$ vanishes. The [rank-law proof](../science/rank-law.md#1-a-finite-common-kernel-theorem) uses these two facts to construct the injective map

```math
|\psi\rangle\longmapsto
\bigl(P_G L^\alpha|\psi\rangle\bigr)_{|\alpha|\le N}.
```

For every nonzero input, a nonzero lowering monomial of maximal degree lands in the common kernel and survives $`P_G`$. Counting its possible multi-indices yields

```math
\dim\mathcal K_G\ge
\left\lceil\frac{2^N}{\binom{N+r}{r}}\right\rceil.
```

This is an application of a standard finite nilpotent-module dimension argument. It uses neither the adjoint-closed algebra theorem in the anchor's Section V nor a permutation-symmetry promise. The [algebraic attribution](../references/related-work.md#what-is-inherited) explains that foundation.

**Convert dimension into a resource law.** Taking logarithms gives $`N-o(N)`$ logical qubits for every $`r=o(N)`$. The [worst-profile argument](../science/rank-law.md#5-worst-profile-dark-code-redundancy) combines the universal estimate with disjoint collective-decay groups to prove redundancy of order $`r\log(N/r)`$. The groups use the inherited one-mode count. This determines an order within common-kernel dark codes; it does not determine unrestricted passive capacity or a sharp leading constant.

**Pay for encoding and decoding.** A large subspace does not automatically give an efficient encoder. The [endpoint construction](../science/encoding-and-precision.md) computes exact rational kernels in logarithmic-size blocks, chooses fixed-excitation sectors and compiles block unitaries. It achieves rate one with polynomial endpoint cost for $`r=o(\log N)`$, including fixed rank, under its declared coefficient and gate model. General $`r=o(N)`$ retains the existence theorem. Standard gate synthesis is inherited. Endpoint approximation and a wrong physical coupling matrix have separate error bounds.

## 5. Foundations, proofs and dependencies

| Role | Authoritative route |
|---|---|
| Selected educational foundation | Lidar v3, the sections and equations listed above. |
| Physical assumptions and reference-sensitive storage guarantee | [Model](../science/model.md). |
| Local counting proof, stationary-sector cost and redundancy law | [Rank law](../science/rank-law.md). |
| Finite-input algorithm, circuit cost and precision accounting | [Encoding and precision](../science/encoding-and-precision.md). |
| Earlier rank-one counts, multimode comparisons, local-algebra ingredients and synthesis sources | [Related work](../references/related-work.md), [source register](../references/source-register.md) and [bibliography](../references/bibliography.bib). |
| Bounded computational evidence | [Verification](../verification/README.md); finite calculations complement the analytical proofs. |

The anchor explains why a protected encoding is a meaningful quantum memory. The local proofs establish how large that encoding must be for arbitrary supplied lowering profiles, and what endpoint implementation is actually paid for.
