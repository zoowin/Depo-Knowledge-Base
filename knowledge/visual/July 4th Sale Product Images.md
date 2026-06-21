# 🎆 July 4th Sale 2026 — Product Image & OFFER URL Registry

> **July 4th Sale 2026 专用**（7/1–7/7）。这些图 + URL 仅用于本次 July 4th 邮件系列 / HTML / SMS / sale page，**不可写入 `knowledge/products/product-links.md`**（那个是 canonical 全局参考）。
> 视觉风格：**统一深蓝 / 烟花微光 / 红白蓝星条台面摆拍**，与 6 张 hero 调性一致（区别 Memorial 的白亮台面）。
> Last updated: 2026-06-17

---

## 卡片产品图清单（10 SKU — 真实产品摆拍，由 Leon 提供上传）

| # | SKU | 出现封 | 产品页 slug（带码：`/discount/JULY4TH10?redirect=/products/<slug>`） | July 4th Email Image（Klaviyo CDN） |
|---|---|---|---|---|
| 1 | Matrixyl® 3000 **3 for 2** | ①④⑤ | `offer-matrixyl-r-3000-triple-bundle` | ⬜ 待 Leon |
| 2 | Argireline™ **3 for 2** | ①③⑤ | `offer-peptide-complex-10-serum-3-for-2` | ⬜ 待 Leon |
| 3 | Argireline™ MPS Serum（Trio step） | ② | `argireline-anti-wrinkle-serum` | ⬜ 待 Leon |
| 4 | Deepcare+ Micro-dart Eye Patch（含 retinol） | ①③⑤ | `deepcare-serum-infused-micro-dart-patches-lp1-t0` | ⬜ 待 Leon |
| 5 | Matriplex™ Peptide Intense Cream | ①④ | `tri-active-matrixyl-complex-cream` | ⬜ 待 Leon |
| 6 | Peptide Complex Eye Cream | ②④ | `peptide-complex-wrinkle-defense-eye-cream` | ⬜ 待 Leon |
| 7 | Peptide Activation Trio（$89 + 赠 M3K） | ②③⑤ | `peptide-activation-trio`（活动价，不叠码） | ⬜ 待 Leon |
| 8 | Deepcare+ MicroOperator Cream（MOP，Trio step） | ② | `deepcare-r-microoperator-boosting-cream-beginner` | ⬜ 待 Leon |
| 9 | Retinol Radiance Body Lotion | ④ | `retinol-radiance-body-lotion` | ⬜ 待 Leon |
| 10 | Replenishing Night Under Eye Patch | ③ | `replenishing-night-under-eye-patch` | ⬜ 待 Leon |

> 封号对应：① KickOff ② Trio ③ 正日 Micro-dart ④ Creams ⑤ Last Call。
> **M2F Forehead 不在此表**：它走自己的 launch 产品图（unlisted，仅 M2F 专属封）。

---

## 做图规范
- **真实产品图**合成到统一 July 4th 背景（深蓝台面 + 微光烟花 + 红白蓝星条点缀）。**不要 AI 生成产品本体**（标签文字会穿帮）。
- 尺寸：正方形或 4:3，卡片内宽 296px，建议出 ≥600px。
- bundle（3f2 / Trio）出**群像**；单品出单瓶/单盒。
- 风格与 6 张 hero 统一，但产品要清晰、可辨。

## 流程（同 Memorial）
1. Leon 做好图 → 上传 Klaviyo → 取 cloudfront CDN URL。
2. 把 URL 填回本表"Email Image"列。
3. 告诉 Leon's cc，我把 `build_july4th.py` 里 `IMG{}` 的占位 PNG 换成这些 CDN 图，重跑 HTML。

## 关联
- `knowledge/visual/Memorial Sale Product Images.md` — 上次同类注册表（参考）
- `tools/build_july4th.py` — 构建脚本（`IMG{}` 当前用 product-links 占位 PNG，待替换）
- `production/email-drafts/2026-07/00_July4th_Sale_Plan.md` — 总览
