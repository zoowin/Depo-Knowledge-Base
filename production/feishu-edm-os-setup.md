# Feishu EDM OS — 实时表结构参考

> 多维表格已建好并已填入数据,本文件是**线上真实表结构**的参考(非建表手册)。
> 最后核对:2026-05-22(由 Claude 通过 API dump 实际字段生成)

---

## 接入信息

| 项 | 值 |
|----|-----|
| 形态 | wiki 内嵌多维表格 |
| 打开链接 | https://ka1js7qy9xg.feishu.cn/wiki/UP5iw1W63iklvYk0wJHckAm8nCh |
| `app_token`(API 用) | `UP5iw1W63iklvYk0wJHckAm8nCh`(wiki token 可直接当 app_token) |
| 操作应用 | `cli_a923ac5a14f8dcc2`(凭证见 `.env` 的 `FEISHU_APP_ID/SECRET`) |
| 通知群 chat_id | `oc_3a7115c5c5b70ed83ed3435765b4492d`(Email 群) |

**权限说明:** 该应用有 bitable 记录读写权限,可直接用 wiki token 操作 6 张表;
但**没有** `wiki:*` 权限,所以不能用 wiki 节点 API。所有读写走 `bitable/v1/apps/{app_token}/...`。

`.env` 已配置 `FEISHU_APP_TOKEN` + 6 个 `FEISHU_TABLE_*`,脚本和 MCP 直接读。

---

## 表 1：Campaign Calendar — `tblFRpkA3BAdiE0o`

EDM 排期主表。16 字段。

| 字段 | 类型 | 选项/说明 |
|------|------|-----------|
| Campaign Name | 文本 | 主字段 |
| Month | 单选 | 2026-05 … 2026-12 |
| Product Line | 多选 | A / B / C / E / F / G / H |
| Hero Product | 文本 | 主推 SKU |
| Email Type | 单选 | Educational / Promotional / Social Proof / Lifestyle / Trend / Storytelling |
| Send Date | 日期 | |
| Klaviyo Campaign ID | 文本 | 部署后回写 |
| Subject Line A | 文本 | A/B test 变体 A |
| Subject Line B | 文本 | A/B test 变体 B |
| Preview Text | 文本 | |
| Status | 单选 | 📋 Planning / ✍️ Draft Requested / ⚡ Generating / 👀 Review / ✅ Approved / 🎨 Image Needed / 🔧 HTML Build / 🚀 Ready to Deploy / 🚀 Deployed / 📊 Live ⚠️ `Ready to Deploy`(待部署)与 `Deployed`(已部署)是两个阶段,非重复,仅 emoji 相同 |
| Notes | 文本 | 目前也临时存放 Klaviyo 拉取的效果数据 |
| Discount Code | 文本 | |
| Topic Angle | 文本 | 话题切入角度 |
| Drafts | 双向关联 | → Draft Workshop |
| Klaviyo Template ID | 文本 | 部署后回写 |

---

## 表 2：Draft Workshop — `tblR7C9nGhTsixPl`

草稿工作台。19 字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| ID | 自动编号 | |
| Draft Title | 文本 | 主字段 |
| Preview Text | 文本 | 40-90 字符 |
| Subject Lines | 文本 | 候选 SL 集合 |
| Draft Status | 单选 | Requested / Generating / Ready for Review / Revision Needed / Approved |
| Hero Headline | 文本 | TB1，≤9 词 |
| Hero Subheadline | 文本 | |
| Hero CTA | 文本 | |
| Body Headline | 文本 | TB2，≤8 词 |
| Body Copy | 文本 | 2-4 段 |
| Body CTA | 文本 | |
| Product Cards | 文本 | HB1/2/3 文案 |
| Hero Image Brief | 文本 | |
| AI Image Prompt | 文本 | |
| Hero Image URL | 超链接 | Leon 上传后填 |
| HTML File Path | 文本 | 本地 HTML 路径 |
| Revision Notes | 文本 | Leon 审阅意见 |
| Created At | 创建时间 | 自动 |
| Campaign | 双向关联 | → Campaign Calendar |

---

## 表 3：Task Queue — `tblWz66HAx8BkseB`

任务看板(注意:与旧设计的"机器任务队列"不同,这是更偏人读的任务板)。17 字段。

| 字段 | 类型 | 选项/说明 |
|------|------|-----------|
| ID | 自动编号 | |
| Task Name | 文本 | 主字段 |
| Owner | 人员 | 负责人 |
| Due Date | 日期 | |
| Priority | 单选 | P1 / P2 / P3 |
| Type | 单选 | Campaign Build / Draft Review / Image Gen / HTML Build / Data Sync / Research |
| Status | 单选 | Todo / In Progress / Done / Blocked |
| Task Context | 文本 | 执行上下文 |
| Target Table | 单选 | Campaign Calendar / Draft Workshop / Performance Dashboard |
| Target Record ID | 文本 | 关联记录 |
| Trigger Message ID | 文本 | 触发消息 ID |
| Created By | 单选 | Aily / Leon / Cron / Claude |
| Created At | 创建时间 | 自动 |
| Started At | 日期 | |
| Completed At | 日期 | |
| Error Message | 文本 | |
| Claude Notes | 文本 | Claude 执行说明 |

