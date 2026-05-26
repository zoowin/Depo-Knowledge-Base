# Feishu EDM OS — Flow 全景图

> 一个完整的 EDM 操作系统不是表格，是 **flows**。
> 这里列出从规划到效果回收的所有 12 个 flow，每个 flow 都有明确的触发条件、Claude 行为、输出。

---

> ⚠️ **schema 校准说明(2026-05-22)** —— 本文档是早期设计稿,部分字段名/枚举值与
> 线上真实表不一致。**线上表结构以 `feishu-edm-os-setup.md` 为准。** 已知偏差:
>
> | 本文档写的 | 线上实际 |
> |-----------|---------|
> | Campaign Calendar 单一 `Subject Line` | 拆为 `Subject Line A` / `Subject Line B` |
> | Draft Status 带 emoji(`👀 Ready for Review`、`✏️ Revision Needed`) | 无 emoji:`Requested / Generating / Ready for Review / Revision Needed / Approved` |
> | Draft Status `🎨 Awaiting Image`、`🔧 HTML Ready` | 线上不存在;`Approved` 之后无更细的 Draft Status |
> | Campaign Calendar Status `📤 Sent` | 线上不存在,发送后直接进 `📊 Live` |
> | 表名 `Performance Dashboard` | 线上叫 `Campaign 数据`,指标字段名带 `(%)`/`($)` 后缀 |
> | Task Queue(机器任务队列) | 已重设计为人读任务板,见 `feishu-bridge-protocol.md` 顶部校准说明 |
>
> 下方 flow 的**逻辑设计仍然有效**,执行前按上表换算字段名与枚举值。

---

## Flow 时间轴

```
月初规划 ───────► 草稿生成 ───────► 审阅修改 ───────► 批准
   │                  │                  │             │
   ▼                  ▼                  ▼             ▼
月度日历            草稿就绪          修改完成        待制图
                                                       │
                                                       ▼
                                                  Hero Image
                                                       │
                                                       ▼
效果复盘 ◄──── 数据回收 ◄──── Klaviyo 发送 ◄──── HTML 构建
```

---

## 🟦 Flow 1：月度规划 Flow

**触发：** 每月 1 日上午 9:00（飞书定时提醒 / 手动："规划下月日历"）

**Claude 行为：**
1. 通过 Klaviyo MCP 拉取上月所有 campaign 数据
2. 写入 Performance Dashboard（每条 campaign 一行）
3. 计算上月类别表现（Education vs Promo vs Social Proof 哪类 Revenue 最高）
4. 读 Promotion Calendar 检查下月活动（Big/Middle/Small/None）
5. 读 Topic Pool 中 Status = Available 的话题
6. 排除：45 天内用过的话题角度、30 天内推过的主力产品
7. 按比例生成下月 8-15 封 campaign 计划
8. 批量写入 Campaign Calendar（Status = "📋 Planning"）
9. 发飞书消息到 Email 群："📅 [Month] 月度日历已生成，X 封邮件待排期"

**输入数据源：** Klaviyo + Topic Pool + Promotion Calendar + Performance Dashboard
**输出：** Campaign Calendar 新增 N 条记录

---

## 🟦 Flow 2：草稿生成 Flow

**触发：** Campaign Calendar 中某条记录 Status 从 "📋 Planning" → "✍️ Draft Requested"
（Leon 在飞书改字段时触发）

**Claude 行为：**
1. 读取该 campaign 的所有字段（Type, Product Line, Hero Product, Notes, Discount Code）
2. 立即更新 Status → "⚡ Generating"（防止重复处理）
3. 读 `knowledge/products/[Line]/` 对应产品知识
4. 读 `knowledge/compliance/` 合规规则
5. 检查重复（过去 45 天话题角度 / 30 天产品）
6. 按 Copy Winning Formula 生成完整草稿
7. 在 Draft Workshop 新建一条记录，填入：
   - 关联 Campaign（双向链接）
   - Subject Lines (3-4 候选)
   - Preview Text
   - Hero Headline / Subheadline / CTA
   - Body Headline / Copy / CTA
   - Product Cards (HB1/2/3)
   - Hero Image Brief
   - AI Image Prompt
8. Draft Status → "👀 Ready for Review"
9. Campaign Calendar Status → "👀 Review"
10. 发飞书消息："✅ [Campaign Name] 草稿已就绪，请审阅"

**预估耗时：** 2-3 分钟/封

---

## 🟦 Flow 3：修改反馈 Flow

**触发：** Draft Workshop 中某条记录 Draft Status 从 "👀 Ready for Review" → "✏️ Revision Needed"
（且 Revision Notes 字段已填写内容）

