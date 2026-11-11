# The radiative-rank law

[Scientific overview](README.md) · [Storage model](model.md) · [Encoding and precision](encoding-and-precision.md) · [Examples](examples.md)

The [model](model.md) turns a common kernel of collective lowering operators into an exact vacuum quantum memory. This page bounds its dimension for every supplied profile matrix and determines the order of the worst-profile redundancy. The result concerns common-kernel dark codes; it does not optimize unrestricted passive quantum capacity.

All logarithms on this page are base two.

## 1. A finite common-kernel theorem

Let $`G\in\mathbb C^{r\times N}`$ have row rank $`r`$, and set

```math
L_a=\sum_{j=1}^{N}G_{aj}\sigma_j^-,
\qquad
\mathcal K_G=\bigcap_{a=1}^{r}\ker L_a.
```

**Theorem 1.** For every $`N\ge1`$ and $`0\le r\le N`$,

```math
\dim\mathcal K_G
\ge
\left\lceil
\frac{2^N}{\binom{N+r}{r}}
\right\rceil.
```

The all-ground state always belongs to $`\mathcal K_G`$. The displayed bound may reduce to this trivial dimension in a large-rank finite instance; it is not asserted to be the exact finite-size minimum.

The proof uses only commutation and a bound on the degree of a nonzero lowering monomial. It is an elementary nilpotent-module dimension argument. The contribution is its uniform physical resource consequence for arbitrary profiles and growing interaction rank, rather than a new general algebraic framework.

### Proof

Lowering operators on distinct sites commute, and each satisfies $`(\sigma_j^-)^2=0`$. Therefore

```math
[L_a,L_b]=0,
\qquad
L_1^{\alpha_1}\cdots L_r^{\alpha_r}=0
\quad\text{if }|\alpha|:=\sum_a\alpha_a>N.
```

Let $`P_G`$ be the orthogonal projector onto $`\mathcal K_G`$. Define

```math
T:\mathbb C^{2^N}
\longrightarrow
\bigoplus_{\substack{\alpha\in\mathbb N_0^r\\|\alpha|\le N}}
\mathcal K_G,
\qquad
T|\psi\rangle
=\bigl(P_GL^\alpha|\psi\rangle\bigr)_\alpha,
```

where $`L^\alpha=L_1^{\alpha_1}\cdots L_r^{\alpha_r}`$ and the zero-degree monomial is the identity.

This map is injective. Given nonzero $`|\psi\rangle`$, choose a multi-index $`\alpha`$ of maximal total degree for which $`L^\alpha|\psi\rangle\ne0`$. Such an index exists because the identity monomial is nonzero on $`|\psi\rangle`$, and its degree is at most $`N`$. For every $`a`$,

```math
L_aL^\alpha|\psi\rangle=0,
```

by commutation and maximality. Thus $`L^\alpha|\psi\rangle\in\mathcal K_G`$, so its component survives $`P_G`$. At least one component of $`T|\psi\rangle`$ is nonzero.

There are $`\binom{N+r}{r}`$ multi-indices of degree at most $`N`$. Comparing source and target dimensions yields

```math
2^N\le\binom{N+r}{r}\dim\mathcal K_G.
```

Taking the integer ceiling proves the theorem. For $`r=0`$, the map is the identity and equality holds. $`\square`$

The injection is a dimension proof. Constructing all of its components is not the proposed storage algorithm and is not assumed to be efficient.

## 2. Logical qubits and the sublinear-rank regime

