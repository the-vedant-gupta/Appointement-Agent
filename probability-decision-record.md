# Probability Decision Record — AI Appointment/Triage Agent

## 1. Decision Problem

The agent must select a care-routing action when patient information is
incomplete or uncertain.

The routing levels are:

- Routine
- Urgent
- Emergency

The agent does not diagnose the patient's medical condition.

The main research problem is:

> How should the agent make a safe routing decision when the available
> patient information does not completely reveal the appropriate urgency?

The agent may also:

- ask for more information; or
- escalate the case to a human.

## 2. Hidden States

The initial model represents the patient's underlying urgency as a hidden
state.

The three initial hidden states are:

- Low urgency
- Medium urgency
- High urgency

The agent cannot directly observe the hidden state.

Instead, it estimates the hidden state from the available evidence.

## 3. Observable Evidence

The agent receives patient-provided information.

The initial evidence variables are:

- Condition / symptoms
- Time / duration
- Severity

Evidence may be:

- complete;
- incomplete;
- unclear; or
- contradictory.

The agent uses the available evidence to estimate the probability of
each hidden urgency state.

## 4. Belief State

For observed evidence E, the agent maintains a probability distribution
over the hidden urgency states:

P(Low urgency | E)

P(Medium urgency | E)

P(High urgency | E)

These probabilities represent the agent's current belief about the
underlying urgency state.

The probabilities should sum to 1.
For example:
			P(Low | E)    = 0.60
			P(Medium | E) = 0.30
			P(High | E)   = 0.10
These values are illustrative only and are not medical probabilities.
## 5. Prior Probability

#### Decision
For the initial simulation, I will use a synthetic prior distribution.

The prior probabilities are:
- P(Low urgency) = 0.33
- P(Medium urgency) = 0.33
- P(High urgency) = 0.34
The probabilities sum to 1:
				P(Low) + P(Medium) + P(High) = 1.00
#### Rationale
A near-uniform prior is used so that the initial simulation does not strongly favor one urgency state before evidence is observed.
These values are **synthetic simulation assumptions**. They are not clinical probabilities and do not represent the real distribution of patients across urgency levels.

A future version may replace these assumptions with a dataset-derived or empirically supported prior.
## 6. Likelihood

#### Definition
Likelihood represents how compatible an observed piece of evidence is with each possible hidden urgency state.
For evidence E, the model considers:
		P(E | Low urgency)
		P(E | Medium urgency)
		P(E | High urgency)
These values describe how frequently the evidence would be expected under
each hidden state.
#### Evidence Currently Considered

The initial evidence variables are:
- Condition / symptoms
- Time / duration
- Severity
The agent may receive incomplete, unclear, or contradictory evidence.
### Decision
Prior                  → DECIDED
Condition likelihood   → DECIDED (synthetic)
Duration likelihood    → NEXT
Severity likelihood    → AFTER THAT
#### Research Questions
1. How can likelihoods be estimated for clinical triage?
2. What data can provide evidence-to-state relationships?
3. Can likelihoods be estimated separately for different evidence
   variables?
4. How should missing evidence affect the model?
5. How should contradictory evidence be handled?

### Synthetic Condition/Symptom Likelihoods

For the initial simulation, condition/symptom evidence will be represented using three abstract categories:
- Lower-concern
- Intermediate
- Higher-concern
The synthetic likelihood table is:

| Condition/Symptom Evidence | P(E \| Low) | P(E \| Medium) | P(E \| High) |
| :------------------------- | :---------- | :------------- | :----------- |
| Lower-concern              | 0.70        | 0.25           | 0.05         |
| Intermediate               | 0.20        | 0.60           | 0.20         |
| Higher-concern             | 0.05        | 0.25           | 0.70         |

