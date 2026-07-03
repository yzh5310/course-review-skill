---
name: course-review
description: 基于9大学习科学理论的通用课程交互式复习方案生成器v4.0——三层深度选择+自适应学习路径+间隔重复+错因分类+正反馈系统+纸质输出全场景+知识点屏蔽+AI出题助手。面向基础薄弱、短时间需完成复习的群体，帮助AI为任意课程创建定制化单文件HTML复习应用。适用于大学课程考前速通、职业资格考试冲刺、跨专业补课等场景。
---

# Course Review Skill v4.0 — 学习科学驱动的课程速通复习应用生成器

> **核心理念**：不是文档，是学习应用。融合费曼学习法、主动回忆、间隔重复、掌握学习、最近发展区、认知负荷理论、元认知训练、自我效能感、情境认知9大学习科学理论，用精准急救设计哲学帮基础薄弱学生在最短时间内建立应试框架。v4.0新增**系统十：AI出题助手**（导出个性化提示词→外部AI生成题目→一键导入扩充题库，解决题目数量不足和文件体积过大的问题）。
> **不是固定模板**：AI应根据课程特点自主增减模块，本skill提供的是设计理念和最佳实践，而非刻板框架。template.html是可直接运行的完整参考实现。

---

## v4.0 重大升级总览

v4.0 在v3.1基础上新增"AI出题助手"系统，实现题库无限扩展与文件体积控制的平衡：

| 新系统/组件 | 学习科学理论 | 核心价值 | 版本 |
|--------|-------------|---------|------|
| 三层深度选择器 | 最近发展区（Vygotsky） | 不同基础学生各取所需（60分/80分/90分） | v3.0 |
| 自适应学习路径引擎 | 掌握学习（Bloom） | 知识图谱+前置依赖+微检测门控，只学该学的 | v3.0 |
| 间隔重复系统（类Anki） | 间隔重复（Ebbinghaus） | 7级间隔算法+四级掌握度+到期提醒 | v3.0 |
| 错因6分类系统 | 元认知（Metacognition） | 把错题从失败转化为精准诊断数据 | v3.0 |
| 主动回忆强化机制 | 主动回忆（Active Recall） | 遮挡做题+翻转卡片+诊断前置 | v3.0 |
| 情感设计系统 | 自我效能感（Bandura） | 撒花庆祝+CTA脉冲+进度可感知+心理建设 | v3.0 |
| 全局进度追踪 | 自我调节学习 | 四维加权进度条+localStorage持久化 | v3.0 |
| 纸质输出与全场景陪伴 | 情境认知+分布式认知 | 一页纸打印+移动端适配+状态可导出 | v3.1 |
| 知识点屏蔽系统 | 认知负荷+自我调节学习 | 一键标记不考知识点，联动隐藏 | v3.1 |
| **AI出题助手** | **最近发展区+元认知+自我效能感** | **个性化提示词生成+智能JSON解析+一键导入，题库无限扩充且保持文件轻量** | **v4.0** |

版本演进轨迹：
- v2.1-v3.1: （略，见提交历史）
- **v4.0: AI出题助手（系统十）——轻量核心题库+外部AI出题+智能导入，三步零摩擦扩充题库**

---

## 给AI的阅读指南（最高优先级）

如果你是AI，正在阅读这个skill来为用户创建复习方案，请严格遵循以下原则：

### 第一原则：9大学习科学理论是灵魂

你创建的每一个复习页面，都必须系统性地融合以下学习科学理论，而非仅用费曼法一个：

| 学习科学理论 | 在复习页中的核心体现 | 你必须做到 |
|-------------|---------------------|-----------|
| **费曼学习法** | 白话解释+几何直观+类比+误区+口诀 | 用最简单的话解构抽象，禁止术语堆砌 |
| **主动回忆** | 遮挡做题+翻转卡片+诊断前置+配套小测 | 始终让学生输出，而非被动阅读 |
| **间隔重复** | 类Anki算法+到期提醒+掌握度分级 | 自动安排复习时机，对抗遗忘曲线 |
| **最近发展区** | 三层深度选择器+自适应路径门控 | 内容始终在"跳一跳够得着"的难度 |
| **认知负荷理论** | 渐进披露（四层折叠）+模块化卡片+ScrollSpy+着陆高亮 | 避免一次性呈现过多内容，长页面不迷路 |
| **掌握学习** | 微检测门控+知识地图+撒花庆祝+回学机制 | 必须掌握当前节点才能前进 |
| **元认知训练** | 错因6分类+错因统计+自测清单+盲区诊断 | 帮学生知道"我哪里不会、为什么错" |
| **自我效能感** | CTA脉冲+撒花动效+进度可视化+可行动Toast+页脚心理建设 | 降低焦虑，建立信心，每步操作都有闭环反馈 |
| **情境认知/分布式认知（v3.1）** | 一页纸打印+移动端速翻+多端连续 | 学习发生在多场景，纸张和手机是认知延伸 |

### 第二原则：精准急救，而非全面灌输

这是一个**考前冲刺工具**，不是教材。所有设计决策服务于"最短时间拿最多分"：
- 诊断前置，拒绝盲目复习
- 依赖树预警，优先攻克阻塞点
- 三层深度，不同基础的人各取所需
- 考什么学什么，以模拟卷原题为锚点

### 第三原则：学习应用，而非静态文档

这不是一个静态HTML页面，而是一个**单文件Web应用**：
- 零构建、零后端、零依赖（除KaTeX CDN），一个HTML文件即完整应用
- 完整的数据持久层（localStorage）
- 模块化IIFE脚本架构，功能间互不干扰
- 渐进增强+优雅降级
- v3.1新增：支持打印为一页纸，移动端适配候考速翻场景

### 第四原则：情感设计降低焦虑

你的读者是考前焦虑的基础薄弱学生：
- 零基础入口不歧视"小白"，开头第一句安抚
- 正向反馈密度高：每步操作都有Toast/颜色/动画反馈
- 进度始终可视化：让学习者知道"我在哪里、走了多远、下一步是什么"
- 页脚必须有心理建设（呼吸提示、鼓励话语）

### 第五原则：课程类型决定设计哲学

**不同类型的课程需要不同的"降维"策略。** AI必须先判断课程类型，再决定采用哪种设计哲学。详见下文"课程类型差异化设计指南"。

### 第六原则：参考材料优先于AI推测（v2.2继承·最重要）

**AI在生成复习方案前，必须主动询问用户是否有参考材料。** 详见下文"参考材料使用指南"。

### 第七原则：例题驱动优于概念罗列（v2.3继承）

对计算型/应用型课程，以典型题目为核心展开知识点，从解题过程中学概念。详见下文"例题驱动设计指南"。

### 第八原则：灵活组合，而非照搬模板

**不要照搬任何已有复习页的全部模块。** 分析课程特点，决定：
- 哪些模块需要？概念型课程不需要Canvas可视化；文科课程不需要计算题库
- 模块顺序如何排？编程课可能先放代码示例再放概念；历史课可能先放时间线
- 内容深度多深？保命模式只显示核心母题；冲刺模式全部展开
- 需要哪些题型？看考试形式

---

## 指令

### 步骤一：收集参考材料（必须执行）

**这是生成复习方案前的第一个步骤，不可跳过。** AI必须主动向用户询问参考材料。

#### 1.1 询问话术模板

```
在开始生成复习方案之前，我想先了解一下你手上是否有以下参考材料。
这些材料能帮我更精准地匹配你们学校的考点和出题风格，避免"复习偏了"：

1. 📝 往年试卷/期末卷（最有价值——直接反映考点和难度）
2. 📋 平时作业/练习题（反映老师关注的重点）
3. 📊 上课课件/PPT（反映教学大纲和重点）
4. 📖 教学大纲/考试范围（明确考什么、不考什么）
5. 📚 教材课后习题（基础题型参考）

你可以提供以下任意形式：
- 直接上传文件（PDF、Word、图片、PPT等）
- 粘贴文字内容
- 描述考点和题型（如"往年考了3道Green公式大题"）

即使没有这些材料也没关系，我会基于通用知识生成方案，
但会在页面中标注哪些内容是基于推测的，建议你自行校验。
```

#### 1.2 参考材料处理原则

| 用户回应 | AI的行动 |
|---------|---------|
| 提供了往年试卷 | **最高优先级**：提取原题加入题库，分析考点分布调整章节权重，模仿出题风格补充相似题。标注"📌 来源于往年试卷" |
| 提供了平时作业 | 提取典型题加入题库，识别高频考点。标注"📌 来源于平时作业" |
| 提供了课件/PPT | 校准知识点覆盖范围，识别老师额外强调的内容。标注"📌 课件强调" |
| 提供了考试范围 | 精准划定复习边界，删除不考的章节。标注"📌 考试范围" |
| 描述了考点（无文件） | 根据描述调整知识点权重和题型分布 |
| 表示没有材料 | 明确告知用户内容基于AI推测，添加显著提醒"⚠️ 本方案基于通用知识生成，考点可能与你校实际考试有偏差" |

### 步骤二：分析课程信息

向用户收集以下信息（如用户未提供）：

1. 课程名称
2. 课程类型（概念型/计算型/实践型/混合型）
3. 章节范围
4. 考试形式（选择题/简答题/计算题/论文/混合）
5. 学生基础（完全零基础/有一定基础/基础较好）
6. 复习时间（1天/2天/3天）
7. 目标分数（补考救命60分/稳过及格75-85分/冲刺高分90+）
8. 核心概念（3-5个最重要的概念）

### 步骤三：确定模块组合与深度层级

根据课程类型和目标分数选择模块组合，详见"模块系统"章节。

### 步骤四：生成单文件HTML复习应用

生成一个**单个自包含HTML文件**，包含所有CSS和JavaScript。推荐页面结构（宏观流程）：

