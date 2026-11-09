import tempfile
import unittest
from pathlib import Path

from verify_reproduction import compare_csv


class ReproductionReportTests(unittest.TestCase):
    def compare(self, value):
        with tempfile.TemporaryDirectory() as directory:
            old, new = Path(directory) / "reference.csv", Path(directory) / "rerun.csv"
            old.write_text("scenario,mean_estimate\nknown,0.01\n")
            new.write_text(f"scenario,mean_estimate\nknown,{value}\n")
            return compare_csv(old, new)

    def test_within_tolerance_rounding_is_reported_as_match(self):
        report = self.compare(0.010000000001)
        self.assertTrue(report["matches_within_tolerance"])
        self.assertEqual(report["numeric_failures"], [])

    def test_strict_failure_retains_difference_and_row_keys(self):
        report = self.compare(0.010000005)
        self.assertFalse(report["matches_within_tolerance"])
        failure = report["numeric_failures"][0]
        self.assertEqual(failure["cells_outside_tolerance"], 1)
        self.assertEqual(failure["examples"][0]["row_keys"], {"scenario": "known"})
        example = failure["examples"][0]
        self.assertGreater(example["absolute_difference"], example["allowed_absolute_difference"])


if __name__ == "__main__":
    unittest.main()
