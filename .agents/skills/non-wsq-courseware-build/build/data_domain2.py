"""Topic 2 - Automated Trend Discovery and Viral Content Research. Labs 3-4."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Build and Score a Source-Linked Trend Signal Table",
        objective="LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity",
        duration="40 minutes",
        prerequisites=[
            "Complete Labs 1-2.",
            "Open labs/resources/aurora-trend-signals.csv in Excel, Google Sheets, or LibreOffice Calc.",
            "Keep the Aurora brand brief open for brand-fit and risk decisions.",
        ],
        desc=(
            "You normalize eight synthetic trend signals, calculate a transparent opportunity score, "
            "and apply a separate risk veto. You then inspect the strongest and riskiest records so the "
            "ranking is based on evidence rather than engagement alone."
        ),
        build=(
            "02-trends/03-trend-signal-scorecard.xlsx (or a native Google Sheet) with calculated "
            "opportunity_score and decision columns, plus a short data-quality note."
        ),
        services="Spreadsheet application, Aurora trend signals CSV, Aurora brand brief",
        steps=[
            (
                "Save a working copy of aurora-trend-signals.csv as 02-trends/03-trend-signal-scorecard.xlsx. Freeze row 1 and turn on filters.",
                "",
            ),
            (
                "Check that every row contains signal_id, source, observed_at, market, topic, hook, brand_fit_1_5, freshness_1_5, evidence_1_5, risk_1_5, and source_url. Highlight any blank required cell yellow.",
                "",
            ),
            (
                "Add column M named opportunity_score. In M2 enter the formula below, then fill it down through M9. Format it as a whole number.",
                "=ROUND(AVERAGE(H2:J2)*20,0)",
            ),
            (
                "Add column N named decision. In N2 enter the rule below and fill it down. A missing source or risk score 4-5 must HOLD even when freshness is high.",
                "=IF(OR(K2>=4,L2=\"\"),\"HOLD\",IF(M2>=70,\"PROCEED\",IF(M2>=50,\"RESEARCH\",\"PARK\")))",
            ),
            (
                "Apply conditional formatting: PROCEED green, RESEARCH amber, HOLD red, and PARK grey. Sort first by decision and then by opportunity_score from largest to smallest.",
                "",
            ),
            (
                "Inspect T01. Confirm the row describes a product-relevant audience routine, has a source and timestamp, and scores PROCEED. Add a note explaining which verified product fact could support the angle.",
                "",
            ),
            (
                "Inspect T07. Even though its engagement index and freshness are high, confirm the celebrity rumour is HOLD because risk is 5 and evidence is 1. Add the note 'Do not amplify; verify independently or reject.'",
                "",
            ),
            (
                "Create a Data Quality sheet. Record row count 8, required-field completeness, the scoring formula, the decision rule, the fact that source URLs using example.com are synthetic, and the limitation that engagement_index values are not comparable across real platforms.",
                "",
            ),
            (
                "Save the workbook and export the sorted signal table as 02-trends/03-ranked-trend-signals.csv for the next lab.",
                "",
            ),
        ],
        test=(
            "The workbook contains exactly eight signals. T01 has opportunity_score 93 and decision "
            "PROCEED. T07 has opportunity_score 47 and decision HOLD. No row with risk 4 or 5 is "
            "labelled PROCEED, and the Data Quality sheet states the formula and limitations."
        ),
        troubleshooting=[
            ("The formula displays as text", "Change the cell format to General, remove any leading apostrophe, re-enter the formula, and fill down again."),
            ("CSV columns appear in one column", "Import the file with comma as the delimiter and UTF-8 as the character encoding."),
            ("A high-risk row still says PROCEED", "Confirm the risk column is K, the source URL column is L, and the OR test is evaluated before the opportunity thresholds."),
        ],
        challenge="Add a corroboration_count column and require at least two independent source types before a signal can become PROCEED.",
        reflection="Why is a separate risk veto more defensible than subtracting a few risk points from a high opportunity score?",
        checkpoint="A source-linked, formula-driven ranking table that feeds the trend brief.",
        deck_steps=[
            "Validate provenance and required fields for eight synthetic signals.",
            "Calculate opportunity from fit, freshness, and evidence.",
            "Apply an independent risk veto and document data limitations.",
        ],
    ),
    dict(
        num=4,
        topic=2,
        title="Generate a Viral Opportunity Brief and Scheduled Research Spec",
        objective="LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity",
        duration="40 minutes",
        prerequisites=[
            "Complete Lab 3 and keep 02-trends/03-ranked-trend-signals.csv available.",
            "Keep the Lab 2 operating specification and the Aurora brand brief open.",
            "Use a document editor and a classroom-approved AI assistant.",
        ],
        desc=(
            "You use only the ranked records to create an evidence-linked trend opportunity brief. "
            "You then specify a weekly research workflow with a fixed schedule, required fields, "
            "deduplication, expiry, and exception route so the process can be automated safely later."
        ),
        build=(
            "02-trends/04-viral-opportunity-brief.md and 02-trends/04-weekly-trend-workflow-spec.md, "
            "both linked to the Lab 3 signal IDs and review rules."
        ),
        services="Ranked trend CSV, Aurora brief, Lab 2 operating specification, classroom-approved AI assistant",
        steps=[
            (
                "Filter the ranked CSV to PROCEED and RESEARCH rows. Select T01, T03, and T06 as the candidate set because they address routine, leakage, and cleaning needs without relying on the held rumour.",
                "",
            ),
            (
                "Create 02-trends/04-viral-opportunity-brief.md with headings Recommendation, Why Now, Audience Tension, Hook, Evidence, Product Truth, Channel Ideas, Risks, Needs Confirmation, and Next Check.",
                "",
            ),
            (
                "Send the following prompt with only the three selected rows and the fictional brand brief. Ask for one recommended angle, not three disconnected posts.",
                "You are the Aurora trend-research agent operating under the supplied specification. Use only signal IDs T01, T03, and T06 plus the verified brand brief. Recommend one content opportunity. Separate Observation from Interpretation. Cite every supporting signal ID. Extract one hook, three supporting angles, five relevant hashtags or search phrases, and two emotional triggers. Do not infer absolute demand from relative or synthetic signals. Flag every missing fact as NEEDS CONFIRMATION. Return the exact headings: Recommendation, Why Now, Audience Tension, Hook, Evidence, Product Truth, Channel Ideas, Risks, Needs Confirmation, Next Check.",
            ),
            (
                "Paste the response into the brief. Check each factual statement against the candidate rows and brand brief. Remove any invented certification, testimonial, sales result, health benefit, or competitor claim.",
                "",
            ),
            (
                "Add this decision statement at the top: 'Recommended angle: Stop the bag spill with a practical commute-bag hydration routine.' Mark the status REVIEW because the leak-resistant claim still needs the product owner to confirm evidence for the planned demonstration.",
                "",
            ),
            (
                "Create 02-trends/04-weekly-trend-workflow-spec.md. Add the states Collect, Normalize, Enrich, Score, Review, Brief, and Archive with one input and one output for each.",
                "",
            ),
            (
                "Set the schedule to Monday at 08:30 Asia/Singapore. Set lookback to 7 days, maximum signal age to 72 hours for 'active' status, and deduplication key to lowercase(topic + market + source_url).",
                "Schedule: Monday 08:30 Asia/Singapore\nLookback: 7 days\nActive signal age: <= 72 hours\nDedup key: lowercase(topic + market + source_url)",
            ),
            (
                "Define exception routes: missing URL -> RESEARCH; risk 4-5 -> HOLD; source older than 72 hours -> STALE; duplicate key -> MERGE; fewer than two credible sources -> NEEDS CORROBORATION; workflow error -> create review ticket and retain the last successful brief.",
                "",
            ),
            (
                "Add an output schema with run_id, signal_ids, retrieved_at_sgt, brief_version, reviewer, status, and archive_path. Save both files and link the brief to 03-trend-signal-scorecard.xlsx.",
                "",
            ),
        ],
        test=(
            "The opportunity brief recommends one angle, cites only T01/T03/T06, separates observation "
            "and interpretation, and marks the product demonstration for review. The workflow spec says "
            "Monday 08:30 Asia/Singapore, 7-day lookback, 72-hour active limit, a deduplication key, six "
            "exception routes, and a versioned output schema."
        ),
        troubleshooting=[
            ("The AI cites a signal not supplied", "Delete the unsupported claim, restate the allowed signal IDs in the first and last sentence of the prompt, and regenerate."),
            ("The brief confuses engagement with market demand", "Replace the claim with an observation about the supplied index and add the limitation that it is synthetic and cross-platform values are not directly comparable."),
            ("The schedule lacks a failure path", "Add a review ticket, last-successful-output retention, and a named marketing owner before considering the spec complete."),
        ],
        challenge="Add a second weekly run for Friday 15:00 SGT that reports only material changes since Monday rather than repeating the full brief.",
        reflection="Which part of the brief is evidence and which part is a creative hypothesis that still needs a test?",
        checkpoint="A selected, review-gated trend angle and a reproducible weekly research specification for the content labs.",
        deck_steps=[
            "Turn three ranked signals into one evidence-linked opportunity.",
            "Review every claim and mark missing product evidence explicitly.",
            "Specify schedule, freshness, deduplication, exceptions, and versioned output.",
        ],
    ),
]
