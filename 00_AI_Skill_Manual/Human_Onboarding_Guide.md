# Depology EDM Knowledge Base - 使用手册

这份知识库不仅仅是文件的堆砌，它是 Depology EDM 营销的**大脑（策略）**、**手脚（执行）**和**眼睛（洞察）**。

本手册将指导你如何利用这个生态系统来持续产出高转化的邮件。

---

## 1. 核心工作流 (Operations)
*这是你日常最高频使用的文件夹，涵盖了从“创意”到“执行”再到“复盘”的全过程。*

### 📁 `Operations/Topic Pool.md` (选题池)
*   **意义**：你的弹药库。永远不要在写邮件的那一刻才开始想写什么。
*   **如何使用**：
    *   **日常**：定期运行 `fetch_trends.py` 工具，它会自动把 Google 和 Reddit 上的热门护肤话题抓取并填充到这里。
    *   **策划时**：打开文件，从 "Testing Lab" 或分类列表中挑选一个话题，打钩 `[x]` 表示已选用。

### 📁 `Operations/Email_Template_with_Analytics.md` (智能模板)
*   **意义**：你的生产模具。它强制你遵循 "Winning Formula" 的结构，同时预留了数据复盘的位置。
*   **如何使用**：
    *   **写新邮件时**：复制这份文件的内容建立新文档（例如 `2024-05-20_Topic_Name.md`）。
    *   **填充内容**：按照模板里的提示（Hero, Body, Product）填入文案。模板会提醒你哪里该放“承诺”，哪里该放“社会认同”。
    *   **发信后**：不要扔掉文件！等待 3-7 天，回来填写顶部的 `[Post-Campaign Analytics]` 数据区域。

### 📁 `Operations/Campaign Log.md` (进化日志)
*   **意义**：你的长期记忆。记录什么行得通，什么行不通，避免重蹈覆辙。
*   **如何使用**：
    *   **复盘时**：每次发信结束并获得数据后，在这里新增一行。
    *   **决策时**：在策划下个月活动前，先看一眼这个文件。如果上个月 "Educational" 类型的邮件点击率最高，下个月就多排几封。

---

## 2. 战略宪法 (Strategy & Guidelines)
*这些文件定义了 Depology 的灵魂，确保所有邮件风格统一且高效。*

### 📄 `Depology Brand Guidelines.md`
*   **意义**：品牌护栏。规定了我们“说什么”和“怎么说”。
*   **关键点**：确保你的语气是 "Professional yet Accessible"（专业但亲民），视觉风格保持 "Clean & Clinical"。

### 📄 `Depology Product Cards.md`
*   **意义**：军火库。包含了所有核心产品的卖点、成分和痛点解决方案。
*   **使用场景**：当你需要在邮件里推荐 "Matrixyl 3000" 时，直接从这里复制其“主要功效”和“适合人群”，无需重复造轮子。

### 📂 `Winning Formula` (文件夹)
*   **意义**：成功的数学公式。基于过往高转化邮件总结出的规律。
    *   **Topic Formula**：教你如何起标题（Scene -> Surprise -> Promise -> Product）。
    *   **Copy Formula**：教你如何写正文（PAS模型：Problem-Agitation-Solution）。
*   **使用场景**：当你感觉写出来的邮件“没劲”或者“像推销员”时，对照这些公式检查，通常能发现问题所在。

---

## 3. 自动化雷达 (Tools)
*你的全天候市场侦察兵。*

### 🛠 `tools/fetch_trends.py`
*   **意义**：自动化趋势捕获器。
*   **功能**：
    1.  **Google Trends**：监控 "Skincare", "Retinol" 等大词的搜索飙升趋势。
    2.  **Reddit (r/SkincareAddiction)**：监听真实硬核用户的讨论热点。
*   **如何使用**：
    *   直接运行脚本。
    *   它会自动去重、格式化，并将新话题追加到 `Operations/Topic Pool.md` 的底部。
    *   *注：如果 Google API 暂时受限，它会自动切换到模拟模式演示流程，Reddit 部分则持续提供真实数据。*

---

## 💡 标准作业程序 (SOP) - 打造一封爆款邮件

1.  **侦察**：运行 `fetch_trends.py`，看看最近大家在聊什么（比如 "Skin Cycling"）。
2.  **选材**：在 `Topic Pool.md` 中选中该话题，结合 `Product Cards.md` 里的产品（比如 Retinol Serum）。
3.  **起草**：复制 `Email_Template_with_Analytics.md`，运用 `Winning Formula` 的技巧撰写文案。
4.  **发送**：在 Klaviyo 中配置发送。
5.  **记录**：3天后，将 Open Rate / Click Rate / Revenue 填回邮件文档，并在 `Campaign Log.md` 中记下一笔：“这个话题很火，但转化一般，下次尝试更换落地页”。

---

**Depology EDM Team**
*Data-Driven, Customer-Centric.*
