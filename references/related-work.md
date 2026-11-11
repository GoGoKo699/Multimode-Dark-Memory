# Relation to collective-decay codes and dark-state memories

The result studied here is a guarantee for an entire unknown quantum register. For $`N`$ two-level systems with $`r`$ independent coupling profiles,

```math
L_a=\sum_{i=1}^{N}g_{ai}\sigma_i^-,\qquad
\mathcal K=\bigcap_{a=1}^{r}\ker L_a,
```

the common dark space obeys

```math
\dim\mathcal K\geq\frac{2^N}{\binom{N+r}{r}}.
```

Consequently, every family with $`r=o(N)`$ admits $`N-o(N)`$ logical qubits. The profiles can be inhomogeneous and need no permutation symmetry. The physical statement uses excitation-conserving coupling to vacuum bosonic modes, together with a system Hamiltonian that preserves the code. It concerns passive storage after encoding; it does not supply an optical write/read interface or protection against additional local noise.

Bibliographic identities, versions and precise reading locations are recorded in the [source register](source-register.md).

## What is inherited

Decoherence-free subspaces and their Hamiltonian invariance conditions are established tools for preserving quantum information [LW03]. The common-kernel condition is a sufficient special case of that theory for a purely lowering Lindblad dissipator. Coupling a null space to a vacuum cavity also has a substantial history. Halati, Jin and Moessner [HJM26] develop a general hybrid-system construction using one matter operator coupled to a lossy bosonic mode, with representation theory furnishing large and structured null spaces. These mechanisms provide the setting for the present dimension estimate.

Asymptotic rate one is already known for a single collective lowering operator. Duan and Guo [DG98] obtain

```math
\dim\ker\!\left(\sum_i\sigma_i^-\right)
=\binom{N}{\lfloor N/2\rfloor},
```

which costs only about $`\tfrac12\log_2 N`$ redundant physical qubits. Theerthagiri, Narayanan and Ganesh [TNG25] show that the sector dimensions remain unchanged for arbitrary nonzero couplings in one inhomogeneous Tavis–Cummings profile. High-rate storage and rank-one coupling-disorder independence must therefore be credited to earlier work.

The mathematical dimension argument is also standard in origin. Let

```math
A=\mathbb C[z_1,\ldots,z_r]/(z_1,\ldots,z_r)^{N+1}
```

act on the qubit Hilbert space through $`z_a\mapsto L_a`$. The common kernel is the module's socle. Finite local-algebra duality gives the usual bound

```math
\dim M\leq(\dim A)\dim\operatorname{soc}M.
```

Oudompheng [Oud09], especially Proposition 9 and Theorem 10, gives an accessible account of the duality and injective-hull ingredients. The repository provides an elementary finite-dimensional proof. Its use here is an application of that module bound, rather than a new result in local algebra.

## The multimode distinction

| Scientific claim | Earlier result and scope | Scope of the present result |
|---|---|---|
| High-rate dark encoding | [DG98] gives the exact uniform rank-one dimension; [TNG25] extends its counting to arbitrary nonzero rank-one couplings. | A uniform guarantee for every rank-$`r`$ profile matrix, including growing $`r=o(N)`$. |
| Several cavity profiles | Emary [Emary13] treats an arbitrary multimode coupling matrix by singular-value decomposition in a model restricted to at most one excitation. | An exponentially large code in the full qubit Hilbert space; the argument retains spin saturation. |
| Several collective decay channels | Lee et al. [Lee26] exploit partial permutation symmetry at commensurate spacings, organizing qubits into collective spins. | The dimension guarantee requires only commuting lowering operators and their joint nilpotency, with arbitrary profiles. |
| Large null spaces in hybrid systems | [HJM26] constructs structured examples from a single collective root-vector operator and representation theory. | A simultaneous-kernel bound for multiple independent inhomogeneous profiles, expressed as a worst-case redundancy law. |
| Coupling disorder in optical memories | Hanamura et al. [Han26] map a single-resonator ensemble to bright and dark bosonic modes near its ground or inverted state. | Exact register storage without a Holstein–Primakoff approximation, with a rank-dependent capacity guarantee. |
| Photon-storage fidelity | Asenjo-Garcia et al. [AG17] use ordered-array subradiance and selective radiance to improve the light–matter interface. | A passive code-space size theorem; interface efficiency is a separate question. |

The order of the universal redundancy is sharp: disjoint ordinary Dicke groups provide profile matrices whose redundancy grows as $`r\log(N/r)`$, up to constant factors in the subextensive-rank regime. Logarithmic-size blocks also turn the existence argument into polynomial-size endpoint constructions for the stated low-rank regimes. These are the quantitative capabilities at issue here; the existence of dark states alone is established physics.

Hanamura et al. merit a particularly precise distinction. Their v4 explicitly uses small deviations from a fully polarized reference state, and Appendix H states the applicability conditions. The continuum of dark modes in that effective waveguide is not a collection of independent cavity coupling profiles. Their echo-silencing and retrieval protocols address an optical-memory problem complementary to the full-Hilbert-space register bound.

## Connection to squares of linear forms

There is a second standard algebraic description. Identify the computational basis with squarefree monomials in

```math
B=\mathbb C[x_1,\ldots,x_N]/(x_1^2,\ldots,x_N^2).
```

The adjoints $`L_a^\dagger`$ act as multiplication by linear forms $`\ell_a=\sum_i\overline{g_{ai}}x_i`$. Orthogonal complementation of their combined image gives

```math
\dim\mathcal K=\dim B/(\ell_1,\ldots,\ell_r).
```

Eliminating $`r`$ independent linear forms leaves a quotient of a polynomial ring in $`N-r`$ variables by the squares of $`N`$ linear forms. This connects exact dark-state counting to the classical Hilbert-series problem for powers of linear forms. Boij and Lundqvist [BL26] determine the generic case of $`n+2`$ powers in $`n`$ variables; with power two, it supplies exact generic rank-two counting through this identification. Moreover, each excitation-sector constraint matrix has polynomial entries in the profiles, so its rank is maximal on a nonempty Zariski-open set. Generic nullities are therefore the minimum sector dimensions: when the specialization's hypotheses apply, the generic rank-two formula also yields sharper all-profile lower bounds there. The present elementary estimate is coarser in that case. Its scope is the arbitrary and growing-rank resource law and its physical implementation; no new exact generic Hilbert series or sharper rank-two optimum is asserted.

## Hamiltonians and physical scope

A bath-state-independent Hamiltonian DFS and a code protected for an initially vacuum bath have different requirements. Lidar and Whaley [LW03], Section 5.6, explicitly explain the distinction between lowering Lindblad operators and the Hermitian interaction containing both lowering and raising terms. Here the raising term is harmless because its bath annihilation operator kills the vacuum. The vacuum assumption is therefore part of the theorem, rather than an inference from a bath-independent DFS criterion.

A dark space for the dissipative part need not be invariant under an additional exchange Hamiltonian. Brooke, Patra and Cresser [BPC08] analyze precisely this leakage mechanism; [Lee26] also identifies the symmetry-breaking effect of coherent waveguide evolution. The full vacuum-cavity model used here avoids elimination-induced ambiguity by checking invariance before eliminating the bosons. This does not justify replacing a generic free-space electromagnetic environment by a few decay modes while discarding its coherent interactions.

The comparison covers the source versions and passages listed below. It supports the specific arbitrary-profile rank–redundancy statement, while keeping established dark-state mechanisms, rank-one codes, optical-memory interfaces and standard algebraic ingredients explicitly attributed.
