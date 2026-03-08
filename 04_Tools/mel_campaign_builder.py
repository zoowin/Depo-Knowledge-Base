#!/usr/bin/env python3
"""
mel_campaign_builder.py  —  Depology EDM Campaign Builder
===========================================================
Reads the Mel-style master template and injects per-campaign content.
Output: a ready-to-upload HTML file for Klaviyo.

Usage
-----
1. Fill in the CAMPAIGN dict below with the new campaign's content.
2. Run:  python mel_campaign_builder.py
3. Preview the output HTML in a browser.
4. Upload via Klaviyo MCP (or Claude's Klaviyo tools).

Content supplied per campaign
------------------------------
• hero_headline_1 / hero_headline_2   — Two-line hero heading
• hero_subheadline                    — One-line subheadline below hero
• hero_cta_url                        — SHOP NOW button URL in hero section
• hero_img_1 / hero_img_2             — Leon uploads to Klaviyo, pastes CDN URL here
• body_headline                       — Section heading (bold, above body copy)
• body_para_1/2/3                     — Body copy paragraphs
• goals_title / goal_1/2/3            — "Goals" bullet list (left column)
• product_section_title               — Section heading above product cards
• p1_title / p1_desc / p1_url / p1_img — Product card 1
• p2_title / p2_desc / p2_url / p2_img — Product card 2
• p3_title / p3_desc / p3_url / p3_img — Product card 3

Notes
------
• p1_title: use \\n for a line-break inside the title (renders as <br/>)
• hero_img_1 & hero_img_2: Claude leaves these as placeholders (HERO_IMAGE_1_URL_HERE /
  HERO_IMAGE_2_URL_HERE). Leon uploads hero images to Klaviyo, then pastes the CDN URLs
  into the final HTML before uploading the template.
• Product images: Claude looks up CDN URLs from PRODUCT_IMAGES dict below.
  Source of truth: 04_Tools/Product_Image_Library.md
  If a product's URL shows "PENDING", ask Leon to upload the image to Klaviyo first.
"""

import os
import re
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# PRODUCT IMAGE LIBRARY
# Source: 04_Tools/Product_Image_Library.md
# ─────────────────────────────────────────────────────────────
PRODUCT_IMAGES = {
    # ── Confirmed uploaded to Klaviyo ────────────────────────
    "opuntia_cleansing_balm":
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/"
        "63b261a2-9e8a-403f-8343-cde631ec3b49.png",
    "argireline_mps_serum":
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/"
        "8f6ca609-56c2-4152-aca9-60db1fae9f1e.png",
    "cica_recovery_serum":
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/"
        "fc33e5c3-ab65-40a0-92f1-031418fc7478.png",

    # ── Pending upload — update URL after Leon uploads ───────
    "matrixyl_serum":       "PENDING_UPLOAD",
    "matriplex_cream":      "PENDING_UPLOAD",
    "profi_overnight_mask": "PENDING_UPLOAD",
    "argireline_eye_stick": "PENDING_UPLOAD",
    "microdart_eye_patch":  "PENDING_UPLOAD",
    "argireline_eye_cream": "PENDING_UPLOAD",
    "retinol_night_cream":  "PENDING_UPLOAD",
    "retinol_body_lotion":  "PENDING_UPLOAD",
    "cica_cleanser":        "PENDING_UPLOAD",
    "microoperator_cream":  "PENDING_UPLOAD",
}

PRODUCT_URLS = {
    "opuntia_cleansing_balm":  "https://depology.com/products/opuntia-c-relief-cleansing-balm",
    "argireline_mps_serum":    "https://depology.com/products/argireline-anti-wrinkle-serum",
    "cica_recovery_serum":     "https://depology.com/products/cica-h-a-calm-repair-serum",
    "matrixyl_serum":          "https://depology.com/products/depology-matrixyl-3000-serum",
    "matriplex_cream":         "https://depology.com/products/tri-active-matrixyl-complex-cream",
    "profi_overnight_mask":    "https://depology.com/products/pro-firming-matrixyl-3000-dynalift-night-mask",
    "argireline_eye_stick":    "https://depology.com/products/argireline-anti-aging-eye-stick",
    "microdart_eye_patch":     "https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-pb",
    "argireline_eye_cream":    "https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream",
    "retinol_night_cream":     "https://depology.com/products/anti-aging-retinol-night-cream",
    "retinol_body_lotion":     "https://depology.com/products/retinol-radiance-body-lotion",
    "cica_cleanser":           "https://depology.com/products/cica-redness-relief-nourishing-cleanser",
    "microoperator_cream":     "https://depology.com/products/deepcare-r-microoperator-boosting-cream-beginner",
}

