# Lab 7 — Build the Campaign Blueprint, KPI Tree, and Experiment Map

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 4:** Creating and Launching AI-Driven Marketing Campaigns  
**Maps to:** LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs  
**Tools:** Aurora brief, Labs 5-6 artifacts, document editor, classroom-approved AI assistant  
**Duration:** 40 minutes

---

## Goal

LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs.

## What You Will Do

You connect the Aurora business objective to segments, messages, creative formats, KPIs, guardrails, and one controlled experiment. The blueprint prevents the agent from optimizing a convenient platform metric that is disconnected from the launch outcome.

## What You Will Build

04-launch/07-campaign-blueprint.md containing an objective tree, segment-message matrix, channel roles, KPI dictionary, experiment card, and ownership map.

## Prerequisites

- Complete Labs 5-6.
- Keep the Aurora brand brief, content kit, creative board, and claim ledger open.
- Use a document editor and a classroom-approved AI assistant.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Create 04-launch/07-campaign-blueprint.md with headings Business Outcome, Campaign Objective, Segments, Message and Creative Matrix, Channel Roles, KPI Dictionary, Experiment Card, Guardrails, and Owners.**

**2. Under Business Outcome, enter first-week HydraLoop purchases. Under Campaign Objective, enter qualified product-page visits and purchases during the four-week launch. Keep the fictional SGD 300 daily spend cap per platform campaign visible; the cap applies to the combined ad sets in that campaign each day.**

**3. Create a KPI tree with: outcome = purchases/revenue; conversion = purchase; decision KPIs = CPA, landing conversion rate, and ROAS; diagnostics = impressions, reach, CTR, CPC, engagement, and sentiment; guardrails = tracking quality, complaint signals, claim status, and spend cap.**

**4. Create a KPI Dictionary table with columns KPI, Formula, Denominator, Source, Window, Target, Limitation, and Owner. Enter the targets from the Aurora brief and write each formula explicitly.**

```text
CTR = clicks / impressions
Landing conversion rate = purchases / product-page sessions
CPA = spend / purchases
ROAS = attributed purchase revenue / spend
```

**5. Create one matrix row for each Aurora segment. Use columns Segment, Situation, Tension, Promise, Evidence, Objection, Format, CTA, and Claim IDs. Reuse only facts from the claim ledger.**

**6. Assign channel roles: Instagram = visual discovery; Facebook = practical demonstration and discussion; LinkedIn = workplace wellbeing context; X = timely reminder; Google Ads = active-intent capture. These are planning roles, not guaranteed outcomes.**

**7. Ask the assistant to identify gaps and return exact edits rather than a new strategy. Apply only revisions supported by the supplied artifacts.**

```text
Review this campaign blueprint for broken links between business outcome, segment, message, evidence, channel role, KPI, and owner. Return a table with Broken Link, Consequence, Exact Fix, and Evidence Needed. Do not add new facts or channels.
```

**8. Create Experiment Card EXP-01. Hypothesis: because commuters respond to bag-leak tension, a demonstrated-use hook will improve product-page CTR versus the colour-choice hook. Control = colour-choice hook. Treatment = bag-leak tension hook. Keep audience, placement, offer, image style, and CTA stable.**

**9. Set primary KPI to link CTR and calculate it as total clicks divided by total impressions for each arm. Require at least 10,000 impressions and 150 clicks per arm across one complete seven-day cycle. Promote the treatment only if relative CTR lift is at least 10%, tracking is ok, and claim-trust comments do not increase; otherwise continue, stop, or redesign. Stop immediately on a tracking, claim, or complaint guardrail breach. Set status to DESIGNED - NOT LAUNCHED and name campaign owner, analyst, brand reviewer, and product-evidence owner.**

## Test It

The blueprint links the business outcome to a conversion, three decision KPIs, diagnostics, and guardrails. All three segments have complete matrix rows. EXP-01 changes one primary hook, names control and treatment, keeps other fields stable, requires 10,000 impressions and 150 clicks per arm, calculates aggregate CTR, defines a 10% lift plus guardrail decision rule, and is marked NOT LAUNCHED.

## Checkpoint for the Next Lab

A coherent campaign blueprint and predeclared experiment that the calendar can operationalize.

## Troubleshooting

- **The KPI dictionary lists names but no formulas:** Add the exact numerator and denominator and state the platform field or source for each metric.
- **The experiment changes copy, image, audience, and offer:** Choose one primary hook change and copy every other control field unchanged into both arms.
- **A segment depends on inferred sensitive traits:** Rewrite it around an observable situation and need, such as commute-bag use or office bundle planning.

## Challenge

Add a second experiment card for a landing-page message test, but schedule it after EXP-01 so the two effects are not confounded.

## Reflection

Which metric in your KPI tree should drive the decision, and which metrics only help explain that result?

---

[← Lab 6](lab-06-design-a-branded-image-concept-and-short-form-video-storyboard.md) · [Lab 8 →](lab-08-create-the-content-calendar-and-run-a-controlled-launch-dry-run.md)
