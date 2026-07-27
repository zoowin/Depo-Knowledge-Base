# Flow 邮件合规复核 — 2026-06-25

> 范围：5 条主力 flow 全量邮件（弃结账 / 弃购 / 弃浏 / Winback / Welcome），约 50 封（含 A/B 变体）。
> 方法：5 路并行审核，拉取每封正文文本，对照 `email-compliance-rules.md` 黑名单扫描。

## ⚠️ 关键前提：全是图片型邮件
这 5 条 flow 的正文文案几乎全部嵌在图片（PNG）的 alt/title 里，模板无可编辑文字段。**含义：**
1. 改文案 = **重做图片素材**（不是改 HTML）。
2. 部分图片型模板 API 读不到正文（见末尾"盲区"），需人工在 Klaviyo 看图核对。
3. 关图后用户看到空白（text fallback 为空），无障碍/可达性差。

---

## 🚨 P0 — 必须立即处理（红线 / 掉钱）

| # | Flow / 邮件 | 问题 | 处理 |
|---|---|---|---|
| 1 | **弃结账 #4 "Last chance"** | 推荐**已停产产品**：Anti-Aging Retinol Night Cream、Pro-Firming Dream Mask → 客户点进死链/买不到，合规+商品准确性双错 | 移除/替换为在售 SKU |
| 2 | **弃浏 #3** | "restored, **regenerated**, and renewed" → 命中黑名单 **regenerate**（暗示改变皮肤结构） | 改 "refreshed, replenished, and renewed" |
| 3 | **弃结账 #2（+2个变体）** | Jennifer 评价 "she asked if I had done **injectables**…" → "injectable results" 红线，3 封共用、触达大 | 换评价或删去 injectables 对比 |
| 4 | **折扣链接格式（系统性）** | 弃结账 #3/#3A/#3B/#4B、弃浏 #2/#3 全系列用 `?discount=CODE` 查询参数 → 违反硬规则，**码不自动应用→客户结账没折扣→直接流失** | 全部换成 `/discount/{CODE}?redirect=` |
| 5 | **弃购 #1 + Winback #2** | 弃购："say goodbye to wrinkles **for good**"（永久暗示）、SL "reduction in fine lines **in 4 weeks**"（无据时效）；Winback #2："**SLOW THE AGING PROCESS**"（药物声称） | 改外观/过程表述 |
| 6 | **临床数据无脚注** | 弃结账 #2-VarB、弃购 #2："46.31%… **clinically proven**" 无人数/来源 → FTC 风险 | 补 `*Based on a [N]-person study` 脚注 |

## 🟧 P1 — 批量统一修

- **效果证言普遍缺 `*Individual results may vary.` 免责**（弃结账 #2/#4A、弃购 #4A、弃浏 #1/#3 等）→ FTC Endorsement 风险，所有含强效果评价的邮件底部统一补。
- **散见黑名单/夸大词**：`magic`（弃结账 #2B/#4A）、`treat`（弃浏 #2 subject、Welcome #1.5）、`transform/transformative`（弃结账 #4、Welcome #5）、`literally overnight`（弃结账 #4A，即时承诺）、`100%/💯`（弃浏 #1/#3）、`incredible results`（弃浏、弃购）。
- **社证背书需溯源**：Welcome #5 "Depology WORKS"、弃购 #2 "doctor recommended" / "RECOMMENDED BY DOCTORS"（与正文具名引述口径不符）→ 确认真实出处或改表述。

---

## 各 Flow 风险速览

| Flow | ID | 邮件数 | 风险 | 一句话 |
|---|---|---|---|---|
| 弃结账 Abandoned Checkout | `YmrJTu` | 16 | **高** | 停产产品 + injectables 评价 + 临床无脚注 + 链接格式 |
| 弃浏 Browse Abandonment | `TtcziZ` | 16 | **高** | regenerate 红线 + treat subject + 100% + 无 disclaimer，2022 旧文案 |
| 弃购 Abandoned Cart | `Y9uwrR` | 6 | 中 | for good/4weeks/doctor，~16 处 |
| Welcome | `RKQ5fs` | 8 | 中低 | transformative + 社证溯源；6 封图片正文是盲区 |
| Winback | `RNA7fy` | 5 | 低 | 仅 "slow the aging process" 一处明显 |

## 🕳 盲区（API 读不到，需人工在 Klaviyo 看图核对）
- 弃结账：`X4KAMb`（#3A "Crow's feet no more!" 正文）、`SmiziB`（#3B-VarB）
- Welcome：6 封图片正文（#1、#2、#3、#4、#5、#6）

---

## 战略结论
这些都是 2022–2024 的旧 flow，文案与现行品牌合规标准**严重脱节**，且全是图片型——**合规整改 ≈ 重做素材**。两条路径：
- **短期止血**：先修 P0（停产产品、regenerate、injectables、折扣链接格式），其中链接格式是直接掉钱项，优先。
- **中长期**：把弃结账/弃浏这两条高风险旧 flow，连同 post-purchase 一起纳入 **MEL 风格重做计划**，而非逐词打补丁。
