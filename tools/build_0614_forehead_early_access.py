#!/usr/bin/env python3
"""Build 20260614_Forehead_Early_Access.html from 0408 white-bg base.

This email is a teaser/sign-up email (no product sale). Major restructuring:
  - REMOVE Section 4 (secondary atmosphere image)
  - REMOVE Section 6 (3 product cards) -> REPLACE with Sign-up CTA Block
    (cream/gold gradient + dart-pattern watermark + single SIGN ME UP CTA)
  - INSERT Eyebrow text above Hero Headline ("COMING IN JULY...")
  - INSERT Retinol Disclaimer between Closing and Footer (compliance)
  - All 3 CTA links -> sign-up landing page (placeholder URL)

Notes:
  - dart-pattern-light.png uses LOCAL relative path for browser preview.
    Before Klaviyo deploy: upload to Klaviyo CDN, swap URL.
  - Sign-up landing page is placeholder; swap when Shopify page is live.
"""
import sys, io, re, webbrowser
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'production' / 'html-output' / '2026-04' / '20260408_Hydration_Hierarchy.html'
OUT = ROOT / 'production' / 'html-output' / '2026-06' / '20260614_Forehead_Early_Access.html'

# --- Config ---
HERO_IMAGE_URL = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/034e2a24-f489-4b48-928c-951115be59db.jpeg'
SIGNUP_URL = 'https://depology.com/pages/early-access'  # LIVE Shopify sign-up page
DART_PATTERN_PATH = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fa3e0ac6-a943-451f-a5c9-dd62cc418cf6.png'  # Klaviyo CDN (uploaded 2026-06-10)

html = SRC.read_text(encoding='utf-8')

# ============================================================
# 1. REMOVE Section 4 (Secondary Atmosphere Image)
# ============================================================
sec4_marker = '\n\n<!-- ============================================ -->\n<!-- SECTION 4: SECONDARY ATMOSPHERE IMAGE        -->'
sec5_marker = '\n\n<!-- ============================================ -->\n<!-- SECTION 5: CHECKLIST (3 LAYERS)              -->'
idx4 = html.find(sec4_marker)
idx5 = html.find(sec5_marker)
if idx4 != -1 and idx5 != -1:
    html = html[:idx4] + html[idx5:]
    print('Removed Section 4 (secondary atmosphere image)')
else:
    raise SystemExit(f'Section 4 removal failed -- idx4={idx4}, idx5={idx5}')

# ============================================================
# 2. REPLACE Section 6 (Product Cards) with Sign-up CTA Block
# ============================================================
SIGNUP_BLOCK = f'''<!-- ============================================ -->
<!-- SECTION 6: SIGN-UP CTA BLOCK (cream/gold)    -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="kl-section" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#f7f2ea;background-color:#f7f2ea;background-image:linear-gradient(180deg,#ffffff 0%,#f3ead9 100%);margin:0px auto;max-width:600px;">
<!-- PATTERN: dart-pattern-light.png watermark. Local preview path; replace with Klaviyo CDN URL before deploy. -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#f7f2ea;background-image:url('{DART_PATTERN_PATH}'),linear-gradient(180deg,#ffffff 0%,#f3ead9 100%);background-repeat:no-repeat,no-repeat;background-size:100% auto,100% 100%;background-position:center top,center top;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:54px 40px 48px 40px;text-align:center;">

<!-- Block eyebrow -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:12px;font-weight:700;letter-spacing:4px;color:#b08d57;text-transform:uppercase;padding-bottom:10px;">Early Access</div>

<!-- Block headline -->
<div style="font-family:TimesNewRoman,'Times New Roman',Times,Georgia,serif;font-size:32px;color:#0e0e0e;line-height:1.2;padding-bottom:14px;">Get early access.</div>

<!-- Gold accent rule -->
<div style="width:40px;border-top:1px solid #b08d57;margin:0 auto 20px auto;font-size:0;line-height:0;">&nbsp;</div>

<!-- Block copy -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:16px;color:#5a5145;line-height:1.6;padding-bottom:30px;max-width:440px;margin:0 auto;">The full reveal comes in July. Be on the list when it does.</div>

<!-- CTA button -->
<table border="0" cellpadding="0" cellspacing="0" role="presentation" align="center" style="margin:0 auto;">
<tbody><tr>
<td align="center" bgcolor="#0e0e0e" style="border-radius:2px;background:#0e0e0e;">
<a href="{SIGNUP_URL}" target="_blank" style="color:#ffffff;text-decoration:none;display:inline-block;background:#0e0e0e;font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:16px;font-weight:700;line-height:100%;letter-spacing:2px;padding:16px 38px;border-radius:2px;">SIGN ME UP &rarr;</a>
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
'''