```
[Header: 标题+三层深度选择器+CTA]
  ↓
[Sticky Nav: 入门→诊断→路径→学习→刷题→一页纸]
  ↓
🌱 新手引导（零基础入口+6步学习路径+速记口诀+时间分配）
  ↓
🔍 知识盲区诊断（6题快速测试→盲区报告→学习路径推荐）
  ↓
🧭 自适应学习路径（知识地图+推荐引擎+微检测+进度条）【v3.0核心】
  ↓
🪢 计算依赖树（计算型课程：可视化链式依赖+阻塞点预警）
  ↓
🔗 统一性主线表（有统一性主线的课程：对比表展示推广关系）
  ↓
📚 核心内容精讲（例题驱动/概念精讲，手风琴折叠）
  ↓
📋 公式/要点速查（卡片网格）
  ↓
⚠️ 陷阱库（计算型：计算陷阱库；概念型：常见误区库）
  ↓
🎯 题库刷题（多模式:顺序/随机/章节/间隔复习/错题本）【v3.0增强】
  ↓
✅ 考前自测清单（可勾选能力清单+完成度）
  ↓
📄 考前一页纸（翻转卡+随机抽测+我的摘录+打印模式）【v3.0增强】
  ↓
[Footer: 心理建设+深呼吸提示]
```

---

## v3.0 核心系统设计指南

### 系统一：三层深度选择器（最近发展区理论）

通过CSS `body[data-depth]`属性动态控制内容可见性，匹配不同学习者的"最近发展区"。

#### 三档定义

| 档位 | data-depth值 | 目标人群 | 显示内容 | 隐藏内容 |
|------|-------------|---------|---------|---------|
| 补考救命 | `survival` | 只求及格（60分） | 每章第1道母题+核心公式+最基础考点 | 变式、陷阱库、可视化、统一性主线、难题 |
| 稳过及格 | `standard` | 目标75-85分 | 核心+变式+陷阱库+所有例题+题库基础题 | Canvas高级动画、超纲内容 |
| 冲刺高分 | `advanced` | 目标90+ | 全部内容含Canvas动画+综合题+统一性主线深度理解 | 无 |

#### HTML结构

```html
<!-- Header中的深度选择器 -->
<div class="depth-selector">
  <span class="depth-label">选择目标：</span>
  <button class="depth-btn active" data-depth="survival">🆘 补考救命(60分)</button>
  <button class="depth-btn" data-depth="standard">✅ 稳过及格(80分)</button>
  <button class="depth-btn" data-depth="advanced">🚀 冲刺高分(90+)</button>
</div>
```

#### CSS控制

```css
/* 默认显示所有（冲刺档） */
.depth-survival-only { display: none; }
.depth-standard-only { display: none; }
.depth-advanced-only { display: block; }

/* 保命档：只显示核心 */
body[data-depth="survival"] .depth-advanced-only,
body[data-depth="survival"] .depth-standard-only { display: none !important; }
body[data-depth="survival"] .depth-survival-only { display: block; }
body[data-depth="survival"] .example-card:not(.survival-core) { display: none; }

/* 标准档：显示核心+变式+陷阱 */
body[data-depth="standard"] .depth-advanced-only { display: none !important; }
body[data-depth="standard"] .depth-standard-only { display: block; }
body[data-depth="standard"] .depth-survival-only { display: block; }
```

#### JavaScript实现

```javascript
function setDepth(depth) {
  document.body.setAttribute('data-depth', depth);
  localStorage.setItem('course_depth', depth);
  showToast('已切换到' + depthLabels[depth] + '模式');
  // 更新按钮状态
  document.querySelectorAll('.depth-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.depth === depth);
  });
}
```

### 系统二：自适应学习路径引擎（掌握学习理论）

基于知识图谱的自适应推荐系统，确保学习内容始终在"跳一跳够得着"的难度。

#### 核心要素

1. **知识图谱节点**：10-20个知识点节点，每个节点有id、名称、前置依赖数组、关联章节、难度
2. **就绪算法**（`isReady(node)`）：只有当所有前置依赖节点都已掌握时，该节点才解锁
3. **微检测门控**：每个知识点必须通过1道微检测题才能标记为"掌握"
4. **四色状态可视化**：
   - 🟢 绿色（mastered）：已掌握
   - 🟡 黄色（ready）：已就绪可学（前置已掌握）
   - ⚪ 灰色（locked）：未解锁（前置未掌握）
   - 🟣 紫色（current）：当前学习中
5. **进度条**：已掌握节点/总节点数
6. **聚焦模式**：淡化已掌握和未解锁节点，高亮当前和就绪节点

#### 知识图谱数据结构

```javascript
const knowledgeGraph = [
  { id: 'vec', name: '向量运算', chapter: 1, prereqs: [], difficulty: 'easy' },
  { id: '偏导', name: '偏导数', chapter: 2, prereqs: ['vec'], difficulty: 'medium' },
  { id: '重积分', name: '二重积分', chapter: 3, prereqs: ['偏导'], difficulty: 'hard' },
  { id: 'green', name: 'Green公式', chapter: 4, prereqs: ['重积分'], difficulty: 'hard' },
  // ...更多节点
];
```

#### 微检测设计

- 每个就绪节点显示"开始学习"按钮
- 学习完概念/例题后，弹出1道微检测题
- 答对 → 绿色庆祝+撒花纸屑+标记为mastered+自动推荐下一节点
- 答错 → 红色+正确答案+"回学重试"按钮

### 系统三：间隔重复系统（间隔重复理论）

实现类Anki的v3间隔重复引擎，自动安排复习时机。

#### 算法参数

- **7级间隔序列**：`[20分钟, 1小时, 9小时, 1天, 2天, 4天, 7天]`
- **四级掌握度**：`new(0) → learning(1-2) → review(3-5) → mastered(6+)`
- **晋级规则**：答对 → stage+1（间隔拉长）；答错 → stage=0（5分钟后重现）
- **到期题闪烁**：红色`sr-due-indicator`脉冲提示

#### 数据结构

```javascript
// localStorage键: course_sr_data
{
  questionId: {
    stage: 0-6,           // 当前间隔阶段
    streak: 0,            // 连续答对次数
    nextReview: timestamp, // 下次复习时间
    lastReview: timestamp,
    history: []           // 答题历史
  }
}
```

#### 关键函数

```javascript
const SR_INTERVALS = [20*60*1000, 60*60*1000, 9*60*60*1000, 24*60*60*1000, 
                      2*24*60*60*1000, 4*24*60*60*1000, 7*24*60*60*1000];

function updateSRS(questionId, correct) {
  var data = getSRData();
  var item = data[questionId] || { stage: 0, streak: 0 };
  if (correct) {
    item.streak++;
    item.stage = Math.min(item.stage + 1, 6);
  } else {
    item.streak = 0;
    item.stage = 0;
  }
  item.lastReview = Date.now();
  item.nextReview = Date.now() + (item.stage === 0 ? 5*60*1000 : SR_INTERVALS[item.stage]);
  data[questionId] = item;
  localStorage.setItem('course_sr_data', JSON.stringify(data));
}

function getDueQuestions() {
  var data = getSRData();
  var now = Date.now();
  return Object.keys(data).filter(id => data[id].nextReview <= now);
}
```

### 系统四：错因6分类系统（元认知训练）

把错题从"失败"转化为"精准诊断数据"，这是v3.0最核心的元认知工具。

#### 6类错因定义

| 错因类型 | 颜色 | 诊断话术 | 精准补救路径 |
|---------|------|---------|-------------|
| 概念误解 | 蓝色 | "你对XX概念的理解有偏差" | 跳转概念精讲区白话版+类比 |
| 公式记错 | 紫色 | "XX公式记错了/漏了关键部分" | 跳转公式速查卡+口诀强化 |
| 计算失误 | 橙色 | "方法对了但计算出错" | 推荐计算专项练习+陷阱提醒 |
| 方法选错 | 红色 | "这道题不该用这个方法" | 跳转方法决策树+信号识别训练 |
| 审题失误 | 灰色 | "题目条件没看清/漏看" | 提示圈画关键词的审题习惯 |
| 前置薄弱 | 黄色 | "这道题需要XX前置知识，你还没掌握" | 跳转前置依赖节点回学 |

#### AI智能猜错因

`guessErrorCategory()`根据题目关键词预标注⭐建议：
- 题目含"极坐标/柱坐标/球坐标" → 公式错（极坐标忘乘r是高频错误）
- 题目含"Green/Gauss/Stokes" → 方法错（未检查封闭性/方向）
- 题目含"极限/连续/可导" → 概念误解
- 题目含"应用/实际问题" → 审题失误

#### 错因统计面板

答题结束后展示：
- 柱状图展示各错因类型数量分布
- 个性化薄弱环节建议："你在【方法选择】上错误最多，建议复习方法决策树"
- 每类错因配"立即补救"跳转按钮

### 系统五：主动回忆强化机制（主动回忆理论）

v3.0系统性地强化主动回忆，让学生始终在"输出"而非被动阅读。

#### 5.1 遮挡式练习模式

例题关键结果（`.ex-step-result`）默认隐藏，显示"🤔 先自己算算？点击查看"，强制学习者先尝试再看答案。

```css
.ex-step-result.hidden {
  filter: blur(6px);
  cursor: pointer;
  user-select: none;
}
.ex-step-result.hidden::after {
  content: '🤔 先自己算算？点击查看';
  position: absolute;
  /* ... */
}
```

#### 5.2 翻转卡片（Flip Cards）

考前一页纸的所有公式/要点以问答卡片形式呈现：问题朝上、答案点击翻转，配合"已记住/需复习"二元标记。

```html
<div class="flip-card" onclick="this.classList.toggle('flipped')">
  <div class="flip-inner">
    <div class="flip-front"><strong>Q:</strong> Green公式的条件是什么？</div>
    <div class="flip-back"><strong>A:</strong> P、Q在闭区域D上有一阶连续偏导数...</div>
  </div>
</div>
```

#### 5.3 诊断前置

学习前必须先做6道诊断题，以"输出"驱动"输入"。诊断结果与自适应路径联动：答对章节自动标记基础节点为已掌握。

#### 5.4 选择题加"不会"选项

所有选择题增加"🤷 不会"选项（降低猜测率，诚实反映盲区）：

```javascript
options: ["A选项", "B选项", "C选项", "D选项", "🤷 不会"]
// 选"不会"直接标记为盲区，不蒙答案
```

### 系统六：情感设计与正反馈系统（自我效能感理论）

v3.0高度重视情感设计，降低考前焦虑，建立信心。

#### 6.1 微交互动效

