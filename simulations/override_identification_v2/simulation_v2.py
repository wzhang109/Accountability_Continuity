"""Accountability Continuity simulation v2.

This is a small identification study, not evidence about any real deployment.

The script has four jobs:

1. State the analytic non-identification result for override rate alone.
2. Show a broad equivalence set and a likelihood ridge, rather than one
   hand-picked pair of trajectories.
3. Use repeated Monte Carlo experiments to test recovery when model audits and
   an imperfect engagement proxy are added.
4. Stress-test the result across sample sizes, parameter values, and a
   misspecified world in which detection ability changes over time.

Author: Wenwen (Celine) Zhang
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import minimize
from scipy.stats import chi2


@dataclass(frozen=True)
class StudyConfig:
    periods: int = 24
    cases_per_period: int = 4000
    detection: float = 0.75
    false_alarm: float = 0.05
    disengaged_override: float = 0.04
    proxy_sensitivity: float = 0.90
    proxy_false_positive: float = 0.10
    proxy_sample_share: float = 0.25
    master_seed: int = 20260827
    sweep_draws: int = 60000
    sweep_tolerance: float = 0.005
    monte_carlo_replications: int = 1000
    sample_sizes: tuple[int, ...] = (250, 1000, 4000)
    audit_shares: tuple[float, ...] = (0.10, 0.25)

    @classmethod
    def from_json(cls, path: Path) -> "StudyConfig":
        raw = json.loads(path.read_text(encoding="utf-8"))
        if "sample_sizes" in raw:
            raw["sample_sizes"] = tuple(raw["sample_sizes"])
        if "audit_shares" in raw:
            raw["audit_shares"] = tuple(raw["audit_shares"])
        return cls(**raw)


def linear_path(start: float, end: float, periods: int) -> np.ndarray:
    return np.linspace(start, end, periods, dtype=float)


def override_rate(
    p: np.ndarray | float,
    e: np.ndarray | float,
    d: np.ndarray | float,
    f: float,
    q: float,
) -> np.ndarray:
    """Expected override rate under the stated binary engagement model."""
    p_arr = np.asarray(p, dtype=float)
    e_arr = np.asarray(e, dtype=float)
    d_arr = np.asarray(d, dtype=float)
    return e_arr * (d_arr * (1.0 - p_arr) + f * p_arr) + (1.0 - e_arr) * q


def engagement_from_rate(
    rate: np.ndarray | float,
    p: np.ndarray | float,
    d: np.ndarray | float,
    f: float,
    q: float,
) -> np.ndarray:
    """Method-of-moments engagement implied by rate and independently known p."""
    rate_arr = np.asarray(rate, dtype=float)
    p_arr = np.asarray(p, dtype=float)
    d_arr = np.asarray(d, dtype=float)
    denominator = d_arr * (1.0 - p_arr) + f * p_arr - q
    with np.errstate(divide="ignore", invalid="ignore"):
        return (rate_arr - q) / denominator


def proxy_rate(e: np.ndarray | float, sensitivity: float, false_positive: float) -> np.ndarray:
    """Observed process-log rate for a misclassified engagement proxy."""
    e_arr = np.asarray(e, dtype=float)
    return false_positive + (sensitivity - false_positive) * e_arr


def trend_change(values: np.ndarray) -> float:
    """Projected end-to-end change from an OLS linear trend over normalized time."""
    values = np.asarray(values, dtype=float)
    x = np.linspace(0.0, 1.0, values.size)
    mask = np.isfinite(values)
    if mask.sum() < 3:
        return float("nan")
    return float(np.polyfit(x[mask], values[mask], 1)[0])


def trend_change_with_se(
    values: np.ndarray, variances: np.ndarray
) -> tuple[float, float]:
    """OLS end-to-end trend and its design-based standard error.

    Time is normalized to [0, 1], so the slope is the projected end-to-end
    change. Period estimates are independent in the simulation and may have
    different known or plug-in sampling variances.
    """
    values = np.asarray(values, dtype=float)
    variances = np.asarray(variances, dtype=float)
    x = np.linspace(0.0, 1.0, values.size)
    mask = np.isfinite(values) & np.isfinite(variances) & (variances >= 0.0)
    if mask.sum() < 3:
        return float("nan"), float("nan")
    x_used = x[mask]
    centered = x_used - x_used.mean()
    denominator = float(np.sum(centered**2))
    weights = centered / denominator
    slope = float(np.sum(weights * values[mask]))
    standard_error = float(np.sqrt(np.sum((weights**2) * variances[mask])))
    return slope, standard_error


def label_trajectory_pattern(
    delta_p: float, delta_e: float, threshold: float = 0.08
) -> str:
    """Coarse p/e trajectory pattern; it does not identify a causal mechanism."""
    improves = delta_p > threshold
    disengages = delta_e < -threshold
    if improves and disengages:
        return "mixed"
    if improves:
        return "improvement_only"
    if disengages:
        return "disengagement_only"
    return "stable_p_and_e"


def label_detected_trend_regime(
    delta_p: float,
    se_p: float,
    delta_e: float,
    se_e: float,
    z_value: float = 1.959963984540054,
) -> str:
    """Classify only when a two-sided 95% interval excludes zero.

    This is a simple decision rule for simulation performance, not a proposed
    operational governance threshold.
    """
    if not np.all(np.isfinite([delta_p, se_p, delta_e, se_e])):
        return "indeterminate"
    improves = delta_p - z_value * se_p > 0.0
    accuracy_declines = delta_p + z_value * se_p < 0.0
    disengages = delta_e + z_value * se_e < 0.0
    engagement_increases = delta_e - z_value * se_e > 0.0
    if improves and disengages:
        return "mixed"
    if improves and not engagement_increases:
        return "improvement_only"
    if disengages and not accuracy_declines:
        return "disengagement_only"
    if not any([improves, accuracy_declines, disengages, engagement_increases]):
        return "no_detected_target_trend"
    return "other_detected_trend"


def build_scenarios(config: StudyConfig) -> dict[str, pd.DataFrame]:
    """Return six specified scenarios, including two misspecification checks."""
    t = np.arange(config.periods)
    f = config.false_alarm
    q = config.disengaged_override
    d0 = config.detection

    p_a = linear_path(0.60, 0.88, config.periods)
    e_a = np.full(config.periods, 0.90)
    d_a = np.full(config.periods, d0)
    r_a = override_rate(p_a, e_a, d_a, f, q)

    p_b = np.full(config.periods, 0.60)
    d_b = np.full(config.periods, d0)
    e_b = engagement_from_rate(r_a, p_b, d_b, f, q)

    s0 = np.full(config.periods, config.proxy_sensitivity)
    g0 = np.full(config.periods, config.proxy_false_positive)

    raw = {
        "improvement_only": (p_a, e_a, d_a, s0, g0),
        "exact_equivalent_disengagement": (p_b, e_b, d_b, s0, g0),
        "mixed": (
            linear_path(0.60, 0.75, config.periods),
            linear_path(0.90, 0.55, config.periods),
            np.full(config.periods, d0),
            s0,
            g0,
        ),
        "stable_negative_control": (
            np.full(config.periods, 0.75),
            np.full(config.periods, 0.75),
            np.full(config.periods, d0),
            s0,
            g0,
        ),
        "detection_drift_misspecification": (
            np.full(config.periods, 0.60),
            np.full(config.periods, 0.90),
            linear_path(0.75, 0.30, config.periods),
            s0,
            g0,
        ),
        "proxy_drift_misspecification": (
            np.full(config.periods, 0.60),
            np.full(config.periods, 0.90),
            np.full(config.periods, d0),
            linear_path(config.proxy_sensitivity, 0.65, config.periods),
            g0,
        ),
    }

    scenarios: dict[str, pd.DataFrame] = {}
    for name, (p, e, d, proxy_sensitivity_actual, proxy_fpr_actual) in raw.items():
        rate = override_rate(p, e, d, f, q)
        z_rate = proxy_fpr_actual + (
            proxy_sensitivity_actual - proxy_fpr_actual
        ) * e
        scenarios[name] = pd.DataFrame(
            {
                "scenario": name,
                "period": t,
                "model_accuracy": p,
                "engagement": e,
                "detection": d,
                "proxy_sensitivity_actual": proxy_sensitivity_actual,
                "proxy_false_positive_actual": proxy_fpr_actual,
                "expected_override_rate": rate,
                "expected_proxy_rate": z_rate,
            }
        )
    return scenarios


def identification_curves(config: StudyConfig, target_rates: Iterable[float]) -> pd.DataFrame:
    """Feasible (p,e) pairs for selected observed override rates."""
    p_grid = np.linspace(0.35, 0.95, 601)
    rows: list[pd.DataFrame] = []
    for rate in target_rates:
        e_grid = engagement_from_rate(
            rate,
            p_grid,
            config.detection,
            config.false_alarm,
            config.disengaged_override,
        )
        valid = np.isfinite(e_grid) & (e_grid >= 0.0) & (e_grid <= 1.0)
        rows.append(
            pd.DataFrame(
                {
                    "observed_override_rate": rate,
                    "model_accuracy": p_grid[valid],
                    "implied_engagement": e_grid[valid],
                }
            )
        )
    return pd.concat(rows, ignore_index=True)


def parameter_sweep(
    config: StudyConfig, target_rate: np.ndarray, rng: np.random.Generator
) -> pd.DataFrame:
    """Find many smooth paths that nearly reproduce the target override path."""
    draws = config.sweep_draws
    p_end = rng.uniform(0.55, 0.92, draws)
    e_end = rng.uniform(0.20, 0.95, draws)
    x = np.linspace(0.0, 1.0, config.periods)
    p_paths = 0.60 + (p_end[:, None] - 0.60) * x[None, :]
    e_paths = 0.90 + (e_end[:, None] - 0.90) * x[None, :]
    rates = override_rate(
        p_paths,
        e_paths,
        config.detection,
        config.false_alarm,
        config.disengaged_override,
    )
    rmse = np.sqrt(np.mean((rates - target_rate[None, :]) ** 2, axis=1))
    max_abs = np.max(np.abs(rates - target_rate[None, :]), axis=1)
    accepted = rmse <= config.sweep_tolerance
    result = pd.DataFrame(
        {
            "p_start": 0.60,
            "p_end": p_end[accepted],
            "e_start": 0.90,
            "e_end": e_end[accepted],
            "override_path_rmse": rmse[accepted],
            "override_path_max_abs": max_abs[accepted],
        }
    )
    result["delta_p"] = result["p_end"] - result["p_start"]
    result["delta_e"] = result["e_end"] - result["e_start"]
    result["trajectory_trend_pattern"] = [
        label_trajectory_pattern(dp, de, threshold=0.05)
        for dp, de in zip(result["delta_p"], result["delta_e"])
    ]
    return result.sort_values("override_path_rmse").reset_index(drop=True)


def likelihood_surface(
    config: StudyConfig,
    target_rate: np.ndarray,
    p_grid: np.ndarray | None = None,
    e_grid: np.ndarray | None = None,
) -> pd.DataFrame:
    """Expected-data likelihood surface with fixed starts and linear paths."""
    if p_grid is None:
        p_grid = np.linspace(0.55, 0.92, 121)
    if e_grid is None:
        e_grid = np.linspace(0.20, 0.95, 121)
    observed = np.rint(config.cases_per_period * target_rate)
    x = np.linspace(0.0, 1.0, config.periods)
    rows: list[tuple[float, float, float]] = []
    for p_end in p_grid:
        p_path = 0.60 + (p_end - 0.60) * x
        for e_end in e_grid:
            e_path = 0.90 + (e_end - 0.90) * x
            rate = override_rate(
                p_path,
                e_path,
                config.detection,
                config.false_alarm,
                config.disengaged_override,
            )
            rate = np.clip(rate, 1e-9, 1.0 - 1e-9)
            loglik = float(
                np.sum(
                    observed * np.log(rate)
                    + (config.cases_per_period - observed) * np.log1p(-rate)
                )
            )
            rows.append((p_end, e_end, loglik))
    result = pd.DataFrame(rows, columns=["p_end", "e_end", "log_likelihood"])
    result["delta_log_likelihood"] = result["log_likelihood"].max() - result["log_likelihood"]
    return result


def _binomial_log_likelihood(
    counts: np.ndarray, totals: int | np.ndarray, probability: np.ndarray
) -> float:
    probability = np.clip(np.asarray(probability, dtype=float), 1e-9, 1.0 - 1e-9)
    counts = np.asarray(counts, dtype=float)
    totals = np.asarray(totals, dtype=float)
    return float(
        np.sum(counts * np.log(probability) + (totals - counts) * np.log1p(-probability))
    )


def _endpoint_design(periods: int) -> np.ndarray:
    x = np.linspace(0.0, 1.0, periods)
    return np.column_stack([1.0 - x, x])


def _best_bounded_fit(
    objective, starts: list[np.ndarray], gradient=None
) -> tuple[np.ndarray, bool]:
    """Use several starts for a small bounded likelihood problem."""
    results = [
        minimize(
            objective,
            np.clip(start, 0.001, 0.999),
            method="L-BFGS-B",
            jac=gradient,
            bounds=[(0.001, 0.999)] * len(start),
        )
        for start in starts
    ]
    best = min(results, key=lambda result: float(result.fun))
    return np.asarray(best.x, dtype=float), bool(best.success)


def _safe_inverse(matrix: np.ndarray) -> np.ndarray:
    """Moore-Penrose inverse keeps weak-identification cases explicit."""
    return np.linalg.pinv(matrix, rcond=1e-10)


def fit_audit_override(
    accuracy_counts: np.ndarray,
    n_audit: int,
    override_counts: np.ndarray,
    n_operational: int,
    config: StudyConfig,
) -> dict[str, float | bool | np.ndarray]:
    """Constrained joint likelihood for accuracy audit plus override counts.

    The fit assumes d, f, and q are known and constant. It is deliberately
    challenged by the detection-drift scenario.
    """
    periods = len(accuracy_counts)
    design = _endpoint_design(periods)

    def objective(theta: np.ndarray) -> float:
        p = design @ theta[:2]
        e = design @ theta[2:]
        r = override_rate(
            p,
            e,
            config.detection,
            config.false_alarm,
            config.disengaged_override,
        )
        return -(
            _binomial_log_likelihood(accuracy_counts, n_audit, p)
            + _binomial_log_likelihood(override_counts, n_operational, r)
        )

    def gradient(theta: np.ndarray) -> np.ndarray:
        p = design @ theta[:2]
        e = design @ theta[2:]
        a_minus_q = (
            config.detection * (1.0 - p)
            + config.false_alarm * p
            - config.disengaged_override
        )
        r = config.disengaged_override + e * a_minus_q
        p = np.clip(p, 1e-9, 1.0 - 1e-9)
        r = np.clip(r, 1e-9, 1.0 - 1e-9)
        score_p = (n_audit * p - accuracy_counts) / (p * (1.0 - p))
        score_r = (n_operational * r - override_counts) / (r * (1.0 - r))
        j_r = np.column_stack(
            [
                e[:, None] * (config.false_alarm - config.detection) * design,
                a_minus_q[:, None] * design,
            ]
        )
        return np.concatenate([design.T @ score_p, np.zeros(2)]) + j_r.T @ score_r

    # The override probability is bilinear in p and e, so use multiple starts.
    starts = [
        np.array([0.60, 0.85, 0.90, 0.80]),
        np.array([0.60, 0.60, 0.90, 0.30]),
        np.array([0.75, 0.75, 0.75, 0.75]),
    ]
    theta, converged = _best_bounded_fit(objective, starts, gradient)
    p = design @ theta[:2]
    e = design @ theta[2:]
    r = override_rate(
        p,
        e,
        config.detection,
        config.false_alarm,
        config.disengaged_override,
    )

    # Expected Fisher information for the fitted, correctly specified model.
    j_p = np.column_stack([design, np.zeros_like(design)])
    a_minus_q = (
        config.detection * (1.0 - p)
        + config.false_alarm * p
        - config.disengaged_override
    )
    j_r = np.column_stack(
        [
            e[:, None] * (config.false_alarm - config.detection) * design,
            a_minus_q[:, None] * design,
        ]
    )
    info = (
        j_p.T @ ((n_audit / np.clip(p * (1.0 - p), 1e-9, None))[:, None] * j_p)
        + j_r.T @ ((n_operational / np.clip(r * (1.0 - r), 1e-9, None))[:, None] * j_r)
    )
    covariance = _safe_inverse(info)
    contrast_p = np.array([-1.0, 1.0, 0.0, 0.0])
    contrast_e = np.array([0.0, 0.0, -1.0, 1.0])
    return {
        "theta": theta,
        "covariance": covariance,
        "delta_p": float(contrast_p @ theta),
        "delta_e": float(contrast_e @ theta),
        "se_delta_p": float(np.sqrt(max(0.0, contrast_p @ covariance @ contrast_p))),
        "se_delta_e": float(np.sqrt(max(0.0, contrast_e @ covariance @ contrast_e))),
        "converged": converged,
        "boundary_hit": bool(np.any((theta < 0.002) | (theta > 0.998))),
    }


def fit_audit_proxy(
    accuracy_counts: np.ndarray,
    n_audit: int,
    proxy_counts: np.ndarray,
    n_proxy: int,
    config: StudyConfig,
) -> dict[str, float | bool | np.ndarray]:
    """Best-case constrained fit using a calibrated engagement proxy.

    The estimator assumes the configured sensitivity and false-positive rate
    are known and constant. A separate sensitivity analysis violates this.
    """
    periods = len(accuracy_counts)
    design = _endpoint_design(periods)
    proxy_gap = config.proxy_sensitivity - config.proxy_false_positive

    def objective(theta: np.ndarray) -> float:
        p = design @ theta[:2]
        e = design @ theta[2:]
        z = config.proxy_false_positive + proxy_gap * e
        return -(
            _binomial_log_likelihood(accuracy_counts, n_audit, p)
            + _binomial_log_likelihood(proxy_counts, n_proxy, z)
        )

    def gradient(theta: np.ndarray) -> np.ndarray:
        p = np.clip(design @ theta[:2], 1e-9, 1.0 - 1e-9)
        e = design @ theta[2:]
        z = np.clip(
            config.proxy_false_positive + proxy_gap * e,
            1e-9,
            1.0 - 1e-9,
        )
        score_p = (n_audit * p - accuracy_counts) / (p * (1.0 - p))
        score_z = (n_proxy * z - proxy_counts) / (z * (1.0 - z))
        return np.concatenate(
            [design.T @ score_p, proxy_gap * design.T @ score_z]
        )

    # This likelihood is concave in the two linear endpoint paths, so one
    # interior start is sufficient.
    starts = [np.array([0.75, 0.75, 0.75, 0.75])]
    theta, converged = _best_bounded_fit(objective, starts, gradient)
    p = design @ theta[:2]
    e = design @ theta[2:]
    z = config.proxy_false_positive + proxy_gap * e

    j_p = np.column_stack([design, np.zeros_like(design)])
    j_z = np.column_stack([np.zeros_like(design), proxy_gap * design])
    info = (
        j_p.T @ ((n_audit / np.clip(p * (1.0 - p), 1e-9, None))[:, None] * j_p)
        + j_z.T @ ((n_proxy / np.clip(z * (1.0 - z), 1e-9, None))[:, None] * j_z)
    )
    covariance = _safe_inverse(info)
    contrast_p = np.array([-1.0, 1.0, 0.0, 0.0])
    contrast_e = np.array([0.0, 0.0, -1.0, 1.0])
    return {
        "theta": theta,
        "covariance": covariance,
        "delta_p": float(contrast_p @ theta),
        "delta_e": float(contrast_e @ theta),
        "se_delta_p": float(np.sqrt(max(0.0, contrast_p @ covariance @ contrast_p))),
        "se_delta_e": float(np.sqrt(max(0.0, contrast_e @ covariance @ contrast_e))),
        "converged": converged,
        "boundary_hit": bool(np.any((theta < 0.002) | (theta > 0.998))),
    }


def override_predictive_check(
    fit: dict[str, float | bool | np.ndarray],
    override_counts: np.ndarray,
    n_operational: int,
    config: StudyConfig,
) -> tuple[float, float]:
    """Compare override data to a prediction built from independent channels."""
    theta = np.asarray(fit["theta"], dtype=float)
    covariance = np.asarray(fit["covariance"], dtype=float)
    design = _endpoint_design(len(override_counts))
    p = design @ theta[:2]
    e = design @ theta[2:]
    predicted = override_rate(
        p,
        e,
        config.detection,
        config.false_alarm,
        config.disengaged_override,
    )
    a_minus_q = (
        config.detection * (1.0 - p)
        + config.false_alarm * p
        - config.disengaged_override
    )
    jacobian = np.column_stack(
        [
            e[:, None] * (config.false_alarm - config.detection) * design,
            a_minus_q[:, None] * design,
        ]
    )
    operational_variance = np.diag(
        np.clip(predicted * (1.0 - predicted) / n_operational, 1e-10, None)
    )
    predictive_variance = operational_variance + jacobian @ covariance @ jacobian.T
    difference = override_counts / n_operational - predicted
    statistic = float(difference @ _safe_inverse(predictive_variance) @ difference)
    p_value = float(chi2.sf(statistic, df=len(difference)))
    return statistic, p_value


def simulate_aggregate_observations(
    scenario: pd.DataFrame,
    config: StudyConfig,
    cases_per_period: int,
    audit_share: float,
    rng: np.random.Generator,
) -> dict[str, np.ndarray | int]:
    """Simulate three independent measurement channels period by period.

    The channels are:
      * override counts from the operational log;
      * model correctness from an independently adjudicated audit sample;
      * a noisy process log for whether primary evidence was opened.
    """
    n = int(cases_per_period)
    n_audit = max(20, int(round(n * audit_share)))
    n_proxy = max(20, int(round(n * config.proxy_sample_share)))
    rate = scenario["expected_override_rate"].to_numpy()
    p = scenario["model_accuracy"].to_numpy()
    z_rate = scenario["expected_proxy_rate"].to_numpy()
    return {
        "override_count": rng.binomial(n, rate),
        "accuracy_count": rng.binomial(n_audit, p),
        "proxy_count": rng.binomial(n_proxy, z_rate),
        "n_operational": n,
        "n_audit": n_audit,
        "n_proxy": n_proxy,
    }


def monte_carlo(config: StudyConfig, scenarios: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Repeatedly fit two constrained measurement bundles.

    `audit_override` assumes d, f, and q are known and stable. `audit_proxy`
    is a best-case benchmark that assumes the proxy calibration is known and
    stable. The independently fitted audit-proxy paths are then used to predict
    override counts; disagreement is reported as an assumption check rather
    than forced into an engagement conclusion.
    """
    seed_sequence = np.random.SeedSequence(config.master_seed)
    total_cells = (
        len(scenarios)
        * len(config.sample_sizes)
        * len(config.audit_shares)
        * config.monte_carlo_replications
    )
    child_seeds = iter(seed_sequence.spawn(total_cells))
    rows: list[dict[str, float | int | str]] = []

    for name, scenario in scenarios.items():
        true_p = scenario["model_accuracy"].to_numpy()
        true_e = scenario["engagement"].to_numpy()
        true_r = scenario["expected_override_rate"].to_numpy()
        true_dp = float(true_p[-1] - true_p[0])
        true_de = float(true_e[-1] - true_e[0])
        true_dr = float(true_r[-1] - true_r[0])
        true_regime = label_trajectory_pattern(true_dp, true_de)

        for n in config.sample_sizes:
            for audit_share in config.audit_shares:
                for replication in range(config.monte_carlo_replications):
                    rng = np.random.default_rng(next(child_seeds))
                    obs = simulate_aggregate_observations(
                        scenario, config, n, audit_share, rng
                    )
                    override_counts = np.asarray(obs["override_count"], dtype=int)
                    accuracy_counts = np.asarray(obs["accuracy_count"], dtype=int)
                    proxy_counts = np.asarray(obs["proxy_count"], dtype=int)
                    n_operational = int(obs["n_operational"])
                    n_audit = int(obs["n_audit"])
                    n_proxy = int(obs["n_proxy"])

                    audit_override = fit_audit_override(
                        accuracy_counts,
                        n_audit,
                        override_counts,
                        n_operational,
                        config,
                    )
                    audit_proxy = fit_audit_proxy(
                        accuracy_counts,
                        n_audit,
                        proxy_counts,
                        n_proxy,
                        config,
                    )
                    check_statistic, check_p = override_predictive_check(
                        audit_proxy,
                        override_counts,
                        n_operational,
                        config,
                    )

                    dp_ao = float(audit_override["delta_p"])
                    de_ao = float(audit_override["delta_e"])
                    se_dp_ao = float(audit_override["se_delta_p"])
                    se_de_ao = float(audit_override["se_delta_e"])
                    dp_ap = float(audit_proxy["delta_p"])
                    de_ap = float(audit_proxy["delta_e"])
                    se_dp_ap = float(audit_proxy["se_delta_p"])
                    se_de_ap = float(audit_proxy["se_delta_e"])

                    r_hat = override_counts / n_operational
                    var_r = np.clip(r_hat * (1.0 - r_hat) / n_operational, 1e-10, None)
                    dr_hat, dr_se = trend_change_with_se(r_hat, var_r)
                    z95 = 1.959963984540054

                    rows.append(
                        {
                            "scenario": name,
                            "cases_per_period": n,
                            "audit_share": audit_share,
                            "replication": replication,
                            "true_delta_p": true_dp,
                            "true_delta_e": true_de,
                            "true_delta_override": true_dr,
                            "delta_override_hat": dr_hat,
                            "delta_override_se": dr_se,
                            "delta_p_audit_override_hat": dp_ao,
                            "delta_p_audit_override_se": se_dp_ao,
                            "delta_e_audit_override_hat": de_ao,
                            "delta_e_audit_override_se": se_de_ao,
                            "delta_p_audit_proxy_hat": dp_ap,
                            "delta_p_audit_proxy_se": se_dp_ap,
                            "delta_e_audit_proxy_hat": de_ap,
                            "delta_e_audit_proxy_se": se_de_ap,
                            "delta_p_audit_override_covered_95": abs(dp_ao - true_dp) <= z95 * se_dp_ao,
                            "delta_e_audit_override_covered_95": abs(de_ao - true_de) <= z95 * se_de_ao,
                            "delta_p_audit_proxy_covered_95": abs(dp_ap - true_dp) <= z95 * se_dp_ap,
                            "delta_e_audit_proxy_covered_95": abs(de_ap - true_de) <= z95 * se_de_ap,
                            "delta_override_covered_95": abs(dr_hat - true_dr) <= z95 * dr_se,
                            "true_p_e_trend_regime": true_regime,
                            "audit_override_trend_regime": label_detected_trend_regime(
                                dp_ao, se_dp_ao, de_ao, se_de_ao
                            ),
                            "audit_proxy_trend_regime": label_detected_trend_regime(
                                dp_ap, se_dp_ap, de_ap, se_de_ap
                            ),
                            "audit_override_converged": bool(audit_override["converged"]),
                            "audit_proxy_converged": bool(audit_proxy["converged"]),
                            "audit_override_boundary_hit": bool(audit_override["boundary_hit"]),
                            "audit_proxy_boundary_hit": bool(audit_proxy["boundary_hit"]),
                            "override_predictive_check_statistic": check_statistic,
                            "override_predictive_check_p": check_p,
                            "override_predictive_check_reject_05": check_p < 0.05,
                        }
                    )
    return pd.DataFrame(rows)


