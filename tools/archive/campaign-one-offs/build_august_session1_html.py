#!/usr/bin/env python3
"""Build local preview HTML for the first five August 2026 campaigns."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "production" / "html-output" / "2026-08"
ASSET_PREFIX = "../../assets/2026-08"

HEADER_IMAGE = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a91ce3e7-44ab-42dc-a9e6-c3dc74b6f3bf.jpeg"
FOOTER_LOGO = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/82cac524-3eb2-4807-a508-af61cee50920.png"
SOCIAL = {
    "Facebook": (
        "https://www.facebook.com/depologyskincare",
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a8ca6d02-61db-4641-bc0e-cbe61d23d563.png",
    ),
    "Instagram": (
        "https://www.instagram.com/depologyskincare/",
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/b2baf081-c148-44a5-9793-96be804b238f.png",
    ),
    "TikTok": (
        "https://www.tiktok.com/@depology",
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/df012502-6c20-496b-b7eb-db6c6c603e3b.png",
    ),
    "Pinterest": (
        "https://www.pinterest.co/depologyskincare/",
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/8149ca4d-d368-4ec0-ab45-8b6d815399c8.png",
    ),
    "YouTube": (
        "https://www.youtube.com/c/DepologySkincare",
        "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/803eb370-a807-4966-9f69-7cbf9e73a61b.png",
    ),
}

IMG = {
    "eye_cream": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/17182a51-02dc-4114-8b61-d82e29c46bcb.png",
    "matriplex": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/420e0d8e-091d-4a94-ad76-e4c2bea97c46.png",
    "mps": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/160b6da8-e5a3-4202-bcef-a511922d5954.png",
    "night_patch": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fb01a6c6-6cdf-4159-b40b-9f605f71ab65.png",
    "forehead": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/6df074e5-4930-49b2-8c4f-052336c9a7be.png",
    "triple_lipid": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/f11a370d-d5dc-426a-90b0-1ec12a1f8c85.png",
    "cleansing_balm": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/63b261a2-9e8a-403f-8343-cde631ec3b49.png",
    "m3k": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/44a0bdde-9c05-4c2b-854b-fe92895a2a6f.png",
    "eye_microdart": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/bdb87085-8617-43d8-be9b-f2cc405c16d1.png",
}


CAMPAIGNS = [
    {
        "filename": "20260803_Face_Eye_Peptide_Firming_Duo.html",
        "internal": "Verify bundle inventory and the $79 / $114 display pricing before send.",
        "preview": "Daily eye-area hydration and a nourishing peptide finish for the face—paired for $79.",
        "hero_image": "20260803_face_eye_duo_hero_v1.png",
        "hero_alt": "Face and Eye Peptide Firming Duo",
        "hero_link": "https://www.depology.com/products/face-eye-peptide-firming-duo",
        "headline": "A Considered Pair for Face + Eyes",
        "subline1": "Daily care for two zones",
        "subline2": "Eye hydration + face moisture",
        "hero_cta": "DISCOVER THE DUO",
        "body_headline": "Two areas, two roles",
        "body": [
            "Your eye area and the rest of your face do not always need the same finish. This duo gives under-eyes a daily hydration-focused cream and gives your face a nourishing peptide seal.",
            "The Face & Eye Peptide Firming Duo pairs Peptide Complex Eye Cream with Matriplex™ Peptide Intense Cream for $79, a $35 saving versus purchasing both separately. Use them AM or PM after serum.",
        ],
        "note_title": "HOW TO LAYER",
        "note_items": [
            "Apply eye cream after eye serum, AM and PM.",
            "Use Matriplex™ after serum as your face seal.",
        ],
        "section_title": "ONE ROUTINE, CLEAR ROLES",
        "section_subtitle": "Face + eye value · Expression support · PM eye hydration",
        "products": [
            {
                "role": "01 — Face + Eye Value",
                "badge": "BUNDLE SAVING",
                "name": "Face & Eye Peptide Firming Duo",
                "description": "Peptide Complex Eye Cream plus Matriplex™ Peptide Intense Cream: daily eye hydration and a nourishing face finish, bundled at $79.",
                "cta": "SHOP THE DUO",
                "link": "https://www.depology.com/products/face-eye-peptide-firming-duo",
                "images": [IMG["eye_cream"], IMG["matriplex"]],
            },
            {
                "role": "02 — Expression Support",
                "name": "Peptide Complex 10% Argireline™ Serum",
                "description": "Add this lightweight AM/PM serum before cream where expression lines are most visible, including forehead and around the eyes.",
                "cta": "SHOP MPS SERUM",
                "link": "https://depology.com/products/argireline-anti-wrinkle-serum",
                "images": [IMG["mps"]],
            },
            {
                "role": "03 — PM Eye Hydration",
                "name": "Replenishing Night Under Eye Patch",
                "description": "Choose a hydrogel patch night when your under-eyes want extra hydration and comfort; 60 patches provide 30 uses.",
                "cta": "SHOP NIGHT PATCHES",
                "link": "https://depology.com/products/replenishing-night-under-eye-patch",
                "images": [IMG["night_patch"]],
            },
        ],
        "closing": "Start with the two areas you see every day, then keep the routine easy enough to repeat.",
        "final_cta": "BUILD YOUR DUO",
        "final_link": "https://www.depology.com/products/face-eye-peptide-firming-duo",
    },
    {
        "filename": "20260805_Forehead_Micro_Dart_Value.html",
        "internal": "Verify the live Forehead Patch price and inventory before send. Recheck the Triple Lipid sale status before retaining its ON SALE badge.",
        "preview": "Four targeted patches with 0.1% retinol and peptides—use one every 2–3 nights for a simple forehead routine.",
        "hero_image": "20260805_forehead_value_hero_v3.png",
        "hero_alt": "Four Retinol Forehead Micro Dart Patches",
        "hero_link": "https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches",
        "headline": "One zone. Four focused nights.",
        "subline1": "0.1% retinol + peptides",
        "subline2": "A simple two-week format",
        "hero_cta": "EXPLORE THE PATCH",
        "body_headline": "Make forehead care simpler",
        "body": [
            "Forehead lines can be the first lines you notice, yet a full-face active routine is not always the routine you want. These self-dissolving micro-darts focus only on the forehead.",
            "Each box holds four patches with 0.1% retinol, Argireline™ and other peptides. Apply to clean, dry skin every 2–3 nights; the micro-darts deliver the formula into the skin’s surface layers for a smoother-looking forehead.",
            "Use daytime sunscreen. A brief adjustment period with mild redness or slight peeling may occur. If sensitive, begin at the lower end of the every-2–3-night schedule; discontinue if irritation persists.",
        ],
        "note_title": "RETINOL USE NOTE",
        "note_items": [
            "Apply sunscreen during the daytime while using this product.",
            "An adjustment period may occur: mild redness or slight peeling can happen at first and typically settles within a few uses.",
            "If your skin is sensitive, begin at the lower end of the every-2–3-night schedule. Do not combine on the same night with other retinoids, high-strength AHA/BHA, or pure vitamin C. Discontinue use if irritation persists.",
        ],
        "section_title": "TARGET, SUPPORT, SEAL",
        "section_subtitle": "Forehead focus · Daily zone support · Recovery-night seal",
        "products": [
            {
                "role": "01 — The Forehead Focus",
                "name": "Deepcare+® Retinol Forehead Micro Dart Patches",
                "description": "Four self-dissolving micro-dart patches with 0.1% retinol and peptides for the appearance of set-in forehead lines.",
                "cta": "SHOP FOREHEAD PATCH",
                "link": "https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches",
                "images": [IMG["forehead"]],
            },
            {
                "role": "02 — Daily Zone Support",
                "name": "Peptide Complex 10% Argireline™ Serum",
                "description": "A lightweight AM/PM option for smoother-looking skin in high-movement areas, including the forehead and eye area.",
                "cta": "SHOP MPS SERUM",
                "link": "https://depology.com/products/argireline-anti-wrinkle-serum",
                "images": [IMG["mps"]],
            },
            {
                "role": "03 — Recovery-Night Seal",
                "badge": "ON SALE",
                "name": "Triple Lipid + Q10 Moisturizing Treatment RICH",
                "description": "Use as the rich final moisturizing step on non-patch or recovery nights when your skin wants lipid-focused comfort.",
                "cta": "SHOP TRIPLE LIPID",
                "link": "https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich",
                "images": [IMG["triple_lipid"]],
            },
        ],
        "closing": "Target the forehead on a measured schedule, and let the rest of your routine stay uncomplicated.",
        "final_cta": "SEE YOUR FOREHEAD PLAN",
        "final_link": "https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches",
    },
    {
        "filename": "20260807_Cleansing_Balm_18_Value.html",
        "internal": "Leon verified $18 versus $36 on 2026-07-27. Recheck live Shopify price, regular price, and inventory immediately before send. Recheck the Triple Lipid sale status. Remove or update prices and ON SALE badges if they no longer match.",
        "preview": "Remove makeup and sunscreen without the tight after-feel—Opuntia-C™ Balm is currently $18.",
        "hero_image": "20260807_cleansing_balm_value_hero_v1.png",
        "hero_alt": "Opuntia-C Relief Cleansing Balm",
        "hero_link": "https://depology.com/products/opuntia-c-relief-cleansing-balm",
        "headline": "A Softer Way to Begin",
        "subline1": "Melt makeup and sunscreen",
        "subline2": "Leave skin feeling comfortable",
        "hero_cta": "DISCOVER THE BALM",
        "body_headline": "Start soft, not stripped",
        "body": [
            "Makeup, sunscreen and surface buildup can make your evening cleanse feel like a trade-off: thorough removal or a comfortable finish. A balm lets you begin with both in mind.",
            "Opuntia-C™ Relief Cleansing Balm melts away makeup and sunscreen with cactus extract, plant oils and squalane. Massage onto dry skin and rinse with lukewarm water. It is currently $18 versus $36.",
        ],
        "note_title": "",
        "note_items": [],
        "section_title": "FROM CLEANSE TO SEAL",
        "section_subtitle": "Gentle start · Hydration layer · Rich finish",
        "products": [
            {
                "role": "01 — The Gentle Start",
                "badge": "ON SALE",
                "name": "Opuntia-C™ Relief Cleansing Balm",
                "description": "Melt away makeup, sunscreen and surface buildup while keeping your cleanse comfortable. Currently $18 versus $36; verify before send.",
                "cta": "SHOP THE BALM",
                "link": "https://depology.com/products/opuntia-c-relief-cleansing-balm",
                "images": [IMG["cleansing_balm"]],
            },
            {
                "role": "02 — The Hydration Layer",
                "name": "Matrixyl® 3000 Collagen Serum",
                "description": "After cleansing, add this AM/PM peptide serum to support hydration, plumpness and smoother-looking skin.",
                "cta": "SHOP M3K SERUM",
                "link": "https://depology.com/products/depology-matrixyl-3000-serum",
                "images": [IMG["m3k"]],
            },
            {
                "role": "03 — The Rich Finish",
                "badge": "ON SALE",
                "name": "Triple Lipid + Q10 Moisturizing Treatment RICH",
                "description": "Finish a PM routine with a rich lipid moisturizer that helps seal in your serum and support lasting comfort.",
                "cta": "SHOP TRIPLE LIPID",
                "link": "https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich",
                "images": [IMG["triple_lipid"]],
            },
        ],
        "closing": "When your first step feels comfortable, the rest of your evening routine has a better place to begin.",
        "final_cta": "START WITH THE BALM",
        "final_link": "https://depology.com/products/opuntia-c-relief-cleansing-balm",
    },
    {
        "filename": "20260810_Forehead_High_Intent_Followup.html",
        "internal": "High-intent non-buyers only. Suppress Forehead Patch purchasers before scheduling. Verify live price and inventory. Keep the Forehead Patch as the primary purchase CTA.",
        "preview": "Four patches, about two weeks, one forehead zone: see the schedule, formula, and the alternative formats.",
        "hero_image": "20260810_forehead_followup_hero_v2.png",
        "hero_alt": "Four-patch Forehead care decision guide",
        "hero_link": "https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches",
        "headline": "Four patches. A clear plan.",
        "subline1": "About two weeks of use",
        "subline2": "One focused forehead format",
        "hero_cta": "SEE THE DETAILS",
        "body_headline": "Is this your next step?",
        "body": [
            "If you looked at the Forehead Patch but paused, the practical answer is simple: one box contains four self-dissolving patches, intended for one targeted zone over about two weeks.",
            "Use one on clean, dry skin every 2–3 nights and leave it on for at least one hour. Its 0.1% retinol and peptide formula is for people who want focused forehead care rather than another full-face step.",
            "Use daytime sunscreen. A brief adjustment period with mild redness or slight peeling may occur. If sensitive, begin at the lower end of the every-2–3-night schedule; discontinue if irritation persists.",
        ],
        "note_title": "RETINOL USE NOTE",
        "note_items": [
            "Apply sunscreen during the daytime while using this product.",
            "An adjustment period may occur: mild redness or slight peeling can happen at first and typically settles within a few uses.",
            "If your skin is sensitive, begin at the lower end of the every-2–3-night schedule. Do not combine on the same night with other retinoids, high-strength AHA/BHA, or pure vitamin C. Discontinue use if irritation persists.",
        ],
        "section_title": "CHOOSE YOUR FORMAT",
        "section_subtitle": "Forehead patch · Daily serum · Eye-zone patch",
        "products": [
            {
                "role": "01 — Your Forehead Option",
                "name": "Deepcare+® Retinol Forehead Micro Dart Patches",
                "description": "Choose four focused patch nights for the look of set-in forehead lines, with 0.1% retinol and peptides delivered into the skin’s surface layers.",
                "cta": "SHOP FOREHEAD PATCH",
                "link": "https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches",
                "images": [IMG["forehead"]],
            },
            {
                "role": "02 — Daily Serum Option",
                "name": "Peptide Complex 10% Argireline™ Serum",
                "description": "Prefer an everyday serum? Use this lightweight AM/PM formula on the forehead and other high-movement areas.",
                "cta": "VIEW SERUM OPTION",
                "link": "https://depology.com/products/argireline-anti-wrinkle-serum",
                "images": [IMG["mps"]],
            },
            {
                "role": "03 — Eye Zone Option",
                "name": "Deepcare+ Micro-dart Eye Patch",
                "description": "If your priority is under-eye lines and crow’s feet, choose the dedicated micro-dart patch for that smaller eye-area zone.",
                "cta": "VIEW EYE OPTION",
                "link": "https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0",
                "images": [IMG["eye_microdart"]],
            },
        ],
        "closing": "You do not need a larger routine to focus on one concern—just the format that fits the zone you want to prioritize.",
        "final_cta": "SHOP FOREHEAD PATCH",
        "final_link": "https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches",
    },
    {
        "filename": "20260812_Peptide_Serum_Duo_Value.html",
        "internal": "Verify bundle inventory and the $80 / $89 display pricing before send.",
        "preview": "One serum supports all-over hydration; the other focuses on high-movement zones—together for $80.",
        "hero_image": "20260812_peptide_serum_duo_hero_v1.png",
        "hero_alt": "Matrixyl and Argireline Peptide Serum Duo",
        "hero_link": "https://www.depology.com/products/prevent-and-rewind-serum-duo",
        "headline": "Two Peptides. Two Clear Roles.",
        "subline1": "All-over hydration",
        "subline2": "Targeted expression support",
        "hero_cta": "DISCOVER THE DUO",
        "body_headline": "Not every line moves alike",
        "body": [
            "Some concerns call for an all-over hydration layer; others show most in the areas that move with every expression. One serum can be your foundation, while the other gives those zones extra attention.",
            "The Peptide Serum Duo combines Matrixyl® 3000 Collagen Serum with Peptide Complex 10% Argireline™ Serum for $80, a $9 saving. Apply the targeted serum first, then follow with Matrixyl® AM and PM.",
        ],
        "note_title": "HOW TO LAYER",
        "note_items": [
            "Apply MPS first to forehead, eye area and smile lines.",
            "Follow with Matrixyl® serum, then one moisturizing cream.",
        ],
        "section_title": "LAYER BY ROLE, NOT GUESSWORK",
        "section_subtitle": "Two-serum start · Peptide seal · Daily eye comfort",
        "products": [
            {
                "role": "01 — The Two-Serum Start",
                "badge": "BUNDLE SAVING",
                "name": "Peptide Serum Duo",
                "description": "Matrixyl® 3000 Collagen Serum plus Peptide Complex 10% Argireline™ Serum: hydration support and focused expression-zone care for $80.",
                "cta": "SHOP THE DUO",
                "link": "https://www.depology.com/products/prevent-and-rewind-serum-duo",
                "images": [IMG["m3k"], IMG["mps"]],
            },
            {
                "role": "02 — The Peptide Seal",
                "name": "Matriplex™ Peptide Intense Cream",
                "description": "Follow your serums with this 8% Matrixyl Complex cream to moisturize, add comfort and finish the peptide-focused routine.",
                "cta": "SHOP MATRIPLEX",
                "link": "https://depology.com/products/tri-active-matrixyl-complex-cream",
                "images": [IMG["matriplex"]],
            },
            {
                "role": "03 — Daily Eye Comfort",
                "name": "Peptide Complex Eye Cream",
                "description": "Add a simple AM/PM eye cream for hydration, comfort and a smoother-looking under-eye appearance alongside your face serums.",
                "cta": "SHOP EYE CREAM",
                "link": "https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream",
                "images": [IMG["eye_cream"]],
            },
        ],
        "closing": "Give your whole face a dependable peptide layer, then give high-movement areas their own targeted step.",
        "final_cta": "BUILD YOUR SERUM DUO",
        "final_link": "https://www.depology.com/products/prevent-and-rewind-serum-duo",
    },
]


def button(label, link, large=False):
    padding = "16px 36px" if large else "11px 18px"
    size = "14px" if large else "12px"
    return f"""
