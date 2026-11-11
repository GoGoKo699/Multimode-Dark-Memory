# A qubit dark to two different radiation profiles

Consider four emitters and two coupling rows

```math
G=\begin{pmatrix}1&1&1&1\\1&2&3&4\end{pmatrix},\qquad
L_1=\sum_{j=1}^4\sigma_j^-,\quad
L_2=\sum_{j=1}^4 j\sigma_j^-.
```

Write $`|j\rangle`$ for the state with only emitter $`j`$ excited. Both jumps map the one-excitation sector to the same vacuum vector. An amplitude vector is dark precisely when its ordinary and weighted sums vanish.

## 1. Encode an arbitrary qubit

Two orthonormal codewords are

```math
|0_L\rangle=\frac{|1\rangle-2|2\rangle+|3\rangle}{\sqrt6},\qquad
|1_L\rangle=\frac{2|1\rangle-|2\rangle-4|3\rangle+3|4\rangle}{\sqrt{30}}.
```

For the first word the two sums are $`1-2+1=0`$ and $`1-4+3=0`$. For the second they are $`2-1-4+3=0`$ and $`2-2-12+12=0`$. Their unnormalized inner product is $`2+2-4=0`$. Therefore both $`L_1`$ and $`L_2`$ annihilate every superposition

```math
\alpha|0_L\rangle+\beta|1_L\rangle.
```

Linearity protects correlations with an inaccessible logical reference too. No measurement learns $`\alpha`$ or $`\beta`$, and no emitted photon carries that logical information in the stated vacuum model.

## 2. Couple to a reservoir and wait

Let any collection of reservoir oscillators couple through time-dependent combinations of these same two profiles, as in the [model](model.md). The term creating a reservoir excitation multiplies a jump that annihilates the code; the reverse term annihilates the reservoir vacuum. The interaction therefore vanishes on the encoded state tensor vacuum.

Both words have one excitation. The common emitter Hamiltonian contributes only the same global phase $`e^{-i\omega t}`$ to both. The logical state is stationary for every storage duration. Encoding and decoding occur at the boundaries.

This small example illustrates simultaneous cancellation of different profiles. It is not used to infer the large-system theorem. The four-emitter rank bound is deliberately conservative and need not certify this exact two-dimensional sector by itself.

## 3. Finite spaces checked exactly

The verification program computes common kernels in every excitation sector by exact integer linear algebra. Selected outcomes are:

| Emitters | Profiles | Sector dimensions from vacuum upward | Total dark dimension |
|---|---|---|---|
| 4 | One row $`(1,2,3,4)`$ | $`1,3,2,0,0`$ | 6 |
| 6 | One row $`(1,2,3,4,5,6)`$ | $`1,5,9,5,0,0,0`$ | 20 |
| 8 | Independent loss on every emitter | $`1,0,0,0,0,0,0,0,0`$ | 1 |
| 8 | Separate collective loss on two groups of four | Product of the two group decompositions | 36 |

The full [finite output](../verification/results/dark_rank_checks.json) also lists arbitrary two- and three-profile integer matrices. Its exact nullspaces satisfy the original lowering constraints. Floating orthonormalization is a separate residual check, not the basis of the dimension count.

## 4. Why disjoint groups bound the worst case

If $`r`$ independent profiles each act on a different group of about $`N/r`$ emitters, their dark spaces tensor together. The inherited one-mode count in a group of size $`b`$ is $`\binom{b}{\lfloor b/2\rfloor}`$. The product loses about $`\tfrac r2\log_2(N/r)`$ qubits. This supplies the matching-order example in the [rank law](rank-law.md), while the universal bound protects every allowed profile matrix.

The matching statement concerns an order of redundancy. It does not establish a sharp leading constant or a generic-profile exact formula.