---

## 表 4：Topic Pool — `tblhHy3aWxNIJD7D`

话题池。13 字段。

| 字段 | 类型 | 选项/说明 |
|------|------|-----------|
| ID | 自动编号 | 如 NO.002 |
| Topic | 文本 | 主字段,话题角度 |
| Category | 单选 | Educational / Social Proof / Promotional / Lifestyle / Testing |
| Description | 文本 | 角度说明 |
| Product Line | 多选 | A / B / C / E / F / G / H |
| Priority | 数字 | 1-5 |
| Status | 单选 | Available / Scheduled / Used / Archived |
| Last Used | 日期 | 45 天防重复 |
| Source | 单选 | Manual / Google Trends / Reddit / AI Generated / Aily Weekly Discovery |
| Source URL | 文本 | |
| Performance Hint | 文本 | 历史表现提示 |
| Depology DNA | 多选 | Korean Derm Origin / Notox Movement / Tech Innovation / Science Made Simple / Mature Skin Truth / Routine Architecture / Real Results / Brand Manifesto / Sale Mechanics / Lifestyle Moments / Authority |
| Hook Type | 单选 | Curiosity / Contradiction / Authority / Scenario / Numeric / Promise |

---

## 表 5：Promotion Calendar — `tblFUDPYj6pluBfI`

促销日历。12 字段。

| 字段 | 类型 | 选项/说明 |
|------|------|-----------|
| ID | 自动编号 | |
| Event Name | 文本 | 主字段 |
| Start Date | 日期 | |
| End Date | 日期 | |
| Level | 单选 | Big / Middle / Small / None |
| Discount Code | 文本 | |
| Discount Type | 文本 | 如 Sitewide % / Tiered |
| Email Count | 数字 | 该活动邮件封数 |
| Landing URL | 超链接 | |
| VIP Prewarm Date | 日期 | |
| Status | 单选 | Planning / Active / Completed / Upcoming / Optional |
| Notes | 文本 | |

---

## 表 6：Campaign 数据 — `tblKFoefG8yeQovN`

效果数据表(即旧设计的 Performance Dashboard)。11 字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| Campaign Name | 文本 | 主字段 |
| 序号 | 数字 | |
| Send Date | 日期 | |
| Open Rate (%) | 数字 | 直接存百分数值,如 `64.7` 表示 64.7% |
| Click Rate (%) | 数字 | 同上 |
| CTOR (%) | 数字 | 同上 |
| Conv (%) | 数字 | 同上 |
| RPR ($) | 数字 | 美元金额 |
| Revenue ($) | 数字 | 美元金额 |
| Unsub Rate (%) | 数字 | 同上 |
| Key Learning | 文本 | 复盘总结 |

**注意:** 此表无 `Rating`、无 `Klaviyo Campaign ID`、无到 Campaign Calendar 的关联字段。
百分比字段存的是**百分数值本身**(64.7),不是比率(0.647)——回写时不要乘 100。

---

## 与旧设计文档的差异(已知)

| 旧设计(`feishu-edm-os-flows.md` / `feishu-bridge-protocol.md`) | 线上实际 |
|------|------|
| Campaign Calendar 单一 `Subject Line` | 拆成 `Subject Line A` / `Subject Line B` |
| Task Queue 用 `Task Type`(generate_draft 等机器枚举) | 改成人读的 `Type`(Campaign Build 等)+ `Owner` / `Due Date` |
| Task Queue Priority = High/Normal/Low | 改成 `P1/P2/P3` |
| Task Queue Status = ⏳Pending/🔄Processing/✅Done/❌Failed | 改成 `Todo/In Progress/Done/Blocked` |
| Performance Dashboard | 表名为 `Campaign 数据`,字段名带 `(%)` `($)` 后缀 |
| Topic Pool 仅基础字段 | 新增 `Depology DNA` / `Hook Type` / `Performance Hint` / `Source URL` |

> ⚠️ `feishu-edm-os-flows.md` 和 `feishu-bridge-protocol.md` 仍按旧设计写,**尚未校准**——
> 它们引用的字段名/枚举值与线上表已不一致,后续若启用 flow/桥接需先同步。

---

## 脏选项清理记录(2026-05-22 已完成)

| 字段 | 处理 |
|------|------|
| `Campaign Calendar.Email Type` | 删除零使用的遗留选项 `Education`、`Promo` |
| `Topic Pool.Category` | 27 条记录从 emoji 选项迁到纯文字,删除 5 个 emoji 选项,补 `Testing` |
| `Topic Pool.Depology DNA` | 合并重复的 `Authority`(1 条记录迁移),删除重复选项 |

未处理:`Campaign Calendar.Status` 的 `🚀 Ready to Deploy` 与 `🚀 Deployed` 经核对是
两个不同阶段(待部署 / 已部署),非重复,仅 emoji 相同——是否给 `Deployed` 换图标待定。
