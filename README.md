<div align="center">

# Agentic AI for Digital Marketing and Advertising

[![Course](https://img.shields.io/badge/Course-C1798-1f6feb?style=for-the-badge)](https://www.tertiarycourses.com.sg/agentic-ai-for-digital-marketing-and-advertising.html)
[![Agentic AI](https://img.shields.io/badge/Focus-Agentic_AI-7c3aed?style=for-the-badge)](#architecture)
[![Digital Marketing](https://img.shields.io/badge/Domain-Digital_Marketing-10b981?style=for-the-badge)](#lab-activities)
[![Labs](https://img.shields.io/badge/Hands--on_Labs-12-f59e0b?style=for-the-badge)](labs/)
[![License](https://img.shields.io/badge/License-Educational-fbbf24?style=for-the-badge)](#license)

**Hands-on courseware for designing governed agentic marketing systems—from trend discovery and multi-platform content creation to performance monitoring and bounded advertising optimization.**

[📘 Course Page](https://www.tertiarycourses.com.sg/agentic-ai-for-digital-marketing-and-advertising.html) · [📖 Learner Guide](LG-Agentic%20AI%20for%20Digital%20Marketing%20and%20Advertising%20(C1798).md) · [🐛 Report Bug](https://github.com/tertiarycourses/C1798---Agentic-AI-for-Digital-Marketing-and-Advertising/issues) · [💡 Request Feature](https://github.com/tertiarycourses/C1798---Agentic-AI-for-Digital-Marketing-and-Advertising/issues)

</div>

> [!NOTE]
> **These are the official hands-on materials for the non-WSQ course:**
> ### 🎓 Agentic AI for Digital Marketing and Advertising
> **Course Code:** `C1798` · by Tertiary Courses / Tertiary Infotech
> **Course page:** https://www.tertiarycourses.com.sg/agentic-ai-for-digital-marketing-and-advertising.html

---

## Lab Activities

**Lab 1 — Map the Aurora Agentic Marketing Control Loop** · Define the goal, tools, state, approval gates, guardrails, and evidence trail for a fictional campaign agent.

**Lab 2 — Write and Test the Marketing Agent Operating Specification** · Turn the control-loop design into a testable operating contract with allowed actions and failure routes.

**Lab 3 — Build and Score a Source-Linked Trend Signal Table** · Validate synthetic trend signals, calculate an opportunity score, and apply a separate risk veto.

**Lab 4 — Generate a Viral Opportunity Brief and Scheduled Research Spec** · Produce an evidence-linked brief plus a reproducible, versioned weekly research workflow.

**Lab 5 — Create a Governed Four-Platform Content Kit** · Adapt one verified message for Instagram, Facebook, LinkedIn, and X while preserving claims and accessibility.

**Lab 6 — Design a Branded Image Concept and Short-Form Video Storyboard** · Create or wireframe a reviewable image concept and a six-scene, 15-second vertical-video storyboard.

**Lab 7 — Build the Campaign Blueprint, KPI Tree, and Experiment Map** · Connect business outcomes, segments, channel roles, decision KPIs, guardrails, and a bounded experiment.

**Lab 8 — Create the Content Calendar and Run a Controlled Launch Dry-Run** · Build a versioned calendar and validate launch controls without publishing or activating a campaign.

**Lab 9 — Build a Social Performance Dashboard with Defined Metrics** · Calculate denominator-aware social metrics, aggregate results correctly, and create labelled charts.

**Lab 10 — Analyse Audience Feedback and Produce an Insight-to-Content Memo** · Review AI-assisted comment labels, route claim risks, and connect qualitative evidence to the next test.

**Lab 11 — Diagnose Paid-Media Anomalies Before Recommending a Change** · Calculate CTR, conversion rate, CPA, and ROAS while checking tracking quality and campaign-day spend caps first.

**Lab 12 — Design and Simulate a Human-Governed Optimization Loop** · Integrate the course outputs into an auditable observe–validate–diagnose–propose–approve–learn loop.

---

## About

This repository contains the complete courseware and connected lab materials for **Agentic AI for Digital Marketing and Advertising** (**C1798**) by Tertiary Courses / Tertiary Infotech. The twelve activities form one progressive campaign journey: learners design an agent, research trends, create governed content, plan a controlled launch, interpret performance, and simulate bounded optimization decisions.

All practical work uses the fictional **Aurora Active / HydraLoop** campaign and synthetic datasets. Public posting, live campaign activation, targeting changes, and advertising-spend changes remain outside the classroom workflow; impactful actions are prepared as reviewable proposals with named owners and stop conditions.

### What you'll learn

| # | Activity | Concepts |
|---|----------|----------|
| **1** | **Agentic Marketing Control Loop** | Goals, tools, state, memory boundaries, approvals, guardrails |
| **2** | **Agent Operating Specification** | Input/output contracts, permissions, exception routes, audit evidence |
| **3** | **Trend Signal Scorecard** | Source provenance, freshness, normalization, scoring, risk veto |
| **4** | **Opportunity Brief and Research Workflow** | Evidence-linked recommendations, schedules, deduplication, expiry |
| **5** | **Four-Platform Content Kit** | Message hierarchy, channel adaptation, claim ledger, accessibility, version review |
| **6** | **Image Concept and Video Storyboard** | Prompt anatomy, visual continuity, safe zones, rights and disclosure checks |
| **7** | **Campaign Blueprint and Experiment Map** | KPI trees, metric definitions, controlled variables, decision thresholds |
| **8** | **Content Calendar and Launch Dry-Run** | States, ownership, readiness formulas, rollback versions, zero-live verification |
| **9** | **Social Performance Dashboard** | Reach, impressions, CTR, engagement rate, weighted aggregation, chart design |
| **10** | **Audience Feedback Analysis** | Sentiment and theme review, severity routing, evidence-linked content decisions |
| **11** | **Paid-Media Diagnostics** | CTR, click conversion, CPA, ROAS, tracking quality, spend-cap validation |
| **12** | **Human-Governed Optimization Loop** | Approval gates, cooldowns, idempotency, scaling thresholds, rollback and audit logs |

> 📖 **Full walkthrough:** see the [Learner Guide](LG-Agentic%20AI%20for%20Digital%20Marketing%20and%20Advertising%20(C1798).md) and the individual files in [`labs/`](labs/). Slides, the formatted Learner Guide, and the Lesson Plan are in [`courseware/`](courseware/).

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **AI Assistance** | Classroom-approved AI assistant for structured drafting, classification, critique, and control audits |
| **Visual Creation** | Google Gemini image generation, Canva, or a tool-free storyboard/wireframe route |
| **Analytics** | Spreadsheet formulas, pivot tables, charts, and synthetic CSV datasets |
| **Marketing Channels** | Instagram, Facebook, LinkedIn, X, Meta advertising, and Google Ads planning concepts |
| **Governance** | Human approval gates, claim review, privacy boundaries, spend caps, cooldowns, rollback, and audit evidence |
| **Courseware** | PowerPoint via `python-pptx`; Learner Guide and Lesson Plan via `python-docx`; PDF export via LibreOffice |
| **Single Source** | `course_data.py` plus `data_domain1.py`–`data_domain6.py` generate the aligned PPT, LG, LP, and labs |

---

## Architecture

```text
DAY 1 — Agent Foundations · Trend Intelligence · Content Automation
  Lab 1  Agent canvas and control loop
      └─▶ Lab 2  Operating specification and tests
              └─▶ Lab 3  Source-linked trend scorecard
                      └─▶ Lab 4  Opportunity brief + scheduled research spec
                              └─▶ Lab 5  Governed four-platform content kit
                                      └─▶ Lab 6  Image concept + video storyboard

DAY 2 — Campaign Orchestration · Performance Learning · Controlled Optimization
  Lab 7  Campaign blueprint + KPI tree + experiment map
      └─▶ Lab 8  Content calendar + controlled launch dry-run
              └─▶ Lab 9  Social performance dashboard
                      └─▶ Lab 10 Audience feedback + insight-to-content memo
                              └─▶ Lab 11 Paid-media diagnosis
                                      └─▶ Lab 12 Human-governed optimization loop
```

---

## Project Structure

```text
C1798---Agentic-AI-for-Digital-Marketing-and-Advertising/
├── LG-Agentic AI for Digital Marketing and Advertising (C1798).md
├── README.md
├── reference/
│   └── SOURCES.md                    # Official references used by the course
├── labs/
│   ├── README.md                     # Lab index, setup, and continuity map
│   ├── lab-01-*.md … lab-12-*.md    # Connected hands-on activities
│   └── resources/                    # Fictional brief and synthetic CSV datasets
├── courseware/
│   ├── Agentic AI for Digital Marketing and Advertising (C1798)-v1.0.pptx
│   ├── Agentic AI for Digital Marketing and Advertising (C1798)-v1.0.pdf
│   ├── LG-Agentic AI for Digital Marketing and Advertising (C1798).docx / .pdf
│   └── LP-Agentic AI for Digital Marketing and Advertising (C1798).docx / .pdf
└── .agents/skills/non-wsq-courseware-build/
    └── build/                        # Reproducible single-source generators
```

---

## Getting Started

### Prerequisites

- A document editor and spreadsheet application
- A classroom-approved AI assistant
- Optional: Google Gemini image generation or Canva for Lab 6
- No live social-media publishing or advertising-spend access is required

### 1. Clone the repository

```bash
git clone https://github.com/tertiarycourses/C1798---Agentic-AI-for-Digital-Marketing-and-Advertising.git
cd C1798---Agentic-AI-for-Digital-Marketing-and-Advertising
```

### 2. Prepare the lab workspace

Open [`labs/README.md`](labs/README.md), create the six campaign folders shown in its **Setup** section, and keep [`labs/resources/aurora-brand-brief.md`](labs/resources/aurora-brand-brief.md) available throughout the course.

### 3. Complete the labs in order

Start with Lab 1 and carry each checkpoint into the next activity. Every lab includes prerequisites, numbered steps, a **Test It** verification, troubleshooting, a challenge, and reflection prompts.

### 4. Rebuild all courseware

From Git Bash on Windows with Python, LibreOffice, `python-pptx`, `python-docx`, and `pypdf` available:

```bash
COURSE_REPO="$PWD" bash .agents/skills/non-wsq-courseware-build/build/build_courseware.sh
```

The build uses one canonical content model to regenerate the PPT, Learner Guide, Lesson Plan, and twelve lab files together.

---

## Contributing

Contributions, fixes, and improvements are welcome:

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/my-improvement`
3. Commit your changes: `git commit -m "Add my improvement"`
4. Push the branch: `git push origin feature/my-improvement`
5. Open a **Pull Request**

Found a bug or have an idea? Open an [issue](https://github.com/tertiarycourses/C1798---Agentic-AI-for-Digital-Marketing-and-Advertising/issues).

---

## License

This material is provided for **educational use** as part of the course **C1798 — Agentic AI for Digital Marketing and Advertising**. © Tertiary Infotech Pte. Ltd. All rights reserved.

---

## Developed By

**Tertiary Infotech Pte. Ltd.** — [Tertiary Courses](https://www.tertiarycourses.com.sg)

Course: [Agentic AI for Digital Marketing and Advertising (C1798)](https://www.tertiarycourses.com.sg/agentic-ai-for-digital-marketing-and-advertising.html)

## Acknowledgements

- [Anthropic](https://www.anthropic.com/research/building-effective-agents) — practical agent and workflow design patterns
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — risk and governance framing
- [Google Trends](https://trends.google.com/) — relative search-interest concepts
- [Google Ads](https://support.google.com/google-ads/) and [Meta](https://developers.facebook.com/docs/marketing-apis/) — advertising metrics and platform concepts
- Course trainers and learners of C1798

---

<div align="center">

⭐ **If this helped you learn governed agentic marketing, star the repo!**

Powered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/)

[📘 Course Page](https://www.tertiarycourses.com.sg/agentic-ai-for-digital-marketing-and-advertising.html) · [📖 Learner Guide](LG-Agentic%20AI%20for%20Digital%20Marketing%20and%20Advertising%20(C1798).md)

</div>
