#!/usr/bin/env python3
"""Build 20260614_Forehead_Early_Access_v2.html — STORY-DRIVEN version.

Starts from the v1 teaser HTML (header/hero/footer/sign-up block already correct)
and restructures the middle into a story:
  Body (empathy) -> WHY WE MADE IT -> HOW WE MADE IT (2 image-text rows)
  -> first-look hints -> Why-join cards -> Sign-up CTA.

Design intent (confirmed with Leon 2026-06-12):
  - Story first, skeleton reused (600px, gold #b08d57 accents, MEL idiom).
  - 2 image slots inside HOW WE MADE IT, alternating left-image / right-image.
  - Mystery preserved: NO "forehead" naming, NO dart count / size / retinol %.
  - "launch-day offer" -> "A limited first batch" (no discount wording).

Image slots are labeled placeholder boxes (dashed gold). Leon swaps each for an
<img> (Klaviyo CDN URL) before deploy — search "IMAGE SLOT" in the HTML.

Compliance: no cure/heal/treat/permanent/Botox-equivalence; "into the skin's
surface layers" (not "penetrates deep"); self-dissolving micro-darts, no numbers.
"""
import sys, io, webbrowser
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'production' / 'html-output' / '2026-06' / '20260614_Forehead_Early_Access.html'
OUT = ROOT / 'production' / 'html-output' / '2026-06' / '20260614_Forehead_Early_Access_v2.html'

GOLD = '#b08d57'
html = SRC.read_text(encoding='utf-8')

# --- Final image URLs (Klaviyo CDN, supplied by Leon 2026-06-12) ---
IMG1_URL = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/b7de851b-b2bb-47d6-a607-8255f408d174.jpeg'  # slot 1 — the curve problem
IMG2_URL = 'https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/4c0983a9-8291-43c0-83b5-d35ae9e98bd3.jpeg'  # slot 2 — months of prototyping

# ============================================================
# Helper: image-slot cell — real <img> when url given, else placeholder
# ============================================================
def _img_slot(n, label, url=None):
    if url:
        return (
        f'<td align="center" valign="middle" style="padding:0;">'
        f'<img src="{url}" width="280" alt="Depology micro-dart patch in the making" '
        f'style="display:block;width:100%;max-width:280px;height:auto;border-radius:6px;"/>'
        f'</td>'
        )
    return (
    f'<td align="center" valign="middle" bgcolor="#f3eee2" '
    f'style="background-color:#f3eee2;border:1px dashed {GOLD};border-radius:6px;height:330px;">'
    f'<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;'
    f'font-size:12px;font-weight:700;letter-spacing:2px;color:{GOLD};text-transform:uppercase;'
    f'line-height:1.5;padding:12px;">IMAGE SLOT {n}<br/>'
    f'<span style="font-weight:400;font-size:11px;color:#9a8c70;letter-spacing:0;">{label}</span></div>'
    f'</td>'
    )

def _txt_cell(title, copy):
    return (
    f'<td valign="middle" style="padding:6px 6px;">'
    f'<div style="font-family:TimesNewRoman,\'Times New Roman\',Times,Georgia,serif;'
    f'font-size:22px;line-height:1.25;color:#0e0e0e;padding-bottom:10px;">{title}</div>'
    f'<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;'
    f'font-size:15px;line-height:1.6;color:#4a4234;">{copy}</div>'
    f'</td>'
    )

