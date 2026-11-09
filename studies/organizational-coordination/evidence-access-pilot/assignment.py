"""Fictional design slots, not enrollment or participant data. Python 3 stdlib."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random

ARMS = ("visible", "one_click")
FAMILIES = (
    ("file_release", "If independent review is complete and outstanding discrepancies are two or fewer, release the file. Otherwise, hold.", "Independent review complete; outstanding discrepancies: {value}.", 2, 3, "at_most", 2),
    ("training_access", "If training is complete and the assessment score is at least 80, grant access. Otherwise, hold.", "Training complete; assessment score: {value}.", 80, 79, "at_least", 80),
    ("invoice_route", "If supplier approval is complete and the invoice amount is no more than 500 fictional units, route the invoice for payment. Otherwise, hold.", "Supplier approval complete; invoice amount: {value} fictional units.", 500, 501, "at_most", 500),
    ("equipment_dispatch", "If inspection is complete and the battery charge is at least 60 percent, dispatch the equipment. Otherwise, hold.", "Inspection complete; battery charge: {value} percent.", 60, 59, "at_least", 60),
    ("archive_publish", "If consent is recorded and there are zero unresolved redactions, publish the archive entry. Otherwise, hold.", "Consent recorded; unresolved redactions: {value}.", 0, 1, "at_most", 0),
    ("stock_transfer", "If the seal check is complete and at least 10 units remain after transfer, transfer the stock batch. Otherwise, hold.", "Seal check complete; remaining units after transfer: {value}.", 10, 9, "at_least", 10),
)


def eligible(family, value):
    """The named completion condition is always true in these draft items."""
    return value <= family[6] if family[5] == "at_most" else value >= family[6]


def build(seed=20261106):
    rng = random.Random(seed)
    allocation, tasks, key = [], [], []
    base = list(range(6))
    rng.shuffle(base)
    # Two complete blocks: 24 fictional reviewer slots, 12 in each interface.
    # Within each block: six order rotations per interface, three valid drafts
    # per family per interface, and three valid/three invalid per reviewer.
    for block in range(2):
        slots = [(arm, rotation) for arm in ARMS for rotation in range(6)]
        rng.shuffle(slots)
        for arm, rotation in slots:
            slot = f"design-{len(allocation)+1:02d}"
            allocation.append({"slot_id": slot, "arm": arm, "block": block})
            for position in range(6):
                i = base[(position + rotation) % 6]
                f = FAMILIES[i]
                # A three-family window keeps validity balanced without making
                # every underlying record in a slot share one disposition.
                valid = (i + rotation + 3 * block) % 6 < 3
                recommended = "proceed" if (i + block) % 2 == 0 else "hold"
                should_proceed = (recommended == "proceed") == valid
                value = f[3] if should_proceed else f[4]
                assert eligible(f, value) == should_proceed
                item = hashlib.sha256(f"{seed}:{slot}:{position}".encode()).hexdigest()[:16]
                tasks.append({"slot_id": slot, "item_id": item, "position": position+1,
                              "source_title": "Fictional local rule", "source_location": "Paragraph 1",
                              "source_text": f[1], "record": f[2].format(value=value),
                              "recommendation": recommended,
                              "prompt": "Pass this recommendation onward, or return the recommendation for correction?"})
                key.append({"slot_id": slot, "item_id": item, "family": f[0],
                            "draft_valid": valid, "correct_action": "pass" if valid else "return",
                            "recommended_disposition": recommended, "value": value,
                            "rule_operator": f[5], "threshold": f[6]})
    return {"kind": "FICTIONAL_DESIGN_ONLY", "seed": seed,
            "allocation": allocation, "tasks": tasks, "answer_key": key}


def check(design):
    allocations = {a["slot_id"]: a for a in design["allocation"]}
    assert len(allocations) == len(design["allocation"]) == 24
    assert Counter(a["arm"] for a in allocations.values()) == {a: 12 for a in ARMS}
    task_ids = [(t["slot_id"], t["item_id"]) for t in design["tasks"]]
    key_ids = [(k["slot_id"], k["item_id"]) for k in design["answer_key"]]
    assert len(set(task_ids)) == len(task_ids) == 144 and set(task_ids) == set(key_ids)
    by_key = {(k["slot_id"], k["item_id"]): k for k in design["answer_key"]}
    families, positions, per_slot = Counter(), Counter(), Counter()
    recommendation_cells = Counter()
    family_by_name = {f[0]: f for f in FAMILIES}
    for t in design["tasks"]:
        assert "draft_valid" not in t and "correct_action" not in t and "family" not in t
        k = by_key[t["slot_id"], t["item_id"]]
        f = family_by_name[k["family"]]
        assert t["recommendation"] == k["recommended_disposition"]
        assert k["draft_valid"] == ((t["recommendation"] == "proceed") == eligible(f, k["value"]))
        assert k["correct_action"] == ("pass" if k["draft_valid"] else "return")
        arm = allocations[t["slot_id"]]["arm"]
        families[arm, k["family"], k["draft_valid"]] += 1
        recommendation_cells[arm, k["family"], k["recommended_disposition"], k["draft_valid"]] += 1
        positions[arm, t["position"], k["draft_valid"]] += 1
        per_slot[t["slot_id"], k["draft_valid"]] += 1
    assert all(families[a, f[0], v] == 6 for a in ARMS for f in FAMILIES for v in (False, True))
    assert all(positions[a, p, v] == 6 for a in ARMS for p in range(1, 7) for v in (False, True))
    assert all(per_slot[s, v] == 3 for s in allocations for v in (False, True))
    assert all(recommendation_cells[a, f[0], r, v] == 3
               for a in ARMS for f in FAMILIES for r in ("proceed", "hold") for v in (False, True))
    for s in allocations:
        rows = [k for k in design["answer_key"] if k["slot_id"] == s]
        assert len({k["family"] for k in rows}) == 6  # never both pair variants
        assert Counter(k["recommended_disposition"] for k in rows) == {"proceed": 3, "hold": 3}
        assert {eligible(family_by_name[k["family"]], k["value"]) for k in rows} == {False, True}
    return {"kind": "FICTIONAL_DESIGN_CHECK", "seed": design["seed"],
            "slots": 24, "tasks": 144, "slots_per_arm": 12,
            "per_arm_family_validity_cell": 6, "per_arm_position_validity_cell": 6,
            "per_arm_family_recommendation_validity_cell": 3,
            "underlying_dispositions_per_slot": 2,
            "valid_and_invalid_per_slot": [3, 3], "checks": "passed"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261106)
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "generated")
    args = parser.parse_args()
    design = build(args.seed)
    report = check(design)
    args.out.mkdir(parents=True, exist_ok=True)
    for name in ("allocation", "tasks", "answer_key"):
        (args.out / f"{name}.json").write_text(json.dumps(design[name], indent=2)+"\n")
    (args.out / "balance.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
