# Feishu EDM Bridge Group — 消息协议规范

> Aily 监听桥接群（`Depology EDM Bridge`）的消息来感知飞书 bitable 变更。
> 飞书 bitable 自动化在字段变更时，按这套规范发送消息。Aily 解析后写入 Task Queue。

---

> ⚠️ **schema 校准说明(2026-05-22)** —— 本文档按早期"机器任务队列"设计,但线上
> Task Queue 表已被重设计为**人读任务板**,字段与枚举全部变了。**以 `feishu-edm-os-setup.md` 为准。**
>
> | 本文档写的 | 线上实际(Task Queue `tblWz66HAx8BkseB`) |
> |-----------|---------|
> | `Task Type`(generate_draft / build_html …) | `Type`:Campaign Build / Draft Review / Image Gen / HTML Build / Data Sync / Research |
> | `Status` ⏳Pending / 🔄Processing / ✅Done / ❌Failed | `Todo / In Progress / Done / Blocked` |
> | `Priority` High / Normal / Low | `P1 / P2 / P3` |
> | `Task ID`(时间戳格式主字段) | 主字段是 `Task Name`(文本),另有自动 `ID` |
> | `Payload`(JSON) | `Task Context`(文本) |
> | `Created By` Aily / Leon / Cron | 增加了 `Claude` |
> | —— | 新增 `Owner`(人员)、`Due Date`、`Trigger Message ID` |
>
> **后果:** 下方"event → Task Type"映射表需重做,映射到新的 `Type` 枚举值。
> 桥接机制本身(自动化发结构化消息)仍可用,但 Aily 写 Task Queue 时字段要按新 schema。

---

## 桥接群角色

```
飞书 Bitable 字段变更
        ↓ (自动化触发)
桥接群发送结构化消息
        ↓ (Aily 监听)
Aily 解析 → 写入 Task Queue 表（Status = Pending）
        ↓
Leon 打开 Claude Code → 一句话清空队列 → Claude 批量处理
```

---

## 消息标准格式

**所有桥接消息使用一致格式（机器易解析）：**

```
🔔 BRIDGE_EVENT
event: {event_name}
table: {table_name}
record_id: {record_id}
field: {field_name}
old_value: {old_value}
new_value: {new_value}
record_summary: {summary_for_context}
timestamp: {ISO_8601}
```

**示例：**

```
🔔 BRIDGE_EVENT
event: STATUS_CHANGED
table: Campaign Calendar
record_id: rec_xxxxxxxxxx
field: Status
old_value: 📋 Planning
new_value: ✍️ Draft Requested
record_summary: Memorial Day Sale Day 1 - Education - Line B - 2026-05-20
timestamp: 2026-05-16T14:23:00+08:00
```

---

## 事件清单（飞书 bitable 自动化需配置的规则）

### Campaign Calendar 表

| 触发条件 | event 值 | Aily 应建的 Task Type |
|----------|----------|----------------------|
| Status 改成 ✍️ Draft Requested | `STATUS_CHANGED` | `generate_draft` |
| Status 改成 🔧 HTML Build | `STATUS_CHANGED` | `build_html` |
| Status 改成 🚀 Ready to Deploy | `STATUS_CHANGED` | `deploy_klaviyo` |

### Draft Workshop 表

| 触发条件 | event 值 | Aily 应建的 Task Type |
|----------|----------|----------------------|
| Draft Status 改成 ✏️ Revision Needed | `STATUS_CHANGED` | `revise_draft` |
| Draft Status 改成 ✅ Approved | `STATUS_CHANGED` | （发送 image prompt 通知，不入队列） |
| Hero Image URL 字段从空变非空 | `FIELD_FILLED` | `build_html` |

### Performance Dashboard 表

| 触发条件 | event 值 | Aily 应建的 Task Type |
|----------|----------|----------------------|
| 新记录被插入 | `RECORD_CREATED` | `generate_learning`（让 Claude 补 Key Learning） |

### Topic Pool 表

| 触发条件 | event 值 | Aily 应建的 Task Type |
|----------|----------|----------------------|
| Status 改成 Used | `STATUS_CHANGED` | （仅记录，不入队列） |

### Promotion Calendar 表

| 触发条件 | event 值 | Aily 应建的 Task Type |
|----------|----------|----------------------|
| 新记录被插入 / Start Date 改 | `NEW_PROMOTION` | （检查是否需要 prewarm，定时触发） |

---

## 飞书 Bitable 自动化配置模板

