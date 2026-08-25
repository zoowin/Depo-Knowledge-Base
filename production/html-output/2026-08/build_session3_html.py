from __future__ import annotations

from html import escape
from pathlib import Path


OUT = Path(__file__).resolve().parent
ASSET = "../../assets/2026-08/"
FONT = "'Century Gothic',CenturyGothic,AppleGothic,Arial,sans-serif"
SERIF = "Georgia,'Times New Roman',serif"
HEADER = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a91ce3e7-44ab-42dc-a9e6-c3dc74b6f3bf.jpeg"
LOGO = "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/82cac524-3eb2-4807-a508-af61cee50920.png"

HEROES = {
    "mps": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/ff908cd3-620d-4fca-9c35-fb485b9e4e25.jpeg",
    "m3k": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/c11a9b2b-b2d7-4b96-9734-cf451c03b997.jpeg",
    "body": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/27ef4b97-4a12-4134-862c-130791233d69.jpeg",
    "triple": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/d95cc67e-94be-4ac6-8f92-71c8b2a923d3.jpeg",
    "microdart": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/f5a9661a-f8cd-4342-9032-52595bf06460.jpeg",
}


IMAGES = {
    "mps": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/160b6da8-e5a3-4202-bcef-a511922d5954.png",
    "eye": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/17182a51-02dc-4114-8b61-d82e29c46bcb.png",
    "m3k": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/44a0bdde-9c05-4c2b-854b-fe92895a2a6f.png",
    "matriplex": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/420e0d8e-091d-4a94-ad76-e4c2bea97c46.png",
    "triple": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/f11a370d-d5dc-426a-90b0-1ec12a1f8c85.png",
    "body": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/65227851-df6d-4cbd-bcae-6a5c9e446619.png",
    "microdart": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/bdb87085-8617-43d8-be9b-f2cc405c16d1.png",
    "nightpatch": "https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fb01a6c6-6cdf-4159-b40b-9f605f71ab65.png",
}


def button(label: str, url: str, compact: bool = False) -> str:
    padding = "11px 18px" if compact else "15px 32px"
    size = "11px" if compact else "13px"
    return f'''<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto;"><tr>
<td bgcolor="#000000" style="border-radius:2px;mso-padding-alt:{padding};">
<a href="{escape(url, quote=True)}" target="_blank" style="display:inline-block;background:#000000;color:#FFFFFF;font-family:{FONT};font-size:{size};font-weight:700;letter-spacing:1.5px;padding:{padding};text-decoration:none;border-radius:2px;">{escape(label)}</a>
</td></tr></table>'''


def product_card(index: int, label: str, name: str, description: str, cta: str, url: str, image: str) -> str:
    return f'''<tr><td style="padding:8px 20px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="background:#FFFFFF;border:1px solid #E4E4E4;border-radius:3px;"><tr>
<td class="product-img" align="center" valign="middle" style="width:33%;padding:20px 0 20px 20px;">
<img src="{escape(image, quote=True)}" alt="{escape(name, quote=True)}" width="140" style="display:block;width:140px;max-width:100%;height:auto;margin:0 auto;"/>
</td>
<td class="product-copy" valign="middle" style="padding:20px 24px 20px 16px;">
<div style="font-family:{FONT};font-size:10px;color:#858585;font-weight:700;letter-spacing:1.8px;line-height:1.4;margin:0 0 7px;text-transform:uppercase;">{index:02d} &mdash; {escape(label)}</div>
<div style="font-family:{FONT};font-size:16px;color:#111111;font-weight:700;line-height:1.3;margin:0 0 8px;">{escape(name)}</div>
<p style="font-family:{FONT};font-size:13px;color:#454545;line-height:1.55;margin:0 0 13px;">{escape(description)}</p>
{button(cta, url, compact=True)}
</td></tr></table></td></tr>'''


def footer() -> str:
    return f'''<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" role="presentation" width="600" style="width:600px;max-width:600px;background:#000000;"><tr>
<td class="footer-left" valign="top" style="width:50%;padding:28px 18px 24px;">
<a href="{{{{ organization.url }}}}" style="text-decoration:none;"><img alt="{{{{ organization.name }}}}" src="{LOGO}" width="230" style="display:block;width:230px;max-width:100%;height:auto;"/></a>
</td>
<td class="footer-right" valign="top" style="width:50%;padding:25px 18px;">
<div style="font-family:{FONT};font-size:12px;color:#F7F7F7;line-height:1.55;text-transform:uppercase;">&copy; {{{{ organization.name }}}}<br/><span style="font-size:10px;color:#D9D9D7;">{{{{ organization.full_address }}}}</span><br/><br/><a href="{{% unsubscribe_link %}}" style="color:#FFFFFF;text-decoration:underline;">UNSUBSCRIBE</a></div>
</td></tr></table>'''


