#!/usr/bin/env python3
"""Build July 4th 2026 campaign HTML from base_block_promo_sale_0520. Zero tokens.
5 promo emails (Kick Off / Activation Trio / Micro-dart / Creams / Last Call) + M2F hero patch.
Pricing per July 4th matrix (00_July4th_Sale_Plan.md). Product cards link to offer product pages.
Run: python3 tools/archive/campaign-one-offs/build_july4th.py
"""
import sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
BASE = (ROOT / 'tools/templates/base_block_promo_sale_0520.html').read_text(encoding='utf-8')
OUT = ROOT / 'production/html-output/2026-07'
OUT.mkdir(parents=True, exist_ok=True)

CDN = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/'
IMG = {  # July 4th campaign images (Codex image-gen, navy July 4th bg)
    'm3k': CDN+'dd4f2dc6-46ef-4d9c-ae61-e7ffecb83ea0.jpeg',
    'argireline': CDN+'4f625167-8a29-4432-9bb2-d124fa6393bc.jpeg',
    'microdart': CDN+'9c71e6c9-47a0-4e0c-8250-8370aeada422.jpeg',
    'matriplex': CDN+'df6cd138-c092-4ed8-9699-e66ee802086a.jpeg',
    'eyecream': CDN+'353d6dfe-1422-42c5-8d10-3f638c5f49b4.jpeg',
    'trio': CDN+'cd88931b-17f5-405c-be06-0f56119c8cba.jpeg',
    'mop': CDN+'3f73cfd6-7b84-40f0-a118-e8a16de4b58f.jpeg',
    'night': CDN+'a3bf45b7-3f2c-43f2-b5a9-5785b1bd7b25.jpeg',
    'rbltrio': CDN+'559c3ffa-cb9f-4c3a-a35e-2c36241c8381.jpeg',
    'staticduo': CDN+'5a0b5318-c3cf-47b7-b3af-25cb64a0fb34.jpeg',
    'dynamicduo': CDN+'f8102291-a2ef-47b3-8b1e-e7e297cf3248.jpeg',
    'opuntia': CDN+'df7f7e7a-b3a1-4121-a11b-ac3ab3e5d3ec.jpeg',
}
PROD = 'https://depology.com/discount/JULY4TH10?redirect=/products/'  # 全挂自动折扣码，结账自动应用
L = {  # product cards = discount link -> offer product page (auto-apply JULY4TH10)
    'm3k3f2': PROD+'offer-matrixyl-r-3000-triple-bundle',
    'arg3f2': PROD+'offer-peptide-complex-10-serum-3-for-2',
    'microdart': PROD+'offer-deepcare-serum-infused-micro-dart-patches',
    'trio': PROD+'peptide-activation-trio',
    'matriplex': PROD+'offer-matriplex-peptide-intense-cream-copy',
    'eyecream': PROD+'offer-peptide-complex-wrinkle-defense-eye-cream-copy',
    'mop': PROD+'deepcare-r-microoperator-boosting-cream-beginner',
    'argstd': PROD+'argireline-anti-wrinkle-serum',
    'night': PROD+'offer-replenishing-night-under-eye-patch',
    'rbltrio': PROD+'offer-retinol-body-firming-lotion-trio',
    'staticduo': PROD+'static-wrinkle-repair-duo',
    'dynamicduo': PROD+'dynamic-wrinkle-defense-duo',
    'opuntia': 'https://depology.com/discount/JULY4TH10?redirect=/products/opuntia-c-relief-cleansing-balm',
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

EMPTY = '<td class="mem-card-col" style="width:50%;padding:8px;"></td>'

def build(e):
    html = BASE
    cards = e['cards']
    rows = ''
    for i in range(0, len(cards), 2):
        b = cards[i+1] if i+1 < len(cards) else EMPTY
        rows += f'<!-- ROW {i//2+1} -->\n' + row(cards[i], b) + '\n\n'
    grid = rows.rstrip() + '\n'
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
    print(f"OK {e['file']} ({len(html)} chars, {len(cards)} cards, {miss} miss)")

# --- card library (July 4th pricing) ---
M3K3F2 = card('blue', '3 FOR 2', IMG['m3k'], 'Target Static Wrinkles', 'Collagen support, 28 days', 'Matrixyl&reg; 3000 Collagen Serum', '30ml*3', '2000+', '$80.00', '$120.00', 'SAVE $40', L['m3k3f2'], 'SHOP 3 FOR 2')
ARG3F2 = card('blue', '3 FOR 2', IMG['argireline'], 'Target Dynamic Wrinkles', 'Softens expression lines', 'Peptide Complex Argireline&trade; Serum', '30ml*3', '800+', '$98.00', '$147.00', 'SAVE $49', L['arg3f2'], 'SHOP 3 FOR 2')
MICRODART = card('red', '40% OFF', IMG['microdart'], 'Newly upgraded (retinol)', '1,000+ self-dissolving darts', 'Deepcare+ Micro-dart Eye Patch', '16 pairs', '2000+', '$86.00', '$144.00', 'SAVE $58', L['microdart'])
TRIO = card('red', '$89 &middot; SAVE $46', IMG['trio'], 'Skincare Priming &middot; 3 Steps', 'MOP + MPS + Eye Cream', 'Peptide Activation Trio', 'Full routine', '300+', '$89.00', '$135.00', 'SAVE $46', L['trio'], 'SHOP THE TRIO')
MATRIPLEX = card('blue', '30% OFF', IMG['matriplex'], 'Firming seal step', 'Triple Matrixyl&reg;', 'Matriplex&trade; Peptide Intense Cream', '50ml', '', '$43.00', '$62.00', 'SAVE $19', L['matriplex'])
EYECREAM = card('blue', '30% OFF', IMG['eyecream'], 'Delicate eye zone', 'Lightweight argireline', 'Peptide Complex Eye Cream', '15ml', '', '$36.00', '$52.00', 'SAVE $16', L['eyecream'])
NIGHT = card('blue', '25% OFF', IMG['night'], 'Overnight eye care', 'Replenish while you sleep', 'Replenishing Night Under Eye Patch', '60 patches', '', '$27.00', '$36.00', 'SAVE $9', L['night'])
RBLTRIO = card('red', 'BODY &middot; 33% OFF', IMG['rbltrio'], 'Summer skin (sandal season)', '0.05% retinol, ultra-size x3', 'Retinol Radiance Body Lotion Trio', '3-pack', '', '$52.00', '$78.00', 'SAVE $26', L['rbltrio'])
STATICDUO = card('blue', '30% OFF &middot; DUO', IMG['staticduo'], 'Static lines duo', 'M1 patch + M3K serum', 'Static Wrinkle Repair Duo', 'Bundle', '', '$53.00', '$76.00', 'SAVE $23', L['staticduo'])
DYNAMICDUO = card('blue', '30% OFF &middot; DUO', IMG['dynamicduo'], 'Dynamic lines duo', 'M1 patch + Argireline', 'Dynamic Wrinkle Defense Duo', 'Bundle', '', '$59.00', '$85.00', 'SAVE $26', L['dynamicduo'])
OPUNTIA = card('red', '30% OFF &middot; CLEARANCE', IMG['opuntia'], 'Gentle cleansing balm', 'Melts away makeup &amp; SPF', 'Opuntia-C Relief Cleansing Balm', '100ml', '', '$25.20', '$36.00', 'SAVE $11 + JULY4TH10', L['opuntia'])
STEP1 = card('blue', 'STEP 1', IMG['mop'], 'Primes the skin', 'Surface tech, week 1-2', 'Deepcare+ MicroOperator Cream', '', '', 'In the Trio', '', '', L['mop'], 'LEARN MORE')
STEP2 = card('blue', 'STEP 2', IMG['argireline'], 'Builds the peptide layer', 'Week 3-4 texture shift', 'Argireline&trade; MPS Serum', '', '', 'In the Trio', '', '', L['argstd'], 'LEARN MORE')
STEP3 = card('blue', 'STEP 3', IMG['eyecream'], 'Daily eye care', 'Week 5-6 maintenance', 'Peptide Complex Eye Cream', '', '', 'In the Trio', '', '', L['eyecream'], 'LEARN MORE')

EMAILS = [
    {'file': '20260701_July4th_KickOff.html', 'title': 'July 4th Sale IS LIVE',
     'hero': CDN+'41c521cb-ab36-403c-bf2d-7cc1c7f60f80.jpeg',
     'h1': 'Your July 4th Sale Is Live.',
     'lead': 'Our biggest summer event is here &mdash; best-sellers now 3-for-2, with up to 50% off across the site.',
     'code': 'Extra 10% off site-wide with code <span style="text-decoration:underline;">JULY4TH10</span> &mdash; all week long.',
     'cta1': 'SHOP THE SALE', 'cta2': 'SHOP ALL JULY 4TH',
     'closing': 'Everything&#39;s on sale this week &mdash; explore the full event before it ends.',
     'cards': [M3K3F2, ARG3F2, MICRODART, MATRIPLEX, OPUNTIA, EYECREAM]},
    {'file': '20260703_July4th_ActivationTrio.html', 'title': 'The Activation Trio - Now $89',
     'hero': CDN+'b55b16b6-5257-4023-b51e-6f31460bb31e.jpeg',
     'h1': 'The Activation Trio. Now $89.',
     'lead': 'Three formulas, one sequence &mdash; six weeks of skincare priming. Repeat orders beat our forecast.',
     'code': 'The full 3-step priming routine &mdash; now <span style="text-decoration:underline;">$89</span>, save $46.',
     'cta1': 'SHOP THE TRIO', 'cta2': 'SHOP THE JULY 4TH SALE',
     'closing': 'Six weeks is enough to know what a routine does. Start yours &mdash; now $89, save $46.',
     'cards': [TRIO, STEP1, STEP2, STEP3]},
    {'file': '20260704_July4th_HeroDay_Microdart.html', 'title': 'Happy 4th - The Sale Peaks Today',
     'hero': CDN+'b5f836f5-bf65-45e6-a87d-45176667c608.jpeg',
     'h1': 'Happy 4th. The Sale Peaks Today.',
     'lead': 'Our micro-dart eye patch just got an upgrade &mdash; retinol + argireline in 1,000+ self-dissolving darts.',
     'code': 'The micro-dart is 40% off today &mdash; save $58. Extra 10% on everything else with <span style="text-decoration:underline;">JULY4TH10</span>.',
     'cta1': 'SHOP THE 4TH', 'cta2': 'SHOP ALL JULY 4TH',
     'closing': 'The 4th comes once a year &mdash; and so does this price on our micro-darts.',
     'cards': [MICRODART, ARG3F2, MATRIPLEX, NIGHT]},
    {'file': '20260705_July4th_Creams.html', 'title': 'The Seal Step, On Sale',
     'hero': CDN+'7f662d51-ad99-4fcd-832b-dee81d870607.jpeg',
     'h1': 'The Seal Step, On Sale.',
     'lead': 'Serums do the work &mdash; but without a seal it fades. That&#39;s the job of a cream.',
     'code': 'Creams 30% off this weekend, plus an extra 10% with <span style="text-decoration:underline;">JULY4TH10</span>.',
     'cta1': 'SHOP THE CREAMS', 'cta2': 'SHOP ALL JULY 4TH',
     'closing': 'A serum starts it; a cream keeps it &mdash; and don&#39;t forget your body in sandal season.',
     'cards': [MATRIPLEX, EYECREAM, M3K3F2, RBLTRIO]},
    {'file': '20260707_July4th_LastCall.html', 'title': 'Last Call - Ends Tonight',
     'hero': CDN+'57adcc65-e773-4dbb-9b1e-f1149824176e.jpeg',
     'h1': 'Last Call. Ends Tonight.',
     'lead': 'The July 4th Sale closes tonight &mdash; everything moving fastest is rounded up below.',
     'code': 'Up to 50% off + extra 10% with <span style="text-decoration:underline;">JULY4TH10</span> &mdash; gone at midnight ET.',
     'cta1': 'SHOP BEFORE IT ENDS', 'cta2': 'SHOP THE LAST HOURS',
     'closing': 'At midnight the codes switch off and prices reset. This is the last call.',
     'cards': [MICRODART, ARG3F2, TRIO, M3K3F2, STATICDUO, DYNAMICDUO]},
]

for e in EMAILS:
    build(e)

# Patch M2F sign-up launch hero (its own white-bg HTML)
m2f = OUT / '20260701_M2F_Launch_SignupExclusive.html'
if m2f.exists():
    h = m2f.read_text(encoding='utf-8')
    if '837cb32f-0a5c-4de0-aa36-dbaeea5c99ae' in h:
        m2f.write_text(h.replace('837cb32f-0a5c-4de0-aa36-dbaeea5c99ae', 'ec3c52a4-6669-481b-909f-50c150dda060'), encoding='utf-8')
        print('OK M2F hero patched')
    else:
        print('  NOTE: M2F hero already patched (ok)')

print('\nDone. Preview files in production/html-output/2026-07/')
