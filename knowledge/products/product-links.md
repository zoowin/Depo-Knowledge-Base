# Product Links & Image Registry

> **Single source of truth** for all product URLs and Klaviyo CDN image URLs.
> Agent reads this file when building email HTML to populate product cards.
> **Canonical / global reference** — campaign-specific assets (e.g., Memorial Sale, BFCM)
> live in their own registry files (see `knowledge/visual/Memorial Sale Product Images.md`).
> Last updated: 2026-06-04

---

## Active Products

| Line | Product Name | Shopify URL | Offer URL | Klaviyo CDN Image |
|------|-------------|-------------|-----------|------------------------|
| **A** | Matrixyl® 3000 Collagen Serum | `https://depology.com/products/depology-matrixyl-3000-serum` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/44a0bdde-9c05-4c2b-854b-fe92895a2a6f.png` |
| **A** | Matriplex™ Peptide Intense Cream | `https://depology.com/products/tri-active-matrixyl-complex-cream` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/420e0d8e-091d-4a94-ad76-e4c2bea97c46.png` |
| **B** | Peptide Complex 10% Argireline™ Serum | `https://depology.com/products/argireline-anti-wrinkle-serum` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/160b6da8-e5a3-4202-bcef-a511922d5954.png` |
| **B** | Deepcare+ Micro-dart Eye Patch | `https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/bdb87085-8617-43d8-be9b-f2cc405c16d1.png` |
| **B** | Deepcare+® Retinol Forehead Micro Dart Patches 🆕 | `https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/6df074e5-4930-49b2-8c4f-052336c9a7be.png` |
| **B** | Peptide Complex Eye Cream | `https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream` | `https://depology.com/products/offer-peptide-complex-wrinkle-defense-eye-cream-copy` | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/17182a51-02dc-4114-8b61-d82e29c46bcb.png` |
| **B** | Replenishing Night Under Eye Patch | `https://depology.com/products/replenishing-night-under-eye-patch` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/fb01a6c6-6cdf-4159-b40b-9f605f71ab65.png` |
| **C** | Retinol Radiance Rescue Body Lotion | `https://depology.com/products/retinol-radiance-body-lotion` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/65227851-df6d-4cbd-bcae-6a5c9e446619.png` |
| **E** | Deepcare+® MicroOperator Boosting Cream | `https://depology.com/products/deepcare-r-microoperator-boosting-cream-beginner` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/6db87278-16b2-48dd-bb79-837047b7142f.png` |
| **F** | Opuntia-C Relief Cleansing Balm | `https://depology.com/products/opuntia-c-relief-cleansing-balm` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/63b261a2-9e8a-403f-8343-cde631ec3b49.png` |
| **G** | Bakuchiol Smoothing Serum Stick | `https://depology.com/products/bakuchiol-smoothing-serum-stick` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/642001c5-54b0-4900-90fd-bc0c5dc37dc0.png` |
| **H** | Triple Lipid + Q10 Moisturizing Treatment RICH | `https://depology.com/products/triple-lipid-q10-revive-moisturizing-treatment-rich` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/f11a370d-d5dc-426a-90b0-1ec12a1f8c85.png` |
| **Bundle** | Peptide Activation Trio (NEW 2026, 5/8 launch) | `https://depology.com/products/peptide-activation-trio` | — | ⚠️ canonical image TBD by Leon |
| **Bundle** | Static Wrinkle Repair Duo (M1 + M3K) | `https://depology.com/products/static-wrinkle-repair-duo` | — | ⚠️ canonical image TBD by Leon |
| **Bundle** | Dynamic Wrinkle Defense Duo (M1 + Argireline) | `https://depology.com/products/dynamic-wrinkle-defense-duo` | — | ⚠️ canonical image TBD by Leon |

**⚠️ 已废弃 SKU（库存归零，2026-05-13）：**
- Caviar Multi-Balm Stick + Peptide Serum Duo + Free Caviar Bundle

---

## Offer URL 使用规则

- **有 Offer URL 的产品**：促销邮件中使用 Offer URL，教育邮件使用标准 URL
- **Offer URL 为 `—` 的产品**：统一使用标准 Shopify URL
- **带折扣码的促销**：使用 `/discount/{CODE}?redirect=/products/{slug}` 格式（见 CLAUDE.md）
- **大型 Sale（如 Memorial / BFCM）**：使用 campaign-specific OFFER URL，不写入本文件（参见对应 campaign 的视觉注册表，如 `knowledge/visual/Memorial Sale Product Images.md`）

---

## Brand Assets

| Asset | URL |
|-------|-----|
| Header Image（所有邮件统一） | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a91ce3e7-44ab-42dc-a9e6-c3dc74b6f3bf.jpeg` |
| Footer Logo（白色） | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/82cac524-3eb2-4807-a508-af61cee50920.png` |
| Facebook Icon | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a8ca6d02-61db-4641-bc0e-cbe61d23d563.png` |
| Instagram Icon | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/b2baf081-c148-44a5-9793-96be804b238f.png` |
| TikTok Icon | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/df012502-6c20-496b-b7eb-db6c6c603e3b.png` |
| Pinterest Icon | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/8149ca4d-d368-4ec0-ab45-8b6d815399c8.png` |
| YouTube Icon | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/803eb370-a807-4966-9f69-7cbf9e73a61b.png` |
