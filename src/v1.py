"""v1: a synthetic uncertainty-aware appointment-routing simulation.

This educational prototype does not diagnose, provide medical advice, or make
real care-routing decisions.  Its priors, likelihoods, and thresholds are
synthetic assumptions used only to demonstrate Bayesian updating with
incomplete controlled evidence.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Mapping

STATES = ("Low", "Medium", "High")
EVIDENCE_FIELDS = (
    "condition_evidence",
    "duration_evidence",
    "severity_evidence",
)
PRIOR = {"Low": 0.33, "Medium": 0.33, "High": 0.34}

# Each table is a synthetic simulation assumption, not a clinical model.
LIKELIHOODS: dict[str, dict[str, dict[str, float]]] = {
    "condition_evidence": {
        "Lower-concern": {"Low": 0.70, "Medium": 0.25, "High": 0.05},
        "Intermediate": {"Low": 0.20, "Medium": 0.60, "High": 0.20},
        "Higher-concern": {"Low": 0.05, "Medium": 0.25, "High": 0.70},
    },
    "duration_evidence": {
        "Short": {"Low": 0.50, "Medium": 0.35, "High": 0.15},
        "Medium": {"Low": 0.25, "Medium": 0.50, "High": 0.25},
        "Long": {"Low": 0.15, "Medium": 0.35, "High": 0.50},
    },
    "severity_evidence": {
        "Mild": {"Low": 0.70, "Medium": 0.25, "High": 0.05},
        "Moderate": {"Low": 0.20, "Medium": 0.60, "High": 0.20},
        "Severe": {"Low": 0.05, "Medium": 0.25, "High": 0.70},
    },
}

ROUTES = {"Low": "Routine", "Medium": "Urgent", "High": "Emergency"}
ROUTE_THRESHOLD = 0.40
ASK_THRESHOLD = 0.20
ASK_ACTION = "Ask for more information"
ESCALATE_ACTION = "Escalate to a human"


@dataclass(frozen=True)
class SyntheticCase:
    """A controlled-evidence case. Empty strings represent missing evidence."""

    case_id: str
    condition_evidence: str = ""
    duration_evidence: str = ""
    severity_evidence: str = ""


@dataclass(frozen=True)
class DecisionResult:
    """Transparent result of one synthetic v1 decision."""

    case_id: str
    evidence: dict[str, str]
    missing_fields: tuple[str, ...]
    posterior: dict[str, float]
    highest_state: str
    margin: float
    selected_action: str
    predicted_state: str | None


def _normalise_value(value: str | None) -> str:
    return (value or "").strip()


def _canonical_value(field: str, value: str) -> str:
    """Return the controlled category with canonical capitalization."""
    normalised = _normalise_value(value)
    for allowed in LIKELIHOODS[field]:
        if allowed.casefold() == normalised.casefold():
            return allowed
    return normalised


def extract_evidence(case: SyntheticCase) -> tuple[dict[str, str], tuple[str, ...]]:
    """Validate controlled values and return available evidence plus omissions.

    v1 deliberately refuses free-text extraction: no evidence-based mapping
    from patient language to these synthetic categories exists in this project.
    """
    available: dict[str, str] = {}
    missing: list[str] = []
    for field in EVIDENCE_FIELDS:
        value = _canonical_value(field, getattr(case, field))
        if not value:
            missing.append(field)
            continue
        if value not in LIKELIHOODS[field]:
            allowed = ", ".join(LIKELIHOODS[field])
            raise ValueError(
                f"Invalid {field!r} value {value!r}. Allowed values: {allowed}."
            )
        available[field] = value
    return available, tuple(missing)


def calculate_posterior(evidence: Mapping[str, str]) -> dict[str, float]:
    """Apply synthetic likelihoods to the prior and normalise the result."""
    scores = dict(PRIOR)
    for field, value in evidence.items():
        if field not in LIKELIHOODS:
            raise ValueError(f"Unknown evidence field: {field!r}")
        if value not in LIKELIHOODS[field]:
            raise ValueError(f"Invalid {field!r} value: {value!r}")
        for state in STATES:
            scores[state] *= LIKELIHOODS[field][value][state]

    total = sum(scores.values())
    if total <= 0:
        raise ValueError("Synthetic evidence produced a zero probability total.")
    return {state: scores[state] / total for state in STATES}


def calculate_margin(posterior: Mapping[str, float]) -> tuple[str, float]:
    """Return the most probable state and its gap over the runner-up."""
    if set(posterior) != set(STATES):
        raise ValueError("Posterior must contain exactly Low, Medium, and High.")
    ranked = sorted(STATES, key=lambda state: (-posterior[state], STATES.index(state)))
    return ranked[0], posterior[ranked[0]] - posterior[ranked[1]]


def choose_action(highest_state: str, margin: float) -> tuple[str, str | None]:
    """Apply the documented synthetic uncertainty policy at exact boundaries."""
    if highest_state not in ROUTES:
        raise ValueError(f"Unknown synthetic state: {highest_state!r}")
    if margin >= ROUTE_THRESHOLD:
        return ROUTES[highest_state], highest_state
    if margin >= ASK_THRESHOLD:
        return ASK_ACTION, None
    return ESCALATE_ACTION, None


def evaluate_case(case: SyntheticCase) -> DecisionResult:
    """Evaluate one case without any reference label entering the decision."""
    evidence, missing_fields = extract_evidence(case)
    posterior = calculate_posterior(evidence)
    highest_state, margin = calculate_margin(posterior)
    selected_action, predicted_state = choose_action(highest_state, margin)
    return DecisionResult(
        case_id=case.case_id,
        evidence=evidence,
        missing_fields=missing_fields,
        posterior=posterior,
        highest_state=highest_state,
        margin=margin,
        selected_action=selected_action,
        predicted_state=predicted_state,
    )


def _prompt(field: str, allowed: Mapping[str, object]) -> str:
    print(f"{field} ({', '.join(allowed)}; leave blank if missing)")
    while True:
        value = input("> ").strip()
        if not value:
            return ""
        for option in allowed:
            if option.casefold() == value.casefold():
                return option
        print(f"Invalid input. Choose one of: {', '.join(allowed)}")


def main() -> None:
    """Run one controlled synthetic case interactively."""
    parser = argparse.ArgumentParser(
        description="Run one synthetic v1 simulation case."
    )
    parser.add_argument("--case-id", default="interactive")
    args = parser.parse_args()

    print("v1 — synthetic uncertainty-aware simulation; not medical advice.\n")
    print("Use only the controlled categories below. Do not enter patient symptoms.\n")
    case = SyntheticCase(
        case_id=args.case_id,
        condition_evidence=_prompt(
            "Condition evidence", LIKELIHOODS["condition_evidence"]
        ),
        duration_evidence=_prompt(
            "Duration evidence", LIKELIHOODS["duration_evidence"]
        ),
        severity_evidence=_prompt(
            "Severity evidence", LIKELIHOODS["severity_evidence"]
        ),
    )
    result = evaluate_case(case)
    print("\nAvailable evidence:", result.evidence or "none")
    print("Missing fields:", ", ".join(result.missing_fields) or "none")
    print("Posterior (synthetic):")
    for state in STATES:
        print(f"  {state}: {result.posterior[state]:.2%}")
    print(f"Probability margin: {result.margin:.2%}")
    print(f"Selected action: {result.selected_action}")
    print("This action is produced by synthetic assumptions, not clinical criteria.")


if __name__ == "__main__":
    main()
