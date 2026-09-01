# Research File — AI Appointment/Triage Agent

## 1. Technical Terms for My Problem

My problem is:

> **An AI agent must decide the urgency of a patient-routing case when the available information is incomplete.**

I am using **low urgency, medium urgency, and high urgency** as my initial hidden states.

The technical terms I need to research are:

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

I will treat these as **research terms**, not automatically as definitions of my final system.

Recent research describes triage as a decision problem involving incomplete information and uncertainty, which makes these terms relevant to my investigation.

---

# 2. Useful Search Queries

I will use search queries in groups instead of searching only for "AI appointment agent."

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

These searches should help me investigate the problem without assuming in  
advance that a particular model or method is correct.

---

# 3. Relevant Reddit Communities

I will investigate the following communities:

1. **r/nursing**
2. **r/medicine**
3. **r/emergencymedicine**
4. **r/healthIT**
5. **r/HealthInformatics**
6. **r/medicalschool**
7. **r/MachineLearning**
8. **r/ArtificialIntelligence**

I will use Reddit primarily to understand **real-world experiences,  
workflow problems, opinions, and questions worth researching**.

I will not use Reddit discussions as authoritative evidence for medical  
routing rules.

---

# 4. Why Each Community Is Relevant

### 1. r/nursing

This community is relevant because nurses have direct experience with  
triage, patient assessment, prioritization, and incomplete information.

For example, discussions from nurses describe the difficulty of phone triage  
because the nurse must make decisions from what the patient reports rather  
than from a complete examination.

**What I want to learn:**

- How humans handle incomplete information.
- What questions they ask.
- What makes triage difficult.
- Where uncertainty appears.
- What kinds of errors concern practitioners.

---

### 2. r/medicine

This community is relevant because physicians discuss clinical decision  
support, AI in medicine, triage, and the limitations of AI systems.

There are discussions about how AI is currently being used in healthcare and  
where human review remains important.

**What I want to learn:**

- Physician perspectives on AI.
- Clinical decision-making problems.
- Concerns about AI errors.
- Human oversight.

---

### 3. r/emergencymedicine

This is particularly relevant because emergency medicine directly involves  
prioritizing patients according to urgency.

The community contains discussions specifically about triage processes and  
how clinicians determine priority from limited information.

**What I want to learn:**

- How urgency is determined.
- What information is important at the beginning.
- How incomplete information affects decisions.
- How triage workflows operate.

---

### 4. r/healthIT

This community is relevant to the **technology and healthcare workflow**  
side of my problem.

There are discussions about AI in medicine, clinical systems, workflow, and  
how AI could support rather than replace healthcare professionals.  

**What I want to learn:**

- How AI fits into healthcare systems.
- Where human review is needed.
- Technical implementation concerns.
- Workflow limitations.

---

### 5. r/HealthInformatics

This community is relevant because it connects healthcare with information  
systems, data, AI, and clinical decision support.

Recent discussions include practical concerns about AI being used during  
healthcare encounters and the need for auditing and human review.  

**What I want to learn:**

- Healthcare AI workflows.
- Clinical decision-support systems.
- Data problems.
- Human-AI interaction.
- Safety and auditing.

---

### 6. r/medicalschool

This community can help me understand how medical trainees think about  
clinical reasoning and prioritization.

There are also discussions about AI triage and concerns about incomplete  
patient histories.

**What I want to learn:**

- How people reason from patient information.
- How missing information affects decisions.
- What humans look for when prioritizing patients.

---

### 7. r/MachineLearning

This community is relevant to the **technical side** of my problem.

It can help me investigate:

- machine learning for healthcare;
- incomplete/noisy data;
- uncertainty;
- classification;
- evaluation.

There are discussions specifically about AI in medicine and challenges such  
as heterogeneous inputs and labeling problems.

---

### 8. r/ArtificialIntelligence

This community is useful for broader discussions around AI capabilities,  
limitations, reliability, and healthcare applications.

I will use it mainly to discover ideas and discussions rather than as a  
source of clinical evidence.

---

# 5. Relevant Researchers and Engineers on X

I want to follow people working around:

- healthcare AI;
- machine learning;
- clinical decision support;
- medical informatics;
- AI safety;
- human-AI interaction.

### Suchi Saria

**X:** `@suchisaria`

Relevant because her research focuses on AI/ML in healthcare, including  
clinical applications and robustness.

### Ziad Obermeyer

Relevant areas:

- machine learning in healthcare;
- clinical prediction;
- healthcare systems;
- algorithmic decision-making.

### Jenna Wiens

Relevant because her research sits directly at the intersection of **AI,  
machine learning, and healthcare**. Her research group specifically studies  
real-world healthcare problems using ML and AI.

### Isaac Kohane

**X:** `@zakkohane`

Relevant because he works at the intersection of computer science and  
biomedicine and leads work in biomedical informatics. His X profile confirms  
this focus.

### Eric Topol

**X:** `@EricTopol`

Relevant because he is a physician-scientist who frequently discusses AI,  
medicine, and healthcare technology.

### What I want to learn from X

I will not treat posts from these researchers as medical evidence.

Instead, I want to use X to:

- find papers;
- discover researchers;
- identify current research questions;
- understand debates;
- find technical approaches;
- find discussions about AI limitations and safety.

---

