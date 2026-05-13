"""
Memorial Sale 2026 — Render all 8 Memorial emails to HTML.

Templates:
  A: 主题型 (white-base + STAR badge + 4-card 2×2 grid)
     Used by: 5/20 AM, 5/20 PM, 5/21, 5/22, 5/23, 5/24 AM
  B: 红警示型 (red banner top + tilted hero + $X ONLY price-anchored CTAs)
     Used by: 5/24 PM
  C: 收尾型 (LAST CHANCE overlay text + mixed-CTA cards)
     Used by: 5/25

Hero images left as grey placeholder divs (Leon generates separately).
Output: production/html-output/*.html
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).parent.parent
OUT_DIR = ROOT / "production" / "html-output"

# ══════════════════════════════════════════════════════════════════════
# SKU REGISTRY (Memorial Sale 2026 specific images + URLs)
# Source: knowledge/visual/Memorial Sale Product Images.md
# ══════════════════════════════════════════════════════════════════════

IMG_BASE = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images"

SKU = {
    "m3k_3f2": {
        "name": "Matrixyl® 3000 Collagen Serum",
        "tag": "Target Static Wrinkles",
        "rating_count": "(2000+)",
        "volume": "30ml*3",
        "img": f"{IMG_BASE}/19ffd3a2-1cee-4a87-96f2-4dda1a5878d2.jpeg",
        "alt": "Matrixyl 3000 Collagen Serum 3 for 2",
        "slug": "offer-matrixyl-r-3000-triple-bundle",
    },
    "argireline_3f2": {
        "name": "Peptide Complex Argireline™ Serum",
        "tag": "Target Dynamic Wrinkles",
        "rating_count": "(800+)",
        "volume": "30ml*3",
        "img": f"{IMG_BASE}/922c97bf-7f09-4545-b04d-805354e5b770.jpeg",
        "alt": "Argireline Peptide Complex Serum 3 for 2",
        "slug": "offer-peptide-complex-10-serum-3-for-2",
    },
    "face_eye_duo": {
        "name": "Face &amp; Eye Peptide Firming Duo",
        "tag": "Smooth &amp; Firm — Cream Duo",
        "rating_count": "(500+)",
        "volume": "50ml + 15ml",
        "img": f"{IMG_BASE}/85a9714d-4d1c-45c9-8b50-3bd6b040c1be.jpeg",
        "alt": "Face and Eye Peptide Firming Duo",
        "slug": "face-eye-peptide-firming-duo",
    },
    "matriplex": {
        "name": "Matriplex™ Peptide Intense Cream",
        "tag": "Intensive Peptide Care",
        "rating_count": "(1500+)",
        "volume": "50ml",
        "img": f"{IMG_BASE}/3a22afe6-fe59-4f2d-953e-bacf46f4bfc5.jpeg",
        "alt": "Matriplex Peptide Intense Cream",
        "slug": "offer-matriplex-peptide-intense-cream-copy",
    },
    "pec": {
        "name": "Peptide Complex Wrinkle Defense Eye Cream",
        "tag": "Smooth Eye Wrinkles",
        "rating_count": "",
        "volume": "15ml",
        "img": f"{IMG_BASE}/73fc6218-3682-4111-89bb-e18f46fbfa46.jpeg",
        "alt": "Peptide Complex Wrinkle Defense Eye Cream",
        "slug": "offer-peptide-complex-wrinkle-defense-eye-cream-copy",
    },
    "mop": {
        "name": "Deepcare+® MicroOperator Boosting Cream",
        "tag": "Boosts Skin Renewal &amp; Radiance",
        "rating_count": "",
        "volume": "50ml",
        "img": f"{IMG_BASE}/784eeb0d-b743-4f5d-b31c-c20f068bcefc.jpeg",
        "alt": "Deepcare MicroOperator Boosting Cream",
        "slug": "offer-deepcare-%C2%AE-microoperator-boosting-cream-beginner-us-exclusive-only",
    },
    "tlq": {
        "name": "Triple Lipid + Q10 RICH",
        "tag": "Support Skin Barrier",
        "rating_count": "",
        "volume": "50ml",
        "img": f"{IMG_BASE}/3c2e2c94-913d-4568-afe0-85347f641eb9.jpeg",
        "alt": "Triple Lipid Q10 Revive Moisturizing Treatment RICH",
        "slug": "offer-triple-lipid-q10-revive-moisturizing-treatment-rich",
    },
    "bakuchiol": {
        "name": "Bakuchiol Smoothing Serum Stick",
        "tag": "Improve Fine Lines &amp; Wrinkles",
        "rating_count": "",
        "volume": "10g",
        "img": f"{IMG_BASE}/996a4cfa-1508-40d8-8866-10419c175a92.jpeg",
        "alt": "Bakuchiol Smoothing Serum Stick",
        "slug": "bakuchiol-smoothing-serum-stick",
    },
    "m2": {
        "name": "Deepcare+® Micro-dart Patches",
        "tag": "Now Stronger — Retinol Inside · 16 pairs",
        "rating_count": "(3000+)",
        "volume": "8 weeks supply",
        "img": f"{IMG_BASE}/9e3d370f-de96-4240-88b2-3f4f229b084f.jpeg",
        "alt": "Deepcare Serum-Infused Micro-Dart Patches with Retinol",
        "slug": "offer-deepcare-serum-infused-micro-dart-patches",
    },
    "pat": {
        "name": "Peptide Activation Trio",
        "tag": "Smooth &amp; Youthful Glow — 3-Step Activation",
        "rating_count": "(NEW)",
        "volume": "3 items",
        "img": f"{IMG_BASE}/42ce5493-c458-47db-b07e-ea974578f7f5.jpeg",
        "alt": "Peptide Activation Trio Bundle",
        "slug": "peptide-activation-trio",
    },
    "static_duo": {
        "name": "Static Wrinkle Repair Duo",
        "tag": "Deep Wrinkle Fix · M1 + M3K",
        "rating_count": "(1500+)",
        "volume": "2 items",
        "img": f"{IMG_BASE}/68e2e5d9-ce35-47f7-b8ac-1b1295156323.jpeg",
        "alt": "Static Wrinkle Repair Duo M1 plus M3K",
        "slug": "static-wrinkle-repair-duo",
    },
    "dynamic_duo": {
        "name": "Dynamic Wrinkle Defense Duo",
        "tag": "Early Line Defense · M1 + Argireline",
        "rating_count": "(1500+)",
        "volume": "2 items",
        "img": f"{IMG_BASE}/9856be7d-aff5-491e-b26c-4db02e5c5104.jpeg",
        "alt": "Dynamic Wrinkle Defense Duo M1 plus Argireline",
        "slug": "dynamic-wrinkle-defense-duo",
    },
    "night_eye": {
        "name": "Replenishing Night Under Eye Patch",
        "tag": "Deep Overnight Care",
        "rating_count": "",
        "volume": "60 patches",
        "img": f"{IMG_BASE}/ed2bfcb0-8b14-4cf2-ad3e-5b26f457626c.jpeg",
        "alt": "Replenishing Night Under Eye Patch",
        "slug": "offer-replenishing-night-under-eye-patch",
    },
}


def product_url(sku_key, use_mem10):
    slug = SKU[sku_key]["slug"]
    if use_mem10:
        return f"https://depology.com/discount/MEM10?redirect=/products/{slug}"
    return f"https://depology.com/products/{slug}"


def sale_page_url(use_mem10):
    if use_mem10:
        return "https://depology.com/discount/MEM10?redirect=/pages/memorial-2026-sale"
    return "https://depology.com/pages/memorial-2026-sale"


# ══════════════════════════════════════════════════════════════════════
# HTML BLOCKS
# ══════════════════════════════════════════════════════════════════════

def html_head(title):
    return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
<title>{title}</title>
<!--[if !mso]><!-->
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<!--<![endif]-->
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<![endif]-->
<style>
a:not([name]) {{color:#444;text-decoration:underline}}
a:link {{color:#444;text-decoration:underline}}
a:visited {{color:#444;text-decoration:underline}}
a:active {{color:#444;text-decoration:underline}}
a:hover {{color:#444;text-decoration:underline}}
</style>
<style>
@import url(https://static-forms.klaviyo.com/fonts/api/v1/XbHdQN/custom_fonts.css);
#outlook a {{ padding: 0 }}
body {{ margin: 0; padding: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100% }}
table, td {{ border-collapse: collapse; mso-table-lspace: 0; mso-table-rspace: 0 }}
img {{ border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; max-width: 100% }}
p {{ display: block; margin: 0 }}
@media only screen and (min-width: 480px) {{
  .mj-column-per-100 {{ width: 100% !important; max-width: 100% }}
  .mj-column-per-50 {{ width: 50% !important; max-width: 50% }}
}}
@media only screen and (max-width: 480px) {{
  div.kl-row.colstack div.kl-column {{ display: block !important; width: 100% !important }}
  .mem-card-col {{ display: block !important; width: 100% !important; max-width: 100% !important }}
  .mem-card-wrap {{ padding: 0 16px 12px 16px !important }}
}}
.kl-button a {{ display: block !important }}
.root-container {{ background-repeat: repeat !important; background-size: auto !important; background-position: left top !important }}
.root-container-spacing {{ padding-top: 25px !important; padding-bottom: 20px !important; font-size: 0 !important }}
.content-padding {{ padding-left: 0 !important; padding-right: 0 !important }}
.content-padding.kl-first {{ padding-top: 0 !important }}
.content-padding.kl-last {{ padding-bottom: 0 !important }}
h1 {{ color:#1E3A8A; font-family:'Times New Roman', Times, Baskerville, Georgia, serif; font-size:40px; font-weight:700; line-height:1.15; letter-spacing:0.5px; margin:0; text-align:center }}
@media only screen and (max-width: 480px) {{ h1 {{ font-size:28px !important; line-height:1.25 !important }} }}
@media only screen and (max-width: 480px) {{
  .root-container {{ width: 100% !important }}
  .root-container-spacing {{ padding: 0 !important }}
  .kl-text {{ padding-right: 18px !important; padding-left: 18px !important }}
}}
</style>
</head>
<body style="word-spacing:normal;background-color:#DDDDDD;">
<div class="root-container" id="bodyTable" style="background-color:#DDDDDD;">
<div class="root-container-spacing">
"""


