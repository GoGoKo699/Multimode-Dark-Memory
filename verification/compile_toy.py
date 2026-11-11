#!/usr/bin/env python3
"""Bounded matrix-level endpoint and coefficient-error checks.

This constructs one four-emitter encoder matrix. It does not implement the
generic elementary-gate compiler or certify asymptotic bit complexity. Choi
trace distances are finite-input diagnostics, not diamond-norm evaluations.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import scipy
import sympy as sp
from scipy.linalg import expm, null_space


def jump(row):
    n = len(row)
    out = np.zeros((2**n, 2**n), dtype=complex)
    for column in range(2**n):
        for site, coefficient in enumerate(row):
            if column & (1 << site):
                out[column ^ (1 << site), column] = coefficient
    return out


def generator(rows):
    d = 2 ** len(rows[0])
    identity = np.eye(d)
    result = np.zeros((d * d, d * d), dtype=complex)
    for row in rows:
        a = jump(row)
        norm = a.conj().T @ a
        result += np.kron(a.conj(), a)
        result -= 0.5 * np.kron(identity, norm)
        result -= 0.5 * np.kron(norm.T, identity)
    return result


def trace_redundancy(matrix):
    return np.trace(matrix.reshape(8, 2, 8, 2), axis1=0, axis2=2)


def logical_choi(evolution, encoder):
    encoded = encoder[:, :2]
    result = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            state = np.outer(encoded[:, i], encoded[:, j].conj())
            state = (evolution @ state.reshape(-1, order="F")).reshape(16, 16, order="F")
            decoded = trace_redundancy(encoder.conj().T @ state @ encoder)
            result[2 * i : 2 * i + 2, 2 * j : 2 * j + 2] = decoded / 2
    return result


def half_trace_norm(a):
    return float(np.linalg.svd(a, compute_uv=False).sum() / 2)


def run():
    rows = np.array([[1, 1, 1, 1], [1, 2, 3, 4]], dtype=float)
    integer_vectors = sp.Matrix([[1, 2], [-2, -1], [1, -4], [0, 3]])
    assert sp.Matrix(rows.astype(int)).multiply(integer_vectors) == sp.zeros(2, 2)
    assert integer_vectors.T * integer_vectors == sp.diag(6, 30)
    code = np.zeros((16, 2), dtype=complex)
    code[[1, 2, 4, 8], :] = np.array(integer_vectors, dtype=float) / np.sqrt([6, 30])
    encoder = np.column_stack([code, null_space(code.conj().T)])
    assert np.linalg.norm(encoder.conj().T @ encoder - np.eye(16)) < 1e-12
    annihilation = [float(np.linalg.norm(jump(row) @ code)) for row in rows]
    assert max(annihilation) < 1e-12

    # The overrotation deliberately mixes one code vector with a bright,
    # four-excitation state; the inverse overrotation is used by the decoder.
    bright = np.eye(16, dtype=complex)[:, -1]
    h = np.outer(bright, code[:, 0].conj()) + np.outer(code[:, 0], bright.conj())
    theta = 0.02
    approximate_encoder = expm(-1j * theta * h) @ encoder
    endpoint_distance = float(np.linalg.norm(approximate_encoder - encoder, 2))
    analytic_endpoint_bound = 2 * endpoint_distance
    assert abs(endpoint_distance - 2 * np.sin(theta / 2)) < 1e-12

    # Independent small profile perturbation, in the same declared Markov model.
    delta = np.array([[0.001, -0.002, 0.0, 0.001], [0.0, 0.001, -0.001, 0.0]])
    calibration_slope = 4 * sum(
        2 * np.linalg.norm(row) * np.linalg.norm(change) + np.linalg.norm(change) ** 2
        for row, change in zip(rows, delta)
    )
    ideal_choi_vector = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    ideal_choi = np.outer(ideal_choi_vector, ideal_choi_vector.conj())
    original_generator = generator(rows)
    perturbed_generator = generator(rows + delta)
    observations = []
    for time in [0.0, 0.01, 0.1, 1.0, 10.0]:
        physical = expm(time * original_generator)
        perfect_error = half_trace_norm(logical_choi(physical, encoder) - ideal_choi)
        endpoint_error = half_trace_norm(logical_choi(physical, approximate_encoder) - ideal_choi)
        calibration_error = half_trace_norm(logical_choi(expm(time * perturbed_generator), encoder) - ideal_choi)
        assert perfect_error < 2e-10
        assert endpoint_error <= analytic_endpoint_bound + 2e-10
        assert calibration_error <= min(1.0, time * calibration_slope) + 2e-10
        observations.append({
            "time": time,
            "exact_endpoint_normalized_choi_half_trace_error": perfect_error,
            "approximate_endpoint_normalized_choi_half_trace_error": endpoint_error,
            "endpoint_half_diamond_analytic_upper_bound": analytic_endpoint_bound,
            "perturbed_profile_normalized_choi_half_trace_error": calibration_error,
            "perturbed_profile_half_diamond_analytic_upper_bound": min(1.0, time * calibration_slope),
        })
    return {
        "scope": "One four-emitter two-profile fixed-excitation code; exact rational annihilation, numerical unitary completion and listed finite-time normalized-Choi diagnostics. No diamond SDP or elementary-gate compiler executed.",
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__, "sympy": sp.__version__},
        "coupling_rows": rows.astype(int).tolist(),
        "code_integer_columns": np.array(integer_vectors, dtype=int).tolist(),
        "squared_column_norms": [6, 30],
        "unitary_completion_frobenius_residual": float(np.linalg.norm(encoder.conj().T @ encoder - np.eye(16))),
        "annihilation_frobenius_residuals": annihilation,
        "endpoint_overrotation_radians": theta,
        "endpoint_unitary_operator_distance": endpoint_distance,
        "profile_perturbation": delta.tolist(),
        "calibration_error_slope_bound": float(calibration_slope),
        "observations": observations,
        "status": "all bounded checks passed",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("build/compile_toy_results.json"))
    args = parser.parse_args()
    output = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "output": str(args.output), "times_checked": len(output["observations"])}))
