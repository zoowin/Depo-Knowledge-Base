# 🇺🇸 Memorial Sale Visual Style Guide

> **用途：** 2026 Memorial Sale 8 封邮件 + 未来 July 4th / Labor Day 美式爱国主题促销复用。
> **基于：** 2025 Memorial Sale 真实邮件破译（$185k / 8 emails 验证）。
> **基础模板：** `production/email-drafts/templates/20260408_Hydration_Hierarchy.html`（白底 0408 改造）。
> Last updated: 2026-05-08

---

## 一、风格哲学

Memorial Sale 是**美式爱国主义 × 高端护肤**的视觉语境。

- **不是**："黑底 + 红蓝 banner + Sale 大字"的廉价电商促销感
- **是**："白底 premium product + 红蓝 STAR 徽章 + 深蓝 H1"的高端节日促销

**视觉语言核心：**
- **底色：** 白 / 浅米色（与品牌教育型邮件一致），**不用黑底**
- **强调色：** 深蓝（#1E3A8A 系）+ 警示红（#DC2626 系）
- **爱国元素：** 仅出现在 STAR badge + 国旗布料背景（hero 图）+ 红字加粗（关键文案）
- **Premium 感：** 产品摄影留白多 + 金属质感包装 + 自然光

---

## 二、模板分级

| 模板类型 | 使用场景 | 邮件 | 视觉特征 |
|---|---|---|---|
| **A. 主题型（白底 + STAR badge）** | Day 1-5 AM 主体促销 | 5/20 AM, 5/20 PM, 5/21, 5/22, 5/23, 5/24 AM | 白底 + 深蓝 H1 + 红蓝 STAR badge + 4-card grid |
| **B. 红警示型（红顶 banner + 价格 CTA）** | Day 5 PM 24 Hours Left | 5/24 PM | 红底大字顶部 banner + 倾斜动感 hero + "$X ONLY" 价格 CTA |
| **C. 收尾型（混合白底 + LAST CHANCE 红字）** | Day 6 Last Chance | 5/25 | 白底 + 顶部红字 "LAST CHANCE" + 蓝字副标 + 遗憾叙事 lead |

---

## 三、模板 A：主题型详解（白底 STAR badge）

### 结构（自上而下）

```
┌─────────────────────────────────────────┐
│ [Header logo]                            │
├─────────────────────────────────────────┤
│ HERO ZONE (high)                         │
│   ┌─────────────────────────────┐        │
│   │ H1 (深蓝 #1E3A8A，居中)      │        │
│   │ Celebrate Memorial Day        │        │
│   │ with the Power of Peptides    │        │
│   └─────────────────────────────┘        │
│   ┌─────────────────────────────┐        │
│   │ Hero image (产品 + STAR badge) │        │
│   │   STAR badge：               │        │
│   │   ⭐⭐⭐                       │        │
│   │   "UP TO 50% OFF"             │        │
│   │   ⭐⭐⭐                       │        │
│   │   红蓝双圈 + 5 颗星           │        │
│   └─────────────────────────────┘        │
├─────────────────────────────────────────┤
│ LEAD COPY (居中, 黑色 18px)              │
│ Don't miss your chance to stock up on   │
│ our #1 bestselling peptide serum.       │
│                                          │
│ Grab yours today and see proven results │
│ in just 28 days.                         │
│                                          │
│ [CODE block - 仅 Day 1 双发显示]         │
│ Extra 10% off site-wide with code       │
│ MEM10 for subscribers, 48 hours only.   │
│ (红色加粗 + 下划线)                      │
├─────────────────────────────────────────┤
│ [PRIMARY CTA] (黑底白字)                  │
│   SHOP MEMORIAL SALE                     │
├─────────────────────────────────────────┤
│ 4-CARD PRODUCT GRID (2×2)                │
│ ┌──────────┬──────────┐                  │
│ │ [3 FOR 2]│ [50% OFF]│  ← 蓝色横条      │
│ │ Product  │ Product  │                  │
│ │ image    │ image    │                  │
│ │ Tag      │ Tag      │                  │
│ │ Name     │ Name     │                  │
│ │ ⭐⭐⭐⭐  │ ⭐⭐⭐⭐  │                  │
│ │ (2000+)  │ (800+)   │                  │
│ │ $80 ~$120~│ $98 ~$147~│                │
│ │ [SAVE $40]│ [SAVE $49]│  ← 黑底 CTA   │
│ └──────────┴──────────┘                  │
│ ┌──────────┬──────────┐                  │
│ │ ...      │ ...      │                  │
│ └──────────┴──────────┘                  │
├─────────────────────────────────────────┤
│ CLOSING COPY (黑底白字 banner)           │
│ "Limited stock available — grab yours   │
│  while you can!"                         │
├─────────────────────────────────────────┤
│ [SECONDARY CTA] (白底黑字)               │
│   SHOP ALL SALE                          │
├─────────────────────────────────────────┤
│ [Footer]                                  │
└─────────────────────────────────────────┘
```