def recovery_summary(mc: pd.DataFrame) -> pd.DataFrame:
    mappings = {
        "delta_p_audit_override": ("delta_p_audit_override_hat", "true_delta_p", "delta_p_audit_override_se", "delta_p_audit_override_covered_95"),
        "delta_e_audit_override": ("delta_e_audit_override_hat", "true_delta_e", "delta_e_audit_override_se", "delta_e_audit_override_covered_95"),
        "delta_p_audit_proxy": ("delta_p_audit_proxy_hat", "true_delta_p", "delta_p_audit_proxy_se", "delta_p_audit_proxy_covered_95"),
        "delta_e_audit_proxy": ("delta_e_audit_proxy_hat", "true_delta_e", "delta_e_audit_proxy_se", "delta_e_audit_proxy_covered_95"),
        "delta_override": ("delta_override_hat", "true_delta_override", "delta_override_se", "delta_override_covered_95"),
    }
    rows: list[dict[str, float | int | str]] = []
    group_cols = ["scenario", "cases_per_period", "audit_share"]
    for keys, group in mc.groupby(group_cols, sort=False):
        scenario, n, audit_share = keys
        for estimator, (estimate_col, truth_col, se_col, coverage_col) in mappings.items():
            estimate = group[estimate_col].to_numpy(dtype=float)
            truth = group[truth_col].to_numpy(dtype=float)
            standard_error = group[se_col].to_numpy(dtype=float)
            covered = group[coverage_col].to_numpy(dtype=bool)
            error = estimate - truth
            finite = np.isfinite(error) & np.isfinite(standard_error)
            error = error[finite]
            estimate_finite = estimate[finite]
            if error.size == 0:
                continue
            rows.append(
                {
                    "scenario": scenario,
                    "cases_per_period": int(n),
                    "audit_share": float(audit_share),
                    "estimator": estimator,
                    "replications": int(error.size),
                    "truth": float(truth[finite][0]),
                    "mean_estimate": float(np.mean(estimate_finite)),
                    "bias": float(np.mean(error)),
                    "rmse": float(np.sqrt(np.mean(error**2))),
                    "empirical_sd": float(np.std(estimate_finite, ddof=1)),
                    "mean_reported_se": float(np.mean(standard_error[finite])),
                    "coverage_95": float(np.mean(covered[finite])),
                    "mcse_bias": float(np.std(error, ddof=1) / math.sqrt(error.size)),
                    "mcse_coverage": float(
                        np.sqrt(
                            np.mean(covered[finite])
                            * (1.0 - np.mean(covered[finite]))
                            / error.size
                        )
                    ),
                }
            )
    return pd.DataFrame(rows)


