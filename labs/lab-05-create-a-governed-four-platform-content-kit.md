# Lab 5 — Create a Governed Four-Platform Content Kit

**Course:** Agentic AI for Digital Marketing and Advertising (C1798)  
**Topic 3:** AI Content Creation and Multimedia Automation  
**Maps to:** LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights  
**Tools:** Aurora brief, Lab 4 opportunity brief, document editor, classroom-approved AI assistant  
**Duration:** 40 minutes

---

## Goal

LO3: Produce an aligned multi-platform content and multimedia kit that preserves audience intent, brand voice, factual accuracy, and creative rights.

## What You Will Do

You turn one selected, review-gated trend angle into Facebook, Instagram, LinkedIn, and X drafts without changing the core product truth. A claim ledger and per-platform review fields make every variant traceable and ready for human review.

## What You Will Build

03-content/05-four-platform-content-kit.md containing a message hierarchy, four platform drafts, accessibility notes, a claim ledger, and a final review status.

## Prerequisites

- Complete Lab 4 and keep the selected, review-gated 02-trends/04-viral-opportunity-brief.md open.
- Keep labs/resources/aurora-brand-brief.md and the Lab 2 operating specification available.
- Use a document editor and a classroom-approved AI assistant.

> **Data note.** Use only the fictional Aurora Active scenario and synthetic course data. Keep credentials out of prompts and files. Do not publish a post, activate a campaign, change targeting, or change spend during class; prepare a reviewable draft and route high-impact actions to the named owner.

## Steps

**1. Create 03-content/05-four-platform-content-kit.md with sections Message Hierarchy, Instagram Draft, Facebook Draft, LinkedIn Draft, X Draft, Claim Ledger, and Review Log.**

**2. Under Message Hierarchy, write: audience = urban commuters; tension = bottle leaks in a work bag; promise = a practical bottle designed to be leak-resistant; evidence = verified specification plus a proposed demonstration awaiting owner confirmation; offer = 10% off first seven days with LOOP10; CTA = view the HydraLoop product page.**

**3. Add these required fields under every platform heading: Audience Moment, Hook, Body, CTA, Hashtags or Keywords, Visual Direction, Alt Text, Claim IDs, and Status. Set Status to DRAFT.**

**4. Send this structured request with the brand brief and Lab 4 opportunity brief. Do not include any real account or audience data.**

```text
Create four platform-specific drafts from one verified message hierarchy. Preserve the same product truth and offer. Instagram: visual-first caption under 120 words with 5 relevant hashtags. Facebook: practical context under 150 words plus one conversation question. LinkedIn: workplace commute use case under 180 words with one operational takeaway. X: under 260 characters with no more than 2 hashtags. For every platform return Audience Moment, Hook, Body, CTA, Hashtags or Keywords, Visual Direction, Alt Text, Claim IDs, and Status=DRAFT. Do not invent certifications, medical or environmental benefits, testimonials, popularity, or scarcity. If a claim needs proof, label it NEEDS EVIDENCE.
```

**5. Paste each variant into its matching section. Confirm the opening and format differ by platform while the audience tension, product truth, offer, and CTA stay aligned.**

**6. Create Claim Ledger columns Claim ID, Exact Wording, Source, Evidence Owner, Status, and Used In. Add one row each for capacity, cold duration, leak resistance, colours, price, offer, and shipping. Use BRIEF-01 as source and PRODUCT_OWNER as evidence owner.**

**7. Mark the proposed leak demonstration NEEDS OWNER CONFIRMATION until a real protocol and result exist. Remove or rewrite any statement that implies the demonstration has already happened.**

**8. Review accessibility: alt text should describe the useful visual information without repeating the entire caption; hashtags should use readable capitalization; emojis must not carry the only meaning. Record fixes in Review Log.**

**9. After the four drafts, Claim Ledger, evidence review, and accessibility review are complete, save this pre-assistant-review baseline as version v0.1. Add a Review Log row with draft owner, prompt version, source versions, timestamp_sgt, and baseline status.**

**10. Ask the assistant for a final consistency check. In Review Log add one row per proposed edit with Proposed Edit, Evidence, Accepted or Rejected, Reason, Owner, and Resulting Version. Apply only accepted evidence-supported edits, save version v0.2, and keep every platform Status as DRAFT.**

```text
Compare these four drafts against the supplied Message Hierarchy and Claim Ledger. Return only: Contradiction, Unsupported Claim, Missing Accessibility Detail, Platform Mismatch, and Exact Fix. Do not rewrite correct content and do not add new facts.
```

## Test It

The file contains exactly four platform drafts with all nine required fields. Every factual claim maps to the ledger, the unperformed demonstration is not presented as fact, each draft has usable alt text, and all four statuses remain DRAFT. The complete pre-assistant-review baseline is preserved as v0.1, accepted evidence-supported edits form v0.2, and the Review Log records every proposed edit as accepted or rejected with its reason, owner, and resulting version.

## Checkpoint for the Next Lab

A four-platform draft kit with evidence-linked claims that feeds campaign planning.

## Troubleshooting

- **All four drafts sound identical:** Keep the message hierarchy fixed but restate the channel constraints and request a different opening structure for each platform.
- **The assistant invents a certification or health benefit:** Delete it, add the phrase 'use only Claim IDs in the ledger,' and rerun the affected platform draft.
- **Alt text becomes promotional copy:** Rewrite it as a concise description of subject, action, setting, and essential text visible in the image.

## Challenge

Add two controlled hook variants for Instagram while keeping the body, visual, CTA, and audience fixed for a later experiment.

## Reflection

Which content fields are allowed to vary by platform, and which must remain invariant to preserve campaign integrity?

---

[← Lab 4](lab-04-generate-a-viral-opportunity-brief-and-scheduled-research-spec.md) · [Lab 6 →](lab-06-design-a-branded-image-concept-and-short-form-video-storyboard.md)
