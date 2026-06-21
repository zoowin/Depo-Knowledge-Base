#!/usr/bin/env python3
"""Build July 4th 2026 campaign HTML from base_block_promo_sale_0520. Zero tokens.
Generates 5 promo emails (Kick Off / Activation Trio / Micro-dart / Creams / Last Call)
and patches the M2F sign-up launch hero image. Run: python3 tools/build_july4th.py
"""
import sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
BASE = (ROOT / 'tools/templates/base_block_promo_sale_0520.html').read_text(encoding='utf-8')
OUT = ROOT / 'production/html-output/2026-07'
OUT.mkdir(parents=True, exist_ok=True)

CDN = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/'
IMG = {
    'm3k': CDN+'44a0bdde-9c05-4c2b-854b-fe92895a2a6f.png',
    'matriplex': CDN+'420e0d8e-091d-4a94-ad76-e4c2bea97c46.png',
    'argireline': CDN+'160b6da8-e5a3-4202-bcef-a511922d5954.png',
    'microdart': CDN+'bdb87085-8617-43d8-be9b-f2cc405c16d1.png',
    'eyecream': CDN+'17182a51-02dc-4114-8b61-d82e29c46bcb.png',
    'night': CDN+'fb01a6c6-6cdf-4159-b40b-9f605f71ab65.png',
    'bodylotion': CDN+'65227851-df6d-4cbd-bcae-6a5c9e446619.png',
    'mop': CDN+'6db87278-16b2-48dd-bb79-837047b7142f.png',
}
DISC = 'https://depology.com/discount/JULY4TH10?redirect='
L = {
    'm3k3f2': DISC+'/products/offer-matrixyl-r-3000-triple-bundle',
    'arg3f2': DISC+'/products/offer-peptide-complex-10-serum-3-for-2',
    'microdart': DISC+'/products/deepcare-serum-infused-micro-dart-patches-lp1-t0',
    'matriplex': DISC+'/products/tri-active-matrixyl-complex-cream',
    'eyecream': DISC+'/products/peptide-complex-wrinkle-defense-eye-cream',
    'bodylotion': DISC+'/products/retinol-radiance-body-lotion',
    'trio': 'https://depology.com/products/peptide-activation-trio',
    'mop': 'https://depology.com/products/deepcare-r-microoperator-boosting-cream-beginner',
    'argstd': 'https://depology.com/products/argireline-anti-wrinkle-serum',
    'night': DISC+'/products/replenishing-night-under-eye-patch',
    'salepage': 'https://depology.com/discount/JULY4TH10?redirect=/pages/july4th-sale-2026',
}

def card(theme, badge, img, tag, sub, name, size, rate, now, old, save, link, cta='SHOP NOW'):
    if theme == 'red':
        border, bg, grad = '#C8102E', '#C8102E', 'linear-gradient(180deg, #E62844 0%, #C8102E 50%, #A30C24 100%)'
    else:
        border, bg, grad = '#1E3A8A', '#1E3A8A', 'linear-gradient(180deg, #2A4FA8 0%, #1E3A8A 50%, #15296F 100%)'
    price = f'<span style="color:#C8102E;font-weight:700;">{now}</span>'
    if old:
        price += f' <span style="color:#999;text-decoration:line-through;">{old}</span>'
    rate_html = f'&#9733;&#9733;&#9733;&#9733;&frac12; <span style="color:#888;">({rate})</span>' if rate else '&#9733;&#9733;&#9733;&#9733;&frac12;'
    size_tr = f'<tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:11px;color:#999;padding:0 12px 4px 12px;">{size}</td></tr>' if size else ''
    save_tr = f'<tr><td align="center" bgcolor="#C8102E" style="background:#C8102E;background-image:linear-gradient(90deg, #A30C24 0%, #DC2626 50%, #A30C24 100%);color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:1px;padding:7px 8px;">{save}</td></tr>' if save else ''
    return f'''<td class="mem-card-col" style="width:50%;vertical-align:top;padding:8px;" valign="top">
  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;border:2px solid {border};background:#FFFFFF;">
    <tbody>
      <tr><td align="center" bgcolor="{bg}" style="background:{bg};background-image:{grad};color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:1.5px;padding:10px 8px;">{badge}</td></tr>
      <tr><td style="padding:0;font-size:0;line-height:0;"><img alt="{name}" src="{img}" style="display:block;width:100%;height:auto;" width="296"/></td></tr>
      <tr><td align="center" style="font-family:Helvetica,Arial,sans-serif;font-size:11px;color:#666;padding:6px 12px 4px 12px;background:#F5F5F5;line-height:1.4;">{tag}</td></tr>
      <tr><td align="center" style="font-family:Helvetica,Arial,sans-serif;font-size:10px;font-style:italic;color:#555;padding:0 12px 8px 12px;background:#F5F5F5;line-height:1.3;">{sub}</td></tr>
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;color:#000;padding:10px 12px 4px 12px;line-height:1.3;">{name}</td></tr>
      {size_tr}
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:11px;color:#1E3A8A;padding:0 12px 4px 12px;">{rate_html}</td></tr>
      <tr><td align="left" style="font-family:Helvetica,Arial,sans-serif;font-size:14px;padding:4px 12px 10px 12px;">{price}</td></tr>
      {save_tr}
      <tr><td align="center" style="background:#000000;padding:0;"><a href="{link}" style="display:block;color:#FFF;text-decoration:none;font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:700;letter-spacing:1px;padding:12px 8px;" target="_blank">{cta}</a></td></tr>
    </tbody>
  </table>
</td>'''

