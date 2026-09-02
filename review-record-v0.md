# Review Record — v0 Deterministic Routing Baseline

## Scope and safety boundary

This review covers `src/v0.py` and its synthetic blind test in
`src/v0_evaluation.py`. v0 is an educational routing prototype only. It does
not diagnose, does not use real clinical criteria, and must not be used for
medical advice or real patient routing.

## What v0 implements

v0 follows the planned fixed flow:

```text
Patient input → extract information → emergency check → urgent check → routine
```

It collects condition/symptoms, duration, and severity. However, its decision
uses only two synthetic text tags:

- `[simulation: emergency]` → Emergency
- `[simulation: urgent]` → Urgent
- no tag → Routine

Duration and severity are retained in the input record, but they are not part
of v0's routing rule.

## Evaluation method

The evaluation ran 13 synthetic cases. v0 made all predictions before the
expected routes were compared, so it did not read the expected-route field
when choosing a route.

## Result

| Test group | Correct | Total |
| --- | ---: | ---: |
| Emergency-tag cases | 3 | 3 |
| Urgent-tag cases | 3 | 3 |
| No-tag routine cases | 4 | 4 |
| Edge cases with no routing tag | 0 | 3 |
| **Overall** | **10** | **13** |

The resulting synthetic exact-match score was **76.9% (10/13)**.

## What worked

- The emergency check occurred before the urgent check.
- Every case containing the emergency or urgent simulation tag received the
  matching route.
- Every normal no-tag test case received the default Routine route.
- The test successfully exposed the baseline's expected limitation: it cannot
  respond to information that is not encoded as one of its two tags.

## Failed cases and explanation

| Case | Test-defined expected route | v0 route | Why v0 failed |
| --- | --- | --- | --- |
| `edge_1` | Urgent | Routine | It had no urgent or emergency simulation tag. |
| `edge_2` | Urgent | Routine | It had no urgent or emergency simulation tag. |
| `edge_3` | Urgent | Routine | It had no urgent or emergency simulation tag. |

These three outcomes are predictable from the code. v0 ignores the written
symptoms, duration, and severity when no tag is present, then applies its
default Routine route.

## Important interpretation limits

1. This is a **synthetic software test**, not a clinical validation.
2. The emergency and urgent test cases already contain the tag that tells v0
   which route to select. Their success verifies tag detection and route order;
   it does not show that the program can triage patient language.
3. The edge-case expected routes are described in the evaluation code as
   clinical judgments. No supported clinical routing protocol or source is
   documented there, so those labels must remain test assumptions rather than
   medical facts.
4. Thirteen cases are enough to demonstrate the v0 mechanism, but too few to
   support a broad performance claim.

## Review decision

**Accept v0 as the deterministic baseline.** It correctly demonstrates the
planned if/else architecture and clearly shows why a later version needs a
documented way to handle information beyond fixed tags.

## Next steps for a later version

- Keep v0 unchanged as the comparison baseline.
- Document a separate, synthetic decision table before adding any new rules.
- Define reference routes from that documented simulation table, rather than
  presenting unsupported symptom-based labels as clinical truth.
- Evaluate v1 on the same cases plus additional tag-free synthetic cases.
- If the project ever moves beyond simulation, use an appropriate evidence
  base, expert review, safety governance, and real validation; do not infer
  those from this v0 result.