### STAR Badge 规范

```
        ⭐ ⭐ ⭐
      ┌─────────┐
      │  XX%    │
      │  OFF    │
      └─────────┘
        ⭐ ⭐ ⭐
```

- **外圈：** 红色细线（约 #C8102E）
- **内圈：** 深蓝（#1E3A8A）
- **5 颗星分布：** 顶部 3 颗 + 底部 2 颗（或 5 颗围绕圆形）
- **中心文字：** 黑色 bold sans-serif，"XX% OFF" 或 "3 FOR 2" 或 "ONLY $9 SUNSCREEN"
- **尺寸：** Hero 图右下或居中叠加，约占 hero 高度的 35-40%
- **变体：**
  - "UP TO 50% OFF" — Day 1 群像 hero 用
  - "3 FOR 2" — Day 3 Peptide 双瓶 hero 用
  - "50% OFF / LIMITED AVAILABILITY" — Day 4 Matriplex solo hero 用
  - "$9 ONLY" — Day 5 AM Bakuchiol hero 用

### Lead Copy 规范

- **黑色 18px Century Gothic**（与品牌教育邮件一致）
- **关键文案红色加粗：** 数字 / 价格 / 紧迫语
- **关键短语下划线：** "see proven results in just 28 days." / "dermatologist-approved"
- **斜体蓝色：** 时间锚点 / 威胁话术（"won't be back until BFCM"）
- **Code block 红色加粗：** "MEM10" / "48 hours only"

### 4-Card Grid 规范

每张卡片（2x2 共 4 张）：

| 元素 | 规范 |
|---|---|
| 顶部蓝色横条 | 折扣类型（"50% OFF" / "3 FOR 2" / "FREE CAVIAR STICK" / "BUNDLE"），白底深蓝字 |
| BEST 角标 | 左上椭圆，仅 best-seller 用（Matrixyl 3F2, Peptide Complex 3F2, Peptide Duo Bundle）|
| Dermatologist seal | 右上圆形（"Dermatologist Recommended"）|
| 产品图 | 居中，留白多，产品实物或开盖效果 |
| Tag | 灰色小字，产品定位（"Target Static Wrinkles" / "Smooth & Youthful Glow"）|
| 产品名 | 黑色 14-16px bold |
| 容量 | 灰色小字（"30ml*3" / "50ml"）|
| 评分 | ⭐ 4-4.5 + (review count) |
| 价格 | **红色 sale 价 + 灰色删除线原价** |
| CTA | 黑底白字按钮，**两种格式**（见下） |

**CTA 格式分支：**

| Phase | CTA 格式 | 示例 |
|---|---|---|
| Day 1-4 | "SAVE $XX" 节省额度型 | "SAVE $40" / "SAVE $49" |
| Day 5 PM + Day 6 | "$XX ONLY - SHOP NOW" 价格锚化型 | "$22 ONLY - SHOP NOW" |
| 混合（可选）| 部分用 SAVE 部分用 ONLY | Day 6 实际用了混合 |