# --- "Why get on the list" — 3 early-access perks as numbered cards (stand-out layout) ---
def _perk_card(num, title, sub, last=False):
    mb = '0' if last else '10'
    return (
    f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="margin-bottom:{mb}px;">'
    '<tbody><tr>'
    f'<td style="background:#faf6ec;border:1px solid #e7ddc8;border-left:3px solid #b08d57;border-radius:6px;padding:16px 18px;">'
    '<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr>'
    # gold number badge
    f'<td width="40" valign="middle" style="width:40px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation"><tbody><tr>'
    f'<td width="32" height="32" align="center" valign="middle" bgcolor="#b08d57" style="width:32px;height:32px;border-radius:50%;color:#ffffff;font-family:TimesNewRoman,\'Times New Roman\',Times,Georgia,serif;font-size:14px;font-weight:700;">{num}</td>'
    '</tr></tbody></table></td>'
    # title + sub
    '<td valign="middle" style="padding-left:14px;">'
    f'<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;font-size:16px;font-weight:700;color:#0e0e0e;line-height:1.3;">{title}</div>'
    f'<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;font-size:13px;color:#6b6353;line-height:1.4;padding-top:2px;">{sub}</div>'
    '</td>'
    '</tr></tbody></table>'
    '</td></tr></tbody></table>'
    )

WHY_JOIN_BLOCK = '''<!-- ============================================ -->
<!-- SECTION 5b: WHY GET ON THE LIST (3 perk cards) -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="kl-section" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#FFFFFF;background-color:#FFFFFF;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:12px 40px 24px 40px;text-align:center;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:12px;font-weight:700;letter-spacing:3px;color:#b08d57;text-transform:uppercase;padding-bottom:16px;">Why get on the list</div>
''' + _perk_card('1', 'Be first', 'Shop before the public launch.') \
    + _perk_card('2', 'A launch-day offer', 'Reserved just for the list.') \
    + _perk_card('3', 'See the making', 'Front-row, from sketch to reveal.', last=True) + '''
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
'''

sec6_marker = '<!-- ============================================ -->\n<!-- SECTION 6: PRODUCT CARDS (white bg, gray cards) -->'
sec7_marker = '\n\n<!-- ============================================ -->\n<!-- SECTION 7: CLOSING + FINAL CTA               -->'
idx6 = html.find(sec6_marker)
idx7 = html.find(sec7_marker)
if idx6 != -1 and idx7 != -1:
    html = html[:idx6] + WHY_JOIN_BLOCK + SIGNUP_BLOCK + html[idx7:]
    print('Injected Why-join perk cards + Sign-up CTA Block')
else:
    raise SystemExit(f'Section 6 replacement failed -- idx6={idx6}, idx7={idx7}')

# ============================================================
# 2.5 REMOVE Section 7 (Closing + Final CTA)
#     Single CTA now lives in the Section 6 sign-up block (bottom).
# ============================================================
sec7_start = html.find('<!-- ============================================ -->\n<!-- SECTION 7: CLOSING + FINAL CTA')
footer_start = html.find('<!-- ============================================ -->\n<!-- FOOTER')
if sec7_start != -1 and footer_start != -1 and sec7_start < footer_start:
    html = html[:sec7_start] + html[footer_start:]
    print('Removed Section 7 (closing + final CTA)')
else:
    raise SystemExit(f'Section 7 removal failed -- sec7={sec7_start}, footer={footer_start}')

