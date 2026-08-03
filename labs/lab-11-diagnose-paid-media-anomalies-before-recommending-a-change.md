# Lab 11 — Diagnose Paid-Media Anomalies Before Recommending a Change

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 6:** Agentic AI for Advertising Optimization and Scaling  
**Maps to:** LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence  
**Tools:** Spreadsheet application, Aurora ad performance CSV, Aurora targets, Lab 10 memo  
**Duration:** 45 minutes

---

## Goal

LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence.

## What You Will Do

You calculate CTR, click conversion rate, CPA, and ROAS for eighteen synthetic, unpublished paid-media rows, flag target or tracking breaches, and diagnose the deteriorating commuter ad set. The workflow checks data quality before creative or budget action.

## What You Will Build

06-optimize/11-paid-media-diagnostics.xlsx and 06-optimize/11-diagnosis-memo.md with calculated metrics, anomaly flags, a diagnosis tree, evidence, and a safest-next-test recommendation.

## Prerequisites

- Complete Lab 10.
- Open labs/resources/aurora-ad-performance.csv in a spreadsheet application.
- Keep the Aurora targets and Lab 10 insight memo available.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Save aurora-ad-performance.csv as 06-optimize/11-paid-media-diagnostics.xlsx. Rename the first sheet Raw Ads, freeze row 1, and confirm there are eighteen sandbox-simulation rows from 20-25 July 2026. Check experiment, creative-version, and simulation-status fields before analysis; none of the rows represents a live launch.**

**2. Insert six blank columns immediately before experiment_id so the lineage fields remain intact. Name columns L CTR, M Click Conversion Rate, N CPA SGD, O ROAS, P Daily Campaign Spend, and Q Review Flag. Enter the formulas below in L2 through Q2 respectively, then fill down through row 19. Format L:M as percentages and N:P as two-decimal numbers.**

```text
=IFERROR(G2/F2,0)
=IFERROR(I2/G2,0)
=IF(I2=0,"",H2/I2)
=IFERROR(J2/H2,0)
=SUMIFS($H$2:$H$19,$A$2:$A$19,A2,$B$2:$B$19,B2,$C$2:$C$19,C2)
=IF(OR(K2<>"ok",P2>300,I2=0,N2>24,O2<2.5),"REVIEW","OK")
```

**3. Create a Metric Definitions sheet. Record formulas, denominators, currency, date window, fictional attribution assumption, and the fact that partial tracking invalidates strong conversion conclusions.**

**4. Filter campaign HydraLoop Launch, ad_set Commuters. Create a line chart by date for CPA and a second line chart for ROAS. Add a vertical note at 24 July when tracking_status changes to partial.**

**5. Compare 20 July with 24-25 July for the commuter ad set. Record the exact spend, purchases, CPA, ROAS, CTR, and tracking_status values in an Evidence table.**

**6. Create 06-optimize/11-diagnosis-memo.md with headings Symptom, Evidence, Data Quality, Competing Explanations, Missing Checks, Safest Next Action, Do Not Do, Owner, and Next Observation.**

**7. Walk the diagnosis tree in this order: tracking; delivery and auction; audience and frequency; creative and comments; landing page; conversion lag. For every branch write observed, not available, or needs owner check.**

**8. Use C01/C04 from Lab 10 as contextual evidence that the leak angle raises product-proof questions, but do not claim those comments caused paid results. Note that frequency and landing-page data are not supplied.**

**9. Set Safest Next Action to hold automated budget or targeting changes, route tracking_status=partial to the analytics owner, and prepare a claim-safe creative experiment only after data quality returns to ok. Under Do Not Do write 'Do not double spend, broaden targeting, or declare creative failure from partial tracking.'**

## Test It

All eighteen rows have formulas and review flags. The commuter rows on 24 and 25 July show partial tracking, CPA of SGD 21.25 and SGD 29.17, and ROAS of 2.26 and 1.65. Every simulated campaign-day total is at or below the SGD 300 cap, while partial tracking and the 25 July target breach still route to REVIEW. The memo checks tracking first, states missing frequency/landing data, cites comments only as context, and recommends no budget or targeting change until tracking is repaired.

## Checkpoint for the Next Lab

A data-quality-first diagnosis and safest-next-test recommendation for the final control-loop design.

## Troubleshooting

- **CPA shows an error for zero purchases:** Return a blank CPA with IF(I2=0,"",H2/I2) and make the review flag test I2=0; do not replace the business meaning with a false zero CPA.
- **The chart mixes campaigns:** Filter campaign and ad_set before charting, then verify all plotted rows are the commuter segment.
- **The diagnosis jumps straight to creative fatigue:** Move tracking quality to the first branch and list creative as one competing explanation rather than a conclusion.

## Challenge

Add a three-day rolling CPA and show how smoothing changes the apparent timing of the anomaly, with a note about delayed detection.

## Reflection

Why is 'hold and repair measurement' sometimes a better optimization decision than changing the campaign immediately?

---

[← Lab 10](lab-10-analyse-audience-feedback-and-produce-an-insight-to-content-memo.md) · [Lab 12 →](lab-12-design-and-simulate-a-human-governed-optimization-loop.md)