LOGO_BLOCK = """<!-- Logo -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td align="center" style="font-size:0px;word-break:break-word;">
<a href="https://depology.com/" style="color:#444;text-decoration:underline;display:block">
<img alt="Depology" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a91ce3e7-44ab-42dc-a9e6-c3dc74b6f3bf.jpeg" style="display:block;outline:none;text-decoration:none;height:auto;font-size:13px;width:100%;" width="600"/>
</a>
</td>
</tr></tbody>
</table>
"""


def hero_placeholder_a(badge_text, hero_link):
    """Template A: white-base hero with STAR badge text overlay note in placeholder"""
    return f"""<!-- Hero Image PLACEHOLDER — Leon to replace with AI-generated 600x400 image (multi-SKU still life + STAR badge text "{badge_text}" built into image) -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td align="center" style="font-size:0px;word-break:break-word;padding:0;">
<a href="{hero_link}" style="color:#444;text-decoration:underline;display:block">
<!-- REPLACE THIS DIV WITH: <img src="HERO_IMAGE_URL_HERE" alt="Memorial Day Sale" width="600" style="display:block;width:100%;max-width:600px;height:auto;"/> -->
<div style="background:#E8E8E8;width:100%;max-width:600px;height:400px;display:block;text-align:center;line-height:400px;font-family:Helvetica,Arial,sans-serif;font-size:14px;color:#999;font-style:italic;letter-spacing:1px;">
[ HERO IMAGE PLACEHOLDER 600×400 — STAR badge "{badge_text}" ]
</div>
</a>
</td>
</tr></tbody>
</table>
"""


