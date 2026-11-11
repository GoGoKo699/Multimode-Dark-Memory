# Physical and computational scope

The resource law concerns exact passive dark codes under supplied lowering profiles. Its strength is uniformity in those profiles and in the number and memory of reservoir oscillators. Its assumptions identify which physical perturbations require additional analysis.

| Requirement | Why it matters |
|---|---|
| Reservoir initially in vacuum | The reverse interaction annihilates that state. A thermal photon can activate a raising process. |
| Rotating-wave coupling | Counterrotating creation of both matter and field excitations need not vanish on a dark code. |
| Common emitter frequency, or another code-preserving system Hamiltonian | Generic frequency disorder or exchange can move the state out of the common kernel. |
| Every actual spatial profile lies in the supplied span | A new independent loss direction adds a constraint. Raw oscillator count alone is not the relevant rank. |
| Known coefficient data for code construction | Encoding depends on the actual kernel. Exact rational input is a mathematical input model, not a free experimental calibration procedure. |
| Ideal boundary operations, with paid synthesis accuracy | Compilation error can be bounded uniformly in time around an exact code. Physical noise during those operations is a separate problem. |

## What is optimized

The [matching-order bound](rank-law.md) optimizes the dimension of the common dark-kernel code over coupling profiles. It does not optimize all passive memory encodings, noiseless subsystems, transient recoveries or reservoir-assisted protocols. A particular channel may preserve information beyond the common kernel. The project does not assert that its kernel code is optimal for every profile.

The code is a vacuum-conditioned passive quantum memory. It is not a Hamiltonian decoherence-free subspace for every initial bath state. This distinction is part of established DFS theory; the [source comparison](../references/related-work.md) credits it explicitly.

## Endpoint precision and calibration are different resources

When the exact coupling matrix is supplied, one can compile an approximation to a chosen exact dark encoder. Contractivity then prevents its initial encoding error from growing beyond the complete-channel comparison bound during ideal storage. This does not mean that an error in the *physical coupling matrix* is harmless for arbitrary time. Such an error changes the dynamics throughout the interval and generally produces a time-dependent bound. See [encoding and precision](encoding-and-precision.md).

For fixed rank, or $`r=o(\log N)`$, the block construction has polynomial endpoint cost in the stated finite-input model. The general $`r=o(N)`$ information-theoretic theorem does not by itself provide an efficient global encoder, an efficient calibration procedure or a robust hardware threshold.

## Spatial radiation and ordinary free space

Generic extended free-space ensembles have a full-rank radiative kernel and coherent Green-function exchange. They are not automatically examples of exact finite spatial rank. Spherical-harmonic truncation can supply an approximate low-rank dissipator, but using it for storage requires a separate bound on the residual generator and a compatible coherent Hamiltonian. The validity of any Markov or instantaneous-propagation asymptotic must also be justified.

Those conditional spatial extensions are not needed for the full vacuum cavity theorem. No unconditional free-space, finite-temperature or independent-local-noise protection is claimed here.