**针对 Campaign Calendar 的 Status 变更：**

1. 在 Campaign Calendar 表点击"自动化"
2. 触发：**字段变更**
3. 监听字段：**Status**
4. 动作：**发送群消息**
5. 接收群：**Depology EDM Bridge**
6. 消息内容（粘贴下面这段，替换变量）：

```
🔔 BRIDGE_EVENT
event: STATUS_CHANGED
table: Campaign Calendar
record_id: {{record_id}}
field: Status
old_value: {{Status.before}}
new_value: {{Status.after}}
record_summary: {{Campaign Name}} | {{Send Date}} | {{Email Type}} | {{Hero Product}}
timestamp: {{trigger_time}}
```

**注：** 飞书 bitable 自动化字段变量语法可能略有差异，按你飞书版本调整。

---

## Aily 监听 & 解析逻辑（给 Aily 配置时用）

**Aily 应该这样处理收到的桥接消息：**

```
当收到群消息且消息首行 = "🔔 BRIDGE_EVENT"：
  1. 解析消息体，提取 event / table / record_id / field / new_value / record_summary
  2. 根据 event + table + new_value 查找应建的 Task Type（见上方事件清单）
  3. 在 Task Queue 表新建一条记录：
     - Task ID: {timestamp}-{Task Type}
     - Task Type: 查到的类型
     - Target Record ID: 桥接消息里的 record_id
     - Target Table: 桥接消息里的 table
     - Status: ⏳ Pending
     - Priority: Normal（除非 record_summary 含 "Memorial" / "BFCM" / "VIP" 则 High）
     - Payload: 整条桥接消息原文（JSON 包装）
     - Created By: Aily
  4. 检查 Email 群是否需要同步通知（仅特定 Task Type 通知，避免噪音）：
     - generate_draft → 通知："🆕 新草稿待生成：{record_summary}"
     - build_html → 通知："🔧 HTML 待构建：{record_summary}"
     - deploy_klaviyo → 通知："🚀 待部署：{record_summary}"
     - revise_draft → 通知："✏️ 待改稿：{record_summary}"
     - generate_learning → 不通知（每日汇总）
```

---

## Aily 每日待办汇总（每天早上 9:00）

**Aily 定时任务：每天 09:00 执行**

```
1. 读取 Task Queue 表，筛选 Status = Pending 的记录
2. 按 Task Type 分组统计
3. 在 Email 群发汇总消息：

📋 今日 EDM 待办（{date}）
━━━━━━━━━━━━━━━━━━
🆕 待生成草稿: {count} 封
✏️ 待改稿: {count} 封
🔧 待构建 HTML: {count} 封
🚀 待部署: {count} 封
📊 待写 Learning: {count} 封
━━━━━━━━━━━━━━━━━━
打开 Claude Code 说 "清空 EDM 待办" 即可批量处理。
```

---

## Leon 在 Claude Code 的触发命令

```
"清空 EDM 待办"
"处理 Task Queue"
"处理今天的 EDM 任务"
"清空 [Task Type] 类型的任务"  （如：清空 generate_draft 类任务）
```

Claude Code 收到指令后会：
1. 读 Task Queue → 筛选 Pending
2. 按 Priority 排序（High 优先）
3. 逐个执行，每个任务：
   - 更新 Status → Processing
   - 读 Target Record 的完整内容
   - 调用对应 Skill（edm-writer / edm-html-builder / klaviyo-deploy 等）
   - 写回结果
   - 更新 Status → Done，写 Completed At
4. 全部完成后在 Email 群发飞书消息汇总

---

## 错误处理协议

**如果某个 Task 失败：**
- Status → ❌ Failed
- Error Message 字段写入错误详情
- Aily 在 Email 群发紧急消息："⚠️ Task {Task ID} 失败 - {Error Message}"
- Leon 检查后可手动改 Status 回 Pending 重试

---

## Phase 2 切换全自动时的变化

| 维度 | Phase 1 半自动（当前） | Phase 2 全自动（未来） |
|------|----------------------|----------------------|
| Task Queue 消费者 | Claude Code | Aily |
| 内容生成 | Claude Code（订阅） | Aily 内置 LLM |
| 触发 | Leon 一句话清队列 | Aily 定时轮询自动消费 |
| 表结构 | **不变** | **不变** |
| 消息协议 | **不变** | **不变** |
| 桥接群机制 | **不变** | **不变** |

**核心：表结构和协议是稳定的，切换全自动时只换消费者，零迁移成本。**