def hero_placeholder_b(banner_line_1, banner_line_2, hero_link):
    """Template B: red banner overlay on top + tilted product hero placeholder"""
    return f"""<!-- Hero Image PLACEHOLDER (Template B) — red banner + tilted product hero. Leon to replace with full 600x400 image including banner text + tilted products. -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td align="center" style="font-size:0px;word-break:break-word;padding:0;">
<a href="{hero_link}" style="color:#444;text-decoration:underline;display:block">
<!-- Red banner mockup (will be part of hero image once Leon generates it) -->
<div style="background:#DC2626;width:100%;max-width:600px;padding:18px 12px;text-align:center;font-family:Helvetica,Arial,sans-serif;color:#FFFFFF;letter-spacing:1px;">
<div style="font-size:24px;font-weight:700;line-height:1.2;">{banner_line_1}</div>
<div style="font-size:16px;font-weight:600;line-height:1.4;margin-top:4px;">{banner_line_2}</div>
</div>
<!-- Tilted hero image placeholder -->
<div style="background:#E8E8E8;width:100%;max-width:600px;height:320px;display:block;text-align:center;line-height:320px;font-family:Helvetica,Arial,sans-serif;font-size:14px;color:#999;font-style:italic;letter-spacing:1px;">
[ HERO IMAGE PLACEHOLDER 600×320 — tilted products + red urgency aesthetic ]
</div>
</a>
</td>
</tr></tbody>
</table>
"""


def hero_placeholder_c(overlay_red, overlay_blue, badge_text, hero_link):
    """Template C: hero with LAST CHANCE red + sub blue overlay text + STAR badge"""
    return f"""<!-- Hero Image PLACEHOLDER (Template C) — Multi-SKU group + STAR badge "{badge_text}" + top overlay text. -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td align="center" style="font-size:0px;word-break:break-word;padding:0;">
<a href="{hero_link}" style="color:#444;text-decoration:underline;display:block">
<!-- Hero placeholder with text-overlay mockup (will be part of generated image) -->
<div style="background:#E8E8E8;width:100%;max-width:600px;height:400px;display:block;text-align:center;font-family:Helvetica,Arial,sans-serif;letter-spacing:1px;position:relative;padding-top:36px;box-sizing:border-box;">
<div style="font-size:38px;font-weight:700;color:#DC2626;line-height:1.0;">{overlay_red}</div>
<div style="font-size:18px;font-weight:700;color:#1E3A8A;line-height:1.4;margin-top:6px;">{overlay_blue}</div>
<div style="font-size:13px;color:#999;font-style:italic;margin-top:60px;">[ HERO IMAGE PLACEHOLDER 600×400 — multi-SKU group + STAR "{badge_text}" ]</div>
</div>
</a>
</td>
</tr></tbody>
</table>
"""


def headline_block(h1_text):
    """Template A/C headline below hero"""
    return f"""<!-- H1 Headline -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td class="kl-text" style="font-size:0px;padding:28px 32px 4px 32px;word-break:break-word;">
<h1>{h1_text}</h1>
</td>
</tr></tbody>
</table>
"""


