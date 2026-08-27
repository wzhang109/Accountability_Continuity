import unittest

import numpy as np

from simulation_v2 import (
    StudyConfig,
    build_scenarios,
    engagement_from_rate,
    fit_audit_override,
    fit_audit_proxy,
    label_detected_trend_regime,
    likelihood_surface,
    monte_carlo,
    override_predictive_check,
    override_rate,
    proxy_rate,
    sensitivity_grid,
    simulate_aggregate_observations,
    trend_change_with_se,
)


class IdentificationTests(unittest.TestCase):
    def setUp(self):
        self.config = StudyConfig(monte_carlo_replications=5, sweep_draws=100)

    def test_exact_equivalent_expected_paths(self):
        scenarios = build_scenarios(self.config)
        a = scenarios["improvement_only"]["expected_override_rate"].to_numpy()
        b = scenarios["exact_equivalent_disengagement"][
            "expected_override_rate"
        ].to_numpy()
        np.testing.assert_allclose(a, b, atol=1e-12)

    def test_population_engagement_recovery_with_known_accuracy(self):
        p = np.linspace(0.55, 0.90, 20)
        e = np.linspace(0.25, 0.95, 20)
        r = override_rate(
            p,
            e,
            self.config.detection,
            self.config.false_alarm,
            self.config.disengaged_override,
        )
        recovered = engagement_from_rate(
            r,
            p,
            self.config.detection,
            self.config.false_alarm,
            self.config.disengaged_override,
        )
        np.testing.assert_allclose(e, recovered, atol=1e-12)

    def test_population_proxy_correction(self):
        e = np.linspace(0.0, 1.0, 21)
        z = proxy_rate(
            e,
            self.config.proxy_sensitivity,
            self.config.proxy_false_positive,
        )
        recovered = (
            z - self.config.proxy_false_positive
        ) / (
            self.config.proxy_sensitivity - self.config.proxy_false_positive
        )
        np.testing.assert_allclose(e, recovered, atol=1e-12)

    def test_equivalent_engagement_is_feasible(self):
        scenario = build_scenarios(self.config)["exact_equivalent_disengagement"]
        self.assertTrue(scenario["engagement"].between(0.0, 1.0).all())
        self.assertAlmostEqual(scenario["engagement"].iloc[0], 0.90, places=12)
        self.assertAlmostEqual(scenario["engagement"].iloc[-1], 0.2917241379, places=8)

    def test_trend_estimator_uses_end_to_end_scale(self):
        values = np.linspace(0.20, 0.70, 24)
        estimate, standard_error = trend_change_with_se(
            values, np.full(24, 0.01)
        )
        self.assertAlmostEqual(estimate, 0.50, places=12)
        self.assertGreater(standard_error, 0.0)

    def test_constrained_fits_recover_population_paths(self):
        scenario = build_scenarios(self.config)["improvement_only"]
        n = 1_000_000
        n_audit = 250_000
        n_proxy = 250_000
        audit_override = fit_audit_override(
            scenario["model_accuracy"].to_numpy() * n_audit,
            n_audit,
            scenario["expected_override_rate"].to_numpy() * n,
            n,
            self.config,
        )
        audit_proxy = fit_audit_proxy(
            scenario["model_accuracy"].to_numpy() * n_audit,
            n_audit,
            scenario["expected_proxy_rate"].to_numpy() * n_proxy,
            n_proxy,
            self.config,
        )
        self.assertAlmostEqual(float(audit_override["delta_p"]), 0.28, places=4)
        self.assertAlmostEqual(float(audit_override["delta_e"]), 0.00, places=4)
        self.assertAlmostEqual(float(audit_proxy["delta_p"]), 0.28, places=4)
        self.assertAlmostEqual(float(audit_proxy["delta_e"]), 0.00, places=4)

    def test_independent_channels_flag_detection_drift(self):
        scenario = build_scenarios(self.config)["detection_drift_misspecification"]
        n = 100_000
        n_audit = 25_000
        n_proxy = 25_000
        fit = fit_audit_proxy(
            scenario["model_accuracy"].to_numpy() * n_audit,
            n_audit,
            scenario["expected_proxy_rate"].to_numpy() * n_proxy,
            n_proxy,
            self.config,
        )
        _, p_value = override_predictive_check(
            fit,
            scenario["expected_override_rate"].to_numpy() * n,
            n,
            self.config,
        )
        self.assertLess(p_value, 1e-8)

    def test_seed_reproduces_aggregate_draws(self):
        scenario = build_scenarios(self.config)["mixed"]
        first = simulate_aggregate_observations(
            scenario, self.config, 250, 0.10, np.random.default_rng(7)
        )
        second = simulate_aggregate_observations(
            scenario, self.config, 250, 0.10, np.random.default_rng(7)
        )
        for key in ["override_count", "accuracy_count", "proxy_count"]:
            np.testing.assert_array_equal(first[key], second[key])

    def test_both_constructed_endpoints_are_high_fit(self):
        scenarios = build_scenarios(self.config)
        a = scenarios["improvement_only"]
        b = scenarios["exact_equivalent_disengagement"]
        surface = likelihood_surface(
            self.config,
            a["expected_override_rate"].to_numpy(),
            p_grid=np.array([0.60, 0.88]),
            e_grid=np.array([float(b["engagement"].iloc[-1]), 0.90]),
        )
        selected = surface[
            ((surface["p_end"].eq(0.60)) & surface["e_end"].eq(float(b["engagement"].iloc[-1])))
            | ((surface["p_end"].eq(0.88)) & surface["e_end"].eq(0.90))
        ]
        self.assertTrue((selected["delta_log_likelihood"] < 0.2).all())

    def test_sensitivity_contains_infeasible_cells(self):
        self.assertGreater((~sensitivity_grid(self.config)["feasible_equivalent"]).sum(), 0)

    def test_monte_carlo_schema_and_row_count(self):
        config = StudyConfig(
            monte_carlo_replications=2,
            sample_sizes=(250,),
            audit_shares=(0.10,),
            sweep_draws=10,
        )
        result = monte_carlo(config, build_scenarios(config))
        self.assertEqual(len(result), 12)
        self.assertIn("override_predictive_check_p", result.columns)

    def test_non_target_direction_is_not_labeled_stable(self):
        label = label_detected_trend_regime(
            delta_p=-0.20,
            se_p=0.01,
            delta_e=0.00,
            se_e=0.01,
        )
        self.assertEqual(label, "other_detected_trend")


if __name__ == "__main__":
    unittest.main()
