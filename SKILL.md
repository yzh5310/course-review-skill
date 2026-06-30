---
name: course-review
description: 基于7大学习科学理论的通用课程交互式复习方案生成器v3.0——三层深度选择+自适应学习路径+间隔重复+错因分类+正反馈系统。面向基础薄弱、短时间需完成复习的群体，帮助AI为任意课程创建定制化单文件HTML复习应用。适用于大学课程考前速通、职业资格考试冲刺、跨专业补课等场景。
---

# Course Review Skill v3.0 — 学习科学驱动的课程速通复习应用生成器

> **核心理念**：不是文档，是学习应用。融合费曼学习法、主动回忆、间隔重复、掌握学习、最近发展区、认知负荷理论、元认知训练7大学习科学理论，用精准急救设计哲学帮基础薄弱学生在最短时间内建立应试框架。
> **不是固定模板**：AI应根据课程特点自主增减模块，本skill提供的是设计理念和最佳实践，而非刻板框架。

---

## v3.0 重大升级总览

v3.0 从"静态复习页"进化为"完整学习应用"，核心新增7大系统：

| 新系统 | 学习科学理论 | 核心价值 |
|--------|-------------|---------|
| 三层深度选择器 | 最近发展区（Vygotsky） | 不同基础学生各取所需（60分/80分/90分） |
| 自适应学习路径引擎 | 掌握学习（Bloom） | 知识图谱+前置依赖+微检测门控，只学该学的 |
| 间隔重复系统（类Anki） | 间隔重复（Ebbinghaus） | 7级间隔算法+四级掌握度+到期提醒 |
| 错因6分类系统 | 元认知（Metacognition） | 把错题从失败转化为精准诊断数据 |
| 主动回忆强化机制 | 主动回忆（Active Recall） | 遮挡式做题+翻转卡片+诊断前置 |
| 情感设计系统 | 自我效能感（Bandura） | 撒花庆祝+CTA脉冲+进度可感知+心理建设 |
| 全局进度追踪 | 自我调节学习 | 四维加权进度条+12套localStorage持久化 |

v3.0 版本演进轨迹（从v2.x继承并增强）：
- v2.1: 计算型课程差异化设计（几何直观/依赖树/统一性主线）
- v2.2: 参考材料收集机制（考点校准/来源标注）
- v2.3: 例题驱动模式（五段式例题卡片）
- v2.4: 配套小测（学完即练）
- **v3.0: 学习应用化（7大学习科学系统完整落地）**

---

## 给AI的阅读指南（最高优先级）

如果你是AI，正在阅读这个skill来为用户创建复习方案，请严格遵循以下原则：

### 第一原则：7大学习科学理论是灵魂

你创建的每一个复习页面，都必须系统性地融合以下学习科学理论，而非仅用费曼法一个：

| 学习科学理论 | 在复习页中的核心体现 | 你必须做到 |
|-------------|---------------------|-----------|
| **费曼学习法** | 白话解释+几何直观+类比+误区+口诀 | 用最简单的话解构抽象，禁止术语堆砌 |
| **主动回忆** | 遮挡做题+翻转卡片+诊断前置+配套小测 | 始终让学生输出，而非被动阅读 |
| **间隔重复** | 类Anki算法+到期提醒+掌握度分级 | 自动安排复习时机，对抗遗忘曲线 |
| **最近发展区** | 三层深度选择器+自适应路径门控 | 内容始终在"跳一跳够得着"的难度 |
| **认知负荷理论** | 渐进披露（四层折叠）+模块化卡片+hint脚手架 | 避免一次性呈现过多内容 |
| **掌握学习** | 微检测门控+知识地图+撒花庆祝+回学机制 | 必须掌握当前节点才能前进 |
| **元认知训练** | 错因6分类+错因统计+自测清单+盲区诊断 | 帮学生知道"我哪里不会、为什么错" |
| **自我效能感** | CTA脉冲+撒花动效+进度可视化+页脚心理建设 | 降低焦虑，建立信心，正向反馈密度高 |

### 第二原则：精准急救，而非全面灌输