These values are synthetic simulation assumptions. They are not clinical probabilities and are not intended to represent real-world medical relationships.
The purpose of these values is to test whether the probabilistic model updates its belief appropriately when evidence is introduced.
#### Synthetic Duration Likelihoods
For the initial simulation, duration evidence will be represented using three abstract categories:
- Short
- Medium
- Long
The synthetic likelihood table is:

| Duration Evidence | P(E \| Low) | P(E \| Medium) | P(E \| High) |
| ----------------- | :---------- | :------------- | :----------- |
| Short             | 0.50        | 0.35           | 0.15         |
| Medium            | 0.25        | 0.50           | 0.25         |
| Long              | 0.15        | 0.35           | 0.50         |

These values are synthetic simulation assumptions. 
#### Synthetic Severity Likelihoods
For the initial simulation, severity evidence will be represented using three abstract categories:
- Mild
- Moderate
- Severe
The synthetic likelihood table is:

| Severity Evidence | P(E \| Low) | P(E \| Medium) | P(E \| High) |
| :---------------- | :---------- | :------------- | :----------- |
| Mild              | 0.70        | 0.25           | 0.05         |
| Moderate          | 0.20        | 0.60           | 0.20         |
| Severe            | 0.05        | 0.25           | 0.70         |

These values are synthetic simulation assumptions. 
## 7. Posterior Probability

#### Definition
Posterior probability represents the agent's updated belief about each hidden urgency state after observing evidence.

For evidence E:
		P(Low urgency | E)
		P(Medium urgency | E)
		P(High urgency | E)
The posterior probability is obtained by updating the prior belief using the likelihood of the observed evidence.

Conceptually:
			Prior belief
			    +
			New evidence
			    ↓
			Updated belief (posterior)

#### Bayesian Update
The general Bayesian relationship is:
					P(S | E) = P(E | S) P(S) / P(E)
where:

	- S = hidden urgency state
	- E = observed evidence
	- P(S) = prior probability
	- P(E | S) = likelihood of the evidence given the state
	- P(S | E) = posterior probability
#### Example
Suppose the agent starts with some prior belief about the three hidden states and then receives new evidence.
The evidence changes the agent's belief:

Before evidence:
			P(Low)
			P(Medium)
			P(High)

After evidence:
			P(Low | E)
			P(Medium | E)
			P(High | E)
The numerical values in this example will not be treated as medical probabilities.
#### Worked Synthetic Example
For the simulation, consider a case with:
- Condition/Symptoms = Higher-concern
- Duration = Long
- Severity = Severe

The prior probabilities are:	
	P(Low) = 0.33
	P(Medium) = 0.33
	P(High) = 0.34
The corresponding synthetic likelihoods are:

| Evidence       |  Low | Medium | High |
| -------------- | ---: | -----: | ---: |
| Higher-concern | 0.05 |   0.25 | 0.70 |
| Long duration  | 0.15 |   0.35 | 0.50 |
| Severe         | 0.05 |   0.25 | 0.70 |
The unnormalized values are:
Low:
	0.33 × 0.05 × 0.15 × 0.05 = 0.00012375
Medium:
	0.33 × 0.25 × 0.35 × 0.25 = 0.00721875
High:
	0.34 × 0.70 × 0.50 × 0.70 = 0.08330

After normalization:
	P(Low | E) ≈ 0.14%
	P(Medium | E) ≈ 7.96%
	P(High | E) ≈ 91.90%

This example demonstrates how multiple pieces of synthetic evidence can update the agent's prior belief.

- PRIOR
"What did I believe before seeing this evidence?"
- LIKELIHOOD
"How compatible is this evidence with each state?"
- POSTERIOR
"What do I believe after seeing the evidence?"
For our agent:- 
		Patient information
			↓
		Evidence
		    ↓
		Prior + Likelihood
		    ↓
	    Posterior
		    ↓
	What is my current belief about urgency?

## 8. Decision Rule / Action Selection

#### Decision Problem
After observing the available evidence, the agent has a probability distribution over the hidden urgency states.
The agent must use this belief to select an action.

