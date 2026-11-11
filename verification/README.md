# Verification and reproduction

The general results are established by the [analytical proofs](../science/rank-law.md) and the [compiler argument](../science/encoding-and-precision.md). These programs test finite instances and load-bearing conventions. Passing them is not a proof of asymptotic scaling, novelty or hardware feasibility.

## Run the checks

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_dark_rank.py
python verification/compile_toy.py
python verification/check_vacuum.py
```

Each command accepts `--output PATH`. Defaults are files in the ignored `build/` directory, so ordinary reproduction does not overwrite the included [recorded results](results/). Dependencies and versions actually used are recorded in those JSON files; small floating differences across versions are expected.

| Program | What it actually checks | Expected result |
|---|---|---|
| `check_dark_rank.py` | Eleven listed integer-profile instances with $`N\le8`$: exact sector nullspaces, exact annihilation, independent floating orthonormalization, known one-mode count, independent loss and disjoint-group example. | `all listed finite exact-rational checks passed` |
| `compile_toy.py` | The four-emitter example's code and full unitary completion; exact code under a declared Markov generator at five times; endpoint overrotation and coefficient perturbations against analytical upper bounds. | `all bounded checks passed` |
| `check_vacuum.py` | Four emitters with two explicitly retained truncated cavity oscillators, complex coupling coefficients and bath-mode mixing. Checks that the joint code-vacuum isometry evolves by one common phase and the bath stays vacuum at five times. | `all full-vacuum checks passed` |

## Evidence conventions

Kernel dimensions are obtained by exact integer linear algebra. Floating SVD/QR residuals check a numerically orthonormalized representation of those spaces separately. The many-emitter capacity statement is not extrapolated from these small cases.

The toy encoder uses the two rows $`(1,1,1,1)`$ and $`(1,2,3,4)`$ from [the worked example](../science/examples.md). Its channel diagnostics use a normalized maximally entangled input and report a **normalized-Choi half-trace distance**. This is not a numerical diamond norm. The displayed half-diamond upper bounds are analytical consequences of endpoint operator error or the declared generator perturbation bound. No diamond SDP is executed.

The full vacuum script retains its field variables and therefore does not use a master-equation approximation. Each oscillator is truncated to levels zero and one for the bounded calculation. The exact dark-state interaction already vanishes before truncation, as proved in the model; the finite check does not establish convergence of a general truncated-bath simulation or simulate a continuum.

The generic block compiler is proved with explicit finite-input and gate-model assumptions. The small matrix-level unitary completion is not an implementation of its generic CNOT/one-qubit synthesis algorithm or an asymptotic complexity benchmark.

## Recorded outputs and source changes

- [Exact finite rank checks](results/dark_rank_checks.json).
- [Toy endpoint and calibration checks](results/compile_toy_results.json).
- [Full vacuum Hamiltonian checks](results/vacuum_results.json).

After changing a scientific claim, matrix convention or verification program, rerun the affected commands and reconcile the explanation with their actual outputs. Current repository verification is performed by these local commands; no GitHub Actions requirement is configured in this initial scientific integration.
