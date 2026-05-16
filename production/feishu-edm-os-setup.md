# Feishu EDM Operating System — 建表操作手册

> 这是给 Leon 手动在飞书创建多维表格的完整规格。按顺序建好 5 张表后，把每张表的 **app_token** 和 **table_id** 告知 Claude，Claude 即可开始数据迁移和自动生产。

---

## 第一步：创建多维表格文件

1. 打开飞书 → 点击"+"创建 → 选择「多维表格」
2. 命名为：**Depology EDM OS**
3. 创建完成后，从 URL 获取 `app_token`：
   - URL 格式：`https://xxx.feishu.cn/base/xxxxxxxxxxxxxx`
   - `app_token` = URL 中 `/base/` 后面的字符串

---

## 第二步：创建 6 张数据表

在同一个多维表格文件内，依次添加以下 6 张表（点击底部"+"新增数据表）。

> **架构说明：** 当前是「半自动模式（Level 2）」。Aily 监听字段变更、写 Task Queue、推消息；Claude Code 读 Task Queue 批量处理生产任务。未来切换全自动只需把 Task Queue 的消费者从 Claude Code 改成 Aily。

---

### 表 1：📅 Campaign Calendar

**表名：** `Campaign Calendar`

| 字段名 | 字段类型 | 选项/说明 |
|--------|----------|-----------|
| Campaign Name | 文本 | 主字段（默认已有） |
| Send Date | 日期 | 格式：YYYY/MM/DD |
| Month | 单选 | 选项：2026-05 / 2026-06 / 2026-07 / 2026-08 / 2026-09 / 2026-10 / 2026-11 / 2026-12 |
| Email Type | 单选 | 选项：Education / Promo / Social Proof / Lifestyle / Trend |
| Product Line | 多选 | 选项：A / B / C / E / F / G / H |
| Hero Product | 文本 | 主推 SKU 全名 |
| Status | 单选 | 选项（含颜色）：📋 Planning（灰） / ✍️ Draft Requested（蓝） / ⚡ Generating（黄） / 👀 Review（橙） / ✅ Approved（绿） / 🎨 Image Needed（紫） / 🔧 HTML Build（蓝） / 🚀 Deployed（深绿） / 📊 Live（绿） |
| Subject Line | 文本 | 最终选用的 SL |
| Preview Text | 文本 | |
| Klaviyo Campaign ID | 文本 | 部署后由 Claude 回写 |
| Discount Code | 文本 | 促销邮件适用 |
| Notes | 多行文本 | |

**视图设置：**
- 默认网格视图保留
- 添加「日历视图」→ 日期字段选 Send Date
- 添加「看板视图」→ 分组字段选 Status

---

### 表 2：✍️ Draft Workshop

**表名：** `Draft Workshop`

| 字段名 | 字段类型 | 选项/说明 |
|--------|----------|-----------|
| Draft Title | 文本 | 主字段，如：Micro-dart Draft v1 |
| Campaign | 关联其他记录 | 关联到「Campaign Calendar」表 |
| Draft Status | 单选 | 选项：Requested（红） / Generating（黄） / Ready for Review（蓝） / Revision Needed（橙） / Approved（绿） |
| Subject Lines | 多行文本 | 3-4 候选，带/不带 emoji 各版本 |
| Preview Text | 文本 | 40-90 字符 |
| Hero Headline | 文本 | TB1，≤9 词 |
| Hero Subheadline | 多行文本 | |
| Hero CTA | 文本 | 如：Explore the Science |
| Body Headline | 文本 | TB2，≤8 词 |
| Body Copy | 多行文本 | 2-4 段正文 |
| Body CTA | 文本 | |
| Product Cards | 多行文本 | HB1/2/3 完整文案（Markdown 格式） |
| Hero Image Brief | 多行文本 | 给设计师/AI 的图片描述 |
| AI Image Prompt | 多行文本 | ChatGPT/Midjourney 可直接使用的 prompt |
| Hero Image URL | 超链接 | Klaviyo CDN 链接（Leon 上传后填入） |
| Revision Notes | 多行文本 | Leon 审阅意见 → Claude 据此修改 |
| HTML File Path | 文本 | 本地 HTML 文件相对路径 |
| Klaviyo Template ID | 文本 | 部署后由 Claude 回写 |
| Created At | 创建时间 | 自动 |

**视图设置：**
- 添加「看板视图」→ 分组字段选 Draft Status

---

### 表 3：📊 Performance Dashboard

**表名：** `Performance Dashboard`

| 字段名 | 字段类型 | 选项/说明 |
|--------|----------|-----------|
| Campaign Name | 文本 | 主字段 |
| Campaign | 关联其他记录 | 关联到「Campaign Calendar」表 |
| Send Date | 日期 | |
| Open Rate | 数字 | 格式：百分比（如输入 0.245 显示 24.5%）|
| Click Rate | 数字 | 百分比 |
| CTOR | 数字 | Click-to-Open Rate，百分比 |
| Conv% | 数字 | 转化率，百分比 |
| Revenue | 货币 | USD |
| RPR | 数字 | Revenue Per Recipient（$），保留 4 位小数 |
| Unsub Rate | 数字 | 退订率，百分比 |
| Rating | 单选 | 选项：A（绿） / B（蓝） / C（黄） / D（红） |
| Key Learning | 多行文本 | Claude 生成的复盘总结 |
| Klaviyo Campaign ID | 文本 | 对应 Klaviyo ID |
| Synced At | 创建时间 | 自动 |

