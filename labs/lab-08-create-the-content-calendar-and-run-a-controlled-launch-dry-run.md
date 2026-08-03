# Lab 8 — Create the Content Calendar and Run a Controlled Launch Dry-Run

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 4:** Creating and Launching AI-Driven Marketing Campaigns  
**Maps to:** LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs  
**Tools:** Spreadsheet application, Labs 5-7 artifacts, document editor  
**Duration:** 40 minutes

---

## Goal

LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs.

## What You Will Do

You schedule eight draft content items across one week, attach owners and evidence, and walk each item through a launch-state dry-run. A formula prevents an incomplete row from entering review, while a zero-LIVE check proves nothing was published during class.

## What You Will Build

04-launch/08-content-calendar.xlsx and 04-launch/08-launch-checklist.md with eight versioned draft items, readiness flags, approval ownership, observation windows, and rollback steps.

## Prerequisites

- Complete Lab 7 and keep the campaign blueprint open.
- Keep the four-platform content kit and creative board available.
- Use a spreadsheet application and a document editor.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Create 04-launch/08-content-calendar.xlsx. In row 1 add columns Item ID, Date, Time SGT, Platform, Segment, Asset Version, Copy Version, CTA URL, Claim IDs, Owner, Status, Readiness, Experiment Arm, First Check, and Rollback Version.**

**2. Add eight items dated across a Monday-Sunday week: two Instagram, two Facebook, two LinkedIn, and two X. Use item IDs CAL-01 through CAL-08 and times in Asia/Singapore.**

**3. For each row, reference the exact Lab 5 copy section and Lab 6 asset or storyboard version. Use https://example.com/hydraloop as the classroom-only CTA URL and copy the required Claim IDs from the ledger.**

**4. Set every Status cell in K2:K9 to DRAFT. In L2 enter the readiness formula below and fill it down. The row may enter REVIEW only when all required fields are present and Status is DRAFT or REVIEW.**

```text
=IF(OR(COUNTA(A2:J2)<10,N2="",O2="",AND(OR(A2="CAL-01",A2="CAL-02"),M2="")),"INCOMPLETE",IF(OR(K2="DRAFT",K2="REVIEW"),"READY FOR REVIEW","CHECK STATE"))
```

**5. Assign CAL-01 and CAL-02 to EXP-01 Control and Treatment. Keep their platform, segment, date window, offer, CTA, and creative style aligned; only the planned hook differs.**

**6. Set First Check to two hours after the scheduled time for routine delivery checks and next-business-day for the first performance note. Set Rollback Version to the last approved copy and asset version, not a blank value.**

**7. Create 04-launch/08-launch-checklist.md with sections Tracking, Creative and Copy, Claims and Rights, Audience and Placement, Budget and Pacing, Schedule and Timezone, Response Owner, Approval Record, First Observation, Pause Conditions, and Rollback.**

**8. Run a tabletop dry-run for CAL-01. Move its spreadsheet Status from DRAFT to REVIEW only. In the checklist record the item ID, versions, reviewer, unresolved leak-demonstration evidence, and decision HOLD IN REVIEW until the product owner confirms the demonstration protocol.**

**9. Add a control cell labelled LIVE Count with formula =COUNTIF(K2:K9,"LIVE"). Confirm the result is 0. Save the workbook and checklist without opening any social scheduling or advertising account.**

```text
=COUNTIF(K2:K9,"LIVE")
```

## Test It

The calendar has eight unique item IDs, complete dates/times/platforms/versions/owners, two aligned experiment arms, and no blank rollback version. CAL-01 is REVIEW with a documented hold reason; all other rows are DRAFT. LIVE Count equals 0 and the checklist covers all eleven sections.

## Checkpoint for the Next Lab

A zero-LIVE content calendar and complete controlled-launch checklist ready for synthetic performance monitoring.

## Troubleshooting

- **Readiness says INCOMPLETE:** Filter column L, fill the missing field in A:J from the approved artifacts, and do not bypass the formula.
- **The experiment rows differ in more than the hook:** Copy the control row, create a new item ID, and edit only the hook-specific copy version.
- **A platform opens a live composer:** Close it without saving, return to the spreadsheet dry-run, and keep the class workflow account-free.

## Challenge

Add a dependency column that prevents a Treatment item moving to REVIEW until the matching Control item and experiment card share the same experiment version.

## Reflection

Which launch check is easiest to automate reliably, and which still requires contextual human judgement?

---

[← Lab 7](lab-07-build-the-campaign-blueprint-kpi-tree-and-experiment-map.md) · [Lab 9 →](lab-09-build-a-social-performance-dashboard-with-defined-metrics.md)