def row(a, b):
    return ('<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">\n'
            f'<tbody><tr>\n{a}\n{b}\n</tr></tbody>\n</table>')

def build(e):
    html = BASE
    grid = '<!-- ROW 1 -->\n' + row(e['cards'][0], e['cards'][1]) + '\n\n<!-- ROW 2 -->\n' + row(e['cards'][2], e['cards'][3]) + '\n'
    i1 = html.index('<!-- ROW 1: Card 1 + Card 2 -->')
    i2 = html.index('</td>\n</tr></tbody>\n</table>\n</div>\n</td></tr></tbody>', i1)
    html = html[:i1] + grid + html[i2:]
    html = html.replace('MEM10', 'JULY4TH10').replace('memorialday-sale-2026', 'july4th-sale-2026')
    reps = [
        ('<title>Memorial Day Sale IS LIVE</title>', f"<title>{e['title']}</title>"),
        ('alt="Memorial Day Sale"', f'alt="{e["title"]}"'),
        ('https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/416e231c-6611-4b7b-babf-35745e0e61f7.jpeg', e['hero']),
        ('The Summer Sale You&#39;ve Been Waiting For&hellip; IS LIVE!', e['h1']),
        ('Memorial Day is here. We&#39;re offering our <span style="color:#C8102E;font-weight:700;">BIGGEST</span> summer deal &mdash; with new launches and our best-selling peptide series.', e['lead']),
        ('Extra 10% off site-wide with code <span style="text-decoration:underline;">JULY4TH10</span> for subscribers, 48 hours only.', e['code']),
        ('SHOP MEMORIAL DAY SALE', e['cta1']),
        ('With <span style="text-decoration:underline;">limited stock</span> available, now&#39;s the time to secure your picks!', e['closing']),
        ('SHOP ALL SALE', e['cta2']),
    ]
    miss = 0
    for old, new in reps:
        if old in html:
            html = html.replace(old, new)
        else:
            print(f"  MISS [{e['file']}]: {old[:50]}...")
            miss += 1
    (OUT / e['file']).write_text(html, encoding='utf-8')
    print(f"OK {e['file']} ({len(html)} chars, {miss} miss)")

