# Learning the dark-memory argument

[Repository overview](../README.md) · [Scientific account](../science/README.md) · [30-milestone map](milestones.md) · [Source bridge](anchor-and-bridge.md)

Start with the [four-emitter stored qubit](../science/examples.md). Two different radiation patterns impose two amplitude-sum constraints. The displayed orthonormal codewords satisfy both, so every unknown superposition is dark. This gives a concrete object to keep in view while studying the general model and dimension theorem.

The selected educational anchor is **Daniel A. Lidar, _Review of Decoherence Free Subspaces, Noiseless Subsystems, and Dynamical Decoupling_, arXiv:1208.5791v3, 24 October 2013**. The [versioned PDF](https://arxiv.org/pdf/1208.5791v3) supplies the DFS language; the [source bridge](anchor-and-bridge.md) identifies exact sections, translates notation and separates its assumptions from the vacuum-conditioned memory proved here.

## An example-first reading route

1. **See the stored information.** Read [Examples, Sections 1–2](../science/examples.md#1-encode-an-arbitrary-qubit). Follow the cancellation of both profiles and the common phase of the one-excitation codewords.
2. **Understand protection.** Read the anchor's II.B–D alongside [the bridge](anchor-and-bridge.md#2-exact-reading-locations-in-the-anchor), then [the storage model](../science/model.md). Separate emitter-side darkness, reservoir vacuum and Hamiltonian invariance.
3. **Count the available codewords.** Read [the nilpotent injection proof](../science/rank-law.md#1-a-finite-common-kernel-theorem), the stationary-sector corollary and the worst-profile construction. Use the anchor's IV.E to connect code dimension to logical rate while keeping its collective-noise example distinct.
4. **Account for implementation.** Read [encoding and precision](../science/encoding-and-precision.md), then [the verification guide](../verification/README.md). Distinguish a supplied exact coefficient matrix, synthesis accuracy and experimental calibration.
5. **Place the claim in context.** Read [limitations](../science/limitations.md) and [related work](../references/related-work.md). The anchor's V.A explains noiseless subsystems, a broader code class than the common-kernel subspaces optimized here.

## The milestone map

The [30 milestones](milestones.md) organize the full route through the physical setup, linear-algebra mechanism, asymptotic resource law, endpoint construction and evidence limits. Each milestone's scientific references and dependencies connect back to the authoritative topic pages. The [source bridge](anchor-and-bridge.md#5-foundations-proofs-and-dependencies) distinguishes anchor foundations, local proofs and inherited research ingredients.

The central distinction throughout is between a general DFS criterion and a quantitative code-size guarantee. Initial vacuum and the supplied spatial span make the physical memory possible; commuting nilpotent constraints give the profile-dependent dimension bound. Polynomial endpoint compilation has its own exact-input and rank assumptions.
