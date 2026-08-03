"""Topic 5 - Agentic AI for Social Media Performance Monitoring. Labs 9-10."""

DOMAIN5 = [
    dict(
        num=9,
        topic=5,
        title="Build a Social Performance Dashboard with Defined Metrics",
        objective="LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations",
        duration="40 minutes",
        prerequisites=[
            "Complete Lab 8.",
            "Open labs/resources/aurora-post-performance.csv, a synthetic sandbox simulation that uses the Lab 8 plan plus two labelled control or benchmark rows, in a spreadsheet application.",
            "Keep the KPI Dictionary from Lab 7 available.",
        ],
        desc=(
            "You calculate platform-neutral performance rates from ten simulated, unpublished posts, validate the "
            "denominators, and build a compact dashboard. You separate descriptive findings from causal "
            "claims so the dashboard becomes a decision aid rather than a leaderboard."
        ),
        build=(
            "05-monitor/09-social-performance-dashboard.xlsx containing raw data, calculated metrics, "
            "a summary table, two charts, metric definitions, and a three-part insight note."
        ),
        services="Spreadsheet application, Aurora post performance CSV, Lab 7 KPI Dictionary",
        steps=[
            (
                "Save a working copy of aurora-post-performance.csv as 05-monitor/09-social-performance-dashboard.xlsx. Rename the first sheet Raw Posts and freeze row 1.",
                "",
            ),
            (
                "Check that there are ten unique post_id values and no blank platform, reach, impressions, clicks, or simulation_status fields. Confirm impressions are greater than or equal to reach for every row. Check the calendar_item_id, experiment_id, experiment_arm, asset_version, and copy_version lineage fields; P08 is a deliberately failed legacy negative control marked DO NOT REUSE, and P09 is an unpublished benchmark outside the eight-item Lab 8 calendar. Neither is a published Lab 8 item.",
                "",
            ),
            (
                "Insert four blank columns immediately before calendar_item_id so the lineage fields remain intact. Name column O engagements. In O2 sum likes, comments, shares, and saves, then fill down to O11.",
                "=SUM(I2:L2)",
            ),
            (
                "Add columns P click_through_rate, Q engagement_rate_by_reach, and R video_view_rate. Enter the formulas below in P2, Q2, and R2 respectively, then fill down through row 11. Format P:R as percentages with two decimals.",
                "=IFERROR(H2/G2,0)\n=IFERROR(O2/F2,0)\n=IFERROR(M2/G2,0)",
            ),
            (
                "Create a Metric Definitions sheet with columns Metric, Formula, Denominator, Source Columns, Interpretation, and Limitation. Document reach, impressions, engagements, CTR, engagement rate by reach, and video view rate.",
                "",
            ),
            (
                "Create a Summary sheet. Build a pivot table with platform in rows and sums of reach, impressions, clicks, and engagements in values. Add calculated overall CTR as total clicks divided by total impressions rather than averaging row percentages.",
                "",
            ),
            (
                "Add a ranked post table showing post_id, platform, theme, clicks, CTR, engagements, engagement rate, and video view rate. Sort once by clicks and once by CTR to see whether the leader changes.",
                "",
            ),
            (
                "Create two charts: a clustered column chart of clicks by post_id and a horizontal bar chart of engagement_rate_by_reach by post_id. Use direct labels and titles that name the denominator.",
                "",
            ),
            (
                "Write an Insight Note with labelled Observation, Interpretation, Recommendation, Evidence IDs, Confidence, and Next Check. Use P10 as the click observation, P08 as the low-CTR observation, and the related content themes. Do not state that theme alone caused the results.",
                "",
            ),
        ],
        test=(
            "The Raw Posts sheet contains ten unique rows and formulas through row 11. P10 has the most "
            "clicks (522). P08 has the lowest CTR at about 0.68%. The summary uses aggregated numerators "
            "and denominators, both charts name their metric, and the insight note cites P10 and P08 while "
            "separating observation from interpretation. P08 is identified as a simulated negative-control "
            "failure marked DO NOT REUSE."
        ),
        deck_test=(
            "Ten unique rows calculate correctly; P10 leads clicks and P08 has about 0.68% CTR. The summary "
            "uses weighted denominators, charts are labelled, and the insight separates observation from "
            "interpretation while marking P08 DO NOT REUSE."
        ),
        troubleshooting=[
            ("Percentages show values such as 250%", "Confirm clicks are divided by impressions, apply percentage formatting once, and do not multiply the formula by 100."),
            ("The platform CTR is an average of row CTR", "Replace it with SUM(clicks)/SUM(impressions) so differently sized posts receive the correct weight."),
            ("A chart implies a causal winner", "Retitle it as observed performance, add the date window, and move causal language into a testable hypothesis."),
        ],
        challenge="Add a format-level summary and compare Reels, images, carousels, video, and text while clearly noting the small synthetic sample sizes.",
        reflection="How did the ranking change when you sorted by clicks versus rate, and what decision risk comes from choosing only one view?",
        checkpoint="A denominator-aware social dashboard that provides quantitative evidence for comment analysis.",
        deck_steps=[
            "Validate ten post records and calculate engagements, CTR, and rates.",
            "Aggregate with weighted formulas and build two labelled charts.",
            "Write an evidence-linked insight that separates fact from hypothesis.",
        ],
    ),
    dict(
        num=10,
        topic=5,
        title="Analyse Audience Feedback and Produce an Insight-to-Content Memo",
        objective="LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations",
        duration="40 minutes",
        prerequisites=[
            "Complete Lab 9 and keep the dashboard open.",
            "Open labs/resources/aurora-comments.csv.",
            "Use a spreadsheet application, document editor, and classroom-approved AI assistant.",
        ],
        desc=(
            "You classify twelve synthetic comments by sentiment, theme, severity, and owner, then review "
            "the AI labels against the original text. You combine comment evidence with the dashboard to "
            "propose one bounded content revision and one experiment."
        ),
        build=(
            "05-monitor/10-comment-analysis.xlsx and 05-monitor/10-insight-to-content-memo.md with "
            "reviewed labels, escalation routes, representative evidence, and a controlled next action."
        ),
        services="Aurora comments CSV, Lab 9 dashboard, spreadsheet application, classroom-approved AI assistant",
        steps=[
            (
                "Save aurora-comments.csv as 05-monitor/10-comment-analysis.xlsx. Add columns D Sentiment, E Theme, F Severity, G Evidence Phrase, H Suggested Owner, I Draft Response, J Human Review, and K Reviewer Note.",
                "",
            ),
            (
                "Send all twelve synthetic comments to the AI assistant with the exact schema below. Ask for one row per comment_id and no invented product facts.",
                "Classify each supplied synthetic comment. Return a Markdown table with Comment ID, Sentiment (positive/neutral/negative/mixed), Theme (price/leak concern/hydration routine/colour/cleaning/team bundle/offer/claim trust/other), Severity (routine/investigate/urgent), Evidence Phrase, Suggested Owner (community/product/brand/legal/privacy), Draft Response, and Human Review (yes/no). Preserve the comment ID. For claim-trust, legal, health, safety, privacy, or uncertain product facts, set Human Review=yes and do not invent an answer.",
            ),
            (
                "Copy the labels into columns D:J. Compare every row with the original comment. In K record confirmed or the exact manual correction; never accept a label without reading the source row.",
                "",
            ),
            (
                "Verify C06 and C07 are theme claim trust, severity investigate or urgent, Suggested Owner brand or legal, and Human Review yes. Verify C11 also routes to review because it raises health-claim risk.",
                "",
            ),
            (
                "Create a Summary sheet with counts by Sentiment, Theme, Severity, Suggested Owner, and Human Review. Add one representative comment_id for the three most frequent themes.",
                "",
            ),
            (
                "Create 05-monitor/10-insight-to-content-memo.md with headings Quantitative Observation, Qualitative Observation, Interpretation, Alternative Explanation, Recommendation, Evidence, Owner, Guardrail, and Next Check.",
                "",
            ),
            (
                "Under Quantitative Observation cite P08's low CTR and P10's leading click count from Lab 9. Under Qualitative Observation cite C06 and C07 as claim-trust concerns and C01/C04 as leak-proof questions. Do not copy names or infer customer traits.",
                "",
            ),
            (
                "Mark P08 / LEGACY-FAIL-01 DO NOT REUSE and replace that negative-control concept with a product-owner-approved, clearly described leak-resistance demonstration. State that the demonstration result must exist before a performance claim is written.",
                "",
            ),
            (
                "Define the next check as controlled hook experiment EXP-01 with claim-trust comments as a guardrail and link CTR as the primary KPI. Assign product owner and brand reviewer. Save both files.",
                "",
            ),
        ],
        test=(
            "All twelve comment IDs have reviewed labels and reviewer notes. C06, C07, and C11 require "
            "human review. The memo cites P08, P10, C01, C04, C06, and C07; separates observation from "
            "interpretation; marks P08 / LEGACY-FAIL-01 DO NOT REUSE; and proposes EXP-01 without asserting an unperformed result."
        ),
        troubleshooting=[
            ("The assistant returns fewer than twelve rows", "List the missing comment IDs explicitly and request only those rows using the same schema."),
            ("A draft response invents a product answer", "Replace it with an acknowledgement and route to PRODUCT_OWNER; keep Human Review yes."),
            ("The memo treats sentiment as representative of all customers", "State the sample size, synthetic source, and that comments are directional qualitative evidence only."),
        ],
        challenge="Add a confidence column and require low-confidence or mixed labels to be reviewed by a second learner before they enter the summary.",
        reflection="What useful context did the comments add that the dashboard metrics alone could not provide?",
        checkpoint="A reviewed audience-feedback table and evidence-linked memo that feeds paid-media diagnosis and optimization design.",
        deck_steps=[
            "Classify twelve synthetic comments using a strict output schema.",
            "Review every label and route claim, health, or product uncertainty.",
            "Combine comment and performance evidence into one bounded next experiment.",
        ],
    ),
]
