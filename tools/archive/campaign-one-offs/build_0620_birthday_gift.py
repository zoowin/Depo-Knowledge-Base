#!/usr/bin/env python3
"""Build 20260620_Birthday_Gift.html from 0408 white-bg base.

Birthday opener + BIRTHDAY10 code (3 days, through 6/22 birthday).
Structure changes vs 0408:
  - REMOVE Section 4 (secondary image) + Section 5 (checklist) in one cut
  - REPLACE Section 6 (product cards) with Gift Block
    (cream/gold gradient + dart-pattern + code display + CTA)
  - KEEP Section 7 closing (copy swapped) + INSERT P.S. early-access row before Footer
  - INSERT Eyebrow above Hero Headline
All shop links -> Shopify discount URL (auto-apply BIRTHDAY10).
"""
import sys, io, re, webbrowser
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'production' / 'html-output' / '2026-04' / '20260408_Hydration_Hierarchy.html'
OUT = ROOT / 'production' / 'html-output' / '2026-06' / '20260620_Birthday_Gift.html'

HERO_IMG = '357e56df-d955-46a5-9084-5fbaf5df99dd.jpeg'
DISCOUNT_URL = 'https://depology.com/discount/BIRTHDAY10?redirect=/collections/all'
EARLY_ACCESS_URL = 'https://depology.com/pages/early-access'
DART_PATTERN = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fa3e0ac6-a943-451f-a5c9-dd62cc418cf6.png'

html = SRC.read_text(encoding='utf-8')

# ---------- 1. Remove Section 4 + Section 5 (one cut: sec4 start -> sec6 start) ----------
sec4 = '\n\n<!-- ============================================ -->\n<!-- SECTION 4: SECONDARY ATMOSPHERE IMAGE        -->'
sec6 = '\n\n<!-- ============================================ -->\n<!-- SECTION 6: PRODUCT CARDS (white bg, gray cards) -->'
i4, i6 = html.find(sec4), html.find(sec6)
if i4 == -1 or i6 == -1 or i4 > i6:
    raise SystemExit(f'Section markers wrong: i4={i4}, i6={i6}')
html = html[:i4] + html[i6:]
print('Removed Section 4 + Section 5')

# ---------- 2. Replace Section 6 (product cards) with Gift Block ----------
GIFT_BLOCK = f'''<!-- ============================================ -->
<!-- SECTION 6: GIFT BLOCK (cream/gold + code)    -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="kl-section" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#f7f2ea;background-color:#f7f2ea;background-image:linear-gradient(180deg,#ffffff 0%,#f3ead9 100%);margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#f7f2ea;background-image:url('{DART_PATTERN}'),linear-gradient(180deg,#ffffff 0%,#f3ead9 100%);background-repeat:no-repeat,no-repeat;background-size:100% auto,100% 100%;background-position:center top,center top;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:54px 40px 48px 40px;text-align:center;">

<!-- Block eyebrow -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:12px;font-weight:700;letter-spacing:4px;color:#b08d57;text-transform:uppercase;padding-bottom:10px;">Your Birthday Gift</div>

<!-- Block headline -->
<div style="font-family:TimesNewRoman,'Times New Roman',Times,Georgia,serif;font-size:32px;color:#0e0e0e;line-height:1.2;padding-bottom:14px;">10% off everything.</div>

<!-- Gold accent rule -->
<div style="width:40px;border-top:1px solid #b08d57;margin:0 auto 20px auto;font-size:0;line-height:0;">&nbsp;</div>

<!-- Block copy -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:16px;color:#5a5145;line-height:1.6;padding-bottom:24px;max-width:440px;margin:0 auto;">72 hours only, through Monday, June 22. The code applies automatically at checkout.</div>

<!-- Code display -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 26px auto;">
<tbody><tr>
<td align="center" style="border:2px dashed #b08d57;border-radius:6px;padding:14px 34px;background:#fffdf8;">
<span style="font-family:'Courier New',Courier,monospace;font-size:24px;font-weight:700;letter-spacing:5px;color:#0e0e0e;">BIRTHDAY10</span>
</td>
</tr></tbody>
</table>

<!-- CTA button -->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto;">
<tbody><tr>
<td align="center" bgcolor="#0e0e0e" style="border-radius:2px;background:#0e0e0e;">
<a href="{DISCOUNT_URL}" target="_blank" style="color:#ffffff;text-decoration:none;display:inline-block;background:#0e0e0e;font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:16px;font-weight:700;line-height:100%;letter-spacing:2px;padding:16px 38px;border-radius:2px;">CLAIM YOUR GIFT &rarr;</a>
</td>
</tr></tbody>
</table>

<!-- Under-button small text -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:12px;color:#8a7a64;line-height:1.5;padding-top:16px;">Ends Monday at 11:59 PM ET.</div>

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
j6, j7 = html.find(sec6_marker), html.find(sec7_marker)
if j6 == -1 or j7 == -1:
    raise SystemExit(f'Gift block replace failed: j6={j6}, j7={j7}')
html = html[:j6] + GIFT_BLOCK + html[j7:]
print('Replaced product cards with Gift Block')

# ---------- 3. Insert P.S. early-access row before Footer ----------
PS_BLOCK = '''<!-- ============================================ -->
<!-- P.S. EARLY ACCESS CROSS-PROMO                -->
<!-- ============================================ -->
<table align="center" border="0" cellpadding="0" cellspacing="0" class="kl-section" role="presentation" style="width:100%;">
<tbody><tr><td>
<div style="margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
<div style="background:#FFFFFF;background-color:#FFFFFF;margin:0px auto;max-width:600px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;background-color:#FFFFFF;width:100%;">
<tbody><tr>
<td style="direction:ltr;font-size:0px;padding:6px 50px 30px 50px;text-align:center;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:13px;color:#888888;line-height:1.6;font-style:italic;">P.S. Something new is coming in July. <a href="''' + EARLY_ACCESS_URL + '''" target="_blank" style="color:#b08d57;text-decoration:underline;">Join the early-access list</a> to see it first.</div>
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
footer_marker = '<!-- ============================================ -->\n<!-- FOOTER'
kf = html.find(footer_marker)
if kf == -1:
    raise SystemExit('Footer marker not found')
