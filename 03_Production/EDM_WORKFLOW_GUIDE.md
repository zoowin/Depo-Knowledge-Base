# Depology EDM 全系统自动化工作流

> 最后更新：2026-03-05
> 工具栈：Claude (Cowork) · Klaviyo MCP · fetch_trends.py · Figma MCP

---

## 系统概览

```
后台工具               知识库                  实时数据
fetch_trends.py  →  Topic Pool         ←  Klaviyo MCP（历史表现）
                    Product Library    ←  库存系统（待接入）
                    Winning Formula
                    Brand Guidelines
                    Campaign Log
                         ↓
              [阶段 0] Claude 生成月度日历
                         ↓
              [阶段 1] Claude 生成单封邮件内容
                         ↓
              [阶段 2] 本地 HTML 制作 + Leon 预览（≈ 0 tokens）
                         ↓（仅通过审核后）
              [阶段 3] Klaviyo 上传（~12K tokens · 唯一不可压缩）
                         ↓
              [阶段 4] Leon 在 Klaviyo 后台发送
```

**Leon 只需参与 2 个环节：**
1. 审核月度日历（可选，Claude 也可直接推进）
2. 本地预览 HTML → 反馈修改意见 → 确认上传
3. Klaviyo 后台点击发送

---

## 后台工具｜自动趋势抓取

**文件：** `04_Tools/fetch_trends.py`
**触发：** 手动或定期运行
**输出：** 自动追加新趋势到 `Topic_Pool.md`

抓取来源：
- **Google Trends API** — 上升中的关键词查询
- **Google Autocomplete** — 搜索联想词（skincare / retinol / peptide serum 等）
- **Reddit** — r/SkincareAddiction、r/30PlusSkinCare、r/AsianBeauty 本周热帖

运行方式：
```bash
cd /path/to/Depo-Knowledge-Base/04_Tools
python fetch_trends.py
```

---

## 本地知识库｜Claude 的决策基础

所有文件均在本地，Claude 读取时 **0 API token 消耗**。

| 文件 | 路径 | 用途 |
|------|------|------|
| **Brand Guidelines** | `02_Knowledge_Base/Brand_Assets/Winning_Formula/Brand Guidelines.md` | 品牌调性、语气、禁忌词 |
| **Product Library** | `02_Knowledge_Base/Products/` | 6条产品线、SKU卡、成分、卖点 |
| **Winning Formula** | `02_Knowledge_Base/Brand_Assets/Winning_Formula/copy winning formula.md` | 邮件结构公式（Hero→Body→Product→Close） |
| **Topic Winning Formula** | `02_Knowledge_Base/Brand_Assets/Winning_Formula/topic winning formula.md` | 高效话题的构成规律 |
| **Topic Pool** | `01_Strategy_and_Planning/Topic_Pool.md` | 话题库（手动 + 自动抓取趋势） |
| **Campaign Log** | `01_Strategy_and_Planning/Campaign_Log.md` | 历史发送记录（防重复） |
| **Email Strategy** | `01_Strategy_and_Planning/Email Strategy.md` | 整体策略方向 |

---

## 实时数据接入

| 数据源 | 状态 | 接入方式 | Claude 用途 |
|--------|------|---------|------------|
| **Klaviyo 历史表现** | ✅ 已接通 | Klaviyo MCP | 识别高开信率主题类型、最佳发送时间、受众表现 |
| **库存数据** | ⏳ 待接入 | Shopify API / 手动告知 | 过滤缺货产品，避免推广无库存 SKU |

Klaviyo 可查询指标：`open_rate` · `click_rate` · `conversion_rate` · `revenue_per_recipient`

---

## 阶段 0｜月度营销日历（Claude 全自动）

**Token 消耗：** ~3–5K（对话 + 决策，视月份邮件数量而定）
**输出：** `01_Strategy_and_Planning/Calendars/2026 EDM Calendar/2026_XX_Month_Plan.md`

### Claude 的决策逻辑