### 4-Card 标准组合（按 Day 推荐）

| Day | 主题 | 4 张产品卡 |
|---|---|---|
| 5/20 AM Launch_1 | 群像揭幕 | Matrixyl 3F2 / MPS 3F2 / PEC 50% / Bakuchiol $9 |
| 5/20 PM Launch_2 | 群像动量 | Peptide Duo+Caviar Bundle / Matriplex 50% / MOP 35% / TLQ 30% |
| 5/21 Eye+Texture Trio | Eye + Texture 主题 | PEC 50% / MOP 35% / MPS 3F2 / Matriplex 50% |
| 5/22 Peptide 3F2 + 100-cap | Peptide 主题 | Matrixyl 3F2 / MPS 3F2 / **Face & Eye Duo $57 (100-cap)** / Peptide Duo+Caviar Bundle |
| 5/23 Matriplex + 售罄叙事 | Cream 主题 | Matriplex 50% (hero) / TLQ 30% / MOP 35% / Peptide Duo+Caviar Bundle |
| 5/24 AM Bakuchiol + M1 | Sunday Essentials | Bakuchiol $9 (hero) / M1 50% / Caviar Stick 50% / Matrixyl 3F2 |
| 5/24 PM 24 Hours Left | 红警示（模板 B）| MOP 35% / Caviar 50% / Bakuchiol $9 / PEC 50% (价格 CTA) |
| 5/25 Last Chance | 收尾（模板 C）| Matrixyl 3F2 / MPS 3F2 / MOP 35% / Matriplex 50% (混合 CTA) |

---

## 四、模板 B：红警示型详解（5/24 PM 24 Hours Left）

### 结构（自上而下）

```
┌─────────────────────────────────────────┐
│ [Header logo]                            │
├─────────────────────────────────────────┤
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ ┌────── 红底全宽 banner ──────┐          │
│ │                              │          │
│ │   ONLY 24 HOURS LEFT!        │          │
│ │   THE MEMORIAL DAY SALE      │          │
│ │   (大字白色 sans-serif)       │          │
│ │                              │          │
│ │   [背景：产品瓶倾斜动感]      │          │
│ └──────────────────────────────┘          │
├─────────────────────────────────────────┤
│ LEAD COPY (居中)                          │
│ This is your **last chance** to get the  │
│ BEST savings of the season!               │
│                                           │
│ The offers below won't be back            │
│ until Black Friday (下划线)               │
│                                           │
│ *Shop now or miss out until the end       │
│  of the year.* (蓝色斜体)                 │
├─────────────────────────────────────────┤
│ [PRIMARY CTA] (黑底白字)                  │
│   LAST CHANCE TO SAVE!                    │
├─────────────────────────────────────────┤
│ 4-CARD GRID (价格 CTA)                    │
│ ┌──────────┬──────────┐                  │
│ │ Product  │ Product  │                  │
│ │ ...      │ ...      │                  │
│ │ $22 ~$34~│ $15 ~$30~│                  │
│ │ [$22 ONLY│ [$15 ONLY│  ← 价格化 CTA   │
│ │  - SHOP  │  - SHOP  │                  │
│ │  NOW]    │  NOW]    │                  │
│ └──────────┴──────────┘                  │
│ ┌──────────┬──────────┐                  │
│ │ ...      │ ...      │                  │
│ └──────────┴──────────┘                  │
├─────────────────────────────────────────┤
│ CLOSING COPY                              │
│ "The offer is ending soon, so be sure    │
│  not to miss out!"                        │
├─────────────────────────────────────────┤
│ [SHOP MEMORIAL SALE]                      │
└─────────────────────────────────────────┘
```

### 关键差异（vs 模板 A）

