# Encoding, circuit cost and coefficient precision

[Scientific overview](README.md) · [Model](model.md) · [Rank law](rank-law.md)

The high-rate theorem is an existence statement for every sublinear spatial interaction rank. A direct compiler is efficient in a smaller regime: fixed rank, or more generally $`r=o(\log N)`$. Its input is the actual coupling matrix, specified exactly by rational numbers. The distinction between this input model and experimental calibration is essential.

## 1. Endpoint compilation theorem

Fix a constant $`c>0`$, take $`N`$ large enough that $`1\le b=\lfloor c\log_2N\rfloor\le N`$, and put $`m=\lfloor N/b\rfloor`$. The real and imaginary parts of every entry of the supplied matrix $`G\in\mathbb Q(i)^{r\times N}`$ have numerators and positive denominators with at most $`B`$ binary digits. Zero entries are allowed. Exact rank decisions use these rational data.

Partition $`mb`$ emitters into $`m`$ blocks of size $`b`$. Initialize the fewer than $`b`$ unused emitters in their ground state. There are block encoders and inverse decoders storing $`k`$ logical qubits, with

```math
k\ge N-b-m\left[\log_2\binom{b+r}{r}+\log_2(b+1)+1\right].
\tag{E1}
```

The lower bound can be replaced by zero whenever its right side is negative. Every block code has a definite excitation number. The ideal logical channel is therefore the identity for every storage time in the [vacuum model](model.md), without a clock-dependent phase correction.

For any requested endpoint error $`0<\epsilon<1`$, the classical preprocessing and circuit-description size are polynomial in

```math
N,\quad r,\quad B,\quad \log(1/\epsilon).
\tag{E2}
```

Here $`c`$ is fixed and the endpoint gate model is CNOT gates between arbitrary pairs within one block, together with single-qubit rotations. A conservative elementary-gate bound per encoder or decoder is

```math
Q=O\!\left(mb^3 4^b\right)
 =O\!\left(N^{1+2c}(\log N)^2\right).
\tag{E3}
```

This bound uses generic unitary synthesis; it is deliberately not optimized. Replacing the one-qubit rotations by a fixed inverse-closed universal gate library gives $`O(Q\,\operatorname{polylog}(Q/\epsilon))`$ gates. All numerical precision and single-qubit approximation costs are paid in (E2) and this latter gate count. No state-preparation oracle or QRAM is supplied.

The implemented logical channel obeys

```math
\sup_{t\ge0}\frac12\left\|
\widetilde{\mathcal R}\circ\Phi_t\circ\widetilde{\mathcal E}
-\mathrm{id}_{2^k}\right\|_\diamond\le\epsilon.
\tag{E4}
```

The supremum concerns endpoint synthesis error under the **exact supplied dynamics**. It is not a uniform-in-time tolerance to a wrong coupling matrix.

If $`r=o(\log N)`$, (E1) gives $`k=N-o(N)`$. For larger ranks $`r=o(N)`$, the global [rank theorem](rank-law.md) still guarantees rate one, but this block compiler does not prove a polynomial endpoint implementation of that global code.

## 2. Block construction and stored dimension

Write the restricted lowering operator on block $`\nu`$ as

```math
L_{a,\nu}=\sum_{j\in\nu}G_{aj}\sigma_j^-,
\qquad
K_\nu=\bigcap_{a=1}^{r}\ker L_{a,\nu}.
\tag{E5}
```

The block's actual row rank can be below $`r`$; using $`r`$ only weakens the following bound. The finite rank theorem gives

```math
\dim K_\nu\ge\frac{2^b}{\binom{b+r}{r}}.
\tag{E6}
```

Every lowering operator decreases excitation number by one, so $`K_\nu`$ is a direct sum of its $`b+1`$ excitation sectors. Some sector has dark dimension

```math
d_\nu\ge\frac{2^b}{(b+1)\binom{b+r}{r}}.
\tag{E7}
```

Compute all sector kernels, select a largest one, and retain any $`2^{k_\nu}`$ orthonormal columns, where $`k_\nu=\lfloor\log_2 d_\nu\rfloor`$. Their span is the block code. Its input consists of $`k_\nu`$ unknown qubits and $`b-k_\nu`$ initialized physical qubits. Those initialized qubits are included in the $`N`$-emitter count.

