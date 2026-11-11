#!/usr/bin/env python3
"""Finite full-Hamiltonian check of the stated vacuum-conditioned code.

Two truncated cavity modes, including mode mixing and complex couplings, are
retained explicitly. The code annihilates the interaction before truncation;
the check does not infer continuum reservoir dynamics from a finite cutoff.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm


def lower(row):
    out = np.zeros((16, 16), dtype=complex)
    for col in range(16):
        for j, value in enumerate(row):
            if col & (1 << j):
                out[col ^ (1 << j), col] = value
    return out


def run():
    g = np.array([[1, 1, 1, 1], [1, 2, 3, 4]], dtype=complex)
    vectors = np.array([[1, 2], [-2, -1], [1, -4], [0, 3]], dtype=complex)
    code = np.zeros((16, 2), dtype=complex)
    code[[1, 2, 4, 8]] = vectors / np.sqrt([6, 30])
    jumps = [lower(row) for row in g]
    a = np.array([[0, 1], [0, 0]], dtype=complex)
    bath_a = [np.kron(a, np.eye(2)), np.kron(np.eye(2), a)]
    vacuum = np.array([1, 0, 0, 0], dtype=complex)
    omega = 0.71
    h_a = np.diag([omega * x.bit_count() for x in range(16)])
    h_b = 1.17 * bath_a[0].conj().T @ bath_a[0]
    h_b += 1.93 * bath_a[1].conj().T @ bath_a[1]
    h_b += 0.13j * (bath_a[0].conj().T @ bath_a[1] - bath_a[1].conj().T @ bath_a[0])
    eta = np.array([[0.3 + 0.2j, -0.17j], [-0.21 + 0.1j, 0.19]], dtype=complex)
    h_int = np.zeros((64, 64), dtype=complex)
    for mu in range(2):
        for index in range(2):
            term = eta[mu, index] * np.kron(jumps[index], bath_a[mu].conj().T)
            h_int += term + term.conj().T
    h = np.kron(h_a, np.eye(4)) + np.kron(np.eye(16), h_b) + h_int
    encoded_vacuum = np.kron(code, vacuum[:, None])
    annihilation = float(np.linalg.norm(h_int @ encoded_vacuum))
    observations = []
    for time in [0.0, 0.03, 0.4, 2.0, 10.0]:
        actual = expm(-1j * time * h) @ encoded_vacuum
        ideal = np.exp(-1j * time * omega) * encoded_vacuum
        residual = float(np.linalg.norm(actual - ideal, 2))
        # Isometry operator error bounds half-diamond error, including references.
        assert residual < 3e-12
        bath_excitation = float(np.linalg.norm(actual.reshape(16, 4, 2)[:, 1:, :]))
        assert bath_excitation < 3e-12
        observations.append({"time": time, "joint_isometry_operator_error": residual,
                             "bath_nonvacuum_amplitude_frobenius": bath_excitation})
    assert annihilation < 1e-12
    return {"scope": "Four emitters and two explicitly retained two-level-truncated cavity oscillators; one fixed-excitation logical qubit. Finite identity check only; no bath elimination, diamond SDP or continuum simulation.",
            "versions": {"numpy": np.__version__, "scipy": scipy.__version__},
            "joint_dimension": 64, "interaction_on_encoded_vacuum_frobenius": annihilation,
            "observations": observations, "status": "all full-vacuum checks passed"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("build/vacuum_results.json"))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "output": str(args.output)}))