def img(key: str) -> str:
    """Return product image CDN URL by key.  Raises ValueError if not yet uploaded."""
    url = PRODUCT_IMAGES.get(key)
    if url is None:
        raise ValueError(f"Unknown product key: '{key}'. Check Product_Image_Library.md.")
    if url == "PENDING_UPLOAD":
        raise ValueError(
            f"Product image for '{key}' has not been uploaded to Klaviyo yet.\n"
            "Ask Leon to upload the image and update Product_Image_Library.md + PRODUCT_IMAGES."
        )
    return url

def url(key: str) -> str:
    """Return product Shopify URL by key."""
    u = PRODUCT_URLS.get(key)
    if u is None:
        raise ValueError(f"Unknown product key: '{key}'. Check Product_Image_Library.md.")
    return u

# ─────────────────────────────────────────────────────────────
# CAMPAIGN CONFIG  ← Claude fills this in per campaign
# ─────────────────────────────────────────────────────────────
CAMPAIGN = {
    # ── Meta ──────────────────────────────────────────────
    "campaign_name": "Spring Equinox: Transitioning Routine",
    "date": "2026-03-20",

    # ── Hero Section ──────────────────────────────────────
    "hero_headline_1": "Spring Cleaning...",
    "hero_headline_2": "For Your Face?",
    "hero_subheadline": "The seasons are changing. Your skincare should too.",
    "hero_cta_url": "https://depology.com",

    # Hero images — Leon uploads to Klaviyo, then provides the CDN URL.
    # Claude leaves these blank (empty string) until Leon provides them.
    "hero_img_1": "HERO_IMAGE_1_URL_HERE",
    "hero_img_2": "HERO_IMAGE_2_URL_HERE",

    # ── Body Section ──────────────────────────────────────
    "body_headline": "Shedding The Winter Coat",
    "body_para_1": (
        "You wouldn't wear a heavy wool coat in 60°F weather. "
        "So why are you still \u201cwearing\u201d your heavy winter skincare?"
    ),
    "body_para_2": (
        "During winter, our skin is in survival mode, fighting dry air, "
        "wind, and indoor heating. We layer on thick, occlusive creams "
        "to lock moisture in."
    ),
    "body_para_3": (
        "But as the air gets humid and temperatures rise, those heavy layers "
        "can start to feel suffocating (and even clog pores)."
    ),

    # ── Goals / CTA Bullets ───────────────────────────────
    "goals_title": "Spring Skin Goals:",
    "goal_1": "\u2714 Gently slough off the dull, dead winter skin cells.",
    "goal_2": "\u2714 Swap heavy creams for hydrating serums.",
    "goal_3": "\u2714 UV rays are getting stronger\u2014don\u2019t skip SPF.",

    # ── Product Section ───────────────────────────────────
    "product_section_title": "Spring Wardrobe... For Skin",

    # Product 1 — use img("key") / url("key") from PRODUCT_IMAGES / PRODUCT_URLS above
    "p1_title": "The Deep Cleanse\n(Melt Away Winter)",
    "p1_desc": (
        "Spring cleaning starts here. Gently melt away makeup, SPF, and "
        "dull winter skin cells without stripping your moisture barrier."
    ),
    "p1_url": url("opuntia_cleansing_balm"),
    "p1_img": img("opuntia_cleansing_balm"),

    # Product 2
    "p2_title": "The Lightweight Line-Fighter",
    "p2_desc": (
        "Swap heavy anti-aging creams for this water-light peptide serum. "
        "It targets dynamic lines and relaxes tension, perfect for a fresh, "
        "rested look."
    ),
    "p2_url": url("argireline_mps_serum"),
    "p2_img": img("argireline_mps_serum"),

    # Product 3
    "p3_title": "The Seasonal Soother",
    "p3_desc": (
        "Spring weather can be unpredictable. Keep this soothing serum on "
        "hand to calm any redness or sensitivity during the transition."
    ),
    "p3_url": url("cica_recovery_serum"),
    "p3_img": img("cica_recovery_serum"),
}

# ─────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
TEMPLATE    = os.path.join(SCRIPT_DIR, "mel_master_template.html")
OUTPUT_DIR  = os.path.join(os.path.dirname(SCRIPT_DIR),
                           "03_Production", "05_HTML_Drafts")