html = html[:kf] + PS_BLOCK + html[kf:]
print('Inserted P.S. cross-promo row')

# ---------- 4. Eyebrow above Hero Headline ----------
EYEBROW_BLOCK = '''<!-- Eyebrow -->
<div class="mj-column-per-100 mj-outlook-group-fix component-wrapper" style="font-size:0px;text-align:left;direction:ltr;vertical-align:top;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;" width="100%">
<tbody><tr>
<td style="background-color:#FFFFFF;vertical-align:top;padding:30px 16px 0px 16px;">
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:11px;font-weight:700;letter-spacing:4px;color:#b08d57;text-transform:uppercase;text-align:center;">Birthday Weekend &middot; Turning Five</div>
</td>
</tr></tbody>
</table>
</div>

<!-- Headline -->'''
if '<!-- Headline -->' not in html:
    raise SystemExit('Headline marker not found')
html = html.replace('<!-- Headline -->', EYEBROW_BLOCK, 1)
html = html.replace('<td style="background-color:#FFFFFF;vertical-align:top;padding:24px 16px 8px 16px;">',
                    '<td style="background-color:#FFFFFF;vertical-align:top;padding:12px 16px 8px 16px;">', 1)
print('Injected Eyebrow')

# ---------- 5. Content replacements ----------
replacements = [
    ('<title></title>', "<title>It's our birthday. The gift is yours.</title>"),
    ('alt="The Hydration Hierarchy"', 'alt="Our 5th birthday - 10% off everything"'),
    ('91d179ef-00c8-44e8-b396-8204ae4a28ca.jpeg', HERO_IMG),

    ('The Hydration Hierarchy.', 'It&rsquo;s our birthday.<br/>The gift is yours.'),
    ('Your skin needs layers, not puddles.',
     'We turn five next Monday. The celebration starts today.'),
    ('\nSHOP THE LAYERS\n', '\nUNWRAP 10% OFF\n'),

    ("Wet Isn't Hydrated.", 'Thank you for five years.'),

    ("""<p style="padding-bottom:1em;">Splashing water on your face feels refreshing. But within minutes, your skin can feel tighter than before. That's evaporation — not hydration.</p>
<p style="padding-bottom:1em;">True hydration works in layers: attract moisture (humectants), nourish the barrier (emollients), and seal it in (occlusives). Skip a layer, and the others lose their effect.</p>
<p style="padding-bottom:0;">The right routine doesn't just add water — it teaches your skin to hold onto it. That's where smart formulation makes all the difference.</p>""",

     '<p style="padding-bottom:1em;">Next Monday, D&#275;pology turns five. Every formula we&rsquo;ve made in those five years was shaped by the people who use it. That means you.</p>\n'
     '<p style="padding-bottom:0;">So this weekend, the gift goes to you. Take 10% off everything for the next 72 hours. Every serum, every patch, every cream.</p>'),

    ("Hydration isn't a step.<br/>It's a system. Build yours today.",
     'On Monday we&rsquo;ll send you our birthday letter.<br/>Today, just enjoy the gift.'),
    ('BUILD YOUR HYDRATION ROUTINE', 'UNWRAP 10% OFF'),
]
ok, miss = 0, 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        ok += 1
    else:
        print(f'  MISS: {old[:70]!r}')
        miss += 1
print(f'Replacements: {ok} OK, {miss} MISS')

# ---------- 6. Reroute shop links to discount URL ----------
n = html.count('https://depology.com/collections/all')
html = html.replace('https://depology.com/collections/all', DISCOUNT_URL)
print(f'Rerouted {n} links to discount URL')

# ---------- 7. Sanity ----------
leaks = re.findall(r'(?i)hydration', html)
print('Sanity hydration leftovers:', len(leaks))
OUT.write_text(html, encoding='utf-8')
print(f'Output: {OUT} ({len(html)} chars)')

if '--preview' in sys.argv:
    webbrowser.open(str(OUT))
