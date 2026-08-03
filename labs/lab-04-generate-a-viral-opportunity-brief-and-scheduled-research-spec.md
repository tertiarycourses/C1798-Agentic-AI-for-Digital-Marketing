# Lab 4 — Generate a Viral Opportunity Brief and Scheduled Research Spec

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 2:** Automated Trend Discovery and Viral Content Research  
**Maps to:** LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity  
**Tools:** Ranked trend CSV, Aurora brief, Lab 2 operating specification, classroom-approved AI assistant  
**Duration:** 40 minutes

---

## Goal

LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity.

## What You Will Do

You use only the ranked records to create an evidence-linked trend opportunity brief. You then specify a weekly research workflow with a fixed schedule, required fields, deduplication, expiry, and exception route so the process can be automated safely later.

## What You Will Build

02-trends/04-viral-opportunity-brief.md and 02-trends/04-weekly-trend-workflow-spec.md, both linked to the Lab 3 signal IDs and review rules.

## Prerequisites

- Complete Lab 3 and keep 02-trends/03-ranked-trend-signals.csv available.
- Keep the Lab 2 operating specification and the Aurora brand brief open.
- Use a document editor and a classroom-approved AI assistant.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Filter the ranked CSV to PROCEED and RESEARCH rows. Select T01, T03, and T06 as the candidate set because they address routine, leakage, and cleaning needs without relying on the held rumour.**

**2. Create 02-trends/04-viral-opportunity-brief.md with headings Recommendation, Why Now, Audience Tension, Hook, Evidence, Product Truth, Channel Ideas, Risks, Needs Confirmation, and Next Check.**

**3. Send the following prompt with only the three selected rows and the fictional brand brief. Ask for one recommended angle, not three disconnected posts.**

```text
You are the Aurora trend-research agent operating under the supplied specification. Use only signal IDs T01, T03, and T06 plus the verified brand brief. Recommend one content opportunity. Separate Observation from Interpretation. Cite every supporting signal ID. Extract one hook, three supporting angles, five relevant hashtags or search phrases, and two emotional triggers. Do not infer absolute demand from relative or synthetic signals. Flag every missing fact as NEEDS CONFIRMATION. Return the exact headings: Recommendation, Why Now, Audience Tension, Hook, Evidence, Product Truth, Channel Ideas, Risks, Needs Confirmation, Next Check.
```

**4. Paste the response into the brief. Check each factual statement against the candidate rows and brand brief. Remove any invented certification, testimonial, sales result, health benefit, or competitor claim.**

**5. Add this decision statement at the top: 'Recommended angle: Stop the bag spill with a practical commute-bag hydration routine.' Mark the status REVIEW because the leak-resistant claim still needs the product owner to confirm evidence for the planned demonstration.**

**6. Create 02-trends/04-weekly-trend-workflow-spec.md. Add the states Collect, Normalize, Enrich, Score, Review, Brief, and Archive with one input and one output for each.**

**7. Set the schedule to Monday at 08:30 Asia/Singapore. Set lookback to 7 days, maximum signal age to 72 hours for 'active' status, and deduplication key to lowercase(topic + market + source_url).**

```text
Schedule: Monday 08:30 Asia/Singapore
Lookback: 7 days
Active signal age: <= 72 hours
Dedup key: lowercase(topic + market + source_url)
```

**8. Define exception routes: missing URL -> RESEARCH; risk 4-5 -> HOLD; source older than 72 hours -> STALE; duplicate key -> MERGE; fewer than two credible sources -> NEEDS CORROBORATION; workflow error -> create review ticket and retain the last successful brief.**

**9. Add an output schema with run_id, signal_ids, retrieved_at_sgt, brief_version, reviewer, status, and archive_path. Save both files and link the brief to 03-trend-signal-scorecard.xlsx.**

## Test It

The opportunity brief recommends one angle, cites only T01/T03/T06, separates observation and interpretation, and marks the product demonstration for review. The workflow spec says Monday 08:30 Asia/Singapore, 7-day lookback, 72-hour active limit, a deduplication key, six exception routes, and a versioned output schema.

## Checkpoint for the Next Lab

A selected, review-gated trend angle and a reproducible weekly research specification for the content labs.

## Troubleshooting

- **The AI cites a signal not supplied:** Delete the unsupported claim, restate the allowed signal IDs in the first and last sentence of the prompt, and regenerate.
- **The brief confuses engagement with market demand:** Replace the claim with an observation about the supplied index and add the limitation that it is synthetic and cross-platform values are not directly comparable.
- **The schedule lacks a failure path:** Add a review ticket, last-successful-output retention, and a named marketing owner before considering the spec complete.

## Challenge

Add a second weekly run for Friday 15:00 SGT that reports only material changes since Monday rather than repeating the full brief.

## Reflection

Which part of the brief is evidence and which part is a creative hypothesis that still needs a test?

---

[← Lab 3](lab-03-build-and-score-a-source-linked-trend-signal-table.md) · [Lab 5 →](lab-05-create-a-governed-four-platform-content-kit.md)
