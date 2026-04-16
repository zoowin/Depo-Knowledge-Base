# Depology EDM 月度生产流程

> 标准操作流程（SOP），每月初按此执行。
> 最后更新：2026-03-16

---

## 流程总览

| Phase | 负责人 | 做什么 | 产出 |
|-------|--------|--------|------|
| **Phase 0** | Claude | 趋势更新 + 月度选题排期 | 月度 Calendar |
| **Phase 1** | Claude | 批量写邮件草稿 | email-drafts/2026-XX/ |
| **Phase 2** | Leon | 审核草稿，提修改意见 | 批注/反馈 |
| **Phase 3** | Claude | 根据反馈修改定稿 | 定稿 drafts |
| **Phase 4** | Leon | AI 生成 Hero Image | Hero images |
| **Phase 5** | Leon | Klaviyo drag & drop 组装 + Schedule | Klaviyo campaign |
| **Phase 6** | Claude | 更新 campaign-log | 历史记录 |

---

## Phase 0: 趋势更新 + 月度规划（Claude）

### Step 0.1: 趋势更新
每月初，运行 `tools/fetch_trends.py` 更新 topic pool：
```bash
cd tools/
python fetch_trends.py
```
更新结果写入 `strategy/topic-pool.md`，标注抓取日期。

抓取来源：
- Google Trends API — 上升中的关键词
- Google Autocomplete — 搜索联想词
- Reddit — r/SkincareAddiction、r/30PlusSkinCare、r/AsianBeauty 热帖

### Step 0.2: 上月数据回顾
1. 通过 Klaviyo MCP 拉取上月全部 campaign 的 performance 数据
2. 更新 `strategy/campaign-log.md`，补全 Learning 字段
3. 对比 Benchmarks，识别 winners 和 underperformers
4. 总结发现：哪类话题表现好/差，哪个产品线转化高

### Step 0.3: 促销日历检查
1. 读取 `strategy/promotion-calendar.md` → 检查下月是否有活动
2. 确定活动级别（Big/Middle/Small/None）→ 决定促销邮件数量和比例
3. 如有 Middle+ 活动，检查是否需要 VIP list 预热

### Step 0.4: 月度选题
1. 读 `strategy/topic-pool.md` → 结合上月数据筛选话题
2. 读 `strategy/campaign-log.md` → 排除最近 45 天用过的话题、30 天内推过的产品
3. 读 `knowledge/products/` → 确认在售产品（5 条线 10 SKU），均匀分配产品线
4. 根据活动级别调整话题类型比例：
   - 无活动月：教育 2 : 社证 1 : 趋势 1 : 生活方式 1
   - 小促销月：上述 +1-2 封促销
   - 中型活动：5-8 封活动 + 剩余 Evergreen
   - 大促月：60-80% 促销
5. 参考上月表现调整比例
6. 结合季节/节日/热点
7. 输出：`strategy/calendars/2026/2026_XX_Month_Plan.md`

### 防重复规则
- 同一话题角度：45 天内不重复
- 同一主推产品：30 天内不重复
- 同一产品线最多连续出现 2 次
- 不连续发 2 封促销邮件

---

## Phase 1: 批量写稿（Claude）

对月度 Calendar 中的每封邮件：

1. 读对应产品的 SKU 卡（`knowledge/products/`）
2. 对照合规规则（`knowledge/compliance/email-compliance-rules.md`）
3. **严格按 `knowledge/formulas/draft-output-template.md` 格式输出**
4. 保存到 `production/email-drafts/2026-XX/YYYYMMDD_Campaign_Name.md`

### 每封 draft 必须包含：
- Campaign Info（含 Klaviyo 模板指定：VE92sd / R5x7wg）
- 3 条 Subject Line 候选（含带/不带 emoji 版本作为 A/B test）
- Preview Text（40-90 字符）
- Hero Section（Headline ≤9词 + Subheadline 2行 + CTA）
- Body Section（Headline ≤5词 + 3 段正文共~376字符 + Goals 列表）
- Product Section（2-3 个产品卡片，每个描述~120字符）
- Closing Section（如使用 VE92sd 模板）
- Hero Image Brief + AI Prompt（用于 ChatGPT/Midjourney）

