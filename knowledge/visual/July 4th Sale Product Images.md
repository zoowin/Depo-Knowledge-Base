# 🎆 July 4th Sale 2026 — Product Image & OFFER URL Registry

> **July 4th Sale 2026 专用**（7/1–7/7）。这些图 + URL 仅用于本次 July 4th 邮件系列 / HTML / SMS / sale page，**不可写入 `knowledge/products/product-links.md`**（那个是 canonical 全局参考）。
> 视觉风格：**统一深蓝 / 烟花微光 / 红白蓝星条台面摆拍**，与 6 张 hero 调性一致（区别 Memorial 的白亮台面）。
> Last updated: 2026-06-17

---

## 卡片产品图清单（10 SKU — 真实产品摆拍，由 Leon 提供上传）

| # | SKU | 出现封 | 产品页 slug（带码：`/discount/JULY4TH10?redirect=/products/<slug>`） | July 4th Email Image（Klaviyo CDN） |
|---|---|---|---|---|
| 1 | Matrixyl® 3000 **3 for 2** | ①④⑤ | `offer-matrixyl-r-3000-triple-bundle` | `…/dd4f2dc6-46ef-4d9c-ae61-e7ffecb83ea0.jpeg` |
| 2 | Argireline™ **3 for 2** | ①③⑤ | `offer-peptide-complex-10-serum-3-for-2` | `…/4f625167-8a29-4432-9bb2-d124fa6393bc.jpeg` |
| 3 | Argireline™ MPS Serum（Trio step） | ② | `argireline-anti-wrinkle-serum` | 暂用 #2 的 3f2 图（无单瓶图） |
| 4 | Deepcare+ Micro-dart Eye Patch（含 retinol） | ①③⑤ | `deepcare-serum-infused-micro-dart-patches-lp1-t0` | `…/9c71e6c9-47a0-4e0c-8250-8370aeada422.jpeg` |
| 5 | Matriplex™ Peptide Intense Cream | ①④ | `tri-active-matrixyl-complex-cream` | `…/df6cd138-c092-4ed8-9699-e66ee802086a.jpeg` |
| 6 | Peptide Complex Eye Cream | ②④ | `peptide-complex-wrinkle-defense-eye-cream` | `…/353d6dfe-1422-42c5-8d10-3f638c5f49b4.jpeg` |
| 7 | Peptide Activation Trio（$89 + 赠 M3K） | ②⑤ | `peptide-activation-trio`（活动价，不叠码） | `…/cd88931b-17f5-405c-be06-0f56119c8cba.jpeg` |
| 8 | Deepcare+ MicroOperator Cream（MOP，Trio step） | ② | `deepcare-r-microoperator-boosting-cream-beginner` | `…/3f73cfd6-7b84-40f0-a118-e8a16de4b58f.jpeg` |
| 9 | Retinol Radiance Body Lotion | ④ | `retinol-radiance-body-lotion` | `…/8683a87b-051f-43ed-8708-aec2a6566df3.jpeg` |
| 10 | Replenishing Night Under Eye Patch | ③ | `replenishing-night-under-eye-patch` | `…/a3bf45b7-3f2c-43f2-b5a9-5785b1bd7b25.jpeg` |
| 11 | Opuntia-C Relief Cleansing Balm 🆕清仓($25.20/$36) | ① | `opuntia-c-relief-cleansing-balm`（挂 JULY4TH10 叠加）| `…/df7f7e7a-b3a1-4121-a11b-ac3ab3e5d3ec.jpeg` |

> **多出 4 张备用图**（Codex 也出了，未用进当前邮件，待 Leon 决定是否加进推荐位）：dynamic wrinkle defense duo `…/f8102291` · face & eye firming duo `…/d07ce372` · static wrinkle repair duo `…/5a0b5318` · RBL trio（3瓶）`…/559c3ffa`。

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
