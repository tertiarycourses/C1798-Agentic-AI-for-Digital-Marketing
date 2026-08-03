"""Topic 3 - AI Content Creation and Multimedia Automation. Labs 5-6."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Create a Governed Four-Platform Content Kit",
        objective="LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights",
        duration="40 minutes",
        prerequisites=[
            "Complete Lab 4 and keep the selected, review-gated 02-trends/04-viral-opportunity-brief.md open.",
            "Keep labs/resources/aurora-brand-brief.md and the Lab 2 operating specification available.",
            "Use a document editor and a classroom-approved AI assistant.",
        ],
        desc=(
            "You turn one selected, review-gated trend angle into Facebook, Instagram, LinkedIn, and X "
            "drafts without changing the core product truth. A claim ledger and per-platform review "
            "fields make every variant traceable and ready for human review."
        ),
        build=(
            "03-content/05-four-platform-content-kit.md containing a message hierarchy, four platform "
            "drafts, accessibility notes, a claim ledger, and a final review status."
        ),
        services="Aurora brief, Lab 4 opportunity brief, document editor, classroom-approved AI assistant",
        steps=[
            (
                "Create 03-content/05-four-platform-content-kit.md with sections Message Hierarchy, Instagram Draft, Facebook Draft, LinkedIn Draft, X Draft, Claim Ledger, and Review Log.",
                "",
            ),
            (
                "Under Message Hierarchy, write: audience = urban commuters; tension = bottle leaks in a work bag; promise = a practical bottle designed to be leak-resistant; evidence = verified specification plus a proposed demonstration awaiting owner confirmation; offer = 10% off first seven days with LOOP10; CTA = view the HydraLoop product page.",
                "",
            ),
            (
                "Add these required fields under every platform heading: Audience Moment, Hook, Body, CTA, Hashtags or Keywords, Visual Direction, Alt Text, Claim IDs, and Status. Set Status to DRAFT.",
                "",
            ),
            (
                "Send this structured request with the brand brief and Lab 4 opportunity brief. Do not include any real account or audience data.",
                "Create four platform-specific drafts from one verified message hierarchy. Preserve the same product truth and offer. Instagram: visual-first caption under 120 words with 5 relevant hashtags. Facebook: practical context under 150 words plus one conversation question. LinkedIn: workplace commute use case under 180 words with one operational takeaway. X: under 260 characters with no more than 2 hashtags. For every platform return Audience Moment, Hook, Body, CTA, Hashtags or Keywords, Visual Direction, Alt Text, Claim IDs, and Status=DRAFT. Do not invent certifications, medical or environmental benefits, testimonials, popularity, or scarcity. If a claim needs proof, label it NEEDS EVIDENCE.",
            ),
            (
                "Paste each variant into its matching section. Confirm the opening and format differ by platform while the audience tension, product truth, offer, and CTA stay aligned.",
                "",
            ),
            (
                "Create Claim Ledger columns Claim ID, Exact Wording, Source, Evidence Owner, Status, and Used In. Add one row each for capacity, cold duration, leak resistance, colours, price, offer, and shipping. Use BRIEF-01 as source and PRODUCT_OWNER as evidence owner.",
                "",
            ),
            (
                "Mark the proposed leak demonstration NEEDS OWNER CONFIRMATION until a real protocol and result exist. Remove or rewrite any statement that implies the demonstration has already happened.",
                "",
            ),
            (
                "Review accessibility: alt text should describe the useful visual information without repeating the entire caption; hashtags should use readable capitalization; emojis must not carry the only meaning. Record fixes in Review Log.",
                "",
            ),
            (
                "After the four drafts, Claim Ledger, evidence review, and accessibility review are complete, save this pre-assistant-review baseline as version v0.1. Add a Review Log row with draft owner, prompt version, source versions, timestamp_sgt, and baseline status.",
                "",
            ),
            (
                "Ask the assistant for a final consistency check. In Review Log add one row per proposed edit with Proposed Edit, Evidence, Accepted or Rejected, Reason, Owner, and Resulting Version. Apply only accepted evidence-supported edits, save version v0.2, and keep every platform Status as DRAFT.",
                "Compare these four drafts against the supplied Message Hierarchy and Claim Ledger. Return only: Contradiction, Unsupported Claim, Missing Accessibility Detail, Platform Mismatch, and Exact Fix. Do not rewrite correct content and do not add new facts.",
            ),
        ],
        test=(
            "The file contains exactly four platform drafts with all nine required fields. Every factual "
            "claim maps to the ledger, the unperformed demonstration is not presented as fact, each draft "
            "has usable alt text, and all four statuses remain DRAFT. The complete pre-assistant-review "
            "baseline is preserved as v0.1, accepted evidence-supported edits form v0.2, and the Review Log "
            "records every proposed edit as accepted or rejected with its reason, owner, and resulting version."
        ),
        deck_test=(
            "Four drafts contain all nine fields, link claims to the ledger, use accessible alt text, and "
            "stay DRAFT. v0.1 preserves the complete baseline; v0.2 contains accepted evidence-backed "
            "edits; the Review Log records accepted and rejected decisions."
        ),
        troubleshooting=[
            ("All four drafts sound identical", "Keep the message hierarchy fixed but restate the channel constraints and request a different opening structure for each platform."),
            ("The assistant invents a certification or health benefit", "Delete it, add the phrase 'use only Claim IDs in the ledger,' and rerun the affected platform draft."),
            ("Alt text becomes promotional copy", "Rewrite it as a concise description of subject, action, setting, and essential text visible in the image."),
        ],
        challenge="Add two controlled hook variants for Instagram while keeping the body, visual, CTA, and audience fixed for a later experiment.",
        reflection="Which content fields are allowed to vary by platform, and which must remain invariant to preserve campaign integrity?",
        checkpoint="A four-platform draft kit with evidence-linked claims that feeds campaign planning.",
        deck_steps=[
            "Lock the audience, promise, proof, offer, and CTA in a message hierarchy.",
            "Generate four native platform expressions with a fixed output schema.",
            "Audit claims, accessibility, and cross-channel consistency before review.",
        ],
    ),
    dict(
        num=6,
        topic=3,
        title="Design a Branded Image Concept and Short-Form Video Storyboard",
        objective="LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights",
        duration="45 minutes",
        prerequisites=[
            "Complete Lab 5 and keep the Instagram draft and Claim Ledger open.",
            "Use Gemini image generation (Nano Banana family), Canva, or the storyboard-only route if image generation is unavailable.",
            "Have a document editor and the Aurora visual direction from the brand brief available.",
        ],
        desc=(
            "You translate the campaign message into a reviewable image concept and a 15-second vertical "
            "video storyboard. You practise prompt anatomy, visual continuity, captions, safe zones, and "
            "rights review while keeping the product image conceptual and the output unpublished."
        ),
        build=(
            "03-content/06-creative-board.md plus an optional 06-hydraloop-concept.png, containing the "
            "image prompt, generation record, review checklist, six-scene storyboard, caption, and alt text."
        ),
        services="Gemini image generation or Canva, document editor, Lab 5 content kit",
        steps=[
            (
                "Create 03-content/06-creative-board.md with sections Creative Objective, Image Prompt, Generation Record, Image Review, Video Storyboard, Caption and Alt Text, Rights and Disclosure Check, and Status.",
                "",
            ),
            (
                "Under Creative Objective, write the audience moment, single message, platform, aspect ratio 4:5 for the image and 9:16 for video, and CTA. State that the bottle depiction is a concept because no approved product photograph is supplied.",
                "",
            ),
            (
                "Use this image prompt in Gemini image generation or Canva. If the tool is unavailable, paste it into the board and continue with a hand-drawn wireframe.",
                "Create a clearly labelled concept advertising image for a fictional product named HydraLoop: a reusable 750 ml insulated water bottle in ocean blue, upright beside a closed work tote on a clean desk near a bright Singapore office window. Natural morning light, pale-sand background, subtle coral accent, realistic commercial photography, generous copy space in the upper right, 4:5 portrait composition. No people, no logos other than the fictional word HydraLoop, no certifications, no health claims, no competitor branding, no distorted cap, no unreadable label text.",
            ),
            (
                "Save one acceptable output as 03-content/06-hydraloop-concept.png. In Generation Record write tool, date, prompt version, output filename, and 'AI-generated concept; product fidelity not approved.' Do not record a credential or private account identifier.",
                "",
            ),
            (
                "Complete Image Review with yes/no rows for concept label, product shape, cap geometry, readable text, palette, copy space, brand fit, prohibited claims, third-party marks, representation, and visible artefacts. If any critical row is no, regenerate or use the storyboard-only route.",
                "",
            ),
            (
                "Create a six-row Video Storyboard table with columns Time, Visual, Action, Voiceover, On-Screen Text, Sound, and Review Note. Use intervals 0-2s, 2-4s, 4-7s, 7-10s, 10-13s, and 13-15s.",
                "",
            ),
            (
                "Build the story: work-bag tension; bottle and tote setup; careful concept leak-test setup; carrying-loop detail; three colours and offer; final CTA. Keep on-screen text inside the centre 80% safe zone and use no more than eight words per scene.",
                "",
            ),
            (
                "Write a 15-second voiceover under 38 words. It must not say the fictional leak test proves performance. Use wording such as 'designed to be leak-resistant' and route the demonstration protocol to the product owner.",
                "",
            ),
            (
                "Add a social caption, descriptive alt text for the image, and a plain-text transcript for the video. Check that essential information is present in captions or voiceover rather than colour alone.",
                "",
            ),
            (
                "Under Rights and Disclosure Check, confirm all inputs are fictional or owned for class, no real person or brand is imitated, generated output is labelled internally, platform disclosure requirements must be checked at publication time, and Status remains REVIEW.",
                "",
            ),
        ],
        test=(
            "The creative board contains a complete prompt, generation record or wireframe, eleven-row "
            "image review, six timed video scenes totalling 15 seconds, voiceover under 38 words, caption, "
            "alt text, transcript, rights check, and Status REVIEW. No unverified demonstration result is claimed."
        ),
        troubleshooting=[
            ("The generated bottle has distorted parts or text", "Remove complex label text, restate one bottle and one cap, regenerate, and keep the output labelled as a concept."),
            ("The tool is unavailable or requires a paid feature", "Use the exact prompt to draw a 4:5 wireframe and complete every review and storyboard field without generating an image."),
            ("The storyboard is longer than 15 seconds", "Keep the six fixed time ranges, shorten voiceover, and move supporting detail into the caption."),
        ],
        challenge="Create a second image prompt for the office-wellbeing segment while preserving the same product facts, palette, aspect ratio, and review controls.",
        reflection="Which parts of a generated visual can be checked from the file itself, and which require an external owner or source?",
        checkpoint="A rights-aware image concept and short-video storyboard ready to enter the campaign creative matrix.",
        deck_steps=[
            "Translate the approved message into a bounded image prompt or wireframe.",
            "Review product fidelity, claims, rights, accessibility, and artefacts.",
            "Build a six-scene, 15-second storyboard with captions and safe zones.",
        ],
    ),
]