# ============================================================
# 3. INJECT Retinol Disclaimer between Closing and Footer
# ============================================================
RETINOL_DISCLAIMER = '''<!-- ============================================ -->
<!-- RETINOL DISCLAIMER (compliance, 11px gray)    -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="kl-section" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#F5F5F5;background-color:#F5F5F5;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#F5F5F5;background-color:#F5F5F5;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:20px 40px;text-align:left;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:11px;color:#777777;line-height:1.6;">
<strong style="color:#555555;">A note on Retinol:</strong> Apply sunscreen during daytime &mdash; retinol can increase sensitivity to UV. New to retinol? Your skin may need a short adjustment period (mild redness or slight peeling can be normal at first; this typically subsides within a few uses). Sensitive skin: start 2&ndash;3 times per week and increase gradually. Not recommended during pregnancy, breastfeeding, or for those with a known retinol allergy.
</div>
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

'''

# Email now names retinol in the hints -> compliance disclaimer required.
INCLUDE_RETINOL_DISCLAIMER = False  # Leon 2026-06-10: no long disclaimers in emails
if INCLUDE_RETINOL_DISCLAIMER:
    footer_marker = '<!-- ============================================ -->\n<!-- FOOTER'
    idx_footer = html.find(footer_marker)
    if idx_footer != -1:
        html = html[:idx_footer] + RETINOL_DISCLAIMER + html[idx_footer:]
        print('Injected Retinol Disclaimer before Footer')
    else:
        raise SystemExit('Footer marker not found')
else:
    print('Skipped Retinol Disclaimer (no retinol mention in teaser)')

# ============================================================
# 4. INJECT Eyebrow above Hero Headline (in Section 2)
# ============================================================
EYEBROW_BLOCK = '''<!-- Eyebrow -->
<div class="mj-column-per-100 mj-outlook-group-fix component-wrapper" style="font-size:0px;text-align:left;direction:ltr;vertical-align:top;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;" width="100%">
<tbody><tr>
<td style="background-color:#FFFFFF;vertical-align:top;padding:30px 16px 0px 16px;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:11px;font-weight:700;letter-spacing:4px;color:#b08d57;text-transform:uppercase;text-align:center;">Coming in July &middot; A First for D&#275;pology</div>
</td>
</tr></tbody>
</table>
</div>

<!-- Headline -->'''

eyebrow_target = '<!-- Headline -->'
n_headline = html.count(eyebrow_target)
if n_headline >= 1:
    html = html.replace(eyebrow_target, EYEBROW_BLOCK, 1)
    print('Injected Eyebrow above Hero Headline')
else:
    raise SystemExit('Headline marker not found')

# Reduce Headline td top padding (eyebrow now provides top space)
old_headline_td = '<td style="background-color:#FFFFFF;vertical-align:top;padding:24px 16px 8px 16px;">'
new_headline_td = '<td style="background-color:#FFFFFF;vertical-align:top;padding:12px 16px 8px 16px;">'
if old_headline_td in html:
    html = html.replace(old_headline_td, new_headline_td, 1)
    print('Adjusted Headline top padding (eyebrow above)')

# ============================================================
# 4.5 KEEP Hero CTA button (first-screen CTA; href rerouted in step 6)
# ============================================================
if '\nSHOP THE LAYERS\n' in html:
    html = html.replace('\nSHOP THE LAYERS\n', '\nGET EARLY ACCESS &rarr;\n', 1)
    print('Hero CTA kept, text -> GET EARLY ACCESS')
else:
    raise SystemExit('Hero CTA button text not found')