| 元素 | 模板 A | 模板 B |
|---|---|---|
| 顶部 | 白底 + 深蓝 H1 | **红底全宽 banner + 大字白色** |
| Hero | 静态产品摆拍 + STAR badge | **倾斜动感产品瓶 + 危机感构图** |
| Lead 颜色 | 黑色为主 + 红色加粗 | 黑色 + **红色加粗 "last chance"** + 蓝色斜体威胁话术 |
| CTA 主键 | "SHOP MEMORIAL SALE" | **"LAST CHANCE TO SAVE!"** |
| 卡片 CTA | "SAVE $XX" | **"$XX ONLY - SHOP NOW"** |
| 情绪 | 节日 / 期待 / 种草 | **危机 / 紧急 / FOMO** |

---

## 五、模板 C：收尾型详解（5/25 Last Chance）

### 结构

```
┌─────────────────────────────────────────┐
│ [Header logo]                            │
├─────────────────────────────────────────┤
│ HERO                                      │
│   ┌─────────────────────────────┐        │
│   │ LAST CHANCE (红字大写)        │        │
│   │ THE MEMORIAL DAY SALE         │        │
│   │ (深蓝字大写)                   │        │
│   └─────────────────────────────┘        │
│   [Multi-product 群像 + STAR "UP TO 50%"]│
├─────────────────────────────────────────┤
│ LEAD COPY (遗憾叙事)                       │
│ Yes, you'll regret missing the **BIGGEST**│
│ sale of the summer.                       │
│                                           │
│ Stock up on dermatologist-approved        │
│ peptide serums and more—all for less!     │
│ (dermatologist-approved 下划线)            │
│                                           │
│ *Remember—the offer ends at midnight PDT.*│
│ (蓝色斜体)                                 │
├─────────────────────────────────────────┤
│ [PRIMARY CTA]                             │
│   SAVE 50% NOW!                           │
├─────────────────────────────────────────┤
│ 4-CARD GRID (混合 CTA)                    │
│   - 部分用 "$XX ONLY - SHOP NOW"          │
│   - 部分用 "SAVE $XX - SHOP NOW"          │
├─────────────────────────────────────────┤
│ CLOSING                                    │
│ "The offer is ending soon, so be sure    │
│  not to miss out!"                        │
└─────────────────────────────────────────┘
```

---

## 六、跨模板 H1 演进规则（系列叙事弧线）

```
Day 1 AM  →  "The Summer Sale You've Been Waiting For... IS LIVE!"
Day 1 PM  →  "It's Moving Faster Than We Thought — Memorial Sale"
Day 2-4   →  "Celebrate Memorial Day with the Power of Peptides"
              (3 天连用统一 H1，制造系列感)
Day 5 AM  →  "Celebrate Memorial Day with Sunday Essentials"
              (主题切换：周日 + 季节性钩子)
Day 5 PM  →  "ONLY 24 HOURS LEFT! THE MEMORIAL DAY SALE"
              (危机切换：模板 B 红 banner)
Day 6     →  "LAST CHANCE — THE MEMORIAL DAY SALE"
              (收尾切换：模板 C 红字 + 蓝副标)
```

**这个 H1 演进 = 系列邮件最重要的差异化机制**。同样的 4-card grid 可以反复用，但 H1 + Hero badge + Lead copy 必须按这个弧线推进。

---

## 七、合规注意（基于 2025 Email 2 教训）

⚠️ **2025 Email 2（5/22 单 SKU 教育型 Boosting Cream 35%）有合规违规词，2026 不可照抄：**

| 2025 用语 | 2026 替换 |
|---|---|
| "Remove dead skin cells and impurities" | "Helps refresh the look of skin's surface" |
| "Detoxifies and rejuvenates your complexion" | "Refreshes the appearance of your complexion" |
| "Promotes healthy cell turnover" | "Supports natural skin renewal" |
| "Stimulates collagen" | "Supports natural collagen" |

