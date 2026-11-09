"""Compare a fresh full run with the checked-in synthetic-study outputs.

This checks numerical reproducibility, not empirical or methodological validity.
Run simulation_v2.py into a separate directory before invoking this script.
Strict CSV mismatches are recorded before exiting with status 1; they are not
silently relaxed or replaced by a successful structural check.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare_csv(old_path: Path, new_path: Path) -> dict:
    old, new = pd.read_csv(old_path), pd.read_csv(new_path)
    error = None
    try:
        pd.testing.assert_frame_equal(old, new, check_exact=False, rtol=1e-8, atol=1e-10)
    except AssertionError as exc:
        error = str(exc).splitlines()[0]
    failures, maximum = [], 0.0
    if old.shape == new.shape and list(old.columns) == list(new.columns):
        for column in old.select_dtypes(include="number").columns:
            a, b = old[column].to_numpy(), new[column].to_numpy()
            delta = np.abs(a - b)
            finite = delta[np.isfinite(delta)]
            if finite.size:
                maximum = max(maximum, float(finite.max()))
            bad = np.flatnonzero(~np.isclose(b, a, rtol=1e-8, atol=1e-10, equal_nan=True))
            if bad.size:
                examples = []
                for i in bad[:3]:
                    keys = {k: old.iloc[i][k] for k in
                            ("scenario", "cases_per_period", "audit_share", "estimator")
                            if k in old.columns}
                    keys = {k: v.item() if isinstance(v, np.generic) else v
                            for k, v in keys.items()}
                    examples.append({
                        "row_index": int(i), "row_keys": keys,
                        "reference": float(a[i]), "rerun": float(b[i]),
                        "absolute_difference": float(delta[i]),
                        "allowed_absolute_difference": float(1e-10 + 1e-8 * abs(a[i])),
                    })
                failures.append({"column": column, "cells_outside_tolerance": int(bad.size),
                                 "maximum_absolute_difference": float(delta[bad].max()),
                                 "examples": examples})
    return {
        "file": old_path.name, "rows": len(new),
        "matches_within_tolerance": error is None, "comparison_error": error,
        "maximum_absolute_numeric_difference": maximum,
        "numeric_failures": failures,
        "reference_sha256": sha256(old_path), "rerun_sha256": sha256(new_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rerun-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    try:
        reference_commit = subprocess.run(
            ["git", "-C", str(base), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        reference_commit = None
    reference = base / "outputs"
    fresh = args.rerun_dir.resolve()
    if fresh == reference.resolve():
        raise ValueError("Use a separate output directory; do not overwrite the reference.")

    comparisons = []
    for old_path in sorted(reference.glob("*.csv")):
        new_path = fresh / old_path.name
        comparisons.append(compare_csv(old_path, new_path))
    if not comparisons:
        raise AssertionError("No reference CSVs found.")

    old_manifest = json.loads((reference / "run_manifest.json").read_text())
    new_manifest = json.loads((fresh / "run_manifest.json").read_text())
    assert old_manifest["config"] == new_manifest["config"]
    for key in ("accepted_equivalence_paths", "monte_carlo_rows", "all_fits_converged",
                "maximum_boundary_rate"):
        assert old_manifest[key] == new_manifest[key], key
    for key, expected in old_manifest["checks"].items():
        actual = new_manifest["checks"][key]
        if isinstance(expected, bool):
            assert actual == expected, key
        else:
            np.testing.assert_allclose(actual, expected, rtol=1e-8, atol=1e-10)

    mc = pd.read_csv(fresh / "monte_carlo_replications.csv")
    config = new_manifest["config"]
    expected_cells = 6 * len(config["sample_sizes"]) * len(config["audit_shares"])
    assert len(mc) == expected_cells * config["monte_carlo_replications"]
    assert len(mc) == new_manifest["monte_carlo_rows"]
    cell_counts = mc.groupby(["scenario", "cases_per_period", "audit_share"]).size()
    assert len(cell_counts) == expected_cells
    assert cell_counts.eq(config["monte_carlo_replications"]).all()
    assert not mc.duplicated(["scenario", "cases_per_period", "audit_share", "replication"]).any()
    for bundle in ("audit_override", "audit_proxy"):
        assert mc[f"{bundle}_converged"].all()
        for parameter in ("p", "e"):
            estimate = mc[f"delta_{parameter}_{bundle}_hat"].to_numpy()
            se = mc[f"delta_{parameter}_{bundle}_se"].to_numpy()
            assert np.isfinite(estimate).all()
            assert np.isfinite(se).all() and (se > 0).all()

    figures = []
    for old_path in sorted(reference.glob("figure_*.png")):
        new_path = fresh / old_path.name
        assert new_path.is_file() and new_path.stat().st_size > 0
        figures.append({"file": old_path.name,
                        "same_file_hash": sha256(old_path) == sha256(new_path)})
    assert len(figures) == 6

    csv_passed = all(c["matches_within_tolerance"] for c in comparisons)
    result = ("All numerical comparisons and replication integrity checks passed."
              if csv_passed else
              "Replication integrity checks passed; strict CSV comparison failed. "
              "See per-file diagnostics; original tolerances are unchanged.")
    report = {
        "scope": "Full default synthetic run compared with checked-in outputs; no human data.",
        "reference_repository_commit": reference_commit,
        "simulation_sha256": sha256(base / "simulation_v2.py"),
        "verification_script_sha256": sha256(Path(__file__)),
        "numeric_tolerance": {"relative": 1e-8, "absolute": 1e-10},
        "config": config,
        "software_versions": new_manifest["software_versions"],
        "replication_rows": len(mc),
        "fitted_models": len(mc) * 2,
        "design_cells": expected_cells,
        "accepted_equivalence_paths": new_manifest["accepted_equivalence_paths"],
        "all_fits_converged": new_manifest["all_fits_converged"],
        "maximum_boundary_rate": new_manifest["maximum_boundary_rate"],
        "csv_comparisons": comparisons,
        "csv_comparison_passed": csv_passed,
        "replication_integrity_passed": True,
        "regenerated_figures": figures,
        "replication_data_sha256": sha256(fresh / "monte_carlo_replications.csv"),
        "result": result,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"csv_files": len(comparisons), "rows": len(mc),
                      "fits": len(mc) * 2, "result": report["result"]}))
    if not csv_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
