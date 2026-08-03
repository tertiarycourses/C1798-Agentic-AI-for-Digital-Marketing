# Lab 3 — Build and Score a Source-Linked Trend Signal Table

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 2:** Automated Trend Discovery and Viral Content Research  
**Maps to:** LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity  
**Tools:** Spreadsheet application, Aurora trend signals CSV, Aurora brand brief  
**Duration:** 40 minutes

---

## Goal

LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity.

## What You Will Do

You normalize eight synthetic trend signals, calculate a transparent opportunity score, and apply a separate risk veto. You then inspect the strongest and riskiest records so the ranking is based on evidence rather than engagement alone.

## What You Will Build

02-trends/03-trend-signal-scorecard.xlsx (or a native Google Sheet) with calculated opportunity_score and decision columns, plus a short data-quality note.

## Prerequisites

- Complete Labs 1-2.
- Open labs/resources/aurora-trend-signals.csv in Excel, Google Sheets, or LibreOffice Calc.
- Keep the Aurora brand brief open for brand-fit and risk decisions.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Save a working copy of aurora-trend-signals.csv as 02-trends/03-trend-signal-scorecard.xlsx. Freeze row 1 and turn on filters.**

**2. Check that every row contains signal_id, source, observed_at, market, topic, hook, brand_fit_1_5, freshness_1_5, evidence_1_5, risk_1_5, and source_url. Highlight any blank required cell yellow.**

**3. Add column M named opportunity_score. In M2 enter the formula below, then fill it down through M9. Format it as a whole number.**

```text
=ROUND(AVERAGE(H2:J2)*20,0)
```

**4. Add column N named decision. In N2 enter the rule below and fill it down. A missing source or risk score 4-5 must HOLD even when freshness is high.**

```text
=IF(OR(K2>=4,L2=""),"HOLD",IF(M2>=70,"PROCEED",IF(M2>=50,"RESEARCH","PARK")))
```

**5. Apply conditional formatting: PROCEED green, RESEARCH amber, HOLD red, and PARK grey. Sort first by decision and then by opportunity_score from largest to smallest.**

**6. Inspect T01. Confirm the row describes a product-relevant audience routine, has a source and timestamp, and scores PROCEED. Add a note explaining which verified product fact could support the angle.**

**7. Inspect T07. Even though its engagement index and freshness are high, confirm the celebrity rumour is HOLD because risk is 5 and evidence is 1. Add the note 'Do not amplify; verify independently or reject.'**

**8. Create a Data Quality sheet. Record row count 8, required-field completeness, the scoring formula, the decision rule, the fact that source URLs using example.com are synthetic, and the limitation that engagement_index values are not comparable across real platforms.**

**9. Save the workbook and export the sorted signal table as 02-trends/03-ranked-trend-signals.csv for the next lab.**

## Test It

The workbook contains exactly eight signals. T01 has opportunity_score 93 and decision PROCEED. T07 has opportunity_score 47 and decision HOLD. No row with risk 4 or 5 is labelled PROCEED, and the Data Quality sheet states the formula and limitations.

## Checkpoint for the Next Lab

A source-linked, formula-driven ranking table that feeds the trend brief.

## Troubleshooting

- **The formula displays as text:** Change the cell format to General, remove any leading apostrophe, re-enter the formula, and fill down again.
- **CSV columns appear in one column:** Import the file with comma as the delimiter and UTF-8 as the character encoding.
- **A high-risk row still says PROCEED:** Confirm the risk column is K, the source URL column is L, and the OR test is evaluated before the opportunity thresholds.

## Challenge

Add a corroboration_count column and require at least two independent source types before a signal can become PROCEED.

## Reflection

Why is a separate risk veto more defensible than subtracting a few risk points from a high opportunity score?

---

[← Lab 2](lab-02-write-and-test-the-marketing-agent-operating-specification.md) · [Lab 4 →](lab-04-generate-a-viral-opportunity-brief-and-scheduled-research-spec.md)
