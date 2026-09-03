# Research File — AI Appointment/Triage Agent

## 1. Technical Terms for this Problem

|My concept|Technical term|
|---|---|
|Decide how urgently a patient should be handled|**Triage**|
|Decide the level of urgency|**Urgency / acuity classification**|
|Send the patient to an appropriate pathway|**Care routing**|
|Low, medium, high urgency|**Latent/hidden states**|
|Information available to the agent|**Observations / evidence**|
|Missing information|**Incomplete information**|
|Making a decision without complete information|**Decision-making under uncertainty**|
|Agent's possible choices|**Actions / decisions**|
|Asking another question|**Information gathering**|
|Choosing not to make a decision|**Abstention / deferral**|
|Sending the case to a person|**Human-in-the-loop / human escalation**|
|Routing to lower urgency than appropriate|**Under-triage**|
|Routing to higher urgency than appropriate|**Over-triage**|
|Probability assigned to possible states|**Belief / probability distribution**|
|Updating belief after evidence|**Bayesian updating**|
|Different consequences for different errors|**Cost-sensitive decision-making**|
|Measuring how uncertain the model is|**Uncertainty estimation**|

---
# 2. Useful Search Queries
Use search queries in groups instead of searching only for "AI appointment agent."

### Understanding the problem
```
AI triage incomplete information
clinical triage decision making under uncertainty
AI assisted patient triage
AI care routing healthcare
urgency classification healthcare
```

### Hidden states and uncertainty
```
hidden state decision making under uncertainty
latent state clinical decision making
uncertainty aware clinical AI
clinical decision making incomplete information
AI triage uncertainty estimation
```

### Evidence and information gathering
```
AI triage missing patient information
clinical triage incomplete patient information
information gathering clinical decision making
AI triage asking additional questions
sequential decision making healthcare
```

### Actions and decisions
```
clinical decision support triage
AI care routing decision support
human in the loop clinical triage
AI triage abstention
AI clinical decision deferral
```

### Errors and safety
```
AI triage under-triage over-triage
clinical triage errors
AI triage safety evaluation
cost sensitive clinical triage
AI triage false negative false positive
```

### Evaluation
```
AI triage evaluation
AI triage emergency recall
AI triage under-triage rate
uncertainty aware triage evaluation
selective prediction clinical AI
```

---

# 3. Relevant Reddit Communities

Investigate the following communities:

1. **r/nursing**
2. **r/medicine**
3. **r/emergencymedicine**
4. **r/healthIT**
5. **r/HealthInformatics**
6. **r/medicalschool**
7. **r/MachineLearning**
8. **r/ArtificialIntelligence**
---


# 6. About Hidden States, Evidence, Actions, and Errors

## A. Hidden States
Currently defines hidden states as:

```
Low urgency
Medium urgency
High urgency
```

## B. Evidence
Need to determine what the agent can actually observe.


## C. Actions
Need to determine what the agent can do.
- Low-urgency routing
- Medium-urgency routing
- High-urgency routing
- Ask for more information
- Escalate to a human

## D. Errors
Need to understand what can go wrong.

### Under-triage

The agent selects a lower urgency level than the reference decision.

### Over-triage

The agent selects a higher urgency level than the reference decision.