| 动效 | 触发时机 | CSS/JS实现 |
|------|---------|-----------|
| CTA脉冲呼吸灯 | 主按钮持续 | `@keyframes ctaPulse` 红色阴影呼吸 |
| 撒花庆祝 | 掌握知识点/答对微检测 | `celebrateConfetti()` 40片彩色纸屑下落 |
| 就绪节点脉冲 | 可学节点黄色光环 | `@keyframes ap-pulse` 光环扩散 |
| 到期题闪烁 | 间隔重复到期题 | `@keyframes sr-pulse` 透明度0.5↔1 |
| 章节跳转高亮 | 跳转到某章节 | `.section-highlight` 闪烁2.5秒 |
| Toast通知 | 所有操作反馈 | 淡入淡出+居中弹出 |

#### 6.2 撒花纸屑实现

```javascript
function celebrateConfetti() {
  var colors = ['#7c3aed', '#2563eb', '#16a34a', '#f59e0b', '#ec4899'];
  for (var i = 0; i < 40; i++) {
    var p = document.createElement('div');
    p.style.cssText = 'position:fixed;width:8px;height:8px;border-radius:50%;pointer-events:none;z-index:99999;';
    p.style.background = colors[Math.floor(Math.random()*colors.length)];
    p.style.left = (50 + (Math.random()-0.5)*20) + '%';
    p.style.top = '50%';
    document.body.appendChild(p);
    // 动画：下落+散开+淡出
    var angle = Math.random() * Math.PI * 2;
    var vel = 3 + Math.random() * 5;
    var x = 0, y = 0, vy = -3;
    var anim = setInterval(function() {
      x += Math.cos(angle) * vel * 0.3;
      y += (vy += 0.15);
      p.style.transform = 'translate(' + x + 'px,' + y + 'px)';
      p.style.opacity = Math.max(0, 1 - y/200);
      if (y > 200) { clearInterval(anim); p.remove(); }
    }, 16);
  }
}
```

#### 6.3 Toast通知系统

```javascript
function showToast(msg, duration) {
  duration = duration || 2500;
  var t = document.createElement('div');
  t.className = 'toast-notification';
  t.textContent = msg;
  t.style.cssText = 'position:fixed;top:80px;left:50%;transform:translateX(-50%);background:#1e293b;color:#fff;padding:12px 24px;border-radius:999px;font-weight:700;z-index:99999;box-shadow:0 8px 30px rgba(0,0,0,0.2);opacity:0;transition:0.3s;';
  document.body.appendChild(t);
  requestAnimationFrame(() => { t.style.opacity = '1'; t.style.top = '100px'; });
  setTimeout(() => { t.style.opacity = '0'; t.style.top = '80px'; setTimeout(() => t.remove(), 300); }, duration);
}
```

#### 6.4 页脚心理建设

页面底部必须包含：

```html
<footer style="text-align:center;padding:40px 20px;color:var(--muted);">
  <p style="font-size:16px;">💡 <strong>考前最后提醒：</strong></p>
  <p>深呼吸3次。你已经复习了最核心的考点，及格绝对没问题。</p>
  <p>遇到不会的题先跳过，把会做的都做对就赢了。加油！💪</p>
</footer>
```

### 系统七：全局进度追踪系统

#### 7.1 四维加权全局进度条

顶部固定3px进度条（绿→黄→红渐变）+ 百分比标签，权重：

| 维度 | 权重 | 计算方式 |
|------|------|---------|
| 诊断测试 | 15% | 答对题数/总题数 |
| 自适应路径掌握 | 40% | 已掌握节点/总节点 |
| 自测清单完成 | 25% | 已勾选/总项数 |
| 题库刷题 | 20% | 答对数/目标题数 |

#### 7.2 localStorage数据持久层（12+独立键）

| 存储Key | 追踪对象 |
|---------|---------|
| `course_depth` | 深度偏好（survival/standard/advanced） |
| `course_dark` | 暗黑模式布尔值 |
| `course_ex_hide` | 遮挡模式布尔值 |
| `course_diag_result` | 诊断结果（6题答案+分数+盲区） |
| `course_adaptive_path` | 自适应路径节点掌握状态 |
| `course_checks` | 12项自测清单勾选状态 |
| `course_qb_progress` | 题库进度（答题数/正确数/当前题序） |
| `course_sr_data` | 间隔重复数据（stage/连击/下次复习时间） |
| `course_wrongbook` | 错题本（错题+错因标签+错因历史） |
| `course_flip_marks` | 翻转卡片标记（known/review） |
| `course_my_excerpts` | 划词摘录（选中文本+来源+时间） |

---

## v4.0 系统十：AI出题助手

### 设计目标

解决两个核心矛盾：
1. **题目数量 vs 文件体积**：内置题库越多HTML越大，但内置题少又不够练习
2. **个性化 vs 通用性**：不同学生的薄弱点不同，固定题库无法千人千面

方案：**轻量核心题库（50-80题）+ 外部AI出题 + 智能导入**，用户可以随时用自己的AI工具生成个性化题目并导入，文件保持轻量。

### 用户流程（三步零摩擦）

```
点击AI助手 → 配置出题范围/数量/难度 → 一键复制提示词
    → 打开外部AI（豆包/DeepSeek/Kimi/文心一言）粘贴发送
    → 复制AI回复 → 回到页面粘贴导入 → 自动开练
```

### 核心模块

#### 1. 智能提示词生成器（PromptGenerator）

读取用户学习状态，生成高度个性化的出题提示词：
- **深度适配**：根据当前选择的深度（survival/standard/advanced）自动调整难度分布（简单:中等:困难）
- **薄弱点定位**：读取自适应学习路径（`adaptive_path`）中未通过的节点
- **错题关联**：读取错题本（`wrongbook`），提取错题相关章节
- **格式规范**：提示词内包含完整JSON格式说明、题目示例、评分标准

提示词模板结构：
```
你是一位[课程名]考试出题专家。请为我生成[N]道[难度分布]题目。

【我的学习状态】
- 当前目标：60分及格/80分稳过/90+冲刺
- 已掌握知识点：...
- 薄弱知识点：...
- 错题相关章节：...
- 近期正确率：约X%

【出题要求】
- 范围：[薄弱知识点/全部章节/错题相关/指定章节]
- 题型分布：[选择题X%/判断题X%/计算题X%/简答题X%]
- 难度：基础X% / 中等X% / 困难X%
- 每题必须包含：题干、选项（选择题）、正确答案、详细解析、所属章节、难度标签(e/m/h)

【输出格式】
严格输出JSON数组，不要输出其他内容：
[{"q":"题目","o":["A.选项","B.选项"...],"a":"B","explain":"解析","chapter":"章节","difficulty":"m"}]
```

#### 2. 智能JSON提取器（SmartJSON）

AI输出经常带有markdown标记、解释文字、格式错误，SmartJSON自动处理：
- 去除 ````json` 和 ```` ``` ` 代码块标记
- 找到第一个 `[` 和最后一个 `]` 之间的内容（容错提取）
- 自动修复：尾随逗号、单引号→双引号、未加引号的key
- 失败时给出精确错误位置和修复建议

#### 3. 题目导入引擎（QuestionImporter）

- **SHA256去重**：基于题目文本计算哈希，重复题目自动跳过
- **字段校验**：检查必填字段（q/a/explain）、选项数量、答案有效性
- **自动标准化**：补全选项编号（A./B./C./D.）、规范化字段名
- **localStorage持久化**：导入的题目存储在`custom_questions`键中
- **即时反馈**：显示成功导入数量、跳过数量及原因

#### 4. QuizSystem改造

- `getAllQuestions()`：合并内置题库和自定义题目
- `refreshBank()`：导入新题后刷新当前练习
- `focusQuestions(qs, mode)`：聚焦到特定题目集（如刚导入的新题）
- `getDepth()/getWrongCount()/getWrongbook()/getUnmasteredConcepts()`：供提示词生成器读取学习状态

### 零摩擦体验设计

1. **双入口**：右下角悬浮FAB按钮 + 刷题区域内"AI出题助手"按钮
2. **智能默认值**：自动选择"薄弱知识点"范围、自动匹配难度、默认10题，零配置即可使用
3. **首次引导**：首次使用显示三步操作说明，之后记住偏好直接进入配置
4. **一键复制**：点击按钮自动复制提示词到剪贴板（navigator.clipboard → execCommand降级）
5. **AI快捷跳转**：复制后显示豆包/DeepSeek/Kimi/文心一言快捷入口，点击直达
6. **导入后即时练习**：导入成功后一键开始刷新题，自动聚焦新题集
7. **撒花庆祝**：导入成功触发celebrateConfetti()，给正向反馈
8. **打印时隐藏**：`@media print`中隐藏AI助手FAB和面板，不影响纸质输出

### CSS规范

AI助手CSS类名统一使用`ai-`前缀：
- `.ai-fab`：右下角悬浮按钮
- `.ai-panel-overlay`：半透明遮罩层
- `.ai-panel`：主面板（固定定位，居中显示）
- `.ai-step`：步骤页（默认隐藏，`.active`时显示）
- `.ai-step-indicator`：步骤进度点
- `.ai-config-option`：配置选项卡片（选中时高亮边框）
- `.ai-range-slider`：题目数量滑块
- `.ai-shortcut-btn`：AI工具快捷入口按钮
- `.ai-import-textarea`：粘贴导入文本域
- `.ai-import-status`：导入结果状态提示

### localStorage键命名

所有键使用统一前缀（SLUG + '_'）：
- `custom_questions`：用户导入的自定义题目数组
- `ai_onboarded`：是否已完成首次引导（'1'表示已引导）
- `ai_config`：记住用户上次的配置（range/count/difficulty/type）

### 生成课程页面时的AI注意事项

1. **核心题库保持精简**：内置题目控制在50-80题（平衡模式），覆盖核心考点即可，更多题目交给AI生成
2. **COURSE_META必须填写**：PromptGenerator依赖COURSE_META中的name/type/examFormat/chapters生成提示词
3. **章节名称要准确**：提示词中会包含章节信息，AI出题时会按章节分配题目
4. **题目格式统一**：内置题目遵循相同JSON格式，作为示例给AI参考
5. **不要省略AI助手模块**：所有生成的课程页面都必须包含AI出题助手，这是v4.0的核心功能

---

## v3.0 增强功能设计指南

### 术语悬停词典（TreeWalker智能替换）

构建课程核心术语表（50-100条），用TreeWalker扫描文本节点智能替换，鼠标悬停显示白话解释。

```javascript
const termDict = {
  '偏导数': '固定其他变量，只对一个变量求导——就像站在山坡上，只看东西方向的坡度',
  '梯度': '指向最陡上坡方向的箭头，方向导数取最大值的方向',
  // ...50-100条
};