def trend_regime_summary(mc: pd.DataFrame) -> pd.DataFrame:
    """Secondary labels for p/e trends, not causal mechanism classification."""
    rows: list[dict[str, float | int | str]] = []
    group_cols = ["scenario", "cases_per_period", "audit_share"]
    for keys, group in mc.groupby(group_cols, sort=False):
        scenario, n, audit_share = keys
        for bundle in ["audit_override", "audit_proxy"]:
            predicted = group[f"{bundle}_trend_regime"]
            true_regime = group["true_p_e_trend_regime"].replace(
                {"stable_p_and_e": "no_detected_target_trend"}
            )
            correct = predicted.eq(true_regime)
            any_disengagement = predicted.isin(["disengagement_only", "mixed"])
            rows.append(
                {
                    "scenario": scenario,
                    "cases_per_period": int(n),
                    "audit_share": float(audit_share),
                    "bundle": bundle,
                    "exact_trend_regime_match_rate": float(correct.mean()),
                    "false_any_disengagement_rate": float(
                        any_disengagement.mean()
                        if group["true_p_e_trend_regime"].iloc[0] == "stable_p_and_e"
                        else np.nan
                    ),
                }
            )
    return pd.DataFrame(rows)


def assumption_check_summary(mc: pd.DataFrame) -> pd.DataFrame:
    """Summarize the independent-channel override predictive check."""
    rows: list[dict[str, float | int | str]] = []
    group_cols = ["scenario", "cases_per_period", "audit_share"]
    for keys, group in mc.groupby(group_cols, sort=False):
        scenario, n, audit_share = keys
        rows.append(
            {
                "scenario": scenario,
                "cases_per_period": int(n),
                "audit_share": float(audit_share),
                "replications": int(len(group)),
                "override_predictive_rejection_rate_05": float(
                    group["override_predictive_check_reject_05"].mean()
                ),
                "median_predictive_p_value": float(
                    group["override_predictive_check_p"].median()
                ),
                "audit_override_nonconvergence_rate": float(
                    1.0 - group["audit_override_converged"].mean()
                ),
                "audit_proxy_nonconvergence_rate": float(
                    1.0 - group["audit_proxy_converged"].mean()
                ),
                "audit_override_boundary_rate": float(
                    group["audit_override_boundary_hit"].mean()
                ),
                "audit_proxy_boundary_rate": float(
                    group["audit_proxy_boundary_hit"].mean()
                ),
            }
        )
    return pd.DataFrame(rows)


