"""Analysis plumbing for fictional records; not an efficacy estimate."""
from collections import defaultdict
import json
from pathlib import Path
from statistics import mean

from assignment import ARMS, build, check


def summarize(design, responses):
    allocations = {r["slot_id"]: r["arm"] for r in design["allocation"]}
    if len(allocations) != len(design["allocation"]):
        raise ValueError("duplicate slot")
    keys = {(k["slot_id"], k["item_id"]): k for k in design["answer_key"]}
    if len(keys) != len(design["answer_key"]):
        raise ValueError("duplicate answer key")
    if any(s not in allocations for s, _ in keys):
        raise ValueError("unallocated key")
    indexed = {}
    for r in responses:
        token = r["slot_id"], r["item_id"]
        if token not in keys or token in indexed:
            raise ValueError("unknown or duplicate response")
        if r["decision"] not in (None, "pass", "return"):
            raise ValueError("invalid decision")
        if type(r["rendering_ok"]) is not bool:
            raise ValueError("rendering_ok must be boolean")
        if r["explanation_score"] not in (None, 0, 1):
            raise ValueError("invalid explanation score")
        indexed[token] = r
    reviewers = []
    for slot, arm in allocations.items():
        summary = {"slot_id": slot, "arm": arm}
        for valid, name in ((False, "detection"), (True, "false_return")):
            tokens = [t for t, k in keys.items() if t[0] == slot and k["draft_valid"] == valid]
            observed = []
            render_failed = 0
            explanation_missing = 0
            for token in tokens:
                r = indexed.get(token)
                if r is None:
                    continue
                render_failed += not r["rendering_ok"]
                if r["rendering_ok"] and r["decision"] is not None:
                    observed.append(r)
                    explanation_missing += r["explanation_score"] is None
            n, n_observed = len(tokens), len(observed)
            returns = sum(r["decision"] == "return" for r in observed)
            missing = n - n_observed
            summary[name] = {
                "assigned": n, "observed": n_observed, "returns": returns,
                "missing_or_unusable": missing, "render_failed": render_failed,
                "rate_observed": returns / n_observed if n_observed else None,
                "lower_all_assigned": returns / n if n else None,
                "upper_all_assigned": (returns + missing) / n if n else None,
                "explanation_missing_with_observed_decision": explanation_missing,
            }
        reviewers.append(summary)
    arms = {}
    for arm in ARMS:
        rows = [r for r in reviewers if r["arm"] == arm]
        arms[arm] = {}
        for name in ("detection", "false_return"):
            cells = [r[name] for r in rows]
            rates = [c["rate_observed"] for c in cells if c["rate_observed"] is not None]
            observed = sum(c["observed"] for c in cells)
            # Do not silently drop an all-missing reviewer from the arm mean.
            arms[arm][name] = {
                "reviewers": len(cells), "reviewers_with_observations": len(rates),
                "mean_reviewer_rate": mean(rates) if cells and len(rates) == len(cells) else None,
                "pooled_item_rate_diagnostic": sum(c["returns"] for c in cells) / observed if observed else None,
                "lower_all_assigned": mean(c["lower_all_assigned"] for c in cells) if cells and all(c["assigned"] for c in cells) else None,
                "upper_all_assigned": mean(c["upper_all_assigned"] for c in cells) if cells and all(c["assigned"] for c in cells) else None,
                "assigned": sum(c["assigned"] for c in cells),
                "observed": observed,
                "missing_or_unusable": sum(c["missing_or_unusable"] for c in cells),
                "render_failed": sum(c["render_failed"] for c in cells),
                "explanation_missing_with_observed_decision": sum(c["explanation_missing_with_observed_decision"] for c in cells),
            }
    contrasts = {}
    for name in ("detection", "false_return"):
        a, b = arms["visible"][name], arms["one_click"][name]
        av, bv = a["mean_reviewer_rate"], b["mean_reviewer_rate"]
        lo, hi = a["lower_all_assigned"], a["upper_all_assigned"]
        blo, bhi = b["lower_all_assigned"], b["upper_all_assigned"]
        contrasts[name] = {
            "visible_minus_one_click_observed": av-bv if av is not None and bv is not None else None,
            "lower_all_assigned": lo-bhi if lo is not None and bhi is not None else None,
            "upper_all_assigned": hi-blo if hi is not None and blo is not None else None,
        }
    return {"kind": "SYNTHETIC_ANALYSIS_CHECK_NOT_HUMAN_RESULTS",
            "reviewers": reviewers, "arms": arms, "contrasts": contrasts}


def fixture():
    full = build()
    check(full)
    slots = {a: [r["slot_id"] for r in full["allocation"] if r["arm"] == a][:2] for a in ARMS}
    selected = set(slots["visible"] + slots["one_click"])
    design = dict(full)
    for field in ("allocation", "tasks", "answer_key"):
        design[field] = [r for r in full[field] if r["slot_id"] in selected]
    plans = {
        slots["visible"][0]: {False: ["return", "return", "pass"], True: ["return", "pass", None]},
        slots["visible"][1]: {False: ["return", None, None], True: ["pass", "pass", "pass"]},
        slots["one_click"][0]: {False: ["return", "pass", "pass"], True: ["pass", "pass", "pass"]},
        slots["one_click"][1]: {False: ["return", "pass", None], True: ["return", "pass", None]},
    }
    used = defaultdict(int)
    responses = []
    for k in design["answer_key"]:
        slot, valid = k["slot_id"], k["draft_valid"]
        decision = plans[slot][valid][used[slot, valid]]
        used[slot, valid] += 1
        responses.append({"slot_id": slot, "item_id": k["item_id"], "decision": decision,
                          "rendering_ok": True, "explanation_score": None})
    return design, responses


if __name__ == "__main__":
    design, responses = fixture()
    result = summarize(design, responses)
    out = Path(__file__).parent / "generated"
    out.mkdir(exist_ok=True)
    (out / "synthetic_responses.json").write_text(json.dumps(responses, indent=2)+"\n")
    (out / "synthetic_analysis.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"kind": result["kind"], "arms": result["arms"], "contrasts": result["contrasts"]}, indent=2))
