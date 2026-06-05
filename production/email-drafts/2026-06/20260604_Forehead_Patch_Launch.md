# 20260604_Forehead_Patch_Launch

## Campaign Info
- **Template:** 自定义(基于 0408 白底教育型,header/footer 保留,中段重设计)→ HTML: `production/html-output/20260604_Forehead_Patch_Launch.html`
- **Type:** Promotional — Flagship New Product Launch
- **Audience:** 面向老客(讲"为什么新")
- **Send Date:** **TBD(暂未定 — 保留待发)**
- **Segment:** 标准 4 included / 9 excluded
- **Product Focus:** Line B — Deepcare+® Retinol-Infused Forehead Micro Dart Patches (NEW)
- **Goal:** 重磅发布额头微针贴,用上新价 $36(原 $52,save up to 40%)驱动首批转化
- **Note:** 无折扣码 — 上新价站内自动生效,链接用普通产品 URL(非 `/discount/`)
- **Hero Image (CDN):** `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/837cb32f-0a5c-4de0-aa36-dbaeea5c99ae.jpeg`(米色实验室产品图)
- **Card 1 Image (CDN):** `https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/6df074e5-4930-49b2-8c4f-052336c9a7be.png`(额头贴透明底 PNG)

---

## Subject Lines
1. New: the retinol patch made for your forehead
2. ✨ Your forehead lines just met their match
3. The micro-dart goes to your forehead — now $36
4. Our first forehead patch is here

## Preview Text
Micro-dart delivery. 0.1% retinol. Built for forehead lines. Launch price inside.

---

## Email Structure（最终版）

> Header(logo + hero)与 Footer(黑色 logo/社媒/退订)保留 0408 原结构不动。
> 中段为重设计:发布标题 → 黑金"为什么新" → 成分 → 主推大卡 → routine → 收尾。
> **设计 motif:** 黑金块与成分块顶部各有一条满铺、列对齐、由大到小的**半透明实心倒三角带**(呼应包装 micro-dart),由本地 PNG 实现。

### Hero / Announcement
- **Eyebrow:** NEW · OUR FIRST FOREHEAD PATCH
- **Headline:** The micro-dart, now for your forehead.
- **Sub:** The delivery you already trust from our eye patches — reengineered for the lines creams never reach.
- **Launch price:** $36 ~~$52~~ · Save up to 40%
- **CTA:** SHOP THE LAUNCH → 产品页

### 黑金版块「WHAT MAKES IT NEW」— Three reasons this launch matters
1. **A New Zone** — Our first Deepcare+® patch shaped for forehead lines — vertical and horizontal.
2. **Micro-Dart Delivery** — Self-dissolving darts carry retinol and peptides into the skin's surface layers — not just onto the surface like a cream.
3. **Retinol That Lands** — Retinol + Argireline™ peptide, delivered into the skin's surface layers — not left sitting on top.

### 成分版块「THE FORMULA」— What's inside every dart
- **Retinol (0.1% / 3,300 IU/g)** — Our renewal active — a clinically meaningful mid-strength dose, encouraging visibly smoother, firmer-looking skin over time.
- **Argireline™ Peptide** — Helps relax the look of repeated expression lines across the forehead.
- **Hyaluronic Acid** — Draws moisture into the surface to plump and soften the look of lines.
- **Madecassoside (Cica)** — A calming botanical that buffers the formula, so retinol feels comfortable.
- **Antioxidant Complex** — Glutathione with Vitamins C & E — to brighten and help defend against daily stress.

### 主推大卡（NEW）
- **角色标签:** The Forehead Fix
- **产品名:** Deepcare+® Retinol-Infused Forehead Micro Dart Patches
- **描述:** Softens the look of set-in forehead lines over time. Worn just 2–3 nights a week. 4 patches per box.
- **CTA:** SHOP NOW · $36 → https://depology.com/products/deepcare-retinol-forehead-micro-dart-patches

### Make It A Routine（搭配 2 卡）
- **The Eye Companion** — Deepcare+® Retinol Micro Dart Eye Patches → https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0
- **The Daytime Layer** — Peptide Complex 10% Argireline™ Serum → https://depology.com/products/argireline-anti-wrinkle-serum

### Closing
- **金句:** The technology you trust, somewhere it's never been.
- **Final CTA:** SHOP THE LAUNCH
- **Retinol disclaimer（小字）:** Use sunscreen during the day. New to retinol? You may notice a short adjustment period (mild redness or peeling) that typically eases within a few uses. Sensitive skin: start with 2–3 nights a week.

---

## 设计资源
- `production/assets/images/dart-pattern-dark.png`（600×142,黑金块顶部三角带）
- `production/assets/images/dart-pattern-light.png`（600×142,成分块顶部三角带）
- 渐变配色:黑金块 `#2a2014→#0e0e0e`;成分块 `#fff→#f3ead9`;主推卡 `#fbf7f0→#efe4d2`;金色点缀 `#b08d57`

---

## 合规检查记录
- ✅ "below the surface where creams cannot reach"（官网穿透声称）→ "into the skin's surface layers"
- ✅ "deep-set" → "set-in forehead lines"
- ✅ 无 cure/erase/eliminate/permanent/instant;统一 "softens the look of"
- ✅ Retinol disclaimer 已放（防晒 / 适应期 / 敏感肌频率）
- ✅ 无内部代号;Shopify 官方产品名
- ✅ Retinol 浓度 0.1% / 3,300 IU/g（Leon 2026-06 确认,与眼贴 M1 同级）

---

## 部署待办（定了发送日期后执行）
- [ ] 上传 `dart-pattern-dark.png` / `dart-pattern-light.png` 到 Klaviyo CDN,替换 HTML 中两处 `background-image` 的相对路径为 CDN URL
- [ ] 确认眼贴站内官方展示名（HTML 现用 "Deepcare+® Retinol Micro Dart Eye Patches"）
- [ ] 确认上新价 $36 / $52 仍有效
- [ ] `klaviyo_deploy_campaign`:命名 `[DEP]_YYYYMMDD_Forehead_Patch_Launch`,发件人 Dēpology / support@depology.com,标准 4 included / 9 excluded,9:00 AM ET 工作日
