# Lab 1 — Map the Aurora Agentic Marketing Control Loop

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 1:** Foundations of Agentic AI for Marketing  
**Maps to:** LO1: Explain agentic marketing architecture and define goals, tools, memory, approval gates, and operational guardrails for a marketing agent  
**Tools:** Aurora brand brief, document editor, classroom-approved AI assistant  
**Duration:** 40 minutes

---

## Goal

LO1: Explain agentic marketing architecture and define goals, tools, memory, approval gates, and operational guardrails for a marketing agent.

## What You Will Do

You turn the Aurora Active launch brief into a visible Goal-Sense-Reason-Act-Learn control loop. You decide which actions may run automatically, which remain draft-only, and which need a named human owner. The result becomes the architecture reference for all later labs.

## What You Will Build

01-foundation/01-agent-canvas.md containing the campaign goal, state, inputs, decisions, outputs, permissions, approval gates, stop conditions, and audit fields.

## Prerequisites

- Read labs/resources/aurora-brand-brief.md.
- Create aurora-campaign/01-foundation exactly as shown in the labs/README.md Setup section.
- Open a document editor and a classroom-approved AI assistant.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Create 01-foundation/01-agent-canvas.md. Add the headings Goal, Sense, Reason, Act, Learn, Permissions, Stop Conditions, and Audit Record.**

**2. Under Goal, copy the business objective, audience segments, primary KPI, secondary KPIs, and guardrails from the Aurora brief. Add the decision horizon: four-week launch.**

**3. Under Sense, list the only inputs the system may use in this course: the approved brand brief, synthetic trend records, synthetic content results, synthetic comments, and synthetic advertising results. For each input add owner, observed_at, and source fields.**

**4. Under Reason, define the four decisions the system may support: rank a trend, choose a message angle, diagnose performance, and propose one reversible experiment. Add the rule 'missing evidence routes to review.'**

**5. Under Act, create four outputs: trend brief, content kit, campaign calendar, and optimization proposal. Mark every output DRAFT when first created.**

**6. Create this permission table: READ for approved sources; CALCULATE for spreadsheet metrics; DRAFT for briefs and creative; RECOMMEND for experiments; APPROVE for a named human owner; EXECUTE disabled in class. Add publish, targeting, and spend as approval-gated actions.**

```text
READ -> approved synthetic/public inputs only
CALCULATE -> formulas and summaries
DRAFT -> content and plans; never public
RECOMMEND -> one bounded reversible action
APPROVE -> human campaign owner only
EXECUTE -> disabled during class
```

**7. Ask the AI assistant to critique the canvas. Paste only the fictional brief and your canvas; do not paste account information or credentials.**

```text
You are reviewing a marketing-agent control canvas. Check whether the goal is measurable, every input has provenance, every action has a permission level, high-impact actions have a named approval gate, and stop conditions are observable. Return a table with Gap, Why it matters, Exact revision, and Owner. Do not invent product facts.
```

**8. Apply at least three useful revisions. Under Stop Conditions add: missing or stale source, tracking_status not ok, unsupported claim, risk score 4 or 5, spend-cap breach, and repeated failure. State the safe response for each.**

**9. Under Audit Record, add fields for run_id, input_version, prompt_version, output_version, decision, reason, owner, status, timestamp_sgt, and rollback_version. Save the file.**

## Test It

Open 01-agent-canvas.md and point to all five loop stages, at least six permissioned actions, three approval-gated actions, six stop conditions with safe responses, and the ten audit fields. EXECUTE must be disabled and the campaign goal must match the Aurora brief.

## Checkpoint for the Next Lab

A versioned agent canvas that will govern every later Aurora campaign artifact.

## Troubleshooting

- **The canvas describes a chatbot but no state:** Add the exact input and output versions retained between stages, plus the current campaign status.
- **The AI suggests publishing or changing spend:** Move that action to APPROVE, keep EXECUTE disabled, and name the campaign owner.
- **A guardrail says only 'be safe':** Rewrite it as a detectable condition, an owner, and a specific block, hold, or escalation response.

## Challenge

Add a RACI row for marketing owner, analyst, brand reviewer, and privacy contact at each state transition.

## Reflection

Which single action in your canvas creates the largest downside if the system is wrong, and why is its current gate proportionate?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-write-and-test-the-marketing-agent-operating-specification.md)