```
① 读取 Topic Pool → 筛选未使用 / 表现好的话题
② 查 Campaign Log → 排除近 45 天内已用主题 + 近 30 天已推产品
③ 读 Klaviyo 历史 → 优先选同类型历史高开信率话题
④ 读 Product Library → 确认产品在库（跨线分布，避免同线连续推）
⑤ 结合节日 / 季节节点排期（如 Spring Equinox、Mother's Day）
⑥ 按话题类型配比：教育 2 : 社证 1 : 促销 1 : 生活方式 1（每5封为一周期）
⑦ 输出完整月度日历草稿
```

### 防重复规则

- **主题**：同一话题角度 45 天内不重复
- **产品**：同一产品 30 天内不连续作为主推
- **类型**：连续 2 封不能同为促销类
- **记录更新**：每次 Klaviyo 上传后自动写入 Campaign Log

### 月度日历格式

```markdown
| 日期 | 邮件类型 | 主题 | 主推产品 | 受众 | 预期策略 |
|------|---------|------|---------|------|---------|
| 03/20 | 季节节点 | Spring Equinox: Transitioning Routine | Triple Lipid, Bakuchiol, Caviar Stick | All − Unsubscribed | 教育型 → 轻推3品 |
```

---

## 阶段 1｜单封邮件内容生成（Claude 全自动）

**Token 消耗：** ~2–4K（依内容复杂度）
**输出：** `03_Production/01_Email_Drafts/[Month]/YYYYMMDD_Campaign_Name.md`

### 按 Winning Formula 生成的内容块

```
Hero Section (TB1)
├── Headline      ≤9词，单一信号：结果 / 真相 / 场景
├── Subheadline   承接Hero，引导继续读
└── Hero CTA      非购买型（Explore / Learn / Discover）

Body Section (TB2)
├── Body Headline  ≤8词，被忽视的事实 / 场景矛盾
├── Body Copy      问题 → 原因 → 可执行行为（2–4句）
└── Body CTA       与Hero CTA不同

Product Title (TB3)
└── 产品区标题 + 副标签

Product Cards (HB1/2/3)
├── 产品标签（01 — The Hydration Anchor）
├── 产品名
├── 描述（结果导向，不堆成分名）
└── Shop CTA（SHOP [PRODUCT NAME]）

Meta
├── Subject Line    多个候选（含emoji和无emoji版）
└── Preview Text    40–90字符，承接Subject不重复
```

### Hero Image

当前流程：Leon 提供 Shopify CDN URL → Claude 注入 `<img src="">` 占位符
未来目标：AI 图像生成（基于邮件主题自动生成 + 上传至 CDN）

---

## 阶段 2｜本地制作与预览（≈ 0 tokens）

**谁做：** Claude 生成，Leon 在浏览器审核
**Token 消耗：** 本地 Python 执行，约 0 tokens
**文件位置：** `03_Production/05_HTML_Drafts/[Month]/`

### 工作原理

```python
# base_template_R5x7wg.html（本地缓存，0 tokens读取）
html = html.replace(TEXT_PLACEHOLDER, TB1, 1)   # Hero section
html = html.replace(TEXT_PLACEHOLDER, TB2, 1)   # Body copy
html = html.replace(TEXT_PLACEHOLDER, TB3, 1)   # Product title
html = html.replace(HTML_PLACEHOLDER, HB1, 1)   # Product card 1
html = html.replace(HTML_PLACEHOLDER, HB2, 1)   # Product card 2
html = html.replace(HTML_PLACEHOLDER, HB3, 1)   # Product card 3
```

### 本地预览注意事项

| 差异点 | 说明 |
|--------|------|
| Liquid 变量 | 显示原始代码 `{{ person.first_name }}`，实际发送时替换 |
| 追踪像素 | 预览不触发，不影响设计审核 |
| 自定义字体 | 若浏览器未加载，会降级为 Arial/系统字体 |
| 整体还原度 | 约 85–90%，设计判断完全可靠 |

### 审核 → 修改 → 重新生成（全在本地，0 tokens）

