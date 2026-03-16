# Depology EDM — Draft 输出模板（标准格式）

> Claude 每次生成邮件草稿必须严格按此格式输出。
> Leon 按区块复制粘贴到 Klaviyo 对应位置即可。
> 最后更新：2026-03-16

---

## 模板说明

本模板为**通用格式**，适配所有 Klaviyo drag & drop 模板：
- **VE92sd** — 教育型（黑白配色，有产品角色标签 + 底部总 CTA）
- **R5x7wg** — 通用型（简洁配色，统一 SHOP NOW）
- 未来新模板（促销、强促销、情感等）也使用此格式

---

## Draft 标准格式

```markdown
# YYYYMMDD_Campaign_Topic

## Campaign Info
- **Template:** VE92sd / R5x7wg / [其他]
- **Type:** Educational / General / Promotional / Emotional
- **Send Date:** YYYY-MM-DD
- **Segment:** [目标人群]
- **Product Focus:** Line X — [产品名]
- **Goal:** [一句话目标]

---

## Subject Lines
1. [候选1]
2. [候选2]
3. [候选3]

## Preview Text
[40-90 字符，延伸 subject line，不重复]

---

## Hero Section
> 📐 对应 Klaviyo 位置：Hero Image 下方第一个 Text Block

**Hero Image 方向：** [一句话描述画面概念，用于生成 AI prompt]

**Headline：**
[≤9 英文词 / ≤50 字符]
[单一信号：结果 / 真相 / 场景]

**Subheadline：**
Line 1: [≤30 字符]
Line 2: [≤30 字符]

**Hero CTA：**
[非购买类：EXPLORE / LEARN MORE / DISCOVER]

---

## Body Section
> 📐 对应 Klaviyo 位置：Hero 下方 Text Block（黑底或白底区域）

**Body Headline：**
[≤5 英文词 / ≤30 字符]

**Body Copy（3 段）：**
Paragraph 1: [场景代入 / 问题 — ~110 字符]
Paragraph 2: [原因解释 / 痛点深化 — ~145 字符]
Paragraph 3: [转折 / 引导解决方案 — ~120 字符]

**总计正文：~376 字符 / ~70 词**

---

## Goals / Key Points（可选）
> 📐 对应 Klaviyo 位置：Body 下方 checklist 区域

- ✔ [要点 1 — ~50 字符]
- ✔ [要点 2 — ~45 字符]
- ✔ [要点 3 — ~50 字符]

---

## Product Section
> 📐 对应 Klaviyo 位置：Product Cards 区域（通常 2-3 张卡片）

**Section Title（如 VE92sd 需要）：**
[≤5 词，如 "Potent Results Zero Irritation"]

### Product 1
- **角色标签（VE92sd）：** [如 "The Builder (Matrixyl®)" — ≤25 字符]
- **产品名：** [完整产品名]
- **描述：** [结果导向，~120 字符，不堆成分]
- **CTA：** SHOP [PRODUCT NAME] / SHOP NOW
- **链接：** [Shopify 产品链接]

### Product 2
- **角色标签（VE92sd）：** [如 "The Relaxer (Argireline™)"]
- **产品名：** [完整产品名]
- **描述：** [~120 字符]
- **CTA：** SHOP [PRODUCT NAME] / SHOP NOW
- **链接：** [Shopify 产品链接]

### Product 3
- **角色标签（VE92sd）：** [如 "The Shield (Caviar Stick)"]
- **产品名：** [完整产品名]
- **描述：** [~120 字符]
- **CTA：** SHOP [PRODUCT NAME] / SHOP NOW
- **链接：** [Shopify 产品链接]

---

## Closing Section（VE92sd 需要，R5x7wg 可选）
> 📐 对应 Klaviyo 位置：Product Cards 下方最后一个 Text Block

**Closing Copy：**
[1-2 句，长期/日常/可坚持 — ~80 字符]

**Final CTA：**
[结果导向 — 如 "BUILD YOUR FUTURE SKIN" — ≤25 字符]

---

## Hero Image Brief
> 📐 用于 ChatGPT / Midjourney 生成图片，不放入 Klaviyo

**概念：** [画面描述]
**风格：** [参考 MEL Style — 成熟、干净、科学感]
**AI Prompt：**
```
[完整的 Midjourney / DALL-E prompt]
```
```

---

## 字数速查表

| 区块 | 字数限制 | 备注 |
|------|---------|------|
| Subject Line | ≤60 字符 | 3 个候选，可含 emoji 作为 A/B test 变量 |
| Preview Text | 40-90 字符 | 延伸 subject，不重复 |
| Headline | ≤9 词 / ≤50 字符 | 单一信号 |
| Subheadline | 2 行，每行 ≤30 字符 | 承接 Headline |
| Hero CTA | ≤15 字符 | 非购买类 |
| Body Headline | ≤5 词 / ≤30 字符 | 被忽视的事实 |
| Body Copy | 共 ~376 字符 / 3 段 | 场景→原因→转折 |
| Goals 列表 | 3 条，每条 ≤50 字符 | ✔ 开头 |
| Product 描述 | 每个 ~120 字符 | 结果导向 |
| Product CTA | ≤20 字符 | SHOP [NAME] |
| Closing Copy | ~80 字符 | 长期价值 |
| Final CTA | ≤25 字符 | 结果导向 |

---

## 关键规则

1. **所有正文用英文**，说明和注释可以用中文
2. **Subject Line emoji 自由**：可以提供带 emoji 和不带 emoji 的版本，作为 A/B test 打开率对比变量
3. **产品描述必须来自 SKU 卡片**（`knowledge/products/`），不允许编造
4. **合规检查**：发稿前对照 `knowledge/compliance/email-compliance-rules.md`
5. **每封邮件指定一个 Klaviyo 模板**，在 Campaign Info 中标明
