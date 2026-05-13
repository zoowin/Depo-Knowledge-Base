# Product Links & Image Registry

> **Single source of truth** for all product URLs and Klaviyo CDN image URLs.
> Agent reads this file when building email HTML to populate product cards.
> Last updated: 2026-05-13 (Memorial Sale 13 SKUs URLs + images batch refreshed)

---

## Active Products

| Line | Product Name | Shopify URL | Offer URL | Klaviyo CDN Image |
|------|-------------|-------------|-----------|------------------------|
| **A** | Matrixyl® 3000 Collagen Serum | `https://depology.com/products/offer-matrixyl-r-3000-triple-bundle` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/19ffd3a2-1cee-4a87-96f2-4dda1a5878d2.jpeg` |
| **A** | Matriplex™ Peptide Intense Cream | `https://depology.com/products/offer-matriplex-peptide-intense-cream-copy` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/3a22afe6-fe59-4f2d-953e-bacf46f4bfc5.jpeg` |
| **B** | Peptide Complex 10% Argireline™ Serum | `https://depology.com/products/offer-peptide-complex-10-serum-3-for-2` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/922c97bf-7f09-4545-b04d-805354e5b770.jpeg` |
| **B** | Deepcare+ Micro-dart Eye Patch | `https://depology.com/products/offer-deepcare-serum-infused-micro-dart-patches` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/9e3d370f-de96-4240-88b2-3f4f229b084f.jpeg` |
| **B** | Peptide Complex Eye Cream | `https://depology.com/products/offer-peptide-complex-wrinkle-defense-eye-cream-copy` | `https://depology.com/products/offer-peptide-complex-wrinkle-defense-eye-cream-copy` | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/73fc6218-3682-4111-89bb-e18f46fbfa46.jpeg` |
| **B** | Replenishing Night Under Eye Patch | `https://depology.com/products/offer-replenishing-night-under-eye-patch` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/ed2bfcb0-8b14-4cf2-ad3e-5b26f457626c.jpeg` |
| **Bundle** | Face & Eye Peptide Firming Duo (Matriplex + PEC, Memorial 100-cap) | `https://depology.com/products/face-eye-peptide-firming-duo` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/85a9714d-4d1c-45c9-8b50-3bd6b040c1be.jpeg` |
| **C** | Retinol Radiance Rescue Body Lotion | `https://depology.com/products/retinol-radiance-body-lotion` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/65227851-df6d-4cbd-bcae-6a5c9e446619.png` |
| **E** | Deepcare+® MicroOperator Boosting Cream | `https://depology.com/products/offer-deepcare-%C2%AE-microoperator-boosting-cream-beginner-us-exclusive-only` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/784eeb0d-b743-4f5d-b31c-c20f068bcefc.jpeg` |
| **F** | Opuntia-C Relief Cleansing Balm | `https://depology.com/products/opuntia-c-relief-cleansing-balm` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/63b261a2-9e8a-403f-8343-cde631ec3b49.png` |
| **G** | Bakuchiol Smoothing Serum Stick | `https://depology.com/products/bakuchiol-smoothing-serum-stick` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/996a4cfa-1508-40d8-8866-10419c175a92.jpeg` |
| **H** | Triple Lipid + Q10 Moisturizing Treatment RICH | `https://depology.com/products/offer-triple-lipid-q10-revive-moisturizing-treatment-rich` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/3c2e2c94-913d-4568-afe0-85347f641eb9.jpeg` |
| **Bundle** | Peptide Activation Trio (NEW 2026) | `https://depology.com/products/peptide-activation-trio` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/42ce5493-c458-47db-b07e-ea974578f7f5.jpeg` |
| **Bundle** | Static Wrinkle Repair Duo (M1 + M3K, Memorial) | `https://depology.com/products/static-wrinkle-repair-duo` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/68e2e5d9-ce35-47f7-b8ac-1b1295156323.jpeg` |
| **Bundle** | Dynamic Wrinkle Defense Duo (M1 + Argireline, Memorial) | `https://depology.com/products/dynamic-wrinkle-defense-duo` | — | `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/9856be7d-aff5-491e-b26c-4db02e5c5104.jpeg` |

---

## Offer URL 使用规则

- **有 Offer URL 的产品**：促销邮件中使用 Offer URL，教育邮件使用标准 URL
- **Offer URL 为 `—` 的产品**：统一使用标准 Shopify URL
- **带折扣码的促销**：使用 `/discount/{CODE}?redirect=/products/{slug}` 格式（见 CLAUDE.md）

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