def lead_block(lead_copy_html, mem10_callout_html=None, primary_cta_text="SHOP MEMORIAL SALE", primary_cta_url=""):
    parts = []
    parts.append(f"""<!-- Lead Copy -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td class="kl-text" style="font-size:0px;padding:24px 40px 8px 40px;word-break:break-word;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:18px;font-weight:500;line-height:1.55;text-align:center;color:#171516;">
{lead_copy_html}
</div>
</td>
</tr></tbody>
</table>
""")
    if mem10_callout_html:
        parts.append(f"""<!-- MEM10 Code Callout -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td class="kl-text" style="font-size:0px;padding:8px 40px 24px 40px;word-break:break-word;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:18px;font-weight:700;line-height:1.55;text-align:center;color:#C8102E;">
{mem10_callout_html}
</div>
</td>
</tr></tbody>
</table>
""")
    parts.append(f"""<!-- Primary CTA -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td align="center" class="kl-button" style="font-size:0px;padding:4px 18px 32px 18px;word-break:break-word;">
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse:separate;line-height:100%;">
<tr>
<td align="center" bgcolor="#000000" role="presentation" style="border:none;border-radius:2px;cursor:auto;mso-padding-alt:16px 64px;background:#000000;" valign="middle">
<a href="{primary_cta_url}" style='color:#FFF;text-decoration:none;display:inline-block;background:#000;font-family:"Aktiv Regular + Bold", Helvetica, Arial, sans-serif;font-size:18px;font-weight:700;line-height:100%;letter-spacing:1.5px;margin:0;padding:16px 64px;border-radius:2px;' target="_blank">
{primary_cta_text}
</a>
</td>
</tr>
</table>
</td>
</tr></tbody>
</table>
""")
    return "".join(parts)


def card_html(sku_key, badge_text, badge_color, price, original, cta_text, cta_url):
    """One product card. badge_color: '#1E3A8A' (blue) or '#C8102E' (red 100-cap/scarcity).
    Note: BEST tag + Dermatologist seal removed per Leon 2026-05-13 feedback.
    Product image fills full card width (820x920 ratio, no L/R padding)."""
    s = SKU[sku_key]
    rating_html = ""
    if s["rating_count"]:
        rating_html = f"""★★★★½ <span style="color:#888;">{s["rating_count"]}</span>"""
    else:
        rating_html = "★★★★½"
    return f"""<td class="mem-card-col" style="width:50%;vertical-align:top;padding:8px;" valign="top">
  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;border:2px solid {badge_color};background:#FFFFFF;">
    <tbody>
      <tr><td align="center" style="background:{badge_color};color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:1.5px;padding:10px 8px;">{badge_text}</td></tr>
      <tr><td style="padding:0;font-size:0;line-height:0;">
        <img alt="{s["alt"]}" src="{s["img"]}" style="display:block;width:100%;height:auto;" width="296"/>
      </td></tr>
      <tr><td align="center" style="font-family:Helvetica,Arial,sans-serif;font-size:11px;color:#666;padding:6px 12px 6px 12px;background:#F5F5F5;line-height:1.4;">{s["tag"]}</td></tr>
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;color:#000;padding:10px 12px 4px 12px;line-height:1.3;">{s["name"]}</td></tr>
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:11px;color:#999;padding:0 12px 4px 12px;">{s["volume"]}</td></tr>
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:11px;color:#1E3A8A;padding:0 12px 4px 12px;">{rating_html}</td></tr>
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:14px;padding:4px 12px 10px 12px;"><span style="color:#C8102E;font-weight:700;">${price}</span> <span style="color:#999;text-decoration:line-through;">${original}</span></td></tr>
      <tr><td align="center" style="background:#000000;padding:0;">
        <a href="{cta_url}" style="display:block;color:#FFF;text-decoration:none;font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:700;letter-spacing:1px;padding:12px 8px;" target="_blank">{cta_text}</a>
      </td></tr>
    </tbody>
  </table>
</td>"""


def grid_2x2(cards_4):
    assert len(cards_4) == 4
    return f"""<!-- ============================================ -->
<!-- SECTION 3: 4-CARD 2x2 PRODUCT GRID           -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:8px 8px 16px 8px;text-align:center;background:#FFFFFF;">

<!-- ROW 1: Card 1 + Card 2 -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
{cards_4[0]}
{cards_4[1]}
</tr></tbody>
</table>

<!-- ROW 2: Card 3 + Card 4 -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
{cards_4[2]}
{cards_4[3]}
</tr></tbody>
</table>

</td>
</tr></tbody>
</table>
</div>
</td></tr></tbody>
</table>
"""