Possible actions:
		- Routine routing
		- Urgent routing
		- Emergency routing
		- Ask for more information
		- Escalate to a human
#### Basic Probability-Based Policy
The initial probability-based policy will select the routing level corresponding to the most probable hidden urgency state.

Conceptually:
			Highest posterior probability
		            ↓
		     Select corresponding routing action
#### Limitation
Selecting the most probable state does not necessarily produce the safest action. A less probable high-urgency state may have a substantially greater consequence if it is missed.
Therefore, the project will also investigate a cost-sensitive and uncertainty-aware decision policy.
#### Uncertainty-Aware Policy
The uncertainty-aware policy may:
- select a routing action when the evidence is sufficiently informative;
- ask for additional information when uncertainty is high;
- escalate to a human when the agent should not make the decision alone.
#### Decision Rule — Simulation
The basic probability-based policy selects the routing level corresponding to the hidden urgency state with the highest posterior probability.

For example:
		P(Low | E) = 0.20
		P(Medium | E) = 0.65
		P(High | E) = 0.15
The highest posterior probability is Medium urgency, so the policy selects Urgent routing.

This is a simulation decision rule and does not represent a clinical routing guideline.
#### Uncertainty-Aware Decision Rule
The uncertainty-aware policy does not always force a routing decision.

It can choose among:
1. Routine routing
2. Urgent routing
3. Emergency routing
4. Ask for more information
5. Escalate to a human

Conceptually:

Posterior probabilities
        ↓
Evaluate information sufficiency
        ↓
 ┌──────────┬────────────┬────────────┐
 ↓                               ↓                                    ↓
Sufficient              Uncertain                   Unsafe to
information          information                decide alone
 ↓                              ↓                                      ↓
Route                    Ask                                 Escalate

The exact numerical thresholds for these decisions remain unresolved.
## 9. Uncertainty Rule

The agent should not always make a routing decision when the available evidence does not provide enough confidence. It should be able to recognize uncertainty and either ask for more information or escalate to a human.
#### Uncertainty Measurement
For the simulation, uncertainty is measured using the probability margin.

Margin = Highest Posterior Probability − Second Highest Posterior Probability

The margin compares the two most probable hidden urgency states.

A larger margin means the agent has a clearer preference for one state. A smaller margin means the probabilities are closer and the agent is more uncertain.
#### Example of High Confidence
Suppose the posterior probabilities are:
	P(Low)    = 0.10
	P(Medium) = 0.20
	P(High)   = 0.70

Highest posterior = 0.70
Second highest = 0.20

Margin = 0.70 − 0.20
       = 0.50
The margin is 0.50, which is above the routing threshold. Therefore, the simulation policy allows the agent to make a routing decision.
#### Example of Greater Uncertainty
Suppose the posterior probabilities are:
	P(Low)    = 0.30
	P(Medium) = 0.40
	P(High)   = 0.30

Highest posterior = 0.40
Second highest = 0.30

Margin = 0.40 − 0.30
       = 0.10

The margin is small, meaning that the agent does not have a strong preference between the possible urgency states. Therefore, the simulation policy does not immediately route and instead
considers the uncertainty-handling actions.

#### Synthetic Uncertainty Thresholds
The following thresholds are used:

| Probability Margin | Agent Action             |
| ------------------ | ------------------------ |
| >= 0.40            | Route                    |
| 0.20 to < 0.40     | Ask for more information |
| < 0.20             | Escalate to a human      |
These thresholds are synthetic assumptions created for the simulation. They are not clinical thresholds and do not represent medical guidance.

#### Action Selection Based on Uncertainty
The uncertainty-aware policy is:
1. Calculate the posterior probabilities for Low, Medium, and High urgency.
2. Identify the highest and second-highest posterior probabilities.
3. Calculate the probability margin.
4. Compare the margin with the synthetic thresholds.
5. Select the corresponding action.