**视图设置：**
- 添加「图表视图」→ X 轴: Send Date，Y 轴: Open Rate + Revenue（双轴折线图）

---

### 表 4：🎯 Topic Pool

**表名：** `Topic Pool`

| 字段名 | 字段类型 | 选项/说明 |
|--------|----------|-----------|
| Topic | 文本 | 主字段，话题角度名称 |
| Category | 单选 | 选项：🟢 Education / 🔵 Social Proof / 🔴 Promo / 🟡 Lifestyle / 🧪 Testing |
| Description | 多行文本 | 角度说明和切入思路 |
| Product Line | 多选 | 选项：A / B / C / E / F / G / H |
| Priority | 数字 | 1-5（5 = 最高优先级） |
| Status | 单选 | 选项：Available（绿） / Scheduled（蓝） / Used（灰） / Archived（红） |
| Last Used | 日期 | 最近一次使用日期（45 天防重复规则） |
| Source | 单选 | 选项：Manual / Google Trends / Reddit / AI Generated |

---

### 表 5：🛍️ Promotion Calendar

**表名：** `Promotion Calendar`

| 字段名 | 字段类型 | 选项/说明 |
|--------|----------|-----------|
| Event Name | 文本 | 主字段，如：Memorial Day Sale 2026 |
| Start Date | 日期 | |
| End Date | 日期 | |
| Level | 单选 | 选项：Big（红） / Middle（橙） / Small（黄） / None（灰） |
| Discount Code | 文本 | 如：MEMORIAL20 |
| Discount Type | 文本 | 如：20% OFF sitewide |
| VIP Prewarm Date | 日期 | VIP 提前预热日期 |
| Landing URL | 超链接 | Shopify 落地链接（含 /discount/ 格式） |
| Email Count | 数字 | 该活动对应的邮件封数 |
| Status | 单选 | 选项：Planning（灰） / Active（绿） / Completed（蓝） |
| Notes | 多行文本 | |

---

### 表 6：📬 Task Queue（任务队列 - 半自动模式核心）

**表名：** `Task Queue`

| 字段名 | 字段类型 | 选项/说明 |
|--------|----------|-----------|
| Task ID | 文本 | 主字段，格式：YYYYMMDD-HHMMSS-{type}（如 20260601-093015-draft） |
| Task Type | 单选 | 选项：generate_draft / revise_draft / build_html / deploy_klaviyo / sync_performance / plan_month / monthly_review |
| Target Record ID | 文本 | 关联的 record_id（来自 Campaign Calendar 或 Draft Workshop） |
| Target Table | 单选 | 选项：Campaign Calendar / Draft Workshop / Performance Dashboard |
| Status | 单选 | 选项：⏳ Pending（黄）/ 🔄 Processing（蓝）/ ✅ Done（绿）/ ❌ Failed（红） |
| Priority | 单选 | 选项：High / Normal / Low |
| Payload | 多行文本 | JSON 格式，包含执行任务需要的所有上下文 |
| Created By | 单选 | 选项：Aily / Leon / Cron |
| Created At | 创建时间 | 自动 |
| Started At | 日期时间 | Claude Code 开始处理时填 |
| Completed At | 日期时间 | 完成时填 |
| Error Message | 多行文本 | 失败时记录错误 |
| Claude Notes | 多行文本 | Claude Code 执行过程的简要说明 |

**视图设置：**
- 默认视图：按 Status 筛选只显示 Pending + Processing
- 看板视图：按 Status 分组

**用法：**
- Aily 检测到 bitable 字段变更 → 新建一行 Task（Status = Pending）
- Leon 在 Claude Code 说"清空待办队列" → Claude Code 读取所有 Pending Task → 逐一处理 → 写 Done
- 失败的 Task 自动重试 1 次，仍失败则 Status = Failed 并发飞书提醒

---

## 第三步：获取 Table ID

每张表建好后，获取 table_id：
1. 在多维表格内点击对应数据表
2. 查看 URL：`https://xxx.feishu.cn/base/{app_token}?table={table_id}&view={view_id}`
3. `table_id` = URL 参数 `table=` 后面的字符串（通常以 `tbl` 开头）

---

## 第四步：告知 Claude

建好所有表后，发给 Claude：
```
飞书多维表格已创建完成：
- app_token: [你的 app_token]
- Campaign Calendar table_id: [tblXXXXXX]
- Draft Workshop table_id: [tblXXXXXX]
- Performance Dashboard table_id: [tblXXXXXX]
- Topic Pool table_id: [tblXXXXXX]
- Promotion Calendar table_id: [tblXXXXXX]
- Task Queue table_id: [tblXXXXXX]
- 桥接群 chat_id: [oc_xxxxxx]（新建的 Depology EDM Bridge 群）
```

Claude 收到后会自动执行数据迁移，把现有 Markdown 文件中的历史数据全部写入飞书。

---

## 预计时间

| 阶段 | 操作者 | 时间 |
|------|--------|------|
| 创建多维表格 + 5 张表 | Leon | ~60 分钟 |
| 数据迁移（campaign-log、topic-pool 等） | Claude | ~15 分钟 |
| 首次端到端草稿测试 | Leon + Claude | ~10 分钟 |

---

## 通知渠道

Claude 生成草稿后会发消息到飞书群：**Email**（chat_id: `oc_3a7115c5c5b70ed83ed3435765b4492d`）

格式示例：
> ✅ **[Micro-dart Science] 草稿已就绪**
> Draft Status 已更新为 Ready for Review，请在飞书 Draft Workshop 查看并填写 Revision Notes。