**Claude 行为：**
1. 读取 Revision Notes 内容
2. 解析反馈类型（SL 改 / 文案改 / 产品换 / 角度换）
3. 按反馈修改对应字段（保留其他字段）
4. 在 Revision Notes 末尾追加："✅ Claude 已修改 [日期] - [修改概要]"
5. Draft Status → "👀 Ready for Review"
6. 发飞书消息："✏️ [Campaign Name] 已按反馈修改"

**支持迭代：** Leon 可以多轮修改，每轮都通过 Revision Notes 字段交互

---

## 🟦 Flow 4：批准 & 制图 Flow

**触发：** Draft Status 从 "👀 Ready for Review" → "✅ Approved"

**Claude 行为：**
1. 验证草稿完整性（所有必填字段都已填）
2. 把 AI Image Prompt 复制到飞书消息中，发到 Email 群：
   ```
   🎨 [Campaign Name] 草稿已批准，请生成 Hero Image
   
   📋 AI Image Prompt:
   [完整 prompt]
   
   📐 规格: 600 x 400px, PNG
   👉 生成后上传到 Klaviyo，把 CDN URL 填入飞书 Draft Workshop 的 Hero Image URL 字段
   ```
3. Campaign Calendar Status → "🎨 Image Needed"
4. Draft Workshop Draft Status → "🎨 Awaiting Image"

**Leon 的工作：** 用 ChatGPT/Midjourney 生成图 → 上传 Klaviyo → 把 URL 填回飞书

---

## 🟦 Flow 5：HTML 构建 Flow

**触发：** Draft Workshop 中 Hero Image URL 字段被填入（非空）

**Claude 行为：**
1. 自动选择基础模板：
   - 教育型 Campaign → `20260408_Hydration_Hierarchy.html`（白底）
   - 促销型 Campaign → `20260403_Easter_Sale_Opening.html`（黑底）
2. 生成 replacements.json（从 Draft Workshop 字段读取）
3. 运行 `python3 tools/build_campaign_html.py`
4. 输出 HTML 到 `production/html-output/YYYYMMDD_Campaign.html`
5. 把文件路径填入 Draft Workshop 的 HTML File Path 字段
6. Status → "🔧 HTML Ready"
7. 发飞书消息（附本地 HTML 路径）："🔧 HTML 已构建，预览路径：xxx，确认后回 'deploy [campaign name]'"

---

## 🟦 Flow 6：Klaviyo 部署 Flow

**触发：** Leon 在飞书回复"deploy [campaign name]"，或手动改 Status → "🚀 Ready to Deploy"

**Claude 行为：**
1. 读取 HTML File Path
2. 读取 Subject Line / Preview Text / Send Date
3. 运行 `python3 tools/klaviyo_deploy_campaign.py`：
   - 创建 Klaviyo 模板
   - 创建 campaign（带标准人群 + 排除人群）
   - Assign 模板到 campaign
4. 回写飞书：Klaviyo Template ID + Klaviyo Campaign ID
5. Campaign Calendar Status → "🚀 Deployed"
6. 发飞书消息："🚀 [Campaign Name] 已部署到 Klaviyo，请在 Klaviyo 后台 schedule send"

---

## 🟦 Flow 7：发送确认 Flow

**触发：** Campaign 发送时间到（飞书定时检测 Campaign Calendar 中 Send Date = 今天的记录）

**Claude 行为：**
1. 通过 Klaviyo MCP 验证 campaign 是否已发送
2. 若已发送：Status → "📤 Sent"，记录实际发送时间
3. 若未发送：发飞书提醒"⚠️ [Campaign Name] 应在今日发送但未检测到，请检查 Klaviyo"
4. 启动 Flow 8 定时器（48 小时后自动回收数据）

---

## 🟦 Flow 8：效果回收 Flow

**触发：** Campaign 发送后 48-72 小时（飞书定时 / 手动："同步昨日效果"）

**Claude 行为：**
1. 找到 Campaign Calendar 中 Status = "📤 Sent" 且 Synced At 为空的记录
2. 通过 Klaviyo MCP 拉取每条 campaign 的指标：
   - Open Rate, Click Rate, CTOR, Conversion Rate
   - Revenue, RPR, Unsubscribe Rate
3. 写入 Performance Dashboard（新建一行）
4. 按 Benchmarks 自动评级（A/B/C/D）
5. 生成 Key Learning 摘要（Claude 分析"为什么这封表现好/差"）
6. Campaign Calendar Status → "📊 Live"
7. 发飞书消息："📊 [Campaign Name] 数据已同步 - Rating: B, Revenue: $X, OR: Y%"

