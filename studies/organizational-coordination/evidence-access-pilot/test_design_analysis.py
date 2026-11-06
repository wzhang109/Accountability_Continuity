"""Checks against hand-worked fixtures; no human observations."""
import copy
import unittest

from assignment import build, check, eligible, FAMILIES
from analysis import fixture, summarize


class DesignChecks(unittest.TestCase):
    def test_seeds_and_boundary(self):
        for seed in range(100):
            check(build(seed))
        self.assertEqual(build(77), build(77))
        self.assertNotEqual(build(77), build(78))
        self.assertTrue(eligible(FAMILIES[0], 2))
        self.assertFalse(eligible(FAMILIES[0], 3))

    def test_hand_calculation(self):
        d, r = fixture()
        out = summarize(d, r)
        a, b = out["arms"]["visible"], out["arms"]["one_click"]
        self.assertAlmostEqual(a["detection"]["mean_reviewer_rate"], 5/6)
        self.assertAlmostEqual(b["detection"]["mean_reviewer_rate"], 5/12)
        self.assertAlmostEqual(a["detection"]["pooled_item_rate_diagnostic"], 3/4)
        self.assertAlmostEqual(b["detection"]["pooled_item_rate_diagnostic"], 2/5)
        for arm in (a, b):
            self.assertEqual(arm["false_return"]["mean_reviewer_rate"], 1/4)
        diff = out["contrasts"]["detection"]
        self.assertAlmostEqual(diff["visible_minus_one_click_observed"], 5/12)
        self.assertAlmostEqual(diff["lower_all_assigned"], 0)
        self.assertAlmostEqual(diff["upper_all_assigned"], 1/2)
        self.assertEqual(a["detection"]["missing_or_unusable"], 2)
        self.assertEqual(b["detection"]["missing_or_unusable"], 1)
        self.assertEqual(a["detection"]["explanation_missing_with_observed_decision"], 4)

    def test_missing_row_is_not_a_pass(self):
        d, r = fixture()
        token = next(x for x in r if x["decision"] is None)
        self.assertEqual(summarize(d, r), summarize(d, [x for x in r if x is not token]))

    def test_all_missing_and_render_failure(self):
        d, r = fixture()
        target = d["allocation"][0]["slot_id"]
        arm = d["allocation"][0]["arm"]
        remaining = [x for x in r if x["slot_id"] != target]
        cell = summarize(d, remaining)["arms"][arm]["detection"]
        self.assertIsNone(cell["mean_reviewer_rate"])
        bad = copy.deepcopy(r)
        bad[0]["rendering_ok"] = False
        out = summarize(d, bad)
        self.assertEqual(sum(a["detection"]["render_failed"] + a["false_return"]["render_failed"] for a in out["arms"].values()), 1)
        empty = summarize(d, [])
        self.assertIsNone(empty["contrasts"]["detection"]["visible_minus_one_click_observed"])
        self.assertEqual(empty["contrasts"]["detection"]["lower_all_assigned"], -1)
        self.assertEqual(empty["contrasts"]["detection"]["upper_all_assigned"], 1)

    def test_extreme_decision_strategies(self):
        d, r = fixture()
        for decision, expected in (("return", 1), ("pass", 0)):
            altered = [{**x, "decision": decision} for x in r]
            out = summarize(d, altered)
            for arm in out["arms"].values():
                self.assertEqual(arm["detection"]["mean_reviewer_rate"], expected)
                self.assertEqual(arm["false_return"]["mean_reviewer_rate"], expected)

    def test_reject_invalid_records(self):
        d, r = fixture()
        for broken in (r+[r[0]], [{**r[0], "item_id": "unassigned"}], [{**r[0], "decision": "yes"}]):
            with self.assertRaises(ValueError):
                summarize(d, broken)


if __name__ == "__main__":
    unittest.main()