# ============================================================
# 5. Content replacements
# ============================================================
replacements = [
    # ---------- Title ----------
    ('<title></title>', "<title>Something for the lines you didn't ask for.</title>"),

    # ---------- Hero image ----------
    ('alt="The Hydration Hierarchy"', 'alt="Coming in July - a first for Depology"'),
    ('91d179ef-00c8-44e8-b396-8204ae4a28ca.jpeg',
     '034e2a24-f489-4b48-928c-951115be59db.jpeg'),

    # ---------- Hero headline + subhead (soft tease; CTA removed -> single CTA at bottom) ----------
    ('The Hydration Hierarchy.', 'Something for the lines<br/>you didn&rsquo;t ask for.'),
    ('Your skin needs layers, not puddles.',
     'You stop frowning. The lines don&rsquo;t.'),

    # ---------- Body headline (keeps the "misread" emotion, no longer names forehead) ----------
    ("Wet Isn't Hydrated.", "It&rsquo;s not your mood. It just looks that way."),

    # ---------- Body copy (soft tease: keep forehead + emotion, withhold the product) ----------
    ("""<p style="padding-bottom:1em;">Splashing water on your face feels refreshing. But within minutes, your skin can feel tighter than before. That's evaporation — not hydration.</p>
<p style="padding-bottom:1em;">True hydration works in layers: attract moisture (humectants), nourish the barrier (emollients), and seal it in (occlusives). Skip a layer, and the others lose their effect.</p>
<p style="padding-bottom:0;">The right routine doesn't just add water — it teaches your skin to hold onto it. That's where smart formulation makes all the difference.</p>""",

     '<p style="padding-bottom:1em;">Some lines speak for you &mdash; making you look tired or annoyed on a day you feel completely fine.</p>\n'
     '<p style="padding-bottom:1em;font-family:TimesNewRoman,\'Times New Roman\',Times,Georgia,serif;font-style:italic;font-size:22px;line-height:1.4;color:#0e0e0e;">&ldquo;You saw it on a video call. Then you couldn&rsquo;t unsee it.&rdquo;</p>\n'
     '<p style="padding-bottom:0;">We&rsquo;ve been working on something for exactly that. We&rsquo;re not showing it yet &mdash; but here&rsquo;s a hint:</p>'),

    # ---------- Checklist -> 3 TEASER HINTS (gold dart bullets, raise questions, hide mechanism) ----------
    ('<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:1.8;text-align:center;color:#000000;">\n'
     '<p style="padding-bottom:0.5em;">&#10003; Layer 1: Clean canvas — remove without stripping</p>\n'
     '<p style="padding-bottom:0.5em;">&#10003; Layer 2: Attract — humectants draw moisture in</p>\n'
     '<p style="padding-bottom:0;">&#10003; Layer 3: Seal — emollients lock hydration for hours</p>\n'
     '</div>',

     '<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;font-size:17px;font-weight:400;line-height:1.7;text-align:center;color:#0e0e0e;">\n'
     '<p style="padding-bottom:0.9em;"><span style="color:#b08d57;font-size:13px;">&#9662;</span> <strong>Retinol &mdash; backed by a peptide blend.</strong></p>\n'
     '<p style="padding-bottom:0.9em;"><span style="color:#b08d57;font-size:13px;">&#9662;</span> <strong>A patch, not a cream &mdash; shaped to fit.</strong></p>\n'
     '<p style="padding-bottom:0;"><span style="color:#b08d57;font-size:13px;">&#9662;</span> <strong>For the lines you frown into.</strong></p>\n'
     '</div>'),
]

ok, miss = 0, 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        ok += 1
    else:
        print(f'  MISS: {old[:80]!r}')
        miss += 1
print(f'Replacements: {ok} OK, {miss} MISS')

# ============================================================
# 6. Re-route all "collections/all" links to sign-up URL
#    (hero image link + hero CTA + final CTA = 3 instances)
# ============================================================
old_href = 'https://depology.com/collections/all'
n_links = html.count(old_href)
html = html.replace(old_href, SIGNUP_URL)
print(f'Rerouted {n_links} CTA links to sign-up URL')

# ============================================================
# 7. Sanity check
# ============================================================
leaks = re.findall(r'(?i)hydration', html)
if leaks:
    print(f'WARNING: {len(leaks)} "hydration" leftovers -- review HTML.')
else:
    print('Sanity: no "hydration" leftovers.')

OUT.write_text(html, encoding='utf-8')
print(f'Output: {OUT} ({len(html)} chars)')

if '--preview' in sys.argv:
    webbrowser.open(str(OUT))
    print('Opened in browser.')