设计调整可告知 Claude：
- 字体大小 / 字重 / 颜色
- 模块间距 / 内边距
- 产品图尺寸 / 列宽比例
- 文案微调

**只有 Leon 本地确认后，才进入阶段 3 上传 Klaviyo。**

---

## 阶段 3｜Klaviyo 上传（~12K tokens · 唯一不可压缩）

**谁做：** Claude 自动调用 Klaviyo MCP
**Token 消耗：** ~12K tokens（HTML 内容本身决定，无法进一步压缩）

```
Step 1: create_email_template    上传 HTML body → 获得 Template ID    ~9K tokens
Step 2: create_campaign          设置 subject / preview / from         ~2K tokens
                                  受众 include/exclude / 发送时间
Step 3: assign_template          Template ID → Campaign Message         ~1K tokens
Step 4: 更新 Campaign Log        写入主题 · 产品 · 日期（防重复）
```

### 标准受众配置（March 2026）

| 类型 | Segment / List ID |
|------|------------------|
| Include | QPetUg · X9GvQv · XQqrAQ · YbRy3S |
| Exclude | RNUDwR · RsM7QF · TCpjZJ · TWCwGW · U9crDJ · UzTR6W · XVbFC5 · XWFhWE |

---

## 阶段 4｜发送（Leon · 0 tokens）

1. 登录 [Klaviyo 后台](https://www.klaviyo.com)
2. 找到 Draft 状态的 Campaign
3. 确认 Subject / Preview Text / 发送时间
4. 点击 **Schedule** 或 **Send Now**

---

## Token 消耗全景

| 阶段 | 操作 | Token | 可优化？ |
|------|------|-------|---------|
| 趋势抓取 | fetch_trends.py 本地运行 | **0** | ✅ 已优化 |
| 知识库读取 | 本地文件，不经 API | **0** | ✅ 已优化 |
| 月度日历生成 | Claude 决策对话 | ~3–5K | 减少来回 |
| 邮件内容生成 | Claude 文案生成 | ~2–4K | 减少来回 |
| HTML 本地生成 | Python 脚本 | **0** | ✅ 已优化 |
| 设计迭代（每轮） | 本地修改重新生成 | **0** | ✅ 已优化 |
| Klaviyo 上传 | HTML 传输 | **~9K** | ❌ 不可压缩 |
| Campaign 创建 | API 调用 | ~2K | — |
| Template 绑定 | API 调用 | ~1K | — |
| **单次 campaign 合计** | | **~17–21K** | |

> **关键优化：** 将所有设计迭代限定在"本地预览"阶段，避免多次上传 Klaviyo。
> 每次额外上传 = 额外 ~12K tokens。目标：每个 campaign **只上传一次**。

---

## 系统状态总览

| 模块 | 状态 | 备注 |
|------|------|------|
| Brand Guidelines | ✅ 已建立 | `02_Knowledge_Base/Brand_Assets/` |
| Product Library | ✅ 已建立 | 6条产品线，SKU Cards |
| Winning Formula | ✅ 已建立 | Copy + Topic 两套公式 |
| Topic Pool | ✅ 已建立 + 自动更新 | `fetch_trends.py` 定期追加 |
| Campaign Log | ✅ 已建立 | 需确保每次发送后更新 |
| Klaviyo MCP | ✅ 已接通 | 历史表现数据可查 |
| 库存数据接入 | ⏳ 待接入 | 目前手动确认库存 |
| Hero Image 自动化 | ⏳ 待接入 | 目前提供 CDN URL |
| 月度日历自动生成 | ✅ 可执行 | 知识库 + MCP 已就绪 |

---

## 已创建 Campaign 记录

| 日期 | Campaign 名称 | Campaign ID | Template ID | 状态 |
|------|--------------|------------|------------|------|
| 2026-03-04 | Spring Equinox: Transitioning Routine | `01KJW1CKJ2395EKQH0XFA5A97G` | `XQpR5S` | Draft |

---

*本文档由 Claude 自动维护。每次 campaign 完成后更新 Campaign 记录表。*
