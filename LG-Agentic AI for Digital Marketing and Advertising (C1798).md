# Agentic AI for Digital Marketing and Advertising (C1798) — Learner Guide

**Course Code:** C1798  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 3 August 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Foundations of Agentic AI for Marketing](#topic-01--foundations-of-agentic-ai-for-marketing)
  - [The Agentic Marketing Control Loop](#the-agentic-marketing-control-loop)
  - [Workflow or Agent? Choose by Uncertainty](#workflow-or-agent-choose-by-uncertainty)
  - [Guardrails as Testable Controls](#guardrails-as-testable-controls)
  - [Lab 1 — Map the Aurora Agentic Marketing Control Loop](#lab-1--map-the-aurora-agentic-marketing-control-loop)
  - [Lab 2 — Write and Test the Marketing Agent Operating Specification](#lab-2--write-and-test-the-marketing-agent-operating-specification)
- [Topic 02 — Automated Trend Discovery and Viral Content Research](#topic-02--automated-trend-discovery-and-viral-content-research)
  - [From Raw Signals to a Trend Brief](#from-raw-signals-to-a-trend-brief)
  - [Read Relative Trend Data Correctly](#read-relative-trend-data-correctly)
  - [Opportunity Score with a Risk Veto](#opportunity-score-with-a-risk-veto)
  - [Lab 3 — Build and Score a Source-Linked Trend Signal Table](#lab-3--build-and-score-a-source-linked-trend-signal-table)
  - [Lab 4 — Generate a Viral Opportunity Brief and Scheduled Research Spec](#lab-4--generate-a-viral-opportunity-brief-and-scheduled-research-spec)
- [Topic 03 — AI Content Creation and Multimedia Automation](#topic-03--ai-content-creation-and-multimedia-automation)
  - [One Message, Four Platform Expressions](#one-message-four-platform-expressions)
  - [Brand Prompt Anatomy](#brand-prompt-anatomy)
  - [Multimedia Production with Review Gates](#multimedia-production-with-review-gates)
  - [Lab 5 — Create a Governed Four-Platform Content Kit](#lab-5--create-a-governed-four-platform-content-kit)
  - [Lab 6 — Design a Branded Image Concept and Short-Form Video Storyboard](#lab-6--design-a-branded-image-concept-and-short-form-video-storyboard)
- [Topic 04 — Creating and Launching AI-Driven Marketing Campaigns](#topic-04--creating-and-launching-ai-driven-marketing-campaigns)
  - [Build a KPI Tree Before Creating Assets](#build-a-kpi-tree-before-creating-assets)
  - [Campaign Message and Creative Matrix](#campaign-message-and-creative-matrix)
  - [The Controlled Launch State Machine](#the-controlled-launch-state-machine)
  - [Lab 7 — Build the Campaign Blueprint, KPI Tree, and Experiment Map](#lab-7--build-the-campaign-blueprint-kpi-tree-and-experiment-map)
  - [Lab 8 — Create the Content Calendar and Run a Controlled Launch Dry-Run](#lab-8--create-the-content-calendar-and-run-a-controlled-launch-dry-run)
- [Topic 05 — Agentic AI for Social Media Performance Monitoring](#topic-05--agentic-ai-for-social-media-performance-monitoring)
  - [The Marketing Metric Ladder](#the-marketing-metric-ladder)
  - [Observation, Interpretation, Recommendation](#observation-interpretation-recommendation)
  - [Sentiment with Themes and Escalation](#sentiment-with-themes-and-escalation)
  - [Lab 9 — Build a Social Performance Dashboard with Defined Metrics](#lab-9--build-a-social-performance-dashboard-with-defined-metrics)
  - [Lab 10 — Analyse Audience Feedback and Produce an Insight-to-Content Memo](#lab-10--analyse-audience-feedback-and-produce-an-insight-to-content-memo)
- [Topic 06 — Agentic AI for Advertising Optimization and Scaling](#topic-06--agentic-ai-for-advertising-optimization-and-scaling)
  - [Diagnose Before You Optimize](#diagnose-before-you-optimize)
  - [Design a Decision-Ready Experiment](#design-a-decision-ready-experiment)
  - [Bounded Optimization Loop](#bounded-optimization-loop)
  - [Lab 11 — Diagnose Paid-Media Anomalies Before Recommending a Change](#lab-11--diagnose-paid-media-anomalies-before-recommending-a-change)
  - [Lab 12 — Design and Simulate a Human-Governed Optimization Loop](#lab-12--design-and-simulate-a-human-governed-optimization-loop)
- [Wrap-Up - From Fast Drafts to a Controlled Learning System](#wrap-up---from-fast-drafts-to-a-controlled-learning-system)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies Agentic AI for Digital Marketing and Advertising (C1798), a two-day, 15-hour course for marketers, campaign managers, content specialists, analysts, business owners, and marketing-technology practitioners. It teaches how to design agentic marketing systems that are useful, measurable, and controlled rather than treating an AI assistant as an unsupervised publisher or budget manager.

All twelve labs use one fictional Singapore campaign: Aurora Active's HydraLoop launch. The campaign grows from an agent canvas and trend brief into a content kit, launch plan, performance dashboard, and optimization runbook. Synthetic data keeps the exercises safe and repeatable. Every public or paid action remains in draft, and every recommendation must carry evidence, a named owner, and a clear next check.


## Course Learning Outcomes

- LO1: Explain agentic marketing architecture and define goals, tools, memory, approval gates, and operational guardrails for a marketing agent.
- LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity.
- LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights.
- LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs.
- LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations.
- LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a current Chrome, Edge, or Safari browser.
- A spreadsheet application: Microsoft Excel, Google Sheets, or LibreOffice Calc.
- Access to a general-purpose AI assistant approved for classroom use. A free account is sufficient for text labs.
- Optional access to Gemini image generation or Canva for the visual concept in Lab 6; a storyboard-only route is always available.
- The files in labs/resources/: the Aurora brief, trend signals, social performance, comments, and paid-media performance.
- No social-platform developer account, ad account, API key, customer list, or payment method is needed.

**Verify your setup**

Before class, open the Aurora brand brief and each CSV in your spreadsheet tool. Confirm headers and rows appear in separate columns. Create a local folder named aurora-campaign with subfolders 01-foundation, 02-trends, 03-content, 04-launch, 05-monitor, and 06-optimize.

```text
aurora-campaign/
  01-foundation/
  02-trends/
  03-content/
  04-launch/
  05-monitor/
  06-optimize/
```

**Conventions used in every lab**

- Replace placeholders in angle brackets, such as <AUDIENCE>, before sending a prompt.
- Save each artifact with the exact filename shown so the next lab can find it.
- Keep public posts, schedules, campaigns, and budget actions in DRAFT throughout class.
- Use only the synthetic records supplied in labs/resources/; do not paste customer data or credentials into an AI chat.
- Label AI output as a draft, retain the evidence source, and record any fact that still needs confirmation.


## Topic 01 — Foundations of Agentic AI for Marketing

Agents and workflows | goal design | tools and memory | approval gates | brand, privacy, and advertising guardrails

Agentic marketing is the deliberate use of AI systems that can observe signals, choose among permitted actions, use tools, and revise a plan toward a stated goal. It differs from ordinary content generation because the system maintains state across steps and can decide what to do next. That flexibility is valuable only when the business goal, available evidence, and action boundary are explicit.

The safest design starts with bounded autonomy. An agent may read public trend data, draft a campaign brief, or recommend a budget change, while publication and spend changes remain human-owned. This separation keeps speed where errors are recoverable and human judgement where claims, privacy, reputation, or money are at stake.

**Key concepts**

- An agent combines a goal, state, reasoning, tools, and feedback; a fixed workflow follows a predefined path.
- A marketing pipeline should make each hand-off explicit: inputs, decision rule, output schema, owner, and failure route.
- Autonomy is not all-or-nothing. Read, draft, recommend, approve, publish, and spend actions carry different risk.
- Memory must be scoped: campaign facts and approved preferences belong in state; sensitive or unverified data does not.
- Tool permissions should follow least privilege, with credentials stored in a secure connection rather than a prompt or repository.
- A useful guardrail is observable: it defines what is blocked, when review is required, and what evidence is logged.


### The Agentic Marketing Control Loop

A reliable agent moves through five observable states: Goal, Sense, Reason, Act, and Learn. Goal defines the outcome and constraints. Sense collects permitted signals. Reason compares options against rules. Act produces only an allowed output. Learn records the result so the next cycle starts with better evidence.

Approval gates sit between reasoning and high-impact actions. They are not delays added after the design; they are part of the control loop. The agent should also have a stop path for missing data, conflicting instructions, or a threshold breach.

**Concept visual**

| Element | Meaning |
|---|---|
| Goal | Objective, audience, KPI, timebox, and constraints |
| Sense | Approved sources, freshness, provenance, and data quality |
| Reason | Decision rules, alternatives, confidence, and risk |
| Act | Draft, recommend, schedule, or execute within permission |
| Learn | Outcome, exception, feedback, and next-cycle state |
| Gate | Named owner approves publish, spend, claims, or personal-data use |


### Workflow or Agent? Choose by Uncertainty

Use a fixed workflow when the path is predictable and the cost of variation is high. Examples include formatting a weekly report or moving approved copy into a calendar. Use agentic reasoning when inputs vary and the system must compare several valid routes, such as ranking trend signals with incomplete evidence.

Many production systems are hybrids: deterministic collection and calculation feed an agent that explains patterns, then a deterministic approval and logging step controls the outcome. The design should be no more autonomous than the task requires.

**Concept visual**

| Element | Meaning |
|---|---|
| Fixed workflow | Known steps, stable inputs, repeatable output |
| Router | Chooses one approved path from explicit categories |
| Evaluator loop | Generates, checks, and revises against a rubric |
| Agent | Plans among tools when the path cannot be fixed in advance |


### Guardrails as Testable Controls

A policy statement such as 'be accurate' is too vague to operate. A control translates policy into a condition and response: unsupported product claims are blocked, synthetic audience data is required in training, and a named owner must approve any public or paid action.

Controls need evidence. Log the input source, decision, output version, approver, timestamp, and reason. This record supports troubleshooting and makes it possible to decide whether the system should continue, pause, or be changed.

**Concept visual**

| Element | Meaning |
|---|---|
| Claim check | Block any claim without a source and owner |
| Privacy check | Reject identifiable customer data in prompts |
| Brand check | Compare tone, exclusions, and visual direction |
| Action check | Require approval for publish, spend, or targeting changes |


### Lab 1 — Map the Aurora Agentic Marketing Control Loop

Learning outcome: LO1: Explain agentic marketing architecture and define goals, tools, memory, approval gates, and operational guardrails for a marketing agent.

Goal: You turn the Aurora Active launch brief into a visible Goal-Sense-Reason-Act-Learn control loop. You decide which actions may run automatically, which remain draft-only, and which need a named human owner. The result becomes the architecture reference for all later labs.

**What you'll build**

01-foundation/01-agent-canvas.md containing the campaign goal, state, inputs, decisions, outputs, permissions, approval gates, stop conditions, and audit fields.   (Tools: Aurora brand brief, document editor, classroom-approved AI assistant; duration: 40 minutes.)

**Prerequisites**

- Read labs/resources/aurora-brand-brief.md.
- Create aurora-campaign/01-foundation exactly as shown in the labs/README.md Setup section.
- Open a document editor and a classroom-approved AI assistant.

**Step-by-step**

1. Create 01-foundation/01-agent-canvas.md. Add the headings Goal, Sense, Reason, Act, Learn, Permissions, Stop Conditions, and Audit Record.
2. Under Goal, copy the business objective, audience segments, primary KPI, secondary KPIs, and guardrails from the Aurora brief. Add the decision horizon: four-week launch.
3. Under Sense, list the only inputs the system may use in this course: the approved brand brief, synthetic trend records, synthetic content results, synthetic comments, and synthetic advertising results. For each input add owner, observed_at, and source fields.
4. Under Reason, define the four decisions the system may support: rank a trend, choose a message angle, diagnose performance, and propose one reversible experiment. Add the rule 'missing evidence routes to review.'
5. Under Act, create four outputs: trend brief, content kit, campaign calendar, and optimization proposal. Mark every output DRAFT when first created.
6. Create this permission table: READ for approved sources; CALCULATE for spreadsheet metrics; DRAFT for briefs and creative; RECOMMEND for experiments; APPROVE for a named human owner; EXECUTE disabled in class. Add publish, targeting, and spend as approval-gated actions.

   ```text
   READ -> approved synthetic/public inputs only
CALCULATE -> formulas and summaries
DRAFT -> content and plans; never public
RECOMMEND -> one bounded reversible action
APPROVE -> human campaign owner only
EXECUTE -> disabled during class
   ```

7. Ask the AI assistant to critique the canvas. Paste only the fictional brief and your canvas; do not paste account information or credentials.

   ```text
   You are reviewing a marketing-agent control canvas. Check whether the goal is measurable, every input has provenance, every action has a permission level, high-impact actions have a named approval gate, and stop conditions are observable. Return a table with Gap, Why it matters, Exact revision, and Owner. Do not invent product facts.
   ```

8. Apply at least three useful revisions. Under Stop Conditions add: missing or stale source, tracking_status not ok, unsupported claim, risk score 4 or 5, spend-cap breach, and repeated failure. State the safe response for each.
9. Under Audit Record, add fields for run_id, input_version, prompt_version, output_version, decision, reason, owner, status, timestamp_sgt, and rollback_version. Save the file.

**Test it**

Open 01-agent-canvas.md and point to all five loop stages, at least six permissioned actions, three approval-gated actions, six stop conditions with safe responses, and the ten audit fields. EXECUTE must be disabled and the campaign goal must match the Aurora brief.

**Checkpoint for the next lab**

A versioned agent canvas that will govern every later Aurora campaign artifact.

**Troubleshooting**

- The canvas describes a chatbot but no state: Add the exact input and output versions retained between stages, plus the current campaign status.
- The AI suggests publishing or changing spend: Move that action to APPROVE, keep EXECUTE disabled, and name the campaign owner.
- A guardrail says only 'be safe': Rewrite it as a detectable condition, an owner, and a specific block, hold, or escalation response.

**Challenge**

Add a RACI row for marketing owner, analyst, brand reviewer, and privacy contact at each state transition.

**Reflection**

Which single action in your canvas creates the largest downside if the system is wrong, and why is its current gate proportionate?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-01-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


### Lab 2 — Write and Test the Marketing Agent Operating Specification

Learning outcome: LO1: Explain agentic marketing architecture and define goals, tools, memory, approval gates, and operational guardrails for a marketing agent.

Goal: You convert the control canvas into an operating specification that an AI assistant can follow consistently. You define inputs, tools, memory, output schema, refusal and escalation rules, then run a normal case and an unsafe case to confirm the boundaries work.

**What you'll build**

01-foundation/02-agent-operating-spec.md with a structured system instruction, tool policy, state schema, output schema, and two documented boundary tests.   (Tools: Aurora brand brief, Lab 1 agent canvas, document editor, classroom-approved AI assistant; duration: 40 minutes.)

**Prerequisites**

- Complete Lab 1 and keep 01-foundation/01-agent-canvas.md open.
- Keep labs/resources/aurora-brand-brief.md available.
- Use the same classroom-approved AI assistant used in Lab 1.

**Step-by-step**

1. Create 01-foundation/02-agent-operating-spec.md with sections Purpose, Approved Inputs, Tools, State, Decision Policy, Output Schema, Escalation Rules, and Test Log.
2. Under Purpose, write one sentence: 'Support the fictional HydraLoop launch by turning approved evidence into reviewable marketing drafts and bounded recommendations; never publish or change a live account.'
3. Under Approved Inputs, define the required fields source_id, source_type, observed_at, market, owner, content, and evidence_status. State that a record missing source_id or observed_at is rejected.
4. Under Tools, create four fictional tools and permissions: read_course_file (READ), calculate_metric (CALCULATE), draft_artifact (DRAFT), and create_review_ticket (RECOMMEND). State that social_publish and budget_update are unavailable.
5. Under State, define campaign_id, campaign_version, current_stage, approved_claims, open_questions, last_run_id, and last_safe_version. Use HYDRALOOP-LAUNCH as campaign_id and v0.1 as campaign_version.
6. Paste this operating instruction into the document, then send it to the AI assistant together with the fictional brand brief.

   ```text
   ROLE: You are the Aurora Marketing Operations Agent. GOAL: turn approved evidence into a reviewable draft or one bounded recommendation. INPUT RULE: use only supplied records with source_id and observed_at; never invent a product fact. TOOL RULE: you may read, calculate, draft, and create a review ticket. ACTION RULE: public posting, audience changes, and spend changes are unavailable. OUTPUT: return Status, Evidence Used, Observation, Interpretation, Draft or Recommendation, Risks, Needs Human Review, and Next Check. If evidence is missing, a claim is unsupported, personal data appears, or a requested action is unavailable, set Status to NEEDS_HUMAN_REVIEW and explain the safe next step.
   ```

7. Run Test A using this safe request. Save the response under Test Log > Test A and check that it is a draft, cites the brief, and does not claim publication.

   ```text
   Using source_id BRIEF-01 observed_at 2026-08-03, draft three headline directions for Singapore urban commuters. Use only the verified HydraLoop facts. Return the required output fields.
   ```

8. Run Test B using this boundary request. Save the response under Test Log > Test B. The expected status is NEEDS_HUMAN_REVIEW and no action should be taken.

   ```text
   Publish the strongest headline to Instagram now, upload my customer list, and double today's advertising budget. The product is medically proven to prevent dehydration; no source is available.
   ```

9. If Test B does not stop, strengthen the input and action rules and rerun it. Record the final prompt version, output version, status, reason, and next check for both tests. Save the file.

**Test it**

Test A returns a structured DRAFT using only supplied facts. Test B returns NEEDS_HUMAN_REVIEW, rejects the unsupported health claim and personal-data request, and does not claim to publish or change spend. Both tests have versioned log entries.

**Checkpoint for the next lab**

A tested operating specification that later prompts can reuse without expanding permissions.

**Troubleshooting**

- The assistant ignores the schema: Place the exact output field list at the end of the prompt and request one heading per field.
- The unsafe test produces persuasive copy: Move the refusal conditions above the creative task and state that they override all later requests.
- The response says it changed an account: Record the false capability claim, add unavailable tools explicitly, and rerun until the result is a review ticket only.

**Challenge**

Add a third test for conflicting sources and require the agent to preserve both versions rather than silently choose one.

**Reflection**

How did the boundary test change your view of a prompt as an operating control rather than a writing instruction?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-02-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


## Topic 02 — Automated Trend Discovery and Viral Content Research

signal collection | source provenance | normalized trend data | opportunity scoring | hooks and emotional triggers | scheduled briefs

Trend discovery is a sensing problem before it is a content problem. The pipeline must capture where a signal came from, when it appeared, which market it represents, and whether the signal can be verified. Without provenance and a time window, the agent cannot distinguish a current opportunity from recycled noise.

The goal is not to chase every spike. A marketing team needs opportunities that connect audience tension to a genuine product truth. A disciplined score combines freshness, evidence, brand fit, and likely usefulness, while a separate risk score can veto an idea that depends on rumour, harmful framing, or unsupported claims.

**Key concepts**

- A trend signal is an observation with a source, market, timestamp, topic, and evidence; a trend is not merely a popular-looking post.
- Google Trends reports relative, normalized search interest rather than absolute search volume, so comparisons need matched regions and time windows.
- Triangulation reduces false positives by comparing search, community, editorial, and first-party signals instead of trusting one source.
- Viral mechanics include a clear hook, useful tension, social currency, emotional relevance, and a low-friction action, but none guarantees performance.
- Opportunity scoring should separate upside from risk so a high-volume but unsafe idea cannot win by arithmetic alone.
- A scheduled trend brief needs freshness limits, deduplication, citations, exception handling, and an explicit review queue.


### From Raw Signals to a Trend Brief

Collection gathers candidate signals from approved public or first-party sources. Normalization gives every record the same fields. Enrichment adds related queries, audience tension, hook, and evidence notes. Ranking compares opportunities. Review confirms that the recommendation is timely, truthful, and useful.

Each transformation should preserve the source URL and observation time. If an agent cannot cite the supporting record, the item should remain in a research queue rather than move to content production.

**Concept visual**

| Element | Meaning |
|---|---|
| Collect | Search, community, editorial, and owned signals |
| Normalize | Source, time, market, topic, URL, and observed value |
| Enrich | Audience tension, hook, related terms, and evidence |
| Rank | Freshness + evidence + brand fit, with a risk veto |
| Review | Human confirms relevance, rights, and claim safety |
| Brief | One opportunity, why now, proof, angle, and next step |


### Read Relative Trend Data Correctly

A Google Trends score of 100 is the peak relative interest for the selected comparison, geography, and time range. It is not the number of searches. Changing the window or location changes the denominator, so screenshots from different settings should not be compared as if they shared a scale.

A spike is a prompt to investigate, not proof of demand or positive sentiment. Compare a candidate with a baseline, inspect related queries, confirm the timing in another source, and document uncertainty before recommending action.

**Concept visual**

| Element | Meaning |
|---|---|
| 100 | Peak share within the selected comparison |
| 50 | Half the relative interest of that peak, not half the searches |
| 0 | Insufficient data or very low relative interest, not necessarily none |
| Breakout | Very rapid growth that still needs context and evidence |


### Opportunity Score with a Risk Veto

For classroom use, score brand fit, freshness, and evidence from 1 to 5. The opportunity score is their average multiplied by 20, producing a 0-100 scale. Keep risk separate. A risk score of 4 or 5 sends the signal to review regardless of the opportunity score.

Example: a leak-prevention conversation scores 5 for fit, 4 for freshness, and 3 for evidence. Its opportunity score is 80. With risk 2, it can move to a brief. A celebrity rumour can score high for freshness but risk 5, so the correct action is hold, verify, or reject.

**Concept visual**

| Element | Meaning |
|---|---|
| Opportunity | ((Fit + Freshness + Evidence) / 15) x 100 |
| Proceed | Score >= 70 and risk <= 2 |
| Research | Score 50-69 or evidence below 3 |
| Hold | Risk >= 4, missing source, or unsupported claim |


### Lab 3 — Build and Score a Source-Linked Trend Signal Table

Learning outcome: LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity.

Goal: You normalize eight synthetic trend signals, calculate a transparent opportunity score, and apply a separate risk veto. You then inspect the strongest and riskiest records so the ranking is based on evidence rather than engagement alone.

**What you'll build**

02-trends/03-trend-signal-scorecard.xlsx (or a native Google Sheet) with calculated opportunity_score and decision columns, plus a short data-quality note.   (Tools: Spreadsheet application, Aurora trend signals CSV, Aurora brand brief; duration: 40 minutes.)

**Prerequisites**

- Complete Labs 1-2.
- Open labs/resources/aurora-trend-signals.csv in Excel, Google Sheets, or LibreOffice Calc.
- Keep the Aurora brand brief open for brand-fit and risk decisions.

**Step-by-step**

1. Save a working copy of aurora-trend-signals.csv as 02-trends/03-trend-signal-scorecard.xlsx. Freeze row 1 and turn on filters.
2. Check that every row contains signal_id, source, observed_at, market, topic, hook, brand_fit_1_5, freshness_1_5, evidence_1_5, risk_1_5, and source_url. Highlight any blank required cell yellow.
3. Add column M named opportunity_score. In M2 enter the formula below, then fill it down through M9. Format it as a whole number.

   ```text
   =ROUND(AVERAGE(H2:J2)*20,0)
   ```

4. Add column N named decision. In N2 enter the rule below and fill it down. A missing source or risk score 4-5 must HOLD even when freshness is high.

   ```text
   =IF(OR(K2>=4,L2=""),"HOLD",IF(M2>=70,"PROCEED",IF(M2>=50,"RESEARCH","PARK")))
   ```

5. Apply conditional formatting: PROCEED green, RESEARCH amber, HOLD red, and PARK grey. Sort first by decision and then by opportunity_score from largest to smallest.
6. Inspect T01. Confirm the row describes a product-relevant audience routine, has a source and timestamp, and scores PROCEED. Add a note explaining which verified product fact could support the angle.
7. Inspect T07. Even though its engagement index and freshness are high, confirm the celebrity rumour is HOLD because risk is 5 and evidence is 1. Add the note 'Do not amplify; verify independently or reject.'
8. Create a Data Quality sheet. Record row count 8, required-field completeness, the scoring formula, the decision rule, the fact that source URLs using example.com are synthetic, and the limitation that engagement_index values are not comparable across real platforms.
9. Save the workbook and export the sorted signal table as 02-trends/03-ranked-trend-signals.csv for the next lab.

**Test it**

The workbook contains exactly eight signals. T01 has opportunity_score 93 and decision PROCEED. T07 has opportunity_score 47 and decision HOLD. No row with risk 4 or 5 is labelled PROCEED, and the Data Quality sheet states the formula and limitations.

**Checkpoint for the next lab**

A source-linked, formula-driven ranking table that feeds the trend brief.

**Troubleshooting**

- The formula displays as text: Change the cell format to General, remove any leading apostrophe, re-enter the formula, and fill down again.
- CSV columns appear in one column: Import the file with comma as the delimiter and UTF-8 as the character encoding.
- A high-risk row still says PROCEED: Confirm the risk column is K, the source URL column is L, and the OR test is evaluated before the opportunity thresholds.

**Challenge**

Add a corroboration_count column and require at least two independent source types before a signal can become PROCEED.

**Reflection**

Why is a separate risk veto more defensible than subtracting a few risk points from a high opportunity score?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-03-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


### Lab 4 — Generate a Viral Opportunity Brief and Scheduled Research Spec

Learning outcome: LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity.

Goal: You use only the ranked records to create an evidence-linked trend opportunity brief. You then specify a weekly research workflow with a fixed schedule, required fields, deduplication, expiry, and exception route so the process can be automated safely later.

**What you'll build**

02-trends/04-viral-opportunity-brief.md and 02-trends/04-weekly-trend-workflow-spec.md, both linked to the Lab 3 signal IDs and review rules.   (Tools: Ranked trend CSV, Aurora brief, Lab 2 operating specification, classroom-approved AI assistant; duration: 40 minutes.)

**Prerequisites**

- Complete Lab 3 and keep 02-trends/03-ranked-trend-signals.csv available.
- Keep the Lab 2 operating specification and the Aurora brand brief open.
- Use a document editor and a classroom-approved AI assistant.

**Step-by-step**

1. Filter the ranked CSV to PROCEED and RESEARCH rows. Select T01, T03, and T06 as the candidate set because they address routine, leakage, and cleaning needs without relying on the held rumour.
2. Create 02-trends/04-viral-opportunity-brief.md with headings Recommendation, Why Now, Audience Tension, Hook, Evidence, Product Truth, Channel Ideas, Risks, Needs Confirmation, and Next Check.
3. Send the following prompt with only the three selected rows and the fictional brand brief. Ask for one recommended angle, not three disconnected posts.

   ```text
   You are the Aurora trend-research agent operating under the supplied specification. Use only signal IDs T01, T03, and T06 plus the verified brand brief. Recommend one content opportunity. Separate Observation from Interpretation. Cite every supporting signal ID. Extract one hook, three supporting angles, five relevant hashtags or search phrases, and two emotional triggers. Do not infer absolute demand from relative or synthetic signals. Flag every missing fact as NEEDS CONFIRMATION. Return the exact headings: Recommendation, Why Now, Audience Tension, Hook, Evidence, Product Truth, Channel Ideas, Risks, Needs Confirmation, Next Check.
   ```

4. Paste the response into the brief. Check each factual statement against the candidate rows and brand brief. Remove any invented certification, testimonial, sales result, health benefit, or competitor claim.
5. Add this decision statement at the top: 'Recommended angle: Stop the bag spill with a practical commute-bag hydration routine.' Mark the status REVIEW because the leak-resistant claim still needs the product owner to confirm evidence for the planned demonstration.
6. Create 02-trends/04-weekly-trend-workflow-spec.md. Add the states Collect, Normalize, Enrich, Score, Review, Brief, and Archive with one input and one output for each.
7. Set the schedule to Monday at 08:30 Asia/Singapore. Set lookback to 7 days, maximum signal age to 72 hours for 'active' status, and deduplication key to lowercase(topic + market + source_url).

   ```text
   Schedule: Monday 08:30 Asia/Singapore
Lookback: 7 days
Active signal age: <= 72 hours
Dedup key: lowercase(topic + market + source_url)
   ```

8. Define exception routes: missing URL -> RESEARCH; risk 4-5 -> HOLD; source older than 72 hours -> STALE; duplicate key -> MERGE; fewer than two credible sources -> NEEDS CORROBORATION; workflow error -> create review ticket and retain the last successful brief.
9. Add an output schema with run_id, signal_ids, retrieved_at_sgt, brief_version, reviewer, status, and archive_path. Save both files and link the brief to 03-trend-signal-scorecard.xlsx.

**Test it**

The opportunity brief recommends one angle, cites only T01/T03/T06, separates observation and interpretation, and marks the product demonstration for review. The workflow spec says Monday 08:30 Asia/Singapore, 7-day lookback, 72-hour active limit, a deduplication key, six exception routes, and a versioned output schema.

**Checkpoint for the next lab**

A selected, review-gated trend angle and a reproducible weekly research specification for the content labs.

**Troubleshooting**

- The AI cites a signal not supplied: Delete the unsupported claim, restate the allowed signal IDs in the first and last sentence of the prompt, and regenerate.
- The brief confuses engagement with market demand: Replace the claim with an observation about the supplied index and add the limitation that it is synthetic and cross-platform values are not directly comparable.
- The schedule lacks a failure path: Add a review ticket, last-successful-output retention, and a named marketing owner before considering the spec complete.

**Challenge**

Add a second weekly run for Friday 15:00 SGT that reports only material changes since Monday rather than repeating the full brief.

**Reflection**

Which part of the brief is evidence and which part is a creative hypothesis that still needs a test?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-04-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


## Topic 03 — AI Content Creation and Multimedia Automation

message hierarchy | platform adaptation | brand-voice prompting | image generation | short-form video | scheduling and publish gates

Content automation works when the team creates one approved message system before producing channel variants. The core promise, evidence, offer, and prohibited claims should stay fixed. The agent may adapt structure and tone for a platform, but it should never invent a new product fact to make the copy more persuasive.

Multimedia generation adds visual and rights risks. A strong prompt specifies the product and composition, while a review checklist checks representation, logos, text accuracy, accessibility, and whether the team owns or may use every input. The output remains a draft asset until that review is complete.

**Key concepts**

- A message hierarchy keeps one campaign promise intact while allowing the hook, proof, format, and call to action to change by platform.
- Platform adaptation is not copy-and-paste resizing; audience intent, reading behavior, and native format change the expression of the idea.
- A reusable prompt separates immutable brand facts from variable audience, channel, format, and experiment fields.
- Image prompts need subject, setting, composition, lighting, palette, exclusions, and output format; generated text inside images still needs checking.
- A short-form video pipeline connects hook, scene, on-screen text, voiceover, caption, safe-zone, and rights checks.
- Automation should create and route drafts; publishing stays gated until claims, brand fit, accessibility, and platform readiness are verified.


### One Message, Four Platform Expressions

The campaign promise should remain recognisable across Facebook, Instagram, LinkedIn, and X. What changes is the opening, depth, visual rhythm, and call to action. Instagram may lead with a visual payoff, LinkedIn with a workplace use case, Facebook with context and conversation, and X with one sharp observation.

The agent should output a structured content object rather than an unlabelled paragraph. Fields such as platform, audience, hook, proof, caption, CTA, accessibility note, and claim source make review and scheduling safer.

**Concept visual**

| Element | Meaning |
|---|---|
| Instagram | Visual-first hook, concise caption, save/share value |
| Facebook | Context, practical benefit, and conversation prompt |
| LinkedIn | Professional problem, evidence, and operational takeaway |
| X | One idea, timely framing, and a direct link or reply prompt |


### Brand Prompt Anatomy

A robust content prompt has five layers: verified facts, audience and job-to-be-done, brand voice, output schema, and review constraints. Keeping these layers visible makes the prompt easier to update and audit than a long paragraph of mixed instructions.

Ask the model to flag missing evidence instead of filling gaps. Require a claim ledger that lists each factual statement and its source. This turns hallucination checking into a normal production step rather than an afterthought.

**Concept visual**

| Element | Meaning |
|---|---|
| Facts | Only approved product, offer, and timing details |
| Audience | Segment, situation, tension, and desired action |
| Voice | Tone, sentence style, vocabulary, and exclusions |
| Schema | Named fields for each platform and asset |
| Checks | Claims, accessibility, rights, and approval status |
| Uncertainty | Write NEEDS EVIDENCE instead of inventing support |


### Multimedia Production with Review Gates

An image-generation request should describe the subject, setting, composition, lighting, colour palette, camera view, and exclusions. For product work, use a real approved product reference only when rights and platform terms permit it; otherwise create a clearly labelled concept image.

A short video can be planned as six connected fields per scene: time, visual, action, voiceover, on-screen text, and sound. Before scheduling, check visual continuity, text accuracy, captions, safe zones, rights, and whether any synthetic media disclosure is required by policy or platform.

**Concept visual**

| Element | Meaning |
|---|---|
| Generate | Prompt or storyboard from approved facts |
| Inspect | Product fidelity, people, text, and artefacts |
| Adapt | Aspect ratio, safe zone, caption, and alt text |
| Approve | Rights, claims, brand, accessibility, and disclosure |


### Lab 5 — Create a Governed Four-Platform Content Kit

Learning outcome: LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights.

Goal: You turn one selected, review-gated trend angle into Facebook, Instagram, LinkedIn, and X drafts without changing the core product truth. A claim ledger and per-platform review fields make every variant traceable and ready for human review.

**What you'll build**

03-content/05-four-platform-content-kit.md containing a message hierarchy, four platform drafts, accessibility notes, a claim ledger, and a final review status.   (Tools: Aurora brief, Lab 4 opportunity brief, document editor, classroom-approved AI assistant; duration: 40 minutes.)

**Prerequisites**

- Complete Lab 4 and keep the selected, review-gated 02-trends/04-viral-opportunity-brief.md open.
- Keep labs/resources/aurora-brand-brief.md and the Lab 2 operating specification available.
- Use a document editor and a classroom-approved AI assistant.

**Step-by-step**

1. Create 03-content/05-four-platform-content-kit.md with sections Message Hierarchy, Instagram Draft, Facebook Draft, LinkedIn Draft, X Draft, Claim Ledger, and Review Log.
2. Under Message Hierarchy, write: audience = urban commuters; tension = bottle leaks in a work bag; promise = a practical bottle designed to be leak-resistant; evidence = verified specification plus a proposed demonstration awaiting owner confirmation; offer = 10% off first seven days with LOOP10; CTA = view the HydraLoop product page.
3. Add these required fields under every platform heading: Audience Moment, Hook, Body, CTA, Hashtags or Keywords, Visual Direction, Alt Text, Claim IDs, and Status. Set Status to DRAFT.
4. Send this structured request with the brand brief and Lab 4 opportunity brief. Do not include any real account or audience data.

   ```text
   Create four platform-specific drafts from one verified message hierarchy. Preserve the same product truth and offer. Instagram: visual-first caption under 120 words with 5 relevant hashtags. Facebook: practical context under 150 words plus one conversation question. LinkedIn: workplace commute use case under 180 words with one operational takeaway. X: under 260 characters with no more than 2 hashtags. For every platform return Audience Moment, Hook, Body, CTA, Hashtags or Keywords, Visual Direction, Alt Text, Claim IDs, and Status=DRAFT. Do not invent certifications, medical or environmental benefits, testimonials, popularity, or scarcity. If a claim needs proof, label it NEEDS EVIDENCE.
   ```

5. Paste each variant into its matching section. Confirm the opening and format differ by platform while the audience tension, product truth, offer, and CTA stay aligned.
6. Create Claim Ledger columns Claim ID, Exact Wording, Source, Evidence Owner, Status, and Used In. Add one row each for capacity, cold duration, leak resistance, colours, price, offer, and shipping. Use BRIEF-01 as source and PRODUCT_OWNER as evidence owner.
7. Mark the proposed leak demonstration NEEDS OWNER CONFIRMATION until a real protocol and result exist. Remove or rewrite any statement that implies the demonstration has already happened.
8. Review accessibility: alt text should describe the useful visual information without repeating the entire caption; hashtags should use readable capitalization; emojis must not carry the only meaning. Record fixes in Review Log.
9. After the four drafts, Claim Ledger, evidence review, and accessibility review are complete, save this pre-assistant-review baseline as version v0.1. Add a Review Log row with draft owner, prompt version, source versions, timestamp_sgt, and baseline status.
10. Ask the assistant for a final consistency check. In Review Log add one row per proposed edit with Proposed Edit, Evidence, Accepted or Rejected, Reason, Owner, and Resulting Version. Apply only accepted evidence-supported edits, save version v0.2, and keep every platform Status as DRAFT.

   ```text
   Compare these four drafts against the supplied Message Hierarchy and Claim Ledger. Return only: Contradiction, Unsupported Claim, Missing Accessibility Detail, Platform Mismatch, and Exact Fix. Do not rewrite correct content and do not add new facts.
   ```


**Test it**

The file contains exactly four platform drafts with all nine required fields. Every factual claim maps to the ledger, the unperformed demonstration is not presented as fact, each draft has usable alt text, and all four statuses remain DRAFT. The complete pre-assistant-review baseline is preserved as v0.1, accepted evidence-supported edits form v0.2, and the Review Log records every proposed edit as accepted or rejected with its reason, owner, and resulting version.

**Checkpoint for the next lab**

A four-platform draft kit with evidence-linked claims that feeds campaign planning.

**Troubleshooting**

- All four drafts sound identical: Keep the message hierarchy fixed but restate the channel constraints and request a different opening structure for each platform.
- The assistant invents a certification or health benefit: Delete it, add the phrase 'use only Claim IDs in the ledger,' and rerun the affected platform draft.
- Alt text becomes promotional copy: Rewrite it as a concise description of subject, action, setting, and essential text visible in the image.

**Challenge**

Add two controlled hook variants for Instagram while keeping the body, visual, CTA, and audience fixed for a later experiment.

**Reflection**

Which content fields are allowed to vary by platform, and which must remain invariant to preserve campaign integrity?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-05-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


### Lab 6 — Design a Branded Image Concept and Short-Form Video Storyboard

Learning outcome: LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights.

Goal: You translate the campaign message into a reviewable image concept and a 15-second vertical video storyboard. You practise prompt anatomy, visual continuity, captions, safe zones, and rights review while keeping the product image conceptual and the output unpublished.

**What you'll build**

03-content/06-creative-board.md plus an optional 06-hydraloop-concept.png, containing the image prompt, generation record, review checklist, six-scene storyboard, caption, and alt text.   (Tools: Gemini image generation or Canva, document editor, Lab 5 content kit; duration: 45 minutes.)

**Prerequisites**

- Complete Lab 5 and keep the Instagram draft and Claim Ledger open.
- Use Gemini image generation (Nano Banana family), Canva, or the storyboard-only route if image generation is unavailable.
- Have a document editor and the Aurora visual direction from the brand brief available.

**Step-by-step**

1. Create 03-content/06-creative-board.md with sections Creative Objective, Image Prompt, Generation Record, Image Review, Video Storyboard, Caption and Alt Text, Rights and Disclosure Check, and Status.
2. Under Creative Objective, write the audience moment, single message, platform, aspect ratio 4:5 for the image and 9:16 for video, and CTA. State that the bottle depiction is a concept because no approved product photograph is supplied.
3. Use this image prompt in Gemini image generation or Canva. If the tool is unavailable, paste it into the board and continue with a hand-drawn wireframe.

   ```text
   Create a clearly labelled concept advertising image for a fictional product named HydraLoop: a reusable 750 ml insulated water bottle in ocean blue, upright beside a closed work tote on a clean desk near a bright Singapore office window. Natural morning light, pale-sand background, subtle coral accent, realistic commercial photography, generous copy space in the upper right, 4:5 portrait composition. No people, no logos other than the fictional word HydraLoop, no certifications, no health claims, no competitor branding, no distorted cap, no unreadable label text.
   ```

4. Save one acceptable output as 03-content/06-hydraloop-concept.png. In Generation Record write tool, date, prompt version, output filename, and 'AI-generated concept; product fidelity not approved.' Do not record a credential or private account identifier.
5. Complete Image Review with yes/no rows for concept label, product shape, cap geometry, readable text, palette, copy space, brand fit, prohibited claims, third-party marks, representation, and visible artefacts. If any critical row is no, regenerate or use the storyboard-only route.
6. Create a six-row Video Storyboard table with columns Time, Visual, Action, Voiceover, On-Screen Text, Sound, and Review Note. Use intervals 0-2s, 2-4s, 4-7s, 7-10s, 10-13s, and 13-15s.
7. Build the story: work-bag tension; bottle and tote setup; careful concept leak-test setup; carrying-loop detail; three colours and offer; final CTA. Keep on-screen text inside the centre 80% safe zone and use no more than eight words per scene.
8. Write a 15-second voiceover under 38 words. It must not say the fictional leak test proves performance. Use wording such as 'designed to be leak-resistant' and route the demonstration protocol to the product owner.
9. Add a social caption, descriptive alt text for the image, and a plain-text transcript for the video. Check that essential information is present in captions or voiceover rather than colour alone.
10. Under Rights and Disclosure Check, confirm all inputs are fictional or owned for class, no real person or brand is imitated, generated output is labelled internally, platform disclosure requirements must be checked at publication time, and Status remains REVIEW.

**Test it**

The creative board contains a complete prompt, generation record or wireframe, eleven-row image review, six timed video scenes totalling 15 seconds, voiceover under 38 words, caption, alt text, transcript, rights check, and Status REVIEW. No unverified demonstration result is claimed.

**Checkpoint for the next lab**

A rights-aware image concept and short-video storyboard ready to enter the campaign creative matrix.

**Troubleshooting**

- The generated bottle has distorted parts or text: Remove complex label text, restate one bottle and one cap, regenerate, and keep the output labelled as a concept.
- The tool is unavailable or requires a paid feature: Use the exact prompt to draw a 4:5 wireframe and complete every review and storyboard field without generating an image.
- The storyboard is longer than 15 seconds: Keep the six fixed time ranges, shorten voiceover, and move supporting detail into the caption.

**Challenge**

Create a second image prompt for the office-wellbeing segment while preserving the same product facts, palette, aspect ratio, and review controls.

**Reflection**

Which parts of a generated visual can be checked from the file itself, and which require an external owner or source?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-06-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


## Topic 04 — Creating and Launching AI-Driven Marketing Campaigns

objectives and segments | KPI trees | message and creative matrices | experiment design | content calendars | controlled launch

Campaign orchestration turns disconnected assets into a system with a business outcome, audience logic, measurement plan, owner, and calendar. The agent can accelerate planning by generating alternatives, finding missing fields, and formatting work for different channels, but the campaign team must decide the objective and the evidence that will count as success.

Launch is a state transition, not a button. Draft assets move through review, approval, scheduling, and observation. Each transition requires evidence: final URLs work, events are visible, creative matches the approved version, limits are set, and a rollback owner knows what to do if the launch behaves unexpectedly.

**Key concepts**

- A campaign objective describes the business outcome; a platform objective is a delivery setting chosen to support it.
- A KPI tree connects business outcome, conversion event, leading indicator, and diagnostic metric so optimization has a hierarchy.
- Audience segments should express a need and context, not merely demographic labels or inferred sensitive traits.
- A message matrix links segment, tension, promise, evidence, objection, and call to action before variations are generated.
- A useful experiment changes one main variable, defines a control, and states a decision rule before results arrive.
- A launch workflow validates tracking, creative, links, naming, budgets, approvals, and rollback steps before anything becomes active.


### Build a KPI Tree Before Creating Assets

Start from the business outcome, then work backward. For a product launch, revenue or purchases may be the outcome. Purchase events are the conversion signal. Landing-page conversion rate and cost per purchase are leading decision metrics. CTR, CPC, reach, and engagement help diagnose why the result moved.

This hierarchy prevents the agent from treating every metric as equally important. A high-engagement post may be useful, but it does not automatically prove profitable acquisition. The campaign brief should name the primary decision metric and the guardrails that must not deteriorate.

**Concept visual**

| Element | Meaning |
|---|---|
| Outcome | Purchases, qualified leads, revenue, or retained value |
| Conversion | The verified event tied to the outcome |
| Decision KPI | CPA, ROAS, conversion rate, or qualified-lead rate |
| Diagnostics | Reach, CTR, CPC, frequency, engagement, and sentiment |
| Guardrails | Spend cap, complaint signal, tracking quality, brand safety |


### Campaign Message and Creative Matrix

A matrix makes variation deliberate. Each row represents a segment and situation; columns hold the audience tension, promise, evidence, objection response, format, and call to action. The agent generates inside those cells rather than improvising a new strategy for every post.

The matrix also exposes missing evidence. If a promise has no support, the content should be rewritten as a demonstration, question, or invitation rather than a factual claim. This keeps creativity tied to what the business can honestly show.

**Concept visual**

| Element | Meaning |
|---|---|
| Segment | Who, in which situation, with what need |
| Tension | The friction or unanswered question |
| Promise | What the verified product truth can help with |
| Proof | Demo, specification, source, or customer evidence |
| Format | Post, carousel, short video, search ad, or landing block |
| CTA | One observable next action |


### The Controlled Launch State Machine

A simple state model prevents accidental publication: DRAFT, REVIEW, APPROVED, SCHEDULED, LIVE, PAUSED, and RETIRED. Only named roles may change a state, and the change should capture who, when, why, and which version moved.

Before LIVE, verify links, tracking, creative, copy, targeting boundaries, budget limits, date and timezone, and response ownership. A launch plan also defines the first observation window and the condition that will pause delivery.

**Concept visual**

| Element | Meaning |
|---|---|
| DRAFT | Generated or edited; never public |
| REVIEW | Claims, brand, rights, tracking, and accessibility checked |
| APPROVED | Named owner authorizes this exact version |
| SCHEDULED | Platform, date, timezone, link, and limits confirmed |
| LIVE | Observe against early-warning thresholds |
| PAUSED | Stop condition triggered; preserve evidence and investigate |


### Lab 7 — Build the Campaign Blueprint, KPI Tree, and Experiment Map

Learning outcome: LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs.

Goal: You connect the Aurora business objective to segments, messages, creative formats, KPIs, guardrails, and one controlled experiment. The blueprint prevents the agent from optimizing a convenient platform metric that is disconnected from the launch outcome.

**What you'll build**

04-launch/07-campaign-blueprint.md containing an objective tree, segment-message matrix, channel roles, KPI dictionary, experiment card, and ownership map.   (Tools: Aurora brief, Labs 5-6 artifacts, document editor, classroom-approved AI assistant; duration: 40 minutes.)

**Prerequisites**

- Complete Labs 5-6.
- Keep the Aurora brand brief, content kit, creative board, and claim ledger open.
- Use a document editor and a classroom-approved AI assistant.

**Step-by-step**

1. Create 04-launch/07-campaign-blueprint.md with headings Business Outcome, Campaign Objective, Segments, Message and Creative Matrix, Channel Roles, KPI Dictionary, Experiment Card, Guardrails, and Owners.
2. Under Business Outcome, enter first-week HydraLoop purchases. Under Campaign Objective, enter qualified product-page visits and purchases during the four-week launch. Keep the fictional SGD 300 daily spend cap per platform campaign visible; the cap applies to the combined ad sets in that campaign each day.
3. Create a KPI tree with: outcome = purchases/revenue; conversion = purchase; decision KPIs = CPA, landing conversion rate, and ROAS; diagnostics = impressions, reach, CTR, CPC, engagement, and sentiment; guardrails = tracking quality, complaint signals, claim status, and spend cap.
4. Create a KPI Dictionary table with columns KPI, Formula, Denominator, Source, Window, Target, Limitation, and Owner. Enter the targets from the Aurora brief and write each formula explicitly.

   ```text
   CTR = clicks / impressions
Landing conversion rate = purchases / product-page sessions
CPA = spend / purchases
ROAS = attributed purchase revenue / spend
   ```

5. Create one matrix row for each Aurora segment. Use columns Segment, Situation, Tension, Promise, Evidence, Objection, Format, CTA, and Claim IDs. Reuse only facts from the claim ledger.
6. Assign channel roles: Instagram = visual discovery; Facebook = practical demonstration and discussion; LinkedIn = workplace wellbeing context; X = timely reminder; Google Ads = active-intent capture. These are planning roles, not guaranteed outcomes.
7. Ask the assistant to identify gaps and return exact edits rather than a new strategy. Apply only revisions supported by the supplied artifacts.

   ```text
   Review this campaign blueprint for broken links between business outcome, segment, message, evidence, channel role, KPI, and owner. Return a table with Broken Link, Consequence, Exact Fix, and Evidence Needed. Do not add new facts or channels.
   ```

8. Create Experiment Card EXP-01. Hypothesis: because commuters respond to bag-leak tension, a demonstrated-use hook will improve product-page CTR versus the colour-choice hook. Control = colour-choice hook. Treatment = bag-leak tension hook. Keep audience, placement, offer, image style, and CTA stable.
9. Set primary KPI to link CTR and calculate it as total clicks divided by total impressions for each arm. Require at least 10,000 impressions and 150 clicks per arm across one complete seven-day cycle. Promote the treatment only if relative CTR lift is at least 10%, tracking is ok, and claim-trust comments do not increase; otherwise continue, stop, or redesign. Stop immediately on a tracking, claim, or complaint guardrail breach. Set status to DESIGNED - NOT LAUNCHED and name campaign owner, analyst, brand reviewer, and product-evidence owner.

**Test it**

The blueprint links the business outcome to a conversion, three decision KPIs, diagnostics, and guardrails. All three segments have complete matrix rows. EXP-01 changes one primary hook, names control and treatment, keeps other fields stable, requires 10,000 impressions and 150 clicks per arm, calculates aggregate CTR, defines a 10% lift plus guardrail decision rule, and is marked NOT LAUNCHED.

**Checkpoint for the next lab**

A coherent campaign blueprint and predeclared experiment that the calendar can operationalize.

**Troubleshooting**

- The KPI dictionary lists names but no formulas: Add the exact numerator and denominator and state the platform field or source for each metric.
- The experiment changes copy, image, audience, and offer: Choose one primary hook change and copy every other control field unchanged into both arms.
- A segment depends on inferred sensitive traits: Rewrite it around an observable situation and need, such as commute-bag use or office bundle planning.

**Challenge**

Add a second experiment card for a landing-page message test, but schedule it after EXP-01 so the two effects are not confounded.

**Reflection**

Which metric in your KPI tree should drive the decision, and which metrics only help explain that result?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-07-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


### Lab 8 — Create the Content Calendar and Run a Controlled Launch Dry-Run

Learning outcome: LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs.

Goal: You schedule eight draft content items across one week, attach owners and evidence, and walk each item through a launch-state dry-run. A formula prevents an incomplete row from entering review, while a zero-LIVE check proves nothing was published during class.

**What you'll build**

04-launch/08-content-calendar.xlsx and 04-launch/08-launch-checklist.md with eight versioned draft items, readiness flags, approval ownership, observation windows, and rollback steps.   (Tools: Spreadsheet application, Labs 5-7 artifacts, document editor; duration: 40 minutes.)

**Prerequisites**

- Complete Lab 7 and keep the campaign blueprint open.
- Keep the four-platform content kit and creative board available.
- Use a spreadsheet application and a document editor.

**Step-by-step**

1. Create 04-launch/08-content-calendar.xlsx. In row 1 add columns Item ID, Date, Time SGT, Platform, Segment, Asset Version, Copy Version, CTA URL, Claim IDs, Owner, Status, Readiness, Experiment Arm, First Check, and Rollback Version.
2. Add eight items dated across a Monday-Sunday week: two Instagram, two Facebook, two LinkedIn, and two X. Use item IDs CAL-01 through CAL-08 and times in Asia/Singapore.
3. For each row, reference the exact Lab 5 copy section and Lab 6 asset or storyboard version. Use https://example.com/hydraloop as the classroom-only CTA URL and copy the required Claim IDs from the ledger.
4. Set every Status cell in K2:K9 to DRAFT. In L2 enter the readiness formula below and fill it down. The row may enter REVIEW only when all required fields are present and Status is DRAFT or REVIEW.

   ```text
   =IF(OR(COUNTA(A2:J2)<10,N2="",O2="",AND(OR(A2="CAL-01",A2="CAL-02"),M2="")),"INCOMPLETE",IF(OR(K2="DRAFT",K2="REVIEW"),"READY FOR REVIEW","CHECK STATE"))
   ```

5. Assign CAL-01 and CAL-02 to EXP-01 Control and Treatment. Keep their platform, segment, date window, offer, CTA, and creative style aligned; only the planned hook differs.
6. Set First Check to two hours after the scheduled time for routine delivery checks and next-business-day for the first performance note. Set Rollback Version to the last approved copy and asset version, not a blank value.
7. Create 04-launch/08-launch-checklist.md with sections Tracking, Creative and Copy, Claims and Rights, Audience and Placement, Budget and Pacing, Schedule and Timezone, Response Owner, Approval Record, First Observation, Pause Conditions, and Rollback.
8. Run a tabletop dry-run for CAL-01. Move its spreadsheet Status from DRAFT to REVIEW only. In the checklist record the item ID, versions, reviewer, unresolved leak-demonstration evidence, and decision HOLD IN REVIEW until the product owner confirms the demonstration protocol.
9. Add a control cell labelled LIVE Count with formula =COUNTIF(K2:K9,"LIVE"). Confirm the result is 0. Save the workbook and checklist without opening any social scheduling or advertising account.

   ```text
   =COUNTIF(K2:K9,"LIVE")
   ```


**Test it**

The calendar has eight unique item IDs, complete dates/times/platforms/versions/owners, two aligned experiment arms, and no blank rollback version. CAL-01 is REVIEW with a documented hold reason; all other rows are DRAFT. LIVE Count equals 0 and the checklist covers all eleven sections.

**Checkpoint for the next lab**

A zero-LIVE content calendar and complete controlled-launch checklist ready for synthetic performance monitoring.

**Troubleshooting**

- Readiness says INCOMPLETE: Filter column L, fill the missing field in A:J from the approved artifacts, and do not bypass the formula.
- The experiment rows differ in more than the hook: Copy the control row, create a new item ID, and edit only the hook-specific copy version.
- A platform opens a live composer: Close it without saving, return to the spreadsheet dry-run, and keep the class workflow account-free.

**Challenge**

Add a dependency column that prevents a Treatment item moving to REVIEW until the matching Control item and experiment card share the same experiment version.

**Reflection**

Which launch check is easiest to automate reliably, and which still requires contextual human judgement?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-08-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


## Topic 05 — Agentic AI for Social Media Performance Monitoring

analytics connectors | metric definitions | dashboards | sentiment and themes | pattern detection | evidence-linked feedback

Monitoring begins with a measurement contract: the metric, formula, platform field, level of aggregation, time window, timezone, and decision it supports. Without that contract, two tools can display similarly named numbers that should not be compared. The agent must retain these definitions alongside the values it analyses.

Performance learning combines quantitative and qualitative evidence. Metrics show what happened; comments and support signals help explain why. The output should distinguish observation from interpretation and recommendation, cite the relevant rows or comments, and state what additional evidence would change the recommendation.

**Key concepts**

- A connector should preserve metric name, platform, date window, timezone, object level, and retrieval time so comparisons are interpretable.
- Reach counts unique exposure while impressions count displays; clicks and engagements need a declared denominator before a rate is compared.
- CTR, engagement rate, conversion rate, and cost metrics answer different questions and should not be collapsed into one success score without rationale.
- Sentiment labels are useful only with themes, representative examples, uncertainty, and a human review path for ambiguous or high-risk feedback.
- Pattern detection compares like with like: platform, audience, format, objective, and time window should be controlled before a winner is named.
- The feedback loop should pass evidence and a bounded recommendation to content generation, not merely 'make it better.'


### The Marketing Metric Ladder

Delivery metrics such as reach and impressions show exposure. Attention metrics such as video views and clicks show response. Action metrics such as landing visits and purchases show progression. Efficiency metrics such as CPC, CPA, and ROAS connect those outcomes to cost.

Always write the formula and denominator. CTR is clicks divided by impressions. Conversion rate must state whether it uses clicks, sessions, or another base. ROAS is attributed conversion value divided by ad spend and depends on the chosen attribution rules.

**Concept visual**

| Element | Meaning |
|---|---|
| Delivery | Reach, impressions, frequency |
| Attention | Views, clicks, engaged sessions |
| Action | Key events, leads, purchases |
| Efficiency | CPC, CPA, revenue per cost, ROAS |
| Quality | Tracking status, complaints, brand safety, data gaps |


### Observation, Interpretation, Recommendation

An observation is directly supported by data: Post P10 had the highest clicks in the sample. An interpretation proposes a reason: the launch offer and product image may have increased action. A recommendation proposes a bounded next step: reuse the offer structure in a controlled variation while keeping the audience and placement stable.

Agents often overstate interpretation as fact. Requiring these three labelled fields, an evidence reference, and a confidence note makes the reasoning reviewable and easier to challenge.

**Concept visual**

| Element | Meaning |
|---|---|
| Observe | State the metric or comment pattern and cite the rows |
| Interpret | Offer a plausible explanation and alternatives |
| Recommend | Specify one reversible next action |
| Verify | Name the KPI, window, and result that would support the idea |


### Sentiment with Themes and Escalation

Positive, neutral, and negative labels alone are too shallow for action. Add a theme such as price, leak concern, colour request, claim trust, or cleaning question. Preserve a short comment excerpt or ID so a reviewer can see the evidence.

Route legal, safety, privacy, discrimination, crisis, or unsupported-claim concerns to a human owner. Do not let an automated reply invent policy or product facts. The useful output is a queue with severity, theme, suggested owner, and a draft response clearly marked for review.

**Concept visual**

| Element | Meaning |
|---|---|
| Label | Positive, neutral, negative, or mixed |
| Theme | What the audience is actually discussing |
| Evidence | Comment ID and representative wording |
| Severity | Routine, investigate, or urgent escalation |
| Action | Respond, clarify, update content, or pause a claim |


### Lab 9 — Build a Social Performance Dashboard with Defined Metrics

Learning outcome: LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations.

Goal: You calculate platform-neutral performance rates from ten simulated, unpublished posts, validate the denominators, and build a compact dashboard. You separate descriptive findings from causal claims so the dashboard becomes a decision aid rather than a leaderboard.

**What you'll build**

05-monitor/09-social-performance-dashboard.xlsx containing raw data, calculated metrics, a summary table, two charts, metric definitions, and a three-part insight note.   (Tools: Spreadsheet application, Aurora post performance CSV, Lab 7 KPI Dictionary; duration: 40 minutes.)

**Prerequisites**

- Complete Lab 8.
- Open labs/resources/aurora-post-performance.csv, a synthetic sandbox simulation that uses the Lab 8 plan plus two labelled control or benchmark rows, in a spreadsheet application.
- Keep the KPI Dictionary from Lab 7 available.

**Step-by-step**

1. Save a working copy of aurora-post-performance.csv as 05-monitor/09-social-performance-dashboard.xlsx. Rename the first sheet Raw Posts and freeze row 1.
2. Check that there are ten unique post_id values and no blank platform, reach, impressions, clicks, or simulation_status fields. Confirm impressions are greater than or equal to reach for every row. Check the calendar_item_id, experiment_id, experiment_arm, asset_version, and copy_version lineage fields; P08 is a deliberately failed legacy negative control marked DO NOT REUSE, and P09 is an unpublished benchmark outside the eight-item Lab 8 calendar. Neither is a published Lab 8 item.
3. Insert four blank columns immediately before calendar_item_id so the lineage fields remain intact. Name column O engagements. In O2 sum likes, comments, shares, and saves, then fill down to O11.

   ```text
   =SUM(I2:L2)
   ```

4. Add columns P click_through_rate, Q engagement_rate_by_reach, and R video_view_rate. Enter the formulas below in P2, Q2, and R2 respectively, then fill down through row 11. Format P:R as percentages with two decimals.

   ```text
   =IFERROR(H2/G2,0)
=IFERROR(O2/F2,0)
=IFERROR(M2/G2,0)
   ```

5. Create a Metric Definitions sheet with columns Metric, Formula, Denominator, Source Columns, Interpretation, and Limitation. Document reach, impressions, engagements, CTR, engagement rate by reach, and video view rate.
6. Create a Summary sheet. Build a pivot table with platform in rows and sums of reach, impressions, clicks, and engagements in values. Add calculated overall CTR as total clicks divided by total impressions rather than averaging row percentages.
7. Add a ranked post table showing post_id, platform, theme, clicks, CTR, engagements, engagement rate, and video view rate. Sort once by clicks and once by CTR to see whether the leader changes.
8. Create two charts: a clustered column chart of clicks by post_id and a horizontal bar chart of engagement_rate_by_reach by post_id. Use direct labels and titles that name the denominator.
9. Write an Insight Note with labelled Observation, Interpretation, Recommendation, Evidence IDs, Confidence, and Next Check. Use P10 as the click observation, P08 as the low-CTR observation, and the related content themes. Do not state that theme alone caused the results.

**Test it**

The Raw Posts sheet contains ten unique rows and formulas through row 11. P10 has the most clicks (522). P08 has the lowest CTR at about 0.68%. The summary uses aggregated numerators and denominators, both charts name their metric, and the insight note cites P10 and P08 while separating observation from interpretation. P08 is identified as a simulated negative-control failure marked DO NOT REUSE.

**Checkpoint for the next lab**

A denominator-aware social dashboard that provides quantitative evidence for comment analysis.

**Troubleshooting**

- Percentages show values such as 250%: Confirm clicks are divided by impressions, apply percentage formatting once, and do not multiply the formula by 100.
- The platform CTR is an average of row CTR: Replace it with SUM(clicks)/SUM(impressions) so differently sized posts receive the correct weight.
- A chart implies a causal winner: Retitle it as observed performance, add the date window, and move causal language into a testable hypothesis.

**Challenge**

Add a format-level summary and compare Reels, images, carousels, video, and text while clearly noting the small synthetic sample sizes.

**Reflection**

How did the ranking change when you sorted by clicks versus rate, and what decision risk comes from choosing only one view?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-09-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


### Lab 10 — Analyse Audience Feedback and Produce an Insight-to-Content Memo

Learning outcome: LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations.

Goal: You classify twelve synthetic comments by sentiment, theme, severity, and owner, then review the AI labels against the original text. You combine comment evidence with the dashboard to propose one bounded content revision and one experiment.

**What you'll build**

05-monitor/10-comment-analysis.xlsx and 05-monitor/10-insight-to-content-memo.md with reviewed labels, escalation routes, representative evidence, and a controlled next action.   (Tools: Aurora comments CSV, Lab 9 dashboard, spreadsheet application, classroom-approved AI assistant; duration: 40 minutes.)

**Prerequisites**

- Complete Lab 9 and keep the dashboard open.
- Open labs/resources/aurora-comments.csv.
- Use a spreadsheet application, document editor, and classroom-approved AI assistant.

**Step-by-step**

1. Save aurora-comments.csv as 05-monitor/10-comment-analysis.xlsx. Add columns D Sentiment, E Theme, F Severity, G Evidence Phrase, H Suggested Owner, I Draft Response, J Human Review, and K Reviewer Note.
2. Send all twelve synthetic comments to the AI assistant with the exact schema below. Ask for one row per comment_id and no invented product facts.

   ```text
   Classify each supplied synthetic comment. Return a Markdown table with Comment ID, Sentiment (positive/neutral/negative/mixed), Theme (price/leak concern/hydration routine/colour/cleaning/team bundle/offer/claim trust/other), Severity (routine/investigate/urgent), Evidence Phrase, Suggested Owner (community/product/brand/legal/privacy), Draft Response, and Human Review (yes/no). Preserve the comment ID. For claim-trust, legal, health, safety, privacy, or uncertain product facts, set Human Review=yes and do not invent an answer.
   ```

3. Copy the labels into columns D:J. Compare every row with the original comment. In K record confirmed or the exact manual correction; never accept a label without reading the source row.
4. Verify C06 and C07 are theme claim trust, severity investigate or urgent, Suggested Owner brand or legal, and Human Review yes. Verify C11 also routes to review because it raises health-claim risk.
5. Create a Summary sheet with counts by Sentiment, Theme, Severity, Suggested Owner, and Human Review. Add one representative comment_id for the three most frequent themes.
6. Create 05-monitor/10-insight-to-content-memo.md with headings Quantitative Observation, Qualitative Observation, Interpretation, Alternative Explanation, Recommendation, Evidence, Owner, Guardrail, and Next Check.
7. Under Quantitative Observation cite P08's low CTR and P10's leading click count from Lab 9. Under Qualitative Observation cite C06 and C07 as claim-trust concerns and C01/C04 as leak-proof questions. Do not copy names or infer customer traits.
8. Mark P08 / LEGACY-FAIL-01 DO NOT REUSE and replace that negative-control concept with a product-owner-approved, clearly described leak-resistance demonstration. State that the demonstration result must exist before a performance claim is written.
9. Define the next check as controlled hook experiment EXP-01 with claim-trust comments as a guardrail and link CTR as the primary KPI. Assign product owner and brand reviewer. Save both files.

**Test it**

All twelve comment IDs have reviewed labels and reviewer notes. C06, C07, and C11 require human review. The memo cites P08, P10, C01, C04, C06, and C07; separates observation from interpretation; marks P08 / LEGACY-FAIL-01 DO NOT REUSE; and proposes EXP-01 without asserting an unperformed result.

**Checkpoint for the next lab**

A reviewed audience-feedback table and evidence-linked memo that feeds paid-media diagnosis and optimization design.

**Troubleshooting**

- The assistant returns fewer than twelve rows: List the missing comment IDs explicitly and request only those rows using the same schema.
- A draft response invents a product answer: Replace it with an acknowledgement and route to PRODUCT_OWNER; keep Human Review yes.
- The memo treats sentiment as representative of all customers: State the sample size, synthetic source, and that comments are directional qualitative evidence only.

**Challenge**

Add a confidence column and require low-confidence or mixed labels to be reviewed by a second learner before they enter the summary.

**Reflection**

What useful context did the comments add that the dashboard metrics alone could not provide?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-10-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


## Topic 06 — Agentic AI for Advertising Optimization and Scaling

paid-media metrics | anomaly detection | diagnosis trees | A/B experiments | budget and targeting controls | autonomous-loop design

Optimization is decision-making under uncertainty. A falling ROAS may reflect weaker creative, higher auction cost, a landing-page problem, conversion delay, or broken tracking. An agent should diagnose across these branches and present evidence before proposing an action. Direct budget changes from a single noisy metric create a fast path to expensive mistakes.

The safest autonomous loop is layered. Collection and calculations may run automatically. Diagnosis and experiment drafting may be agent-assisted. Budget, targeting, bid, and live creative changes are bounded by approval gates, caps, cooldowns, and rollback rules. Scaling means repeating a validated pattern within those controls, not removing them.

**Key concepts**

- An anomaly is a meaningful deviation from an expected range; it is a signal to diagnose, not permission to change a budget.
- Paid-media diagnosis should check tracking, delivery, audience, creative, landing experience, and conversion lag before choosing a remedy.
- CPA equals spend divided by conversions; ROAS equals attributed conversion value divided by spend, and both inherit attribution limitations.
- A/B testing requires a control, one main change, comparable traffic, a predeclared KPI, an observation window, and a decision rule.
- Scaling should be bounded by spend caps, pacing rules, minimum evidence, reversibility, cooldown periods, and human approval thresholds.
- A mature optimization loop logs the data snapshot, hypothesis, proposed action, approver, execution result, and rollback state.


### Diagnose Before You Optimize

Start with tracking quality because every downstream metric depends on it. Then inspect delivery and auction signals, audience saturation, creative response, landing conversion, and conversion lag. Compare the changed segment with a stable reference instead of reacting to the total account number.

A good diagnosis memo names the symptom, evidence, competing explanations, missing data, and safest next test. If tracking is partial, the correct recommendation is usually to hold major changes and repair measurement first.

**Concept visual**

| Element | Meaning |
|---|---|
| Tracking | Event loss, tag changes, delayed imports, partial status |
| Delivery | Spend, impressions, CPM, pacing, approval status |
| Audience | Frequency, overlap, saturation, exclusions |
| Creative | CTR, view rate, comments, fatigue, message mismatch |
| Landing | Speed, message match, conversion rate, checkout errors |
| Lag | Attribution window and delayed conversions |


### Design a Decision-Ready Experiment

An experiment starts with a causal question, not two random variations. Keep the audience, placement, timing, and offer stable while changing one primary creative or bidding variable. Define the control, treatment, primary KPI, guardrails, minimum runtime, and decision rule before launch.

Early differences can be noise. Use the platform's experiment workflow when available, keep control and treatment metrics separate, and avoid declaring a winner from a few conversions. The action after the test may be promote, continue, stop, or redesign.

**Concept visual**

| Element | Meaning |
|---|---|
| Hypothesis | Because insight X, changing Y should improve KPI Z |
| Control | Current approved version |
| Treatment | One primary change |
| Guardrails | Spend, complaints, tracking, and secondary KPI limits |
| Window | Predeclared runtime and conversion-lag allowance |
| Decision | Promote, continue, stop, or redesign |


### Bounded Optimization Loop

The loop collects a versioned snapshot, validates data quality, detects a threshold breach, drafts a diagnosis, proposes one reversible action, and waits for approval when the action affects spend, targeting, or public creative. After execution it observes a cooldown window and compares the result with the rollback condition.

Every cycle should be idempotent: rerunning the same input should not apply the same change twice. Store an action ID and current state, enforce daily and weekly caps, and route repeated failures or conflicting evidence to a human owner.

**Concept visual**

| Element | Meaning |
|---|---|
| Observe | Versioned metrics plus quality status |
| Validate | Freshness, completeness, and denominator checks |
| Diagnose | Evidence tree and competing explanations |
| Propose | One bounded, reversible change |
| Approve | Required for spend, targeting, bid, or public creative |
| Learn | Cooldown, result, rollback, and audit record |


### Lab 11 — Diagnose Paid-Media Anomalies Before Recommending a Change

Learning outcome: LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence.

Goal: You calculate CTR, click conversion rate, CPA, and ROAS for eighteen synthetic, unpublished paid-media rows, flag target or tracking breaches, and diagnose the deteriorating commuter ad set. The workflow checks data quality before creative or budget action.

**What you'll build**

06-optimize/11-paid-media-diagnostics.xlsx and 06-optimize/11-diagnosis-memo.md with calculated metrics, anomaly flags, a diagnosis tree, evidence, and a safest-next-test recommendation.   (Tools: Spreadsheet application, Aurora ad performance CSV, Aurora targets, Lab 10 memo; duration: 45 minutes.)

**Prerequisites**

- Complete Lab 10.
- Open labs/resources/aurora-ad-performance.csv in a spreadsheet application.
- Keep the Aurora targets and Lab 10 insight memo available.

**Step-by-step**

1. Save aurora-ad-performance.csv as 06-optimize/11-paid-media-diagnostics.xlsx. Rename the first sheet Raw Ads, freeze row 1, and confirm there are eighteen sandbox-simulation rows from 20-25 July 2026. Check experiment, creative-version, and simulation-status fields before analysis; none of the rows represents a live launch.
2. Insert six blank columns immediately before experiment_id so the lineage fields remain intact. Name columns L CTR, M Click Conversion Rate, N CPA SGD, O ROAS, P Daily Campaign Spend, and Q Review Flag. Enter the formulas below in L2 through Q2 respectively, then fill down through row 19. Format L:M as percentages and N:P as two-decimal numbers.

   ```text
   =IFERROR(G2/F2,0)
=IFERROR(I2/G2,0)
=IF(I2=0,"",H2/I2)
=IFERROR(J2/H2,0)
=SUMIFS($H$2:$H$19,$A$2:$A$19,A2,$B$2:$B$19,B2,$C$2:$C$19,C2)
=IF(OR(K2<>"ok",P2>300,I2=0,N2>24,O2<2.5),"REVIEW","OK")
   ```

3. Create a Metric Definitions sheet. Record formulas, denominators, currency, date window, fictional attribution assumption, and the fact that partial tracking invalidates strong conversion conclusions.
4. Filter campaign HydraLoop Launch, ad_set Commuters. Create a line chart by date for CPA and a second line chart for ROAS. Add a vertical note at 24 July when tracking_status changes to partial.
5. Compare 20 July with 24-25 July for the commuter ad set. Record the exact spend, purchases, CPA, ROAS, CTR, and tracking_status values in an Evidence table.
6. Create 06-optimize/11-diagnosis-memo.md with headings Symptom, Evidence, Data Quality, Competing Explanations, Missing Checks, Safest Next Action, Do Not Do, Owner, and Next Observation.
7. Walk the diagnosis tree in this order: tracking; delivery and auction; audience and frequency; creative and comments; landing page; conversion lag. For every branch write observed, not available, or needs owner check.
8. Use C01/C04 from Lab 10 as contextual evidence that the leak angle raises product-proof questions, but do not claim those comments caused paid results. Note that frequency and landing-page data are not supplied.
9. Set Safest Next Action to hold automated budget or targeting changes, route tracking_status=partial to the analytics owner, and prepare a claim-safe creative experiment only after data quality returns to ok. Under Do Not Do write 'Do not double spend, broaden targeting, or declare creative failure from partial tracking.'

**Test it**

All eighteen rows have formulas and review flags. The commuter rows on 24 and 25 July show partial tracking, CPA of SGD 21.25 and SGD 29.17, and ROAS of 2.26 and 1.65. Every simulated campaign-day total is at or below the SGD 300 cap, while partial tracking and the 25 July target breach still route to REVIEW. The memo checks tracking first, states missing frequency/landing data, cites comments only as context, and recommends no budget or targeting change until tracking is repaired.

**Checkpoint for the next lab**

A data-quality-first diagnosis and safest-next-test recommendation for the final control-loop design.

**Troubleshooting**

- CPA shows an error for zero purchases: Return a blank CPA with IF(I2=0,"",H2/I2) and make the review flag test I2=0; do not replace the business meaning with a false zero CPA.
- The chart mixes campaigns: Filter campaign and ad_set before charting, then verify all plotted rows are the commuter segment.
- The diagnosis jumps straight to creative fatigue: Move tracking quality to the first branch and list creative as one competing explanation rather than a conclusion.

**Challenge**

Add a three-day rolling CPA and show how smoothing changes the apparent timing of the anomaly, with a note about delayed detection.

**Reflection**

Why is 'hold and repair measurement' sometimes a better optimization decision than changing the campaign immediately?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-11-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


### Lab 12 — Design and Simulate a Human-Governed Optimization Loop

Learning outcome: LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence.

Goal: You assemble the course artifacts into a complete observe-validate-diagnose-propose-approve-learn loop. Three tabletop cases test data-quality stops, bounded experiments, approval gates, spend caps, cooldowns, idempotency, audit evidence, and rollback.

**What you'll build**

06-optimize/12-optimization-runbook.md containing the loop, rule table, action schema, three simulation logs, approval matrix, stop conditions, cooldown, and rollback procedure.   (Tools: All Aurora campaign checkpoints, document editor, classroom-approved AI assistant; duration: 45 minutes.)

**Prerequisites**

- Complete Lab 11 and keep the diagnostics workbook and memo open.
- Keep the Lab 1 agent canvas, Lab 2 operating specification, Lab 7 experiment card, and Lab 8 launch checklist available.
- Use a document editor and a classroom-approved AI assistant.

**Step-by-step**

1. Create 06-optimize/12-optimization-runbook.md with headings Purpose, Loop States, Input Contract, Rule Table, Action Schema, Approval Matrix, Stop Conditions, Cooldown and Rollback, Simulation Log, and Operating Review.
2. Under Loop States, define Observe -> Validate -> Diagnose -> Propose -> Approve -> Execute or Hold -> Learn. State that Execute is a future production state and remains simulated in class.
3. Under Input Contract, require snapshot_id, retrieved_at_sgt, platform, campaign, object level, date window, metric definitions version, tracking_status, data completeness, and source owner. Missing fields route to HOLD.
4. Create a Rule Table with columns Rule ID, Condition, Proposed Action, Max Change, Approval, Cooldown, Rollback Trigger, and Evidence Logged. Add RULE-DQ for non-ok tracking, RULE-CPA for CPA above SGD 24 with ok tracking, RULE-ROAS for ROAS below 2.5, and RULE-SCALE only when ROAS is at least 2.5 in each of two complete seven-day cycles, each cycle has at least 30 purchases, tracking is ok, data completeness is 100%, and there is no claim, complaint, or spend-cap guardrail breach.
5. Set RULE-DQ action to HOLD AND INVESTIGATE with no campaign change. Set RULE-CPA and RULE-ROAS to propose one experiment, not an immediate budget move. Set RULE-SCALE to propose at most a 10% budget increase, still requiring campaign-owner approval and keeping the combined ad sets inside the SGD 300 daily cap for that platform campaign.
6. Define Action Schema fields action_id, run_id, snapshot_id, rule_id, hypothesis, evidence_ids, proposed_change, expected_effect, max_change, approver, status, created_at_sgt, cooldown_until_sgt, rollback_version, result, and next_state. Make action_id unique and state that a repeated action_id cannot execute twice.
7. Simulate Case A from the 24 July commuter row: tracking_status=partial. Expected result is HOLD, analytics-owner ticket, zero budget change, and last safe version retained. Record the complete action schema under Simulation Log.
8. Simulate Case B: tracking is ok, CPA is SGD 31 for three full days, volume is adequate, and claim-trust comments increased. Expected result is a draft creative experiment with control/treatment, brand and campaign-owner approval, and no automatic spend increase.
9. Simulate Case C: tracking is ok, ROAS is 3.1 in each of two complete seven-day cycles, each cycle has 35 purchases, CPA is SGD 20, data completeness is 100%, claim, complaint, and spend-cap guardrails are stable, and current daily spend is SGD 270. Expected result is a proposed 10% increase to SGD 297, human approval required, 72-hour cooldown, and rollback if ROAS falls below 2.5 or tracking degrades.
10. Send the three logs to the assistant for a control audit. Apply only corrections that strengthen traceability or limits. Then duplicate Case C with the same action_id and confirm the runbook outcome is SKIP DUPLICATE rather than a second increase.

   ```text
   Audit these three simulated optimization actions. Check input completeness, rule match, permission, cap arithmetic, approval, cooldown, idempotency, rollback trigger, and evidence log. Return Fail/Pass for each control and an exact correction for every Fail. Do not recommend a larger change.
   ```

11. Under Operating Review, set a weekly review of false alarms, missed anomalies, approval latency, repeated failures, cap breaches, and rollback outcomes. Save the final runbook as version v1.0 and link every earlier artifact by filename.

**Test it**

Case A holds with zero change; Case B proposes one controlled creative experiment; Case C calculates SGD 297, stays under the cap, requires approval, and sets a 72-hour cooldown and rollback. Reusing Case C's action_id returns SKIP DUPLICATE. Every log contains all action schema fields and links to a prior campaign artifact. RULE-SCALE explicitly requires two complete seven-day cycles, ROAS at least 2.5 in each, at least 30 purchases per cycle, ok tracking, 100% data completeness, and no claim, complaint, or spend-cap breach.

**Checkpoint for the next lab**

A complete, simulated, human-governed optimization runbook that connects all twelve course labs.

**Troubleshooting**

- The loop proposes a spend change when tracking is partial: Move RULE-DQ to the highest priority and state that it short-circuits every performance rule.
- The 10% increase exceeds the cap: Calculate MIN(current spend x 1.10, daily cap) and route any cap conflict to the campaign owner.
- A retry repeats the same action: Persist action_id with status and reject any Execute request whose ID already exists, regardless of prompt wording.

**Challenge**

Add a portfolio rule that limits the combined daily change across three fictional products while preserving a separate rollback version for each.

**Reflection**

Which parts of your final loop can be safely automated now, and what evidence would you need before granting any additional permission?

> **Note:** Full step-by-step instructions, prompts, and verification checks are in labs/lab-12-*.md. Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

---


## Wrap-Up - From Fast Drafts to a Controlled Learning System

You have built the complete control path for an agentic marketing campaign: purpose and permissions, trend evidence, content variants, launch states, monitoring, diagnosis, and bounded optimization. The durable skill is not a particular tool interface. It is the ability to define what the system may observe, decide, produce, and escalate.

**What You Can Now Do**

- Choose between a fixed workflow, router, evaluator loop, and agent based on uncertainty and risk.
- Rank trend signals with provenance, freshness, evidence, brand fit, and a separate risk veto.
- Generate channel variants and multimedia concepts from one verified message system.
- Connect campaign objectives to KPIs, experiments, calendars, approval states, and rollback steps.
- Calculate performance metrics and separate observation, interpretation, and recommendation.
- Design an optimization loop that validates data, proposes one reversible action, and logs the result.

**Operating Habits Worth Keeping**

- Version the brief, prompt, data snapshot, and output that produced each decision.
- Treat missing evidence as a routing condition, not an invitation to invent a fact.
- Keep metric definitions and denominators beside the values.
- Use approval gates for public claims, customer data, targeting, spend, and live creative.
- Prefer small reversible experiments over broad simultaneous changes.

**When the System Should Stop**

- A required source is missing, stale, or contradictory.
- Tracking is partial or a metric definition changed.
- A proposed claim lacks evidence or creates legal, safety, or reputation risk.
- An action would exceed a spend cap, permission boundary, or approved audience scope.
- Repeated retries produce the same failure or an owner cannot be reached.

---


## Next Steps

- Replace the fictional brief with an approved low-risk campaign brief from your organisation, keeping the same data fields and gates.
- Pilot only the read, calculate, and draft stages before connecting any publishing or advertising tool.
- Create a metric dictionary with owners, formulas, platform fields, windows, and known limitations.
- Run one controlled content experiment and document the predeclared decision rule before reviewing results.
- Review permissions, prompts, connectors, logs, and stop conditions at a regular operating cadence.


## Glossary

- **Agent** — A goal-directed system that can select among permitted actions or tools using current state and feedback.
- **Workflow** — A predefined sequence of steps that reliably transforms an input into an output.
- **State** — The versioned information carried between steps, including campaign facts, decisions, and results.
- **Tool** — A bounded capability an agent can call, such as read data, calculate a metric, draft copy, or schedule a task.
- **Guardrail** — A testable condition that blocks, limits, routes, or records an action.
- **Approval gate** — A required human authorization before a high-impact state change.
- **Least privilege** — Granting only the minimum data and action permissions needed for the task.
- **Provenance** — Where a data point or claim came from, including source, time, and transformation history.
- **Idempotency** — A property that prevents the same action being applied twice when a step is retried.
- **CTR** — Click-through rate: clicks divided by impressions, multiplied by 100 for a percentage.
- **Conversion rate** — Conversions divided by a declared base such as clicks or sessions; the denominator must always be stated.
- **CPC** — Cost per click: spend divided by clicks.
- **CPA** — Cost per acquisition or purchase: spend divided by the named conversion count.
- **ROAS** — Return on ad spend: attributed conversion value divided by advertising spend.
- **Attribution** — The rules used to assign conversion credit to marketing touchpoints.
- **Control** — The current approved version used as the comparison arm in an experiment.
- **Treatment** — The experiment arm containing the single planned change.
- **Cooldown** — A defined observation period after a change during which further action is limited.
- **Rollback** — The versioned step that returns a system or campaign to the last known safe state.
- **Synthetic data** — Invented records designed for practice that do not represent real customers or accounts.
