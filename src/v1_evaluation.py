"""Blind evaluation for the synthetic v1 uncertainty-aware simulation."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import cast

from v1 import STATES, SyntheticCase, evaluate_case

DATA_PATH = Path(__file__).parents[1] / "data" / "v1_test_cases.csv"
RESULT_PATH = Path(__file__).parents[1] / "data" / "v1_evaluation_results.csv"
REFERENCE_ORDER = {"Low": 0, "Medium": 1, "High": 2}
# Synthetic relative cost for routed decisions only. Rows: reference state.
ERROR_COSTS = {
    "Low": {"Low": 0, "Medium": 1, "High": 2},
    "Medium": {"Low": 2, "Medium": 0, "High": 1},
    "High": {"Low": 5, "Medium": 3, "High": 0},
}


def load_cases(path: Path = DATA_PATH) -> list[tuple[SyntheticCase, str, str]]:
    """Load labelled synthetic cases; labels remain out of the decision function."""
    required = {
        "case_id",
        "condition_evidence",
        "duration_evidence",
        "severity_evidence",
        "information_status",
        "reference_state",
    }
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise ValueError(f"CSV must contain: {', '.join(sorted(required))}")
        cases: list[tuple[SyntheticCase, str, str]] = []
        for row in reader:
            reference_state = (row["reference_state"] or "").strip()
            if reference_state not in STATES:
                raise ValueError(
                    f"{row['case_id']}: invalid reference state {reference_state!r}"
                )
            cases.append(
                (
                    SyntheticCase(
                        case_id=(row["case_id"] or "").strip(),
                        condition_evidence=row["condition_evidence"] or "",
                        duration_evidence=row["duration_evidence"] or "",
                        severity_evidence=row["severity_evidence"] or "",
                    ),
                    reference_state,
                    (row["information_status"] or "").strip(),
                )
            )
    if not 30 <= len(cases) <= 50:
        raise ValueError("The synthetic v1 dataset must contain 30–50 cases.")
    return cases


def evaluate_v1(path: Path = DATA_PATH) -> dict[str, object]:
    """Make all predictions first, then reveal synthetic reference labels."""
    labelled_cases = load_cases(path)

    # Phase 1: references deliberately do not enter evaluate_case().
    blinded = [
        (evaluate_case(case), reference, status)
        for case, reference, status in labelled_cases
    ]

    records: list[dict[str, object]] = []
    action_counts: Counter[str] = Counter()
    routed = correct = under_triage = over_triage = total_cost = 0
    for result, reference_state, information_status in blinded:
        action_counts[result.selected_action] += 1
        record: dict[str, object] = {
            "case_id": result.case_id,
            "reference_state": reference_state,
            "information_status": information_status,
            "posterior_low": result.posterior["Low"],
            "posterior_medium": result.posterior["Medium"],
            "posterior_high": result.posterior["High"],
            "margin": result.margin,
            "selected_action": result.selected_action,
            "predicted_state": result.predicted_state,
            "error_type": "Deferred",
            "error_cost": None,
        }
        if result.predicted_state is not None:
            routed += 1
            prediction = result.predicted_state
            cost = ERROR_COSTS[reference_state][prediction]
            total_cost += cost
            if prediction == reference_state:
                correct += 1
                error_type = "Exact match"
            elif REFERENCE_ORDER[prediction] < REFERENCE_ORDER[reference_state]:
                under_triage += 1
                error_type = "Under-triage"
            else:
                over_triage += 1
                error_type = "Over-triage"
            record.update(error_type=error_type, error_cost=cost)
        records.append(record)

    return {
        "records": records,
        "total_cases": len(records),
        "routed_cases": routed,
        "routed_exact_matches": correct,
        "routed_exact_match_rate": correct / routed if routed else None,
        "under_triage": under_triage,
        "over_triage": over_triage,
        "total_synthetic_error_cost": total_cost,
        "ask_count": action_counts["Ask for more information"],
        "escalate_count": action_counts["Escalate to a human"],
        "action_counts": dict(action_counts),
    }


def write_results(report: dict[str, object], path: Path = RESULT_PATH) -> Path:
    """Save transparent per-case output for the synthetic evaluation."""
    fields = [
        "case_id",
        "reference_state",
        "information_status",
        "posterior_low",
        "posterior_medium",
        "posterior_high",
        "margin",
        "selected_action",
        "predicted_state",
        "error_type",
        "error_cost",
    ]
    with path.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cast(list[dict[str, object]], report["records"]))
    return path


def main() -> None:
    """Print a concise synthetic v1 evaluation report."""
    report = evaluate_v1()
    result_path = write_results(report)
    print("V1 SYNTHETIC SIMULATION EVALUATION — NOT CLINICAL VALIDATION")
    print(f"Cases: {report['total_cases']}")
    print(f"Routed cases: {report['routed_cases']}")
    rate = report["routed_exact_match_rate"]
    print(
        "Routed exact matches:",
        f"{report['routed_exact_matches']} ({rate:.1%})" if rate is not None else "n/a",
    )
    print(f"Under-triage: {report['under_triage']}")
    print(f"Over-triage: {report['over_triage']}")
    print(f"Ask for more information: {report['ask_count']}")
    print(f"Escalate to a human: {report['escalate_count']}")
    print(
        f"Total synthetic error cost (routed cases): {report['total_synthetic_error_cost']}"
    )
    print(f"Saved per-case synthetic results: {result_path}")
    print("\nPer-case results")
    for row in cast(list[dict[str, object]], report["records"]):
        print(
            f"{row['case_id']}: action={row['selected_action']}; "
            f"state={row['predicted_state'] or '-'}; margin={row['margin']:.3f}; "
            f"outcome={row['error_type']}"
        )


if __name__ == "__main__":
    main()
