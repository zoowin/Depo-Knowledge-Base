# Hero Image Prompt Formula（即梦专用）

> **工具：** 即梦（Jimeng）
> **核心原则：** 产品用真实 PNG，AI 只生成背景场景。绝不在 prompt 里描述产品外观。
> **Last updated:** 2026-03-18

---

## 工作流程

### Step 1: 准备底图
1. 从 `knowledge/products/product-image-urls.md` 获取对应产品的 PNG 图片
2. 在即梦画布中导入产品 PNG，摆好位置（通常居中偏右或居中偏左）
3. 产品大小约占画面 25-35%

### Step 2: 局部重绘
1. 使用即梦的「局部重绘」功能
2. **涂抹产品以外的所有区域**（背景、空白处）
3. 产品本身不涂，保持原样
4. 输入下方的场景 Prompt

### Step 3: 输入 Prompt
只描述背景/场景/光线/氛围，不提任何产品相关词汇。

---

## Prompt 模板

```
[表面材质], [装饰元素], [光线描述], [色调氛围], [构图说明]. Premium beauty editorial photography, clean composition --ar 3:2
```

### 各字段选项库

**表面材质（Surface）：**
- soft blush marble surface
- white travertine stone surface
- light oak wood surface
- frosted glass surface
- pale linen fabric background
- concrete gray surface with subtle texture
- black marble surface with gold veins

**装饰元素（Props）— 按季节/主题选：**

| 主题 | 装饰元素 |
|------|---------|
| 春季/Easter | delicate white ranunculus, pale pink tulips, small pastel eggs, fresh green leaves |
| 夏季 | citrus slices, ice cubes, monstera leaves, water droplets on surface |
| 秋季 | dried eucalyptus, warm amber glass, cinnamon sticks, maple leaves |
| 冬季/Holiday | pine branches, gold ribbon, soft snow texture, warm candlelight glow |
| 科学/教育 | clean minimalist lab aesthetic, petri dishes with clear gel, molecular structure shadows |
| 日常/Lifestyle | soft cotton towel, morning coffee cup edge, reading glasses, fresh flowers |
| 夜间/Night | dark moody surface, soft moonlight glow, silk fabric, candle |

**光线（Lighting）：**
- soft diffused morning light from left
- warm golden hour side lighting
- cool studio lighting with soft shadows
- overhead natural light with gentle shadows
- dramatic side light with deep shadows

**色调（Color Palette）：**
- warm blush and cream tones
- cool blue and silver tones
- neutral beige and white
- rich dark tones with gold accents
- fresh green and white

**构图说明（Composition）：**
- clean open space on left side for product
- generous negative space in center for product placement
- shallow depth of field, background slightly blurred
- overhead flat lay angle
- 45-degree angle, eye-level perspective

---

## 示例 Prompt（完整版）

### Easter Weekend（春季促销）
```
Soft blush marble surface, delicate white ranunculus and pale pink tulips arranged loosely, a few small pastel Easter eggs as subtle accents, fresh green leaves scattered naturally. Soft diffused morning light from left, warm blush and cream tones, clean open space in center-right for product placement. Premium beauty editorial photography, clean composition --ar 3:2
```

### 教育类（成分科学）
```
White travertine stone surface, clean minimalist aesthetic, a single petri dish with clear gel in background, subtle molecular shadow pattern on surface. Cool studio lighting with soft shadows, neutral white and gray tones, generous negative space on right side. Premium beauty editorial photography, scientific yet elegant --ar 3:2
```

### 夜间护肤（Retinol / Night Routine）
```
Dark charcoal marble surface with subtle gold veins, soft silk fabric draped in corner, warm candlelight glow from behind. Dramatic side light with deep shadows, rich dark tones with warm amber accents, clean space in center for product. Premium beauty editorial photography, moody and luxurious --ar 3:2
```

### Lifestyle 日常
```
Light oak wood surface, soft white cotton towel folded neatly in corner, fresh eucalyptus sprigs, morning light streaming in from window. Warm golden hour side lighting, neutral beige and white tones, overhead flat lay angle with open center space. Premium beauty editorial photography, calm and inviting --ar 3:2
```

---

## Claude 输出格式

以后每封邮件 draft 的 Hero Image Brief 按以下格式输出：

```
## Hero Image Brief

**主推产品：** [产品名] — 图片编号 #[X]（来自 product-image-urls.md）
**产品位置：** [居中偏右 / 居中偏左 / 居中]
**产品占比：** 约 [25-35]% 画面

**即梦操作：**
1. 导入产品 PNG 到画布，放置在 [位置]
2. 局部重绘：涂抹产品以外所有区域
3. 输入以下 prompt：

**场景 Prompt：**
[完整 prompt，只有场景描述，不含产品]

**备选 Prompt（如果第一版效果不好）：**
[换一个不同风格/材质的 prompt]
```

---

## 注意事项

1. **绝不在 prompt 里写** "skincare product"、"bottle"、"serum"、"cream jar" 等产品词汇 — 这会导致 AI 生成假产品
2. **多试几次** — 即梦的局部重绘可能需要 2-3 次才能得到满意的融合效果
3. **调整重绘强度** — 如果背景太抢眼，降低重绘强度；如果太单调，提高强度
4. **最终图片尺寸** — 600 × 400px（邮件 hero 标准比例 3:2）
