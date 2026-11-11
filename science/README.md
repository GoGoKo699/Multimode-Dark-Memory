# Dark memory from the number of radiation profiles

An ensemble can be coupled to many reservoir oscillators while exposing only a few independent spatial combinations of its emitters. This account asks how much *unknown quantum information* can remain dark to all those combinations, including at high excitation density and with uneven supplied couplings.

For $`N`$ two-level emitters and $`r`$ independent collective lowering profiles, the common dark space obeys

```math
\dim K_G\geq\frac{2^N}{\binom{N+r}{r}}.
```

The worst-profile dark-code redundancy has order $`r\log(N/r)`$ when $`1\leq r=o(N)`$. Consequently a sublinear profile count permits $`N-o(N)`$ logical qubits. The guarantee is uniform over the supplied complex coupling matrix. It uses no distributional or permutation-symmetry promise.

The code is preserved in a full rotating-wave vacuum light–matter model. It does not require eliminating the reservoir into a Markov equation. Common emitter frequency, vacuum preparation and the supplied coupling-profile span are load-bearing assumptions. The theorem is about dark codes; it does not identify unrestricted passive capacity.

## Read the argument

| Question | Authoritative page |
|---|---|
| What information, dynamics and operations are supplied? | [Model and exact storage interface](model.md) |
| Why are there exponentially many jointly dark states? | [Finite bound, proof and matching-order law](rank-law.md) |
| Can the code be computed and compiled, and what precision is paid? | [Encoding and precision](encoding-and-precision.md) |
| What does a stored qubit look like? | [A four-emitter example and finite counts](examples.md) |
| Which physical changes defeat the argument? | [Scope and limitations](limitations.md) |
| Which ingredients and earlier conclusions are inherited? | [Related work](../references/related-work.md) |
| What has actually been checked computationally? | [Verification](../verification/README.md) |

The proof is short because the lowering constraints commute and are jointly nilpotent. Its physical consequence concerns a many-excitation quantum code, rather than the single-excitation bright/dark normal-mode count. Standard decoherence-free-subspace theory and single-mode counts are inherited; the general profile-count resource law and its endpoint construction are the subject here.

## Two different implementation statements

The information-theoretic bound holds for every sublinear $`r`$. A general global encoder may be expensive. For fixed $`r`$, and more generally $`r=o(\log N)`$, logarithmic-size blocks give a rate approaching one with polynomial classical computation and polynomial circuit size under an exact rational-coefficient input model. The [compiler account](encoding-and-precision.md) separates that statement from experimental calibration and from storage under imperfectly known couplings.

No additional quantum carrier holds part of the input during storage. Temporary workspace is confined to encoding and recovery. A stationary fixed-excitation subcode removes the need to track a logical free-precession phase, at a further cost of at most $`\log_2(N+1)`$ qubits for the global code.
