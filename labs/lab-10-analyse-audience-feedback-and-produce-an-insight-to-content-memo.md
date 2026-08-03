# Lab 10 — Analyse Audience Feedback and Produce an Insight-to-Content Memo

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 5:** Agentic AI for Social Media Performance Monitoring  
**Maps to:** LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations  
**Tools:** Aurora comments CSV, Lab 9 dashboard, spreadsheet application, classroom-approved AI assistant  
**Duration:** 40 minutes

---

## Goal

LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations.

## What You Will Do

You classify twelve synthetic comments by sentiment, theme, severity, and owner, then review the AI labels against the original text. You combine comment evidence with the dashboard to propose one bounded content revision and one experiment.

## What You Will Build

05-monitor/10-comment-analysis.xlsx and 05-monitor/10-insight-to-content-memo.md with reviewed labels, escalation routes, representative evidence, and a controlled next action.

## Prerequisites

- Complete Lab 9 and keep the dashboard open.
- Open labs/resources/aurora-comments.csv.
- Use a spreadsheet application, document editor, and classroom-approved AI assistant.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Save aurora-comments.csv as 05-monitor/10-comment-analysis.xlsx. Add columns D Sentiment, E Theme, F Severity, G Evidence Phrase, H Suggested Owner, I Draft Response, J Human Review, and K Reviewer Note.**

**2. Send all twelve synthetic comments to the AI assistant with the exact schema below. Ask for one row per comment_id and no invented product facts.**

```text
Classify each supplied synthetic comment. Return a Markdown table with Comment ID, Sentiment (positive/neutral/negative/mixed), Theme (price/leak concern/hydration routine/colour/cleaning/team bundle/offer/claim trust/other), Severity (routine/investigate/urgent), Evidence Phrase, Suggested Owner (community/product/brand/legal/privacy), Draft Response, and Human Review (yes/no). Preserve the comment ID. For claim-trust, legal, health, safety, privacy, or uncertain product facts, set Human Review=yes and do not invent an answer.
```

**3. Copy the labels into columns D:J. Compare every row with the original comment. In K record confirmed or the exact manual correction; never accept a label without reading the source row.**

**4. Verify C06 and C07 are theme claim trust, severity investigate or urgent, Suggested Owner brand or legal, and Human Review yes. Verify C11 also routes to review because it raises health-claim risk.**

**5. Create a Summary sheet with counts by Sentiment, Theme, Severity, Suggested Owner, and Human Review. Add one representative comment_id for the three most frequent themes.**

**6. Create 05-monitor/10-insight-to-content-memo.md with headings Quantitative Observation, Qualitative Observation, Interpretation, Alternative Explanation, Recommendation, Evidence, Owner, Guardrail, and Next Check.**

**7. Under Quantitative Observation cite P08's low CTR and P10's leading click count from Lab 9. Under Qualitative Observation cite C06 and C07 as claim-trust concerns and C01/C04 as leak-proof questions. Do not copy names or infer customer traits.**

**8. Mark P08 / LEGACY-FAIL-01 DO NOT REUSE and replace that negative-control concept with a product-owner-approved, clearly described leak-resistance demonstration. State that the demonstration result must exist before a performance claim is written.**

**9. Define the next check as controlled hook experiment EXP-01 with claim-trust comments as a guardrail and link CTR as the primary KPI. Assign product owner and brand reviewer. Save both files.**

## Test It

All twelve comment IDs have reviewed labels and reviewer notes. C06, C07, and C11 require human review. The memo cites P08, P10, C01, C04, C06, and C07; separates observation from interpretation; marks P08 / LEGACY-FAIL-01 DO NOT REUSE; and proposes EXP-01 without asserting an unperformed result.

## Checkpoint for the Next Lab

A reviewed audience-feedback table and evidence-linked memo that feeds paid-media diagnosis and optimization design.

## Troubleshooting

- **The assistant returns fewer than twelve rows:** List the missing comment IDs explicitly and request only those rows using the same schema.
- **A draft response invents a product answer:** Replace it with an acknowledgement and route to PRODUCT_OWNER; keep Human Review yes.
- **The memo treats sentiment as representative of all customers:** State the sample size, synthetic source, and that comments are directional qualitative evidence only.

## Challenge

Add a confidence column and require low-confidence or mixed labels to be reviewed by a second learner before they enter the summary.

## Reflection

What useful context did the comments add that the dashboard metrics alone could not provide?

---

[← Lab 9](lab-09-build-a-social-performance-dashboard-with-defined-metrics.md) · [Lab 11 →](lab-11-diagnose-paid-media-anomalies-before-recommending-a-change.md)