✅ **2025 合规通过的用语（可以沿用）：**
- "dermatologist-approved" — Day 6 Last Chance 用
- "see proven results in just 28 days"
- "broad-spectrum physical protection with zero white cast"
- "it firms, lifts and smooths while you sleep" (Pro-Firming Mask 用语 — 2026 该 SKU 已停产)

完整 blacklist 见 `knowledge/compliance/email-compliance-rules.md`。

---

## 八、链接格式规范（CLAUDE.md 非协商）

| 邮件 | 期间 | 链接格式 |
|---|---|---|
| 5/20 AM/PM Launch | MEM10 有效期内 | `https://depology.com/discount/MEM10?redirect=/products/{slug}` |
| 5/21 Day 2 | MEM10 有效期内 | 仍可用 `/discount/MEM10?redirect=...` |
| 5/22 9 AM 之后 | MEM10 失效 | 切换 `https://depology.com/products/{slug}` 或 `/collections/memorial-2026` |
| 5/22-25 | MEM10 失效，但 SKU 已直接降价 | 标准产品 URL 即可（用户加购看到降价）|

**HTML 注释、alt text 全部英文，不允许中文字符。**

---

## 九、实施 Checklist（视觉资产）

### Hero Image（共 8 张，5/15 之前 ready）

| # | 邮件 | Hero 描述 | STAR Badge 文字 | 模板 |
|---|---|---|---|---|
| 1 | 5/20 AM Launch_1 | Multi-SKU 群像（4-5 个产品摆拍）+ 国旗布料背景 | "UP TO 50% OFF" | A |
| 2 | 5/20 PM Launch_2 | 不同 multi-SKU 群像 + 不同角度 | "UP TO 50% OFF" | A（变体）|
| 3 | 5/21 Eye+Texture Trio | PEC + MOP + MPS 三件 | "50% OFF" | A |
| 4 | 5/22 Peptide 3F2 | Matrixyl 3000 双瓶 + 1 瓶倒置 | "3 FOR 2" | A |
| 5 | 5/23 Matriplex Cream | Matriplex Cream 单品 + 国旗布料 | "50% OFF / LIMITED AVAILABILITY" | A |
| 6 | 5/24 AM Bakuchiol + M1 | Bakuchiol Stick 主 + M1 副 | "ONLY $9" + "M1 50% OFF" | A |
| 7 | 5/24 PM 24 Hrs Left | 倾斜产品瓶动感构图 + 红底背景 | （顶部红 banner 替代 STAR）| B |
| 8 | 5/25 Last Chance | Multi-SKU 群像 + 顶部红字 LAST CHANCE | "UP TO 50% OFF" | C |

### 视觉素材（5/15 之前 ready）

- [ ] STAR badge 矢量图（红蓝双圈 + 5 颗星）— 4 个变体（"UP TO 50%" / "3 FOR 2" / "ONLY $9" / "50% OFF LIMITED"）
- [ ] 国旗布料背景图（高分辨率，hero 群像用）
- [ ] 红底 banner 模板（5/24 PM 顶部用）
- [ ] 倾斜动感构图模板（5/24 PM hero 用）
- [ ] dermatologist seal（4-card grid 右上角用）

---

**模板 A/B/C 实际 HTML 见 `production/email-drafts/templates/` 目录（5/15 之前由 Leon + Claude 协作完成基础模板）**。

---

## 十、与既有体系的关系

- **基础：** 0408 Hydration 白底教育型模板（`20260408_Hydration_Hierarchy.html`）
- **改造点：** 加红蓝 STAR badge + 4-card grid + Memorial 专属配色 + 红警示模板（B）+ 收尾模板（C）
- **未来复用：** July 4th Sale（🟠 Middle，相同美式主题）+ Labor Day（🟠 Middle，可借鉴）
- **不复用：** Easter / Mother's Day / 教育邮件 — 仍用 0408 原版或黑底 0403
