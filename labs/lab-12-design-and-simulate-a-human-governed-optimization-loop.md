# Lab 12 — Design and Simulate a Human-Governed Optimization Loop

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 6:** Agentic AI for Advertising Optimization and Scaling  
**Maps to:** LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence  
**Tools:** All Aurora campaign checkpoints, document editor, classroom-approved AI assistant  
**Duration:** 45 minutes

---

## Goal

LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence.

## What You Will Do

You assemble the course artifacts into a complete observe-validate-diagnose-propose-approve-learn loop. Three tabletop cases test data-quality stops, bounded experiments, approval gates, spend caps, cooldowns, idempotency, audit evidence, and rollback.

## What You Will Build

06-optimize/12-optimization-runbook.md containing the loop, rule table, action schema, three simulation logs, approval matrix, stop conditions, cooldown, and rollback procedure.

## Prerequisites

- Complete Lab 11 and keep the diagnostics workbook and memo open.
- Keep the Lab 1 agent canvas, Lab 2 operating specification, Lab 7 experiment card, and Lab 8 launch checklist available.
- Use a document editor and a classroom-approved AI assistant.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Create 06-optimize/12-optimization-runbook.md with headings Purpose, Loop States, Input Contract, Rule Table, Action Schema, Approval Matrix, Stop Conditions, Cooldown and Rollback, Simulation Log, and Operating Review.**

**2. Under Loop States, define Observe -> Validate -> Diagnose -> Propose -> Approve -> Execute or Hold -> Learn. State that Execute is a future production state and remains simulated in class.**

**3. Under Input Contract, require snapshot_id, retrieved_at_sgt, platform, campaign, object level, date window, metric definitions version, tracking_status, data completeness, and source owner. Missing fields route to HOLD.**

**4. Create a Rule Table with columns Rule ID, Condition, Proposed Action, Max Change, Approval, Cooldown, Rollback Trigger, and Evidence Logged. Add RULE-DQ for non-ok tracking, RULE-CPA for CPA above SGD 24 with ok tracking, RULE-ROAS for ROAS below 2.5, and RULE-SCALE only when ROAS is at least 2.5 in each of two complete seven-day cycles, each cycle has at least 30 purchases, tracking is ok, data completeness is 100%, and there is no claim, complaint, or spend-cap guardrail breach.**

**5. Set RULE-DQ action to HOLD AND INVESTIGATE with no campaign change. Set RULE-CPA and RULE-ROAS to propose one experiment, not an immediate budget move. Set RULE-SCALE to propose at most a 10% budget increase, still requiring campaign-owner approval and keeping the combined ad sets inside the SGD 300 daily cap for that platform campaign.**

**6. Define Action Schema fields action_id, run_id, snapshot_id, rule_id, hypothesis, evidence_ids, proposed_change, expected_effect, max_change, approver, status, created_at_sgt, cooldown_until_sgt, rollback_version, result, and next_state. Make action_id unique and state that a repeated action_id cannot execute twice.**

**7. Simulate Case A from the 24 July commuter row: tracking_status=partial. Expected result is HOLD, analytics-owner ticket, zero budget change, and last safe version retained. Record the complete action schema under Simulation Log.**

**8. Simulate Case B: tracking is ok, CPA is SGD 31 for three full days, volume is adequate, and claim-trust comments increased. Expected result is a draft creative experiment with control/treatment, brand and campaign-owner approval, and no automatic spend increase.**

**9. Simulate Case C: tracking is ok, ROAS is 3.1 in each of two complete seven-day cycles, each cycle has 35 purchases, CPA is SGD 20, data completeness is 100%, claim, complaint, and spend-cap guardrails are stable, and current daily spend is SGD 270. Expected result is a proposed 10% increase to SGD 297, human approval required, 72-hour cooldown, and rollback if ROAS falls below 2.5 or tracking degrades.**

**10. Send the three logs to the assistant for a control audit. Apply only corrections that strengthen traceability or limits. Then duplicate Case C with the same action_id and confirm the runbook outcome is SKIP DUPLICATE rather than a second increase.**

```text
Audit these three simulated optimization actions. Check input completeness, rule match, permission, cap arithmetic, approval, cooldown, idempotency, rollback trigger, and evidence log. Return Fail/Pass for each control and an exact correction for every Fail. Do not recommend a larger change.
```

**11. Under Operating Review, set a weekly review of false alarms, missed anomalies, approval latency, repeated failures, cap breaches, and rollback outcomes. Save the final runbook as version v1.0 and link every earlier artifact by filename.**

## Test It

Case A holds with zero change; Case B proposes one controlled creative experiment; Case C calculates SGD 297, stays under the cap, requires approval, and sets a 72-hour cooldown and rollback. Reusing Case C's action_id returns SKIP DUPLICATE. Every log contains all action schema fields and links to a prior campaign artifact. RULE-SCALE explicitly requires two complete seven-day cycles, ROAS at least 2.5 in each, at least 30 purchases per cycle, ok tracking, 100% data completeness, and no claim, complaint, or spend-cap breach.

## Checkpoint for the Next Lab

A complete, simulated, human-governed optimization runbook that connects all twelve course labs.

## Troubleshooting

- **The loop proposes a spend change when tracking is partial:** Move RULE-DQ to the highest priority and state that it short-circuits every performance rule.
- **The 10% increase exceeds the cap:** Calculate MIN(current spend x 1.10, daily cap) and route any cap conflict to the campaign owner.
- **A retry repeats the same action:** Persist action_id with status and reject any Execute request whose ID already exists, regardless of prompt wording.

## Challenge

Add a portfolio rule that limits the combined daily change across three fictional products while preserving a separate rollback version for each.

## Reflection

Which parts of your final loop can be safely automated now, and what evidence would you need before granting any additional permission?

---

[← Lab 11](lab-11-diagnose-paid-media-anomalies-before-recommending-a-change.md) · [Labs index →](README.md)