def closing_block(closing_copy_html, secondary_cta_text, secondary_cta_url):
    return f"""<!-- ============================================ -->
<!-- SECTION 4: CLOSING BANNER + SECONDARY CTA    -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#000000;background-color:#000000;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#000000;background-color:#000000;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">

<!-- Closing copy on black -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td class="kl-text" style="font-size:0px;padding:28px 40px 20px 40px;word-break:break-word;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:18px;font-weight:500;line-height:1.55;text-align:center;color:#FFFFFF;">
{closing_copy_html}
</div>
</td>
</tr></tbody>
</table>

<!-- Secondary CTA (white) -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
<tbody><tr>
<td align="center" class="kl-button" style="font-size:0px;padding:0 18px 32px 18px;word-break:break-word;">
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse:separate;line-height:100%;">
<tr>
<td align="center" bgcolor="#FFFFFF" role="presentation" style="border:none;border-radius:2px;cursor:auto;mso-padding-alt:16px 64px;background:#FFFFFF;" valign="middle">
<a href="{secondary_cta_url}" style='color:#000;text-decoration:none;display:inline-block;background:#FFF;font-family:"Aktiv Regular + Bold", Helvetica, Arial, sans-serif;font-size:18px;font-weight:700;line-height:100%;letter-spacing:1.5px;margin:0;padding:16px 64px;border-radius:2px;' target="_blank">
{secondary_cta_text}
</a>
</td>
</tr>
</table>
</td>
</tr></tbody>
</table>

</td>
</tr></tbody>
</table>
</div>
</td>
</tr></tbody>
</table>
</div>
</td></tr></tbody>
</table>
"""


FOOTER_BLOCK = """<!-- ============================================ -->
<!-- FOOTER                                       -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#000000;background-color:#000000;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#000000;background-color:#000000;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div class="content-padding kl-last">
<div class="kl-row colstack" style="display:table;table-layout:fixed;width:100%;">

<div class="kl-column" style="display:table-cell;vertical-align:top;width:50%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr>
<td style="vertical-align:top;padding:27px 18px 0px 18px;">
<a href="https://depology.com/" style="color:#444;text-decoration:underline;display:block">
<img alt="Depology" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/82cac524-3eb2-4807-a508-af61cee50920.png" style="display:block;outline:none;text-decoration:none;height:auto;width:100%;max-width:230px;" width="230"/>
</a>
</td>
</tr></tbody></table>
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr>
<td style="vertical-align:top;padding:9px 30px;">
<div style="width:100%;text-align:left">
<div style="display:inline-block;padding-right:12px;"><a href="https://www.facebook.com/depologyskincare" target="_blank"><img alt="Facebook" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a8ca6d02-61db-4641-bc0e-cbe61d23d563.png" style="width:30px;" width="30"/></a></div>
<div style="display:inline-block;padding-right:12px;"><a href="https://www.instagram.com/depologyskincare/" target="_blank"><img alt="Instagram" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/b2baf081-c148-44a5-9793-96be804b238f.png" style="width:30px;" width="30"/></a></div>
<div style="display:inline-block;padding-right:12px;"><a href="https://www.tiktok.com/@depology" target="_blank"><img alt="TikTok" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/df012502-6c20-496b-b7eb-db6c6c603e3b.png" style="width:30px;" width="30"/></a></div>
<div style="display:inline-block;padding-right:12px;"><a href="https://www.pinterest.co/depologyskincare/" target="_blank"><img alt="Pinterest" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/8149ca4d-d368-4ec0-ab45-8b6d815399c8.png" style="width:30px;" width="30"/></a></div>
<div style="display:inline-block;padding-right:12px;"><a href="https://www.youtube.com/c/DepologySkincare" target="_blank"><img alt="YouTube" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/803eb370-a807-4966-9f69-7cbf9e73a61b.png" style="width:30px;" width="30"/></a></div>
</div>
</td>
</tr></tbody></table>
</div>

<div class="kl-column" style="display:table-cell;vertical-align:top;width:50%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr>
<td style="vertical-align:top;padding:25px 18px 18px 18px;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;letter-spacing:0px;line-height:1.5;text-align:left;color:#171516;">
<div style="line-height:100% !important;text-align:left;">
<span style="color:#f7f7f7;text-transform:uppercase;font-family:futura-pt,'Century Gothic',CenturyGothic,AppleGothic,sans-serif;font-weight:500;font-size:14px;">
&copy; Depology, <br/>
<span style="font-size:10px;color:#d9d9d7;">support@depology.com</span><br/><br/><br/>
<a href="#" style="color:#fff;text-decoration:underline;font-weight:500">UNSUBSCRIBE</a>
</span>
</div>
</div>
</td>
</tr></tbody></table>
</div>

</div>
</div>
</td>
</tr></tbody>
</table>
</div>
</td>
</tr></tbody>
</table>

</div>
</div>
</body>
</html>
"""


def section_wrap_open():
    return """<!-- ============================================ -->
<!-- SECTION: HERO / LEAD / GRID                  -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#FFFFFF;background-color:#FFFFFF;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;background-color:#FFFFFF;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div class="content-padding kl-first">
"""


def section_wrap_close():
    return """</div>
</td>
</tr></tbody>
</table>
</div>
</td>
</tr></tbody>
</table>
</div>
</td></tr></tbody>
</table>
"""


