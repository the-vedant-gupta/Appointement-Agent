"""Week 1 v0: a deterministic appointment-routing baseline.

This educational prototype is for synthetic simulation only.  It does not
diagnose and must not be used for real medical decisions.  The routing tags
below are placeholders, not clinical rules.
"""

from dataclasses import dataclass

# Simulation-only labels.  A later, evidence-based version may replace these
# with properly documented criteria.  They are deliberately not medical rules.
EMERGENCY_TAG = "[simulation: emergency]"
URGENT_TAG = "[simulation: urgent]"

# Five made-up cases for checking the v0 flow.  They contain no real patient
# data and the tags are simulation labels, not descriptions of medical rules.
SYNTHETIC_PATIENT_CASES = {
    "case_1": {
        "condition_or_symptoms": "Synthetic scenario " + EMERGENCY_TAG,
        "duration": "short",
        "severity": "severe",
    },
    "case_2": {
        "condition_or_symptoms": "Synthetic scenario " + URGENT_TAG,
        "duration": "medium",
        "severity": "moderate",
    },
    "case_3": {
        "condition_or_symptoms": "Synthetic scenario with no routing tag",
        "duration": "long",
        "severity": "mild",
    },
    "case_4": {
        "condition_or_symptoms": "Another synthetic scenario " + URGENT_TAG,
        "duration": "short",
        "severity": "mild",
    },
    "case_5": {
        "condition_or_symptoms": "Another synthetic scenario with no routing tag",
        "duration": "medium",
        "severity": "severe",
    },
}


@dataclass
class PatientInput:
    """The information collected from one synthetic patient scenario."""

    condition_or_symptoms: str
    duration: str
    severity: str


def collect_patient_input() -> PatientInput:
    """Ask for the three information fields defined for the v0 prototype."""
    print("Week 1 v0 — synthetic simulation only; not medical advice.\n")
    print(
        "For a simulated emergency or urgent case, include the exact placeholder "
        "tag in the condition/symptoms field."
    )
    print(f"  Emergency tag: {EMERGENCY_TAG}")
    print(f"  Urgent tag:    {URGENT_TAG}\n")

    return PatientInput(
        condition_or_symptoms=input("Condition or symptoms: ").strip(),
        duration=input("Duration: ").strip(),
        severity=input("Severity: ").strip(),
    )


def extract_information(patient: PatientInput) -> dict[str, str]:
    """Put the collected fields into the simple structure used by v0."""
    return {
        "condition_or_symptoms": patient.condition_or_symptoms.lower(),
        "duration": patient.duration,
        "severity": patient.severity,
    }


def choose_route(information: dict[str, str]) -> str:
    """Route in the fixed v0 order: emergency, then urgent, then routine.

    Only the two clearly labelled simulation tags decide the route. Duration
    and severity are retained as part of the extracted input, but v0 has no
    evidence-based rule for using them yet.
    """
    condition_or_symptoms = information["condition_or_symptoms"]

    # First check: emergency.
    if EMERGENCY_TAG in condition_or_symptoms:
        return "Emergency"

    # Second check: urgent.
    if URGENT_TAG in condition_or_symptoms:
        return "Urgent"

    # Default route when neither placeholder condition is present.
    return "Routine"


def run_synthetic_cases() -> None:
    """Run the five made-up cases through the same deterministic v0 rules."""
    print("Five synthetic v0 test cases — not medical data or advice.\n")
    for case_name, case_data in SYNTHETIC_PATIENT_CASES.items():
        patient = PatientInput(**case_data)
        information = extract_information(patient)
        route = choose_route(information)
        print(f"{case_name}: {route}")


def main() -> None:
    """Run the v0 flow from input collection through the route decision."""
    patient = collect_patient_input()
    information = extract_information(patient)
    route = choose_route(information)

    print("\nExtracted information")
    print(f"- Condition/symptoms: {patient.condition_or_symptoms}")
    print(f"- Duration: {information['duration']}")
    print(f"- Severity: {information['severity']}")
    print(f"\nRouting result: {route}")
    print(
        "This result is produced by placeholder simulation rules, not clinical criteria."
    )


if __name__ == "__main__":
    main()
