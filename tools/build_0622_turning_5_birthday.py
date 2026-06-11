# -*- coding: utf-8 -*-
"""Build 20260622_Turning_5_Birthday.html from the 0620 Birthday Gift HTML.

Letter-style email: hero -> letter body (3 paragraphs) -> closing + CTA -> P.S.
Changes vs 0620 base:
  - new hero image, eyebrow, headline, subheadline
  - remove Hero CTA (letter opens with no first-screen button)
  - body: 3 paragraphs (Brand Story exception)
  - remove Section 6 gift block (code shown on 6/20 already; today is the letter)
  - closing + final CTA "ENJOY YOUR GIFT" (discount link, code valid until tonight)
  - P.S. = gift deadline reminder
"""
import io
import os
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', 'production', 'html-output', '2026-06', '20260620_Birthday_Gift.html')
OUT = os.path.join(os.path.dirname(__file__), '..', 'production', 'html-output', '2026-06', '20260622_Turning_5_Birthday.html')

HERO_IMG = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/23024831-2bc8-4fb3-a19f-6f7875ce69c9.jpeg'

with io.open(BASE, 'r', encoding='utf-8') as f:
    html = f.read()

# ---------- 1. Remove Hero CTA block (between marker and section triple-close) ----------
start = html.index('<!-- Hero CTA -->')
end = html.index('</div></div></div>', start)
html = html[:start] + html[end:]

# ---------- 2. Remove Section 6 gift block ----------
SEC6 = '<!-- ============================================ -->\n<!-- SECTION 6: GIFT BLOCK'
SEC7 = '<!-- ============================================ -->\n<!-- SECTION 7: CLOSING'
s6 = html.index(SEC6)
s7 = html.index(SEC7)
html = html[:s6] + html[s7:]

# ---------- 3. Text replacements ----------
REPLACEMENTS = [
    # title + hero image
    ("<title>It's our birthday. The gift is yours.</title>",
     '<title>Turning five. A letter from Depology.</title>'),
    ('alt="Our 5th birthday - 10% off everything" src="https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/357e56df-d955-46a5-9084-5fbaf5df99dd.jpeg"',
     'alt="Turning five - a letter from Depology" src="%s"' % HERO_IMG),
    # eyebrow
    ('Birthday Weekend &middot; Turning Five',
     'June 22 &middot; Our Fifth Birthday'),
    # headline
    ('It&rsquo;s our birthday.<br/>The gift is yours.',
     'Turning five.'),
    # subheadline
    ('We turn five next Monday. The celebration starts today.',
     'A letter from D&#275;pology.'),
    # body headline
    ('Thank you for five years.',
     'Five years today.'),
    # body copy: 2 paragraphs -> 3 paragraphs
    ('<p style="padding-bottom:1em;">Next Monday, D&#275;pology turns five. Every formula we&rsquo;ve made in those five years was shaped by the people who use it. That means you.</p>\n<p style="padding-bottom:0;">So this weekend, the gift goes to you. Take 10% off everything for the next 72 hours. Every serum, every patch, every cream.</p>',
     '<p style="padding-bottom:1em;">Today, D&#275;pology turns five. Five years of serums, patches, and creams made for mature skin. None of it would exist without you.</p>\n<p style="padding-bottom:1em;">And we are not slowing down. Our team keeps testing, refining, and improving every formula we make. Something new is already on the way.</p>\n<p style="padding-bottom:0;">But today is not about what comes next. It is a simple thank you. To everyone who trusted us with their skin, thank you for five wonderful years.</p>'),
    # closing copy
    ('On Monday we&rsquo;ll send you our birthday letter.<br/>Today, just enjoy the gift.',
     'Here&rsquo;s to the next five years.<br/>Thank you for being here.'),
    # final CTA label (hero CTA already removed, only one left)
    ('\nUNWRAP 10% OFF\n',
     '\nENJOY YOUR GIFT &rarr;\n'),
    # P.S. row: early-access promo -> gift deadline
    ('P.S. Something new is coming in July. <a href="https://depology.com/pages/early-access" target="_blank" style="color:#b08d57;text-decoration:underline;">Join the early-access list</a> to see it first.',
     'P.S. Your birthday gift ends tonight at 11:59 PM ET. 10% off everything, applied automatically at checkout.'),
]

miss = []
for old, new in REPLACEMENTS:
    if old not in html:
        miss.append(old[:70])
        continue
    html = html.replace(old, new, 1)

with io.open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

# ---------- 4. Verify ----------
print('MISS: %d' % len(miss))
for m in miss:
    print('  - ' + m)
print('chars: %d' % len(html))
print('em-dash: %d  &mdash;: %d' % (html.count('—'), html.count('&mdash;')))
print('discount links: %d' % html.count('https://depology.com/discount/BIRTHDAY10'))
print('early-access links: %d' % html.count('/pages/early-access'))
print('UNWRAP leftover: %d' % html.count('UNWRAP'))
print('table open/close: %d/%d' % (html.count('<table'), html.count('</table>')))
sys.exit(1 if miss else 0)