EMAILS = [
    {  # 1. Kick Off
        'file': '20260701_July4th_KickOff.html', 'title': 'July 4th Sale IS LIVE',
        'hero': IMG and 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/41c521cb-ab36-403c-bf2d-7cc1c7f60f80.jpeg',
        'h1': 'Your July 4th Sale Is Live.',
        'lead': 'Our biggest summer event is here &mdash; best-sellers now 3-for-2, with 40% off across the whole site.',
        'code': 'Extra 10% off site-wide with code <span style="text-decoration:underline;">JULY4TH10</span>, 6 days only.',
        'cta1': 'SHOP THE SALE', 'cta2': 'SHOP ALL JULY 4TH',
        'closing': 'Everything&#39;s on sale this week &mdash; explore the full event before it ends.',
        'cards': [
            card('blue', '3 FOR 2', IMG['m3k'], 'Target Static Wrinkles', 'Collagen support, 28 days', 'Matrixyl&reg; 3000 Collagen Serum', '30ml*3', '2000+', '$80.00', '$120.00', 'SAVE $40', L['m3k3f2'], 'SHOP 3 FOR 2'),
            card('blue', '3 FOR 2', IMG['argireline'], 'Target Dynamic Wrinkles', 'Softens expression lines', 'Peptide Complex Argireline&trade; Serum', '30ml*3', '800+', '$98.00', '$147.00', 'SAVE $49', L['arg3f2'], 'SHOP 3 FOR 2'),
            card('red', 'UP TO 45% OFF', IMG['microdart'], 'Under-Eye Micro-darts', 'Retinol + Argireline', 'Deepcare+ Micro-dart Eye Patch', '', '2000+', 'Up to 45% OFF', '', 'NEWLY UPGRADED', L['microdart']),
            card('blue', '30&ndash;40% OFF', IMG['matriplex'], 'Firming Seal Step', 'Triple Matrixyl&reg;', 'Matriplex&trade; Peptide Intense Cream', '50ml', '', '30&ndash;40% OFF', '', '', L['matriplex']),
        ],
    },
    {  # 2. Activation Trio
        'file': '20260703_July4th_ActivationTrio.html', 'title': 'The Activation Trio - Now $89',
        'hero': 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/b55b16b6-5257-4023-b51e-6f31460bb31e.jpeg',
        'h1': 'The Activation Trio. Now $89.',
        'lead': 'Three formulas, one sequence &mdash; six weeks of skincare priming. Repeat orders beat our forecast.',
        'code': 'First 500 orders get a full-size Matrixyl&reg; 3000 <span style="text-decoration:underline;">free</span>.',
        'cta1': 'SHOP THE TRIO', 'cta2': 'SHOP THE TRIO',
        'closing': 'Six weeks is enough to know what a routine does. Start yours &mdash; gift included, while the first 500 last.',
        'cards': [
            card('red', '$89 &middot; FREE M3K', IMG['mop'], 'Skincare Priming &middot; 3 Steps', 'MOP + MPS + Eye Cream', 'Peptide Activation Trio', 'Full routine', '300+', '$89.00', '$135.00', '+ FREE MATRIXYL&reg; 3000', L['trio'], 'SHOP THE TRIO'),
            card('blue', 'STEP 1', IMG['mop'], 'Primes the skin', 'Surface tech, week 1-2', 'Deepcare+ MicroOperator Cream', '', '', 'In the Trio', '', '', L['mop'], 'LEARN MORE'),
            card('blue', 'STEP 2', IMG['argireline'], 'Builds the peptide layer', 'Week 3-4 texture shift', 'Argireline&trade; MPS Serum', '', '', 'In the Trio', '', '', L['argstd'], 'LEARN MORE'),
            card('blue', 'STEP 3', IMG['eyecream'], 'Daily eye care', 'Week 5-6 maintenance', 'Peptide Complex Eye Cream', '', '', 'In the Trio', '', '', L['eyecream'], 'LEARN MORE'),
        ],
    },
    {  # 3. Micro-dart peak day
        'file': '20260704_July4th_HeroDay_Microdart.html', 'title': 'Happy 4th - The Sale Peaks Today',
        'hero': 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/b5f836f5-bf65-45e6-a87d-45176667c608.jpeg',
        'h1': 'Happy 4th. The Sale Peaks Today.',
        'lead': 'Our micro-dart eye patch just got an upgrade &mdash; retinol + argireline in 1,000+ self-dissolving darts.',
        'code': 'Up to 45% off today, the event&#39;s lowest. Extra 10% on everything else with <span style="text-decoration:underline;">JULY4TH10</span>.',
        'cta1': 'SHOP THE 4TH', 'cta2': 'SHOP ALL JULY 4TH',
        'closing': 'The 4th comes once a year &mdash; and so does this price on our micro-darts.',
        'cards': [
            card('red', 'UP TO 45% OFF', IMG['microdart'], 'Newly upgraded', 'Retinol + Argireline darts', 'Deepcare+ Micro-dart Eye Patch', '', '2000+', 'Up to 45% OFF', '', 'LOWEST OF THE EVENT', L['microdart']),
            card('blue', '3 FOR 2', IMG['argireline'], 'Target Dynamic Wrinkles', 'Softens expression lines', 'Peptide Complex Argireline&trade; Serum', '30ml*3', '800+', '$98.00', '$147.00', 'SAVE $49', L['arg3f2'], 'SHOP 3 FOR 2'),
            card('red', '$89 &middot; FREE M3K', IMG['mop'], 'Skincare Priming Trio', '3-step routine', 'Peptide Activation Trio', 'Full routine', '300+', '$89.00', '$135.00', '+ FREE M3K', L['trio'], 'SHOP THE TRIO'),
            card('blue', '30&ndash;40% OFF', IMG['night'], 'Overnight eye care', 'Replenish while you sleep', 'Replenishing Night Under Eye Patch', '', '', '30&ndash;40% OFF', '', '', L['night']),
        ],
    },
    {  # 4. Creams
        'file': '20260705_July4th_Creams.html', 'title': 'The Seal Step, On Sale',
        'hero': 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/7f662d51-ad99-4fcd-832b-dee81d870607.jpeg',
        'h1': 'The Seal Step, On Sale.',
        'lead': 'Serums do the work &mdash; but without a seal it fades. That&#39;s the job of a cream.',
        'code': 'Creams 30&ndash;40% off this weekend, plus 40% sitewide with <span style="text-decoration:underline;">JULY4TH10</span>.',
        'cta1': 'SHOP THE CREAMS', 'cta2': 'SHOP ALL JULY 4TH',
        'closing': 'A serum starts it; a cream keeps it &mdash; and don&#39;t forget your body in sandal season.',
        'cards': [
            card('blue', '30&ndash;40% OFF', IMG['matriplex'], 'Firming seal step', 'Triple Matrixyl&reg;', 'Matriplex&trade; Peptide Intense Cream', '50ml', '', '30&ndash;40% OFF', '', '', L['matriplex']),
            card('blue', '30&ndash;40% OFF', IMG['eyecream'], 'Delicate eye zone', 'Lightweight argireline', 'Peptide Complex Eye Cream', '15ml', '', '30&ndash;40% OFF', '', '', L['eyecream']),
            card('blue', '3 FOR 2', IMG['m3k'], 'Pair with the serum it seals', 'Collagen support, 28 days', 'Matrixyl&reg; 3000 Collagen Serum', '30ml*3', '2000+', '$80.00', '$120.00', 'SAVE $40', L['m3k3f2'], 'SHOP 3 FOR 2'),
            card('red', 'BODY &middot; 30&ndash;40% OFF', IMG['bodylotion'], 'Summer skin', '0.05% retinol, ultra-size', 'Retinol Radiance Body Lotion', '', '', '30&ndash;40% OFF', '', 'SANDAL SEASON', L['bodylotion']),
        ],
    },
    {  # 5. Last Call
        'file': '20260707_July4th_LastCall.html', 'title': 'Last Call - Ends Tonight',
        'hero': 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/57adcc65-e773-4dbb-9b1e-f1149824176e.jpeg',
        'h1': 'Last Call. Ends Tonight.',
        'lead': 'The July 4th Sale closes tonight &mdash; everything moving fastest is rounded up below.',
        'code': '40% off + extra 10% with <span style="text-decoration:underline;">JULY4TH10</span> &mdash; gone at midnight ET.',
        'cta1': 'SHOP BEFORE IT ENDS', 'cta2': 'SHOP THE LAST HOURS',
        'closing': 'At midnight the codes switch off and prices reset. This is the last call.',
        'cards': [
            card('red', 'UP TO 45% OFF', IMG['microdart'], 'Lowest of the event', 'Retinol + Argireline darts', 'Deepcare+ Micro-dart Eye Patch', '', '2000+', 'Up to 45% OFF', '', 'ENDS TONIGHT', L['microdart']),
            card('blue', '3 FOR 2', IMG['argireline'], 'Target Dynamic Wrinkles', 'Stock before it&#39;s gone', 'Peptide Complex Argireline&trade; Serum', '30ml*3', '800+', '$98.00', '$147.00', 'SAVE $49', L['arg3f2'], 'SHOP 3 FOR 2'),
            card('red', '$89 &middot; FREE M3K', IMG['mop'], 'Last chance this season', '3-step priming routine', 'Peptide Activation Trio', 'Full routine', '300+', '$89.00', '$135.00', '+ FREE M3K', L['trio'], 'SHOP THE TRIO'),
            card('blue', '3 FOR 2', IMG['m3k'], 'Target Static Wrinkles', 'Routine staple', 'Matrixyl&reg; 3000 Collagen Serum', '30ml*3', '2000+', '$80.00', '$120.00', 'SAVE $40', L['m3k3f2'], 'SHOP 3 FOR 2'),
        ],
    },
]

for e in EMAILS:
    build(e)

# Patch M2F sign-up launch hero image (its own white-bg HTML, not this template)
m2f = OUT / '20260701_M2F_Launch_SignupExclusive.html'
if m2f.exists():
    h = m2f.read_text(encoding='utf-8')
    old_id = '837cb32f-0a5c-4de0-aa36-dbaeea5c99ae'
    new_id = 'ec3c52a4-6669-481b-909f-50c150dda060'
    if old_id in h:
        m2f.write_text(h.replace(old_id, new_id), encoding='utf-8')
        print(f'OK M2F hero patched -> {new_id}')
    else:
        print('  NOTE: M2F old hero id not found; check hero manually')
else:
    print('  NOTE: M2F html not found in 2026-07/')

print('\nDone. Preview files in production/html-output/2026-07/')