# ─────────────────────────────────────────────────────────────
# KNOWN STRINGS IN THE MASTER TEMPLATE
# These are the Spring Equinox campaign values — used as anchors
# for replacement. DO NOT change these unless you regenerate the
# master template from a new Klaviyo export.
# ─────────────────────────────────────────────────────────────

# ── Image URLs ────────────────────────────────────────────────
HERO_IMG_1_OLD  = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/91d179ef-00c8-44e8-b396-8204ae4a28ca.jpeg"
HERO_IMG_2_OLD  = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/40dc6ed9-2481-481c-99ca-a0da5680945d.jpeg"
P1_IMG_OLD      = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/63b261a2-9e8a-403f-8343-cde631ec3b49.png"
P2_IMG_OLD      = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/8f6ca609-56c2-4152-aca9-60db1fae9f1e.png"
P3_IMG_OLD      = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fc33e5c3-ab65-40a0-92f1-031418fc7478.png"

# ── Hero headline ─────────────────────────────────────────────
HERO_H1_OLD     = "Spring Cleaning..."
HERO_H2_OLD     = "For Your Face?"

# ── Hero subheadline — desktop (3-span block) ─────────────────
DESKTOP_SUB_MARKER = 'white-space:pre-line; line-height:140%">'
DESKTOP_SUB_OLD = (
    '<span style="font-size: 24px; color: rgb(255, 255, 255); font-family: '
    "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
    'font-style: normal;">The seasons are changing. </span>'
    '<span style="font-size: 24px; color: rgb(255, 255, 255); font-family: '
    "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
    'font-style: normal;">Your skincare\xa0</span>'
    '<span style="font-size: 24px; color: rgb(255, 255, 255); font-family: '
    "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
    'font-style: normal;">should too.</span>'
)

# ── Hero subheadline — mobile (2-paragraph block) ─────────────
MOBILE_SUB_OLD = (
    '<p style="text-align: center; line-height: 50%;">'
    '<span style="color: rgb(255, 255, 255); font-size: 20px; font-family: '
    "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
    'font-style: normal;">The seasons are changing. </span></p>'
    '<p style="padding-bottom:0; text-align:center; line-height:50%">'
    '<span style="color: rgb(255, 255, 255); font-size: 20px; font-family: '
    "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
    'font-style: normal;">Your skincare should too.</span></p>'
)

# ── Hero SHOP NOW button href (hero section, appears twice) ───
HERO_CTA_OLD    = 'href="http://depology.com"'

# ── Body section ──────────────────────────────────────────────
BODY_H_OLD      = "Shedding The Winter Coat\xa0"   # \xa0 = non-breaking space in template
BODY_P1_OLD     = (
    # Template: curly apostrophe \u2019 for "wouldn't", straight " for "wearing"
    "You wouldn\u2019t wear a heavy wool coat in 60\u00b0F weather. "
    'So why are you still "wearing" your heavy winter skincare?'
)
BODY_P2_OLD     = (
    "During winter, our skin is in survival mode, fighting dry air, wind, "
    "and indoor heating. We layer on thick, occlusive creams to lock moisture in."
)
BODY_P3_OLD     = (
    "But as the air gets humid and temperatures rise, those heavy layers "
    "can start to feel suffocating (and even clog pores)."
)

# ── Goals ─────────────────────────────────────────────────────
GOALS_TITLE_OLD = "Spring Skin Goals:"
GOAL1_OLD       = "\u2714 Gently slough off the dull, dead winter skin cells."
GOAL2_OLD       = "\u2714 Swap heavy creams for hydrating serums."
GOAL3_OLD       = "\u2714 UV rays are getting stronger\u2014don\u2019t skip SPF."

# ── Product section ───────────────────────────────────────────
PROD_TITLE_OLD  = "Spring Wardrobe... For Skin"

# ── Product card 1 ────────────────────────────────────────────
P1_TITLE_OLD    = " The Deep Cleanse<br/>(Melt Away Winter) "
P1_DESC_OLD     = (
    " Spring cleaning starts here. Gently melt away makeup, SPF, and dull "
    "winter skin cells without stripping your moisture barrier. "
)
P1_URL_OLD      = "https://depology.com/products/opuntia-c-relief-cleansing-balm"

# ── Product card 2 ────────────────────────────────────────────
P2_TITLE_OLD    = "The Lightweight Line-Fighter\xa0"  # \xa0 = non-breaking space in template
P2_DESC_OLD     = (
    "Swap heavy anti-aging creams for this water-light peptide serum. "
    "It targets dynamic lines and relaxes tension, perfect for a fresh, "
    "rested look. "
)
P2_URL_OLD      = "https://depology.com/products/argireline-anti-wrinkle-serum"

