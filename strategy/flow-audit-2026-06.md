# Klaviyo Flow 全面梳理与优化 — 2026-06-25

> 本次对账户全部 flow（100+，live ~30）做了全盘诊断。本文件 = 已做动作 + 待跟进总账。

## 账户概况
- live flow ~30 个，其余 ~70 为 2022–2023 历史草稿（噪音，待清）。
- 过去 12 个月 live flow 总营收 ≈ $32.6 万，高度集中在头部 6 条（Abandoned Checkout 占 ~1/3）。

## ✅ 已完成动作

| 日期 | Flow | 动作 | 理由 |
|------|------|------|------|
| 06-25 | `SAwiYB` Fulfilled-Order Post Purchase | 暂停（→draft） | 与 SCZyhi 人群重合、互不排除 → 重复轰炸（退订/投诉最高） |
| 06-25 | `SCZyhi` 新客分支 Hype Email | 关闭 | 90 天 0 转化、纯 hype 不合品牌 |
| 06-25 | `Y9uwrR` [CAYLA] Abandoned Cart | 删除 2 条 Omni 死条件（Initiate Checkout / Purchase Completed） | Omni OS 集成已死（事件近 30 天 0 次），却作 AND 进入门槛 → 整条流空转，近 30 天 0 触达，每月漏 ~2,700 加购用户、约 $1.5–2k |
| 06-25 | `UxuE3f` Review Request [TURNED OFF] | 归档 | 近 90 天 0 发送的僵尸；数据证实 Judge.me eligible 事件 ≈ 履约订单（已全覆盖），无缺口可补，纯冗余。评价流现仅 `WPM2fk` Judge.me 一条 |

## ⏳ 待跟进

- [x] ~~5 条主力 flow 合规复核~~：已完成 → `strategy/flow-compliance-review-2026-06.md`（弃结账/弃购/弃浏/Winback/Welcome，约 50 封）。整改待办见下。
- [ ] **P0 整改**：折扣链接格式批量修（掉钱项）；弃结账 #4 停产产品；弃浏 `regenerate`；弃结账 #2 `injectables` 评价；临床数据补脚注。
- [ ] 弃结账 `YmrJTu` + 弃浏 `TtcziZ`（均高风险旧 flow）纳入 MEL 重做。
- [~] **M2（原 M1）Winback `RRSpCh`（0 触发已修，待观察发送）**：
  - 根因：trigger 商品名是片段 `Micro Dart`/`Micro-Dart` → Klaviyo `Items contains` 对 List 是**整名匹配（非子串）**，匹配不到任何订单 → 0 触发。已改为从下拉选**完整 SKU 名**并保存。
  - 产品 Q2 已改名为 "…Micro-Dart…"（连字符）；`XBJHNj` Replenishment 仍用旧名 "…Micro Dart…"（空格），**待同步更新否则漏新订单**。
  - 动态码 `M1TEN`/`M1FS`（`{% coupon_code %}`）已实测：回填用户可正常生成（如 `M1TEN-BWH6VN36`）。
  - **存量召回纠正**：metric flow 不会自动回溯历史订单，但 Klaviyo **"Add past profiles" 可手动回填**——已回填 ~700 名历史首购者（341+360 在 Day60 邮件 waiting）。（之前"必须用 segment+campaign"的说法不准确。）
  - 待办：观察 48h，Day60 邮件 Delivered 是否从 waiting 启动；2026-06-29 时近 7 天仅 1 封 delivered（测试邮件）。
- [ ] **Cart `Y9uwrR` 折扣码确认**：#3A/#4A「10% off」需确认是 Klaviyo 动态券（永久有效）而非硬编码过期码。
- [ ] **Cart `Y9uwrR` 序列长度**：6 封 / ~8 天偏长，可评估精简到 3–4 封。
- [x] ~~P0-2 评价流 `UxuE3f`~~：已归档（确认为僵尸，Judge.me 已全覆盖）。
- [ ] **P2 清理**：~70 个历史草稿（BFCM、Gatsby、quiz、停产 SKU back-in-stock、clone）批量归档。
- [ ] **Post-Purchase 重做**：见 [todo-post-purchase-rebuild.md](todo-post-purchase-rebuild.md)。

## ✅ 确认健康、无需动的核心 flow
- `YmrJTu` Abandoned Checkout（现金牛，$108k/12mo）
- `TtcziZ` Browse Abandonment
- `SCZyhi` Post Purchase（精简后，新老客各保留感谢/确认首封）
- `WPM2fk` Review Request | Judge.me（标准评价流）
