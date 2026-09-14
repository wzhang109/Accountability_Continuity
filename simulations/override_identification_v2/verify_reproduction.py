"""Compare a fresh full run with the checked-in synthetic-study outputs.

This checks numerical reproducibility, not empirical or methodological validity.
Run simulation_v2.py into a separate directory before invoking this script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rerun-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    reference = base / "outputs"
    fresh = args.rerun_dir.resolve()
    if fresh == reference.resolve():
        raise ValueError("Use a separate output directory; do not overwrite the reference.")

    comparisons = []
    for old_path in sorted(reference.glob("*.csv")):
        new_path = fresh / old_path.name
        old = pd.read_csv(old_path)
        new = pd.read_csv(new_path)
        pd.testing.assert_frame_equal(old, new, check_exact=False, rtol=1e-8, atol=1e-10)
        numeric = old.select_dtypes(include="number").columns
        delta = (old[numeric] - new[numeric]).abs().to_numpy()
        finite_delta = delta[np.isfinite(delta)]
        comparisons.append({
            "file": old_path.name,
            "rows": len(new),
            "matches_within_tolerance": True,
            "maximum_absolute_numeric_difference": (
                float(finite_delta.max()) if finite_delta.size else 0.0
            ),
            "reference_sha256": sha256(old_path),
            "rerun_sha256": sha256(new_path),
        })
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

    report = {
        "scope": "Full default synthetic run compared with checked-in outputs; no human data.",
        "reference_repository_commit": "11f80d772966ad1f4f58ddc88af5ec1211fbf963",
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
        "regenerated_figures": figures,
        "replication_data_sha256": sha256(fresh / "monte_carlo_replications.csv"),
        "result": "All numerical comparisons and replication integrity checks passed.",
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"csv_files": len(comparisons), "rows": len(mc),
                      "fits": len(mc) * 2, "result": report["result"]}))


if __name__ == "__main__":
    main()
