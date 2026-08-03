# C1798---Agentic-AI-for-Digital-Marketing-and-Advertising

Aligned non-WSQ courseware for **Agentic AI for Digital Marketing and Advertising**.

## Package

- Trainer slide deck and learner-slide PDF in `courseware/`
- Learner Guide in DOCX, PDF, and Markdown
- Lesson Plan in DOCX and PDF
- Twelve connected hands-on labs in `labs/`
- Single-source generators in `.agents/skills/non-wsq-courseware-build/`

The course uses the fictional **Aurora Active / HydraLoop** campaign and synthetic data throughout. No live social post, campaign launch, or advertising-budget change is required by the labs.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$PWD" bash .agents/skills/non-wsq-courseware-build/build/build_courseware.sh
```

## Source of truth

Course metadata, topic teaching, schedule, and version history live in `course_data.py`; the twelve labs live in `data_domain1.py` through `data_domain6.py`. The build pipeline uses those same files to generate the PPT, Learner Guide, Lesson Plan, and lab Markdown so titles, numbering, outcomes, and steps stay aligned.
