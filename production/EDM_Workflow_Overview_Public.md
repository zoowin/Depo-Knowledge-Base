# EDM Automated Workflow — Overview

An AI-assisted email marketing production system. The AI reads a structured brand knowledge base and historical campaign data to generate email content, assemble responsive HTML templates, and deploy campaigns to Klaviyo via API. Human reviews and approves at every key stage.

---

## System Architecture

The system is organized into three layers, each stored as structured files that the AI can read and reference:

```
Knowledge Base (Read-Only)       Strategy Layer (Planning)       Production Layer (Execution)
──────────────────────────       ─────────────────────────       ────────────────────────────
Product Cards (per SKU)          Monthly Email Calendar           Email Drafts (Markdown)
Brand Voice & Tone Rules         Promotion Calendar (yearly)      HTML Code Templates
Compliance Guidelines            Topic Pool (auto + manual)       Image Asset Library
Copy & Topic Formulas            Campaign Performance Log         Klaviyo Campaign Deployment
Visual Style Guides
```

The AI cross-references all three layers when generating content — for example, checking compliance rules while drafting copy, or reviewing past campaign data before selecting next month's topics.

---

## Monthly Workflow (5 Phases)

### Phase 0: Plan

Data-driven monthly planning cycle:

1. **Performance Review** — Pull last month's campaign metrics via Klaviyo API (OR, CR, Revenue, RPR). Identify what worked and what didn't.
2. **Promotion Check** — Cross-reference the yearly promotion calendar for upcoming events. Determine the ratio of promotional vs. evergreen content.
3. **Topic Selection** — Select topics from the pool, applying anti-duplication rules to prevent content fatigue.
4. **Scheduling** — Assign send dates, product focus, template choice, and audience segments for each email.

Output: Monthly calendar with 8-15 emails planned, each with topic, type, product, and template assigned.

### Phase 1: Write

AI drafts each email following a standardized output format:

- 3-4 subject line candidates (with/without emoji for A/B testing)
- Preview text (40-90 characters)
- Hero section (headline, subheadline, CTA)
- Body section (education or promotion copy)
- Product cards ×3 (role label, description, CTA, product image)
- Closing CTA
- Hero image brief (for AI image generation)

All product descriptions are sourced from the knowledge base — never invented. Copy is checked against compliance guidelines before output.

### Phase 2: Build

1. AI generates a complete, responsive email HTML using pre-built code templates
2. Product images are auto-selected from a centralized URL library
3. Hero images are generated using AI image tools (Midjourney / ChatGPT) based on the brief
4. Finished HTML is uploaded to Klaviyo as a CODE template via API

### Phase 3: Deploy

1. AI creates the Klaviyo campaign via API — sets name, included/excluded audiences, send time
2. AI assigns the HTML template to the campaign message
3. Human previews the email in Klaviyo (desktop + mobile)
4. Human sends a test email, then schedules

### Phase 4: Learn

1. Pull performance data 48-72 hours post-send
2. Update the campaign log with metrics + key learnings
3. Insights feed directly into the next month's Phase 0 planning

---

## Template System

Two base HTML templates maintained as pure code (not drag-and-drop):

| Template | Visual Style | Best For |
|----------|-------------|----------|
| Dark | Black background, white text | Education, storytelling, trust-building |
| Light | White background, dark text | Promotions, product highlights, seasonal events |

Both share the same structural skeleton:

```
Header (Logo Banner)
Hero Image (600 × 400px)
Hero Text — Headline + Subheadline + CTA
Body Text — Section Title + 2-3 Paragraphs
Checklist (Optional — 3 key points)
Product Section Title + Subtitle
Product Cards ×3 — Text (65%) | Image (35%)
Closing CTA
Footer — Logo + Social Icons | Company Info + Unsubscribe
```

Technical specs: 600px container width, ~17KB source HTML (well under Gmail's 102KB clipping limit), fully mobile responsive, product cards maintain side-by-side layout on all devices.

---

## Automation vs. Human

| Step | AI | Human |
|------|-----|-------|
| Performance data pull & analysis | ✅ | |
| Topic pool update (trend scraping) | ✅ | Review & curate |
| Monthly calendar generation | ✅ Draft | Approve & adjust |
| Email copywriting | ✅ Draft | Review & edit |
| HTML template generation | ✅ | |
| Product image selection | ✅ From library | Upload new images |
| Hero image creation | | ✅ Via AI image tools |
| Campaign creation + audience setup | ✅ Via API | |
| Template assignment to campaign | ✅ Via API | |
| Preview & QA | | ✅ |
| Send / Schedule | | ✅ |
| Post-send data logging | ✅ | Add learnings |

Estimated human time per email: ~15-20 minutes (review + image + QA + send).

---

## Content Guardrails

- Anti-duplication: Same topic angle no repeat within 45 days; same hero product no repeat within 30 days
- No consecutive promotional emails
- All copy checked against compliance word list before output
- Subject lines provided in multiple variants for A/B testing

---

## Tools

- **Klaviyo** — Email platform with API access (campaign creation, template upload, audience management, performance reporting)
- **AI Assistant** — Content generation, HTML coding, data analysis, campaign deployment
- **Shopify** — E-commerce backend, discount code management, product data
- **AI Image Tools** — Hero image generation from structured briefs
- **Python** — Automated trend scraping for topic pool updates