For the global code $`\bigotimes_\nu K_\nu^{\mathrm{code}}`$, every restricted $`L_{a,\nu}`$ annihilates its own block, hence every global $`L_a=\sum_\nu L_{a,\nu}`$ annihilates the entire code. This argument assumes no independence between the bath noise on different blocks. All blocks can interact with the same reservoir.

Summing $`k_\nu\ge b-\log_2\binom{b+r}{r}-\log_2(b+1)-1`$ proves (E1). For $`r=o(b)`$,

```math
\frac1b\log_2\binom{b+r}{r}
\le\frac rb\log_2\frac{e(b+r)}r\longrightarrow0.
\tag{E8}
```

The lost leftover emitters and the fixed-excitation overhead also have vanishing density. Thus logarithmic blocks achieve rate one throughout $`r=o(\log N)`$.

## 3. Exact classical linear algebra

In excitation sector $`s`$, build the stacked rational matrix

```math
A_{\nu,s}:\mathcal H_{b,s}\longrightarrow
\bigoplus_{a=1}^{r}\mathcal H_{b,s-1},
\qquad
\psi\longmapsto(L_{1,\nu}\psi,\ldots,L_{r,\nu}\psi).
\tag{E9}
```

Its column count is at most $`D=2^b`$ and its row count at most $`rD`$. Each nonzero entry is one supplied coefficient. The matrix is formed explicitly, rather than queried through an oracle. Computing its nullspace over $`\mathbb Q(i)`$ gives exact membership and exact sector dimension.

To see why small singular values do not create an uncharged precision promise, clear the at most $`2rb`$ coefficient denominators in one block. This gives integer real and imaginary parts of bit length

```math
H=O(rbB).
\tag{E10}
```

Fraction-free elimination is polynomial in the matrix dimensions and $`H`$. More explicitly, after selecting a nonsingular pivot minor of order at most $`D`$, Cramer's rule constructs an integer Gaussian-rational nullspace basis using pivot determinants and cofactors. Hadamard's inequality bounds the bit length of its entries by

```math
C=O\!\left(D(H+\log D)\right).
\tag{E11}
```

Multiplying a basis column by its nonzero common denominator changes no subspace. Consequently a full-column-rank integer basis $`Z`$ can be chosen with entries of the size in (E11). Enlarge $`C`$ by one if necessary so that the bound means $`|Z_{ij}|\le2^C`$ also for complex Gaussian-integer entries.

The Gram matrix $`Z^\dagger Z`$ has a positive integer determinant, so that determinant is at least one. Its largest eigenvalue is at most $`D^2 2^{2C}`$. If $`d`$ is the number of columns, then

```math
\lambda_{\min}(Z^\dagger Z)
\ge\left(D^2 2^{2C}\right)^{-(d-1)}.
\tag{E12}
```

Thus the number of precision bits needed to resolve this chosen basis's conditioning is polynomial in $`D,H`$. It can be large as a function of $`b`$, but $`D=2^b\le N^c`$ is polynomial in the declared compiler regime. No lower bound on an experimentally unknown spectral gap is being assumed.

Apply exact rational Gram–Schmidt to independent columns before taking the positive square roots of their rational squared norms. Append independent computational-basis vectors and apply the same procedure to complete an orthonormal basis of the whole block. The resulting full unitary $`U_\nu`$ maps the logical input with its initialized qubits into the selected dark sector. Gram determinants and (E12) give polynomial bounds on the intermediate rational bit lengths. Evaluating the square roots and the subsequent rotations to any requested accuracy therefore costs polynomial bit operations in $`D,r,bB`$ and the output precision.

This is an exact-input algorithm. Near linear dependence can change the exact kernel dimension discontinuously when coefficients are perturbed. Finite noisy samples of the coefficients do not supply the exact rational matrix or its rank for free.

## 4. From block matrices to circuits

Complete each code isometry to the full $`b`$-qubit unitary $`U_\nu`$ described above. A generic elimination uses at most $`O(D^2)`$ two-level unitaries. Gray-code reduction and multi-controlled one-qubit decompositions implement a two-level unitary with a conservative $`O(b^3)`$ CNOT and one-qubit count, without extra persistent qubits. This gives (E3). More economical generic decompositions are available; the polynomial claim does not depend on using them.

