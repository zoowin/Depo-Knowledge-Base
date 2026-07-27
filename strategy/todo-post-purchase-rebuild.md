# 待办立项：Post-Purchase Flow 重做（MEL 教育化）

> 创建日期：2026-06-25
> 状态：📌 已立项，待排产
> 负责：Claude（文案+HTML）/ Leon（Klaviyo 部署+配图）
> 类型：Flow 内容重做（非 campaign）

---

## 背景

全盘梳理 Klaviyo flow 时发现 post-purchase 体系存在重复轰炸 + 内容老旧问题。已完成止血，但核心 flow 需要按品牌 MEL 教育策略重做。

## 现状（2026-06-25）

| Flow | ID | 状态 | 说明 |
|------|-----|------|------|
| Post Purchase [New & Repeat] | `SCZyhi` | live（精简后） | 主 post-purchase；保留新客/老客两封"感谢/确认"首封 |
| Fulfilled Order Post Purchase | `SAwiYB` | **已暂停 (draft)** | 与 SCZyhi 人群完全重合、互不排除 → 重复轰炸，已关 |
| Matrixyl Onboarding | `Uv7r6n` | live | 仅买 Matrixyl 者触发，量小（$367/12mo），与 SCZyhi 重叠待处理 |

**已做的止血动作：**
- ✅ 暂停 SAwiYB（消除下单触发+履约触发的双序列轰炸）
- ✅ 关闭 SCZyhi 新客分支的 `Email 2 - Hype Email`（"results 🔥"，90 天 0 转化）

**SCZyhi 性能（12 个月）：** 转化 65 / 营收 $6,353 / RPR $0.15（偏低）。主力是老客"感谢/确认"首封（$3,931），新客两封合计 $2,422。

## 问题（=重做理由）

1. **内容路线脱节**：现存邮件走"社交关注 + hype + 限时折扣"老路线（2022 年建），与品牌现在的科学教育（MEL）调性完全不符。
2. **缺 post-purchase 核心骨架**：两封感谢邮件都没有"你刚买的产品怎么用"（使用指引/早晚/用量/搭配），新客拿不到见效所需的 onboarding。
3. **老客触点浪费**：老客版 CTA 只有"关注 Instagram"，零复购/补货/交叉销售引导 → 高价值触点没变现。
4. ⚠️ **合规雷区**（新客版"THANKS FOR CHOOSING"）：
   - `guarantee`（"We guarantee you're going to LOVE the results"）→ 黑名单词
   - `transform your skin` / `incredible benefits` → 夸大/绝对化
   - 重做时必须清除，参考 `knowledge/compliance/email-compliance-rules.md`

## 目标

把 post-purchase 从"促销轰炸"重做成"教育型 onboarding"，提升 RPR + 复购铺垫 + 合规，按 MEL 风格（`knowledge/visual/MEL Style.md`）。

## 新结构（草案）

| 序位 | 新客序列 | 老客序列 |
|------|----------|----------|
| 封1 (Day 0–1) | 感谢 + **你买的产品怎么用**（使用指引，确保见效） | 感谢 + 快速使用提醒 |
| 封2 (Day 5–7) | 成分科普 + **逐周预期管理**（科学背书） | **补货/复购提醒**（老客核心） |
| 封3 (Day 14–21) | routine 搭配 + 软交叉销售 → 桥接评价邀请 | VIP/loyalty + 交叉销售 |

- 新客 3 封、老客 2–3 封；用 Klaviyo 产品 block 按"买了什么"做个性化为加分项。
- 评价邀请与现有 Judge.me flow（`WPM2fk`）衔接，避免重复。

## 下一步

- [ ] 关闭 SCZyhi Hype Email（执行中 / Leon 确认）
- [ ] 排进某月 calendar 的产出窗口（建议作为一个独立内容批次）
- [ ] Claude 起草新客封1（使用指引）作为试点 → Leon 配图 → 部署测试
- [ ] 处理 Uv7r6n 与 SCZyhi 的 Matrixyl 重叠（合并或加排除）
- [ ] 重做完成后，评估是否需要重新激活/改写 SAwiYB 的教育邮件素材（"healthy skincare habits"）