The policy is:
If Margin >= 0.40:
    Route to the care level corresponding to the highest posterior.

If 0.20 <= Margin < 0.40:
    Ask for additional information.

If Margin < 0.20:
    Escalate to a human.
#### Ask for More Information
The "Ask" action is used when the agent has some evidence but the   probability distribution is not sufficiently separated for a confident   simulation decision.
The purpose of asking is to obtain additional evidence that may reduce uncertainty and allow the agent to update its posterior probabilities.

Possible additional information in the simulation may include:
- Clarification of the condition or symptoms
- More precise duration
- More precise severity
After receiving additional information, the agent can recalculate the posterior probabilities and reassess the uncertainty.

#### Human Escalation
The "Escalate" action is used when the simulation considers the agent's uncertainty too high for an autonomous routing decision.

Escalation means that the agent does not make the final routing decision itself and instead defers the case to a human.

In this prototype, escalation is a safety-oriented design mechanism for handling uncertainty. It does not represent a clinically validated escalation policy.

#### Relationship Between Probability and Uncertainty
Probability and uncertainty are related but are not the same thing.
The agent may have a highest-probability state without having enough separation between the possible states to justify an autonomous decision.

For example:

Case A:
		P(Low) = 0.05  
		P(Medium) = 0.10  
		P(High) = 0.85
Margin = 0.85 − 0.10 = 0.75
The highest state is clearly separated from the second highest state.

Case B:
		P(Low) = 0.30  
		P(Medium) = 0.40  
	P(High) = 0.30
Margin = 0.40 − 0.30 = 0.10
Medium is still the most probable state, but the difference is small.

Therefore, the uncertainty-aware policy does not simply choose the highest probability. It also considers how strongly that state is separated from the alternatives.

#### Limitations

The uncertainty rule has several limitations:
- The margin thresholds are synthetic.
- The thresholds have not been clinically validated.
- The posterior probabilities are based on synthetic assumptions.
- The simulation uses only three hidden urgency states.
- The simulation does not establish real-world patient safety.
- The "Ask" and "Escalate" policies are prototype decisions rather than clinical protocols.
#### Incomplete Information Handling
When one or more evidence variables are missing, the agent uses only the available evidence to calculate the posterior probabilities.

For example, if `severity_evidence` is missing:
$$
			[ P(S|E) \propto P(S)\times P(condition|S)\times P(duration|S)]
$$
The resulting values are then normalized so that:
$$
	
	[ P(Low|E)+P(Medium|E)+P(High|E)=1 ]
$$

The agent then applies the same probability-margin rule:
1. Calculate posterior probabilities using available evidence.
2. Identify the highest and second-highest posterior.
3. Calculate the probability margin.
4. Compare the margin with the uncertainty thresholds.
5. Route, ask for more information, or escalate to a human.

**Scope:** This is a synthetic simulation rule for testing incomplete information. It is not a clinical protocol.
## 10. Error Costs

### Why Error Costs Matter
The agent can make different types of routing errors. These errors may not have the same consequences.
Therefore, the project will investigate cost-sensitive decision-making rather than assuming that every incorrect decision has the same cost.

#### Main Error Types
#### 1. Under-triage
The agent selects a lower urgency level than the reference decision.
Example:
		Reference: High urgency
		Agent: Low urgency
#### 2. Over-triage
The agent selects a higher urgency level than the reference decision.
Example:
		Reference: Low urgency
		Agent: High urgency
#### 3. Uncertainty-handling error
The agent makes a routing decision when the available information is insufficient and the appropriate action would have been to ask for more information or escalate.
### Cost Matrix
The project may represent the relative cost of different decisions using a cost matrix.
For example:

| Reference State | Routine | Urgent | Emergency |
| :-------------- | :------ | :----- | :-------- |
| Low             | 0       | 1      | 2         |
| Medium          | 2       | 0      | 1         |
| High            | 5       | 3      | 0         |

