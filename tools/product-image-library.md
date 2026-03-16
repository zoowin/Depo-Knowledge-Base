# 📸 Depology — Product Image Library

> **Purpose:** Maps every product to its Klaviyo CDN image URL.
> Claude reads this file when building a new campaign config to populate `p1_img`, `p2_img`, `p3_img`.
>
> **How to add a new image:**
> 1. Upload the product image to Klaviyo (Account → Content → Images).
> 2. Right-click the image → "Copy Image URL" (format: `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/<UUID>.png`).
> 3. Paste the URL into the table below and change status to ✅.

---

## Lookup Table

| Key (builder ID) | Product Name | Shopify URL Slug | Klaviyo CDN Image URL | Status |
| :--- | :--- | :--- | :--- | :---: |
| `opuntia_cleansing_balm` | Opuntia-C Relief Cleansing Balm | `opuntia-c-relief-cleansing-balm` | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/63b261a2-9e8a-403f-8343-cde631ec3b49.png` | ✅ |
| `argireline_mps_serum` | Argireline™ MPS Serum | `argireline-anti-wrinkle-serum` | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/8f6ca609-56c2-4152-aca9-60db1fae9f1e.png` | ✅ |
| `cica_recovery_serum` | Cica Recovery Serum | `cica-h-a-calm-repair-serum` | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fc33e5c3-ab65-40a0-92f1-031418fc7478.png` | ✅ |
| `matrixyl_serum` | Matrixyl® 3000 Collagen Serum | `depology-matrixyl-3000-serum` | — | ⏳ |
| `matriplex_cream` | Matriplex™ Peptide Intense Cream | `tri-active-matrixyl-complex-cream` | — | ⏳ |
| `profi_overnight_mask` | Pro-Firming Overnight Dream Mask | `pro-firming-matrixyl-3000-dynalift-night-mask` | — | ⏳ |
| `argireline_eye_stick` | Argireline™ Eye Stick | `argireline-anti-aging-eye-stick` | — | ⏳ |
| `microdart_eye_patch` | Micro-dart Eye Patch | `deepcare-serum-infused-micro-dart-patches-lp1-pb` | — | ⏳ |
| `argireline_eye_cream` | Argireline™ Eye Cream | `peptide-complex-wrinkle-defense-eye-cream` | — | ⏳ |
| `retinol_night_cream` | Anti-Aging Retinol Night Cream | `anti-aging-retinol-night-cream` | — | ⏳ |
| `retinol_body_lotion` | Retinol Radiance Rescue Body Lotion | `retinol-radiance-body-lotion` | — | ⏳ |
| `cica_cleanser` | Cica Gentle Cleanser | `cica-redness-relief-nourishing-cleanser` | — | ⏳ |
| `microoperator_cream` | "Micro-needling in a jar" Cream | `deepcare-r-microoperator-boosting-cream-beginner` | — | ⏳ |

---

## Product URLs (for builder `p_url` fields)

| Product Name | Full Shopify URL |
| :--- | :--- |
| Opuntia-C Relief Cleansing Balm | `https://depology.com/products/opuntia-c-relief-cleansing-balm` |
| Argireline™ MPS Serum | `https://depology.com/products/argireline-anti-wrinkle-serum` |
| Cica Recovery Serum | `https://depology.com/products/cica-h-a-calm-repair-serum` |
| Matrixyl® 3000 Collagen Serum | `https://depology.com/products/depology-matrixyl-3000-serum` |
| Matriplex™ Peptide Intense Cream | `https://depology.com/products/tri-active-matrixyl-complex-cream` |
| Pro-Firming Overnight Dream Mask | `https://depology.com/products/pro-firming-matrixyl-3000-dynalift-night-mask` |
| Argireline™ Eye Stick | `https://depology.com/products/argireline-anti-aging-eye-stick` |
| Micro-dart Eye Patch | `https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-pb` |
| Argireline™ Eye Cream | `https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream` |
| Anti-Aging Retinol Night Cream | `https://depology.com/products/anti-aging-retinol-night-cream` |
| Retinol Radiance Rescue Body Lotion | `https://depology.com/products/retinol-radiance-body-lotion` |
| Cica Gentle Cleanser | `https://depology.com/products/cica-redness-relief-nourishing-cleanser` |
| "Micro-needling in a jar" Cream | `https://depology.com/products/deepcare-r-microoperator-boosting-cream-beginner` |

---

*Last updated: 2026-03-07 | ✅ = image uploaded to Klaviyo | ⏳ = upload pending*
