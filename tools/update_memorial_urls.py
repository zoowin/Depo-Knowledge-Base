"""
Memorial Sale 2026 — Batch URL replacement script
Replaces all old/placeholder product URLs with final OFFER URLs provided by Leon (2026-05-13).
"""
import os
import re
import sys
from pathlib import Path

# Force UTF-8 stdout on Windows (GBK default chokes on ® and other non-ASCII)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent.parent

# Each tuple: (old_slug_pattern, new_slug)
# old patterns include various placeholder/legacy forms we've used
URL_MAPPING = [
    # 1. Matrixyl 3000 3 for 2 — placeholder slug + old standard slug
    (r"\[NEW_M3K_3F2_SLUG\]", "offer-matrixyl-r-3000-triple-bundle"),
    (r"depology-matrixyl-3000-serum(?=[^a-zA-Z0-9-]|$)", "offer-matrixyl-r-3000-triple-bundle"),

    # 2. Argireline Triple Bundle — old slug we used
    (r"argireline-serum-triple-bundle(?=[^a-zA-Z0-9-]|$)", "offer-peptide-complex-10-serum-3-for-2"),
    (r"argireline-anti-wrinkle-serum(?=[^a-zA-Z0-9-]|$)", "offer-peptide-complex-10-serum-3-for-2"),

    # 3. Face & Eye Duo — already correct, no change
    # face-eye-peptide-firming-duo stays

    # 4. Matriplex Cream
    (r"tri-active-matrixyl-complex-cream(?=[^a-zA-Z0-9-]|$)", "offer-matriplex-peptide-intense-cream-copy"),

    # 5. PEC Eye Cream
    (r"peptide-complex-wrinkle-defense-eye-cream(?=[^a-zA-Z0-9-]|$)", "offer-peptide-complex-wrinkle-defense-eye-cream-copy"),

    # 6. MOP Boosting Cream — ® is URL-encoded as %C2%AE (Leon confirmed)
    (r"deepcare-r-microoperator-boosting-cream-beginner(?=[^a-zA-Z0-9-]|$)", "offer-deepcare-%C2%AE-microoperator-boosting-cream-beginner-us-exclusive-only"),
    # Fix previous run that used literal ® instead of %C2%AE
    (r"offer-deepcare-®-microoperator-boosting-cream-beginner-us-exclusive-only", "offer-deepcare-%C2%AE-microoperator-boosting-cream-beginner-us-exclusive-only"),

    # 7. TLQ
    (r"triple-lipid-q10-revive-moisturizing-treatment-rich(?=[^a-zA-Z0-9-]|$)", "offer-triple-lipid-q10-revive-moisturizing-treatment-rich"),

    # 8. Bakuchiol — already correct, no change
    # bakuchiol-smoothing-serum-stick stays

    # 9. M1/M2 Micro-dart
    (r"deepcare-serum-infused-micro-dart-patches-lp1-t0(?=[^a-zA-Z0-9-]|$)", "offer-deepcare-serum-infused-micro-dart-patches"),

    # 10-12. Peptide Activation Trio / Static Duo / Dynamic Duo — placeholders match final URLs, no change
    # peptide-activation-trio, static-wrinkle-repair-duo, dynamic-wrinkle-defense-duo all OK

    # 13. Night Under Eye Patch
    (r"replenishing-night-under-eye-patch(?=[^a-zA-Z0-9-]|$)", "offer-replenishing-night-under-eye-patch"),
]

# Target files: all Memorial-affected emails + HTML + product-links + Memorial style + May plan
TARGET_FILES = [
    "production/email-drafts/2026-05/20260520_AM_Memorial_Launch.md",
    "production/email-drafts/2026-05/20260520_PM_Memorial_Resend.md",
    "production/email-drafts/2026-05/20260521_Eye_Texture_Trio.md",
    "production/email-drafts/2026-05/20260522_Peptide_3F2.md",
    "production/email-drafts/2026-05/20260523_Matriplex_Cream_50.md",
    "production/email-drafts/2026-05/20260524_AM_Bakuchiol_M1_Sunday.md",
    "production/email-drafts/2026-05/20260524_PM_24_Hours_Left.md",
    "production/email-drafts/2026-05/20260525_Last_Chance.md",
    "production/html-output/20260520_AM_Memorial_Launch.html",
    "knowledge/products/product-links.md",
]


def update_file(path: Path) -> tuple[int, list[str]]:
    """Returns (total_replacements, list of mappings applied)."""
    if not path.exists():
        return 0, []
    content = path.read_text(encoding="utf-8")
    original = content
    applied = []
    for pattern, new_slug in URL_MAPPING:
        count = len(re.findall(pattern, content))
        if count > 0:
            content = re.sub(pattern, new_slug, content)
            applied.append(f"  {pattern} -> {new_slug} ({count}x)")
    if content != original:
        path.write_text(content, encoding="utf-8")
    return len(applied), applied


def main():
    print("Memorial Sale URL batch update")
    print("=" * 60)
    total_files_changed = 0
    total_replacements = 0
    for rel_path in TARGET_FILES:
        path = ROOT / rel_path
        n_patterns, applied = update_file(path)
        if n_patterns > 0:
            print(f"\n[UPDATED] {rel_path}")
            for line in applied:
                print(line)
            total_files_changed += 1
            total_replacements += n_patterns
        else:
            print(f"[no change] {rel_path}")
    print("\n" + "=" * 60)
    print(f"Files updated: {total_files_changed}")
    print(f"Pattern applications: {total_replacements}")


if __name__ == "__main__":
    main()
