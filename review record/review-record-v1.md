# Review Record — v1 Synthetic Uncertainty-Aware Routing Simulation

## Scope and safety boundary

This review covers `src/v1.py`, `src/v1_evaluation.py`, and the synthetic
dataset in `data/v1_test_cases.csv`.

v1 is an educational research simulation. It does not diagnose conditions,
provide medical advice, select care for real people, or validate a clinical
triage policy. Its states, probabilities, likelihoods, thresholds, labels,
and error costs are synthetic project assumptions.

## What v1 implements

v1 replaces v0's fixed placeholder-tag routing with a controlled-evidence
Bayesian simulation:

```text
Controlled synthetic evidence
    -> validate available / missing fields
    -> prior x available likelihoods
    -> normalised posterior over Low / Medium / High
    -> probability margin between the top two states
    -> route, ask for more information, or escalate to a human
```

The accepted controlled values are:

- Condition: `Lower-concern`, `Intermediate`, `Higher-concern`
- Duration: `Short`, `Medium`, `Long`
- Severity: `Mild`, `Moderate`, `Severe`

Free-text symptoms are deliberately rejected. The project has no documented,
evidence-based rule for converting patient language into those synthetic
categories.

The implemented synthetic action policy is:

| Probability margin | Action |
| --- | --- |
| `>= 0.40` | Route by highest state: Low -> Routine, Medium -> Urgent, High -> Emergency |
| `>= 0.20` and `< 0.40` | Ask for more information |
| `< 0.20` | Escalate to a human |

Blank fields are skipped during the synthetic posterior update. This is an
incomplete-information simulation choice; it does not assert that missing
clinical information is safe or unimportant.

## Evaluation method

The evaluator loaded 38 labelled synthetic cases. Each case contained only
the three controlled evidence fields when `v1.py` made its decision. The
synthetic `reference_state` was used only after all predictions were made.

The dataset contains complete and incomplete cases, uses every allowed
evidence category, and produces each policy action. Two cases intentionally
use a reference state different from their model-favoured state to verify that
under-triage, over-triage, and synthetic error-cost reporting work.

Deferred cases are not counted as correct final routes, because v1 does not
simulate the follow-up answer or human decision.

## Verification performed

Five automated acceptance tests passed:

1. A complete-evidence posterior normalises to 1 and favours the expected synthetic state.
2. Blank evidence fields are skipped without failure and the posterior remains normalised.
3. The exact `0.40` and `0.20` policy boundaries produce the documented actions.
4. Invalid controlled values, including free text, are rejected.
5. Evaluation separates routes from deferrals and records under-triage, over-triage, and synthetic cost.

## Synthetic evaluation result

| Measure | Result |
| --- | ---: |
| Total cases | 38 |
| Routed cases | 25 |
| Exact state matches among routed cases | 23 / 25 (92.0%) |
| Ask for more information | 3 |
| Escalate to a human | 10 |
| Under-triage | 1 |
| Over-triage | 1 |
| Total synthetic error cost, routed cases | 3 |

The one under-triage and one over-triage result come from the two intentional
metric-exercise cases. They show the evaluator's reporting path, not a
performance estimate for real triage.

Per-case posterior values, actions, reference states, and error categories
are saved in `data/v1_evaluation_results.csv`.

## What worked

- Posterior beliefs are transparent and sum to one.
- The action decision uses the documented margin policy, including boundary values.
- Missing controlled evidence does not crash the simulation.
- Uncertain cases can defer rather than forcing a route.
- Reference labels remain outside the v1 decision function.
- The evaluator distinguishes final routes from Ask and Escalate actions.
- v0 remains unchanged as the deterministic comparison baseline.

## Important interpretation limits

1. A match to a synthetic reference state is not a measure of clinical accuracy or safety.
2. The evidence categories, priors, likelihoods, threshold values, and error costs are not clinical data.
3. Conditional independence of the three evidence fields is a modelling simplification, not a verified property.
4. Skipping missing fields does not model why information is missing, nor does it make an incomplete case safe.
5. Ask and Escalate end the simulation. The benefit of a follow-up question or human review has not been tested.
6. The test dataset is designed from the same synthetic model being evaluated, so its agreement rate cannot establish generalisation.
7. Nothing in v1 supports using patient free text, real patient data, or real routing decisions.

## Review decision

**Accept v1 as the documented synthetic uncertainty-aware research prototype.**

It meets the stated implementation checks: controlled inputs, transparent
posterior calculation, margin-based routing/deferral, blind use of reference
labels, 30–50 synthetic cases, per-case saved results, and automated boundary
tests. This acceptance is strictly for the research simulation scope.

## Recommended next steps

- Treat v1 as the baseline for testing a simulated follow-up-question loop.
- Define the source and governance process for any future evidence categories
  before considering real-world inputs.
- Pre-register or independently construct future synthetic test cases so the
  evaluation is less coupled to the model assumptions.
- If the work ever leaves simulation, obtain appropriate clinical expertise,
  validation data, privacy controls, safety review, and governance first.