# 6. Questions About Hidden States, Evidence, Actions, and Errors

## A. Hidden States

I currently define my hidden states as:

```
Low urgency
Medium urgency
High urgency
```

Questions I need to investigate:

1. Why should urgency be considered a hidden state?
2. What exactly does low urgency mean?
3. What exactly does medium urgency mean?
4. What exactly does high urgency mean?
5. Are three states enough?
6. Can the true state be uncertain?
7. Can two different states produce similar evidence?
8. What evidence allows me to distinguish between the states?
9. Could my state definitions be too simplified?

---

## B. Evidence

I need to determine what the agent can actually observe.

Questions:

1. What information can the patient provide?
2. Which information is relevant to urgency?
3. Which information can be missing?
4. How should missing information be represented?
5. Can evidence contradict itself?
6. How reliable is patient-provided information?
7. Which evidence is most useful for distinguishing low, medium, and high  
    urgency?
8. Which evidence needs a clinical source?
9. Can asking another question provide useful evidence?
10. Which question would reduce uncertainty the most?

---

## C. Actions

I need to determine what the agent can do.

Possible actions I want to investigate:

```
Low-urgency routing
Medium-urgency routing
High-urgency routing
Ask for more information
Escalate to a human
```

Questions:

1. Should the agent always make a routing decision?
2. Can asking a question be considered an action?
3. When should the agent ask another question?
4. When should it stop asking questions?
5. When should it escalate?
6. Should the agent be allowed to say "I don't know"?
7. Should high uncertainty change the selected action?
8. Should the agent consider the consequences of each action?

---

## D. Errors

I need to understand what can go wrong.

### Under-triage

The agent selects a lower urgency level than the reference decision.

Questions:

1. How should I measure under-triage?
2. Are all under-triage errors equally important?
3. Which under-triage errors are most serious?

### Over-triage

The agent selects a higher urgency level than the reference decision.

Questions:

1. How should I measure over-triage?
2. What are the consequences of unnecessary high-urgency routing?
3. Should over-triage and under-triage have different costs?

### General errors

1. What happens when information is missing?
2. What happens when information contradicts itself?
3. What happens when the agent is uncertain?
4. What happens when the agent chooses the wrong urgency?
5. What happens when the agent should have asked another question?
6. What happens when the agent should have escalated?

---

# 7. Claims That Need a Source or a Test

I need to separate **claims about the real world** from **claims about my  
agent**.

## Claims that need a source

These are claims I should verify using clinical or academic sources:

- What low, medium, and high urgency mean.
- Which evidence is clinically relevant to urgency.
- Which symptoms or observations are associated with different urgency  
    levels.
- What constitutes under-triage and over-triage.
- What existing triage systems use.
- What risks are associated with incorrect triage.
- What human triage processes currently do.
- Whether a particular AI/ML method has previously been used for triage.

For example, I should not simply assume that a particular symptom means  
"high urgency." That needs an appropriate clinical source.

---

## Claims that need a test

These are claims about my proposed agent:

- My agent can distinguish the three urgency states.
- One policy performs better than another.
- Probability improves the decision.
- Asking another question reduces uncertainty.
- Asking another question improves routing.
- An uncertainty-aware policy reduces under-triage.
- Human escalation reduces serious errors.
- A particular probability threshold is useful.
- One type of evidence is more useful than another.

I should not call these facts until I test them.

---

## Claims that may need both

Some claims require **external evidence + experimentation**.

For example:

> "This piece of information is clinically relevant and adding it improves  
> my agent's routing."

The first part requires a source.

The second part requires a test.

---

# 8. Parts of My Problem That Are Not Clear

I currently have several unresolved parts.

### 1. What exactly is low urgency?

I have named the state, but I have not yet defined its boundary.

### 2. What exactly is medium urgency?

I have named the state, but I have not yet defined its boundary.

### 3. What exactly is high urgency?

I have named the state, but I have not yet defined its boundary.

### 4. Are three hidden states sufficient?

I currently use:

```
Low → Medium → High
```

but I need to investigate whether this simplification is appropriate for my  
research experiment.

### 5. What evidence should the agent receive?

I have not yet finalized the input variables.

### 6. How should missing information be represented?

I need to decide whether missing information should cause the agent to ask  
another question, lower confidence, or trigger escalation.

### 7. What actions should the agent have?

I know that routing is an action, but I still need to investigate whether  
asking questions and escalating should also be part of the action space.

### 8. How should I define the correct decision?

I need a reliable reference or labeling process for my test cases.

### 9. How should I measure errors?

I need to determine which metrics are appropriate.

### 10. How should uncertainty affect the decision?

I have not yet determined when the agent should:

```
Make a decision
       OR
Ask another question
       OR
Escalate
```

### 11. What setting am I studying?

I still need to specify whether my prototype represents:

- an appointment system;
- a primary-care intake system;
- an online patient portal;
- telephone/message triage;
- or another setting.

### 12. What population am I studying?

I have not yet specified the population for the experiment.

---

## Research Principle

I will follow this rule throughout my research:

> **If I do not have evidence, I will label something as an assumption,  
> hypothesis, or question rather than presenting it as a fact.**

My research file therefore separates:

**What I know → What I need to verify → What I need to test → What is still unclear.**

This keeps the research file focused on the **research questions**, rather than prematurely turning it into my probabilistic model.