def sensitivity_grid(config: StudyConfig) -> pd.DataFrame:
    rows: list[dict[str, float | bool]] = []
    for d in (0.50, 0.75, 0.90):
        for f in (0.01, 0.05, 0.15):
            for q in (0.00, 0.04, 0.10):
                p_a = linear_path(0.60, 0.88, config.periods)
                e_a = np.full(config.periods, 0.90)
                r_a = override_rate(p_a, e_a, d, f, q)
                p_b = np.full(config.periods, 0.60)
                e_b = engagement_from_rate(r_a, p_b, d, f, q)
                feasible = bool(
                    np.all(np.isfinite(e_b))
                    and np.all(e_b >= 0.0)
                    and np.all(e_b <= 1.0)
                )
                diagnostic_a_end = abs(d * (1.0 - p_a[-1]) + f * p_a[-1] - q)
                diagnostic_b_end = abs(d * (1.0 - p_b[-1]) + f * p_b[-1] - q)
                rows.append(
                    {
                        "detection": d,
                        "false_alarm": f,
                        "disengaged_override": q,
                        "feasible_equivalent": feasible,
                        "equivalent_e_start": float(e_b[0]),
                        "equivalent_e_end": float(e_b[-1]),
                        "override_start": float(r_a[0]),
                        "override_end": float(r_a[-1]),
                        "identification_diagnostic_improvement_path_end": diagnostic_a_end,
                        "identification_diagnostic_equivalent_path_end": diagnostic_b_end,
                    }
                )
    return pd.DataFrame(rows)


