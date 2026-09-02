"""Evaluate v0 accuracy against synthetic patient data with expected outcomes.

This module generates synthetic cases and compares v0's routing decisions
against expected clinical routing to measure accuracy.

BLIND TEST: v0 is NOT given expected outcomes; it makes predictions independently.
"""

from dataclasses import dataclass
from v0 import (
    PatientInput,
    extract_information,
    choose_route,
    EMERGENCY_TAG,
    URGENT_TAG,
)


@dataclass
class PatientCase:
    """Input case data that v0 sees (no expected_route)."""

    case_id: str
    condition_or_symptoms: str
    duration: str
    severity: str


@dataclass
class ExpectedOutcome:
    """Expected routing - hidden from v0 during testing."""

    case_id: str
    expected_route: str


# BLIND TEST DATA: v0 only sees patient cases without expected routes
PATIENT_CASES = [
    # Emergency cases
    PatientCase(
        case_id="emergency_1",
        condition_or_symptoms=f"Chest pain, difficulty breathing {EMERGENCY_TAG}",
        duration="sudden",
        severity="severe",
    ),
    PatientCase(
        case_id="emergency_2",
        condition_or_symptoms=f"Loss of consciousness {EMERGENCY_TAG}",
        duration="acute",
        severity="severe",
    ),
    PatientCase(
        case_id="emergency_3",
        condition_or_symptoms=f"Severe allergic reaction {EMERGENCY_TAG}",
        duration="rapid",
        severity="severe",
    ),
    # Urgent cases
    PatientCase(
        case_id="urgent_1",
        condition_or_symptoms=f"High fever and confusion {URGENT_TAG}",
        duration="few hours",
        severity="moderate",
    ),
    PatientCase(
        case_id="urgent_2",
        condition_or_symptoms=f"Severe headache and stiff neck {URGENT_TAG}",
        duration="overnight",
        severity="moderate",
    ),
    PatientCase(
        case_id="urgent_3",
        condition_or_symptoms=f"Persistent vomiting {URGENT_TAG}",
        duration="several hours",
        severity="moderate",
    ),
    # Routine cases (no tags, various combinations)
    PatientCase(
        case_id="routine_1",
        condition_or_symptoms="Mild headache",
        duration="2 days",
        severity="mild",
    ),
    PatientCase(
        case_id="routine_2",
        condition_or_symptoms="Cough and mild cold symptoms",
        duration="5 days",
        severity="mild",
    ),
    PatientCase(
        case_id="routine_3",
        condition_or_symptoms="Minor skin rash",
        duration="3 days",
        severity="mild",
    ),
    PatientCase(
        case_id="routine_4",
        condition_or_symptoms="Back pain from sitting",
        duration="1 week",
        severity="moderate",
    ),
    # Edge cases - challenging for v0
    PatientCase(
        case_id="edge_1",
        condition_or_symptoms="Severe pain in leg but no tag",
        duration="sudden",
        severity="severe",
    ),
    PatientCase(
        case_id="edge_2",
        condition_or_symptoms="Persistent cough for weeks",
        duration="3 weeks",
        severity="mild",
    ),
    PatientCase(
        case_id="edge_3",
        condition_or_symptoms="Moderate fever for 5 days",
        duration="5 days",
        severity="moderate",
    ),
]

# EXPECTED OUTCOMES: Based on CLINICAL severity/duration, not v0's tags
EXPECTED_OUTCOMES = {
    "emergency_1": "Emergency",  # Has tag + severe → Emergency ✓
    "emergency_2": "Emergency",  # Has tag + severe → Emergency ✓
    "emergency_3": "Emergency",  # Has tag + severe → Emergency ✓
    "urgent_1": "Urgent",  # Has tag + moderate → Urgent ✓
    "urgent_2": "Urgent",  # Has tag + moderate → Urgent ✓
    "urgent_3": "Urgent",  # Has tag + moderate → Urgent ✓
    "routine_1": "Routine",  # Mild → Routine ✓
    "routine_2": "Routine",  # Mild → Routine ✓
    "routine_3": "Routine",  # Mild → Routine ✓
    "routine_4": "Routine",  # Moderate but stable → Routine ✓
    "edge_1": "Urgent",  # SEVERE pain, sudden - should be Urgent (v0 will fail)
    "edge_2": "Urgent",  # Persistent 3 weeks - should be Urgent (v0 will fail)
    "edge_3": "Urgent",  # Moderate + 5 days - should be Urgent (v0 will fail)
}