# ── Product card 3 ────────────────────────────────────────────
P3_TITLE_OLD    = "The Seasonal Soother"
P3_DESC_OLD     = (
    "Spring weather can be unpredictable. Keep this soothing serum on hand "
    "to calm any redness or sensitivity during the transition."
)
P3_URL_OLD      = "https://depology.com/products/cica-h-a-calm-repair-serum"


# ─────────────────────────────────────────────────────────────
# BUILDER
# ─────────────────────────────────────────────────────────────

def title_to_html(title: str) -> str:
    """Convert \\n line-breaks in product titles to <br/>."""
    return title.replace("\n", "<br/>")


def build(cfg: dict) -> str:
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        html = f.read()

    # ── Images ────────────────────────────────────────────────
    html = html.replace(HERO_IMG_1_OLD, cfg["hero_img_1"])
    html = html.replace(HERO_IMG_2_OLD, cfg["hero_img_2"])
    html = html.replace(P1_IMG_OLD,     cfg["p1_img"])
    html = html.replace(P2_IMG_OLD,     cfg["p2_img"])
    html = html.replace(P3_IMG_OLD,     cfg["p3_img"])

    # ── Hero headline ─────────────────────────────────────────
    html = html.replace(HERO_H1_OLD, cfg["hero_headline_1"])
    html = html.replace(HERO_H2_OLD, cfg["hero_headline_2"])

    # ── Hero subheadline (desktop — single consolidated span) ─
    new_desktop_sub = (
        '<span style="font-size: 24px; color: rgb(255, 255, 255); font-family: '
        "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
        f'font-style: normal;">{cfg["hero_subheadline"]}</span>'
    )
    html = html.replace(DESKTOP_SUB_OLD, new_desktop_sub)

    # ── Hero subheadline (mobile — single paragraph) ──────────
    new_mobile_sub = (
        '<p style="text-align: center; line-height: 50%;">'
        '<span style="color: rgb(255, 255, 255); font-size: 20px; font-family: '
        "'Aktiv Regular + Bold', Helvetica, Arial, sans-serif; font-weight: 400; "
        f'font-style: normal;">{cfg["hero_subheadline"]}</span></p>'
    )
    html = html.replace(MOBILE_SUB_OLD, new_mobile_sub)

    # ── Hero CTA URL (both buttons in hero section) ────────────
    new_hero_cta = f'href="{cfg["hero_cta_url"]}"'
    # Replace only the hero section occurrences (http://depology.com)
    html = html.replace(HERO_CTA_OLD, new_hero_cta)

    # ── Body headline ─────────────────────────────────────────
    # Template uses \xa0 (non-breaking space) after headline; preserve it
    new_body_h = cfg["body_headline"] + "\xa0"
    html = html.replace(BODY_H_OLD, new_body_h)

    # ── Body paragraphs ───────────────────────────────────────
    html = html.replace(BODY_P1_OLD, cfg["body_para_1"])
    html = html.replace(BODY_P2_OLD, cfg["body_para_2"])
    # P3 appears in desktop (no leading space) and mobile (leading space).
    # str.replace finds the exact substring within both — the leading space
    # in the mobile version remains untouched since it's not in the target.
    html = html.replace(BODY_P3_OLD, cfg["body_para_3"])

    # ── Goals ─────────────────────────────────────────────────
    html = html.replace(GOALS_TITLE_OLD, cfg["goals_title"])
    html = html.replace(GOAL1_OLD,       cfg["goal_1"])
    html = html.replace(GOAL2_OLD,       cfg["goal_2"])
    html = html.replace(GOAL3_OLD,       cfg["goal_3"])

    # ── Product section title ─────────────────────────────────
    html = html.replace(PROD_TITLE_OLD, cfg["product_section_title"])

    # ── Product card 1 ────────────────────────────────────────
    # Title has leading/trailing spaces matching the template
    p1_title_html = " " + title_to_html(cfg["p1_title"]) + " "
    html = html.replace(P1_TITLE_OLD, p1_title_html)
    # Description has leading/trailing spaces matching the template
    p1_desc_html = " " + cfg["p1_desc"] + " "
    html = html.replace(P1_DESC_OLD, p1_desc_html)
    html = html.replace(P1_URL_OLD,  cfg["p1_url"])

    # ── Product card 2 ────────────────────────────────────────
    # Template uses \xa0 (non-breaking space) after P2 title
    p2_title_html = title_to_html(cfg["p2_title"]) + "\xa0"
    html = html.replace(P2_TITLE_OLD, p2_title_html)
    p2_desc_html = cfg["p2_desc"] + " "
    html = html.replace(P2_DESC_OLD, p2_desc_html)
    html = html.replace(P2_URL_OLD,  cfg["p2_url"])

    # ── Product card 3 ────────────────────────────────────────
    html = html.replace(P3_TITLE_OLD, title_to_html(cfg["p3_title"]))
    html = html.replace(P3_DESC_OLD,  cfg["p3_desc"])
    html = html.replace(P3_URL_OLD,   cfg["p3_url"])

    return html