# ══════════════════════════════════════════════════════════════════════
# EMAIL CONFIGS — 8 Memorial emails
# ══════════════════════════════════════════════════════════════════════

# Helper: red bold span
def rb(text): return f'<span style="color:#C8102E;font-weight:700;">{text}</span>'
# Helper: underline
def ul(text): return f'<span style="text-decoration:underline;">{text}</span>'
# Helper: blue italic
def bi(text): return f'<span style="color:#1E3A8A;font-style:italic;">{text}</span>'


EMAILS = [
    # ─── 5/20 AM Memorial Launch ───
    {
        "filename": "20260520_AM_Memorial_Launch.html",
        "title": "Memorial Day Sale IS LIVE",
        "template": "A",
        "use_mem10": True,
        "hero_badge": "UP TO 60% OFF",
        "h1": "The Summer Sale You&rsquo;ve Been Waiting For&hellip; IS LIVE!",
        "lead": f'Memorial Day is here. We&rsquo;re offering our {rb("BIGGEST")} summer deal &mdash; with new launches and our best-selling peptide series.',
        "mem10_callout": f'Extra 10% off site-wide with code {ul("MEM10")} for subscribers, 48 hours only.',
        "primary_cta": "SHOP MEMORIAL SALE",
        "cards": [
            ("m3k_3f2", "3 FOR 2", "#1E3A8A", "80.00", "120.00", "SAVE $40", True, True),
            ("argireline_3f2", "3 FOR 2", "#1E3A8A", "98.00", "147.00", "SAVE $49", True, True),
            ("face_eye_duo", "50% OFF · ONLY 100 SPOTS", "#C8102E", "57.00", "114.00", "SAVE $57", True, True),
            ("bakuchiol", "70% OFF · $9", "#1E3A8A", "9.00", "30.00", "SAVE $21", False, True),
        ],
        "closing": f"With {ul('limited stock')} available, now&rsquo;s the time to secure your picks!",
        "secondary_cta": "SHOP ALL SALE",
    },
    # ─── 5/20 PM Memorial Resend ───
    {
        "filename": "20260520_PM_Memorial_Resend.html",
        "title": "Memorial Day Sale Going Fast",
        "template": "A",
        "use_mem10": True,
        "hero_badge": "UP TO 60% OFF",
        "h1": "Memorial Day Sale &mdash; It&rsquo;s On, and It&rsquo;s Going Fast!",
        "lead": "The sale has kicked off &mdash; and it&rsquo;s moving faster than we thought.",
        "mem10_callout": f'Extra 10% off site-wide with code {ul("MEM10")} for subscribers, 48 hours only.',
        "primary_cta": "SHOP MEMORIAL SALE",
        "cards": [
            ("pat", "NEW BUNDLE · SAVE $46", "#1E3A8A", "89.00", "135.00", "SAVE $46", True, True),
            ("m3k_3f2", "3 FOR 2", "#1E3A8A", "80.00", "120.00", "SAVE $40", True, True),
            ("mop", "35% OFF", "#1E3A8A", "22.00", "34.00", "SAVE $12", False, False),
            ("tlq", "30% OFF", "#1E3A8A", "31.00", "44.00", "SAVE $13", False, False),
        ],
        "closing": "More amazing offers waiting for you &mdash; click here to shop them before they&rsquo;re gone!",
        "secondary_cta": "SHOP ALL SALE",
    },
    # ─── 5/21 Eye + Texture Trio ───
    {
        "filename": "20260521_Eye_Texture_Trio.html",
        "title": "Smarter Eye + Texture Care",
        "template": "A",
        "use_mem10": True,  # MEM10 still valid morning of 5/21
        "hero_badge": "UP TO 50% OFF",
        "h1": "Celebrate Memorial Day with Smarter Eye + Texture Care",
        "lead": f"Don&rsquo;t miss your chance to upgrade your <b>eye + texture routine</b> with our most-loved peptide trio.<br/><br/>Grab yours today and {ul('see proven results in just 28 days.')}<br/><br/><b>Memorial Day pricing through Monday at midnight PDT.</b>",
        "mem10_callout": None,
        "primary_cta": "SHOP THE TRIO",
        "cards": [
            ("pec", "40% OFF", "#1E3A8A", "31.00", "52.00", "SAVE $21", False, False),
            ("mop", "35% OFF", "#1E3A8A", "22.00", "34.00", "SAVE $12", False, False),
            ("argireline_3f2", "3 FOR 2", "#1E3A8A", "98.00", "147.00", "SAVE $49", True, True),
            ("night_eye", "33% OFF", "#1E3A8A", "24.00", "36.00", "SAVE $12", True, True),
        ],
        "closing": "Limited stock available &mdash; grab yours while you can!",
        "secondary_cta": "SHOP MEMORIAL SALE",
    },
    # ─── 5/22 Peptide 3F2 + 100-cap ───
    {
        "filename": "20260522_Peptide_3F2.html",
        "title": "3 for 2 Peptides + 100-Cap Duo",
        "template": "A",
        "use_mem10": False,  # MEM10 expired 9 AM 5/22
        "hero_badge": "3 FOR 2",
        "h1": "Celebrate Memorial Day with the Power of Peptides",
        "lead": f"Don&rsquo;t miss your chance to stock up on our {rb('#1 bestselling peptide serums.')}<br/><br/>Grab yours today and {ul('see proven results in just 28 days.')}<br/><br/>{rb('🔴 ONLY 100 Face &amp; Eye Peptide Duos at this price. No restocks at $57. Run, don&rsquo;t walk.')}",
        "mem10_callout": None,
        "primary_cta": "SHOP 3 FOR 2!",
        "cards": [
            ("m3k_3f2", "3 FOR 2", "#1E3A8A", "80.00", "120.00", "SAVE $40", True, True),
            ("argireline_3f2", "3 FOR 2", "#1E3A8A", "98.00", "147.00", "SAVE $49", True, True),
            ("face_eye_duo", "50% OFF · ONLY 100 SPOTS", "#C8102E", "57.00", "114.00", "SAVE $57", True, True),
            ("pat", "NEW BUNDLE · SAVE $46", "#1E3A8A", "89.00", "135.00", "SAVE $46", True, True),
        ],
        "closing": "Limited stock available &mdash; grab yours while you can!",
        "secondary_cta": "SHOP MEMORIAL SALE",
    },
    # ─── 5/23 Matriplex Solo + 售罄叙事 ───
    {
        "filename": "20260523_Matriplex_Cream_50.html",
        "title": "Matriplex Cream 40% Off",
        "template": "A",
        "use_mem10": False,
        "hero_badge": "40% OFF / LIMITED",
        "h1": "Celebrate Memorial Day with the Power of Peptides",
        "lead": f"{rb('The first 100 Face &amp; Eye Duos are claimed')} &mdash; but our most powerful anti-aging peptide cream is still <b>solo at 40% off</b> this weekend.<br/><br/>With Matrixyl&reg; and a clinically formulated peptide complex, {bi('it firms, lifts and smooths your skin overnight.')}<br/><br/><b>Memorial pricing through Monday at midnight PDT.</b>",
        "mem10_callout": None,
        "primary_cta": "SAVE 40% TODAY",
        "cards": [
            ("matriplex", "40% OFF", "#1E3A8A", "37.00", "62.00", "SAVE $25", True, True),
            ("tlq", "30% OFF", "#1E3A8A", "31.00", "44.00", "SAVE $13", False, False),
            ("mop", "35% OFF", "#1E3A8A", "22.00", "34.00", "SAVE $12", False, False),
            ("pat", "NEW BUNDLE · SAVE $46", "#1E3A8A", "89.00", "135.00", "SAVE $46", True, True),
        ],
        "closing": "Limited stock available &mdash; grab yours while you can!",
        "secondary_cta": "SHOP MEMORIAL SALE",
    },
    # ─── 5/24 AM Bakuchiol $9 + M2 50% ───
    {
        "filename": "20260524_AM_Bakuchiol_M1_Sunday.html",
        "title": "$9 Bakuchiol + M2 50% First-Ever",
        "template": "A",
        "use_mem10": False,
        "hero_badge": "ONLY $9 BAKUCHIOL · M2 50% NEW WITH RETINOL",
        "h1": "Celebrate Memorial Day with Sunday Essentials",
        "lead": f"Your Sunday skin essential, now just <b>$9.</b><br/><br/>Our <b>Bakuchiol Smoothing Serum Stick</b> softens fine lines and smooths texture &mdash; without retinol&rsquo;s irritation. (Original $30. While supplies last.)<br/><br/>{rb('Plus: First-ever 50% off the new M2 Retinol Micro-dart Patches.')}<br/><br/>{rb('US exclusive for the final 48 hours of Memorial Sale!')}",
        "mem10_callout": None,
        "primary_cta": "SHOP $9 BAKUCHIOL!",
        "cards": [
            ("bakuchiol", "ONLY $9", "#1E3A8A", "9.00", "30.00", "SAVE $21", False, True),
            ("m2", "50% OFF · FIRST EVER", "#1E3A8A", "43.00", "86.00", "SAVE $43", True, True),
            ("pat", "NEW BUNDLE · SAVE $46", "#1E3A8A", "89.00", "135.00", "SAVE $46", True, True),
            ("static_duo", "35% OFF · BUNDLE", "#1E3A8A", "49.00", "76.00", "SAVE $27", True, True),
        ],
        "closing": "Limited stock available &mdash; grab yours while you can!",
        "secondary_cta": "SHOP MEMORIAL SALE",
    },
    # ─── 5/24 PM 24 Hours Left (Template B) ───
    {
        "filename": "20260524_PM_24_Hours_Left.html",
        "title": "Only 24 Hours Left",
        "template": "B",
        "use_mem10": False,
        "banner_line_1": "ONLY 24 HOURS LEFT!",
        "banner_line_2": "THE MEMORIAL DAY SALE",
        "lead": f"This is your {rb('last chance')} to get the BEST savings of the season!<br/><br/>The offers below {ul('won&rsquo;t be back until Black Friday.')}<br/><br/>{bi('Shop now or miss out until the end of the year.')}",
        "mem10_callout": None,
        "primary_cta": "LAST CHANCE TO SAVE!",
        "cards": [
            ("mop", "35% OFF", "#1E3A8A", "22.00", "34.00", "$22 ONLY - SHOP NOW", False, False),
            ("matriplex", "40% OFF", "#1E3A8A", "37.00", "62.00", "$37 ONLY - SHOP NOW", True, True),
            ("bakuchiol", "70% OFF / $9", "#1E3A8A", "9.00", "30.00", "$9 ONLY - SHOP NOW", False, True),
            ("pec", "40% OFF", "#1E3A8A", "31.00", "52.00", "$31 ONLY - SHOP NOW", False, False),
        ],
        "closing": "The offer is ending soon, so be sure not to miss out!",
        "secondary_cta": "SHOP MEMORIAL SALE",
    },
    # ─── 5/25 Last Chance (Template C) ───
    {
        "filename": "20260525_Last_Chance.html",
        "title": "LAST CHANCE — Memorial Sale",
        "template": "C",
        "use_mem10": False,
        "overlay_red": "LAST CHANCE",
        "overlay_blue": "THE MEMORIAL DAY SALE",
        "hero_badge": "UP TO 50% OFF",
        "lead": f"Yes, you&rsquo;ll regret missing the {rb('BIGGEST')} sale of the summer.<br/><br/>Stock up on {ul('dermatologist-approved')} peptide serums, retinol body lotions, and more &mdash; all for less!<br/><br/>{bi('Remember &mdash; the offer ends at <b>midnight PDT</b>.')}",
        "mem10_callout": None,
        "primary_cta": "SAVE 50% NOW!",
        "cards": [
            ("m3k_3f2", "3 FOR 2", "#1E3A8A", "80.00", "120.00", "$80 ONLY - SHOP NOW", True, True),
            ("dynamic_duo", "40% OFF · BUNDLE", "#1E3A8A", "51.00", "85.00", "SAVE $34 - SHOP NOW", True, True),
            ("bakuchiol", "70% OFF / $9", "#1E3A8A", "9.00", "30.00", "$9 ONLY - SHOP NOW", False, True),
            ("matriplex", "40% OFF", "#1E3A8A", "37.00", "62.00", "SAVE $25 - SHOP NOW", True, True),
        ],
        "closing": "The offer is ending soon, so be sure not to miss out!",
        "secondary_cta": "SHOP MEMORIAL SALE",
    },
]


