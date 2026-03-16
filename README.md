# Depology EDM Knowledge Base

Production system for Depology's email marketing, blog content, and SMS campaigns.

## Quick Start

**For Claude / AI:** Read `CLAUDE.md` first — it contains all brand rules, workflows, and file navigation.

**For Humans:** Follow the workflow below.

## Directory Structure

| Folder | Purpose |
|--------|---------|
| `strategy/` | Monthly calendars, topic pool, campaign log, email strategy |
| `knowledge/` | Brand brain — product SKU cards, compliance rules, visual guides, copy formulas |
| `production/` | Active work — email drafts, SMS drafts, blog drafts, HTML output, assets |
| `tools/` | Python scripts for trend fetching, HTML generation, templates |
| `.skills/` | Claude skill definitions (edm-writer, edm-html-builder, edm-image-brief) |

## Monthly Workflow

1. **Plan** — Check `strategy/calendars/2026/` for the month's schedule
2. **Draft** — Claude batch-produces all email drafts for the month
3. **Review** — Preview HTML locally in browser, provide feedback
4. **Upload** — Copy final HTML into Klaviyo, set subject/audience/schedule
5. **Send** — Hit send in Klaviyo
6. **Log** — Update `strategy/campaign-log.md` with results

## Key Files

| File | What it does |
|------|-------------|
| `CLAUDE.md` | AI entry point — brand rules, product system, workflow |
| `strategy/topic-pool.md` | Content ideas (auto-fetched + manual) |
| `strategy/campaign-log.md` | Historical sends — prevents duplication |
| `knowledge/compliance/email-compliance-rules.md` | Blacklisted terms & safe alternatives |
| `knowledge/formulas/copy-winning-formula.md` | Email copy structure template |
| `production/campaign-workflow.md` | Klaviyo execution guide |

## Tools

Run trend fetching:
```bash
cd tools/
python fetch_trends.py
```

---
*Maintained by Depology Operations.*
