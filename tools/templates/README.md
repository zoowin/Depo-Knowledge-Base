# Email Base Templates

> 所有新邮件从这里选基础模板。每个 campaign 复制一份模板 → Python 替换内容 → 输出到 `production/html-output/YYYY-MM/`。
> 最后更新：2026-06-10

## 模板三代体系

| 代际 | 文件 | 类型 | 结构 | 行数 | 状态 |
|------|------|------|------|------|------|
| **3（主力）** | `base_block_education_cards_0624.html` | 白底教育 + 编号产品卡 | 手写 BLOCK（单 600px container） | ~200 | ✅ 新教育/evergreen 邮件首选 |
| **3（主力）** | `base_block_promo_sale_0520.html` | 促销/Sale（Memorial 风格） | 手写 BLOCK | ~200 | ✅ 新促销邮件首选 |
| 2 | `base_education_white_0408.html` | 白底教育（MJML 结构） | 双 hero + checklist + 3 产品卡 | ~750 | 可用（生日周 0614/0620/0622 基于它） |
| 2 | `base_promo_black_0403.html` | 黑底促销（MJML 结构） | 单 hero + checklist + 产品卡 | ~750 | 可用 |
| 1 | `R5x7wg_base_template.html` | 通用促销（Klaviyo 拖拽导出） | desktop/mobile 双版本冗余 | 1600+ | ⚠️ 遗留，不推荐 |
| 1 | `VE92sd_base_template.html` | 教育型（Klaviyo 拖拽导出） | 同上 | 1600+ | ⚠️ 遗留，不推荐 |

## 第 3 代 BLOCK 结构说明（当前主力）

- 每个区块是独立的 `<table class="container" width="600">`，注释标记 `<!-- BLOCK N: XXX -->`
- **编号产品卡**：横排卡片（左图 140px + 右文），眉头 `01 &mdash; Role Name` 灰色小字 + 产品名 + 描述 + SHOP 按钮
- 代表作：0612 / 0616 / 0624 / 0626 / 0630；Memorial 全系列（0520-0528）为促销变体
- 区块增删直接按 BLOCK 注释切割，比第 2 代 MJML 嵌套好改

## 命名规则

`base_<结构>_<类型>_<来源日期>.html` — 来源日期 = 该模板源自哪封已验证的 production 邮件。
模板内容与 `production/html-output/` 中的源文件一致；源文件是已发送 campaign 的存档，**改模板时只改这里的副本，不动源文件**。

## 其他

- `partials/` — 头部/footer 公共片段（`_head_block` / `_footer_block` / `_footer_ref`），供 render 脚本拼装用
- `archive/` — 已弃用的早期模板（mel_master / MEL / NLE），仅留档

## 使用

```bash
# 通用构建（JSON 替换表）
python tools/build_campaign_html.py replacements.json \
  --base base_block_education_cards_0624 \
  --output 2026-07/20260701_Campaign.html --preview

# 复杂改造（删区块/换布局）：写专用 build 脚本，参考 tools/build_0620_birthday_gift.py
```
