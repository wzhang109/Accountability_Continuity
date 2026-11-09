"""Checks against hand-worked fixtures; no human observations."""
import copy
from collections import Counter
import unittest

from assignment import ARMS, build, check, eligible, FAMILIES
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
        self.assertEqual(a["detection"]["explanation_unscored_with_observed_decision"], 4)

    def test_both_underlying_dispositions_and_recommendation_crosses(self):
        d = build()
        allocations = {a["slot_id"]: a["arm"] for a in d["allocation"]}
        family_rules = {
            "file_release": (2, "at_most"),
            "training_access": (80, "at_least"),
            "invoice_route": (500, "at_most"),
            "equipment_dispatch": (60, "at_least"),
            "archive_publish": (0, "at_most"),
            "stock_transfer": (10, "at_least"),
        }
        dispositions = {slot: set() for slot in allocations}
        cells = Counter()
        for k in d["answer_key"]:
            threshold, operator = family_rules[k["family"]]
            should_proceed = k["value"] <= threshold if operator == "at_most" else k["value"] >= threshold
            supported = (k["recommended_disposition"] == "proceed") == should_proceed
            self.assertEqual(k["draft_valid"], supported)
            self.assertEqual(k["correct_action"], "pass" if supported else "return")
            dispositions[k["slot_id"]].add(should_proceed)
            cells[allocations[k["slot_id"]], k["family"], k["recommended_disposition"], supported] += 1
        for values in dispositions.values():
            self.assertEqual(values, {False, True})
        for arm in ARMS:
            for family in family_rules:
                for recommendation in ("proceed", "hold"):
                    for supported in (False, True):
                        self.assertEqual(cells[arm, family, recommendation, supported], 3)

    def test_all_family_boundaries(self):
        for family in FAMILIES:
            with self.subTest(family=family[0]):
                self.assertTrue(eligible(family, family[3]))
                self.assertFalse(eligible(family, family[4]))

    def test_rules_require_proceed_when_conditions_hold(self):
        d = build()
        for family in FAMILIES:
            with self.subTest(family=family[0]):
                # A necessary-only rule cannot establish that holding is wrong.
                self.assertTrue(family[1].startswith("If "))
                self.assertTrue(family[1].endswith(". Otherwise, hold."))
                self.assertNotIn("only if", family[1])
                holds = [k for k in d["answer_key"]
                         if k["family"] == family[0] and k["recommended_disposition"] == "hold"]
                self.assertEqual({k["draft_valid"] for k in holds}, {False, True})
                for k in holds:
                    self.assertEqual(k["correct_action"], "return" if eligible(family, k["value"]) else "pass")

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

    def test_reject_invalid_design_labels(self):
        d, r = fixture()
        bad = copy.deepcopy(d)
        bad["allocation"][0]["arm"] = "other"
        with self.assertRaisesRegex(ValueError, "unknown arm"):
            summarize(bad, r)
        for value in (None, 0, 1, "false"):
            bad = copy.deepcopy(d)
            bad["answer_key"][0]["draft_valid"] = value
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "draft_valid must be boolean"):
                    summarize(bad, r)

    def test_explanation_scoring_does_not_change_decision_credit(self):
        d, r = fixture()
        for score in (0, 1):
            unscored = summarize(d, r)
            scored = summarize(d, [{**x, "explanation_score": score} for x in r])
            for arm in scored["arms"].values():
                for name in ("detection", "false_return"):
                    self.assertEqual(arm[name]["explanation_unscored_with_observed_decision"], 0)
            for result in (unscored, scored):
                for reviewer in result["reviewers"]:
                    for name in ("detection", "false_return"):
                        reviewer[name].pop("explanation_unscored_with_observed_decision")
                for arm in result["arms"].values():
                    for name in ("detection", "false_return"):
                        arm[name].pop("explanation_unscored_with_observed_decision")
            self.assertEqual(scored, unscored)


if __name__ == "__main__":
    unittest.main()
