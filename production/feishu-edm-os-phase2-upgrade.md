# Phase 2 升级：半自动 → 全自动 Aily 模式

> 当你跑顺半自动模式后（预计 1-2 个月），按这份文档把生产环节从 Claude Code 切换给 Aily。
> **核心承诺：表结构、桥接协议、Task Queue 机制全部不变，零迁移成本。**

---

## 切换的前置条件

切换全自动前，请确认：

1. ✅ 半自动模式已稳定跑过 **至少 10 封 campaign**
2. ✅ Aily 写的邮件质量你已经做过 **A/B 对比测试**，与 Claude Code 差距可接受
3. ✅ 你已经把以下内容**整理成 Aily 的知识库**：
   - `knowledge/products/` 所有产品 SKU 卡片
   - `knowledge/compliance/email-compliance-rules.md`
   - `knowledge/formulas/copy-winning-formula.md`
   - `knowledge/brand-voice/` 品牌语调指南
4. ✅ Aily 已连接 Klaviyo Private API Key
5. ✅ Aily 已建好对应 12 个 Flow 的工作流（每个 Task Type 对应一个 Flow）

---

## 切换操作（实际只需 4 步）

### Step 1：在 Aily 配置 Task Queue 消费者

让 Aily 每隔 5 分钟轮询一次 Task Queue 表：
```
定时任务：每 5 分钟
1. 读 Task Queue, Status = Pending
2. 按 Priority 排序
3. 对每个 Task，根据 Task Type 路由到对应 Aily Flow
4. 执行完成 → 更新 Status → Done
```

### Step 2：暂停 Claude Code 的 Task Queue 消费

在 `.skills/feishu-edm-os/skill.md` 顶部加一行：
```
> ⚠️ Phase 2 已启用，Task Queue 消费者已切换至 Aily。
> Claude Code 仅在 Leon 显式触发"用 Claude 重做 [task_id]"时介入。
```

### Step 3：留 Claude Code 作为 fallback

Aily 写的草稿如果你不满意，可以在 Email 群 @Aily 说：
```
@Aily 把 task_id=xxx 标记为 needs_claude_rework
```
Aily 把该 Task Status 改回 Pending + Priority = High + 加标签 "needs_claude_rework"。
Claude Code 检测到这个标签会优先处理（用更高质量上下文）。

### Step 4：验证发送 + 数据回收闭环

切换后第一周观察：
- Aily 生成的草稿是否符合 Copy Winning Formula
- Aily 生成的 HTML 是否能在 Klaviyo 正确渲染
- 数据回收是否自动写入 Performance Dashboard
- 月末复盘是否准确

---

## 切换后 Claude Code 的剩余角色

| 任务 | 频率 | 谁做 |
|------|------|------|
| 日常 EDM 生产 | 每周 5-8 次 | **Aily** |
| 高优先级 campaign 质量补刀 | 每月 2-4 次 | **Claude Code（你 @ 触发）** |
| 月度策略规划 | 每月 1 次 | **Claude Code（深度推理）** |
| 月末复盘分析 | 每月 1 次 | **Claude Code 或 Aily** |
| 知识库更新 | 不定期 | **你 + Claude Code** |

---

## 如果切换失败怎么办

**回滚步骤（5 分钟）：**

1. 在 Aily 关闭那个"每 5 分钟轮询 Task Queue"的定时任务
2. 在 `.skills/feishu-edm-os/skill.md` 删除那行 ⚠️ Phase 2 已启用
3. Claude Code 继续消费 Task Queue

**没有数据损失，因为：**
- 表结构没动
- Task Queue 机制没动
- 桥接协议没动
- 只是消费者换回 Claude Code

---

## 升级时机判断（哪些信号代表"该升级了"）

✅ **可以升级的信号：**
- Aily 写的邮件 OR 不低于 Claude 版本 5%
- 你打开 Claude Code 处理 Task Queue 已经成习惯但觉得"还能更省事"
- 团队有人想接手 EDM 工作（手机就能管理）

❌ **暂时别升级的信号：**
- 半自动模式还没跑过 10 封
- Aily 还没接入完整品牌知识库
- 即将到来 BFCM 等大促（不在风险期切换）

---

## 长期愿景：Phase 3 完全无人值守

未来如果 Aily 质量稳定（半年观察），可以彻底取消 Claude Code 介入：
- 月度规划 Aily 做
- 内容生成 Aily 做
- 部署 Aily 做
- 复盘 Aily 做
- 你只在飞书看仪表盘 + 月度策略调整

到那一步，**整个 EDM OS 真正成为「你在飞书上点点改改就能管理整条邮件业务」的系统**——就是你最早问的那个目标。
