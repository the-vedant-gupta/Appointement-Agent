# v1 Architecture — Synthetic Uncertainty-Aware Appointment Agent

## 1. Purpose

v1 extends the v0 deterministic baseline. It estimates one of three
**synthetic hidden urgency states** from the available evidence, then decides
whether to route, ask for more information, or escalate to a human.

This is a Week 1 research simulation. It does not diagnose conditions, set
clinical urgency, or provide medical advice. Every number and rule below is a
simulation assumption taken from `probability-decision-record.md`.

## 2. v1 flow

```text
Synthetic patient case
        ↓
Extract controlled evidence and record missing fields
        ↓
Start with synthetic prior beliefs
        ↓
Use available evidence to calculate posterior beliefs
Low / Medium / High
        ↓
Find the probability margin
(highest posterior − second-highest posterior)
        ↓
┌───────────────────────┬──────────────────────────┬──────────────────────┐
│ margin >= 0.40         │ 0.20 <= margin < 0.40    │ margin < 0.20        │
│ Route                 │ Ask for more information │ Escalate to a human  │
└───────────────────────┴──────────────────────────┴──────────────────────┘
        ↓
If routing: Low → Routine, Medium → Urgent, High → Emergency
```

## 3. Input design

v1 uses controlled synthetic categories. It must not infer a category from
free-text patient language, because no evidence-based clinical extraction rule
has been defined for this project.

| Field | Allowed values | Missing value |
| --- | --- | --- |
| `condition_evidence` | `Lower-concern`, `Intermediate`, `Higher-concern` | blank |
| `duration_evidence` | `Short`, `Medium`, `Long` | blank |
| `severity_evidence` | `Mild`, `Moderate`, `Severe` | blank |
| `reference_state` | `Low`, `Medium`, `High` | not allowed in a labelled evaluation case |

The `reference_state` is hidden from `v1.py` when it chooses an action. It is
used only after prediction by the evaluation script.

## 4. Synthetic belief model

### Prior

```text
Low     = 0.33
Medium  = 0.33
High    = 0.34
```

### Likelihood tables

`v1.py` will copy these tables exactly from the probability decision record.
Each row lists values in this order: `Low, Medium, High`.

| Evidence field | Value | Synthetic likelihoods |
| --- | --- | --- |
| Condition | Lower-concern | 0.70, 0.25, 0.05 |
| Condition | Intermediate | 0.20, 0.60, 0.20 |
| Condition | Higher-concern | 0.05, 0.25, 0.70 |
| Duration | Short | 0.50, 0.35, 0.15 |
| Duration | Medium | 0.25, 0.50, 0.25 |
| Duration | Long | 0.15, 0.35, 0.50 |
| Severity | Mild | 0.70, 0.25, 0.05 |
| Severity | Moderate | 0.20, 0.60, 0.20 |
| Severity | Severe | 0.05, 0.25, 0.70 |

For every available evidence value, v1 multiplies each state's prior score by
that value's likelihood. It skips a blank field, then normalizes the three
scores so that they sum to 1.

```text
unnormalized_score(state)
    = prior(state) × likelihood_1(state) × likelihood_2(state) ...

posterior(state)
    = unnormalized_score(state) / sum(all unnormalized scores)
```

Skipping a blank field is a simulation choice for incomplete information. It
does not mean missing clinical information is safe or unimportant.

## 5. Action policy

1. Find the highest and second-highest posterior probabilities.
2. Calculate `margin = highest − second-highest`.
3. Use the fixed synthetic policy below.

| Margin | v1 action |
| --- | --- |
| `>= 0.40` | Route according to the highest state |
| `>= 0.20` and `< 0.40` | Ask for more information |
| `< 0.20` | Escalate to a human |

When a route is allowed:

| Highest hidden state | Action |
| --- | --- |
| Low | Routine |
| Medium | Urgent |
| High | Emergency |

`Ask for more information` and `Escalate to a human` are separate actions;
they are not converted into Routine, Urgent, or Emergency for the evaluation.
The initial v1 simulation records the action but does not simulate a follow-up
answer or a human's final decision.

## 6. Planned Python design

The main implementation will be `src/v1.py`.

```text
SyntheticCase dataclass
    ├── case_id
    ├── condition_evidence
    ├── duration_evidence
    └── severity_evidence

extract_evidence(case)
    └── validate controlled values and identify blank fields

calculate_posterior(evidence)
    └── apply prior and available likelihoods; normalize scores

calculate_margin(posterior)
    └── return highest state and margin over second-highest state

choose_action(highest_state, margin)
    └── Route, Ask for more information, or Escalate to a human

evaluate_case(case)
    └── return evidence, posterior, margin, and action in one result record
```

The command-line output for one case should show:

```text
Available evidence
Missing fields
Posterior: Low / Medium / High
Probability margin
Selected action
```

## 7. Dataset contract

Create `data/v1_test_cases.csv` with 30–50 synthetic cases. Its minimum
columns are:

```csv
case_id,condition_evidence,duration_evidence,severity_evidence,information_status,reference_state
```

Example rows are structural examples only:

```csv
C001,Higher-concern,Long,Severe,Complete,High
C002,Intermediate,Medium,Moderate,Complete,Medium
C003,Lower-concern,Short,Mild,Complete,Low
C004,Intermediate,,Moderate,Incomplete,Medium
C005,Higher-concern,Long,,Incomplete,High
```

Dataset requirements:

- Include all three evidence values for each field.
- Include complete and incomplete cases.
- Include cases intended to produce routing, asking, and escalation under the
  documented simulation policy.
- Keep the reference state hidden from the v1 decision function.
- Label every row as synthetic; no real patient information is allowed.

## 8. Evaluation design

`src/v1_evaluation.py` will read the CSV and save one result per case:

```text
case_id
reference_state
posterior_low
posterior_medium
posterior_high
margin
selected_action
predicted_state (only when v1 routes)
```

For routed cases, record:

- exact synthetic-state matches;
- under-triage;
- over-triage; and
- the synthetic error cost from the documented cost matrix.

For deferred cases, record separately:

- number that asked for more information; and
- number escalated to a human.

Do not count a deferred action as a correct final route, because the initial
simulation does not model the later answer or human decision.

## 9. Acceptance checks

Before calling v1 complete, verify that:

- posterior values sum to 1 (allowing small rounding differences);
- blank evidence fields are skipped without crashing;
- margin thresholds use the exact boundary values in Section 5;
- `reference_state` is never passed into the v1 decision function;
- all output labels say `synthetic simulation` or equivalent; and
- v0 remains unchanged as the deterministic comparison baseline.

## 10. Known limitations

- The priors, likelihoods, thresholds, and error costs are synthetic.
- The model assumes the evidence fields can be treated independently for this
  small simulation.
- “Ask” and “Escalate” end the case; they do not simulate a next interaction.
- No result from this system demonstrates clinical safety, medical accuracy, or
  real-world usefulness.
