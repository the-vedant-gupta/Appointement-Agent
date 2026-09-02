# Appointment Agent: AI-Driven Medical Triage Under Uncertainty

An AI agent research project designed to route patient appointments to routine, urgent, or emergency care pathways while handling incomplete or uncertain patient information safely and responsibly.

## 🎯 Problem Statement

Healthcare systems need intelligent routing mechanisms that can:
- **Route patients appropriately** to routine, urgent, or emergency care
- **Avoid diagnosis** while making safe triage decisions
- **Handle uncertainty** when patient information is incomplete
- **Make cost-aware decisions** balancing under-triage and over-triage risks

This project explores how AI can make safe routing decisions under uncertainty without overstepping into medical diagnosis.

## 🔬 Research Question

**How should an AI agent make a safe routing decision when patient information is incomplete or uncertain?**

### Key Research Areas

- Decision-making under uncertainty
- AI triage and risk assessment
- Bayesian reasoning and probabilistic inference
- Decision theory and cost-sensitive classification
- Under-triage vs. over-triage trade-offs
- Human-in-the-loop AI systems
- Uncertainty estimation and safety evaluation

## 📋 Possible Agent Actions

1. **Routine routing** - Standard appointment scheduling
2. **Urgent routing** - Accelerated scheduling (within 24-48 hours)
3. **Emergency routing** - Immediate care referral
4. **Ask for more information** - Request additional patient details
5. **Escalate to human** - Defer to medical professional judgment

## 📁 Project Structure

```
Appointement-Agent/
├── src/                          # Python source code
│   ├── agent/                    # Agent implementation
├── data/                         # Test cases and datasets
├── architecture/                 # System architecture documentation
├── review record/                # Review and evaluation records
├── probability-decision-record.md # Probability analysis & decisions
├── research-file.md              # Detailed research findings
├── readme.md                     # This file
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- 
## 📊 Goal

Build and evaluate a small simulation of an uncertainty-aware appointment/triage agent using **30–50 test cases**.

**Objectives:**
-  Implement baseline decision logic
-  Create test dataset (30-50 scenarios)
-  Evaluate routing accuracy
-  Assess under-triage and over-triage rates
-  Document uncertainty handling approach

## 🔐 Safety & Disclaimers

### Safety Boundary
⚠️ **This project is a research prototype.** It:
- Does **NOT** diagnose medical conditions
- Does **NOT** provide medical advice
- Is **NOT** intended for clinical use
- Should **NOT** replace professional medical judgment

This system is designed for research and evaluation purposes only.

## 📚 Key Documentation

- **[Probability Decision Record](probability-decision-record.md)** - Detailed probability analysis, decision thresholds, and reasoning
- **[Research File](research-file.md)** - Comprehensive research findings, literature review, and analysis

## 🧪 Evaluation Metrics

The agent will be evaluated on:
- **Routing accuracy** - Correct category assignment
- **Under-triage rate** - Cases incorrectly classified as less urgent
- **Over-triage rate** - Cases incorrectly classified as more urgent
- **Escalation rate** - Appropriate human-in-the-loop decisions
- **Uncertainty quantification** - Quality of confidence estimates

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m "Add improvement"`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is provided as-is for research purposes. See LICENSE file for details.

## 🔗 Related Work

This project draws from research in:
- Medical decision support systems
- Uncertainty quantification in AI
- Triage protocols and algorithms
- Human-AI collaboration
- Safety-critical AI systems

---

**Last Updated:** September 2, 2026

**Status:** Active Research Phase 1