- Correct decision → `0` cost
- Small routing mistake → `1–2` cost
- Larger routing mistake → higher cost
- High urgency → Routine routing → `5` cost, representing the most severe
  under-triage scenario in this simulation
These values are synthetic assumptions.
## 11. Open Decisions

The prototype uses synthetic assumptions to make the probability and decision framework testable. 
#### Decisions Made 
- **Prior probability:** Synthetic near-uniform prior
  - Low = 0.33
  - Medium = 0.33
  - High = 0.34
- **Evidence variables:**
  - Condition/Symptoms
  - Duration
  - Severity
- **Likelihood values:** Synthetic likelihood tables for the three evidence
  variables.
- **Decision rule:** Select the routing level corresponding to the highest
  posterior probability when the probability margin is sufficiently large.
- **Uncertainty measure:** Probability margin between the highest and
  second-highest posterior probabilities.
- **Uncertainty thresholds:**
  - Margin >= 0.40 → Route
  - Margin 0.20–<0.40 → Ask for more information
  - Margin < 0.20 → Escalate to a human
- **Error costs:** Synthetic relative cost values for simulation.
- **Evaluation dataset:** 30–50 synthetic test cases.

#### Assumption Boundary

All numerical probabilities, likelihoods, uncertainty thresholds, and error-cost values used are assumptions for simulation purposes.
They must not be interpreted as clinical probabilities, clinical thresholds, or medical recommendations.
## 12. Evaluation Design

The prototype will be evaluated using a small synthetic test set.

#### Test Set
Create **30–50 synthetic cases**.

Each case should contain:
- Patient information
- Hidden/reference urgency state
- Condition/Symptoms
- Duration
- Severity
- Whether the evidence is complete or incomplete
- Agent posterior probabilities
- Agent uncertainty margin
- Agent action
- Whether the agent asked for more information
- Whether the agent escalated to a human
- Final routing decision

The hidden urgency state is used as the known target in the simulation. It is not a clinical diagnosis.

#### Policies to Compare
The evaluation will compare three decision approaches:

#### A. Baseline Policy
A simple rule-based approach that selects a routing level without using the probability model.
#### B. Probability-Based Policy
The agent calculates posterior probabilities and selects the urgency state with the highest posterior probability.
#### C. Uncertainty-Aware Policy
The agent uses the posterior probabilities and probability margin:
	Margin >= 0.40
	    → Route
	0.20 <= Margin < 0.40
	    → Ask for more information
	Margin < 0.20
	    → Escalate to a human
These thresholds are synthetic assumptions. 
#### Evaluation Measures
The following measures will be recorded:

1. **Overall routing accuracy**
    - Percentage of cases where the final routing matches the reference urgency state.
2. **Under-triage**
    - Cases where the agent routes to a lower urgency level than the reference state.
3. **Over-triage**
    - Cases where the agent routes to a higher urgency level than the reference state.
4. **Uncertainty handling**
    - Whether the agent appropriately asks or escalates when the simulation indicates high uncertainty.
5. **Questions asked**
    - Number of cases in which the agent requests additional information.
6. **Human escalations**
    - Number of cases deferred to a human.
7. **Representative errors**
    - Document five representative incorrect decisions and explain why the policy produced them.

#### Error-Cost Evaluation

The synthetic error-cost matrix can be used to compare the decision policies beyond simple accuracy.

The purpose is to investigate whether a policy with slightly different accuracy can produce a lower total simulated error cost.

The cost values are synthetic relative weights and are not clinical cost estimates.
#### Evaluation Boundary
The evaluation is intended to test whether the proposed probability and uncertainty decision framework behaves consistently under the defined synthetic assumptions.

It does **not** establish:
- Clinical effectiveness
- Clinical safety
- Medical accuracy
- Real-world patient outcomes
- Validity of the probability values
- Validity of the uncertainty thresholds
- Validity of the synthetic error costs