### 质量自检：
- [ ] 无违禁词（对照合规规则第 2 章）
- [ ] 产品描述来自 SKU 卡，未编造
- [ ] 临床数据有来源标注（对照第 6 章）
- [ ] 字数符合 draft-output-template 限制
- [ ] 指定了 Klaviyo 模板（VE92sd / R5x7wg）
- [ ] Alex Principle：新概念有 "What it is" + "Why it matters"

---

## Phase 2: 审稿（Leon）

Leon 逐封审核 draft，关注：
- 话题角度是否准确
- 文案语感是否自然
- 产品搭配是否合理
- Subject Line 是否有吸引力

反馈方式：直接在对话中告诉 Claude 修改意见。

---

## Phase 3: 修改定稿（Claude）

根据 Leon 的反馈修改草稿，直到通过审核。
定稿后在文件顶部标注 `✅ APPROVED` + 审核日期。

---

## Phase 4: Hero Image 生成（Leon）

1. 从 draft 底部的 **Hero Image Brief** 中复制 AI Prompt
2. 在 ChatGPT / Midjourney 中生成 Hero Image
3. 下载图片（600 x 400px，PNG，≤300KB）
4. 保存到 `production/assets/images/YYYYMMDD/`（可选）

---

## Phase 5: HTML 构建 + Klaviyo 部署（Claude + Leon）

### Claude 自动完成：
1. 选择基础模板（白底教育型 → 0408，黑底促销型 → 0403）
2. 基于模板生成完整 HTML（替换文案/图片/链接/CTA）
3. 本地保存 HTML → `production/html-output/YYYYMMDD_Campaign_Name.html`
4. 通过 Klaviyo API 执行：
   - 创建 Email Template（纯 HTML）
   - 创建 Campaign（命名 `[DEP]_YYYYMMDD_Campaign_Name`）
   - 设置发件人（`support@depology.com` / `Dēpology`）
   - 设置人群（标准 4 included + 9 excluded，见 Klaviyo Campaign 标准设置）
   - 绑定模板到 Campaign
   - Schedule 发送时间（默认 9:00 AM ET）

### Leon 确认：
1. 在 Klaviyo 后台预览邮件（桌面 + 移动端）
2. 确认 Hero Image 正确显示
3. 确认发送时间 → Schedule 或 Send

---

## Phase 6: 发送后记录（Claude）

发送完成后，Claude 更新 `strategy/campaign-log.md`：
- 发送日期
- Campaign 名称
- 话题角度
- 主推产品
- 使用的模板（VE92sd / R5x7wg）
- 关键数据（打开率、点击率 — 待 Leon 提供）
- 经验备注

---

## 文件命名规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 邮件草稿 | `YYYYMMDD_Campaign_Topic.md` | `20260401_Spring_Peptide_Education.md` |
| 博客草稿 | `YYYYMMDD_Blog_Topic.md` | `20260415_Blog_Retinol_Guide.md` |
| SMS 草稿 | `YYYYMMDD_SMS_Topic.md` | `20260401_SMS_Spring_Sale.md` |
| Hero Image | `YYYYMMDD_hero_topic.png` | `20260401_hero_peptide_education.png` |

---

## 在售产品速查（7 条线 14 SKU）

| 线 | 产品 |
|----|------|
| **A** Matrixyl® | Collagen Serum, Matriplex Cream |
| **B** Argireline™ | MPS Serum, Micro-dart Patch, Eye Cream, Night Under Eye Patch |
| **C** Retinoid | Body Lotion |
| **E** Technology | Micro-needling Cream |
| **F** Opuntia | Cleansing Balm |
| **G** Serum Stick | Bakuchiol Smoothing Stick, Caviar Multi-Balm Stick |
| **H** Barrier Repair | Triple Lipid + Q10 Moisturizing Treatment RICH |

**已停产：** D 线 Cica 全线、A 线 Dream Mask、B 线 Eye Stick、C 线 Anti-Aging Retinol Night Cream

---

## 关键参考文件