def proxy_calibration_sensitivity(config: StudyConfig) -> pd.DataFrame:
    """Expected trend bias when actual proxy calibration differs from assumed."""
    scenarios = build_scenarios(config)
    engagement = scenarios["exact_equivalent_disengagement"]["engagement"].to_numpy()
    true_delta = float(engagement[-1] - engagement[0])
    assumed_gap = config.proxy_sensitivity - config.proxy_false_positive
    rows: list[dict[str, float | bool]] = []
    for actual_sensitivity in (0.70, 0.90, 0.98):
        for actual_false_positive in (0.02, 0.10, 0.25):
            actual_gap = actual_sensitivity - actual_false_positive
            identified = actual_gap > 0.0 and assumed_gap > 0.0
            corrected_delta = (
                actual_gap / assumed_gap * true_delta if identified else float("nan")
            )
            rows.append(
                {
                    "actual_proxy_sensitivity": actual_sensitivity,
                    "actual_proxy_false_positive": actual_false_positive,
                    "actual_proxy_separation": actual_gap,
                    "assumed_proxy_sensitivity": config.proxy_sensitivity,
                    "assumed_proxy_false_positive": config.proxy_false_positive,
                    "true_delta_e": true_delta,
                    "expected_corrected_delta_e": corrected_delta,
                    "expected_bias": corrected_delta - true_delta,
                    "inverse_proxy_separation_squared": (
                        1.0 / actual_gap**2 if identified else float("inf")
                    ),
                    "identified": identified,
                }
            )
    return pd.DataFrame(rows)


