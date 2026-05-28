# SMS Campaign: Memorial Sale Launch + MEM10 First-48hrs Window

**Campaign:** Memorial Sale Launch
**Send Date:** 2026-05-20 (Wednesday)
**Send Time:** 10:00 AM 本地时间（isLocal: true，紧跟 9 AM 邮件后 1 小时）
**Goal:** Day 1 拉满早鸟流量 — 启动 sale awareness + 激活 MEM10 第一波 48 小时窗口
**Target Audience:** All SMS Subscribers (US)
**Tone:** 直接、热闹、节日感 — Memorial Launch 是 5 月最高单日 revenue moment
**Klaviyo Campaign Name:** `[DEP]_SMS_20260520_Memorial_Launch_MEM10`

---

## Strategy

3 条 SMS 精简方案的第 1 条。Memorial Launch day 邮件 9 AM 已发，SMS 10 AM 触发，吃掉没第一时间打开邮件的 SMS-only 受众。

核心信息：
1. **The Event:** Memorial Sale is LIVE
2. **The Offer:** Up to 50% off sitewide + extra 10% with MEM10
3. **The Time:** MEM10 仅头 48 小时（5/20 → 5/21 11:59 PM）
4. **The Action:** Click to shop

MEM10 是头 48 小时 exclusive，SMS 是这个窗口的核心激活渠道（邮件主推 50% sitewide，SMS 把 stack discount 推出来制造"现在最划算"的钩子）。

---

## SMS Copy

### Recommended
> Depology: Memorial Day Sale LIVE 🎉 Up to 50% off + extra 10% w/ MEM10 (auto-applied) — first 48 hrs only. https://depology.com/discount/MEM10?redirect=/pages/memorialday-sale-2026

### Alternative — 更简短
> Depology: Memorial Day Sale LIVE 🎉 Up to 50% off + extra 10% w/ MEM10 — first 48 hrs. https://depology.com/discount/MEM10?redirect=/pages/memorialday-sale-2026

> **URL 说明：** 用 Shopify discount link 格式 `/discount/MEM10?redirect=/pages/memorialday-sale-2026` — 用户点链接进入会自动 apply MEM10 到 cart，无需手动输入折扣码；Klaviyo `shortenLinks: true` 会把长链压成 `k.in/xxxxx` 短链，实际 SMS 字符数约 ~140 chars 单条段
> **Emoji 说明：** 原 🇺🇸 已替换为 🎉 — Active Subscribers segment 包含加拿大订阅者（49,491 人量级里有 Canada 部分），用中性 emoji 避免国旗与地理不符；庆祝感保留

---

## 备注

- ⚠️ **Smart Sending OFF**（确保 SMS 触达，不被频率限制屏蔽）
- 🔗 **短链：** `depology.com/MemDay` redirect → `/pages/memorialday-sale-2026`（Leon 在 Shopify 后台配置）；如未配置，文案里替换为完整 URL `https://depology.com/pages/memorialday-sale-2026`
- 📊 SMS 平均 CTR 15-25%，Memorial Launch 预期增量 revenue **$1,500 - $3,000**
- 🚨 5/20 是 3 触点天（9 AM email + 10 AM SMS + 5 PM email），SMS 排除已在 PM email segment 的用户（避免叠加疲劳）
- ✉️ MMS 可选：上传 Memorial UP TO 50% 主视觉一图，提升点击率
- 🕐 isLocal: true（按收件人本地时区发送）