def evaluate_v0() -> dict:
    """Run v0 against all patient cases in a BLIND TEST.

    BLIND TEST METHODOLOGY:
    1. v0 only sees patient cases (without expected routes)
    2. v0 makes predictions independently
    3. Only after all predictions are made, compare against expected outcomes
    4. This ensures v0 isn't influenced by knowing "correct" answers
    """
    results = []
    correct = 0
    total = len(PATIENT_CASES)

    print("=" * 80)
    print("V0 ROUTING ACCURACY EVALUATION (BLIND TEST)")
    print("=" * 80)
    print(f"\nBLIND TEST: v0 makes predictions WITHOUT knowing expected routes")
    print(f"Testing {total} synthetic patient cases...\n")

    # PHASE 1: v0 makes predictions (blind to expected outcomes)
    predictions = []
    for case in PATIENT_CASES:
        # Create patient input and extract information
        patient = PatientInput(
            condition_or_symptoms=case.condition_or_symptoms,
            duration=case.duration,
            severity=case.severity,
        )
        information = extract_information(patient)
        predicted_route = choose_route(information)

        predictions.append(
            {
                "case_id": case.case_id,
                "predicted": predicted_route,
                "symptoms": case.condition_or_symptoms,
                "severity": case.severity,
            }
        )

    # PHASE 2: Reveal expected outcomes and compare
    print("PHASE 1: V0 Predictions (Blind)\n")
    for pred in predictions:
        print(f"  {pred['case_id']:12} → {pred['predicted']}")

    print("\n" + "=" * 80)
    print("PHASE 2: Comparing Against Expected Outcomes (Revealed)\n")

    for pred in predictions:
        case_id = pred["case_id"]
        expected_route = EXPECTED_OUTCOMES[case_id]
        is_correct = pred["predicted"] == expected_route

        if is_correct:
            correct += 1
            status = "✓ CORRECT"
        else:
            status = "✗ WRONG"

        results.append(
            {
                "case_id": case_id,
                "predicted": pred["predicted"],
                "expected": expected_route,
                "correct": is_correct,
                "symptoms": pred["symptoms"],
                "severity": pred["severity"],
            }
        )

        print(
            f"{status} | {case_id:12} | Expected: {expected_route:10} | "
            f"Predicted: {pred['predicted']:10}"
        )

    # Calculate metrics
    accuracy = (correct / total) * 100

    print("\n" + "=" * 80)
    print("ACCURACY METRICS")
    print("=" * 80)
    print(f"Correct predictions: {correct}/{total}")
    print(f"Accuracy: {accuracy:.1f}%")

    # Break down by category
    emergency_cases = [r for r in results if "emergency" in r["case_id"]]
    urgent_cases = [r for r in results if "urgent" in r["case_id"]]
    routine_cases = [r for r in results if "routine" in r["case_id"]]
    edge_cases = [r for r in results if "edge" in r["case_id"]]

    print(f"\nBy Category:")
    print(
        f"  Emergency: {sum(1 for r in emergency_cases if r['correct'])}/{len(emergency_cases)} correct"
    )
    print(
        f"  Urgent:    {sum(1 for r in urgent_cases if r['correct'])}/{len(urgent_cases)} correct"
    )
    print(
        f"  Routine:   {sum(1 for r in routine_cases if r['correct'])}/{len(routine_cases)} correct"
    )
    print(
        f"  Edge:      {sum(1 for r in edge_cases if r['correct'])}/{len(edge_cases)} correct"
    )

    # Show failures
    failures = [r for r in results if not r["correct"]]
    if failures:
        print(f"\n" + "=" * 80)
        print("FAILED CASES (Misrouted)")
        print("=" * 80)
        for failure in failures:
            print(f"\n{failure['case_id']}:")
            print(f"  Symptoms: {failure['symptoms']}")
            print(f"  Severity: {failure['severity']}")
            print(f"  Expected: {failure['expected']} | Got: {failure['predicted']}")

    return {
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "results": results,
    }


if __name__ == "__main__":
    evaluate_v0()
