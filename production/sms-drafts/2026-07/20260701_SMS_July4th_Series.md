# July 4th Sale — SMS Series（2026）

> 3 条 SMS，配合 email 序列关键节点。per `strategy/campaign-log.md`「7/4 必须重点用 SMS」（Memorial SMS CR 16%、ROI 之王）。
> 每条含品牌名 + STOP opt-out（CAN-SPAM/TCPA）。`[link]` = Shopify discount link（`/discount/JULY4TH10?redirect=/pages/july4th-sale-2026`，部署时换短链）。

---

## SMS 1 — 7/1 Tue ~11:00 AM ET（Launch alert，夹在 email 之后）
**Klaviyo Name:** `[DEP]_SMS_20260701_July4th_Launch`
**人群:** SMS-subscribed（标准营销 SMS list）

> Dēpology: Our July 4th Sale is LIVE 🎆 40% off sitewide + an extra 10% with code JULY4TH10. Best-sellers now 3-for-2. Shop: [link]
> Reply STOP to opt out

字符参考：~155（单条 SMS 上限内）。

---

## SMS 2 — 7/4 Fri ~11:00 AM ET（正日 peak）
**Klaviyo Name:** `[DEP]_SMS_20260704_July4th_PeakDay`
**人群:** SMS-subscribed

> Dēpology: Happy 4th! 🎆 The sale peaks TODAY — micro-dart eye patches up to 45% off, plus 40% sitewide. Add JULY4TH10 for 10% more: [link]
> STOP to opt out

字符参考：~160。

---

## SMS 3 — 7/7 Mon ~4:00 PM ET（Last chance，倒计时）
**Klaviyo Name:** `[DEP]_SMS_20260707_July4th_LastChance`
**人群:** SMS-subscribed（可优先未购）

> Dēpology: Last call ⏳ The July 4th Sale ends TONIGHT. 40% off + extra 10% (JULY4TH10), micro-darts up to 45% off: [link]
> STOP to opt out

字符参考：~150。

---

## 备注
- 全部走 SMS-subscribed 营销人群；勿发非 SMS 同意用户。
- `[link]` 部署时用 Klaviyo 短链或 Shopify discount 短链；确认落地 `/pages/july4th-sale-2026`。
- 时段避开过早/过晚（TCPA 8am–9pm 本地时区）；Klaviyo Smart Sending/quiet hours 开启。
