# Thirty milestones for multimode dark memory

[Learning overview](README.md) · [Scientific overview](../science/README.md) · [Worked memory](../science/examples.md)

The educational anchor is Daniel A. Lidar, [*Review of Decoherence Free Subspaces, Noiseless Subsystems, and Dynamical Decoupling*, arXiv:1208.5791v3](https://arxiv.org/abs/1208.5791v3), dated 24 October 2013. Section and equation pointers below refer to that version. The review supplies the language of protected quantum information and the symmetric collective-noise baseline. The arbitrary-profile dimension argument, its redundancy law, and the stated compilation and precision account are supplied by this project's scientific pages.

The map allocates **ten milestones to background and preliminaries** and **twenty to the narrative and contribution**. The first phase joins local emitters, quantum channels, code spaces, and Hamiltonian invariance into the operational model. The second begins with a complete stored-qubit example, builds the rank argument into a global resource law, and then follows the information through a paid encoder, storage interval, and recovery. Its final milestones reconcile precision, evidence, attribution, and physical scope.

These are common understanding targets. Specialist proofs and calculations remain in their canonical scientific sources.

## Background and preliminaries

### M01 — The quantum information that must survive

- **Central question:** What distinguishes storing an unknown qubit from preserving an excitation or a classical label?
- **Understanding target:** Explain why a memory must preserve arbitrary amplitudes and relative phases, and why emitter populations alone cannot establish quantum storage.
- **Dependencies and story role:** Entry point; identifies the physical task before introducing a protection mechanism.
- **Conceptual connection:** Relates the review's definition of decoherence-free evolution to the project's requirement to return the entire logical quantum state.
- **Source pointers:** Lidar II, Definition 1 and Eq. (2); [model 4, logical input and recovery](../science/model.md#4-logical-input-reference-and-recovery).

### M02 — Reduced dynamics and an inaccessible reference

- **Central question:** How can the environment damage information even though the joint evolution is unitary?
- **Understanding target:** Explain partial trace and reduced quantum channels, and distinguish preservation of isolated inputs from preservation of correlations with a reference.
- **Dependencies and story role:** Builds on M01; supplies the operational meaning of the later identity-channel guarantee.
- **Conceptual connection:** Connects the Kraus description to a unitary emitter–reservoir model without treating the reservoir as another accessible memory carrier.
- **Source pointers:** Lidar II, Eqs. (1)–(2), and II.C, Eqs. (11)–(14); [model 4](../science/model.md#4-logical-input-reference-and-recovery).

### M03 — A lowering operator and the reservoir vacuum

- **Central question:** Which two factors can make an emission or absorption term vanish?
- **Understanding target:** Use the project convention $`\sigma^- = |0\rangle\langle1|`$ to explain lowering, excitation number, and bosonic vacuum annihilation.
- **Dependencies and story role:** Adds the local physical operations needed after M01–M02.
- **Conceptual connection:** Relates the emission and absorption terms in the review to the two separate cancellations used by the vacuum memory.
- **Source pointers:** Lidar IV, the interaction in Eq. (66) and the discussion following Eqs. (68); [model 1–2](../science/model.md). The project's explicit operator definition fixes its normalization.

### M04 — A code is a space of superpositions

- **Central question:** Why does annihilating every codeword protect every logical superposition?
- **Understanding target:** Distinguish a protected vector, a multi-dimensional code space, and a coherent logical register; explain why one common global phase is harmless.
- **Dependencies and story role:** Combines the storage task in M01 with the local action in M03.
- **Conceptual connection:** Uses the review's two-qubit collective-dephasing example to introduce the linear-space reasoning later applied to simultaneous lowering constraints.
- **Source pointers:** Lidar II.B, Eqs. (7)–(9); [worked example 1](../science/examples.md#1-encode-an-arbitrary-qubit); [model 4](../science/model.md#4-logical-input-reference-and-recovery).

### M05 — Dimension, logical qubits, and encoding rate

- **Central question:** What does a dark space of dimension $`D`$ buy as a quantum memory?
- **Understanding target:** Translate dimension into $`\lfloor\log_2D\rfloor`$ ordinary logical qubits, distinguish that count from a qudit description, and interpret rate as logical qubits per physical emitter.
- **Dependencies and story role:** Gives M04 a quantitative information measure before any asymptotic claim.
- **Conceptual connection:** Connects combinatorial code-space counts to operational memory size and makes integer rounding explicit.
- **Source pointers:** Lidar III.B, Eqs. (58)–(61); [rank law 2](../science/rank-law.md#2-logical-qubits-and-the-sublinear-rank-regime).

### M06 — Collective coupling, profile span, and oscillator count

- **Central question:** When do many reservoir oscillators impose only a few independent emitter constraints?
- **Understanding target:** Read a coupling matrix as a list of spatial profiles; distinguish its row span and rank from its number of rows, the number of bath modes, and permutation symmetry.
- **Dependencies and story role:** Extends the local interaction in M03 to an ensemble while retaining the information count from M05.
- **Conceptual connection:** The review's identical-coupling factorization is a familiar special case. The project replaces that symmetry promise with a supplied profile span.
- **Source pointers:** Lidar III.A, Eqs. (47)–(50), and IV, Eqs. (69)–(70); [model 1–2](../science/model.md).

### M07 — Invariance under the whole Hamiltonian

- **Central question:** Why can a state dark to the interaction still fail as a memory?
- **Understanding target:** Separate an instantaneous annihilation condition from an invariant code. Identify the roles of initialization, the system Hamiltonian, and the environment's initial state.
- **Dependencies and story role:** Integrates M02, M04, and M06 into a dynamical protection criterion.
- **Conceptual connection:** Connects the review's Hamiltonian DFS conditions to the project's direct check of the code tensor vacuum.
- **Source pointers:** Lidar II.D, hypotheses (18)–(20) and factorization (21)–(26); [model 3, Proposition 1](../science/model.md#3-exact-vacuum-invariance).

### M08 — A dark subspace is not every noiseless subsystem

- **Central question:** Which protection class is actually being counted?
- **Understanding target:** Distinguish a common-kernel subspace from a noiseless subsystem with a gauge factor, and identify the adjoint-closure assumption in the review's algebra decomposition.
- **Dependencies and story role:** Uses M04 and M07 to fix the class of encodings before optimizing their dimension.
- **Conceptual connection:** Prevents a vacuum-conditioned lowering code from being silently promoted to a bath-state-independent Hamiltonian DFS or an unrestricted passive-capacity optimum.
- **Source pointers:** Lidar V.A, Theorem 2 and Eqs. (99)–(101); [limitations, “What is optimized”](../science/limitations.md#what-is-optimized); [related work, “Hamiltonians and physical scope”](../references/related-work.md#hamiltonians-and-physical-scope).

### M09 — The one-mode baseline and its different counts

- **Central question:** What is already supplied by ordinary collective-spin dark states?
- **Understanding target:** Explain lowest-weight states and the inherited central-binomial dimension for one lowering mode. Distinguish it from the review's singlet DFS for simultaneous collective raising, lowering, and dephasing.
- **Dependencies and story role:** Joins the rate calculation in M05 to the protection-class distinction in M08.
- **Conceptual connection:** Angular-momentum multiplicities supply the baseline and later converse example, while their different annihilation requirements explain why the counts differ.
- **Source pointers:** Lidar IV.B–E, especially Eqs. (78), (86)–(90); [rank law 4](../science/rank-law.md#4-what-one-collective-mode-already-supplies); [related work, “What is inherited”](../references/related-work.md#what-is-inherited).

### M10 — Assemble the operational memory model

- **Central question:** What must be specified before a dark-state dimension becomes a storage theorem?
- **Understanding target:** State the complete input, supplied profiles, vacuum rotating-wave interaction, common emitter frequency or code-preserving Hamiltonian, endpoint operations, inaccessible reference, and quantum output.
- **Dependencies and story role:** Synthesizes M01–M09; closes the preliminary phase with a single consistent model.
- **Conceptual connection:** Combines the review's DFS framework with the explicit vacuum premise and resource boundary required by this project.
- **Source pointers:** Lidar II.D and V.A for the framework and its boundary; [model 1–6](../science/model.md); [limitations](../science/limitations.md).

## Narrative and contribution

### M11 — Encode one qubit against two profiles

- **Central question:** Can two different spatial radiation patterns share a useful quantum code?
- **Understanding target:** Interpret the four-emitter codewords as amplitude vectors whose ordinary and weighted sums both vanish; check normalization and mutual orthogonality before assigning a logical qubit.
- **Dependencies and story role:** Starts the new narrative locally, using M03–M06 in one complete physical register.
- **Conceptual connection:** Simultaneous destructive interference replaces the need for identical emitter couplings in this example.
- **Source pointers:** [Worked example 1](../science/examples.md#1-encode-an-arbitrary-qubit); [model 1](../science/model.md#1-emitters-and-supplied-coupling-information). Lidar II.B supplies the earlier code-space analogy.

### M12 — Follow the stored qubit through the reservoir

- **Central question:** What happens to an arbitrary encoded state and its reference while the four emitters wait?
- **Understanding target:** Explain both interaction cancellations, the unchanged reservoir vacuum, the common one-excitation phase, and endpoint recovery without learning the unknown amplitudes.
- **Dependencies and story role:** Completes the example begun in M11, from input to quantum output.
- **Conceptual connection:** Turns the invariant-subspace criterion of M07 into an explicit light–matter process, even with many oscillators and bath memory.
- **Source pointers:** [Worked example 2](../science/examples.md#2-couple-to-a-reservoir-and-wait); [model 3–4](../science/model.md); Lidar II.D for the invariance principle, with the project's vacuum-specific cancellation supplied locally.

### M13 — The algebra left by spin saturation

- **Central question:** What common structure remains when every profile coefficient is arbitrary?
- **Understanding target:** Explain why the collective lowering operators commute and why every lowering product of degree greater than $`N`$ vanishes, without replacing the emitters by unsaturated bosonic modes.
- **Dependencies and story role:** Generalizes M11's cancellation mechanism to the local algebra needed for the dimension proof.
- **Conceptual connection:** The two-level constraint gives joint nilpotency even after permutation symmetry has disappeared.
- **Source pointers:** [Rank law 1, proof opening](../science/rank-law.md#1-a-finite-common-kernel-theorem); [model 1](../science/model.md#1-emitters-and-supplied-coupling-information).

### M14 — A maximal lowering monomial reaches the common kernel

- **Central question:** How can an arbitrary nonzero vector witness the existence of a dark component?
- **Understanding target:** Explain why a nonzero lowering monomial of maximal total degree produces a vector annihilated by every profile, and why commutation is essential to that inference.
- **Dependencies and story role:** Uses M13 to identify the decisive step of the proof.
- **Conceptual connection:** A local termination property becomes a simultaneous constraint on all radiation directions.
- **Source pointers:** [Rank law 1, injection proof](../science/rank-law.md#1-a-finite-common-kernel-theorem); [related work, the finite local-algebra interpretation](../references/related-work.md#what-is-inherited). This step is a project-supplied derivation, not a theorem attributed to the educational review.

### M15 — Count the injective map's target

- **Central question:** How does the maximal-monomial argument force a large common dark space?
- **Understanding target:** Explain the projected-monomial map's injectivity, count degree-at-most-$`N`$ multi-indices, and use source-versus-target dimensions to obtain the finite bound.
- **Dependencies and story role:** Combines M14's witness with M05's dimension viewpoint; completes the mathematical mechanism.
- **Conceptual connection:** An elementary nilpotent-module bound becomes a uniform estimate for every supplied coupling matrix.
- **Source pointers:** [Rank law 1, Theorem 1 and proof](../science/rank-law.md#1-a-finite-common-kernel-theorem); [related work, “What is inherited”](../references/related-work.md#what-is-inherited).

### M16 — Interpret the finite lower bound honestly

- **Central question:** What does the theorem certify for a particular finite register?
- **Understanding target:** Convert its rounded-up dimension lower bound to logical-qubit floors, recognize when the bound certifies only the ground state, and distinguish a lower bound from an exact kernel computation.
- **Dependencies and story role:** Applies M15 before taking a large-system limit.
- **Conceptual connection:** Prevents a conservative universal estimate from being confused with the exact dimension of the worked example or a generic-profile formula.
- **Source pointers:** [Rank law 1–2](../science/rank-law.md); [worked example 1 and 3](../science/examples.md); Lidar III.B, Eq. (60), for the dimension-to-qubit translation.

### M17 — Make the memory stationary

- **Central question:** How can a code avoid needing a storage-time phase correction?
- **Understanding target:** Explain the excitation-sector decomposition of the common kernel, the largest-sector argument, and the additional logarithmic dimension cost of a fixed decoder.
- **Dependencies and story role:** Combines the finite count in M16 with the common-frequency dynamics in M07 and M12.
- **Conceptual connection:** A grading of the mathematical kernel becomes a physical choice between known-duration recovery and a stationary code.
- **Source pointers:** [Rank law 3, Corollary 2](../science/rank-law.md#3-a-stationary-code); [model 4](../science/model.md#4-logical-input-reference-and-recovery). Lidar II.B, Eq. (8), provides the global-phase analogy.

### M18 — Take the sublinear-rank limit

- **Central question:** How fast may the number of profiles grow while the logical-qubit rate still approaches one?
- **Understanding target:** Use the binomial logarithm bound to explain the regime $`r=o(N)`$, including growing rank; distinguish rate one from a dark space occupying almost all Hilbert-space volume.
- **Dependencies and story role:** Promotes the finite estimate in M16–M17 to a uniform information-theoretic statement.
- **Conceptual connection:** The overhead is governed by independent spatial constraints, rather than a fixed-mode or fixed-symmetry assumption.
- **Source pointers:** [Rank law 2](../science/rank-law.md#2-logical-qubits-and-the-sublinear-rank-regime); Lidar III.B and IV.E for the earlier symmetric rate-one baselines.

### M19 — Build a demanding profile family

- **Central question:** Can allowed profiles force a substantial redundancy cost?
- **Understanding target:** Explain the disjoint-group construction, factorization of its dark space, and use of the inherited one-mode count on each balanced group.
- **Dependencies and story role:** Reuses M09 after the universal guarantee in M18 to build an opposing example.
- **Conceptual connection:** A known one-mode result becomes a many-profile resource obstruction through a physical partition of emitters.
- **Source pointers:** [Rank law 5, finite converse construction](../science/rank-law.md#5-worst-profile-dark-code-redundancy); [worked example 4](../science/examples.md#4-why-disjoint-groups-bound-the-worst-case).

### M20 — Match the order of worst-profile redundancy

- **Central question:** In what precise sense is the rank-dependent overhead unavoidable?
- **Understanding target:** State the minimization over supplied rank-$`r`$ common kernels, combine its upper bound with M19, and distinguish matching order from a sharp constant or unrestricted passive-capacity optimum.
- **Dependencies and story role:** Integrates the universal argument and converse family into the quantitative resource law.
- **Conceptual connection:** Makes the contribution a comparison under one declared code class and parameter regime, with inherited ingredients subtracted.
- **Source pointers:** [Rank law 5, Theorem 3](../science/rank-law.md#5-worst-profile-dark-code-redundancy); [limitations, “What is optimized”](../science/limitations.md#what-is-optimized).

### M21 — Understand the uniform threshold and its endpoints

- **Central question:** Why does extensive profile rank defeat a guarantee that works for every allowed matrix?
- **Understanding target:** Explain the independently lossy-emitter example and the zero-rank and full-rank limits. Distinguish failure of a uniform rate-one guarantee from a claim about every favorable extensive-rank ensemble.
- **Dependencies and story role:** Adds necessity and boundary cases to M18–M20.
- **Conceptual connection:** Checks the resource law against ordinary independent loss and clarifies its quantifiers.
- **Source pointers:** [Rank law 6](../science/rank-law.md#6-why-sublinear-rank-is-the-uniform-rate-one-threshold); [finite examples 3](../science/examples.md#3-finite-spaces-checked-exactly).

### M22 — Turn the count into the full memory theorem

- **Central question:** Which physical guarantee follows when the dimension theorem and vacuum invariance are combined?
- **Understanding target:** Explain exact reference-preserving storage for arbitrary duration, the role of a fixed profile span under time-dependent mode mixing, and why neither a Markov approximation nor repeated bath resets are required.
- **Dependencies and story role:** Synthesizes M12–M21 into the general scientific memory statement before considering its implementation.
- **Conceptual connection:** Joins a uniform finite-dimensional count to an exact microscopic invariant subspace, while keeping vacuum and rotating-wave assumptions visible.
- **Source pointers:** [Model 2–5](../science/model.md); [rank law 7](../science/rank-law.md#7-consequence-for-the-physical-memory); [limitations](../science/limitations.md).

### M23 — Assemble a global code from dark blocks

- **Central question:** Why can small separately encoded blocks remain dark to one shared correlated reservoir?
- **Understanding target:** Explain how every restricted block operator annihilates its block code and how summing those operators annihilates the tensor-product code; account for initialized redundancy and unused ground-state emitters.
- **Dependencies and story role:** Starts the implementation narrative locally after the global existence statement in M22.
- **Conceptual connection:** Tensor closure supplies a construction without assuming statistically independent noise on the blocks.
- **Source pointers:** [Encoding and precision 2, Eqs. (E5)–(E7)](../science/encoding-and-precision.md#2-block-construction-and-stored-dimension); Lidar III.C, discussion following Eqs. (64), for the earlier block-code principle.

### M24 — Pay for the classical kernel calculation

- **Central question:** What finite information must be supplied to compute a block's exact dark sector?
- **Understanding target:** Explain the rational coefficient input, stacked sector matrix, exact rank decision, and bit-length/conditioning bounds; distinguish exact data from noisy calibration samples.
- **Dependencies and story role:** Gives the block prescription in M23 an explicit classical input and computation model.
- **Conceptual connection:** Converts a subspace-existence proof into paid finite linear algebra without a free singular-value gap or preparation oracle.
- **Source pointers:** [Encoding and precision 3, Eqs. (E9)–(E12)](../science/encoding-and-precision.md#3-exact-classical-linear-algebra).

### M25 — Choose logarithmic blocks and retain high rate

- **Central question:** Which rank regime makes the direct block construction both high rate and polynomial?
- **Understanding target:** Explain why exponential work on $`b=\Theta(\log N)`$ emitters is polynomial in $`N`$, track sector, rounding, and leftover losses, and distinguish $`r=o(\log N)`$ compilation from general $`r=o(N)`$ existence.
- **Dependencies and story role:** Combines the dimension bookkeeping in M17–M18 with the paid matrices in M23–M24.
- **Conceptual connection:** Exposes the tradeoff between globally available code dimension and an explicit endpoint construction.
- **Source pointers:** [Encoding and precision 1–2, Eqs. (E1)–(E3) and (E8)](../science/encoding-and-precision.md); [scientific overview, “Two different implementation statements”](../science/README.md#two-different-implementation-statements).

### M26 — Compile a physical encoder and inverse decoder

- **Central question:** How do computed code columns become ordinary quantum gates?
- **Understanding target:** Explain orthonormalization, unitary completion, two-level elimination, and the declared CNOT/one-qubit gate model. Identify the cost of gate accuracy and the absence of a retained helper quantum register.
- **Dependencies and story role:** Turns the matrix construction in M24–M25 into the two boundary circuits of the memory.
- **Conceptual connection:** Uses inherited synthesis tools with explicit sizes; it does not reinterpret a matrix-level toy completion as a generic synthesis benchmark.
- **Source pointers:** [Encoding and precision 4, Eqs. (E3) and (E13)–(E13a)](../science/encoding-and-precision.md#4-from-block-matrices-to-circuits); [verification evidence conventions](../verification/README.md#evidence-conventions).

### M27 — Separate endpoint error from storage duration

- **Central question:** Why can a small implemented-encoder error have a time-uniform bound?
- **Understanding target:** Explain comparison to the exact dark encoder, complete-channel contractivity, and the sum of encoding and decoding error budgets, including reference-entangled inputs.
- **Dependencies and story role:** Adds the accuracy guarantee to the circuits in M26 and the exact memory in M22.
- **Conceptual connection:** Distinguishes the possible decay of a small bright component from amplification of the initial distance to the exact encoded channel.
- **Source pointers:** [Encoding and precision 5, Eqs. (E14)–(E15)](../science/encoding-and-precision.md#5-why-endpoint-error-does-not-accumulate-with-storage-time); [model 4](../science/model.md#4-logical-input-reference-and-recovery).

### M28 — Calibration changes the dynamics

- **Central question:** Why does a wrong physical coupling matrix require a different error bound?
- **Understanding target:** Distinguish gate-synthesis error from generator or Hamiltonian mismatch; interpret the duration-dependent perturbation bounds and identify which additional noise processes remain untreated.
- **Dependencies and story role:** Completes the resource account after M24 and M27 by making its experimental boundary explicit.
- **Conceptual connection:** A time-uniform endpoint guarantee cannot be transferred to an unknown drifting bath or a fixed calibration tolerance.
- **Source pointers:** [Encoding and precision 6, Eqs. (E16)–(E17) and the microscopic Hamiltonian bound](../science/encoding-and-precision.md#6-wrong-coefficients-are-a-different-error-source); [limitations, endpoint precision and calibration](../science/limitations.md#endpoint-precision-and-calibration-are-different-resources).

### M29 — Reconcile proof, finite evidence, and attribution

- **Central question:** Which parts are proved generally, checked finitely, inherited, or outside the claim?
- **Understanding target:** Distinguish exact finite kernel counts, floating residuals, normalized-Choi diagnostics, analytical diamond bounds, generic compiler proofs, and physical assumptions. Identify the standard DFS, one-mode, module-bound, and synthesis ingredients.
- **Dependencies and story role:** Integrates the proof and implementation narratives before their final synthesis.
- **Conceptual connection:** Keeps the arbitrary-profile resource contribution separate from established dark-state physics and from evidence that has a narrower scope.
- **Source pointers:** [Verification guide](../verification/README.md); [related work](../references/related-work.md); [source register](../references/source-register.md); [limitations](../science/limitations.md). Lidar II–V remain the single educational anchor.

### M30 — Tell the complete storage story

- **Central question:** What can this model now guarantee, from a supplied input to a recovered quantum output?
- **Understanding target:** Connect the unknown reference-entangled register, known spatial profiles, chosen code and paid endpoints, untouched storage interval, and inverse recovery. State the arbitrary-sublinear-rank rate law, its dark-code-only converse, the smaller efficient-compilation regime, and the physical precision limits together.
- **Dependencies and story role:** Synthesizes M11–M29 into one end-to-end account; no later milestone is needed to supply a hidden assumption.
- **Conceptual connection:** The number of independent spatial radiation patterns controls a worst-case redundancy law under a vacuum excitation-conserving interaction, while memory size, efficient access, and robustness remain distinct statements.
- **Source pointers:** [Scientific overview](../science/README.md); [model](../science/model.md); [rank law](../science/rank-law.md); [encoding and precision](../science/encoding-and-precision.md); [limitations](../science/limitations.md).
