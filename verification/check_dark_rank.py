#!/usr/bin/env python3
"""Bounded exact-rational checks of collective-lowering dark-space rank laws.

All common-kernel dimensions are obtained from exact integer nullspaces sector
by sector, and each nullspace basis is checked against the original matrices.
Float orthonormalization only supplies a separate physical DFS residual.
"""

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import scipy
import sympy as sp
from scipy.linalg import qr
from sympy.polys.matrices import DomainMatrix


def sector_matrix(g, n, k):
    inputs = list(itertools.combinations(range(n), k))
    outputs = list(itertools.combinations(range(n), k - 1)) if k else []
    lookup = {x: i for i, x in enumerate(outputs)}
    a = sp.zeros(len(g) * len(outputs), len(inputs))
    for col, excited in enumerate(inputs):
        for i, site in enumerate(excited):
            lowered = excited[:i] + excited[i + 1 :]
            for mode, row in enumerate(g):
                a[mode * len(outputs) + lookup[lowered], col] = int(row[site])
    return a, inputs


def full_jump(row):
    n = len(row)
    a = np.zeros((2**n, 2**n))
    for col in range(2**n):
        for i, value in enumerate(row):
            if col & (1 << i):
                a[col ^ (1 << i), col] = value
    return a


def check_instance(g, label):
    n = len(g[0])
    r = int(sp.Matrix(g).rank())
    sector_dims = []
    columns = []
    exact_residuals = []
    for k in range(n + 1):
        a, basis = sector_matrix(g, n, k)
        if k == 0:
            kernel = sp.ones(1, 1)
        else:
            kernel = DomainMatrix.from_Matrix(a).nullspace().to_Matrix().T
        residue = a * kernel
        exact_zero = all(x == 0 for x in residue)
        assert exact_zero
        exact_residuals.append(exact_zero)
        sector_dims.append(kernel.cols)
        if kernel.cols:
            numeric = np.array(kernel.tolist(), dtype=float)
            numeric /= np.maximum(np.linalg.norm(numeric, axis=0), 1e-300)
            q, _ = qr(numeric, mode="economic")
            for j in range(q.shape[1]):
                column = np.zeros(2**n)
                for i, configuration in enumerate(basis):
                    column[sum(1 << bit for bit in configuration)] = q[i, j]
                columns.append(column)
    q = np.stack(columns, axis=1)
    residuals = [float(np.linalg.norm(full_jump(row) @ q)) for row in g]
    dim_k = sum(sector_dims)
    lower = 2**n / math.comb(n + r, r)
    assert dim_k + 1e-12 >= lower
    if r == 1 and all(g[0]):
        assert dim_k == math.comb(n, n // 2)
    return {
        "label": label,
        "n": n,
        "rank_r": r,
        "G_integer_rows": [[int(x) for x in row] for row in g],
        "common_kernel_sector_dimensions": sector_dims,
        "common_kernel_total_dimension": dim_k,
        "binomial_lower_bound": lower,
        "logical_qubits_floor_log2_dimension": int(math.floor(math.log2(dim_k))),
        "dark_code_redundancy_bits": n - math.log2(dim_k),
        "exact_annihilation_all_sectors": all(exact_residuals),
        "orthonormal_basis_frobenius_residual": float(np.linalg.norm(q.T @ q - np.eye(dim_k))),
        "floating_annihilation_frobenius_residuals": residuals,
    }


def run():
    generator = np.random.default_rng(20261111)
    cases = []
    for n in (4, 6, 8):
        cases.append(([[j + 1 for j in range(n)]], f"inhomogeneous_single_mode_n{n}"))
        for r in (2, 3):
            while True:
                g = generator.integers(-3, 4, size=(r, n)).tolist()
                if sp.Matrix(g).rank() == r:
                    break
            cases.append((g, f"integer_profiles_n{n}_r{r}"))
    cases.append((np.eye(8, dtype=int).tolist(), "independent_loss_full_rank"))
    cases.append(([[1] * 4 + [0] * 4, [0] * 4 + [1] * 4], "two_disjoint_dicke_blocks"))
    output = {
        "scope": "Exact finite integer-matrix checks for listed n<=8 profiles only. The general rank law is analytical, not inferred from numerics.",
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__, "sympy": sp.__version__},
        "instances": [check_instance(g, label) for g, label in cases],
    }
    full_rank = output["instances"][-2]
    assert full_rank["common_kernel_total_dimension"] == 1
    disjoint = output["instances"][-1]
    assert disjoint["common_kernel_total_dimension"] == math.comb(4, 2) ** 2
    output["status"] = "all listed finite exact-rational checks passed"
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("build/dark_rank_checks.json"))
    args = parser.parse_args()
    output = run()
    destination = args.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "instances": len(output["instances"]), "output": str(destination)}))