function initTermTooltips() {
  // 用TreeWalker扫描所有文本节点，跳过.katex/.tooltip-term等已处理区域
  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: function(node) {
      if (node.parentElement.closest('.katex, .tooltip-term, script, style, textarea')) 
        return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });
  // 按术语长度降序替换（避免短词先匹配）
  var terms = Object.keys(termDict).sort((a,b) => b.length - a.length);
  // ...批量替换逻辑
}
```

**关键规则**：
- 每个术语在每个内容块内只标注一次（避免重复干扰）
- 明确跳过KaTeX渲染区域，防止公式内重复标注
- 术语表用白话写，长度控制在30-60字

### 划词摘录功能

页面任意位置选中文本（≥2字），弹出浮动"📌 加到一页纸"按钮：

```javascript
document.addEventListener('mouseup', function(e) {
  var sel = window.getSelection().toString().trim();
  if (sel.length >= 2) {
    showExcerptButton(sel, e.clientX, e.clientY);
  }
});
```

摘录自动保存到localStorage，渲染在考前一页纸底部"我的摘录"区，记录来源章节+时间戳。

### 填空题智能答案匹配

填空题答案不能做简单字符串比较，需实现`normalizeMathExpr()`和`generateEquivalentForms()`容错：

```javascript
function checkFillAnswer(userInput, correctAnswer) {
  var normalize = function(s) {
    return s.replace(/\s+/g,'').replace(/pi|π/gi,'π').replace(/\*/g,'')
            .replace(/[（）]/g,'()').toLowerCase();
  };
  var u = normalize(userInput);
  // 生成等价形式（如 1/2 = 0.5 = 2/4）
  var variants = generateEquivalentForms(correctAnswer);
  return variants.some(v => normalize(v) === u);
}
```

### 打印优化

#### 通用打印样式（`@media print`）
```css
@media print {
  .sticky-nav, .hero-actions, .depth-selector, .global-progress,
  .global-progress-label, .back-to-top, .toast, .confetti-piece,
  .qb-tabs, .qb-stats, .qb-nav, .btn, .flip-actions,
  .excerpt-btn, .micro-quiz-overlay, .hero-btn { display: none !important; }
  body { background: #fff !important; color: #000 !important; font-size: 11pt; }
  .card { box-shadow: none !important; border: none !important; break-inside: avoid; page-break-inside: avoid; }
  header.hero { background: #fff !important; color: #000 !important; padding: 10px 0 !important; }
}
```

#### 系统八：纸质输出与全场景陪伴（v3.1核心新增）

基于情境认知理论（Situated Cognition）和分布式认知（Distributed Cognition），学习不止发生在电脑屏幕前。纸张和手机是认知的延伸，必须作为一等公民设计。

**核心组件：一页纸专用打印模式**

在一页纸区域提供独立的橙红色"🖨️ 打印一页纸"按钮，区别于浏览器默认打印：

```javascript
function printCheatsheet(){
  document.body.classList.add('printing-cheatsheet');
  document.querySelectorAll('#cheatsheet .flip-card').forEach(function(c){ c.classList.add('flipped'); });
  setTimeout(function(){ window.print(); }, 200);
  var restore = function(){
    document.body.classList.remove('printing-cheatsheet');
    window.removeEventListener('afterprint', restore);
  };
  window.addEventListener('afterprint', restore);
  setTimeout(restore, 15000); // 兜底
}
```

```css
body.printing-cheatsheet > *:not(main) { display: none !important; }
body.printing-cheatsheet main > *:not(#cheatsheet) { display: none !important; }
body.printing-cheatsheet .flip-grid {
  grid-template-columns: 1fr 1fr !important; gap: 4mm !important;
}
body.printing-cheatsheet .flip-card { height: auto !important; break-inside: avoid; }
body.printing-cheatsheet .flip-inner { transform: none !important; }
body.printing-cheatsheet .flip-back {
  transform: none !important; display: block !important; position: static !important;
  border-top: 1px dashed #999 !important; margin-top: 3pt !important;
  font-size: 9.5pt !important; color: #333 !important;
}
body.printing-cheatsheet .flip-front {
  background: #f5f3ff !important; border: 1px solid #8b5cf6 !important;
}
```

**设计原则：**
1. 打印前自动展开所有翻转卡（答案全部显示）
2. 双列排版节省纸张（A4约可印60-80张卡）
3. 问题紫色背景，答案用虚线分隔，字号10pt左右
4. 隐藏所有交互元素（按钮、标记、操作栏）
5. 必须有恢复机制：`afterprint`事件+15秒setTimeout双保险

**移动端适配规范（候考速翻场景）：**

| 要素 | 规范 |
|------|------|
| 断点 | 768px/480px两档 |
| 正文最小字号 | 15px（不跟随系统缩小） |
| 触摸目标最小尺寸 | 44×44px |
| 导航形态 | 横向滚动pill，不加汉堡菜单 |
| 翻转卡 | 单列排列，高度自适应 |
| 回到顶部按钮 | 右下44px圆形 |
| 按钮padding | 不小于8px 14px |
| 打印模式双列 | 移动端打印仍保持双列（打印纸张是A4不受屏幕宽度影响） |

---

#### 系统九：知识点屏蔽（用户可自定义考试范围）

**问题场景**：老师划重点后部分知识点明确不考，用户需要快速屏蔽相关内容，避免复习不考的内容浪费时间。

**设计原则：**
1. **一键屏蔽**：悬停知识点标题时显示"🚫 不考"按钮，点击即屏蔽
2. **联动隐藏**：屏蔽后该知识点的概念精讲、例题、变式、配套小测、知识图谱节点、相关题库题目全部隐藏/灰化
3. **可视化反馈**：屏蔽后标题加删除线+半透明+🚫徽章+"↩️ 撤销"按钮，视觉明确
4. **集中管理**：Header有"🚫 不考项"按钮（带红色角标显示数量），打开模态框统一管理
5. **可恢复**：单个撤销或"恢复全部"，操作有Toast反馈
6. **进度修正**：被屏蔽的知识点不计入学习进度总数，知识图谱标记为🚫不考
7. **打印保留**：打印时被屏蔽内容恢复显示（打印作为全量备份）
8. **持久化**：localStorage存储，刷新页面后保持屏蔽状态

**HTML结构规范（AI必须遵守）：**

每个知识点的accordion-item必须：
- 添加 `data-topic-id="c{N}"` 属性（与knowledgeGraph中的id一致）
- accordion-header使用 `<div role="button" tabindex="0">` 而非 `<button>`（因为内部要嵌套屏蔽按钮，button不能嵌套button）
- 标题用 `<span class="accordion-title-wrap"><span class="accordion-title-text">标题</span></span>` 包裹
- 添加屏蔽按钮：`<button class="topic-exclude-btn" data-topic-id="c{N}" data-topic-name="知识点名称" onclick="event.stopPropagation();excludeTopic(this)">🚫 不考</button>`

```html
<div class="accordion-item" id="concept-ch1" data-topic-id="c1">
  <div class="accordion-header" role="button" tabindex="0">
    <span class="accordion-title-wrap">
      <span class="accordion-title-text">知识点名称</span>
    </span>
    <button class="topic-exclude-btn" data-topic-id="c1" data-topic-name="知识点名称"
            onclick="event.stopPropagation();excludeTopic(this)">🚫 不考</button>
    <span class="accordion-arrow">▼</span>
  </div>
  <div class="accordion-body">
    <!-- 知识点内容 -->
  </div>
</div>
```

**题库题目data属性规范：**

每道题库题目需要添加 `data-topic-ids` 属性，关联到一个或多个知识点id（逗号分隔），屏蔽知识点时相关题目自动隐藏：

```html
<div class="quiz-item" data-topic-ids="c1,c2" data-id="q1">
  <!-- 题目内容 -->
</div>
```

**knowledgeGraph数据无需额外修改**：系统自动从knowledgeGraph读取id/name/chapter/difficulty元数据。

**Header按钮位置：**在hero-actions中"🌙 夜间模式"按钮之后、"📄 一页纸"按钮之前添加：
```html
<button class="hero-btn exclude-manager-btn" id="excludeManagerBtn">
  🚫 不考项
  <span class="exclude-badge-count" id="excludeBadgeCount">0</span>
</button>
```

**屏蔽后的视觉效果：**
- accordion-item添加 `.excluded` 类
- opacity降为0.5，背景变灰，边框变虚线
- 标题文字加删除线变灰色
- 箭头隐藏，内容区强制不展开
- 显示🚫不考徽章和↩️撤销按钮
- hover无背景变化，cursor变为default
- 知识图谱对应节点显示🚫图标、半透明、删除线、去学习按钮隐藏、显示"(不考)"标签

**localStorage键名**：`{SLUG}_excluded_topics`，值为 `{topicId: {name, excludedAt}}` 对象。

---

### v3.1 标准组件库（可直接复制使用）

以下组件为v3.1必选/推荐标准组件，template.html中均有完整实现，AI生成时可直接参考。

#### 1. ScrollSpy 导航（必选）

```javascript
(function(){
  var navLinks = document.querySelectorAll('#stickyNav a');
  var sections = [];
  navLinks.forEach(function(a){
    var id = a.getAttribute('href').slice(1);
    var sec = document.getElementById(id);
    if(sec) sections.push({ id:id, el:sec, link:a });
  });
  function update(){
    var scrollY = window.scrollY + 120;
    var current = sections[0];
    for(var i=0;i<sections.length;i++){
      if(sections[i].el.offsetTop <= scrollY) current = sections[i];
    }
    navLinks.forEach(function(a){ a.classList.remove('active'); });
    if(current) current.link.classList.add('active');
  }
  window.addEventListener('scroll', update, { passive:true });
  update();
})();
```

当前项样式：`transform: scale(1.06)` + 紫蓝渐变背景 + 阴影 + 加粗。

#### 2. 回到顶部按钮（必选）

固定右下44px圆形按钮，滚动>400px淡入，点击平滑回顶。仅允许一个实例。

#### 3. 着陆高亮动效（必选）

```javascript
function scrollToSection(id){
  var el = document.getElementById(id);
  if(!el) return;
  var accordion = el.closest('.accordion-item');
  if(accordion && !accordion.classList.contains('open')) accordion.classList.add('open');
  el.classList.remove('section-highlight');
  void el.offsetWidth; // 触发reflow重启动画
  el.classList.add('section-highlight');
  el.scrollIntoView({ behavior:'smooth', block:'start' });
  setTimeout(function(){ el.classList.remove('section-highlight'); }, 2800);
}
```

所有跨模块跳转（知识图谱"去学习"、错题本"回看"、Toast"查看"）统一使用此函数。

#### 4. 可行动Toast（必选）

API升级为：`showToast(msg, duration, actionText, onAction)`。第三个参数为按钮文字，第四个为点击回调。例如：
```javascript
showToast('📌 已加入一页纸', 2500, '查看', function(){ scrollToSection('cheatsheet'); });
```

#### 5. 撒花庆祝（必选）

`celebrateConfetti()`：40片6色纸屑（紫/蓝/绿/橙/红/粉），从屏幕顶部随机位置下落，1.5-3秒，旋转720度。触发时机：答对微检测、答对题库选择题、诊断完成、考试得分≥75分、标记全部掌握。

#### 6. 划词摘录（推荐）

选中≥2字文字时就近弹出"📌 加到一页纸"浮动按钮，点击后：加入摘录列表、记录来源章节+时间戳、弹出可行动Toast、点击Toast跳转一页纸。

#### 7. 回到顶部（必选）

右下圆形按钮，滚动>400px显示，点击平滑回顶，z-index=400。

#### 8. 错因分类弹窗（必选）

答错后立即弹出错因选择模态框，6类错因（概念误解🧠/公式记错📐/计算失误🧮/方法选错🔀/审题失误👁️/前置薄弱🔗），点击外部或"暂不分类"自动归类为"未分类"。确认后Toast带"查看"按钮跳转错题本。

```javascript
// 调用方式
showErrorReasonModal(questionObject);
// 6类错因定义
var errorCategories = [
  { key:'concept', label:'概念误解', color:'#3b82f6' },
  { key:'formula', label:'公式记错', color:'#8b5cf6' },
  { key:'calc', label:'计算失误', color:'#f59e0b' },
  { key:'method', label:'方法选错', color:'#ef4444' },
  { key:'read', label:'审题失误', color:'#6b7280' },
  { key:'prereq', label:'前置薄弱', color:'#eab308' }
];
```

错题本区域必须包含：①三格统计卡（错题总数/已归类/主要错因）②分类分布柱状条（wb-cat-bar）③每题错因标签（可点击切换）④"回看知识点"补救按钮⑤"已掌握移除"按钮。

#### 9. 间隔重复引擎SRS（推荐）

类Anki的SM-2简化算法，6级间隔（0/1/3/7/15/30天），翻转卡标记✓时升级间隔并显示下次复习时间，标记🔄时降级。一页纸标题旁显示待复习徽章。

```javascript
SRSystem.markReview(cardId, remembered); // 标记复习结果
SRSystem.getDueCount(); // 获取待复习卡片数
SRSystem.updateDueBadge(); // 更新一页纸标题徽章
SRSystem.SR_INTERVALS; // [0,1,3,7,15,30]
```

#### 10. 考试计时器（必选）

进入考试模式自动启动20分钟倒计时，>3分钟变黄色警告（pulse动画），≤1分钟变红色危险。考完自动停止。

```javascript
ExamTimer.start(20); // 启动20分钟计时
ExamTimer.stop();    // 停止并隐藏
```

#### 11. Canvas几何可视化（推荐·计算型课程必选）

提供4个现成Canvas动画组件，AI直接调用即可。仅在`data-depth="advanced"`冲刺档显示。

```javascript
// 黎曼和（积分分割可视化）
var rs = CanvasViz.riemannSum(canvasEl, { n: 10, fn: function(x){return Math.sin(x*2)+1.5;} });
rs.setN(30); // 调整分割数
// 极坐标分割
var pa = CanvasViz.polarArea(canvasEl);
pa.setSectors(16);
// 旋转曲面动画
var rot = CanvasViz.rotationSurface(canvasEl);
rot.play(); rot.stop();
// 向量场
CanvasViz.vectorField(canvasEl);
```

所有Canvas组件已处理devicePixelRatio高分屏问题，支持鼠标拖拽（cursor:grab/grabbing）。

#### 12. 术语悬停词典（推荐）

自动为专业术语添加虚线下划线和hover解释tooltip。

```javascript
TermDictionary.add('导数', '函数在某点的瞬时变化率，即切线斜率');
TermDictionary.add('偏导数', '多元函数固定其他变量对单一变量求导');
TermDictionary.annotate(); // 自动扫描DOM标注术语
```

TreeWalker自动跳过`.katex`、`button`、`a`、`.term`区域，避免重复标注。

#### 13. 进度导入/导出（必选）

考前清单区域折叠面板中提供三个按钮：导出JSON、导入JSON、重置全部进度。导出包含apState/diagResults/wrongbook/srs/checks/flipMarks/dark/depth/excerpts及版本号。

#### 14. 移动端底部导航（必选）

≤768px隐藏顶部sticky-nav，显示底部5个tab（新手/路径/一页纸/刷题/错题），带图标+文字，独立ScrollSpy高亮当前项。

### Canvas几何可视化补充说明（冲刺档专属）

CanvasViz组件库已内置4种可视化（黎曼和/极坐标分割/旋转曲面/向量场），对依赖空间想象的课程（高数、物理等）应在冲刺档（`data-depth="advanced"`）使用。

**关键原则**：Canvas可视化是可选增强，不影响基础档性能，KaTeX加载失败不影响文字内容阅读。新增Canvas组件必须处理devicePixelRatio，否则高分屏模糊。

### 随机抽测功能

在考前一页纸区域，"🎲 随机抽测5题"按钮从题库随机抽取5道题现场自测，模拟考前押题感。

---

## 课程类型差异化设计指南（v2.1继承+增强）

### 何时启用差异化设计

当课程具备以下**任一特征**时，启用差异化设计：

| 特征 | 示例课程 | 差异化设计 |
|------|---------|-----------|
| 大量数学公式和符号运算 | 高数、线代、概率论 | KaTeX渲染+公式速查+计算陷阱库 |
| 强依赖空间想象 | 解析几何、电磁学 | Canvas几何可视化+几何直观优先 |
| 计算链式递进 | 高数、物理 | 计算依赖树+阻塞点预警+微检测门控 |
| 存在统一性主线 | 高数（三大公式） | 统一性主线对比表 |
| 多种方法/坐标系选择 | 高数（积分方法选择） | 方法决策树 |

### 费曼四步法的课程类型适配

| 费曼步骤 | 概念型课程（标准费曼） | 计算型课程（差异化） | 实践型课程 |
|----------|---------------------|---------------------|-----------|
| ① 简单解释 | 白话版（日常语言） | 几何直观优先，辅以白话 | 代码/操作演示 |
| ② 建立直觉 | 生活场景类比 | 数学类比（低维→高维） | 动手实践类比 |
| ③ 暴露盲区 | 概念理解误区 | 计算操作陷阱 | 常见bug/坑 |
| ④ 压缩记忆 | 速记口诀 | 口诀+统一性主线 | 代码片段/模板 |

### 计算型课程六大设计原则（v2.1继承）

1. **公式渲染基础设施**：KaTeX 0.16.9，`strict:false`容错
2. **几何直观优先**：用图形/动画建立直觉，替代白话
3. **计算依赖链+阻塞预警**：红色标注"算不对就全废"的阻塞点
4. **找统一性主线**：识别贯穿全书的统一思想
5. **分步交互**：遮挡式做题+hint脚手架+即时校验
6. **知识盲区诊断**：开篇先测，精准补漏

---

## 参考材料使用指南（v2.2继承）

### 各类参考材料的使用方法

| 参考材料类型 | 价值 | 如何使用 |
|-------------|------|---------|
| 往年试卷/期末卷 | **最高** | 提取原题入题库；分析考点分布调整章节权重；模仿出题风格；标注"📌 往年试卷" |
| 平时作业/练习题 | 高 | 提取典型题；识别高频考点；标注"📌 平时作业" |
| 上课课件/PPT | 中高 | 校准知识点范围；识别老师强调内容；标注"📌 课件强调" |
| 教学大纲/考试范围 | 高 | 精准划定复习边界；删除不考内容 |
| 教材课后习题 | 中 | 补充基础练习题 |

### 页面来源标注系统

所有内容必须通过视觉徽章标注来源，让用户清楚知道哪些是真题风格、哪些是AI推测。

```css
.exam-source-badge.past-exam { background: #fef3c7; color: #92400e; }  /* 黄色：往年试卷 */
.exam-source-badge.courseware { background: #dbeafe; color: #1e40af; } /* 蓝色：课件 */
.exam-source-badge.ai-generated { background: #f3f4f6; color: #6b7280; } /* 灰色：AI生成 */
```

无参考材料时，在新手引导区之前添加全局琥珀色警告框。

---

## 例题驱动设计指南（v2.3继承+增强）

### 例题卡片标准七段式结构（v3.0增强：+遮挡结果+配套小测）

每道例题严格遵循以下结构：

```
┌─────────────────────────────────────┐
│  例题标题 + 来源/分值标签（紫蓝渐变头）│  ← example-header
├─────────────────────────────────────┤
│  📝 题目内容（琥珀色左边框）          │  ← ex-problem
├─────────────────────────────────────┤
│  💡 怎么想到的？（蓝色左边框）        │  ← ex-thinking（元认知层，最关键）
├─────────────────────────────────────┤
│  ① 第一步...（编号圆点）             │
│     → 结果高亮（绿色，遮挡模式隐藏）   │  ← ex-steps + ex-step-result.hidden
│  ② 第二步...                        │
├─────────────────────────────────────┤
│  📚 从题目学到的（紫蓝渐变边框）      │  ← ex-knowledge（知识提炼）
├─────────────────────────────────────┤
│  🔄 变式练习（蓝色虚线框，折叠）      │  ← ex-variant
├─────────────────────────────────────┤
│  📝 配套小测2-3题（绿色主题，折叠）   │  ← ex-practice（每题答案独立折叠）
└─────────────────────────────────────┘
```

### 「怎么想到的」写作要求（灵魂部分）

不能直接给答案，要讲清楚"为什么想到这个方法"：
- 从**题目特征信号**出发：看到 $x^2+y^2$ → 极坐标！
- 从**排除法**出发：为什么不用直角坐标？
- 从**目标倒推**：要求的结果需要什么条件？

**好的思路引导**：
> 积分区域是圆 + 被积函数含 $x^2+y^2$ → 极坐标！别忘了乘 $r$。

**差的思路引导**（等于没说）：
> 用极坐标计算。

### 变式练习四层次

| 层次 | 变式方式 | 检验什么 |
|------|---------|---------|
| 1级 | 改变数字 | 是否自己算的 |
| 2级 | 改变条件 | 方法是否真掌握 |
| 3级 | 反向提问 | 理解深度够不够 |
| 4级 | 综合提升 | 知识迁移能力 |

### 配套小测设计原则（v2.4）

- 紧扣例题知识点
- 2-3道：第1题基础（直接套用），第2题变形，第3题（可选）综合
- 每题答案独立折叠，做完一道看一道
- 详解不跳步

---

## 知识关系图设计指南

### 八种知识关系类型

| 关系类型 | 视觉 | 适用场景 |
|---------|------|---------|
| 因果关系 | A →(导致)→ B | 经济学、物理 |
| 前提依赖 | A →(prerequisite)→ B | 数学、编程 |
| 对比关系 | A ⟷(对比)⟷ B | 任何有对立概念 |
| 递进关系 | A→B→C（简单→复杂） | 数学、编程 |
| 总分关系 | A ⊃ B,C,D | 任何有层级结构 |
| 应用关系 | A →(应用)→ B | 理论+应用 |
| 循环反馈 | A→B→A（循环） | 经济学、生态学 |
| 计算阻塞 | A →(算不对全废)→ B | 计算型课程（红色标注） |

**注意**：计算型课程应使用"计算依赖树"替代概念关系图。

---

## 视觉设计系统

### 色彩体系v3.0

采用**紫色（#7c3aed）为主色、蓝色（#2563eb）为辅色**的现代化配色：

```css
:root {
  --primary: #7c3aed;     /* 主色：紫色（知识/智慧） */
  --primary-light: #ede9fe;
  --accent: #2563eb;      /* 辅色：蓝色 */
  --text: #111827;
  --muted: #6b7280;
  --bg: #f3f4f6;
  --card: #ffffff;
  --border: #e5e7eb;
  --success: #16a34a;
  --warning: #f59e0b;
  --danger: #dc2626;
  --shadow: 0 12px 30px rgba(15,23,42,0.08);
}

/* 暗黑模式完整双套变量 */
body.dark {
  --primary: #a78bfa;
  --primary-light: #4c1d95;
  --bg: #0f172a;
  --card: #111827;
  --border: #334155;
  --shadow: 0 12px 30px rgba(0,0,0,0.28);
}
```

### 语义化信息块配色

| 块类型 | 左边框色 | 语义 |
|--------|---------|------|
| `.key-point` | 琥珀色 | 核心要点/关键提醒 |
| `.geo-intuition` | 绿色 | 几何直观解释 |
| `.plain-explain` | 绿色 | 通俗白话解释 |
| `.common-mistake` | 红色 | 常见错误/计算陷阱 |
| `.formula-box` | 紫色主题 | 核心公式居中展示 |
| `.ex-problem` | 琥珀色 | 题目呈现 |
| `.ex-thinking` | 蓝色 | 思路引导 |
| `.ex-knowledge` | 紫蓝渐变边框 | 知识提炼 |

### 卡片化设计

- 大圆角：`border-radius: 22px`（大卡片）/ `18px`/`14px`/`999px`（药丸按钮）
- 柔和阴影：`0 12px 30px rgba(15,23,42,0.08)`
- 嵌套层次分明：card → example-card → 内部子块

### 难度三色徽章

| 徽章类 | 颜色 | 含义 |
|--------|------|------|
| `.badge-easy` | 绿色 | 零基础可看 |
| `.badge-medium` | 黄色 | 需要理解前置 |
| `.badge-hard` | 红色 | 重点难点 |

### 响应式与打印

- 三断点：>900px多列 / 720-900px压缩 / <720px单列
- `clamp()`响应式字号
- Sticky导航横向滚动
- `@media print`打印优化 + 一页纸专用打印模式

---

## 技术实现参考

### 文件结构

```
course-review-skill/
├── SKILL.md                # TRAE格式（本文件，v3.1）
├── AGENTS.md               # 跨平台标准格式
├── CLAUDE.md               # Claude Code格式
├── .cursorrules            # Cursor格式
├── .windsurfrules          # Windsurf格式
├── .clinerules/course-review.md  # Cline格式
├── skill.json              # Skill配置v3.1
├── README.md               # 人类可读文档v3.1
├── template.html           # 参考模板v3.1（含14个标准组件+4个Canvas可视化）
├── assets/js/quiz.js       # 题库系统参考实现（已整合进template.html）
└── examples/
    ├── data-structure.html # 数据结构示例
    └── calculus2.html      # 高数2完整示例（含Canvas+术语词典+SRS）
```

### KaTeX集成（v3.1增强：含化学mhchem扩展）

> **重要**：数学/物理/化学课程必须使用以下增强配置，确保所有符号正确显示。

```html
<!-- KaTeX 核心 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<!-- 化学方程式扩展（mhchem）——化学/生化课程必加，其他课程可选加（仅增加~15KB） -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<!-- 物理单位扩展（physics）——物理课程推荐 -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/physics.min.js"></script>

<script>
// KaTeX就绪检测
var katexReady = false;
function renderMath(root){
  root = root || document.body;
  if(typeof renderMathInElement !== 'undefined'){
    try {
      renderMathInElement(root, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false},
          {left: '\\(', right: '\\)', display: false},
          {left: '\\[', right: '\\]', display: true}
        ],
        throwOnError: false,
        strict: false,
        trust: true,
        // 化学扩展支持
        macros: {
          // 常用物理符号快捷命令
          "\\v": "\\mathbf{#1}",
          "\\unit": "\\,\\text{#1}",
          "\\const": "\\text{#1}",
          // 常用化学快捷
          "\\chem": "\\ce{#1}"
        }
      });
      katexReady = true;
    } catch(e) {
      console.warn('KaTeX渲染异常:', e);
    }
  }
}
// DOMContentLoaded + load双保险；动态内容更新后重渲染
document.addEventListener('DOMContentLoaded', function(){ setTimeout(function(){ renderMath(); }, 300); });
window.addEventListener('load', function(){ setTimeout(function(){ renderMath(); }, 500); });
// 兜底：CDN加载慢时延迟重试
setTimeout(function(){ if(!katexReady) renderMath(); }, 1500);
setTimeout(function(){ if(!katexReady) renderMath(); }, 3000);
</script>
```

**扩展加载说明**：
- `mhchem.min.js`：化学方程式/化学式渲染，使用 `$\ce{H2O}$`、`$\ce{2H2 + O2 -> 2H2O}$` 语法
- `physics.min.js`：物理常用符号（矢量、微分、bra-ket等），提供 `\vb`、`\dd`、`\pdv` 等快捷命令
- 所有扩展均为CDN加载失败时不影响基础数学符号渲染（优雅降级）

### 数学/物理/化学符号完整写法参考

> **核心原则**：所有数学/物理/化学公式、符号、单位必须放在 `$...$`（行内）或 `$$...$$`（块级）中，**禁止**直接用Unicode特殊字符（如 ∂、∫、∑、α、β、→ 等在正文非数学环境中可能无法正确显示）。

#### 一、数学符号速查表

| 符号 | 错误写法 | ✅ 正确LaTeX写法 | 说明 |
|------|---------|-----------------|------|
| 希腊字母α | α | `$\alpha$` | 不要直接打Unicode字符α |
| 希腊字母β | β | `$\beta$` | |
| 希腊字母π | π | `$\pi$` | 圆周率 |
| 希腊字母θ | θ | `$\theta$` | 角度 |
| 希腊字母λ | λ | `$\lambda$` | 波长/特征值 |
| 希腊字母μ | μ | `$\mu$` | 微/均值 |
| 希腊字母σ | σ | `$\sigma$` | 标准差/求和小写 |
| 大写希腊字母Σ | Σ | `$\Sigma$` | 求和 |
| 大写希腊字母Ω | Ω | `$\Omega$` | 欧姆/样本空间 |
| 大写希腊字母Δ | Δ | `$\Delta$` | 增量/判别式 |
| 无穷大 | ∞ | `$\infty$` | |
| 偏导数∂ | ∂ | `$\partial$` | 或用physics扩展的 `$\pdv{f}{x}$` |
| 积分∫ | ∫ | `$\int$` | 定积分：`$\int_a^b f(x)\,dx$` |
| 求和∑ | ∑ | `$\sum$` | `$\sum_{i=1}^n a_i$` |
| 极限 | lim | `$\lim$` | `$\lim_{x \to 0}$` |
| 箭头→ | → | `$\to$` 或 `$\rightarrow$` | |
| 双箭头⇒ | ⇒ | `$\Rightarrow$` | 推出 |
| 等价⇔ | ⇔ | `$\Leftrightarrow$` | |
| 不等于≠ | ≠ | `$\neq$` | |
| 约等于≈ | ≈ | `$\approx$` | |
| 小于等于≤ | ≤ | `$\leq$` 或 `$\le$` | |
| 大于等于≥ | ≥ | `$\geq$` 或 `$\ge$` | |
| 乘号× | × | `$\times$` | 叉乘/乘法 |
| 点乘· | · | `$\cdot$` | 点积/乘法 |
| 除号÷ | ÷ | `$\div$` | |
| 分数 | a/b | `$\frac{a}{b}$` 或 `$\dfrac{a}{b}$` | dfrac是显示风格更大 |
| 上标 | x^2 | `$x^2$` | 多字符要加花括号：`$x^{10}$` |
| 下标 | x_i | `$x_i$` | 多字符：`$x_{ij}$` |
| 根号√ | √x | `$\sqrt{x}$` | n次根：`$\sqrt[n]{x}$` |
| 绝对值 | |x| | `$|x|$` 或 `$\left|x\right|$` |
| 向量 | v | `$\vec{v}$` 或 `$\mathbf{v}$` | 物理推荐用 `$\vb{v}$`（需physics扩展） |
| hat | â | `$\hat{a}$` | 单位向量/估计量 |
| 平均值 | ā | `$\bar{a}$` | |
| 度° | ° | `$^\circ$` | 角度：`$30^\circ$` |
| 摄氏度 | ℃ | `$^\circ\text{C}$` | 不要直接打℃字符 |
| 上下标同时 |  | `$x_i^2$` 或 `${x_i}^2$` | |
| 括号 | ( ) | `$\left( \right)$` | 自动调整大小的括号 |
| 方括号 | [ ] | `$\left[ \right]$` | |
| 花括号 | { } | `$\left\{ \right\}$` | 花括号需要转义 |
| 行列式/矩阵 |  | `$\begin{vmatrix} a&b\\c&d \end{vmatrix}$` | |
| 矩阵 |  | `$\begin{pmatrix} a&b\\c&d \end{pmatrix}$` | |
| 省略号... | ... | `$\cdots$`（居中）/ `$\ldots$`（基线）/ `$\vdots$`（竖） | |
| 因为 | ∵ | `$\because$` | |
| 所以 | ∴ | `$\therefore$` | |
| 存在 | ∃ | `$\exists$` | |
| 任意 | ∀ | `$\forall$` | |
| 属于 | ∈ | `$\in$` | |
| 不属于 | ∉ | `$\notin$` | |
| 子集 | ⊂ | `$\subset$` | |
| 真子集 | ⊆ | `$\subseteq$` | |
| 并集 | ∪ | `$\cup$` | |
| 交集 | ∩ | `$\cap$` | |
| 空集 | ∅ | `$\emptyset$` | |
| 实数集 | ℝ | `$\mathbb{R}$` | |
| 自然数集 | ℕ | `$\mathbb{N}$` | |
| 整数集 | ℤ | `$\mathbb{Z}$` | |
| 分式(大) |  | `$\dfrac{dy}{dx}$` | display风格分数 |
| 二项式系数 |  | `$\binom{n}{k}$` | |

#### 二、物理符号写法

| 符号 | ✅ 正确LaTeX写法 | 说明 |
|------|-----------------|------|
| 矢量（粗体） | `$\vb{F}$` | 需physics扩展，或用 `$\mathbf{F}$` |
| 矢量（箭头） | `$\vec{v}$` | |
| 单位矢量 | `$\hat{\imath}$`、`$\hat{\jmath}$`、`$\hat{k}$` | |
| 速度 | `$\vec{v}$` 或 `$\vb{v}$` | |
| 加速度 | `$\vec{a}$` 或 `$\vb{a}$` | |
| 力 | `$\vb{F}$` | |
| 电场 | `$\vb{E}$` | |
| 磁场 | `$\vb{B}$` | |
| 微分d | `$\dd{x}$` | physics扩展，直立即是 `$dx$` |
| 一阶导数 | `$\dv{y}{x}$` | physics扩展：dy/dx |
| 二阶导数 | `$\dv[2]{y}{x}$` | physics扩展：d²y/dx² |
| 偏导数 | `$\pdv{f}{x}$` | physics扩展：∂f/∂x |
| 二阶偏导 | `$\pdv[2]{f}{x}$` | physics扩展：∂²f/∂x² |
| 混合偏导 | `$\pdv{f}{x}{y}$` | physics扩展：∂²f/∂x∂y |
| 梯度 | `$\nabla f$` | 或 `$\grad f$`（physics扩展） |
| 散度 | `$\nabla \cdot \vb{F}$` | 或 `$\div \vb{F}$` |
| 旋度 | `$\nabla \times \vb{F}$` | 或 `$\curl \vb{F}$` |
| 拉普拉斯 | `$\nabla^2 f$` | |
| 点积 | `$\vb{a} \cdot \vb{b}$` | |
| 叉积 | `$\vb{a} \times \vb{b}$` | |
|  bra | `$\bra{\psi}$` | physics扩展：左矢 |
|  ket | `$\ket{\psi}$` | physics扩展：右矢 |
| bra-ket | `$\braket{\phi|\psi}$` | physics扩展：内积 |
| 单位（正体） | `$5\,\text{m/s}$` | 单位必须用\text{}包起来并加小空格\, |
| 牛顿N | `$F = 10\,\text{N}$` | |
| 焦耳J | `$E = 100\,\text{J}$` | |
| 帕斯卡Pa | `$P = 1.013\times10^5\,\text{Pa}$` | |
| 电子伏特 | `$E = 13.6\,\text{eV}$` | |
| 米每秒 | `$v = 3\times10^8\,\text{m/s}$` | |
| 千克 | `$m = 5\,\text{kg}$` | |
| 摩尔 | `$n = 2\,\text{mol}$` | |
| 开尔文 | `$T = 300\,\text{K}$` | |
| 安培 | `$I = 2\,\text{A}$` | |
| 伏特 | `$U = 220\,\text{V}$` | |
| 欧姆 | `$R = 10\,\Omega$` | |
| 法拉 | `$C = 10\,\mu\text{F}$` | 注意μ用 `$\mu$`，F用\text{F} |
| 亨利 | `$L = 5\,\text{mH}$` | |
| 赫兹 | `$f = 50\,\text{Hz}$` | |
| 瓦特 | `$P = 1000\,\text{W}$` | |
| 库仑 | `$Q = 1.6\times10^{-19}\,\text{C}$` | |
| 特斯拉 | `$B = 1\,\text{T}$` | |
| 韦伯 | `$\Phi = 1\,\text{Wb}$` | |
| 普朗克常数 | `$h = 6.626\times10^{-34}\,\text{J·s}$` | J·s 中间用\text{·}或\cdot |
| 约化普朗克常数 | `$\hbar = 1.05\times10^{-34}\,\text{J·s}$` | |
| 光速 | `$c = 3\times10^8\,\text{m/s}$` | |
| 真空介电常数 | `$\varepsilon_0$` | |
| 真空磁导率 | `$\mu_0$` | |
| 玻尔兹曼常数 | `$k_B$` | |
| 阿伏伽德罗常数 | `$N_A$` | |

**物理单位书写规则**：
1. 物理量符号用斜体（默认数学模式），单位用正体 `\text{}`
2. 数字与单位之间必须有小空格：`\` （反斜杠加空格）或 `\,`
3. 复合单位用 `/` 或 `\cdot` 连接：`$\text{m/s}$` 或 `$\text{m} \cdot \text{s}^{-1}$`
4. 词头（μ、m、k、M、G等）与单位连写：`$\mu\text{m}$`（微米）、`$\text{keV}$`（千电子伏）

#### 三、化学符号写法（需mhchem扩展）

> 加载 `mhchem.min.js` 后，使用 `$\ce{...}$` 语法自动渲染化学式和方程式。

| 化学式/方程式 | ✅ 正确写法 | 说明 |
|--------------|-----------|------|
| 水 | `$\ce{H2O}$` | 自动下标 |
| 硫酸 | `$\ce{H2SO4}$` | |
| 氢氧化钠 | `$\ce{NaOH}$` | |
| 二氧化碳 | `$\ce{CO2}$` | |
| 铁离子 | `$\ce{Fe^3+}$` | 上标电荷 |
| 硫酸根 | `$\ce{SO4^2-}$` | |
| 铵根 | `$\ce{NH4+}$` | |
| 水合氢离子 | `$\ce{H3O+}$` | |
| 同位素碳14 | `$\ce{^{14}C}$` | 质量数左上标 |
| 铀235 | `$\ce{^{235}_{92}U}$` | 质量数+原子序数 |
| 化学键单键 | `$\ce{CH3-CH3}$` | 单键 |
| 双键 | `$\ce{CH2=CH2}$` | 双键 |
| 三键 | `$\ce{HC#CH}$` | 三键（#符号） |
| 配位键 | `$\ce{[Cu(NH3)4]^2+}$` | 配合物 |
| 反应箭头 | `$\ce{A -> B}$` | 反应箭头 |
| 可逆反应 | `$\ce{A <=> B}$` | 可逆箭头 |
| 平衡反应 | `$\ce{A <--> B}$` | 平衡箭头 |
| 逆反应 | `$\ce{A <- B}$` | 逆反应箭头 |
| 反应条件上 | `$\ce{A ->[H2O] B}$` | 反应条件在箭头上 |
| 反应条件上下 | `$\ce{A ->[催化剂][\Delta] B}$` | 上下都有条件 |
| 加热符号Δ | `$\ce{A ->[\Delta] B}$` | |
| 化学方程式 | `$\ce{2H2 + O2 -> 2H2O}$` | 自动配平系数 |
| 中和反应 | `$\ce{HCl + NaOH -> NaCl + H2O}$` | |
| 合成氨 | `$\ce{N2 + 3H2 <=>[高温高压][催化剂] 2NH3}$` | |
| 氧化还原电子转移 | `$\ce{2Na + Cl2 -> 2NaCl}$` | （可配合上下标说明） |
| 沉淀符号↓ | `$\ce{CaCO3 v}$` | 沉淀 |
| 气体符号↑ | `$\ce{CO2 ^}$` | 气体 |
| 摩尔浓度 | `$\ce{1 M HCl}$` | |
| 物质的量 | `$n = 2\,\text{mol}$` | mol用\text{mol} |
| 浓度 | `$c = 0.1\,\text{mol/L}$` | |
| pH值 | `$\text{pH} = 7$` | pH正体 |
| 反应速率 | `$v = 0.5\,\text{mol/(L·s)}$` | |
| 平衡常数 | `$K_c$` 或 `$K_\text{eq}$` | |
| 焓变 | `$\Delta H = -286\,\text{kJ/mol}$` | Δ是 `$\Delta$` |
| 熵变 | `$\Delta S$` | |
| 吉布斯自由能 | `$\Delta G = \Delta H - T\Delta S$` | |
| 活化能 | `$E_a$` | |
| 化学元素符号 | 在正文也可直接写H、O、C、Fe | 单字母/双字母元素符号作为普通文本即可，但化学式必须用 `$\ce{}$` |
| 有机化学苯环 | `$\ce{C6H6}$` 或用chemfig包（KaTeX不支持chemfig，建议用文字描述或插入图片） | |

**化学符号注意事项**：
1. 化学式中的数字（下标）不需要手动写 `_`，mhchem 自动处理
2. 电荷用 `^+`、`^2+`、`^-`、`^2-` 即可
3. 反应箭头不要用 `->`（C语言指针），必须在 `$\ce{}$` 内用 `->` mhchem会渲染为化学箭头
4. 不加载mhchem扩展时，`$\ce{}$` 命令不会报错但会原样显示，建议始终加载mhchem
5. 状态标注（s/l/g/aq）：`$\ce{H2O(l)}$`、`$\ce{CO2(g)}$`、`$\ce{NaCl(aq)}$`、`$\ce{Fe(s)}$`

#### 四、常见符号渲染问题排查

| 问题现象 | 原因 | ✅ 解决方案 |
|---------|------|-----------|
| 希腊字母显示为方框/乱码 | 直接打了Unicode字符 | 全部改用LaTeX命令如 `$\alpha$` |
| 公式不渲染，显示原始$...$ | KaTeX CDN未加载完成 | 已配置300ms/500ms/1.5s/3s四重渲染兜底 |
| 化学式显示`$\ce{H2O}$`原样 | 未加载mhchem扩展 | 添加 `mhchem.min.js` script标签 |
| 单位显示为斜体 | 未用\text{}包裹 | 单位写为 `$\text{m/s}$` |
| 箭头显示为`->`字符 | 直接打了-> | 在数学模式用 `$\to$` 或化学用 `$\ce{->}$` |
| 中文出现在公式中报错 | KaTeX数学模式不支持中文 | 中文放在数学模式外，或用 `\text{中文}` 包裹 |
| 括号太小不包裹内容 | 直接用了() | 用 `$\left( ... \right)$` 自动调整大小 |
| 下标/上标只显示一个字符 | 没加花括号 | 多字符必须用 `x_{ij}`、`x^{10}` |
| 花括号{}不显示 | 花括号在LaTeX中有特殊含义 | 用 `$\{$` 和 `$\}$` 或 `$\left\{ ... \right\}$` |
| 度符号℃显示异常 | 直接打了Unicode℃ | 写为 `$^\circ\text{C}$` |
| 物理矢量不是粗体 | 直接打了字母 | 用 `$\vb{F}$`（需physics扩展）或 `$\mathbf{F}$` |
| 省略号位置不对 | 直接打了三个点 | 用 `$\cdots$`（居中）或 `$\ldots$`（基线） |

#### 五、符号使用红线（必须遵守）

1. **禁止**在正文/选项/标题中直接使用Unicode数学符号：∂、∫、∑、√、∞、≠、≈、≤、≥、×、→、⇒、∵、∴、∃、∀、∈、⊂、∪、∩、α、β、γ、δ、ε、θ、λ、μ、π、σ、φ、ψ、ω、Δ、Σ、Ω、℃、°、²、³
2. 以上所有符号**必须**放在 `$...$` 内使用对应的LaTeX命令
3. 正文叙述中"如果x>0"这种不等式，x和>也应放数学模式：`如果 $x > 0$`
4. 数字与单位组合必须是 `$5\,\text{cm}$` 格式，禁止直接写"5cm"在技术语境中
5. 化学课程必须加载mhchem扩展，所有化学式/方程式用 `$\ce{}$` 语法
6. 物理课程推荐加载physics扩展简化矢量/微分书写
7. KaTeX渲染失败时不影响页面阅读——CDN加载失败时公式降级为原始LaTeX文本，用户仍可读懂

### 代码生成避坑指南（最高优先级 · 28条常见坑）

> **警告**：AI生成JavaScript代码时极易引入语法错误。严格遵守：

1. **字符串统一单引号**：题库数据中所有字符串用单引号包裹，内部安全使用中文双引号
2. **KaTeX数学模式禁中文**：`\text{收敛}`会触发警告，改为中文在数学模式外
3. **strict:false配置**：务必加上容忍边缘情况
4. **动态内容后重渲染**：手风琴展开、错题渲染后调用`setTimeout(renderMath, 50-120)`
5. **术语替换跳过KaTeX**：TreeWalker明确跳过`.katex`区域
6. **IIFE模块化**：每个功能块用独立IIFE包裹，避免全局污染
7. **函数劫持扩展**：新增功能用Monkey Patching包裹原函数，不破坏已有逻辑
8. **跨模块跳转统一用scrollToSection**：不直接scrollIntoView，要带着陆高亮和父级手风琴展开
9. **Toast带行动按钮**：状态变化通知必须提供下一步操作（查看/跳转/撤销），使用`showToast(msg, duration, actionText, onAction)`
10. **打印必须双保险恢复**：同时监听`afterprint`事件和15秒setTimeout兜底，避免用户取消打印后页面卡在打印模式
11. **仅允许一个回到顶部按钮**：生成前检查DOM，避免重复ID`backToTop`
12. **移动端正文≥15px**：防止iOS Safari自动缩放，所有触摸目标≥44×44px
13. **3D transform翻转卡z-index隔离**：`.flip-card { perspective: 1000px; transform-style: preserve-3d; }`必须在父级设置，否则Safari翻转失效
14. **localStorage必须加前缀**：使用`LS(key)`函数（基于`SLUG`），避免同域下多课程数据互相污染
15. **localStorage读写try-catch包裹**：隐私模式下localStorage可能抛异常，必须lsGet/lsSet统一封装
16. **Canvas必须处理devicePixelRatio**：高分屏模糊问题，`canvas.width = offsetWidth * dpr`后必须`ctx.scale(dpr, dpr)`
17. **Canvas仅在冲刺档加载**：用`body[data-depth="advanced"]`守卫，基础档不加载Canvas避免性能损耗
18. **事件委托优于逐个绑定**：动态生成的选项按钮使用事件委托或在render时绑定，避免内存泄漏
19. **setTimeout/setInterval必须清理**：计时器在模块停止/切换时clearInterval，如ExamTimer.stop()
20. **错题去重**：addToWrongbook前检查是否已存在同一id的错题，避免重复
21. **错因分类emoji映射**：使用`getReasonEmoji(key)`函数统一管理，不要硬编码
22. **移动端底部导航与顶部sticky-nav互斥**：≤768px显示`.mobile-bottom-nav`隐藏`.sticky-nav`，避免双重导航
23. **进度导出必须包含版本号**：JSON中加`_version`字段，导入时可做兼容性处理
24. **撒花动画数量控制**：`celebrateConfetti()`每次40片，上限50片，避免低端机卡顿
25. **IIFE结尾分号**：每个IIFE结束后必须加`;`，防止与后续代码拼接时报错
26. **术语词典TreeWalker跳过表单元素**：`acceptNode`必须跳过`label, input, textarea, select, option, .check-item span, .term-tooltip`，避免checkbox等表单标签被术语tooltip污染导致无障碍名称过长
27. **禁止直接使用Unicode数学/科学符号**：所有希腊字母(αβγΔΣΩ)、数学符号(∂∫∑√∞≠≈≤≥×→∵∴∃∀∈⊂∪∩)、单位(℃°μΩ)、上下标(²³)必须放在`$...$`内用LaTeX命令书写，禁止直接打Unicode字符，否则可能在不同环境显示为方框。详见"数学/物理/化学符号完整写法参考"章节。化学课程必须加载mhchem扩展并用`$\ce{}$`写化学式。
28. **每个accordion-item必须加data-topic-id**：知识点手风琴卡片必须添加`data-topic-id="c{N}"`（与knowledgeGraph的id一致），accordion-header用`<div role="button" tabindex="0">`而非`<button>`（内部要嵌套屏蔽按钮，button不能嵌套button），标题用`.accordion-title-wrap > .accordion-title-text`包裹，并添加`.topic-exclude-btn`屏蔽按钮。题库题目必须加`data-topic-ids`属性关联知识点，否则屏蔽功能无法联动隐藏相关题目。详见"系统九：知识点屏蔽"章节。

```javascript
// 函数劫持示例：不修改原函数，包裹注入新行为
var origSetDepth = setDepth;
setDepth = function(depth) {
  origSetDepth(depth);
  // v3.0新增：深度切换后刷新Canvas可视化显隐
  updateCanvasVisibility();
};
```

---

## 使用指南

### 给AI的提示词模板

```
请使用 course-review skill v3.1 为【课程名称】创建交互式复习应用。

课程信息：
- 课程名称：【名称】
- 课程类型：【概念型/计算型/实践型/混合型】
- 章节范围：【第X章到第Y章】
- 考试形式：【选择题/简答题/计算题/论文/混合】
- 学生基础：【完全零基础/有一定基础/基础较好】
- 复习时间：【1天/2天/3天】
- 目标分数：【补考救命/稳过及格/冲刺高分】

核心概念（列出3-5个最重要的概念）：
1. 【概念1】
2. 【概念2】
3. 【概念3】

参考材料（如有请提供）：
- 往年试卷/期末卷：【上传文件或粘贴题目】
- 平时作业/练习题：【上传文件或粘贴题目】
- 上课课件/PPT：【上传文件】
- 教学大纲/考试范围：【粘贴内容或描述】
- 老师强调的重点/考点描述：【文字描述】

要求：
1. 首先询问参考材料，有参考材料时优先据此校准考点和题目
2. 融合9大学习科学理论：费曼法+主动回忆+间隔重复+掌握学习+最近发展区+认知负荷+元认知+自我效能感+情境认知
3. 包含三层深度选择器（补考救命/稳过及格/冲刺高分）
4. 包含自适应学习路径引擎（知识图谱+微检测门控+四色状态）
5. 包含全局进度条（四维加权：诊断15%+路径40%+清单25%+刷题20%）
6. 例题驱动模式（七段式：题目→思路→分步解→结果遮挡→知识提炼→变式→配套小测）
7. 错因6分类系统+错题本
8. 正反馈系统（撒花庆祝+Toast+脉冲动效+心理建设）
9. 暗黑模式+响应式+打印优化
10. 计算型课程额外包含：KaTeX渲染+计算依赖树+统一性主线+公式速查+计算陷阱库
11. 面向基础薄弱+短时间复习的学生
12. 生成单个自包含HTML文件，零外部依赖（除KaTeX CDN）
13. 在页面中标注内容来源（往年试卷/课件/AI推测）
```

---

**v3.0的灵魂是7大学习科学理论的系统融合，骨架是自适应学习路径引擎，血肉是例题驱动七段式，校准器是参考材料，体验层是情感设计与正反馈。AI在创建复习方案时，请始终问自己：这符合哪个学习科学原理？基础薄弱的学生看得懂吗？短时间能看完吗？内容是否在学生的最近发展区内？是否给了足够的正向反馈？学生能感知到自己的进度吗？错题是否转化为了精准的诊断数据？**