def _img_text_row(n, label, title, copy, image_left=True, url=None):
    """A 2-column image/text row that stacks on mobile (colstack)."""
    img_col = (
    '<div class="kl-column" style="display:table-cell;vertical-align:middle;width:50%;">'
    '<div class="mj-column-per-100 mj-outlook-group-fix component-wrapper" '
    'style="font-size:0px;text-align:left;direction:ltr;vertical-align:middle;width:100%;">'
    '<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">'
    f'<tbody><tr>{_img_slot(n, label, url)}</tr></tbody></table></div></div>'
    )
    txt_col = (
    '<div class="kl-column" style="display:table-cell;vertical-align:middle;width:56%;">'
    '<div class="mj-column-per-100 mj-outlook-group-fix component-wrapper" '
    'style="font-size:0px;text-align:left;direction:ltr;vertical-align:middle;width:100%;">'
    '<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">'
    f'<tbody><tr>{_txt_cell(title, copy)}</tr></tbody></table></div></div>'
    )
    inner = (img_col + txt_col) if image_left else (txt_col + img_col)
    return (
    '<div class="kl-row colstack" style="display:table;table-layout:fixed;width:100%;padding-bottom:18px;">'
    + inner + '</div>'
    )

# ============================================================
# WHY + HOW section (single white kl-section, inserted before checklist)
# ============================================================
ROW1 = _img_text_row(
    1, 'early prototype on skin / the curve test',
    'The hardest place to reach.',
    'We chose one of the most expressive, hardest-to-stick places on the face. It moves, it '
    'creases, it curves. A flat patch simply won&rsquo;t stay.',
    image_left=True, url=IMG1_URL)

ROW2 = _img_text_row(
    2, 'lab samples / colour iterations',
    'Months of prototyping.',
    'Version after version, we shaped the curve so it would hold, tuning the formula so '
    'hundreds of self-dissolving darts carry their actives below the surface, instead of '
    'leaving them on top. We kept going until it could sit steadily on the one place that '
    'refuses to cooperate.',
    image_left=False, url=IMG2_URL)