# ══════════════════════════════════════════════════════════════════════
# RENDERER
# ══════════════════════════════════════════════════════════════════════

def render(cfg):
    use_mem10 = cfg.get("use_mem10", False)
    sale_link = sale_page_url(use_mem10)

    # Build cards (BEST tag + Dermatologist seal removed per Leon 2026-05-13)
    card_blocks = []
    for c in cfg["cards"]:
        # Cards may still carry legacy 8-tuple form (..., show_best, show_seal) — slice first 6
        sku_key, badge_txt, badge_color, price, original, cta_txt = c[:6]
        card_blocks.append(
            card_html(sku_key, badge_txt, badge_color, price, original, cta_txt,
                      product_url(sku_key, use_mem10))
        )

    grid = grid_2x2(card_blocks)

    # Hero + headline + lead per template
    template = cfg["template"]
    if template == "A":
        hero = hero_placeholder_a(cfg["hero_badge"], sale_link)
        head_block = headline_block(cfg["h1"])
    elif template == "B":
        hero = hero_placeholder_b(cfg["banner_line_1"], cfg["banner_line_2"], sale_link)
        head_block = ""  # banner replaces H1 in template B
    elif template == "C":
        hero = hero_placeholder_c(cfg["overlay_red"], cfg["overlay_blue"], cfg["hero_badge"], sale_link)
        head_block = ""  # overlay text replaces H1 in template C
    else:
        raise ValueError(f"Unknown template: {template}")

    lead = lead_block(
        cfg["lead"],
        cfg.get("mem10_callout"),
        cfg["primary_cta"],
        sale_link,
    )

    closing = closing_block(cfg["closing"], cfg["secondary_cta"], sale_link)

    parts = [
        html_head(cfg["title"]),
        section_wrap_open(),
        LOGO_BLOCK,
        hero,
        head_block,
        lead,
        section_wrap_close(),
        grid,
        closing,
        FOOTER_BLOCK,
    ]
    return "".join(parts)


def main():
    print("Memorial Sale HTML render")
    print("=" * 60)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for cfg in EMAILS:
        html = render(cfg)
        out = OUT_DIR / cfg["filename"]
        out.write_bytes(html.encode("utf-8"))
        size_kb = len(html.encode("utf-8")) / 1024
        print(f"[written] {cfg['filename']}  ({size_kb:.1f} KB, template {cfg['template']})")
    print("=" * 60)
    print(f"8 Memorial emails rendered to {OUT_DIR}")


if __name__ == "__main__":
    main()