def verify_replacements(html: str, cfg: dict) -> list[str]:
    """
    Check that old template strings were replaced.
    Skips checks where the new cfg value equals the old template value
    (no-op replacements are intentional when reusing the same content).
    Returns a list of warnings for any unintended leftover old strings.
    """
    # (old_string, cfg_key_for_new_value, label)
    checks = [
        (HERO_IMG_1_OLD,   cfg.get("hero_img_1"),              "hero_img_1 URL"),
        (HERO_IMG_2_OLD,   cfg.get("hero_img_2"),              "hero_img_2 URL"),
        (HERO_H1_OLD,      cfg.get("hero_headline_1"),         "hero_headline_1"),
        (HERO_H2_OLD,      cfg.get("hero_headline_2"),         "hero_headline_2"),
        ("The seasons are changing. ",
                           cfg.get("hero_subheadline","")[:26], "hero_subheadline"),
        (BODY_H_OLD,       (cfg.get("body_headline","") + "\xa0"), "body_headline"),
        (BODY_P1_OLD,      cfg.get("body_para_1"),             "body_para_1"),
        (BODY_P2_OLD,      cfg.get("body_para_2"),             "body_para_2"),
        (GOALS_TITLE_OLD,  cfg.get("goals_title"),             "goals_title"),
        (GOAL1_OLD,        cfg.get("goal_1"),                  "goal_1"),
        (GOAL2_OLD,        cfg.get("goal_2"),                  "goal_2"),
        (GOAL3_OLD,        cfg.get("goal_3"),                  "goal_3"),
        (PROD_TITLE_OLD,   cfg.get("product_section_title"),   "product_section_title"),
        (P1_URL_OLD,       cfg.get("p1_url"),                  "p1_url"),
        (P2_URL_OLD,       cfg.get("p2_url"),                  "p2_url"),
        (P3_URL_OLD,       cfg.get("p3_url"),                  "p3_url"),
    ]
    warnings = []
    for old, new_val, label in checks:
        # Skip: old string intentionally unchanged because new value == old value
        if new_val is not None and old in (new_val if new_val else ""):
            continue
        if new_val == old:
            continue
        if old in html:
            warnings.append(f"  ⚠️  {label} — old string still present (replacement may have failed)")
    return warnings


def save(html: str, cfg: dict) -> str:
    """Save the rendered HTML and return the output path."""
    date_str  = cfg["date"].replace("-", "")
    safe_name = cfg["campaign_name"].replace(" ", "_").replace(":", "").replace("/", "-")
    filename  = f"{date_str}_{safe_name}.html"

    # Month subfolder
    dt     = datetime.strptime(cfg["date"], "%Y-%m-%d")
    month  = dt.strftime("%Y_%m_%B")
    outdir = os.path.join(OUTPUT_DIR, month)
    os.makedirs(outdir, exist_ok=True)

    out_path = os.path.join(outdir, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\n{'='*60}")
    print(f"  Mel Campaign Builder")
    print(f"  Campaign : {CAMPAIGN['campaign_name']}")
    print(f"  Date     : {CAMPAIGN['date']}")
    print(f"{'='*60}\n")

    if not os.path.exists(TEMPLATE):
        print(f"❌ Master template not found: {TEMPLATE}")
        print("   Run: copy new_mel_template.html → 04_Tools/mel_master_template.html")
        exit(1)

    print("🔧 Building HTML...")
    rendered = build(CAMPAIGN)

    print("🔍 Verifying replacements...")
    warnings = verify_replacements(rendered, CAMPAIGN)
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(w)
    else:
        print("  ✅ All replacements successful.")

    print("💾 Saving output...")
    out = save(rendered, CAMPAIGN)
    print(f"\n✅ Done!\n   Output: {out}\n")
    print("   Next steps:")
    print("   1. Open the HTML file in your browser to preview.")
    print("   2. Update hero_img_1 / hero_img_2 with your Klaviyo CDN URLs.")
    print("   3. Once approved, upload via Klaviyo MCP.")
    print()