An isometry into any $`2^q`$-dimensional subspace of $`\mathcal K_G`$ stores $`q`$ ordinary logical qubits, with the reference guarantee in [the model](model.md#4-logical-input-reference-and-recovery). Consequently

```math
q_G:=\left\lfloor\log\dim\mathcal K_G\right\rfloor
\ge
\max\left\{0,
\left\lfloor N-\log\binom{N+r}{r}\right\rfloor
\right\}.
```

For $`r\ge1`$ the standard binomial bound gives

```math
\log\binom{N+r}{r}
\le
r\log\left(\frac{e(N+r)}{r}\right).
```

If $`r=r_N=o(N)`$, the right side is $`o(N)`$. Indeed, with $`x_N=r_N/N\to0`$, its ratio to $`N`$ is at most $`x_N\log(e(1+x_N)/x_N)\to0`$. Therefore every supplied sequence of such profiles admits

```math
q_G=N-o(N).
```

This conclusion holds uniformly over the profile coefficients. It imposes no favorable distribution on their values. It does not assert that the common kernel occupies a fraction tending to one of Hilbert space: a subspace of dimension $`2^{N-o(N)}`$ can still be a vanishing fraction of $`2^N`$. The statement is about asymptotic logical-qubit rate.

## 3. A stationary code

Let $`\mathcal H_k`$ be the $`k`$-excitation sector. Since $`L_a\mathcal H_k\subseteq\mathcal H_{k-1}`$, different excitation components cannot cancel in $`L_a|\psi\rangle`$. Hence

```math
\mathcal K_G
=\bigoplus_{k=0}^{N}\mathcal K_{G,k},
\qquad
\mathcal K_{G,k}:=\mathcal K_G\cap\mathcal H_k.
```

At least one sector $`k_*`$ satisfies

```math
\dim\mathcal K_{G,k_*}
\ge\frac{\dim\mathcal K_G}{N+1}
\ge\frac{2^N}{(N+1)\binom{N+r}{r}}.
```

**Corollary 2.** A stationary dark code exists with

```math
q_G^{\mathrm{stat}}
\ge
\max\left\{0,
\left\lfloor
N-\log\binom{N+r}{r}-\log(N+1)
\right\rfloor
\right\}.
```

Its evolution under the common emitter Hamiltonian is one global phase. The same decoder therefore works for every storage duration. For every $`r=o(N)`$, it still stores $`N-o(N)`$ logical qubits. The extra $`\log(N+1)`$ is a proved upper bound on the cost of selecting one sector, not a sharp sector-by-sector formula.

## 4. What one collective mode already supplies

For the homogeneous single lowering mode

```math
J^-_b=\sum_{j=1}^{b}\sigma_j^-,
```

the established Dicke/angular-momentum count is

```math
\dim\ker J_b^-
=\binom{b}{\lfloor b/2\rfloor}.
```

A short reconstruction fixes the count used below. The $`b`$ spin-$`1/2`$ representation decomposes into spin-$`J=b/2-k`$ multiplets with multiplicities

```math
m_{b,k}=\binom{b}{k}-\binom{b}{k-1},
\qquad 0\le k\le\lfloor b/2\rfloor,
```

where $`\binom b{-1}=0`$. Each multiplet has exactly one lowest-weight vector annihilated by $`J_b^-`$. Summing multiplicities telescopes to the central binomial coefficient.

The same total dimension holds for one inhomogeneous lowering mode with every coefficient nonzero. If

```math
L_g=\sum_{j=1}^{b}g_j\sigma_j^-,
\qquad
D_g=\bigotimes_{j=1}^{b}
\begin{pmatrix}1&0\\0&g_j^{-1}\end{pmatrix},
```

then $`L_g=D_gJ_b^-D_g^{-1}`$. Similarity preserves nullity. This similarity is generally nonunitary and is not, by itself, a physical encoder. Zero coefficients leave additional uncoupled emitters.

The one-mode count, its disorder invariance, and standard decoherence-free storage are inherited results; see [the related-work account](../references/related-work.md). Theorem 1 is deliberately a coarser bound at $`r=1`$. Its value is uniform control of multiple arbitrary profiles and growing $`r`$.

## 5. Worst-profile dark-code redundancy

Define the smallest common dark dimension at a prescribed profile rank and its redundancy by

```math
K_{\min}(N,r)
=\min_{\substack{G\in\mathbb C^{r\times N}\\\operatorname{rank}G=r}}
\dim\mathcal K_G,
\qquad
\Delta(N,r)=N-\log K_{\min}(N,r).
```

The minimum exists because the possible dimensions form a nonempty finite set of integers. This is an optimization over common-kernel dark codes. A noiseless subsystem, a special finite-duration recovery, or a different control model is not covered by this definition. Replacing logarithmic dimension by the integer logical-qubit count changes redundancy by less than one bit.

### A universal finite upper bound

Theorem 1 and $`\dim\mathcal K_G\ge1`$ give

```math
\Delta(N,r)
\le\min\left\{N,\log\binom{N+r}{r}\right\}.
```

### A finite converse construction

For $`1\le r\le N`$, partition the emitters into $`r`$ nonempty groups of sizes $`b_1,\ldots,b_r`$, differing by at most one, with $`\sum_a b_a=N`$. Give group $`a`$ its own uniform collective-lowering profile and set that profile to zero outside the group. These rows have disjoint supports and rank $`r`$. Their common kernel factorizes, so the inherited one-mode formula yields

```math
\dim\mathcal K_G
=\prod_{a=1}^{r}\binom{b_a}{\lfloor b_a/2\rfloor}.
```

This admissible matrix proves the finite lower bound

```math
\Delta(N,r)
\ge
N-\sum_{a=1}^{r}
\log\binom{b_a}{\lfloor b_a/2\rfloor}.
```

The bound requires no assertion that this matrix is the exact minimizer.

### Matching asymptotic order

The central-binomial estimate

```math
\log\binom{b}{\lfloor b/2\rfloor}
=b-\frac12\log b+O(1)
```

has a constant uniform for integer $`b\ge1`$. Since the balanced group sizes are $`N/r+O(1)`$, it follows, when $`N/r\to\infty`$, that

```math
\frac r2\log\left(\frac Nr\right)-O(r)
\le\Delta(N,r)
\le r\log\left(\frac{e(N+r)}r\right).
```

**Theorem 3.** In the regime $`1\le r=o(N)`$,

```math
\Delta(N,r)
=\Theta\!\left(r\log\frac Nr\right).
```

The multiplicative order is matched; the leading constant is not. The statement is compatible with the sharper known coefficient at one mode. It identifies how worst-profile dark-code redundancy grows with radiative rank, without claiming an exact finite-rank minimum.

## 6. Why sublinear rank is the uniform rate-one threshold

Sublinear rank is sufficient by Theorem 1. To see the appropriate necessity, choose $`r`$ profiles that lower $`r`$ individual emitters independently. Every one of those emitters must be in its ground state in the common kernel, while the other $`N-r`$ emitters are free. Thus

```math
\dim\mathcal K_G=2^{N-r}.
```

If $`r_N/N`$ is bounded away from zero on a subsequence, these allowed profiles remove a nonzero logical rate on that subsequence. Therefore a rate tending to one **uniformly over all supplied rank-$`r_N`$ profiles** is possible if and only if $`r_N=o(N)`$.

This is a uniform guarantee. It does not say that every extensive-rank ensemble has the same dark dimension, or that sublinear rank is necessary for every individual favorable ensemble. At $`r=N`$, an invertible profile matrix spans all individual lowering operators, and the common kernel is exactly the one-dimensional all-ground space. At $`r=0`$, all $`N`$ qubits are unaffected.

## 7. Consequence for the physical memory

Combining this page with [vacuum invariance](model.md#3-exact-vacuum-invariance) gives an exact, arbitrarily long storage guarantee for arbitrary reference-entangled quantum inputs. Sublinear spatial interaction rank leaves asymptotically all emitter qubits available, even when no permutation symmetry relates their coupling coefficients. The number of reservoir modes and their memory time do not enter this dimension bound.

This separates a useful count from an implementation claim. The general theorem supplies code existence. A [block compiler](encoding-and-precision.md) provides polynomial endpoints for fixed rank and a specified slowly growing-rank regime. Neither result protects against physical errors outside the stated vacuum profile model.

The finite checks in [the verification guide](../verification/README.md) reconstruct exact common kernels for small supplied profiles and test the one-mode, disjoint-group, and independent-loss cases. Those checks support the finite mechanism; the proofs here establish the general dimension and scaling statements.
