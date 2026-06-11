#!/usr/bin/env python3
"""Build 20260424_Tolerance_Myth.html from 0403 Easter base (black 3-card)."""
import sys, io, re, webbrowser
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'production' / 'html-output' / '2026-04' / '20260403_Easter_Sale_Opening.html'
OUT = ROOT / 'production' / 'html-output' / '2026-04' / '20260424_Tolerance_Myth.html'

html = SRC.read_text(encoding='utf-8')

# ---------- 1. Remove discount code block (educational — no promo code) ----------
discount_block_start = html.find('<!-- Discount Code Block: EASTER20 -->')
discount_block_end = html.find('<!-- Hero CTA: SHOP THE SALE -->')
assert discount_block_start != -1 and discount_block_end != -1, 'Could not locate discount block'
html = html[:discount_block_start] + html[discount_block_end:]
print(f'Removed discount code block ({discount_block_end - discount_block_start} chars)')

# ---------- 2. Content replacements ----------
replacements = [
    # --- Title ---
    ('<title></title>', '<title>The Tolerance Myth</title>'),

    # --- Hero image (alt + src) ---
    ('alt="Your Easter Treat Is Here"',
     'alt="The Tolerance Myth"'),
    ('https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/78c77f2c-77ce-41cf-a431-d8ea88c5ef8b.jpeg',
     'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/4ef41637-c909-45b2-9055-ec4af3ad0795.jpeg'),

    # --- Hero headline + subheadline ---
    ('Your Easter Treat Is Here.', 'The Tolerance Myth.'),
    ('20% off everything. This Easter weekend only.',
     '&ldquo;My skin got used to it.&rdquo; Science says otherwise.'),

    # --- Hero CTA ---
    ('https://depology.com/discount/EASTER20?redirect=/collections/all-products"'
     ' style="color:#000; text-decoration:none; display:inline-block; background:#FFF;'
     ' font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif; font-size:20px;'
     ' font-weight:600; line-height:100%; letter-spacing:0; margin:0; padding:15px 50px;'
     ' border-radius:2px" target="_blank">\nSHOP THE SALE',
     'https://depology.com/"'
     ' style="color:#000; text-decoration:none; display:inline-block; background:#FFF;'
     ' font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif; font-size:20px;'
     ' font-weight:600; line-height:100%; letter-spacing:0; margin:0; padding:15px 50px;'
     ' border-radius:2px" target="_blank">\nSEE THE SCIENCE'),

    # --- Body headline + body copy ---
    ('Invest in Your Skin.', 'Your Serum Didn&rsquo;t Stop Working.'),
    ("Spring is the perfect time to reset your routine. New season, new approach to your skin's needs.<br/><br/>Whether you're starting fresh or stocking up on your favorites, this weekend everything on site is 20% off \u2014 use code EASTER20 at checkout.",
     'Ever feel like a product that once transformed your skin just&hellip; stops? It&rsquo;s one of the most common reasons people switch products. But here&rsquo;s the thing &mdash; peptides don&rsquo;t cause tolerance.<br/><br/>'
     'What actually happens: the initial dramatic improvement levels off. Your skin reached a new baseline. The product is still working &mdash; it&rsquo;s maintaining that improvement. Remove it, and you&rsquo;ll see the difference quickly.<br/><br/>'
     'The real mistake isn&rsquo;t that the product &ldquo;stopped.&rdquo; It&rsquo;s stopping the product and losing the gains you already made.'),

    # --- Section title --- (use surrounding newlines to skip the HTML comment)
    ('\nCUSTOMER FAVORITES\n', '\nStay The Course. See The Results.\n'),

    # --- CARD 1: Peptide Duo → Argireline Serum ---
    # Remove red promo label div entirely; use role-label text as the title (per Figma)
    ('<div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#cc0000;text-transform:uppercase;margin-bottom:6px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">20% OFF \u2014 USE EASTER20</div>\n<div style="font-size:17px;font-weight:700;color:#000000;margin-bottom:10px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">Peptide Duo + Caviar Multi-Balm Serum Stick',
     '<div style="font-size:17px;font-weight:700;color:#000000;margin-bottom:10px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">The Daily Defense (Argireline&trade;)'),
    ('Two best-selling peptide serums + a luxurious caviar serum stick \u2014 your complete treatment set in one box.',
     'Designed for daily, long-term use. Argireline&trade; continues to support smoother expression lines with every application &mdash; no tolerance buildup.'),
    # remove price line for card 1 (unique via $75.00)
    ('<div style="font-size:15px;color:#000000;margin-bottom:16px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;"><span style="text-decoration:line-through;color:#999999;">$75.00</span> &nbsp;<span style="font-weight:700;color:#cc0000;">$60.00 with code</span></div>\n',
     ''),
    ('https://depology.com/discount/EASTER20?redirect=/products/peptide-duo-free-caviar-multi-balm-serum-stick',
     'https://depology.com/products/argireline-anti-wrinkle-serum'),
    ('SHOP PEPTIDE + CAVIAR SET', 'SHOP ARGIRELINE SERUM'),
    # card 1 image: peptide-duo-caviar bundle → argireline
    ('https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/562035fe-955a-42d6-8210-56bf78c79ebb.png',
     '__CARD1_ARGIRELINE_IMG__'),  # placeholder so we can reuse duo img in card 3

    # --- CARD 2: Micro-dart Patches → Matrixyl Serum ---
    ('<div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#cc0000;text-transform:uppercase;margin-bottom:6px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">20% OFF \u2014 USE EASTER20</div>\n<div style="font-size:17px;font-weight:700;color:#000000;margin-bottom:10px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">Micro-dart Eye Patches',
     '<div style="font-size:17px;font-weight:700;color:#000000;margin-bottom:10px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">The Foundation (Matrixyl&reg;)'),
    ('Self-dissolving micro-darts deliver actives below the surface. Non-invasive, at-home eye treatment. Now 20% off.',
     'Peptide-powered hydration and wrinkle support that works best over time. Clinically shown results at 28 days &mdash; and beyond.'),
    ('https://depology.com/discount/EASTER20?redirect=/products/deepcare-serum-infused-micro-dart-patches-lp1-t0',
     'https://depology.com/products/depology-matrixyl-3000-serum'),
    ('SHOP MICRO-DART PATCHES', 'SHOP MATRIXYL SERUM'),
    # card 2 image: micro-dart → matrixyl
    ('https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/bdb87085-8617-43d8-be9b-f2cc405c16d1.png',
     'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/44a0bdde-9c05-4c2b-854b-fe92895a2a6f.png'),

    # --- CARD 3: Bakuchiol Stick → Peptide Duo Bundle ---
    ('<div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#cc0000;text-transform:uppercase;margin-bottom:6px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">20% OFF \u2014 USE EASTER20</div>\n<div style="font-size:17px;font-weight:700;color:#000000;margin-bottom:10px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">Bakuchiol Smoothing Serum Stick',
     '<div style="font-size:17px;font-weight:700;color:#000000;margin-bottom:10px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;">The Full Commitment (Bundle)'),
    ('Plant-powered retinol alternative in a mess-free stick. Glide on for targeted fine-line care \u2014 no irritation, no purging.',
     'Ready to commit? Matrixyl&reg; Serum + Argireline&trade; Serum + a bonus Caviar Stick. The full peptide routine in one set &mdash; $109, and consistency built in.'),
    # remove price line for card 3 (unique via $30.00)
    ('<div style="font-size:15px;color:#000000;margin-bottom:16px;font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;"><span style="text-decoration:line-through;color:#999999;">$30.00</span> &nbsp;<span style="font-weight:700;color:#cc0000;">$24.00 with code</span></div>\n',
     ''),
    ('https://depology.com/discount/EASTER20?redirect=/products/bakuchiol-smoothing-serum-stick',
     'https://depology.com/products/peptide-duo-free-caviar-multi-balm-serum-stick'),
    ('SHOP BAKUCHIOL STICK', 'SHOP THE PEPTIDE DUO'),
    # card 3 image: bakuchiol → peptide duo bundle (reuse original card 1 img)
    ('https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/642001c5-54b0-4900-90fd-bc0c5dc37dc0.png',
     'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/562035fe-955a-42d6-8210-56bf78c79ebb.png'),

    # resolve card 1 placeholder → Argireline image
    ('__CARD1_ARGIRELINE_IMG__',
     'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/160b6da8-e5a3-4202-bcef-a511922d5954.png'),

    # --- Closing copy ---
    ('20% off sitewide. This weekend only.',
     'The best skincare results come from patience, not product-hopping. Stay consistent.'),

    # --- Final CTA ---
    ('https://depology.com/discount/EASTER20?redirect=/collections/all-products',
     'https://depology.com/collections/all-products'),
    ('SHOP ALL PRODUCTS', 'KEEP BUILDING YOUR RESULTS'),
]