def plot_scenarios(paths: pd.DataFrame, output: Path) -> None:
    colors = {
        "improvement_only": "#1f4e79",
        "exact_equivalent_disengagement": "#c1462c",
        "mixed": "#6a3d9a",
        "stable_negative_control": "#2b8a3e",
        "detection_drift_misspecification": "#8c6d31",
        "proxy_drift_misspecification": "#4d4d4d",
    }
    fig, axes = plt.subplots(1, 4, figsize=(17.0, 4.1))
    for name, group in paths.groupby("scenario", sort=False):
        color = colors[name]
        label = name.replace("_", " ")
        axes[0].plot(group["period"], group["model_accuracy"], color=color, lw=2, label=label)
        axes[1].plot(group["period"], group["engagement"], color=color, lw=2)
        axes[2].plot(group["period"], group["expected_override_rate"], color=color, lw=2)
        axes[3].plot(group["period"], group["expected_proxy_rate"], color=color, lw=2)
    axes[0].set_title("Model accuracy")
    axes[1].set_title("Latent engagement")
    axes[2].set_title("Expected override rate")
    axes[3].set_title("Expected proxy rate")
    for ax in axes:
        ax.set_xlabel("Period")
        ax.set_ylim(0.0, 1.0)
        ax.grid(alpha=0.25)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(fontsize=7.7, loc="lower right")
    fig.suptitle("Specified mechanisms: similar surface trends, different latent processes", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_equivalence(
    curves: pd.DataFrame, sweep: pd.DataFrame, output: Path
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8))
    for rate, group in curves.groupby("observed_override_rate"):
        axes[0].plot(
            group["model_accuracy"],
            group["implied_engagement"],
            lw=2,
            label=f"R = {rate:.3f}",
        )
    axes[0].set_title("Analytic equivalence sets")
    axes[0].set_xlabel("Model accuracy p")
    axes[0].set_ylabel("Implied engagement e")
    axes[0].legend(fontsize=8)

    points = axes[1].scatter(
        sweep["p_end"],
        sweep["e_end"],
        s=13,
        alpha=0.55,
        c=sweep["override_path_rmse"],
        cmap="viridis_r",
    )
    axes[1].set_title("Accepted smooth paths within a fixed RMSE tolerance")
    axes[1].set_xlabel("End model accuracy")
    axes[1].set_ylabel("End engagement")
    fig.colorbar(points, ax=axes[1], label="Override-path RMSE")

    for ax in axes:
        ax.set_xlim(0.35, 0.96)
        ax.set_ylim(0.0, 1.0)
        ax.grid(alpha=0.25)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Override rate alone maps to many accuracy and engagement paths", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_likelihood(surface: pd.DataFrame, output: Path, exact_e_end: float) -> None:
    pivot = surface.pivot(index="e_end", columns="p_end", values="delta_log_likelihood")
    x = pivot.columns.to_numpy()
    y = pivot.index.to_numpy()
    z = pivot.to_numpy()
    fig, ax = plt.subplots(figsize=(7.2, 5.6))
    capped = np.minimum(z, 60.0)
    mesh = ax.contourf(x, y, capped, levels=np.linspace(0, 60, 25), cmap="viridis_r")
    ax.contour(x, y, z, levels=[2, 5, 10, 25, 50], colors="white", linewidths=0.7)
    ax.scatter([0.88], [0.90], color="#1f4e79", s=55, label="Improvement endpoint")
    ax.scatter([0.60], [exact_e_end], color="#c1462c", s=55, label="Equivalent disengagement endpoint")
    ax.set_xlabel("End model accuracy")
    ax.set_ylabel("End engagement")
    ax.set_title("Expected-data likelihood forms a connected ridge")
    ax.legend(fontsize=8)
    fig.colorbar(mesh, ax=ax, label="Delta log likelihood, capped at 60")
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_recovery(
    recovery: pd.DataFrame, checks: pd.DataFrame, output: Path
) -> None:
    correctly_specified = recovery[
        ~recovery["scenario"].str.contains("misspecification")
        & recovery["audit_share"].eq(0.10)
    ].copy()
    fig, axes = plt.subplots(1, 3, figsize=(17.0, 4.8))

    estimators = ["delta_e_audit_override", "delta_e_audit_proxy"]
    colors = ["#1f4e79", "#c1462c"]
    for estimator, color in zip(estimators, colors):
        group = correctly_specified[correctly_specified["estimator"].eq(estimator)]
        summary = group.groupby("cases_per_period", as_index=False)["rmse"].mean()
        axes[0].plot(
            summary["cases_per_period"],
            summary["rmse"],
            marker="o",
            lw=2,
            color=color,
            label=estimator.replace("_", " "),
        )
    axes[0].set_xscale("log")
    axes[0].set_xlabel("Cases per period, log scale")
    axes[0].set_ylabel("Mean RMSE of engagement trend")
    axes[0].set_title("RMSE under stated assumptions")
    axes[0].legend(fontsize=8)

    check_focus = checks[checks["audit_share"].eq(0.10)].copy()
    correct_checks = check_focus[~check_focus["scenario"].str.contains("misspecification")]
    maximum_boundary = correct_checks["audit_override_boundary_rate"].max()
    axes[0].text(
        0.03,
        0.04,
        f"Max audit + override boundary rate: {maximum_boundary:.1%}",
        transform=axes[0].transAxes,
        fontsize=7.5,
        bbox={"facecolor": "white", "edgecolor": "#bbbbbb", "alpha": 0.9},
    )

    for estimator, color in zip(estimators, colors):
        group = correctly_specified[correctly_specified["estimator"].eq(estimator)]
        summary = group.groupby("cases_per_period", as_index=False)["coverage_95"].mean()
        axes[1].plot(
            summary["cases_per_period"],
            summary["coverage_95"],
            marker="o",
            lw=2,
            color=color,
            label=estimator.replace("_", " "),
        )
    axes[1].set_xscale("log")
    axes[1].set_ylim(0.0, 1.02)
    axes[1].set_xlabel("Cases per period, log scale")
    axes[1].axhline(0.95, color="#555555", ls="--", lw=1, label="nominal 95%")
    axes[1].set_ylabel("Empirical interval coverage")
    axes[1].set_title("Approximate 95% coverage")
    axes[1].legend(fontsize=8)

    styles = {
        "stable_negative_control": ("#2b8a3e", "-"),
        "detection_drift_misspecification": ("#8c6d31", "--"),
        "proxy_drift_misspecification": ("#4d4d4d", ":"),
    }
    for scenario, (color, linestyle) in styles.items():
        group = check_focus[check_focus["scenario"].eq(scenario)]
        axes[2].plot(
            group["cases_per_period"],
            group["override_predictive_rejection_rate_05"],
            marker="o",
            lw=2,
            ls=linestyle,
            color=color,
            label=scenario.replace("_", " "),
        )
    axes[2].set_xscale("log")
    axes[2].set_ylim(0.0, 1.02)
    axes[2].set_xlabel("Cases per period, log scale")
    axes[2].set_ylabel("Predictive-check rejection rate")
    axes[2].axhline(0.05, color="#777777", ls="--", lw=1, label="nominal .05")
    axes[2].set_title("Independent channels flag model incompatibility")
    axes[2].legend(fontsize=7)

    for ax in axes:
        ax.grid(alpha=0.25)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(
        "10% audit share; RMSE and coverage average four correctly specified scenarios",
        fontsize=11,
        fontweight="bold",
    )
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_sensitivity(sensitivity: pd.DataFrame, output: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), sharey=True, constrained_layout=True)
    for ax, q in zip(axes, sorted(sensitivity["disengaged_override"].unique())):
        group = sensitivity[sensitivity["disengaged_override"].eq(q)]
        scatter = ax.scatter(
            group["detection"],
            group["equivalent_e_end"],
            c=group["false_alarm"],
            cmap="plasma",
            vmin=sensitivity["false_alarm"].min(),
            vmax=sensitivity["false_alarm"].max(),
            s=85,
            edgecolor="white",
        )
        infeasible = group[~group["feasible_equivalent"]]
        if not infeasible.empty:
            ax.scatter(
                infeasible["detection"],
                infeasible["equivalent_e_end"],
                marker="x",
                color="black",
                s=70,
                label="Infeasible implied engagement",
            )
        ax.set_title(f"q = {q:.02f}")
        ax.set_xlabel("Detection d")
        ax.axhline(0.0, color="#555555", lw=0.8)
        ax.set_ylim(-0.35, 1.0)
        ax.grid(alpha=0.25)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Equivalent end engagement")
    handles, labels = axes[-1].get_legend_handles_labels()
    if handles:
        axes[-1].legend(handles, labels, fontsize=7, loc="lower right")
    fig.colorbar(scatter, ax=axes, label="False alarm f", shrink=0.82, pad=0.02)
    fig.suptitle("Sensitivity of the equivalent disengagement path", fontweight="bold")
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_proxy_calibration(sensitivity: pd.DataFrame, output: Path) -> None:
    pivot = sensitivity.pivot(
        index="actual_proxy_sensitivity",
        columns="actual_proxy_false_positive",
        values="expected_bias",
    )
    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    image_plot = ax.imshow(
        pivot.to_numpy(),
        origin="lower",
        aspect="auto",
        cmap="coolwarm",
        vmin=-max(abs(pivot.to_numpy().min()), abs(pivot.to_numpy().max())),
        vmax=max(abs(pivot.to_numpy().min()), abs(pivot.to_numpy().max())),
    )
    ax.set_xticks(range(len(pivot.columns)), [f"{v:.02f}" for v in pivot.columns])
    ax.set_yticks(range(len(pivot.index)), [f"{v:.02f}" for v in pivot.index])
    ax.set_xlabel("Actual proxy false-positive rate")
    ax.set_ylabel("Actual proxy sensitivity")
    ax.set_title("Bias when proxy calibration is assumed fixed")
    for row in range(pivot.shape[0]):
        for column in range(pivot.shape[1]):
            ax.text(
                column,
                row,
                f"{pivot.iloc[row, column]:+.03f}",
                ha="center",
                va="center",
                fontsize=9,
            )
    fig.colorbar(image_plot, ax=ax, label="Expected bias in engagement trend")
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def run_self_checks(
    config: StudyConfig,
    scenarios: dict[str, pd.DataFrame],
    surface: pd.DataFrame,
) -> dict[str, bool | float | int]:
    a = scenarios["improvement_only"]
    b = scenarios["exact_equivalent_disengagement"]
    equal_paths = bool(
        np.allclose(
            a["expected_override_rate"],
            b["expected_override_rate"],
            atol=1e-12,
        )
    )
    b_bounds = bool(b["engagement"].between(0.0, 1.0).all())
    e_probe = np.linspace(0.0, 1.0, 11)
    z_probe = proxy_rate(e_probe, config.proxy_sensitivity, config.proxy_false_positive)
    e_recovered = (
        z_probe - config.proxy_false_positive
    ) / (config.proxy_sensitivity - config.proxy_false_positive)
    proxy_inversion = bool(np.allclose(e_probe, e_recovered, atol=1e-12))

    nearest_a = surface.iloc[
        ((surface["p_end"] - 0.88) ** 2 + (surface["e_end"] - 0.90) ** 2).argmin()
    ]
    nearest_b = surface.iloc[
        (
            (surface["p_end"] - 0.60) ** 2
            + (surface["e_end"] - float(b["engagement"].iloc[-1])) ** 2
        ).argmin()
    ]
    return {
        "exact_expected_paths_equal": equal_paths,
        "equivalent_engagement_in_unit_interval": b_bounds,
        "proxy_inversion_exact_at_population_values": proxy_inversion,
        "equivalent_engagement_end": float(b["engagement"].iloc[-1]),
        "delta_loglik_near_improvement_endpoint": float(nearest_a["delta_log_likelihood"]),
        "delta_loglik_near_disengagement_endpoint": float(nearest_b["delta_log_likelihood"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    config = StudyConfig.from_json(args.config) if args.config else StudyConfig()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(config.master_seed)

    scenarios = build_scenarios(config)
    scenario_paths = pd.concat(scenarios.values(), ignore_index=True)
    a_rate = scenarios["improvement_only"]["expected_override_rate"].to_numpy()
    selected_rates = [a_rate[0], a_rate[len(a_rate) // 2], a_rate[-1]]
    curves = identification_curves(config, selected_rates)
    sweep = parameter_sweep(config, a_rate, rng)
    surface = likelihood_surface(config, a_rate)
    mc = monte_carlo(config, scenarios)
    recovery = recovery_summary(mc)
    regimes = trend_regime_summary(mc)
    assumption_checks = assumption_check_summary(mc)
    sensitivity = sensitivity_grid(config)
    proxy_sensitivity = proxy_calibration_sensitivity(config)
    checks = run_self_checks(config, scenarios, surface)

    scenario_paths.to_csv(output / "scenario_paths.csv", index=False)
    curves.to_csv(output / "identification_curves.csv", index=False)
    sweep.to_csv(output / "equivalence_sweep.csv", index=False)
    surface.to_csv(output / "override_only_likelihood_surface.csv", index=False)
    mc.to_csv(output / "monte_carlo_replications.csv", index=False)
    recovery.to_csv(output / "recovery_summary.csv", index=False)
    regimes.to_csv(output / "trend_regime_summary.csv", index=False)
    assumption_checks.to_csv(output / "assumption_check_summary.csv", index=False)
    sensitivity.to_csv(output / "sensitivity_summary.csv", index=False)
    proxy_sensitivity.to_csv(output / "proxy_calibration_sensitivity.csv", index=False)

    plot_scenarios(scenario_paths, output / "figure_1_scenarios.png")
    plot_equivalence(curves, sweep, output / "figure_2_equivalence.png")
    plot_likelihood(
        surface,
        output / "figure_3_likelihood_ridge.png",
        float(scenarios["exact_equivalent_disengagement"]["engagement"].iloc[-1]),
    )
    plot_recovery(recovery, assumption_checks, output / "figure_4_recovery.png")
    plot_sensitivity(sensitivity, output / "figure_5_sensitivity.png")
    plot_proxy_calibration(proxy_sensitivity, output / "figure_6_proxy_calibration.png")

    manifest = {
        "config": asdict(config),
        "checks": checks,
        "accepted_equivalence_paths": int(len(sweep)),
        "monte_carlo_rows": int(len(mc)),
        "software_versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "matplotlib": matplotlib.__version__,
            "scipy": scipy.__version__,
        },
        "all_fits_converged": bool(
            mc["audit_override_converged"].all()
            and mc["audit_proxy_converged"].all()
        ),
        "maximum_boundary_rate": {
            "audit_override_any_cell": float(
                assumption_checks["audit_override_boundary_rate"].max()
            ),
            "audit_proxy_any_cell": float(
                assumption_checks["audit_proxy_boundary_rate"].max()
            ),
        },
        "prohibited_interpretation": (
            "These illustrative simulations do not estimate the prevalence of "
            "reviewer disengagement in any real deployment."
        ),
    }
    (output / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    if not all(
        checks[key]
        for key in [
            "exact_expected_paths_equal",
            "equivalent_engagement_in_unit_interval",
            "proxy_inversion_exact_at_population_values",
        ]
    ):
        raise RuntimeError(f"Self-check failed: {checks}")

    print(json.dumps(manifest, indent=2))
    print(f"Wrote outputs to {output}")


if __name__ == "__main__":
    main()