STORY_SECTION = f'''<!-- ============================================ -->
<!-- SECTION 4S: WHY WE MADE IT + HOW WE MADE IT  -->
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
<td style="direction:ltr;font-size:0px;padding:8px 40px 8px 40px;text-align:center;">

<!-- WHY eyebrow + copy -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:12px;font-weight:700;letter-spacing:3px;color:{GOLD};text-transform:uppercase;padding-bottom:12px;">Why we made it</div>
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:17px;font-weight:400;line-height:1.65;text-align:center;color:#333333;max-width:480px;margin:0 auto;padding-bottom:34px;">
For years, we kept hearing the same thing from you. The only &ldquo;real&rdquo; fixes meant needles, or a frozen face, and you didn&rsquo;t want either. We didn&rsquo;t think those should be your only options. So we went back to the lab.
</div>

<!-- HOW eyebrow -->
<div style="font-family:'Aktiv Regular + Bold', Helvetica, Arial, sans-serif;font-size:12px;font-weight:700;letter-spacing:3px;color:{GOLD};text-transform:uppercase;padding-bottom:18px;">How we made it</div>

<!-- 2 image-text rows -->
{ROW1}
{ROW2}

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

# Insert STORY_SECTION right before the checklist section
checklist_marker = '<!-- ============================================ -->\n<!-- SECTION 5: CHECKLIST (3 LAYERS)              -->'
if checklist_marker in html:
    html = html.replace(checklist_marker, STORY_SECTION + checklist_marker, 1)
    print('Inserted WHY + HOW story section (2 image slots)')
else:
    raise SystemExit('Checklist marker not found — cannot insert story section')

# ============================================================
# Body copy: replace the whole teaser block with the story opening
# ============================================================
old_body = ('<p style="padding-bottom:1em;">Some lines speak for you &mdash; making you look '
            'tired or annoyed on a day you feel completely fine.</p>\n'
            '<p style="padding-bottom:1em;font-family:TimesNewRoman,\'Times New Roman\',Times,'
            'Georgia,serif;font-style:italic;font-size:22px;line-height:1.4;color:#0e0e0e;">'
            '&ldquo;You saw it on a video call. Then you couldn&rsquo;t unsee it.&rdquo;</p>\n'
            '<p style="padding-bottom:0;">We&rsquo;ve been working on something for exactly that. '
            'We&rsquo;re not showing it yet &mdash; but here&rsquo;s a hint:</p>')
new_body = ('<p style="padding-bottom:1em;">These lines are years of expression, quietly set '
            'into the skin.</p>\n'
            '<p style="padding-bottom:0;font-family:TimesNewRoman,\'Times New Roman\',Times,'
            'Georgia,serif;font-style:italic;font-size:22px;line-height:1.4;color:#0e0e0e;">'
            'Most creams only ever reach the surface, never where the line forms.</p>')
if old_body in html:
    html = html.replace(old_body, new_body, 1)
    print('Replaced body copy with story opening')
else:
    raise SystemExit('Body copy block not found')

# ============================================================
# Replace the 3 teaser hints with a WHAT IT IS story paragraph
# ============================================================
old_hints = ('<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;'
             'font-size:17px;font-weight:400;line-height:1.7;text-align:center;color:#0e0e0e;">\n'
             '<p style="padding-bottom:0.9em;"><span style="color:#b08d57;font-size:13px;">&#9662;</span> <strong>Retinol &mdash; backed by a peptide blend.</strong></p>\n'
             '<p style="padding-bottom:0.9em;"><span style="color:#b08d57;font-size:13px;">&#9662;</span> <strong>A patch, not a cream &mdash; shaped to fit.</strong></p>\n'
             '<p style="padding-bottom:0;"><span style="color:#b08d57;font-size:13px;">&#9662;</span> <strong>For the lines you frown into.</strong></p>\n'
             '</div>')
new_whatitis = (f'<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;'
                f'font-size:12px;font-weight:700;letter-spacing:3px;color:{GOLD};'
                f'text-transform:uppercase;padding-bottom:14px;">What it is</div>\n'
                f'<div style="font-family:\'Aktiv Regular + Bold\', Helvetica, Arial, sans-serif;'
                f'font-size:17px;font-weight:400;line-height:1.65;text-align:center;color:#333333;'
                f'max-width:480px;margin:0 auto;">\n'
                f'A micro-dart patch shaped to the skin, with hundreds of self-dissolving darts that '
                f'deliver their actives just below the surface. Wear it about an hour, every few nights. '
                f'No needles, no downtime, no frozen look. Every expression stays yours.\n'
                f'</div>')
if old_hints in html:
    html = html.replace(old_hints, new_whatitis, 1)
    print('Replaced teaser hints with WHAT IT IS paragraph')
else:
    raise SystemExit('Teaser hints block not found')

# ============================================================
# Why-join card 2: remove offer wording -> limited first batch
# ============================================================
swaps = [
    # Hero + body headlines -> landing-page voice (less clever, more direct)
    ('Something for the lines<br/>you didn&rsquo;t ask for.',
     'We took the micro-dart<br/>somewhere new.'),
    ('You stop frowning. The lines don&rsquo;t.', 'Some lines speak for you.'),
    ('It&rsquo;s not your mood. It just looks that way.', 'It&rsquo;s not about getting older.'),
    ('A launch-day offer', 'A limited first batch'),
    ('Reserved just for the list.', 'Made in small quantities.'),
    # Sign-up block copy: add the limited line
    ('The full reveal comes in July. Be on the list when it does.',
     'The full reveal comes in July, and the first batch is limited. Be on the list when it opens.'),
    # Tab title -> subject
    ("<title>Something for the lines you didn't ask for.</title>",
     '<title>Some lines speak for you.</title>'),
]
for old, new in swaps:
    if old in html:
        html = html.replace(old, new, 1)
        print(f'Swapped: {old[:42]!r} -> {new[:42]!r}')
    else:
        print(f'  MISS: {old[:42]!r}')

OUT.write_text(html, encoding='utf-8')
print(f'Output: {OUT} ({len(html)} chars)')

if '--preview' in sys.argv:
    webbrowser.open(str(OUT))
    print('Opened in browser.')