ok, miss = 0, 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)  # replace first occurrence only for safety
        ok += 1
    else:
        print(f'  MISS: {old[:80]!r}')
        miss += 1
print(f'Replacements: {ok} OK, {miss} MISS')

# ---------- 3. Product card font-size bumps (desktop readability) ----------
# Applied to all 3 cards uniformly via replace_all.
font_bumps = [
    # Role label: 11px -> 13px
    ('font-size:11px;font-weight:700;letter-spacing:1px;color:#cc0000',
     'font-size:13px;font-weight:700;letter-spacing:1px;color:#cc0000'),
    # Product name: 17px -> 20px
    ('font-size:17px;font-weight:700;color:#000000;margin-bottom:10px',
     'font-size:20px;font-weight:700;color:#000000;margin-bottom:10px'),
    # Description (margin-bottom:6px variant): 14px -> 16px
    ('font-size:14px;color:#444444;line-height:1.5;margin-bottom:6px',
     'font-size:16px;color:#444444;line-height:1.5;margin-bottom:6px'),
    # Description (margin-bottom:16px variant): 14px -> 16px
    ('font-size:14px;color:#444444;line-height:1.5;margin-bottom:16px',
     'font-size:16px;color:#444444;line-height:1.5;margin-bottom:16px'),
    # CTA button: 13px -> 15px
    ('font-size:13px;font-weight:700;letter-spacing:1px',
     'font-size:15px;font-weight:700;letter-spacing:1px'),
]
for old, new in font_bumps:
    n = html.count(old)
    html = html.replace(old, new)
    print(f'  Font bump x{n}: {old[10:40]}...')

# Sanity: no remaining Easter/EASTER20 mentions
leftovers = re.findall(r'EASTER20|Easter', html)
if leftovers:
    print(f'WARNING: leftover promo tokens: {set(leftovers)}')

OUT.write_text(html, encoding='utf-8')
print(f'Output: {OUT} ({len(html)} chars)')

if '--preview' in sys.argv:
    webbrowser.open(str(OUT))
    print('Opened in browser.')
