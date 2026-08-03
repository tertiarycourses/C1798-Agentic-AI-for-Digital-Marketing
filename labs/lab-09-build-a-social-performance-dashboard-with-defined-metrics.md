# Lab 9 — Build a Social Performance Dashboard with Defined Metrics

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 5:** Agentic AI for Social Media Performance Monitoring  
**Maps to:** LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations  
**Tools:** Spreadsheet application, Aurora post performance CSV, Lab 7 KPI Dictionary  
**Duration:** 40 minutes

---

## Goal

LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations.

## What You Will Do

You calculate platform-neutral performance rates from ten simulated, unpublished posts, validate the denominators, and build a compact dashboard. You separate descriptive findings from causal claims so the dashboard becomes a decision aid rather than a leaderboard.

## What You Will Build

05-monitor/09-social-performance-dashboard.xlsx containing raw data, calculated metrics, a summary table, two charts, metric definitions, and a three-part insight note.

## Prerequisites

- Complete Lab 8.
- Open labs/resources/aurora-post-performance.csv, a synthetic sandbox simulation that uses the Lab 8 plan plus two labelled control or benchmark rows, in a spreadsheet application.
- Keep the KPI Dictionary from Lab 7 available.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Save a working copy of aurora-post-performance.csv as 05-monitor/09-social-performance-dashboard.xlsx. Rename the first sheet Raw Posts and freeze row 1.**

**2. Check that there are ten unique post_id values and no blank platform, reach, impressions, clicks, or simulation_status fields. Confirm impressions are greater than or equal to reach for every row. Check the calendar_item_id, experiment_id, experiment_arm, asset_version, and copy_version lineage fields; P08 is a deliberately failed legacy negative control marked DO NOT REUSE, and P09 is an unpublished benchmark outside the eight-item Lab 8 calendar. Neither is a published Lab 8 item.**

**3. Insert four blank columns immediately before calendar_item_id so the lineage fields remain intact. Name column O engagements. In O2 sum likes, comments, shares, and saves, then fill down to O11.**

```text
=SUM(I2:L2)
```

**4. Add columns P click_through_rate, Q engagement_rate_by_reach, and R video_view_rate. Enter the formulas below in P2, Q2, and R2 respectively, then fill down through row 11. Format P:R as percentages with two decimals.**

```text
=IFERROR(H2/G2,0)
=IFERROR(O2/F2,0)
=IFERROR(M2/G2,0)
```

**5. Create a Metric Definitions sheet with columns Metric, Formula, Denominator, Source Columns, Interpretation, and Limitation. Document reach, impressions, engagements, CTR, engagement rate by reach, and video view rate.**

**6. Create a Summary sheet. Build a pivot table with platform in rows and sums of reach, impressions, clicks, and engagements in values. Add calculated overall CTR as total clicks divided by total impressions rather than averaging row percentages.**

**7. Add a ranked post table showing post_id, platform, theme, clicks, CTR, engagements, engagement rate, and video view rate. Sort once by clicks and once by CTR to see whether the leader changes.**

**8. Create two charts: a clustered column chart of clicks by post_id and a horizontal bar chart of engagement_rate_by_reach by post_id. Use direct labels and titles that name the denominator.**

**9. Write an Insight Note with labelled Observation, Interpretation, Recommendation, Evidence IDs, Confidence, and Next Check. Use P10 as the click observation, P08 as the low-CTR observation, and the related content themes. Do not state that theme alone caused the results.**

## Test It

The Raw Posts sheet contains ten unique rows and formulas through row 11. P10 has the most clicks (522). P08 has the lowest CTR at about 0.68%. The summary uses aggregated numerators and denominators, both charts name their metric, and the insight note cites P10 and P08 while separating observation from interpretation. P08 is identified as a simulated negative-control failure marked DO NOT REUSE.

## Checkpoint for the Next Lab

A denominator-aware social dashboard that provides quantitative evidence for comment analysis.

## Troubleshooting

- **Percentages show values such as 250%:** Confirm clicks are divided by impressions, apply percentage formatting once, and do not multiply the formula by 100.
- **The platform CTR is an average of row CTR:** Replace it with SUM(clicks)/SUM(impressions) so differently sized posts receive the correct weight.
- **A chart implies a causal winner:** Retitle it as observed performance, add the date window, and move causal language into a testable hypothesis.

## Challenge

Add a format-level summary and compare Reels, images, carousels, video, and text while clearly noting the small synthetic sample sizes.

## Reflection

How did the ranking change when you sorted by clicks versus rate, and what decision risk comes from choosing only one view?

---

[← Lab 8](lab-08-create-the-content-calendar-and-run-a-controlled-launch-dry-run.md) · [Lab 10 →](lab-10-analyse-audience-feedback-and-produce-an-insight-to-content-memo.md)