These synthesis ingredients are inherited. See Barenco et al., [*Elementary gates for quantum computation*](https://arxiv.org/abs/quant-ph/9503016), especially §§7–8, and Shende, Bullock and Markov, [*Synthesis of quantum-logic circuits*](https://arxiv.org/abs/quant-ph/0406176v5). For conversion to a fixed finite universal gate set, the constructive Solovay–Kitaev algorithm of Dawson and Nielsen, [arXiv:quant-ph/0505030v2](https://arxiv.org/abs/quant-ph/0505030v2), supplies the stated polylogarithmic overhead. The memory theorem contributes the small blocks and their rate; it does not introduce a new generic synthesis algorithm.

All required numerical quantities are computed to enough bits to certify

```math
\|\widetilde U_\nu-U_\nu\|_\infty\le\frac{\epsilon}{2m}.
\tag{E13}
```

This certification need not resolve the angle of a nearly zero pivot pair. Here is an explicit thresholded implementation. Put $`\delta=\epsilon/(2m)`$ and choose $`\eta=\delta/(100D^2)`$. In two-level QR elimination, maintain certified absolute enclosures for the working matrix. Skip a pair only when its norm is at most $`2\eta`$, and normalize a pair only when its norm is at least $`\eta`$. Enclosures finer than $`\eta/10`$ leave an overlap in which either decision is allowed. A normalized rotation can be chosen from dyadic approximations to the pair; its exact two-by-two matrix is then obtained by normalizing those dyadic data. Its residual on the actual pair is bounded by the absolute input-enclosure error. Thus no division by an arbitrarily small, unresolved number is required.

For clarity, consider first exact rotations with these thresholds. At the end of the elimination of one column, each skipped entry below the diagonal has magnitude at most $`2\eta`$. Later rotations act unitarily on trailing rows and preserve that earlier column's tail norm. Hence the resulting unitary $`V`$ satisfies $`\|\operatorname{lower}(V)\|_F\le2D\eta`$. Since $`(|V_{ij}|^2)_{ij}`$ is doubly stochastic,

```math
\sum_{i<j}(j-i)|V_{ij}|^2
=\sum_{i>j}(i-j)|V_{ij}|^2.
\tag{E13a}
```

Its strictly upper-triangular squared norm is therefore at most $`D`$ times its strictly lower-triangular squared norm. Replacing each diagonal element by its unit-modulus phase now changes $`V`$ by at most $`4D^{3/2}\eta`$ in Frobenius norm. The chosen $`\eta`$ makes this smaller than $`\delta/20`$. These diagonal elements are bounded away from zero at this tolerance, so their phases require no small-denominator assumption.

The same estimate permits absolute residuals of order $`\eta`$ in the non-skipped eliminations. There are at most $`D^2`$ two-level steps; allocate smaller polynomial fractions of $`\eta`$ to arithmetic enclosures and of $`\delta`$ to rotation approximation. Products of certified matrices can be enclosed with polynomially many precision bits. Every normalization divides by at least $`\eta`$, so its additional precision cost is $`O(\log(1/\eta))`$ plus polynomial factors in the number of steps. Together with §3, this is polynomial in $`D,r,bB,\log(m/\epsilon)`$. A gate-by-gate telescoping sum then certifies (E13).

At the one-qubit stage, accuracy is a matrix-norm requirement. Euler angles need not vary continuously at a zero entry: threshold such entries and charge the resulting matrix residual, or provide the target single-qubit matrix directly to finite-library approximation. Exact CNOTs and single-qubit gates with the certified matrix accuracies implement the continuous-gate version; finite-library approximation allocates the same budget among the one-qubit gates. Thresholding changes no gate-count order in (E3).

The encoder uses the product of these block circuits. The decoder uses their inverses and discards the initialized redundancy qubits after decoding. There is no measurement record or auxiliary quantum carrier retained during storage. The endpoint gate model permits arbitrary within-block connectivity. Imposing a line adds routing cost bounded by a polynomial in $`b`$, preserving the polynomial-in-$`N`$ conclusion.

## 5. Why endpoint error does not accumulate with storage time

Let $`\mathcal E,\mathcal R`$ denote the ideal block encoder and decoder, and $`\widetilde{\mathcal E},\widetilde{\mathcal R}`$ their implemented versions. For unitary channels, half-diamond distance is at most the operator-norm distance of suitably phased implementing unitaries. Tensor-product telescoping and (E13) therefore give

```math
\frac12\|\widetilde{\mathcal E}-\mathcal E\|_\diamond
\le\frac\epsilon2,
\qquad
\frac12\|\widetilde{\mathcal R}-\mathcal R\|_\diamond
\le\frac\epsilon2.
\tag{E14}
```

Initialization, restriction to the logical subspace and final partial trace cannot increase these complete-channel distances. In the exact vacuum model, $`\mathcal R\Phi_t\mathcal E=\mathrm{id}`$ for every $`t`$. The triangle inequality and contractivity under CPTP pre- and post-composition give

```math
\begin{aligned}
\frac12\|\widetilde{\mathcal R}\Phi_t\widetilde{\mathcal E}
 -\mathrm{id}\|_\diamond
&\le\frac12\|\widetilde{\mathcal R}-\mathcal R\|_\diamond
 +\frac12\|\widetilde{\mathcal E}-\mathcal E\|_\diamond\\
&\le\epsilon.
\end{aligned}
\tag{E15}
```

This argument permits fully correlated bath dynamics across the blocks and protects logical inputs entangled with a reference. A small bright component introduced by an imperfect encoder may subsequently decay; it cannot amplify the initial complete-channel distance from the ideal encoded state.

## 6. Wrong coefficients are a different error source

For a declared Markov counterpart, absorb all decay-rate factors into the rows $`\widehat g_a`$ and write the nominal generator as $`\widehat{\mathcal L}=\sum_a\mathcal D[\widehat L_a]`$, with $`\widehat L_a=\sum_j\widehat G_{aj}\sigma_j^-`$. Suppose the actual rows are $`\widehat g_a+\delta g_a`$, so the jump change is $`E_a=\sum_j\delta G_{aj}\sigma_j^-`$.

For $`\mathcal D[L](X)=LXL^\dagger-\{L^\dagger L,X\}/2`$, expansion into cross terms gives

```math
\|\mathcal D[L+E]-\mathcal D[L]\|_\diamond
\le4\|L\|_\infty\|E\|_\infty+2\|E\|_\infty^2.
\tag{E16}
```

Using $`\|\sum_jv_j\sigma_j^-\|_\infty\le\sqrt N\|v\|_2`$ and Duhamel's formula for two CPTP semigroups gives the sufficient bound

```math
\frac12\|\Phi_t-\widehat\Phi_t\|_\diamond
\le tN\sum_a\left(
2\|\widehat g_a\|_2\|\delta g_a\|_2+\|\delta g_a\|_2^2
\right).
\tag{E17}
```

The right side may be capped at one. A separate Hamiltonian mismatch adds $`t\|\delta H\|_\infty`$ in units $`\hbar=1`$. Combining (E15) with (E17) adds this storage error to the endpoint budget. Equation (E17) is a sufficient, generally nonoptimal bound; it does not assume independent noise across emitters or blocks.

For a finite-mode rotating-wave Hamiltonian, the corresponding general statement is the bounded-perturbation Duhamel estimate $`\tfrac12\|\Phi_t-\widehat\Phi_t\|_\diamond\le t\|H-\widehat H\|_\infty`$ on the invariant total-excitation sector used by the device. It applies when that sector's perturbation norm is finite. The Markov jump formula above is not silently substituted for an arbitrary microscopic reservoir.

Consequently the time-uniform promise in (E4) does not follow from a fixed experimental calibration tolerance. To claim a chosen storage duration, one must supply a corresponding coefficient or Hamiltonian error bound, or prove additional robustness. Calibration cost, thermal photons, independent local noise and noisy endpoint fault tolerance are not established here.

## 7. Finite verification scope

The [finite checks](../verification/README.md) test the exact-kernel mechanism and a small matrix-level encoder. Such calculations check dimensions, annihilation, unitary completion and stated finite-time identities. They do not validate the asymptotic compiler bit-complexity theorem by sampling instances, and they do not implement the generic CNOT/one-qubit synthesis routine or an experimental calibration procedure.
