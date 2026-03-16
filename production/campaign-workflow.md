# Depology Email Campaign Workflow
_Last updated: 2026-03-04_

---

## Base Template

| 字段 | 值 |
|---|---|
| Template ID | `R5x7wg` |
| Template Name | Mel style |
| Editor Type | SYSTEM_DRAGGABLE（原生拖拽） |
| Klaviyo URL | https://www.klaviyo.com/email-template-editor/R5x7wg |

---

## 模板内容地图

```
Section 1 — 白色背景 (600px)
│
├── [固定] Header-Template 图片
│     URL: https://d3k81ch9hvuctc.cloudfront.net/company/XbHdQN/images/a91ce3e7-44ab-42dc-a9e6-c3dc74b6f3bf.jpeg
│
├── [用户填] Hero Image 占位块
│     ← 每次 campaign 唯一需要手动操作的地方
│     推荐尺寸: 600 × 400px
│
├── [Text Block 1 — 黑色背景]
│     内容: Hero 标题 + 副标题 + CTA 按钮
│     风格: 居中，大标题，简洁有力
│
├── [Text Block 2 — 黑色背景]
│     内容: 正文区域（2~4 段，讲品牌故事/成分/卖点）
│
├── [Text Block 3 — 黑色背景]
│     内容: 产品推荐区域标题（如 "Your Notox Toolkit"）
│
├── [HTML Block 1] → 产品卡片 1
├── [HTML Block 2] → 产品卡片 2
└── [HTML Block 3] → 产品卡片 3

Section 2 — 黑色背景（固定，不可编辑）
└── Depology logo + FB/IG/TikTok/Pinterest/YouTube + 版权 + Unsubscribe
```

---

## 字体 & 设计规范（从模板提取）

| 元素 | 字体 | 大小 |
|---|---|---|
| H1 | Century Gothic / AppleGothic / Arial | 40px (移动端 28px) |
| H2 | Century Gothic / AppleGothic / Arial | 30px (移动端 20px) |
| H3 | futura-pt / Century Gothic | 26px (移动端 22px) |
| 正文 | Century Gothic / AppleGothic / Arial | 18px |
| 背景色（主体） | `#DDDDDD` | — |
| 文字块背景 | `#000000` | — |
| 文字颜色 | `#FFFFFF` | — |

---

## Campaign 标准受众

| 受众 | List ID |
|---|---|
| 活跃订阅者 | `TFdHSN` |

---

## 每次 Campaign 执行清单

### Claude 完成（全自动）
- [ ] 确定主题角度、产品选择、叙事结构
- [ ] 撰写 Text Block 1：Hero 标题 + 副标题 + CTA 文案
- [ ] 撰写 Text Block 2：正文（品牌故事/成分/卖点）
- [ ] 撰写 Text Block 3：产品推荐区标题
- [ ] 生成 3 个产品 HTML 卡片（产品图、名称、简介、按钮、链接）
- [ ] 创建 Klaviyo Campaign Draft（subject、preview text、受众 TFdHSN）
- [ ] 生成本次专用模板（基于 R5x7wg 填入内容）并挂载到 campaign
- [ ] 输出 Hero Image 创作 brief（尺寸、风格、Midjourney prompt）

### 你完成（约 5 分钟）
- [ ] 根据 brief 生成 / 选取 hero image（600×400px）
- [ ] 上传到 Klaviyo → 填入 Hero Image 占位块
- [ ] 快速审阅内容
- [ ] 设置发送时间 → 确认发出

---

## 历史 Campaign 记录

| 日期 | Campaign 名称 | Campaign ID | 模板 ID | 状态 |
|---|---|---|---|---|
| 2026-03-04 | The 'Notox' Movement | `01KJVD15J74KHVRDJ4D7QR31TH` | `R5x7wg`（待用） | Draft |
| 2026-03-04 | Spring Equinox: Transitioning Routine | `01KJW1CKJ2395EKQH0XFA5A97G` | `XQpR5S` | Draft |

---

## 产品资源库（常用）

| 产品 | 链接 |
|---|---|
| Deepcare+® MicroOperator Boosting Cream | https://depology.com/products/deepcare-r-microoperator-boosting-cream-beginner |
| Argireline™ Eye Cream | https://depology.com/products/peptide-complex-wrinkle-defense-eye-cream |
| Deepcare+ Micro-Dart Patches | https://depology.com/products/deepcare-serum-infused-micro-dart-patches-lp1-t0 |
