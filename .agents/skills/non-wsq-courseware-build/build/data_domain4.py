"""Topic 4 - Creating and Launching AI-Driven Marketing Campaigns. Labs 7-8."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Build the Campaign Blueprint, KPI Tree, and Experiment Map",
        objective="LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs",
        duration="40 minutes",
        prerequisites=[
            "Complete Labs 5-6.",
            "Keep the Aurora brand brief, content kit, creative board, and claim ledger open.",
            "Use a document editor and a classroom-approved AI assistant.",
        ],
        desc=(
            "You connect the Aurora business objective to segments, messages, creative formats, KPIs, "
            "guardrails, and one controlled experiment. The blueprint prevents the agent from optimizing "
            "a convenient platform metric that is disconnected from the launch outcome."
        ),
        build=(
            "04-launch/07-campaign-blueprint.md containing an objective tree, segment-message matrix, "
            "channel roles, KPI dictionary, experiment card, and ownership map."
        ),
        services="Aurora brief, Labs 5-6 artifacts, document editor, classroom-approved AI assistant",
        steps=[
            (
                "Create 04-launch/07-campaign-blueprint.md with headings Business Outcome, Campaign Objective, Segments, Message and Creative Matrix, Channel Roles, KPI Dictionary, Experiment Card, Guardrails, and Owners.",
                "",
            ),
            (
                "Under Business Outcome, enter first-week HydraLoop purchases. Under Campaign Objective, enter qualified product-page visits and purchases during the four-week launch. Keep the fictional SGD 300 daily spend cap per platform campaign visible; the cap applies to the combined ad sets in that campaign each day.",
                "",
            ),
            (
                "Create a KPI tree with: outcome = purchases/revenue; conversion = purchase; decision KPIs = CPA, landing conversion rate, and ROAS; diagnostics = impressions, reach, CTR, CPC, engagement, and sentiment; guardrails = tracking quality, complaint signals, claim status, and spend cap.",
                "",
            ),
            (
                "Create a KPI Dictionary table with columns KPI, Formula, Denominator, Source, Window, Target, Limitation, and Owner. Enter the targets from the Aurora brief and write each formula explicitly.",
                "CTR = clicks / impressions\nLanding conversion rate = purchases / product-page sessions\nCPA = spend / purchases\nROAS = attributed purchase revenue / spend",
            ),
            (
                "Create one matrix row for each Aurora segment. Use columns Segment, Situation, Tension, Promise, Evidence, Objection, Format, CTA, and Claim IDs. Reuse only facts from the claim ledger.",
                "",
            ),
            (
                "Assign channel roles: Instagram = visual discovery; Facebook = practical demonstration and discussion; LinkedIn = workplace wellbeing context; X = timely reminder; Google Ads = active-intent capture. These are planning roles, not guaranteed outcomes.",
                "",
            ),
            (
                "Ask the assistant to identify gaps and return exact edits rather than a new strategy. Apply only revisions supported by the supplied artifacts.",
                "Review this campaign blueprint for broken links between business outcome, segment, message, evidence, channel role, KPI, and owner. Return a table with Broken Link, Consequence, Exact Fix, and Evidence Needed. Do not add new facts or channels.",
            ),
            (
                "Create Experiment Card EXP-01. Hypothesis: because commuters respond to bag-leak tension, a demonstrated-use hook will improve product-page CTR versus the colour-choice hook. Control = colour-choice hook. Treatment = bag-leak tension hook. Keep audience, placement, offer, image style, and CTA stable.",
                "",
            ),
            (
                "Set primary KPI to link CTR and calculate it as total clicks divided by total impressions for each arm. Require at least 10,000 impressions and 150 clicks per arm across one complete seven-day cycle. Promote the treatment only if relative CTR lift is at least 10%, tracking is ok, and claim-trust comments do not increase; otherwise continue, stop, or redesign. Stop immediately on a tracking, claim, or complaint guardrail breach. Set status to DESIGNED - NOT LAUNCHED and name campaign owner, analyst, brand reviewer, and product-evidence owner.",
                "",
            ),
        ],
        test=(
            "The blueprint links the business outcome to a conversion, three decision KPIs, diagnostics, "
            "and guardrails. All three segments have complete matrix rows. EXP-01 changes one primary hook, "
            "names control and treatment, keeps other fields stable, requires 10,000 impressions and 150 "
            "clicks per arm, calculates aggregate CTR, defines a 10% lift plus guardrail decision rule, "
            "and is marked NOT LAUNCHED."
        ),
        deck_test=(
            "The blueprint links outcome, decision KPIs, diagnostics, and guardrails. EXP-01 changes one "
            "hook, requires 10,000 impressions and 150 clicks per arm over seven days, and promotes only "
            "on at least 10% CTR lift with intact guardrails."
        ),
        troubleshooting=[
            ("The KPI dictionary lists names but no formulas", "Add the exact numerator and denominator and state the platform field or source for each metric."),
            ("The experiment changes copy, image, audience, and offer", "Choose one primary hook change and copy every other control field unchanged into both arms."),
            ("A segment depends on inferred sensitive traits", "Rewrite it around an observable situation and need, such as commute-bag use or office bundle planning."),
        ],
        challenge="Add a second experiment card for a landing-page message test, but schedule it after EXP-01 so the two effects are not confounded.",
        reflection="Which metric in your KPI tree should drive the decision, and which metrics only help explain that result?",
        checkpoint="A coherent campaign blueprint and predeclared experiment that the calendar can operationalize.",
        deck_steps=[
            "Connect business outcome, conversion, decision KPIs, diagnostics, and guardrails.",
            "Align each segment with a verified message, evidence, format, and CTA.",
            "Predeclare one controlled experiment and its decision rule.",
        ],
    ),
    dict(
        num=8,
        topic=4,
        title="Create the Content Calendar and Run a Controlled Launch Dry-Run",
        objective="LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs",
        duration="40 minutes",
        prerequisites=[
            "Complete Lab 7 and keep the campaign blueprint open.",
            "Keep the four-platform content kit and creative board available.",
            "Use a spreadsheet application and a document editor.",
        ],
        desc=(
            "You schedule eight draft content items across one week, attach owners and evidence, and "
            "walk each item through a launch-state dry-run. A formula prevents an incomplete row from "
            "entering review, while a zero-LIVE check proves nothing was published during class."
        ),
        build=(
            "04-launch/08-content-calendar.xlsx and 04-launch/08-launch-checklist.md with eight versioned "
            "draft items, readiness flags, approval ownership, observation windows, and rollback steps."
        ),
        services="Spreadsheet application, Labs 5-7 artifacts, document editor",
        steps=[
            (
                "Create 04-launch/08-content-calendar.xlsx. In row 1 add columns Item ID, Date, Time SGT, Platform, Segment, Asset Version, Copy Version, CTA URL, Claim IDs, Owner, Status, Readiness, Experiment Arm, First Check, and Rollback Version.",
                "",
            ),
            (
                "Add eight items dated across a Monday-Sunday week: two Instagram, two Facebook, two LinkedIn, and two X. Use item IDs CAL-01 through CAL-08 and times in Asia/Singapore.",
                "",
            ),
            (
                "For each row, reference the exact Lab 5 copy section and Lab 6 asset or storyboard version. Use https://example.com/hydraloop as the classroom-only CTA URL and copy the required Claim IDs from the ledger.",
                "",
            ),
            (
                "Set every Status cell in K2:K9 to DRAFT. In L2 enter the readiness formula below and fill it down. The row may enter REVIEW only when all required fields are present and Status is DRAFT or REVIEW.",
                "=IF(OR(COUNTA(A2:J2)<10,N2=\"\",O2=\"\",AND(OR(A2=\"CAL-01\",A2=\"CAL-02\"),M2=\"\")),\"INCOMPLETE\",IF(OR(K2=\"DRAFT\",K2=\"REVIEW\"),\"READY FOR REVIEW\",\"CHECK STATE\"))",
            ),
            (
                "Assign CAL-01 and CAL-02 to EXP-01 Control and Treatment. Keep their platform, segment, date window, offer, CTA, and creative style aligned; only the planned hook differs.",
                "",
            ),
            (
                "Set First Check to two hours after the scheduled time for routine delivery checks and next-business-day for the first performance note. Set Rollback Version to the last approved copy and asset version, not a blank value.",
                "",
            ),
            (
                "Create 04-launch/08-launch-checklist.md with sections Tracking, Creative and Copy, Claims and Rights, Audience and Placement, Budget and Pacing, Schedule and Timezone, Response Owner, Approval Record, First Observation, Pause Conditions, and Rollback.",
                "",
            ),
            (
                "Run a tabletop dry-run for CAL-01. Move its spreadsheet Status from DRAFT to REVIEW only. In the checklist record the item ID, versions, reviewer, unresolved leak-demonstration evidence, and decision HOLD IN REVIEW until the product owner confirms the demonstration protocol.",
                "",
            ),
            (
                "Add a control cell labelled LIVE Count with formula =COUNTIF(K2:K9,\"LIVE\"). Confirm the result is 0. Save the workbook and checklist without opening any social scheduling or advertising account.",
                "=COUNTIF(K2:K9,\"LIVE\")",
            ),
        ],
        test=(
            "The calendar has eight unique item IDs, complete dates/times/platforms/versions/owners, two "
            "aligned experiment arms, and no blank rollback version. CAL-01 is REVIEW with a documented "
            "hold reason; all other rows are DRAFT. LIVE Count equals 0 and the checklist covers all eleven sections."
        ),
        troubleshooting=[
            ("Readiness says INCOMPLETE", "Filter column L, fill the missing field in A:J from the approved artifacts, and do not bypass the formula."),
            ("The experiment rows differ in more than the hook", "Copy the control row, create a new item ID, and edit only the hook-specific copy version."),
            ("A platform opens a live composer", "Close it without saving, return to the spreadsheet dry-run, and keep the class workflow account-free."),
        ],
        challenge="Add a dependency column that prevents a Treatment item moving to REVIEW until the matching Control item and experiment card share the same experiment version.",
        reflection="Which launch check is easiest to automate reliably, and which still requires contextual human judgement?",
        checkpoint="A zero-LIVE content calendar and complete controlled-launch checklist ready for synthetic performance monitoring.",
        deck_steps=[
            "Create eight versioned calendar items with owners, evidence, and rollback versions.",
            "Apply a readiness formula and align control/treatment rows.",
            "Dry-run one review transition and verify LIVE Count remains zero.",
        ],
    ),
]