| 文件 | 用途 |
|------|------|
| `CLAUDE.md` | AI 总入口，品牌规则，模板体系 |
| `knowledge/formulas/draft-output-template.md` | 邮件草稿标准格式 + 字数限制 |
| `knowledge/compliance/email-compliance-rules.md` | 合规规则（9 章） |
| `knowledge/formulas/copy-winning-formula.md` | MEL 文案结构 |
| `knowledge/formulas/topic-winning-formula.md` | 话题角度公式 |
| `knowledge/visual/MEL Style.md` | MEL 视觉风格指南 + 12 个案例分析 |
| `strategy/topic-pool.md` | 话题池（手动 + 自动抓取） |
| `strategy/campaign-log.md` | 历史发送记录（防重复） |

---

## Klaviyo 模板体系

### 基础模板（本地 HTML 文件）

| 文件 | 类型 | 布局 | 配色 |
|------|------|------|------|
| `20260408_Hydration_Hierarchy.html` | 教育型 | 双 hero + checklist + 角色标签 + 3 产品卡 | 白底黑字 |
| `20260403_Easter_Sale_Opening.html` | 促销型 | hero + 促销文案 + 3 产品卡 | 黑底白字 |
| `R5x7wg_base_template.html` | 通用促销（旧） | 单 hero + body + checklist + 3 产品卡 | 黑底白字 |
| `VE92sd_base_template.html` | 教育型（旧） | 单 hero + 产品角色标签 + 底部总 CTA | 黑底白字 |

**推荐做法：** 以已验证的 production HTML（0408/0403）为基础构建新邮件。旧的 drag-and-drop 模板（R5x7wg/VE92sd）仅作归档参考。

### 模板选择规则

| 邮件类型 | 基础模板 |
|---------|---------|
| 教育 / Evergreen / 主题型 | `20260408_Hydration_Hierarchy.html`（白底） |
| 促销 / Sale | `20260403_Easter_Sale_Opening.html`（黑底） |

### 模板内容结构

```
[固定] Header 图片（所有邮件统一）
  URL: https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a91ce3e7-44ab-42dc-a9e6-c3dc74b6f3bf.jpeg

[每次替换] Hero Image（600 × 400px）
[每次替换] Hero 标题 + 副标题 + CTA
[每次替换] 正文区域（2-4段）
[每次替换] 产品推荐标题
[每次替换] 产品卡片 ×3（左文右图，67%/33%）
[每次替换] Closing CTA
[固定] Footer（黑底 logo + social icons + unsubscribe）
```

---

## Klaviyo Campaign 标准设置

### 发件人信息
| 字段 | 值 |
|------|-----|
| **From Email** | `support@depology.com` |
| **From Name** | `Dēpology` |

### Campaign 命名规范
格式：`[DEP]_YYYYMMDD_Campaign_Name`
示例：`[DEP]_20260422_Earth_Day`

### 标准发送人群（Included）
| Segment | ID |
|---------|-----|
| [DEP] - Signed up 30 days **DO NOT TOUCH** | `QPetUg` |
| Leon - Engaged Profiles (120 Days) | `X9GvQv` |
| Reviewed 3 Times | `XQqrAQ` |
| Repeat Buyers | `YbRy3S` |

### 标准排除人群（Excluded）
| Segment | ID |
|---------|-----|
| NLE - [EXCLUDE] Spam | `RNUDwR` |
| Exclude (In Flow) | `RsM7QF` |
| NLE - [EXCLUDE] Clean List - Bounced Email > 6 | `TCpjZJ` |
| NLE - [SUPPRESS] Unengaged Profiles | `TWCwGW` |
| NLE - [EXCLUDE] Spam Traps | `U9crDJ` |
| NLE - [EXCLUDE] Received 10+ Emails No Opens | `UzTR6W` |
| NLE - [EXCLUDE] Spam Trap Role Accounts | `VFjbHB` |
| [EXCLUDE] TIKTOK EMAILS | `XVbFC5` |
| NLE - Suppress True | `XWFhWE` |

### 其他设置
- **Smart Sending**: 开启
- **Tracking**: Clicks + Opens 均开启