这是一个**考前冲刺工具**，不是教材。所有设计决策服务于"最短时间拿最多分"：
- 诊断前置，拒绝盲目复习
- 依赖树预警，优先攻克阻塞点
- 三层深度，不同基础的人各取所需
- 考什么学什么，以模拟卷原题为锚点

### 第三原则：学习应用，而非静态文档

这不是一个静态HTML页面，而是一个**单文件Web应用**：
- 零构建、零后端、零依赖（除KaTeX CDN），一个HTML文件即完整应用
- 完整的数据持久层（localStorage，12+独立键）
- 模块化IIFE脚本架构，功能间互不干扰
- 渐进增强+优雅降级

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

- 通用打印样式（`@media print`）：隐藏导航/按钮/交互元素，卡片去阴影
- 专用一页纸打印模式（`body.printing-cheatsheet`）：只显示cheatsheet区域，两列排版，翻转卡片答案全部展开，字号优化为10-12pt

```css
@media print {
  .sticky-nav, .header-tools, button, .global-progress { display: none !important; }
  .card { box-shadow: none; break-inside: avoid; }
  body { background: #fff; }
  body.printing-cheatsheet .accordion-content,
  body.printing-cheatsheet .ex-variant-body,
  body.printing-cheatsheet .flip-back { display: block !important; }
}
```

### Canvas几何可视化（冲刺档专属）

对依赖空间想象的课程（高数、物理等），使用纯原生Canvas 2D API绘制交互式动画，仅在冲刺档（`data-depth="advanced"`）加载：

- 旋转曲面动画：播放/重置/角度滑块
- 极坐标/柱坐标可视化：展示分割方式
- 向量场/环流动画：直观理解Green/Stokes公式

**关键原则**：Canvas可视化是可选增强，不影响基础档性能，KaTeX加载失败不影响文字内容阅读。

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
├── SKILL.md                # TRAE格式（本文件，v3.0）
├── AGENTS.md               # 跨平台标准格式
├── CLAUDE.md               # Claude Code格式
├── .cursorrules            # Cursor格式
├── .windsurfrules          # Windsurf格式
├── .clinerules/course-review.md  # Cline格式
├── skill.json              # Skill配置v3.0
├── README.md               # 人类可读文档v3.0
├── template.html           # 参考模板（含占位符）
├── assets/js/quiz.js       # 题库系统参考实现
└── examples/
    └── data-structure.html # 示例
```

### KaTeX集成

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

<script>
function renderMath(){
  if(typeof renderMathInElement !== 'undefined'){
    renderMathInElement(document.body,{
      delimiters:[
        {left:'$$',right:'$$',display:true},
        {left:'$',right:'$',display:false}
      ],
      throwOnError:false,
      strict:false
    });
  }
}
// DOMContentLoaded + load双保险；动态内容更新后重渲染
document.addEventListener('DOMContentLoaded', () => setTimeout(renderMath, 300));
window.addEventListener('load', () => setTimeout(renderMath, 500));
</script>
```

### 代码生成避坑指南（最高优先级）

> **警告**：AI生成JavaScript代码时极易引入语法错误。严格遵守：

1. **字符串统一单引号**：题库数据中所有字符串用单引号包裹，内部安全使用中文双引号
2. **KaTeX数学模式禁中文**：`\text{收敛}`会触发警告，改为中文在数学模式外
3. **strict:false配置**：务必加上容忍边缘情况
4. **动态内容后重渲染**：手风琴展开、错题渲染后调用`setTimeout(renderMath, 50-120)`
5. **术语替换跳过KaTeX**：TreeWalker明确跳过`.katex`区域
6. **IIFE模块化**：每个功能块用独立IIFE包裹，避免全局污染
7. **函数劫持扩展**：新增功能用Monkey Patching包裹原函数，不破坏已有逻辑

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
请使用 course-review skill v3.0 为【课程名称】创建交互式复习应用。

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
2. 融合7大学习科学理论：费曼法+主动回忆+间隔重复+掌握学习+最近发展区+认知负荷+元认知
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
