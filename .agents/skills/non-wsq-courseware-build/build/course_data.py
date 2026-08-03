"""Single source of truth for C1798 courseware."""

# ------------------------------------------------------------------ metadata
TITLE = "Agentic AI for Digital Marketing and Advertising (C1798)"
SHORT_TITLE = "Agentic AI for Digital Marketing and Advertising (C1798)"
COURSE_CODE = "C1798"
VERSION = "v1.0"
VERSION_DATE = "3 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Courseware Team"
DAYS = 2
MODE = "Instructor-led, concept-first workshops and connected hands-on labs"

# The advertised duration is 15 hours over two days. Each day runs 9:30-17:30
# with a 30-minute lunch; tea breaks are included in the scheduled 450 minutes.
DAY_MINUTES = 450
DAILY_TIMING = "9:30 am - 5:30 pm (30-minute lunch; tea breaks within scheduled time)"
DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain agentic marketing architecture and define goals, tools, memory, approval gates, and operational guardrails for a marketing agent.",
    "LO2: Build a repeatable trend-discovery workflow that evaluates freshness, evidence, brand fit, and risk before recommending an opportunity.",
    "LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights.",
    "LO4: Design an AI-assisted campaign blueprint, experiment plan, content calendar, and controlled launch workflow tied to objectives and KPIs.",
    "LO5: Calculate and interpret social performance metrics, analyse synthetic audience feedback, and turn findings into evidence-linked recommendations.",
    "LO6: Diagnose paid-media performance, propose bounded experiments, and design a human-governed optimization loop with stop conditions and audit evidence.",
]
LO_TITLES = [
    "Agent Architecture",
    "Trend Intelligence",
    "Content Automation",
    "Campaign Orchestration",
    "Performance Learning",
    "Optimization Control",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(
        num=1,
        code="01",
        title="Foundations of Agentic AI for Marketing",
        subtitle="Agents and workflows | goal design | tools and memory | approval gates | brand, privacy, and advertising guardrails",
        concepts=[
            "An agent combines a goal, state, reasoning, tools, and feedback; a fixed workflow follows a predefined path.",
            "A marketing pipeline should make each hand-off explicit: inputs, decision rule, output schema, owner, and failure route.",
            "Autonomy is not all-or-nothing. Read, draft, recommend, approve, publish, and spend actions carry different risk.",
            "Memory must be scoped: campaign facts and approved preferences belong in state; sensitive or unverified data does not.",
            "Tool permissions should follow least privilege, with credentials stored in a secure connection rather than a prompt or repository.",
            "A useful guardrail is observable: it defines what is blocked, when review is required, and what evidence is logged.",
        ],
        overview=[
            "Agentic marketing is the deliberate use of AI systems that can observe signals, choose among permitted actions, use tools, and revise a plan toward a stated goal. It differs from ordinary content generation because the system maintains state across steps and can decide what to do next. That flexibility is valuable only when the business goal, available evidence, and action boundary are explicit.",
            "The safest design starts with bounded autonomy. An agent may read public trend data, draft a campaign brief, or recommend a budget change, while publication and spend changes remain human-owned. This separation keeps speed where errors are recoverable and human judgement where claims, privacy, reputation, or money are at stake.",
        ],
        knowledge_sections=[
            dict(
                title="The Agentic Marketing Control Loop",
                kicker="ARCHITECTURE",
                body=[
                    "A reliable agent moves through five observable states: Goal, Sense, Reason, Act, and Learn. Goal defines the outcome and constraints. Sense collects permitted signals. Reason compares options against rules. Act produces only an allowed output. Learn records the result so the next cycle starts with better evidence.",
                    "Approval gates sit between reasoning and high-impact actions. They are not delays added after the design; they are part of the control loop. The agent should also have a stop path for missing data, conflicting instructions, or a threshold breach.",
                ],
                visual=[
                    ("Goal", "Objective, audience, KPI, timebox, and constraints"),
                    ("Sense", "Approved sources, freshness, provenance, and data quality"),
                    ("Reason", "Decision rules, alternatives, confidence, and risk"),
                    ("Act", "Draft, recommend, schedule, or execute within permission"),
                    ("Learn", "Outcome, exception, feedback, and next-cycle state"),
                    ("Gate", "Named owner approves publish, spend, claims, or personal-data use"),
                ],
            ),
            dict(
                title="Workflow or Agent? Choose by Uncertainty",
                kicker="DESIGN CHOICE",
                body=[
                    "Use a fixed workflow when the path is predictable and the cost of variation is high. Examples include formatting a weekly report or moving approved copy into a calendar. Use agentic reasoning when inputs vary and the system must compare several valid routes, such as ranking trend signals with incomplete evidence.",
                    "Many production systems are hybrids: deterministic collection and calculation feed an agent that explains patterns, then a deterministic approval and logging step controls the outcome. The design should be no more autonomous than the task requires.",
                ],
                visual=[
                    ("Fixed workflow", "Known steps, stable inputs, repeatable output"),
                    ("Router", "Chooses one approved path from explicit categories"),
                    ("Evaluator loop", "Generates, checks, and revises against a rubric"),
                    ("Agent", "Plans among tools when the path cannot be fixed in advance"),
                ],
            ),
            dict(
                title="Guardrails as Testable Controls",
                kicker="RESPONSIBLE OPERATION",
                body=[
                    "A policy statement such as 'be accurate' is too vague to operate. A control translates policy into a condition and response: unsupported product claims are blocked, synthetic audience data is required in training, and a named owner must approve any public or paid action.",
                    "Controls need evidence. Log the input source, decision, output version, approver, timestamp, and reason. This record supports troubleshooting and makes it possible to decide whether the system should continue, pause, or be changed.",
                ],
                visual=[
                    ("Claim check", "Block any claim without a source and owner"),
                    ("Privacy check", "Reject identifiable customer data in prompts"),
                    ("Brand check", "Compare tone, exclusions, and visual direction"),
                    ("Action check", "Require approval for publish, spend, or targeting changes"),
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Automated Trend Discovery and Viral Content Research",
        subtitle="signal collection | source provenance | normalized trend data | opportunity scoring | hooks and emotional triggers | scheduled briefs",
        concepts=[
            "A trend signal is an observation with a source, market, timestamp, topic, and evidence; a trend is not merely a popular-looking post.",
            "Google Trends reports relative, normalized search interest rather than absolute search volume, so comparisons need matched regions and time windows.",
            "Triangulation reduces false positives by comparing search, community, editorial, and first-party signals instead of trusting one source.",
            "Viral mechanics include a clear hook, useful tension, social currency, emotional relevance, and a low-friction action, but none guarantees performance.",
            "Opportunity scoring should separate upside from risk so a high-volume but unsafe idea cannot win by arithmetic alone.",
            "A scheduled trend brief needs freshness limits, deduplication, citations, exception handling, and an explicit review queue.",
        ],
        overview=[
            "Trend discovery is a sensing problem before it is a content problem. The pipeline must capture where a signal came from, when it appeared, which market it represents, and whether the signal can be verified. Without provenance and a time window, the agent cannot distinguish a current opportunity from recycled noise.",
            "The goal is not to chase every spike. A marketing team needs opportunities that connect audience tension to a genuine product truth. A disciplined score combines freshness, evidence, brand fit, and likely usefulness, while a separate risk score can veto an idea that depends on rumour, harmful framing, or unsupported claims.",
        ],
        knowledge_sections=[
            dict(
                title="From Raw Signals to a Trend Brief",
                kicker="PIPELINE",
                body=[
                    "Collection gathers candidate signals from approved public or first-party sources. Normalization gives every record the same fields. Enrichment adds related queries, audience tension, hook, and evidence notes. Ranking compares opportunities. Review confirms that the recommendation is timely, truthful, and useful.",
                    "Each transformation should preserve the source URL and observation time. If an agent cannot cite the supporting record, the item should remain in a research queue rather than move to content production.",
                ],
                visual=[
                    ("Collect", "Search, community, editorial, and owned signals"),
                    ("Normalize", "Source, time, market, topic, URL, and observed value"),
                    ("Enrich", "Audience tension, hook, related terms, and evidence"),
                    ("Rank", "Freshness + evidence + brand fit, with a risk veto"),
                    ("Review", "Human confirms relevance, rights, and claim safety"),
                    ("Brief", "One opportunity, why now, proof, angle, and next step"),
                ],
            ),
            dict(
                title="Read Relative Trend Data Correctly",
                kicker="DATA LITERACY",
                body=[
                    "A Google Trends score of 100 is the peak relative interest for the selected comparison, geography, and time range. It is not the number of searches. Changing the window or location changes the denominator, so screenshots from different settings should not be compared as if they shared a scale.",
                    "A spike is a prompt to investigate, not proof of demand or positive sentiment. Compare a candidate with a baseline, inspect related queries, confirm the timing in another source, and document uncertainty before recommending action.",
                ],
                visual=[
                    ("100", "Peak share within the selected comparison"),
                    ("50", "Half the relative interest of that peak, not half the searches"),
                    ("0", "Insufficient data or very low relative interest, not necessarily none"),
                    ("Breakout", "Very rapid growth that still needs context and evidence"),
                ],
            ),
            dict(
                title="Opportunity Score with a Risk Veto",
                kicker="WORKED EXAMPLE",
                body=[
                    "For classroom use, score brand fit, freshness, and evidence from 1 to 5. The opportunity score is their average multiplied by 20, producing a 0-100 scale. Keep risk separate. A risk score of 4 or 5 sends the signal to review regardless of the opportunity score.",
                    "Example: a leak-prevention conversation scores 5 for fit, 4 for freshness, and 3 for evidence. Its opportunity score is 80. With risk 2, it can move to a brief. A celebrity rumour can score high for freshness but risk 5, so the correct action is hold, verify, or reject.",
                ],
                visual=[
                    ("Opportunity", "((Fit + Freshness + Evidence) / 15) x 100"),
                    ("Proceed", "Score >= 70 and risk <= 2"),
                    ("Research", "Score 50-69 or evidence below 3"),
                    ("Hold", "Risk >= 4, missing source, or unsupported claim"),
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="AI Content Creation and Multimedia Automation",
        subtitle="message hierarchy | platform adaptation | brand-voice prompting | image generation | short-form video | scheduling and publish gates",
        concepts=[
            "A message hierarchy keeps one campaign promise intact while allowing the hook, proof, format, and call to action to change by platform.",
            "Platform adaptation is not copy-and-paste resizing; audience intent, reading behavior, and native format change the expression of the idea.",
            "A reusable prompt separates immutable brand facts from variable audience, channel, format, and experiment fields.",
            "Image prompts need subject, setting, composition, lighting, palette, exclusions, and output format; generated text inside images still needs checking.",
            "A short-form video pipeline connects hook, scene, on-screen text, voiceover, caption, safe-zone, and rights checks.",
            "Automation should create and route drafts; publishing stays gated until claims, brand fit, accessibility, and platform readiness are verified.",
        ],
        overview=[
            "Content automation works when the team creates one approved message system before producing channel variants. The core promise, evidence, offer, and prohibited claims should stay fixed. The agent may adapt structure and tone for a platform, but it should never invent a new product fact to make the copy more persuasive.",
            "Multimedia generation adds visual and rights risks. A strong prompt specifies the product and composition, while a review checklist checks representation, logos, text accuracy, accessibility, and whether the team owns or may use every input. The output remains a draft asset until that review is complete.",
        ],
        knowledge_sections=[
            dict(
                title="One Message, Four Platform Expressions",
                kicker="CONTENT SYSTEM",
                body=[
                    "The campaign promise should remain recognisable across Facebook, Instagram, LinkedIn, and X. What changes is the opening, depth, visual rhythm, and call to action. Instagram may lead with a visual payoff, LinkedIn with a workplace use case, Facebook with context and conversation, and X with one sharp observation.",
                    "The agent should output a structured content object rather than an unlabelled paragraph. Fields such as platform, audience, hook, proof, caption, CTA, accessibility note, and claim source make review and scheduling safer.",
                ],
                visual=[
                    ("Instagram", "Visual-first hook, concise caption, save/share value"),
                    ("Facebook", "Context, practical benefit, and conversation prompt"),
                    ("LinkedIn", "Professional problem, evidence, and operational takeaway"),
                    ("X", "One idea, timely framing, and a direct link or reply prompt"),
                ],
            ),
            dict(
                title="Brand Prompt Anatomy",
                kicker="PROMPT ENGINEERING",
                body=[
                    "A robust content prompt has five layers: verified facts, audience and job-to-be-done, brand voice, output schema, and review constraints. Keeping these layers visible makes the prompt easier to update and audit than a long paragraph of mixed instructions.",
                    "Ask the model to flag missing evidence instead of filling gaps. Require a claim ledger that lists each factual statement and its source. This turns hallucination checking into a normal production step rather than an afterthought.",
                ],
                visual=[
                    ("Facts", "Only approved product, offer, and timing details"),
                    ("Audience", "Segment, situation, tension, and desired action"),
                    ("Voice", "Tone, sentence style, vocabulary, and exclusions"),
                    ("Schema", "Named fields for each platform and asset"),
                    ("Checks", "Claims, accessibility, rights, and approval status"),
                    ("Uncertainty", "Write NEEDS EVIDENCE instead of inventing support"),
                ],
            ),
            dict(
                title="Multimedia Production with Review Gates",
                kicker="IMAGE AND VIDEO",
                body=[
                    "An image-generation request should describe the subject, setting, composition, lighting, colour palette, camera view, and exclusions. For product work, use a real approved product reference only when rights and platform terms permit it; otherwise create a clearly labelled concept image.",
                    "A short video can be planned as six connected fields per scene: time, visual, action, voiceover, on-screen text, and sound. Before scheduling, check visual continuity, text accuracy, captions, safe zones, rights, and whether any synthetic media disclosure is required by policy or platform.",
                ],
                visual=[
                    ("Generate", "Prompt or storyboard from approved facts"),
                    ("Inspect", "Product fidelity, people, text, and artefacts"),
                    ("Adapt", "Aspect ratio, safe zone, caption, and alt text"),
                    ("Approve", "Rights, claims, brand, accessibility, and disclosure"),
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Creating and Launching AI-Driven Marketing Campaigns",
        subtitle="objectives and segments | KPI trees | message and creative matrices | experiment design | content calendars | controlled launch",
        concepts=[
            "A campaign objective describes the business outcome; a platform objective is a delivery setting chosen to support it.",
            "A KPI tree connects business outcome, conversion event, leading indicator, and diagnostic metric so optimization has a hierarchy.",
            "Audience segments should express a need and context, not merely demographic labels or inferred sensitive traits.",
            "A message matrix links segment, tension, promise, evidence, objection, and call to action before variations are generated.",
            "A useful experiment changes one main variable, defines a control, and states a decision rule before results arrive.",
            "A launch workflow validates tracking, creative, links, naming, budgets, approvals, and rollback steps before anything becomes active.",
        ],
        overview=[
            "Campaign orchestration turns disconnected assets into a system with a business outcome, audience logic, measurement plan, owner, and calendar. The agent can accelerate planning by generating alternatives, finding missing fields, and formatting work for different channels, but the campaign team must decide the objective and the evidence that will count as success.",
            "Launch is a state transition, not a button. Draft assets move through review, approval, scheduling, and observation. Each transition requires evidence: final URLs work, events are visible, creative matches the approved version, limits are set, and a rollback owner knows what to do if the launch behaves unexpectedly.",
        ],
        knowledge_sections=[
            dict(
                title="Build a KPI Tree Before Creating Assets",
                kicker="MEASUREMENT DESIGN",
                body=[
                    "Start from the business outcome, then work backward. For a product launch, revenue or purchases may be the outcome. Purchase events are the conversion signal. Landing-page conversion rate and cost per purchase are leading decision metrics. CTR, CPC, reach, and engagement help diagnose why the result moved.",
                    "This hierarchy prevents the agent from treating every metric as equally important. A high-engagement post may be useful, but it does not automatically prove profitable acquisition. The campaign brief should name the primary decision metric and the guardrails that must not deteriorate.",
                ],
                visual=[
                    ("Outcome", "Purchases, qualified leads, revenue, or retained value"),
                    ("Conversion", "The verified event tied to the outcome"),
                    ("Decision KPI", "CPA, ROAS, conversion rate, or qualified-lead rate"),
                    ("Diagnostics", "Reach, CTR, CPC, frequency, engagement, and sentiment"),
                    ("Guardrails", "Spend cap, complaint signal, tracking quality, brand safety"),
                ],
            ),
            dict(
                title="Campaign Message and Creative Matrix",
                kicker="ORCHESTRATION",
                body=[
                    "A matrix makes variation deliberate. Each row represents a segment and situation; columns hold the audience tension, promise, evidence, objection response, format, and call to action. The agent generates inside those cells rather than improvising a new strategy for every post.",
                    "The matrix also exposes missing evidence. If a promise has no support, the content should be rewritten as a demonstration, question, or invitation rather than a factual claim. This keeps creativity tied to what the business can honestly show.",
                ],
                visual=[
                    ("Segment", "Who, in which situation, with what need"),
                    ("Tension", "The friction or unanswered question"),
                    ("Promise", "What the verified product truth can help with"),
                    ("Proof", "Demo, specification, source, or customer evidence"),
                    ("Format", "Post, carousel, short video, search ad, or landing block"),
                    ("CTA", "One observable next action"),
                ],
            ),
            dict(
                title="The Controlled Launch State Machine",
                kicker="LAUNCH OPERATIONS",
                body=[
                    "A simple state model prevents accidental publication: DRAFT, REVIEW, APPROVED, SCHEDULED, LIVE, PAUSED, and RETIRED. Only named roles may change a state, and the change should capture who, when, why, and which version moved.",
                    "Before LIVE, verify links, tracking, creative, copy, targeting boundaries, budget limits, date and timezone, and response ownership. A launch plan also defines the first observation window and the condition that will pause delivery.",
                ],
                visual=[
                    ("DRAFT", "Generated or edited; never public"),
                    ("REVIEW", "Claims, brand, rights, tracking, and accessibility checked"),
                    ("APPROVED", "Named owner authorizes this exact version"),
                    ("SCHEDULED", "Platform, date, timezone, link, and limits confirmed"),
                    ("LIVE", "Observe against early-warning thresholds"),
                    ("PAUSED", "Stop condition triggered; preserve evidence and investigate"),
                ],
            ),
        ],
    ),
    dict(
        num=5,
        code="05",
        title="Agentic AI for Social Media Performance Monitoring",
        subtitle="analytics connectors | metric definitions | dashboards | sentiment and themes | pattern detection | evidence-linked feedback",
        concepts=[
            "A connector should preserve metric name, platform, date window, timezone, object level, and retrieval time so comparisons are interpretable.",
            "Reach counts unique exposure while impressions count displays; clicks and engagements need a declared denominator before a rate is compared.",
            "CTR, engagement rate, conversion rate, and cost metrics answer different questions and should not be collapsed into one success score without rationale.",
            "Sentiment labels are useful only with themes, representative examples, uncertainty, and a human review path for ambiguous or high-risk feedback.",
            "Pattern detection compares like with like: platform, audience, format, objective, and time window should be controlled before a winner is named.",
            "The feedback loop should pass evidence and a bounded recommendation to content generation, not merely 'make it better.'",
        ],
        overview=[
            "Monitoring begins with a measurement contract: the metric, formula, platform field, level of aggregation, time window, timezone, and decision it supports. Without that contract, two tools can display similarly named numbers that should not be compared. The agent must retain these definitions alongside the values it analyses.",
            "Performance learning combines quantitative and qualitative evidence. Metrics show what happened; comments and support signals help explain why. The output should distinguish observation from interpretation and recommendation, cite the relevant rows or comments, and state what additional evidence would change the recommendation.",
        ],
        knowledge_sections=[
            dict(
                title="The Marketing Metric Ladder",
                kicker="MEASUREMENT",
                body=[
                    "Delivery metrics such as reach and impressions show exposure. Attention metrics such as video views and clicks show response. Action metrics such as landing visits and purchases show progression. Efficiency metrics such as CPC, CPA, and ROAS connect those outcomes to cost.",
                    "Always write the formula and denominator. CTR is clicks divided by impressions. Conversion rate must state whether it uses clicks, sessions, or another base. ROAS is attributed conversion value divided by ad spend and depends on the chosen attribution rules.",
                ],
                visual=[
                    ("Delivery", "Reach, impressions, frequency"),
                    ("Attention", "Views, clicks, engaged sessions"),
                    ("Action", "Key events, leads, purchases"),
                    ("Efficiency", "CPC, CPA, revenue per cost, ROAS"),
                    ("Quality", "Tracking status, complaints, brand safety, data gaps"),
                ],
            ),
            dict(
                title="Observation, Interpretation, Recommendation",
                kicker="ANALYTICAL DISCIPLINE",
                body=[
                    "An observation is directly supported by data: Post P10 had the highest clicks in the sample. An interpretation proposes a reason: the launch offer and product image may have increased action. A recommendation proposes a bounded next step: reuse the offer structure in a controlled variation while keeping the audience and placement stable.",
                    "Agents often overstate interpretation as fact. Requiring these three labelled fields, an evidence reference, and a confidence note makes the reasoning reviewable and easier to challenge.",
                ],
                visual=[
                    ("Observe", "State the metric or comment pattern and cite the rows"),
                    ("Interpret", "Offer a plausible explanation and alternatives"),
                    ("Recommend", "Specify one reversible next action"),
                    ("Verify", "Name the KPI, window, and result that would support the idea"),
                ],
            ),
            dict(
                title="Sentiment with Themes and Escalation",
                kicker="QUALITATIVE SIGNALS",
                body=[
                    "Positive, neutral, and negative labels alone are too shallow for action. Add a theme such as price, leak concern, colour request, claim trust, or cleaning question. Preserve a short comment excerpt or ID so a reviewer can see the evidence.",
                    "Route legal, safety, privacy, discrimination, crisis, or unsupported-claim concerns to a human owner. Do not let an automated reply invent policy or product facts. The useful output is a queue with severity, theme, suggested owner, and a draft response clearly marked for review.",
                ],
                visual=[
                    ("Label", "Positive, neutral, negative, or mixed"),
                    ("Theme", "What the audience is actually discussing"),
                    ("Evidence", "Comment ID and representative wording"),
                    ("Severity", "Routine, investigate, or urgent escalation"),
                    ("Action", "Respond, clarify, update content, or pause a claim"),
                ],
            ),
        ],
    ),
    dict(
        num=6,
        code="06",
        title="Agentic AI for Advertising Optimization and Scaling",
        subtitle="paid-media metrics | anomaly detection | diagnosis trees | A/B experiments | budget and targeting controls | autonomous-loop design",
        concepts=[
            "An anomaly is a meaningful deviation from an expected range; it is a signal to diagnose, not permission to change a budget.",
            "Paid-media diagnosis should check tracking, delivery, audience, creative, landing experience, and conversion lag before choosing a remedy.",
            "CPA equals spend divided by conversions; ROAS equals attributed conversion value divided by spend, and both inherit attribution limitations.",
            "A/B testing requires a control, one main change, comparable traffic, a predeclared KPI, an observation window, and a decision rule.",
            "Scaling should be bounded by spend caps, pacing rules, minimum evidence, reversibility, cooldown periods, and human approval thresholds.",
            "A mature optimization loop logs the data snapshot, hypothesis, proposed action, approver, execution result, and rollback state.",
        ],
        overview=[
            "Optimization is decision-making under uncertainty. A falling ROAS may reflect weaker creative, higher auction cost, a landing-page problem, conversion delay, or broken tracking. An agent should diagnose across these branches and present evidence before proposing an action. Direct budget changes from a single noisy metric create a fast path to expensive mistakes.",
            "The safest autonomous loop is layered. Collection and calculations may run automatically. Diagnosis and experiment drafting may be agent-assisted. Budget, targeting, bid, and live creative changes are bounded by approval gates, caps, cooldowns, and rollback rules. Scaling means repeating a validated pattern within those controls, not removing them.",
        ],
        knowledge_sections=[
            dict(
                title="Diagnose Before You Optimize",
                kicker="DECISION TREE",
                body=[
                    "Start with tracking quality because every downstream metric depends on it. Then inspect delivery and auction signals, audience saturation, creative response, landing conversion, and conversion lag. Compare the changed segment with a stable reference instead of reacting to the total account number.",
                    "A good diagnosis memo names the symptom, evidence, competing explanations, missing data, and safest next test. If tracking is partial, the correct recommendation is usually to hold major changes and repair measurement first.",
                ],
                visual=[
                    ("Tracking", "Event loss, tag changes, delayed imports, partial status"),
                    ("Delivery", "Spend, impressions, CPM, pacing, approval status"),
                    ("Audience", "Frequency, overlap, saturation, exclusions"),
                    ("Creative", "CTR, view rate, comments, fatigue, message mismatch"),
                    ("Landing", "Speed, message match, conversion rate, checkout errors"),
                    ("Lag", "Attribution window and delayed conversions"),
                ],
            ),
            dict(
                title="Design a Decision-Ready Experiment",
                kicker="A/B TESTING",
                body=[
                    "An experiment starts with a causal question, not two random variations. Keep the audience, placement, timing, and offer stable while changing one primary creative or bidding variable. Define the control, treatment, primary KPI, guardrails, minimum runtime, and decision rule before launch.",
                    "Early differences can be noise. Use the platform's experiment workflow when available, keep control and treatment metrics separate, and avoid declaring a winner from a few conversions. The action after the test may be promote, continue, stop, or redesign.",
                ],
                visual=[
                    ("Hypothesis", "Because insight X, changing Y should improve KPI Z"),
                    ("Control", "Current approved version"),
                    ("Treatment", "One primary change"),
                    ("Guardrails", "Spend, complaints, tracking, and secondary KPI limits"),
                    ("Window", "Predeclared runtime and conversion-lag allowance"),
                    ("Decision", "Promote, continue, stop, or redesign"),
                ],
            ),
            dict(
                title="Bounded Optimization Loop",
                kicker="SCALING WITH CONTROL",
                body=[
                    "The loop collects a versioned snapshot, validates data quality, detects a threshold breach, drafts a diagnosis, proposes one reversible action, and waits for approval when the action affects spend, targeting, or public creative. After execution it observes a cooldown window and compares the result with the rollback condition.",
                    "Every cycle should be idempotent: rerunning the same input should not apply the same change twice. Store an action ID and current state, enforce daily and weekly caps, and route repeated failures or conflicting evidence to a human owner.",
                ],
                visual=[
                    ("Observe", "Versioned metrics plus quality status"),
                    ("Validate", "Freshness, completeness, and denominator checks"),
                    ("Diagnose", "Evidence tree and competing explanations"),
                    ("Propose", "One bounded, reversible change"),
                    ("Approve", "Required for spend, targeting, bid, or public creative"),
                    ("Learn", "Cooldown, result, rollback, and audit record"),
                ],
            ),
        ],
    ),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Agent Foundations, Trend Intelligence, and Content Automation",
    2: "Campaign Orchestration, Performance Learning, and Controlled Optimization",
}


# ------------------------------------------------------------------ schedule
def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:30", "9:50", 20, "admin", "Welcome, course orientation, learning outcomes, and the Aurora Active scenario"),
            ("9:50", "10:40", 50, "topic", "Topic 1 - " + TOPICS[0]["title"] + " (concepts, architecture, and worked example)"),
            ("10:40", "10:55", 15, "break", "Tea break"),
            ("10:55", "12:15", 80, "lab", "Hands-on: " + lab_titles([1, 2])),
            ("12:15", "13:00", 45, "topic", "Topic 2 - " + TOPICS[1]["title"] + " (concepts, data interpretation, and worked example)"),
            ("13:00", "13:30", 30, "lunch", "Lunch break"),
            ("13:30", "14:50", 80, "lab", "Hands-on: " + lab_titles([3, 4])),
            ("14:50", "15:35", 45, "topic", "Topic 3 - " + TOPICS[2]["title"] + " (concepts, message system, and multimedia review)"),
            ("15:35", "15:50", 15, "break", "Tea break"),
            ("15:50", "17:15", 85, "lab", "Hands-on: " + lab_titles([5, 6])),
            ("17:15", "17:30", 15, "recap", "Day 1 recap, campaign checkpoint, and questions"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:30", "9:45", 15, "admin", "Day 1 recap and Day 2 campaign-state check"),
            ("9:45", "10:30", 45, "topic", "Topic 4 - " + TOPICS[3]["title"] + " (concepts, KPI tree, and launch states)"),
            ("10:30", "10:45", 15, "break", "Tea break"),
            ("10:45", "12:05", 80, "lab", "Hands-on: " + lab_titles([7, 8])),
            ("12:05", "12:50", 45, "topic", "Topic 5 - " + TOPICS[4]["title"] + " (concepts, metrics, and evidence-linked interpretation)"),
            ("12:50", "13:20", 30, "lunch", "Lunch break"),
            ("13:20", "14:40", 80, "lab", "Hands-on: " + lab_titles([9, 10])),
            ("14:40", "15:25", 45, "topic", "Topic 6 - " + TOPICS[5]["title"] + " (concepts, diagnosis, experiments, and control loop)"),
            ("15:25", "15:40", 15, "break", "Tea break"),
            ("15:40", "17:10", 90, "lab", "Hands-on: " + lab_titles([11, 12])),
            ("17:10", "17:30", 20, "recap", "Course recap, optimization-loop review, action planning, and questions"),
        ]),
    }


# ------------------------------------------------------------------ deck and guide framing
COURSE_OVERVIEW = dict(
    section_title="Agentic Marketing Fundamentals",
    concepts_title="Six Ideas That Anchor the Course",
    concepts=[
        ("Agent", "A goal-directed system that can choose among permitted actions and tools."),
        ("Workflow", "A defined path for reliable, repeatable transformations and checks."),
        ("State", "The versioned campaign facts, decisions, and results carried across steps."),
        ("Tool", "A bounded capability to read, calculate, draft, schedule, or act."),
        ("Guardrail", "A testable rule that blocks, routes, limits, or records an action."),
        ("Feedback", "Evidence used to update the next decision rather than repeat the same plan."),
    ],
    framework_title="The GSRAL Control Loop",
    framework=[
        ("Goal", "Define business outcome, audience, KPI, constraints, and owner."),
        ("Sense", "Collect approved signals with source, time, market, and quality."),
        ("Reason", "Compare options against evidence, rules, risk, and uncertainty."),
        ("Act", "Draft or execute only the action permitted for the current state."),
        ("Learn", "Record result, exception, feedback, and the next-cycle state."),
        ("Approval gate", "Human authorization before public, personal-data, targeting, or spend actions."),
    ],
    statement=dict(
        headline="Autonomy is a permission design, not a personality trait.",
        body="Give the system freedom where errors are cheap and reversible; require human judgement where claims, privacy, reputation, or money are at stake.",
        kicker="CORE IDEA",
    ),
    pillars_title="The Connected Campaign You Will Build",
    pillars=[
        ("Intelligence", ["Agent canvas and guardrails", "Trend signal table", "Ranked opportunity brief"]),
        ("Creative", ["Platform content kit", "Image concept", "Short-video storyboard"]),
        ("Launch", ["Campaign and KPI blueprint", "Experiment map", "Controlled content calendar"]),
        ("Learning", ["Performance dashboard", "Feedback themes", "Optimization runbook"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from the current Aurora Active campaign checkpoint.",
        "Apply the topic model to a bounded marketing task.",
        "Create a versioned artifact with sources and assumptions.",
        "Verify the artifact against an observable checklist or formula.",
        "Carry the approved checkpoint into the next lab.",
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies Agentic AI for Digital Marketing and Advertising (C1798), "
    "a two-day, 15-hour course for marketers, campaign managers, content specialists, analysts, "
    "business owners, and marketing-technology practitioners. It teaches how to design agentic "
    "marketing systems that are useful, measurable, and controlled rather than treating an AI "
    "assistant as an unsupervised publisher or budget manager."
)
LG_INTRO2 = (
    "All twelve labs use one fictional Singapore campaign: Aurora Active's HydraLoop launch. "
    "The campaign grows from an agent canvas and trend brief into a content kit, launch plan, "
    "performance dashboard, and optimization runbook. Synthetic data keeps the exercises safe "
    "and repeatable. Every public or paid action remains in draft, and every recommendation must "
    "carry evidence, a named owner, and a clear next check."
)

LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a current Chrome, Edge, or Safari browser.",
        "A spreadsheet application: Microsoft Excel, Google Sheets, or LibreOffice Calc.",
        "Access to a general-purpose AI assistant approved for classroom use. A free account is sufficient for text labs.",
        "Optional access to Gemini image generation or Canva for the visual concept in Lab 6; a storyboard-only route is always available.",
        "The files in labs/resources/: the Aurora brief, trend signals, social performance, comments, and paid-media performance.",
        "No social-platform developer account, ad account, API key, customer list, or payment method is needed.",
    ],
    verify_text=(
        "Before class, open the Aurora brand brief and each CSV in your spreadsheet tool. Confirm "
        "headers and rows appear in separate columns. Create a local folder named aurora-campaign "
        "with subfolders 01-foundation, 02-trends, 03-content, 04-launch, 05-monitor, and 06-optimize."
    ),
    verify_code="aurora-campaign/\n  01-foundation/\n  02-trends/\n  03-content/\n  04-launch/\n  05-monitor/\n  06-optimize/",
    conventions=[
        "Replace placeholders in angle brackets, such as <AUDIENCE>, before sending a prompt.",
        "Save each artifact with the exact filename shown so the next lab can find it.",
        "Keep public posts, schedules, campaigns, and budget actions in DRAFT throughout class.",
        "Use only the synthetic records supplied in labs/resources/; do not paste customer data or credentials into an AI chat.",
        "Label AI output as a draft, retain the evidence source, and record any fact that still needs confirmation.",
    ],
)

LAB_NOTE = (
    "Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out "
    "of prompts and files. Do not publish a post, activate a campaign, change targeting, or change "
    "spend during class; prepare a reviewable draft and route high-impact actions to the named owner."
)

LG_WRAPUP = dict(
    title="Wrap-Up - From Fast Drafts to a Controlled Learning System",
    intro=(
        "You have built the complete control path for an agentic marketing campaign: purpose and "
        "permissions, trend evidence, content variants, launch states, monitoring, diagnosis, and "
        "bounded optimization. The durable skill is not a particular tool interface. It is the "
        "ability to define what the system may observe, decide, produce, and escalate."
    ),
    sections=[
        dict(title="What You Can Now Do", bullets=[
            "Choose between a fixed workflow, router, evaluator loop, and agent based on uncertainty and risk.",
            "Rank trend signals with provenance, freshness, evidence, brand fit, and a separate risk veto.",
            "Generate channel variants and multimedia concepts from one verified message system.",
            "Connect campaign objectives to KPIs, experiments, calendars, approval states, and rollback steps.",
            "Calculate performance metrics and separate observation, interpretation, and recommendation.",
            "Design an optimization loop that validates data, proposes one reversible action, and logs the result.",
        ]),
        dict(title="Operating Habits Worth Keeping", bullets=[
            "Version the brief, prompt, data snapshot, and output that produced each decision.",
            "Treat missing evidence as a routing condition, not an invitation to invent a fact.",
            "Keep metric definitions and denominators beside the values.",
            "Use approval gates for public claims, customer data, targeting, spend, and live creative.",
            "Prefer small reversible experiments over broad simultaneous changes.",
        ]),
        dict(title="When the System Should Stop", bullets=[
            "A required source is missing, stale, or contradictory.",
            "Tracking is partial or a metric definition changed.",
            "A proposed claim lacks evidence or creates legal, safety, or reputation risk.",
            "An action would exceed a spend cap, permission boundary, or approved audience scope.",
            "Repeated retries produce the same failure or an owner cannot be reached.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Replace the fictional brief with an approved low-risk campaign brief from your organisation, keeping the same data fields and gates.",
    "Pilot only the read, calculate, and draft stages before connecting any publishing or advertising tool.",
    "Create a metric dictionary with owners, formulas, platform fields, windows, and known limitations.",
    "Run one controlled content experiment and document the predeclared decision rule before reviewing results.",
    "Review permissions, prompts, connectors, logs, and stop conditions at a regular operating cadence.",
]

LG_GLOSSARY = [
    ("Agent", "A goal-directed system that can select among permitted actions or tools using current state and feedback."),
    ("Workflow", "A predefined sequence of steps that reliably transforms an input into an output."),
    ("State", "The versioned information carried between steps, including campaign facts, decisions, and results."),
    ("Tool", "A bounded capability an agent can call, such as read data, calculate a metric, draft copy, or schedule a task."),
    ("Guardrail", "A testable condition that blocks, limits, routes, or records an action."),
    ("Approval gate", "A required human authorization before a high-impact state change."),
    ("Least privilege", "Granting only the minimum data and action permissions needed for the task."),
    ("Provenance", "Where a data point or claim came from, including source, time, and transformation history."),
    ("Idempotency", "A property that prevents the same action being applied twice when a step is retried."),
    ("CTR", "Click-through rate: clicks divided by impressions, multiplied by 100 for a percentage."),
    ("Conversion rate", "Conversions divided by a declared base such as clicks or sessions; the denominator must always be stated."),
    ("CPC", "Cost per click: spend divided by clicks."),
    ("CPA", "Cost per acquisition or purchase: spend divided by the named conversion count."),
    ("ROAS", "Return on ad spend: attributed conversion value divided by advertising spend."),
    ("Attribution", "The rules used to assign conversion credit to marketing touchpoints."),
    ("Control", "The current approved version used as the comparison arm in an experiment."),
    ("Treatment", "The experiment arm containing the single planned change."),
    ("Cooldown", "A defined observation period after a change during which further action is limited."),
    ("Rollback", "The versioned step that returns a system or campaign to the last known safe state."),
    ("Synthetic data", "Invented records designed for practice that do not represent real customers or accounts."),
]

NEXT_STEPS = dict(title="Put the System into Practice", items=LG_NEXT_STEPS)
THANK_YOU = dict(
    body="You can now design agentic marketing pipelines that move quickly while keeping evidence, ownership, and control visible.",
    kicker="C1798 COMPLETE",
)

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release: 6 topics, 12 connected labs, and 2 days / 15 hours.", TRAINER),
]