<table border="0" cellpadding="0" cellspacing="0" role="presentation"><tr>
<td bgcolor="#000000" style="border-radius:2px;mso-padding-alt:{padding};">
<a href="{escape(link)}" target="_blank" style="display:inline-block;color:#FFFFFF;background:#000000;font-family:'Century Gothic',Arial,sans-serif;font-size:{size};font-weight:700;letter-spacing:1.5px;padding:{padding};text-decoration:none;border-radius:2px;">{escape(label)}</a>
</td></tr></table>"""


def product_images(product):
    images = product["images"]
    width = 140 if len(images) == 1 else 90
    max_width = "100%" if len(images) == 1 else "46%"
    return "".join(
        f'<img src="{escape(src)}" alt="{escape(product["name"])}" width="{width}" style="display:inline-block;width:{width}px;max-width:{max_width};height:auto;margin:0 2px;vertical-align:middle;"/>'
        for src in images
    )


def product_card(product, last=False):
    bottom = "32px" if last else "8px"
    badge = ""
    if product.get("badge"):
        badge = (
            '<div style="display:inline-block;background:#8F2D2D;color:#FFFFFF;'
            "font-family:'Century Gothic',Arial,sans-serif;font-size:10px;font-weight:700;"
            'letter-spacing:1.3px;text-transform:uppercase;padding:5px 9px;border-radius:2px;'
            f'margin:0 0 9px 0;">{escape(product["badge"])}</div>'
        )
    return f"""
