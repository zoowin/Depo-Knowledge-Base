"""
Memorial Sale 2026 — Batch fix double-offer URL bugs + replace product image URLs
Uses bytes I/O to preserve original CRLF line endings (avoids diff bloat).
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).parent.parent

# Step 1: Fix the offer-prefix bug from prior runs (handle triple → double → single)
PREFIX_FIXES = [
    ("offer-offer-offer-", "offer-"),
    ("offer-offer-", "offer-"),
]

# Step 2: Replace all 13 product image URLs (Leon provided 2026-05-13)
# Format: (old_image_filename, new_image_filename)
IMAGE_REPLACEMENTS = [
    # 1. Matrixyl 3000 3 for 2
    ("44a0bdde-9c05-4c2b-854b-fe92895a2a6f.png", "19ffd3a2-1cee-4a87-96f2-4dda1a5878d2.jpeg"),
    # 4. Matriplex Cream
    ("420e0d8e-091d-4a94-ad76-e4c2bea97c46.png", "3a22afe6-fe59-4f2d-953e-bacf46f4bfc5.jpeg"),
    # 2. Argireline Triple Bundle
    ("160b6da8-e5a3-4202-bcef-a511922d5954.png", "922c97bf-7f09-4545-b04d-805354e5b770.jpeg"),
    # 9. M1/M2 Micro-dart
    ("bdb87085-8617-43d8-be9b-f2cc405c16d1.png", "9e3d370f-de96-4240-88b2-3f4f229b084f.jpeg"),
    # 5. PEC Eye Cream
    ("17182a51-02dc-4114-8b61-d82e29c46bcb.png", "73fc6218-3682-4111-89bb-e18f46fbfa46.jpeg"),
    # 13. Night Under Eye Patch
    ("fb01a6c6-6cdf-4159-b40b-9f605f71ab65.png", "ed2bfcb0-8b14-4cf2-ad3e-5b26f457626c.jpeg"),
    # 6. MOP Boosting Cream
    ("6db87278-16b2-48dd-bb79-837047b7142f.png", "784eeb0d-b743-4f5d-b31c-c20f068bcefc.jpeg"),
    # 8. Bakuchiol Stick
    ("642001c5-54b0-4900-90fd-bc0c5dc37dc0.png", "996a4cfa-1508-40d8-8866-10419c175a92.jpeg"),
    # 7. TLQ Triple Lipid RICH
    ("f11a370d-d5dc-426a-90b0-1ec12a1f8c85.png", "3c2e2c94-913d-4568-afe0-85347f641eb9.jpeg"),
    # Note: Face & Eye Duo's HTML card 3 was using the OLD Matriplex image URL as a placeholder
    # After Matriplex replacement above, F&E Duo card needs its own image — handled by adding the
    # Matriplex new image as ALSO matching F&E Duo references in HTML (only Card 3 alt text differs).
    # We replace the residual standalone occurrences below as a final pass.
]

# Step 3: HTML-specific replacements — Card 3 (Face & Eye Duo) was using Matriplex image as placeholder.
# After Matriplex's old image gets replaced, the F&E Duo card image will already point to new Matriplex
# image, which is wrong. We need to detect and explicitly fix HTML Card 3 to use the actual F&E Duo image.
# Strategy: in HTML, the F&E Duo card 3 had `alt="Face and Eye Peptide Firming Duo"` and was using the
# 420e0d8e* URL (Matriplex's). After the global PNG→JPEG mapping for Matriplex, that URL becomes
# 3a22afe6* — but for F&E Duo we want 85a9714d-4d1c-45c9-8b50-3bd6b040c1be.jpeg.
# We do this by an HTML-only post-pass.

HTML_FACE_EYE_DUO_FIX = [
    # New Matriplex URL was just substituted everywhere; in HTML it now appears in Card 3 (F&E Duo)
    # AND Card 4 (real Matriplex if any). 5/20 AM HTML only has F&E Duo in cards (not Matriplex),
    # so we can safely swap the entire Matriplex new URL to F&E Duo URL inside the HTML.
    ("3a22afe6-fe59-4f2d-953e-bacf46f4bfc5.jpeg", "85a9714d-4d1c-45c9-8b50-3bd6b040c1be.jpeg"),
]

TARGETS = [
    "knowledge/products/product-links.md",
    "production/html-output/20260520_AM_Memorial_Launch.html",
    "production/email-drafts/2026-05/20260520_AM_Memorial_Launch.md",
    "production/email-drafts/2026-05/20260520_PM_Memorial_Resend.md",
    "production/email-drafts/2026-05/20260521_Eye_Texture_Trio.md",
    "production/email-drafts/2026-05/20260522_Peptide_3F2.md",
    "production/email-drafts/2026-05/20260523_Matriplex_Cream_50.md",
    "production/email-drafts/2026-05/20260524_AM_Bakuchiol_M1_Sunday.md",
    "production/email-drafts/2026-05/20260524_PM_24_Hours_Left.md",
    "production/email-drafts/2026-05/20260525_Last_Chance.md",
]


def process(rel_path: str):
    p = ROOT / rel_path
    if not p.exists():
        return
    raw = p.read_bytes()
    txt = raw.decode("utf-8")
    original = txt
    counts = []
    for old, new in PREFIX_FIXES:
        n = txt.count(old)
        if n > 0:
            txt = txt.replace(old, new)
            counts.append(f"  bug fix '{old}' → '{new}': {n}x")
    for old, new in IMAGE_REPLACEMENTS:
        n = txt.count(old)
        if n > 0:
            txt = txt.replace(old, new)
            short = old.split("-")[0]
            counts.append(f"  image {short}* → {new[:8]}*: {n}x")
    # HTML-only post-pass: F&E Duo card was using Matriplex placeholder
    if rel_path.endswith(".html"):
        for old, new in HTML_FACE_EYE_DUO_FIX:
            n = txt.count(old)
            if n > 0:
                txt = txt.replace(old, new)
                counts.append(f"  F&E Duo card swap (was new Matriplex img): {n}x")
    if txt != original:
        # Preserve line endings — write bytes
        p.write_bytes(txt.encode("utf-8"))
        print(f"[UPDATED] {rel_path}")
        for line in counts:
            print(line)
    else:
        print(f"[no change] {rel_path}")


def main():
    print("Memorial Sale image URL update + bug fix")
    print("=" * 60)
    for rel in TARGETS:
        process(rel)
    print("=" * 60)


if __name__ == "__main__":
    main()
