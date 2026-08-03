"""Topic 6 - Agentic AI for Advertising Optimization and Scaling. Labs 11-12."""

DOMAIN6 = [
    dict(
        num=11,
        topic=6,
        title="Diagnose Paid-Media Anomalies Before Recommending a Change",
        objective="LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence",
        duration="45 minutes",
        prerequisites=[
            "Complete Lab 10.",
            "Open labs/resources/aurora-ad-performance.csv in a spreadsheet application.",
            "Keep the Aurora targets and Lab 10 insight memo available.",
        ],
        desc=(
            "You calculate CTR, click conversion rate, CPA, and ROAS for eighteen synthetic, unpublished paid-media "
            "rows, flag target or tracking breaches, and diagnose the deteriorating commuter ad set. "
            "The workflow checks data quality before creative or budget action."
        ),
        build=(
            "06-optimize/11-paid-media-diagnostics.xlsx and 06-optimize/11-diagnosis-memo.md with "
            "calculated metrics, anomaly flags, a diagnosis tree, evidence, and a safest-next-test recommendation."
        ),
        services="Spreadsheet application, Aurora ad performance CSV, Aurora targets, Lab 10 memo",
        steps=[
            (
                "Save aurora-ad-performance.csv as 06-optimize/11-paid-media-diagnostics.xlsx. Rename the first sheet Raw Ads, freeze row 1, and confirm there are eighteen sandbox-simulation rows from 20-25 July 2026. Check experiment, creative-version, and simulation-status fields before analysis; none of the rows represents a live launch.",
                "",
            ),
            (
                "Insert six blank columns immediately before experiment_id so the lineage fields remain intact. Name columns L CTR, M Click Conversion Rate, N CPA SGD, O ROAS, P Daily Campaign Spend, and Q Review Flag. Enter the formulas below in L2 through Q2 respectively, then fill down through row 19. Format L:M as percentages and N:P as two-decimal numbers.",
                "=IFERROR(G2/F2,0)\n=IFERROR(I2/G2,0)\n=IF(I2=0,\"\",H2/I2)\n=IFERROR(J2/H2,0)\n=SUMIFS($H$2:$H$19,$A$2:$A$19,A2,$B$2:$B$19,B2,$C$2:$C$19,C2)\n=IF(OR(K2<>\"ok\",P2>300,I2=0,N2>24,O2<2.5),\"REVIEW\",\"OK\")",
            ),
            (
                "Create a Metric Definitions sheet. Record formulas, denominators, currency, date window, fictional attribution assumption, and the fact that partial tracking invalidates strong conversion conclusions.",
                "",
            ),
            (
                "Filter campaign HydraLoop Launch, ad_set Commuters. Create a line chart by date for CPA and a second line chart for ROAS. Add a vertical note at 24 July when tracking_status changes to partial.",
                "",
            ),
            (
                "Compare 20 July with 24-25 July for the commuter ad set. Record the exact spend, purchases, CPA, ROAS, CTR, and tracking_status values in an Evidence table.",
                "",
            ),
            (
                "Create 06-optimize/11-diagnosis-memo.md with headings Symptom, Evidence, Data Quality, Competing Explanations, Missing Checks, Safest Next Action, Do Not Do, Owner, and Next Observation.",
                "",
            ),
            (
                "Walk the diagnosis tree in this order: tracking; delivery and auction; audience and frequency; creative and comments; landing page; conversion lag. For every branch write observed, not available, or needs owner check.",
                "",
            ),
            (
                "Use C01/C04 from Lab 10 as contextual evidence that the leak angle raises product-proof questions, but do not claim those comments caused paid results. Note that frequency and landing-page data are not supplied.",
                "",
            ),
            (
                "Set Safest Next Action to hold automated budget or targeting changes, route tracking_status=partial to the analytics owner, and prepare a claim-safe creative experiment only after data quality returns to ok. Under Do Not Do write 'Do not double spend, broaden targeting, or declare creative failure from partial tracking.'",
                "",
            ),
        ],
        test=(
            "All eighteen rows have formulas and review flags. The commuter rows on 24 and 25 July show "
            "partial tracking, CPA of SGD 21.25 and SGD 29.17, and ROAS of 2.26 and 1.65. Every simulated "
            "campaign-day total is at or below the SGD 300 cap, while partial tracking and the 25 July target "
            "breach still route to REVIEW. The memo checks tracking first, "
            "states missing frequency/landing data, cites comments only as context, and recommends no budget "
            "or targeting change until tracking is repaired."
        ),
        deck_test=(
            "All 18 formulas fill down. The 24-25 July commuter rows show partial tracking; 25 July breaches "
            "CPA and ROAS targets. Campaign-day spend stays within SGD 300, and the memo holds budget and "
            "targeting changes until tracking is repaired."
        ),
        troubleshooting=[
            ("CPA shows an error for zero purchases", "Return a blank CPA with IF(I2=0,\"\",H2/I2) and make the review flag test I2=0; do not replace the business meaning with a false zero CPA."),
            ("The chart mixes campaigns", "Filter campaign and ad_set before charting, then verify all plotted rows are the commuter segment."),
            ("The diagnosis jumps straight to creative fatigue", "Move tracking quality to the first branch and list creative as one competing explanation rather than a conclusion."),
        ],
        challenge="Add a three-day rolling CPA and show how smoothing changes the apparent timing of the anomaly, with a note about delayed detection.",
        reflection="Why is 'hold and repair measurement' sometimes a better optimization decision than changing the campaign immediately?",
        checkpoint="A data-quality-first diagnosis and safest-next-test recommendation for the final control-loop design.",
        deck_steps=[
            "Calculate CTR, conversion rate, CPA, and ROAS for eighteen ad rows.",
            "Flag target and tracking breaches, then compare the deteriorating segment over time.",
            "Diagnose tracking first and propose no live change from partial data.",
        ],
    ),
    dict(
        num=12,
        topic=6,
        title="Design and Simulate a Human-Governed Optimization Loop",
        objective="LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence",
        duration="45 minutes",
        prerequisites=[
            "Complete Lab 11 and keep the diagnostics workbook and memo open.",
            "Keep the Lab 1 agent canvas, Lab 2 operating specification, Lab 7 experiment card, and Lab 8 launch checklist available.",
            "Use a document editor and a classroom-approved AI assistant.",
        ],
        desc=(
            "You assemble the course artifacts into a complete observe-validate-diagnose-propose-approve-"
            "learn loop. Three tabletop cases test data-quality stops, bounded experiments, approval gates, "
            "spend caps, cooldowns, idempotency, audit evidence, and rollback."
        ),
        build=(
            "06-optimize/12-optimization-runbook.md containing the loop, rule table, action schema, "
            "three simulation logs, approval matrix, stop conditions, cooldown, and rollback procedure."
        ),
        services="All Aurora campaign checkpoints, document editor, classroom-approved AI assistant",
        steps=[
            (
                "Create 06-optimize/12-optimization-runbook.md with headings Purpose, Loop States, Input Contract, Rule Table, Action Schema, Approval Matrix, Stop Conditions, Cooldown and Rollback, Simulation Log, and Operating Review.",
                "",
            ),
            (
                "Under Loop States, define Observe -> Validate -> Diagnose -> Propose -> Approve -> Execute or Hold -> Learn. State that Execute is a future production state and remains simulated in class.",
                "",
            ),
            (
                "Under Input Contract, require snapshot_id, retrieved_at_sgt, platform, campaign, object level, date window, metric definitions version, tracking_status, data completeness, and source owner. Missing fields route to HOLD.",
                "",
            ),
            (
                "Create a Rule Table with columns Rule ID, Condition, Proposed Action, Max Change, Approval, Cooldown, Rollback Trigger, and Evidence Logged. Add RULE-DQ for non-ok tracking, RULE-CPA for CPA above SGD 24 with ok tracking, RULE-ROAS for ROAS below 2.5, and RULE-SCALE only when ROAS is at least 2.5 in each of two complete seven-day cycles, each cycle has at least 30 purchases, tracking is ok, data completeness is 100%, and there is no claim, complaint, or spend-cap guardrail breach.",
                "",
            ),
            (
                "Set RULE-DQ action to HOLD AND INVESTIGATE with no campaign change. Set RULE-CPA and RULE-ROAS to propose one experiment, not an immediate budget move. Set RULE-SCALE to propose at most a 10% budget increase, still requiring campaign-owner approval and keeping the combined ad sets inside the SGD 300 daily cap for that platform campaign.",
                "",
            ),
            (
                "Define Action Schema fields action_id, run_id, snapshot_id, rule_id, hypothesis, evidence_ids, proposed_change, expected_effect, max_change, approver, status, created_at_sgt, cooldown_until_sgt, rollback_version, result, and next_state. Make action_id unique and state that a repeated action_id cannot execute twice.",
                "",
            ),
            (
                "Simulate Case A from the 24 July commuter row: tracking_status=partial. Expected result is HOLD, analytics-owner ticket, zero budget change, and last safe version retained. Record the complete action schema under Simulation Log.",
                "",
            ),
            (
                "Simulate Case B: tracking is ok, CPA is SGD 31 for three full days, volume is adequate, and claim-trust comments increased. Expected result is a draft creative experiment with control/treatment, brand and campaign-owner approval, and no automatic spend increase.",
                "",
            ),
            (
                "Simulate Case C: tracking is ok, ROAS is 3.1 in each of two complete seven-day cycles, each cycle has 35 purchases, CPA is SGD 20, data completeness is 100%, claim, complaint, and spend-cap guardrails are stable, and current daily spend is SGD 270. Expected result is a proposed 10% increase to SGD 297, human approval required, 72-hour cooldown, and rollback if ROAS falls below 2.5 or tracking degrades.",
                "",
            ),
            (
                "Send the three logs to the assistant for a control audit. Apply only corrections that strengthen traceability or limits. Then duplicate Case C with the same action_id and confirm the runbook outcome is SKIP DUPLICATE rather than a second increase.",
                "Audit these three simulated optimization actions. Check input completeness, rule match, permission, cap arithmetic, approval, cooldown, idempotency, rollback trigger, and evidence log. Return Fail/Pass for each control and an exact correction for every Fail. Do not recommend a larger change.",
            ),
            (
                "Under Operating Review, set a weekly review of false alarms, missed anomalies, approval latency, repeated failures, cap breaches, and rollback outcomes. Save the final runbook as version v1.0 and link every earlier artifact by filename.",
                "",
            ),
        ],
        test=(
            "Case A holds with zero change; Case B proposes one controlled creative experiment; Case C "
            "calculates SGD 297, stays under the cap, requires approval, and sets a 72-hour cooldown and "
            "rollback. Reusing Case C's action_id returns SKIP DUPLICATE. Every log contains all action "
            "schema fields and links to a prior campaign artifact. RULE-SCALE explicitly requires two complete "
            "seven-day cycles, ROAS at least 2.5 in each, at least 30 purchases per cycle, ok tracking, 100% "
            "data completeness, and no claim, complaint, or spend-cap breach."
        ),
        deck_test=(
            "Case A holds; Case B proposes one controlled experiment; Case C proposes SGD 297 with approval, "
            "cooldown, and rollback. Duplicate action IDs return SKIP DUPLICATE. RULE-SCALE requires two "
            "seven-day cycles, at least 30 purchases each, ROAS at least 2.5, clean data, and intact guardrails."
        ),
        troubleshooting=[
            ("The loop proposes a spend change when tracking is partial", "Move RULE-DQ to the highest priority and state that it short-circuits every performance rule."),
            ("The 10% increase exceeds the cap", "Calculate MIN(current spend x 1.10, daily cap) and route any cap conflict to the campaign owner."),
            ("A retry repeats the same action", "Persist action_id with status and reject any Execute request whose ID already exists, regardless of prompt wording."),
        ],
        challenge="Add a portfolio rule that limits the combined daily change across three fictional products while preserving a separate rollback version for each.",
        reflection="Which parts of your final loop can be safely automated now, and what evidence would you need before granting any additional permission?",
        checkpoint="A complete, simulated, human-governed optimization runbook that connects all twelve course labs.",
        deck_steps=[
            "Define the loop, input contract, rules, permissions, cooldown, and rollback.",
            "Simulate data-quality hold, experiment proposal, and bounded scaling cases.",
            "Test idempotency and audit evidence before setting the runbook to v1.0.",
        ],
    ),
]