<tr><td style="padding:8px 20px {bottom} 20px;">
<table border="0" cellpadding="0" cellspacing="0" width="100%" style="background:#FFFFFF;border:1px solid #E5E5E5;border-radius:4px;"><tr>
<td valign="middle" class="product-img" width="42%" height="220" style="width:42%;height:220px;padding:0;background:#F5F3EF;text-align:center;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" height="220" style="width:100%;height:220px;background:#F5F3EF;"><tr>
<td align="center" valign="middle" height="220" style="height:220px;padding:8px;">
{product_images(product)}
</td></tr></table>
</td>
<td valign="middle" class="product-copy" style="padding:22px 22px 22px 20px;">
<div style="font-family:'Century Gothic',Arial,sans-serif;font-size:11px;color:#888888;letter-spacing:1.6px;text-transform:uppercase;margin-bottom:6px;">{escape(product["role"])}</div>
{badge}
<div style="font-family:'Century Gothic',Arial,sans-serif;font-size:16px;font-weight:700;color:#000000;line-height:1.35;margin-bottom:8px;">{escape(product["name"])}</div>
<p style="font-family:'Century Gothic',Arial,sans-serif;font-size:13px;color:#444444;line-height:1.55;margin:0 0 12px 0;">{escape(product["description"])}</p>
{button(product["cta"], product["link"])}
</td>
</tr></table>
</td></tr>"""


def social_links():
    return "".join(
        f'<a href="{escape(url)}" style="display:inline-block;padding-right:9px;"><img alt="{escape(name)}" src="{escape(icon)}" width="27" style="width:27px;"/></a>'
        for name, (url, icon) in SOCIAL.items()
    )


def render(c):
    paragraphs = "".join(
        f'<p style="font-family:\'Century Gothic\',Arial,sans-serif;font-size:16px;color:#333333;line-height:1.65;margin:0;{"padding-bottom:14px;" if i < len(c["body"]) - 1 else ""}text-align:center;">{escape(text)}</p>'
        for i, text in enumerate(c["body"])
    )
    cards = "".join(product_card(p, i == len(c["products"]) - 1) for i, p in enumerate(c["products"]))
    return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>{escape(c["headline"])}</title>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<style>
body {{ margin:0; padding:0; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; background:#DDDDDD; }}
table, td {{ border-collapse:collapse; mso-table-lspace:0; mso-table-rspace:0; }}
img {{ border:0; height:auto; line-height:100%; outline:none; text-decoration:none; -ms-interpolation-mode:bicubic; max-width:100%; }}
p {{ display:block; margin:0; padding:0; }}
@media only screen and (max-width:480px) {{
  .container {{ width:100% !important; }}
  .stack {{ display:block !important; width:100% !important; box-sizing:border-box !important; }}
  .hero-h {{ font-size:28px !important; line-height:1.2 !important; }}
  .product-img {{ display:block !important; width:auto !important; height:240px !important; padding:0 !important; background:#F5F3EF !important; }}
  .product-img > table, .product-img > table td {{ height:240px !important; background:#F5F3EF !important; }}
  .product-img > table td {{ padding:10px 8px !important; }}
  .product-img img {{ height:auto !important; }}
  .product-copy {{ display:block !important; width:auto !important; padding:14px 24px 24px 24px !important; text-align:center !important; }}
  .product-copy table {{ margin:0 auto !important; }}
}}
</style>
</head>
<body style="word-spacing:normal;background:#DDDDDD;margin:0;padding:0;">
<!-- INTERNAL SEND CHECK: {escape(c["internal"])} -->
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">{escape(c["preview"])}</div>
<div style="background:#DDDDDD;padding:20px 0;">

<!-- BLOCK 1: LOGO -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" width="600" style="width:600px;max-width:600px;background:#FFFFFF;">
<tr><td align="center" style="padding:0;">
<a href="https://depology.com/" style="text-decoration:none;display:block;"><img alt="Depology" src="{HEADER_IMAGE}" width="600" style="display:block;width:100%;height:auto;"/></a>
</td></tr>

<!-- BLOCK 2: HERO IMAGE -->
<tr><td align="center" style="padding:0;">
<a href="{escape(c["hero_link"])}" style="text-decoration:none;display:block;"><img alt="{escape(c["hero_alt"])}" src="{ASSET_PREFIX}/{escape(c["hero_image"])}" width="600" style="display:block;width:100%;height:auto;"/></a>
</td></tr>

<!-- BLOCK 2B: HERO COPY -->
<tr><td align="center" style="padding:30px 24px 8px;background:#FFFFFF;">
<h1 class="hero-h" style="font-family:Georgia,'Times New Roman',serif;font-size:40px;font-weight:400;line-height:1.15;color:#000000;margin:0;text-align:center;">{escape(c["headline"])}</h1>
</td></tr>
<tr><td align="center" style="padding:8px 50px 16px;background:#FFFFFF;">
<p style="font-family:'Century Gothic',Arial,sans-serif;font-size:18px;color:#333333;line-height:1.5;text-align:center;">{escape(c["subline1"])}<br/>{escape(c["subline2"])}</p>
</td></tr>
<tr><td align="center" style="padding:8px 24px 32px;background:#FFFFFF;">{button(c["hero_cta"], c["hero_link"])}</td></tr>

<!-- BLOCK 3: BODY COPY -->
<tr><td style="background:#FFFFFF;padding:0 24px;"><div style="border-top:1px solid #DDDDDD;font-size:1px;line-height:1px;">&nbsp;</div></td></tr>
<tr><td align="center" style="padding:32px 24px 8px;background:#FFFFFF;">
<div style="font-family:'Century Gothic',Arial,sans-serif;font-size:26px;font-weight:700;line-height:1.3;color:#000000;text-align:center;">{escape(c["body_headline"])}</div>
</td></tr>
<tr><td style="padding:12px 50px 36px;background:#FFFFFF;">{paragraphs}</td></tr>
</table>

<!-- BLOCK 5: PRODUCT CARDS -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" width="600" style="width:600px;max-width:600px;background:#FFFFFF;">
<tr><td align="center" style="padding:40px 30px 8px;">
<div style="font-family:'Century Gothic',Arial,sans-serif;font-size:22px;font-weight:700;letter-spacing:1.8px;line-height:1.3;color:#000000;text-align:center;">{escape(c["section_title"])}</div>
<div style="font-family:Georgia,'Times New Roman',serif;font-size:14px;font-style:italic;color:#666666;line-height:1.4;text-align:center;margin-top:7px;">{escape(c["section_subtitle"])}</div>
</td></tr>
{cards}
</table>

<!-- BLOCK 6: CLOSING -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" width="600" style="width:600px;max-width:600px;background:#FFFFFF;">
<tr><td align="center" style="padding:40px 42px 12px;">
<p style="font-family:Georgia,'Times New Roman',serif;font-size:17px;font-style:italic;color:#222222;line-height:1.65;text-align:center;">{escape(c["closing"])}</p>
</td></tr>
<tr><td align="center" style="padding:20px 30px 44px;">{button(c["final_cta"], c["final_link"], large=True)}</td></tr>
</table>

<!-- BLOCK 7: FOOTER -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" width="600" style="width:600px;max-width:600px;background:#000000;">
<tr>
<td valign="top" class="stack" style="width:50%;padding:27px 18px 0;vertical-align:top;">
<a href="{{{{ organization.url }}}}" style="text-decoration:none;"><img alt="{{{{ organization.name }}}}" src="{FOOTER_LOGO}" width="230" style="display:block;width:230px;max-width:100%;height:auto;"/></a>
<div style="padding:14px 0 0;">{social_links()}</div>
</td>
<td valign="top" class="stack" style="width:50%;padding:25px 18px;vertical-align:top;">
<div style="font-family:'Century Gothic',Arial,sans-serif;font-size:14px;font-weight:500;color:#F7F7F7;text-transform:uppercase;line-height:1.4;">&copy; {{{{ organization.name }}}},<br/><span style="font-size:10px;color:#D9D9D7;">{{{{ organization.full_address }}}}</span><br/><br/><br/><a href="{{% unsubscribe_link %}}" style="color:#FFFFFF;text-decoration:underline;font-weight:500;">UNSUBSCRIBE</a></div>
</td>
</tr>
</table>

</div>
</body>
</html>
"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for campaign in CAMPAIGNS:
        output = OUT_DIR / campaign["filename"]
        output.write_text(render(campaign), encoding="utf-8")
        print(f"Built {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