def document(title: str, preview: str, hero: str, hero_alt: str, hero_url: str, headline: str, subheadline: str, hero_cta: str, body_headline: str, paragraphs: list[str], module: str, section_title: str, section_subtitle: str, products: list[tuple], closing: str, final_cta: str, final_url: str, accent: str = "#F8F6F2", internal: str = "") -> str:
    body = "".join(f'<p style="font-family:{FONT};font-size:16px;color:#333333;line-height:1.65;margin:0 0 14px;text-align:center;">{escape(p)}</p>' for p in paragraphs)
    cards = "".join(product_card(i + 1, *product) for i, product in enumerate(products))
    return f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{escape(title)}</title>
<style>
body {{ margin:0; padding:0; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; background-color:#DDDDDD; }}
table, td {{ border-collapse:collapse; mso-table-lspace:0; mso-table-rspace:0; }}
img {{ border:0; height:auto; line-height:100%; outline:none; text-decoration:none; -ms-interpolation-mode:bicubic; }}
@media only screen and (max-width:480px) {{
  .container {{ width:100% !important; }}
  .hero-h {{ font-size:29px !important; line-height:1.18 !important; }}
  .body-pad {{ padding-left:26px !important; padding-right:26px !important; }}
  .product-img, .product-copy {{ display:block !important; width:100% !important; box-sizing:border-box !important; }}
  .product-img {{ padding:22px 20px 5px !important; }}
  .product-copy {{ padding:9px 24px 25px !important; }}
  .module-cell {{ padding-left:16px !important; padding-right:16px !important; }}
  .three-col {{ display:block !important; width:100% !important; padding:9px 0 !important; }}
  .footer-left, .footer-right {{ display:block !important; width:100% !important; box-sizing:border-box !important; }}
}}
</style></head>
<body style="margin:0;padding:0;background:#DDDDDD;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{escape(preview)}</div>
<div style="background:#DDDDDD;padding:20px 0;">
<!-- Hero image uses the approved Klaviyo CDN asset. -->
<!-- {internal} -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" role="presentation" width="600" style="width:600px;max-width:600px;background:#FFFFFF;"><tr><td align="center" style="padding:0;"><a href="https://depology.com/" style="display:block;text-decoration:none;"><img src="{HEADER}" alt="Depology" width="600" style="display:block;width:100%;height:auto;"/></a></td></tr>
<tr><td align="center" style="padding:0;"><a href="{escape(hero_url, quote=True)}" style="display:block;text-decoration:none;"><img src="{escape(hero, quote=True)}" alt="{escape(hero_alt, quote=True)}" width="600" style="display:block;width:100%;height:auto;"/></a></td></tr>
<tr><td align="center" style="padding:32px 26px 8px;background:#FFFFFF;"><h1 class="hero-h" style="font-family:{SERIF};font-size:40px;font-weight:400;line-height:1.13;color:#111111;margin:0;text-align:center;">{escape(headline)}</h1></td></tr>
<tr><td align="center" style="padding:8px 42px 18px;background:#FFFFFF;"><p style="font-family:{FONT};font-size:17px;color:#353535;line-height:1.5;margin:0;text-align:center;">{subheadline}</p></td></tr>
<tr><td align="center" style="padding:7px 24px 36px;background:#FFFFFF;">{button(hero_cta, hero_url)}</td></tr>
<tr><td style="padding:0 24px;background:#FFFFFF;"><div style="border-top:1px solid #DDDDDD;font-size:1px;line-height:1px;">&nbsp;</div></td></tr>
<tr><td align="center" style="padding:35px 26px 10px;background:#FFFFFF;"><div style="font-family:{FONT};font-size:25px;font-weight:700;line-height:1.3;color:#111111;text-align:center;">{escape(body_headline)}</div></td></tr>
<tr><td class="body-pad" style="padding:10px 50px 25px;background:#FFFFFF;">{body}</td></tr>
{module}
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" role="presentation" width="600" style="width:600px;max-width:600px;background:#FFFFFF;"><tr><td align="center" style="padding:43px 28px 8px;"><div style="font-family:{FONT};font-size:21px;font-weight:700;letter-spacing:1.8px;line-height:1.35;color:#111111;text-align:center;">{escape(section_title).upper()}</div><div style="font-family:{SERIF};font-size:14px;font-style:italic;color:#666666;line-height:1.4;margin-top:6px;text-align:center;">{escape(section_subtitle)}</div></td></tr>
<tr><td style="padding:18px 0 30px;">{cards}</td></tr></table>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="container" role="presentation" width="600" style="width:600px;max-width:600px;background:{accent};"><tr><td align="center" style="padding:42px 34px 13px;"><p style="font-family:{SERIF};font-size:17px;font-style:italic;color:#222222;line-height:1.6;margin:0;text-align:center;">{escape(closing)}</p></td></tr><tr><td align="center" style="padding:19px 28px 46px;">{button(final_cta, final_url)}</td></tr></table>
{footer()}
</div></body></html>'''


def three_items(items: list[tuple[str, str]], title: str, accent: str = "#F8F6F2") -> str:
    columns = "".join(f'''<td class="three-col" valign="top" style="width:33.33%;padding:0 7px;"><div style="background:#FFFFFF;border:1px solid #E1E1E1;min-height:102px;padding:18px 12px;box-sizing:border-box;"><div style="font-family:{FONT};font-size:10px;font-weight:700;letter-spacing:1.6px;color:#777777;line-height:1.3;text-transform:uppercase;">{escape(label)}</div><div style="font-family:{SERIF};font-size:17px;color:#111111;line-height:1.3;margin-top:7px;">{escape(detail)}</div></div></td>''' for label, detail in items)
    return f'''<tr><td class="module-cell" style="background:{accent};padding:26px 30px 38px;"><div style="font-family:{FONT};font-size:11px;font-weight:700;letter-spacing:2px;color:#666666;text-align:center;text-transform:uppercase;margin:0 0 14px;">{escape(title)}</div><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tr>{columns}</tr></table></td></tr>'''


campaigns = [
    {
        "file": "20260824_MPS_Lines_That_Move.html",
        "html": document(
            "Care for the lines that move", "A lightweight AM/PM peptide layer for the places your expressions visit most.",
            HEROES["mps"], "A woman applying skincare to her forehead", "https://depology.com/products/argireline-anti-wrinkle-serum",
            "Care for the lines that move", "Target forehead, eyes, smile lines<br/>Lightweight care, AM and PM", "EXPLORE MPS",
            "Precision changes the routine",
            ["Some lines appear where the face moves most: across the forehead, around the eyes, and beside the mouth. A full-face routine can still leave those areas wanting a more deliberate step.", "Peptide Complex 10% Argireline™ Serum is a lightweight AM/PM layer for those high-movement zones. Apply after cleansing, then follow with your preferred serum or cream for smoother-looking skin over time."],
            three_items([("Forehead", "A high-movement zone"), ("Eye area", "A dedicated daily step"), ("Smile lines", "Care where expressions land")], "A focused way to look at expression zones"),
            "Build your targeted routine", "A daily peptide layer, plus a dedicated eye finishing step",
            [("The Daily Target", "Peptide Complex 10% Argireline™ Serum", "A lightweight daily peptide serum that helps reduce the appearance of expression lines in high-movement areas.", "SHOP MPS SERUM", "https://depology.com/products/argireline-anti-wrinkle-serum", IMAGES["mps"]), ("The Eye Comfort Step", "Peptide Complex Eye Cream", "Add daily hydration and comfort where under-eye skin needs a dedicated finishing step.", "SHOP EYE CREAM", "https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream", IMAGES["eye"])],
            "Start with the high-movement zones you notice most, then make daily care easy to keep.", "EXPLORE TARGETED CARE", "https://depology.com/products/argireline-anti-wrinkle-serum"),
    },
    {
        "file": "20260826_M3K_Hydrate_Smooth.html",
        "html": document(
            "Hydrate. Smooth. Keep it simple.", "One AM/PM serum for hydration, plumpness, and a smoother-looking finish.",
            HEROES["m3k"], "Matrixyl 3000 serum in a morning setting", "https://depology.com/products/depology-matrixyl-3000-serum",
            "Hydrate. Smooth. Keep it simple.", "One daily peptide serum<br/>For a comfortable, plumper look", "DISCOVER M3K",
            "Hydration has a visible role",
            ["When skin feels short on moisture, fine lines can look more noticeable and makeup can lose its smooth finish. The most useful routine is often the one you can return to morning and night.", "Matrixyl® 3000 Collagen Serum pairs peptides with hyaluronic acid for hydration, plumpness, and smoother-looking skin. Apply after cleansing, AM and PM, then choose the cream that best fits how your skin feels."],
            three_items([("01", "Cleanse"), ("02", "M3K serum"), ("03", "Choose your cream")], "A simple morning-to-night order", "#EEF5F8"),
            "Build your daily base", "One serum, then a finish that suits your skin",
            [("The Daily Base", "Matrixyl® 3000 Collagen Serum", "A peptide-powered AM/PM serum that supports hydration, plumpness, and the look of smoother skin.", "SHOP M3K SERUM", "https://depology.com/products/depology-matrixyl-3000-serum", IMAGES["m3k"]), ("The Peptide Finish", "Matriplex™ Peptide Intense Cream", "Choose this 8% Matrixyl Complex cream when you want a peptide-focused moisturizing finish after serum.", "SHOP MATRIPLEX", "https://depology.com/products/tri-active-matrixyl-complex-cream", IMAGES["matriplex"]), ("The Rich Alternative", "Triple Lipid + Q10 Moisturizing Treatment RICH", "Choose this rich final step instead when dryness and lasting barrier comfort are your main priorities.", "SHOP TRIPLE LIPID", "https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich", IMAGES["triple"])],
            "One consistent serum layer can make a daily routine feel easier to keep—and easier to see through.", "START WITH HYDRATION", "https://depology.com/products/depology-matrixyl-3000-serum", "#EEF5F8"),
    },
    {
        "file": "20260827_Body_Lotion_Three_Jobs.html",
        "html": document(
            "One body lotion. Three jobs.", "Retinol, AHA, and hydration in one PM lotion for rough, dull, dry-feeling body skin.",
            HEROES["body"], "Retinol body lotion in an evening body-care setting", "https://depology.com/products/retinol-radiance-body-lotion",
            "One body lotion. Three jobs.", "Smooth rough texture at night<br/>Hydrate arms and legs", "EXPLORE BODY CARE",
            "Body care can do more",
            ["Rough-feeling arms, dull-looking legs, and dry texture do not need three separate products. A single PM body step can make the routine feel more practical—and easier to keep.", "Retinol Radiance Rescue Body Lotion combines retinol, AHA, and moisturizing support to gently smooth the skin surface, enhance radiance, and hydrate. Apply to clean, dry body skin at night, then let consistency do the work."],
            '''<tr><td class="module-cell" style="background:#FBF4EF;padding:27px 38px 36px;"><div style="font-family:''' + FONT + ''';font-size:11px;font-weight:700;letter-spacing:2px;color:#6C584C;text-align:center;text-transform:uppercase;margin:0 0 16px;">A practical PM body step</div><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tr><td class="three-col" valign="top" style="width:33.33%;padding:0 8px;text-align:center;"><div style="font-family:''' + FONT + ''';font-size:10px;font-weight:700;color:#8A7163;letter-spacing:1.5px;">01</div><div style="font-family:''' + SERIF + ''';font-size:17px;color:#111111;line-height:1.3;margin-top:5px;">Clean, dry skin</div></td><td class="three-col" valign="top" style="width:33.33%;padding:0 8px;text-align:center;border-left:1px solid #DCCDC3;border-right:1px solid #DCCDC3;"><div style="font-family:''' + FONT + ''';font-size:10px;font-weight:700;color:#8A7163;letter-spacing:1.5px;">02</div><div style="font-family:''' + SERIF + ''';font-size:17px;color:#111111;line-height:1.3;margin-top:5px;">PM lotion</div></td><td class="three-col" valign="top" style="width:33.33%;padding:0 8px;text-align:center;"><div style="font-family:''' + FONT + ''';font-size:10px;font-weight:700;color:#8A7163;letter-spacing:1.5px;">03</div><div style="font-family:''' + SERIF + ''';font-size:17px;color:#111111;line-height:1.3;margin-top:5px;">Sunscreen by day</div></td></tr></table><div style="border-top:1px solid #DCCDC3;margin:22px 0 16px;"></div><p style="font-family:''' + FONT + ''';font-size:13px;color:#4E443D;line-height:1.55;margin:0;text-align:center;"><strong>Use note:</strong> Start 2–3 nights weekly if new or sensitive. Do not use with strong exfoliating body products on the same area that night. Use sunscreen on exposed skin during the day.</p></td></tr>''',
            "Complete your routine simply", "A focused PM body step, plus simple face and eye care",
            [("The PM Body Step", "Retinol Radiance Rescue Body Lotion", "A retinol + AHA body lotion that gently smooths texture, enhances radiance, and deeply hydrates.", "SHOP BODY LOTION", "https://depology.com/products/retinol-radiance-body-lotion", IMAGES["body"]), ("The Face Layer", "Matrixyl® 3000 Collagen Serum", "Keep face care equally simple with a daily peptide serum for hydration and smoother-looking skin.", "SHOP M3K SERUM", "https://depology.com/products/depology-matrixyl-3000-serum", IMAGES["m3k"]), ("The Eye Step", "Peptide Complex Eye Cream", "Add daily under-eye hydration and comfort without duplicating your face or body format.", "SHOP EYE CREAM", "https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream", IMAGES["eye"])],
            "Give the skin on your arms and legs a focused night step—without making the routine complicated.", "SIMPLIFY BODY CARE", "https://depology.com/products/retinol-radiance-body-lotion", "#FBF4EF"),
    },
    {
        "file": "20260828_Triple_Lipid_35_20.html",
        "html": document(
            "Your rich final step is $35.20", "Ceramides, cholesterol, fatty acids, and CoQ10 in one rich final step—currently $35.20.",
            HEROES["triple"], "Triple Lipid cream in a warm evening setting", "https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich",
            "Your rich final step is $35.20", "Regularly $44.00<br/>For dry-skin comfort, AM or PM", "DISCOVER TRIPLE LIPID",
            "Finish with lipid comfort",
            ["When skin feels tight or dry, a final cream can be the step that makes the rest of the routine feel more comfortable. This is a rich option for face, neck, and décolleté—morning or night.", "Triple Lipid + Q10 RICH brings ceramides, cholesterol, fatty acids, and CoQ10 together with squalane and shea butter. It helps seal in your serum and gives dry skin lasting moisture comfort, currently for $35.20."],
            '''<tr><td class="module-cell" style="background:#151515;padding:28px 35px 34px;"><div style="font-family:''' + FONT + ''';font-size:10px;color:#B8B8B8;font-weight:700;letter-spacing:2px;text-align:center;text-transform:uppercase;">Current value</div><div style="font-family:''' + SERIF + ''';font-size:44px;color:#FFFFFF;line-height:1.1;text-align:center;margin:8px 0 5px;">$35.20</div><div style="font-family:''' + FONT + ''';font-size:12px;color:#D2D2D2;line-height:1.5;text-align:center;">Regularly $44.00</div><div style="border-top:1px solid #4A4A4A;margin:22px 0 17px;"></div><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tr><td class="three-col" style="width:33.33%;padding:0 7px;text-align:center;"><div style="font-family:''' + FONT + ''';font-size:10px;color:#B8B8B8;letter-spacing:1.2px;text-transform:uppercase;">Ceramides</div></td><td class="three-col" style="width:33.33%;padding:0 7px;text-align:center;"><div style="font-family:''' + FONT + ''';font-size:10px;color:#B8B8B8;letter-spacing:1.2px;text-transform:uppercase;">Lipids</div></td><td class="three-col" style="width:33.33%;padding:0 7px;text-align:center;"><div style="font-family:''' + FONT + ''';font-size:10px;color:#B8B8B8;letter-spacing:1.2px;text-transform:uppercase;">CoQ10</div></td></tr></table></td></tr>''',
            "Start, layer, choose your finish", "A daily serum layer, then the cream that fits your skin",
            [("The Rich Final Step", "Triple Lipid + Q10 Moisturizing Treatment RICH", "Ceramides, cholesterol, fatty acids, and CoQ10 in a rich cream for lasting moisture comfort.", "SHOP TRIPLE LIPID", "https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich", IMAGES["triple"]), ("The Hydrating Layer", "Matrixyl® 3000 Collagen Serum", "Use this daily peptide serum first when you want hydration and a smoother-looking finish before cream.", "SHOP M3K SERUM", "https://depology.com/products/depology-matrixyl-3000-serum", IMAGES["m3k"]), ("The Peptide Cream Alternative", "Matriplex™ Peptide Intense Cream", "An 8% Matrixyl Complex cream for hydration, comfort, and a smoother-looking finish. Choose it as your final cream instead of Triple Lipid RICH.", "SHOP MATRIPLEX", "https://depology.com/products/tri-active-matrixyl-complex-cream", IMAGES["matriplex"])],
            "Choose one final cream that fits your skin’s need for richer comfort, then keep the rest simple.", "SHOP THE RICH FINISH", "https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich", "#F4F0EA", "INTERNAL: Verify the live $35.20 price and $44.00 regular price immediately before scheduling."),
    },
    {
        "file": "20260831_Micro_Dart_Eye_Patch.html",
        "html": document(
            "One patch night, targeted eyes", "Target under-eye and crow’s-feet concerns with upgraded 0.1% retinol and peptide patch care.",
            HEROES["microdart"], "Deepcare Micro-dart Eye Patch in a bedtime setting", "https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0",
            "One patch night, targeted eyes", "0.1% retinol + peptides<br/>For under-eyes and crow’s feet", "DISCOVER MICRO-DARTS",
            "Make eye care more focused",
            ["The under-eye and crow’s-feet areas often need more than a general face routine. A patch night gives you a focused format: apply to clean, dry skin, then wear for at least two hours or overnight.", "Deepcare+® Micro-dart Eye Patches pair 3,300 IU/g retinol (about 0.1%) with peptides and hydrating support. The hydrocolloid micro-darts place the formula at the skin’s surface layers for a targeted at-home step."],
            '''<tr><td class="module-cell" style="background:#EEF1F4;padding:28px 34px 35px;"><div style="font-family:''' + FONT + ''';font-size:11px;font-weight:700;letter-spacing:2px;color:#59636C;text-align:center;text-transform:uppercase;margin-bottom:18px;">A measured patch night</div><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tr><td class="three-col" valign="top" style="width:33.33%;padding:0 8px;text-align:center;"><div style="font-family:''' + SERIF + ''';font-size:24px;color:#111111;">01</div><div style="font-family:''' + FONT + ''';font-size:13px;color:#333333;line-height:1.45;margin-top:5px;">Clean, dry skin</div></td><td class="three-col" valign="top" style="width:33.33%;padding:0 8px;text-align:center;border-left:1px solid #CBD2D8;border-right:1px solid #CBD2D8;"><div style="font-family:''' + SERIF + ''';font-size:24px;color:#111111;">02</div><div style="font-family:''' + FONT + ''';font-size:13px;color:#333333;line-height:1.45;margin-top:5px;">At least 2 hours or overnight</div></td><td class="three-col" valign="top" style="width:33.33%;padding:0 8px;text-align:center;"><div style="font-family:''' + SERIF + ''';font-size:24px;color:#111111;">03</div><div style="font-family:''' + FONT + ''';font-size:13px;color:#333333;line-height:1.45;margin-top:5px;">Sunscreen by day</div></td></tr></table><div style="border-top:1px solid #CBD2D8;margin:22px 0 15px;"></div><p style="font-family:''' + FONT + ''';font-size:12px;color:#3F4850;line-height:1.6;margin:0;text-align:center;"><strong>Start gradually:</strong> If new to retinol or sensitive, use 2–3 nights weekly. On patch nights, avoid other retinoids, high-strength AHA/BHA, and pure vitamin C around the same area. Discontinue use if irritation persists.</p></td></tr>''',
            "Choose the right eye night", "Targeted patch care, daily hydration, or an alternate night",
            [("The Targeted Patch Night", "Deepcare+® Micro-dart Eye Patch", "A non-invasive eye patch with 3,300 IU/g retinol and peptides for the look of smoother, more radiant under-eyes.", "SHOP MICRO-DARTS", "https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0", IMAGES["microdart"]), ("The Daily Between-Step", "Peptide Complex Eye Cream", "Use AM and PM between patch nights for daily hydration, comfort, and a smoother under-eye appearance.", "SHOP EYE CREAM", "https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream", IMAGES["eye"]), ("The Hydration Night", "Replenishing Night Under Eye Patch", "Choose hydrogel hydration-focused nights with ceramides and multi-weight hyaluronic acid; alternate with Micro-darts.", "SHOP NIGHT PATCH", "https://depology.com/products/replenishing-night-under-eye-patch", IMAGES["nightpatch"])],
            "Give intensive patch nights and everyday hydration distinct roles, so eye care stays focused and easy to follow.", "BUILD YOUR EYE ROUTINE", "https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0", "#EEF1F4"),
    },
]


for campaign in campaigns:
    target = OUT / campaign["file"]
    target.write_text(campaign["html"], encoding="utf-8")
    print(f"Wrote {target.name}")