---

## 🟦 Flow 9：月末复盘 Flow

**触发：** 每月最后一天晚上 9:00

**Claude 行为：**
1. 读取 Performance Dashboard 当月所有数据
2. 统计：
   - 总 Revenue, 平均 OR, 平均 CR
   - 类别表现排序（Education / Promo / Social Proof / Lifestyle / Trend）
   - Top 3 winners（按 Revenue）+ Bottom 2 losers
   - 哪些产品线表现最好
3. 把 Topic Pool 中本月已用话题的 Status → "Used"，Last Used → 发送日期
4. 生成本月复盘报告，写入飞书一个独立的 Markdown 文档（或新建 Monthly Report 字段）
5. 发飞书消息（含核心数字 + Top 3 winners + 下月建议）

---

## 🟦 Flow 10：话题补充 Flow

**触发：** 每月 1 日早上 8:00 / 手动："更新话题池"

**Claude 行为：**
1. 运行 `python3 tools/fetch_trends.py`
2. 解析返回的 Reddit + Google Trends 话题
3. 用 GPT 角度判断每个话题适合的 Category 和 Product Line
4. 批量写入 Topic Pool（Status = "Available", Source = "Google Trends" 或 "Reddit"）
5. 去重（如果 Topic 名已存在则跳过）
6. 发飞书消息："🎯 话题池已补充 X 个新角度"

---

## 🟦 Flow 11：促销活动预热 Flow

**触发：** 飞书定时每周一早上检查 Promotion Calendar

**Claude 行为：**
1. 找到 Start Date 在未来 2-3 周内的活动
2. 检查 Level：
   - Big 活动 → 提醒"3 周前开始 VIP 预热"
   - Middle 活动 → 提醒"1-2 周前开始 VIP 预热"
3. 自动生成预热 campaign 草稿，写入 Campaign Calendar
4. 发飞书消息："⏰ [Event Name] 还有 X 天，预热邮件草稿已生成"

---

## 🟦 Flow 12：重复检查 Flow（防重复使用）

**触发：** 每次 Flow 2（草稿生成）执行前内置调用

**Claude 行为：**
1. 取目标 campaign 的 Topic 关键词 + Hero Product
2. 查询 Campaign Calendar：
   - 过去 45 天有无相同话题角度
   - 过去 30 天有无相同主力产品
3. 若有冲突 → 在飞书 Notes 字段加警告标签 "⚠️ Topic conflict with [date]'s [campaign name]"
4. 仍允许生成（用户决策），但视觉提示

---

## Flow 触发机制总结

| 触发方式 | 数量 | 实现机制 |
|----------|------|----------|
| 飞书字段状态变更（自动） | 6 个 (Flow 2/3/4/5/6/8) | Leon 在飞书改状态 → Claude 轮询/MCP 检测 → 执行 |
| 飞书定时自动 | 5 个 (Flow 1/7/9/10/11) | 飞书自动化触发 → Webhook / Claude 定时轮询 |
| 用户手动触发 | 所有 | Leon 在 Claude Code 说话触发 |
| 内置流程 | 1 个 (Flow 12) | Flow 2 调用前自动执行 |

---

## 状态机：Campaign 完整生命周期

```
📋 Planning
   ↓ (Leon: 准备好写了)
✍️ Draft Requested
   ↓ (Flow 2 自动)
⚡ Generating
   ↓ (Flow 2 完成)
👀 Review
   ↓ (Leon: 改吗?)
   ├─→ ✏️ Revision Needed ──→ (Flow 3) ──→ 👀 Review (循环)
   └─→ ✅ Approved
            ↓ (Flow 4)
       🎨 Image Needed
            ↓ (Leon 填 Hero Image URL)
       🔧 HTML Build
            ↓ (Flow 5)
       🔧 HTML Ready
            ↓ (Leon: deploy / Flow 6)
       🚀 Deployed
            ↓ (Flow 7, 发送时间到)
       📤 Sent
            ↓ (Flow 8, 48-72hr 后)
       📊 Live (数据已记录)
```

---

## 下一步设计决策

需要你确认：

1. **Flow 触发方式选型** —— 选用飞书定时轮询、Claude Code 定时、还是飞书自动化 webhook？
2. **Hero Image 是否纳入 Claude 闭环** —— 现在 Leon 手动生成，未来要不要接 DALL-E API 让 Claude 直接生成图？
3. **复盘报告输出形式** —— 飞书消息 / 飞书文档 / 单独的 Monthly Review 表？
4. **A/B test 标记** —— 飞书表格里要不要加 "A/B Variant" 字段，专门追踪 A/B 对照组？
