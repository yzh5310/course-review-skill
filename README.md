# Course Review Skill — 基于费曼学习法的课程速通复习方案生成器

> **v2.2** | 新增参考材料收集机制——AI主动询问往年试卷/课件等，确保考点与学校实际一致
> **v2.1** | 新增计算型课程差异化设计指南

> **核心理念**：用费曼学习法，帮基础薄弱的学生在最短时间内建立课程框架、抓住考试重点。
> **不是固定模板**：AI应根据课程特点自主增减模块，本skill提供的是设计思路和参考实现，而非刻板框架。

## v2.2 新增：参考材料收集机制

AI生成的知识点和题目基于训练数据，可能与用户学校的实际考试内容不一致。v2.2新增参考材料收集机制：

- **主动询问**：AI在生成复习方案前，必须主动询问用户是否有往年试卷、平时作业、上课课件、教学大纲等参考材料
- **考点校准**：有参考材料时，据此调整知识点权重、章节优先级和题目风格
- **原题入库**：往年试卷中的原题直接加入题库，模仿出题风格补充相似题
- **来源标注**：在页面中标注内容来源（📌 往年试卷/📌 课件强调/⚠️ AI推测）
- **无材料提醒**：无参考材料时，在页面显著位置提醒用户内容基于AI推测，建议自行校验

**核心原则**：费曼法管"怎么讲"，参考材料管"讲什么、练什么"。

## v2.1 新增：计算型课程差异化设计

对高数、物理、线代等强计算+强空间想象的课程，费曼白话法可能失效。v2.1新增差异化设计指南：

- **几何直观优先**：用图形/动画建立直觉，替代白话解释
- **数学类比**：用低维→高维推广替代生活场景类比
- **计算依赖树**：展示计算阻塞关系（偏导算不对→重积分全错）
- **统一性主线**：找课程"纲"（如三大公式本质相同）
- **分步计算填空**：交互式推导链替代静态题库
- **知识盲区诊断**：开篇先测盲区再精准补漏
- **KaTeX公式渲染**：计算型课程的基础设施

---

## 给AI的阅读指南（重要）

如果你是AI，正在阅读这个skill来为用户创建复习方案，请遵循以下原则：

### 第一原则：费曼学习法是灵魂

你创建的每一个复习页面，都必须贯彻费曼学习法的四步精神：

| 费曼步骤 | 在复习页中的体现 | 你必须做到 |
|----------|-----------------|-----------|
| ① 用最简单的话解释 | 每个概念卡片的"白话版" | 用日常语言重新描述，禁止术语堆砌 |
| ② 用类比建立直觉 | 每个核心概念配生活场景 | 找一个学生熟悉的生活场景做类比 |
| ③ 主动暴露盲区 | "常见误区" + 自测清单 | 写出学生最容易犯的错，而非只写正确答案 |
| ④ 压缩为速记口诀 | 速记口诀区 | 用最少的字把核心框架记住 |

### 第二原则：灵活组合，而非照搬模板

**不要照搬宏观经济学复习页的全部模块。** 你应该分析课程特点，决定：

- **哪些模块需要？** 概念型课程不需要公式速查；文科课程不需要计算题库
- **模块顺序如何排？** 编程课可能先放代码示例再放概念；历史课可能先放时间线
- **内容深度多深？** 完全零基础的学生需要更多白话和类比；有一定基础的可以更精炼
- **需要哪些题型？** 看考试形式——纯选择题的考试不需要简答题库

### 第三原则：知识关系图是核心

**这是本skill最重要的创新。** 知识关系图不是简单的"第1章→第2章→第3章"线性罗列，而是要展示**知识点之间的逻辑关系**。详见下文"知识关系图设计指南"。

### 第四原则：面向基础薄弱+短时间

你的读者是：
- 对课程整体框架缺乏认知的人
- 核心概念理解不牢固的人
- 只有1-3天复习时间的人
- 需要直观、通俗解释而非学术语言的人

**每一个设计决策都要问自己：基础薄弱的学生看得懂吗？短时间能看完吗？**

---

## 费曼学习法如何融入复习页

### 费曼法第一步：用最简单的话解释

**在概念精讲区，每个概念卡片必须包含"白话版"：**

```html
<div class="concept-card">
  <h3>乘数效应</h3>
  <p><strong>定义：</strong>投资增加引起的国民收入增加量是投资增加量的倍数。</p>
  
  <!-- 费曼法第一步：白话版 -->
  <div class="plain-explain">
    <strong>白话版：</strong>政府花1块钱修路，修路工人拿到1块钱去买面包，
    面包师拿到钱去买衣服……这1块钱转了好几圈，最后GDP涨了不止1块钱。
    涨了几倍，这个"倍"就是乘数。
  </div>
</div>
```

**关键要求**：
- 禁止用另一个专业术语解释专业术语
- 必须用学生日常生活中的场景
- 宁可啰嗦也不要含糊

### 费曼法第二步：用生活类比建立直觉

**每个核心概念配一个生活类比，用emoji标注：**

```html
<div class="plain-explain">
  <strong>生活类比：</strong>
  IS-LM模型就像跷跷板——商品市场坐在一头，货币市场坐在另一头，
  利率是中间的支点。哪头重（哪个市场需求大），利率就往哪边倾斜。
</div>
```

**类比设计原则**：
- 用学生一定熟悉的场景（吃饭、排队、买东西、打游戏）
- 类比要抓住概念的**核心机制**，而非表面相似
- 一个概念可以配多个类比，从不同角度理解

### 费曼法第三步：主动暴露盲区

**每个概念卡片包含"常见误区"：**

```html
<div class="common-mistake">
  <strong>常见误区：</strong>
  ① 很多人以为乘数越大越好——其实乘数大意味着经济波动更剧烈
  ② 很多人忘了乘数公式里的 MPC 是"边际"消费倾向，不是"平均"消费倾向
  ③ 很多人算乘数时直接用 1/(1-MPC)，但考试常考的是含税乘数，要变形式
</div>
```

**自测清单的作用**：
- 不是"你学到了什么"，而是"你能不能做到什么"
- 用"我能……"句式，强调能力而非知识

### 费曼法第四步：压缩为速记口诀

**每章或每个知识块配速记口诀：**

```html
<div class="mnemonic-box">
  <h4>💡 速记口诀</h4>
  <div class="mnemonic-item">
    <span class="emoji">📊</span>
    <span><b>AD-AS三句话：</b>总需求往下压，总供给往上撑，交点就是均衡价。</span>
  </div>
  <div class="mnemonic-item">
    <span class="emoji">🎚️</span>
    <span><b>政策方向：</b>财政管税收和花销，货币管利率和钞票。</span>
  </div>
</div>
```

**口诀设计原则**：
- 字数越少越好，最好押韵
- 只记框架，细节交给理解
- 一个口诀对应一个知识块，不要贪多

---

## 知识关系图设计指南（核心创新）

### 为什么知识关系图很重要？

基础薄弱的学生最大的问题不是"记不住"，而是"不知道知识点之间有什么关系"。他们看到的是一堆孤立的概念，而不是一张有逻辑的网络。

**知识关系图的目标**：让学生一眼看到"这个知识点为什么在这个位置""它和别的知识点是什么关系"。

### 七种知识关系类型

AI在分析课程内容时，应识别知识点之间的以下关系类型，选择最合适的来组织关系图：

#### 1. 因果关系（A导致B）

**适用场景**：经济学、物理、化学等有因果链条的学科

**视觉表现**：
```
货币供给↑ → 利率↓ → 投资↑ → 产出↑ → 收入↑
                                              ↓
                                         消费↑ ←（循环反馈）
```

**HTML实现思路**：
```html
<div class="causal-chain">
  <div class="chain-node">
    <strong>货币供给↑</strong>
    <span class="chain-arrow">导致</span>
  </div>
  <div class="chain-node">
    <strong>利率↓</strong>
    <span class="chain-arrow">导致</span>
  </div>
  <div class="chain-node">
    <strong>投资↑</strong>
  </div>
</div>
```

#### 2. 前提依赖（理解A才能理解B）

**适用场景**：数学、编程等有严格知识层级的学科

**视觉表现**：
```
        导数
         ↑（前提）
      极限
         ↑（前提）
       函数
         ↑（前提）
       变量
```

#### 3. 对比关系（A vs B）

**适用场景**：任何有对立/对照概念的课程

**视觉表现**：
```
  财政政策              货币政策
  ─────────            ─────────
  政府税收/支出         央行利率/货币供给
  直接影响总需求         间接影响总需求
  见效慢但持久           见效快但短期
         ↕
      两者配合使用
```

#### 4. 递进关系（从简单到复杂）

**适用场景**：数学、编程等循序渐进的学科

**视觉表现**：
```
变量 → 函数 → 导数 → 积分 → 微分方程
（简单）───────────────────→（复杂）
```

#### 5. 总分关系（一个大概念包含子概念）

**适用场景**：任何有层级结构的课程

**视觉表现**：
```
            宏观经济政策
           /      |      \
      财政政策  货币政策  供给政策
       /  \      /  \
    税收 支出  利率 货币供给
```

#### 6. 应用关系（理论→实际问题）

**适用场景**：理论+应用型课程

**视觉表现**：
```
供需理论 ──→ 价格分析
    │
    └──→ 市场均衡判断
    │
    └──→ 政策效果评估
```

#### 7. 循环反馈（A影响B，B反过来影响A）

**适用场景**：经济学、生态学等有反馈机制的课程

**视觉表现**：
```
    收入↑ ───→ 消费↑
      ↑            │
      │            ↓
    产出↑ ←── 投资↑
```

### 如何选择关系类型？

AI应根据课程特点选择**1-2种主要关系类型**，而非全部使用：

| 课程类型 | 推荐关系类型 | 示例 |
|----------|-------------|------|
| 经济学/金融 | 因果关系 + 循环反馈 | 货币政策传导机制 |
| 数学 | 前提依赖 + 递进关系 | 微积分知识链 |
| 编程 | 前提依赖 + 总分关系 | 数据结构层级 |
| 历史 | 因果关系 + 时间线 | 事件因果链 |
| 物理 | 因果关系 + 应用关系 | 力学→运动学→能量 |
| 化学 | 总分关系 + 对比关系 | 元素周期表分类 |
| 文学 | 对比关系 + 总分关系 | 文学流派对比 |

### 关系图的视觉实现建议

**不要只画箭头，要标注关系类型：**

```html
<div class="relation-map">
  <!-- 因果链 -->
  <div class="relation-chain">
    <div class="relation-node highlight">
      <strong>总需求AD</strong>
      <span class="node-tag">核心概念</span>
    </div>
    <div class="relation-arrow">
      <span class="arrow-label">↓ 导致价格下降</span>
    </div>
    <div class="relation-node">
      <strong>价格水平P</strong>
    </div>
    <div class="relation-arrow">
      <span class="arrow-label">↑ 反过来影响</span>
    </div>
    <div class="relation-node">
      <strong>实际货币供给</strong>
    </div>
  </div>
  
  <!-- 对比框 -->
  <div class="relation-compare">
    <div class="compare-side">
      <h4>财政政策</h4>
      <ul>
        <li>工具：税收、政府支出</li>
        <li>主体：政府</li>
        <li>见效：慢但持久</li>
      </ul>
    </div>
    <div class="compare-vs">VS</div>
    <div class="compare-side">
      <h4>货币政策</h4>
      <ul>
        <li>工具：利率、准备金率</li>
        <li>主体：央行</li>
        <li>见效：快但短期</li>
      </ul>
    </div>
  </div>
</div>
```

---

## 模块系统：灵活组合指南

### 必选模块（4个）

这4个模块是费曼学习法的骨架，**任何课程都必须包含**：

| 模块 | 费曼法对应 | 为什么必选 |
|------|-----------|-----------|
| 🌱 新手引导区 | 整体认知 | 基础薄弱学生的第一入口，先看森林再看树木 |
| 🗺️ 知识关系图 | 理解关系 | 用关系代替背诵，理解了关系就不需要死记 |
| 📚 概念精讲区 | 白话+类比 | 费曼法核心实践：白话解释+生活类比+常见误区 |
| ✅ 自测清单 | 暴露盲区 | 主动发现"我不会什么" |

### 可选模块（按需选用）

AI根据课程特点选择，**不要全部加上**：

| 模块 | 适用课程 | 不适用课程 |
|------|---------|-----------|
| 💬 悬浮解释框 | 有专业术语的课程 | 概念极少的课程 |
| 🔍 概念搜索面板 | 概念多、需快速定位 | 概念少（5个以内） |
| 📊 复习仪表盘 | 内容多、需进度管理 | 内容少（3章以内） |
| 📋 公式速查 | 理科、计算类 | 纯文科、概念类 |
| 📈 概念图表化 | 有图形/模型/流程 | 纯文字概念 |
| 🚑 应试急救包 | 有固定题型 | 开卷考、论文考 |
| 🎯 题库系统 | 需针对性练习、错题关联知识点查漏补缺 | 以理解为主 |
| 🏷️ 章节优先级筛选 | 章节多需取舍 | 章节少 |
| 💻 代码示例 | 编程类 | 非编程类 |
| 📅 时间线/历史脉络 | 历史、法律 | 数学、编程 |
| 📊 对比表格 | 有大量对比 | 概念独立 |
| 📄 考前一页纸 | 任何课程 | — |

### 决策流程

```
分析课程 → 确定课程类型 → 选择模块 → 决定顺序 → 填充内容
    │
    ├── 概念型课程（如哲学、文学史）
    │   → 新手引导 + 知识关系图(总分/对比) + 概念精讲 + 时间线 + 自测清单
    │
    ├── 计算型课程（如高数、物理）
    │   → 新手引导 + 知识关系图(前提依赖/递进) + 概念精讲 + 公式速查 + 题库 + 自测清单
    │
    ├── 实践型课程（如编程）
    │   → 新手引导 + 知识关系图(前提依赖) + 概念精讲 + 代码示例 + 题库 + 自测清单
    │
    └── 混合型课程（如经济学）
        → 新手引导 + 知识关系图(因果/循环) + 概念精讲 + 概念图表化 + 公式速查 + 应试急救包 + 题库 + 自测清单
```

---

## 新手引导区设计指南

### 核心目标

用最短时间让基础薄弱的学生建立**整体认知**——知道这门课讲什么、怎么学、从哪开始。

### 必须包含的元素

1. **一句话概括课程**：这门课到底研究什么？
2. **学习路线（3-5步）**：从零到考试的路径
3. **速记口诀**：把课程框架压缩成几句话
4. **难度标识**：哪些零基础可看，哪些需要理解，哪些是难点

### 学习路线设计原则

```
第1步：看大图（看知识关系图，建立整体印象）     ← 零基础可看
第2步：抓核心（看概念精讲的白话版和类比）       ← 零基础可看
第3步：练手感（做几道题，用题库系统）           ← 需要理解
第4步：查盲区（用自测清单，发现不会的）         ← 需要理解
第5步：背口诀（用速记口诀，考前最后冲刺）       ← 零基础可看
```

**注意**：步骤数不固定，AI根据课程复杂度决定3-5步。

---

## 概念精讲区设计指南

### 每个概念卡片的完整结构

```html
<div class="concept-card">
  <h3>概念名称 <span class="beginner-badge">难度标识</span></h3>
  
  <!-- 1. 这章讲什么？（费曼法：建立认知） -->
  <div class="plain-explain">
    <strong>这章讲什么？</strong> 用一段话告诉学生这章解决什么问题。
  </div>
  
  <!-- 2. 正式定义 -->
  <p><strong>定义：</strong>教科书式的准确定义。</p>
  
  <!-- 3. 白话版（费曼法第一步） -->
  <div class="plain-explain">
    <strong>白话版：</strong> 用日常语言重新描述，禁止术语堆砌。
  </div>
  
  <!-- 4. 生活类比（费曼法第二步） -->
  <div class="plain-explain">
    <strong>生活类比：</strong> 用学生熟悉的场景做类比。
  </div>
  
  <!-- 5. 公式/机制（如有） -->
  <div class="formula">公式或运作机制</div>
  
  <!-- 6. 应试要点 -->
  <div class="key-point">
    <strong>应试要点：</strong> 考试怎么考、怎么答。
  </div>
  
  <!-- 7. 常见误区（费曼法第三步） -->
  <div class="common-mistake">
    <strong>常见误区：</strong> 学生最容易犯的错。
  </div>
</div>
```

### 白话版的写作要求

**好的白话版**：
> 乘数效应：政府花1块钱修路，修路工人拿到钱去买面包，面包师拿到钱去买衣服……这1块钱转了好几圈，最后GDP涨了不止1块钱。

**差的白话版**：
> 乘数效应：投资增加导致国民收入成倍增加的效应。

**区别**：好的白话版有**具体场景**和**动作过程**，差的白话版只是换了个说法重复定义。

---

## 自测清单设计指南

### 设计原则

- **不是"你学到了什么"，而是"你能不能做到什么"**
- 用"我能……"句式，强调能力而非记忆
- 8-12个检查点为宜
- 与进度条联动，提供学习建议

### 检查点示例

```html
<label>
  <input class="study-check" type="checkbox" />
  我能用白话向别人解释"乘数效应"是什么（费曼检验）
</label>
<label>
  <input class="study-check" type="checkbox" />
  我能画出IS-LM模型，并说明曲线移动的原因
</label>
<label>
  <input class="study-check" type="checkbox" />
  我能区分财政政策和货币政策的工具与效果
</label>
```

**关键**：检查点要用**可验证的行为**描述，而非"我理解了XX"这种模糊表述。

---

## 悬浮解释框设计指南

### 作用

在页面中遇到专业术语时，鼠标悬停即可看到通俗解释，**不需要跳转到其他位置**。这是费曼学习法的即时实践——让学生在阅读过程中随时获得"白话翻译"。

### 使用场景

- 任何有专业术语的课程都建议使用
- 特别适合：经济学、法学、医学、计算机等术语密集的学科

### HTML实现

```html
<!-- 在任何文本中嵌入术语解释 -->
<p>
  GDP = <span class="tooltip-term" data-tip="消费C：家庭购买商品和服务的支出，如吃饭、买衣服。">消费</span> 
  + <span class="tooltip-term" data-tip="投资I：企业购买资本品（厂房、设备）及增加存货的支出。">投资</span> 
  + <span class="tooltip-term" data-tip="政府购买G：各级政府购买商品和服务的支出，如修路、办公支出。">政府支出</span> 
  + <span class="tooltip-term" data-tip="净出口NX：出口减进口的差额。">净出口</span>
</p>
```

### CSS实现

```css
.tooltip-term {
  border-bottom: 1.5px dashed var(--primary);
  cursor: help;
  position: relative;
  color: var(--primary);
  font-weight: 600;
}

.tooltip-term:hover::after {
  content: attr(data-tip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #1e293b;
  color: #fff;
  padding: 8px 12px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 400;
  white-space: normal;
  width: max-content;
  max-width: 280px;
  line-height: 1.5;
  z-index: 100;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  pointer-events: none;
}

/* 边缘智能定位：避免解释框被遮挡 */
.tooltip-term.tip-flip-down:hover::after { bottom: auto; top: 100%; }
.tooltip-term.tip-shift-left:hover::after { left: 0; transform: translateX(0); }
.tooltip-term.tip-shift-right:hover::after { left: auto; right: 0; transform: translateX(0); }
```

### JavaScript（边缘智能定位）

```javascript
// 避免解释框被屏幕边缘遮挡
document.querySelectorAll('.tooltip-term').forEach(function(term) {
  term.addEventListener('mouseenter', function() {
    term.classList.remove('tip-flip-down', 'tip-shift-left', 'tip-shift-right');
    var rect = term.getBoundingClientRect();
    var tipW = 280;
    var margin = 8;
    
    // 右边缘溢出 → 左移贴右
    if (rect.left + tipW/2 + margin > window.innerWidth) {
      term.classList.add('tip-shift-right');
    } else if (rect.left - tipW/2 - margin < 0) {
      // 左边缘溢出 → 右移贴左
      term.classList.add('tip-shift-left');
    }
    // 顶部空间不足 → 翻转到下方
    if (rect.top < 120) {
      term.classList.add('tip-flip-down');
    }
  });
});
```

### 费曼法结合

悬浮解释框是费曼学习法的**即时实践**：
- 每个 `data-tip` 的内容必须用**白话**写，禁止用术语解释术语
- 解释要包含**具体场景**或**生活类比**
- 例如：`"消费C：家庭购买商品和服务的支出，如吃饭、买衣服。"`

---

## 概念搜索面板设计指南

### 作用

当课程概念较多时，学生需要快速定位某个概念在哪里。搜索面板提供：
- **实时搜索**：输入关键词即时过滤
- **高亮匹配**：搜索结果中高亮显示匹配文字
- **点击跳转**：点击结果自动滚动到对应位置
- **智能展开**：如果概念在折叠面板中，自动展开
- **返回功能**：跳转后可以返回上一位置

### 使用场景

- 概念数量超过10个的课程
- 术语密集、需要反复查阅的课程
- 适合：经济学、法学、医学、计算机科学等

### HTML结构

```html
<!-- 搜索面板（固定在页面右侧） -->
<div class="search-panel" id="searchPanel">
  <div class="search-panel-header">
    <span class="search-panel-title">🔍 概念搜索</span>
    <button class="search-panel-toggle" id="searchPanelToggle">−</button>
  </div>
  <div class="search-panel-body">
    <div class="search-input-wrap">
      <input type="text" id="searchInput" placeholder="搜索概念术语..." autocomplete="off">
      <button id="searchBackBtn" disabled title="返回上一位置">← 返回</button>
    </div>
    <div class="search-results" id="searchResults">
      <div class="search-hint">输入关键词搜索虚线下划线标注的概念</div>
    </div>
    <div class="search-stats" id="searchStats"></div>
  </div>
</div>
```

### CSS实现

```css
.search-panel {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  width: 280px;
  max-height: 70vh;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.search-panel.collapsed .search-panel-body {
  display: none;
}

.search-panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 14px;
  background: var(--primary);
  color: #fff;
  font-weight: 700;
  font-size: 14px;
  cursor: grab;
  user-select: none;
}

.search-panel-body {
  padding: 12px;
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.search-input-wrap {
  display: flex;
  gap: 6px;
  margin-bottom: 10px;
}

#searchInput {
  flex: 1;
  padding: 8px 10px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg);
  color: var(--text);
  font-size: 13px;
  outline: none;
}

#searchInput:focus {
  border-color: var(--primary);
}

.search-results {
  flex: 1;
  overflow-y: auto;
  max-height: calc(70vh - 100px);
}

.search-hint {
  color: var(--muted);
  font-size: 12px;
  text-align: center;
  padding: 20px 10px;
}

.search-result-item {
  padding: 8px 10px;
  border-radius: 8px;
  cursor: pointer;
  margin-bottom: 4px;
  transition: background 0.2s;
  border: 1px solid transparent;
}

.search-result-item:hover {
  background: var(--primary-light);
  border-color: var(--primary);
}

.search-result-term {
  font-weight: 700;
  font-size: 13px;
  color: var(--primary);
  margin-bottom: 2px;
}

.search-result-desc {
  font-size: 11.5px;
  color: var(--muted);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.search-result-item mark {
  background: #fef08a;
  color: inherit;
  padding: 0 1px;
  border-radius: 2px;
}

body.dark .search-result-item mark {
  background: #854d0e;
  color: #fef9c3;
}

.search-stats {
  font-size: 11px;
  color: var(--muted);
  padding-top: 8px;
  border-top: 1px solid var(--border);
  margin-top: 8px;
  text-align: center;
}

/* 移动端适配 */
@media (max-width: 900px) {
  .search-panel {
    right: 10px;
    width: 240px;
    top: auto;
    bottom: 20px;
    transform: none;
    max-height: 50vh;
  }
}
```

### JavaScript实现

```javascript
(function() {
  var searchHistory = [];
  var allTerms = [];

  // 初始化：收集所有 tooltip-term
  function collectTerms() {
    var terms = document.querySelectorAll('.tooltip-term');
    var seen = {};
    allTerms = [];
    terms.forEach(function(el) {
      var text = el.textContent.trim();
      var tip = el.getAttribute('data-tip') || '';
      var key = text + '|' + tip;
      if (!seen[key]) {
        seen[key] = true;
        allTerms.push({ element: el, text: text, tip: tip });
      }
    });
  }

  // 高亮匹配文字
  function highlight(text, keyword) {
    if (!keyword) return text;
    var idx = text.toLowerCase().indexOf(keyword.toLowerCase());
    if (idx < 0) return text;
    return text.substring(0, idx) + '<mark>' + text.substring(idx, idx + keyword.length) + '</mark>' + text.substring(idx + keyword.length);
  }

  // 执行搜索
  function doSearch(keyword) {
    var resultsEl = document.getElementById('searchResults');
    var statsEl = document.getElementById('searchStats');
    keyword = keyword.trim();

    if (!keyword) {
      resultsEl.innerHTML = '<div class="search-hint">输入关键词搜索虚线下划线标注的概念</div>';
      statsEl.textContent = '';
      return;
    }

    var results = allTerms.filter(function(t) {
      return t.text.toLowerCase().indexOf(keyword.toLowerCase()) >= 0
          || t.tip.toLowerCase().indexOf(keyword.toLowerCase()) >= 0;
    });

    if (results.length === 0) {
      resultsEl.innerHTML = '<div class="search-hint">未找到匹配的概念</div>';
      statsEl.textContent = '0 个结果';
      return;
    }

    var html = '';
    results.forEach(function(t, i) {
      html += '<div class="search-result-item" data-idx="' + i + '">'
           +   '<div class="search-result-term">' + highlight(t.text, keyword) + '</div>'
           +   '<div class="search-result-desc">' + highlight(t.tip, keyword) + '</div>'
           + '</div>';
    });
    resultsEl.innerHTML = html;
    statsEl.textContent = results.length + ' 个结果';

    // 绑定点击事件
    resultsEl.querySelectorAll('.search-result-item').forEach(function(item) {
      item.addEventListener('click', function() {
        var idx = +this.getAttribute('data-idx');
        jumpToTerm(results[idx]);
      });
    });
  }

  // 跳转到某个术语
  function jumpToTerm(termObj) {
    searchHistory.push({
      scrollY: window.scrollY,
      keyword: document.getElementById('searchInput').value
    });
    document.getElementById('searchBackBtn').disabled = false;

    var el = termObj.element;

    // 如果在折叠面板里，先展开
    var accordionItem = el.closest('.accordion-item');
    if (accordionItem && !accordionItem.classList.contains('active')) {
      accordionItem.classList.add('active');
    }

    // 高亮闪烁
    el.style.transition = 'background-color 0.3s, color 0.3s';
    el.style.backgroundColor = 'rgba(37, 99, 235, 0.25)';
    el.style.color = 'var(--primary)';
    el.style.borderRadius = '4px';
    el.style.padding = '2px 4px';
    setTimeout(function() {
      el.style.backgroundColor = '';
      el.style.color = '';
      el.style.borderRadius = '';
      el.style.padding = '';
    }, 2000);

    // 滚动定位
    requestAnimationFrame(function() {
      var rect = el.getBoundingClientRect();
      var scrollTop = window.scrollY + rect.top - window.innerHeight / 3;
      window.scrollTo({ top: Math.max(0, scrollTop), behavior: 'smooth' });
    });
  }

  // 返回上一位置
  function goBack() {
    if (searchHistory.length === 0) return;
    var last = searchHistory.pop();
    window.scrollTo({ top: last.scrollY, behavior: 'smooth' });
    if (searchHistory.length === 0) {
      document.getElementById('searchBackBtn').disabled = true;
    }
  }

  // 折叠/展开面板
  function togglePanel() {
    var panel = document.getElementById('searchPanel');
    var btn = document.getElementById('searchPanelToggle');
    panel.classList.toggle('collapsed');
    btn.textContent = panel.classList.contains('collapsed') ? '+' : '−';
  }

  // 防抖
  function debounce(fn, delay) {
    var timer = null;
    return function() {
      var args = arguments;
      var ctx = this;
      clearTimeout(timer);
      timer = setTimeout(function() { fn.apply(ctx, args); }, delay);
    };
  }

  // 初始化
  window.addEventListener('load', function() {
    setTimeout(collectTerms, 500);

    var searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', debounce(function() {
      doSearch(this.value);
    }, 200));

    document.getElementById('searchBackBtn').addEventListener('click', goBack);
    document.getElementById('searchPanelToggle').addEventListener('click', togglePanel);
  });
})();
```

### 费曼法结合

概念搜索面板是费曼学习法的**快速查阅工具**：
- 学生在做题或复习时，遇到不懂的术语可以即时搜索
- 搜索结果同时显示术语名称和通俗解释
- 点击跳转后，概念会高亮闪烁2秒，帮助定位

---

## 视觉设计系统

### CSS变量

```css
:root {
  --primary: #2563eb;
  --primary-light: #dbeafe;
  --text: #111827;
  --muted: #6b7280;
  --bg: #f3f4f6;
  --card: #ffffff;
  --border: #e5e7eb;
  --success: #16a34a;
  --warning: #f59e0b;
  --danger: #dc2626;
}
```

### 难度标识系统

| 标识 | 含义 | 颜色 |
|------|------|------|
| 零基础可看 | 完全不需要基础 | 绿色 |
| 需要理解 | 需要先理解前置概念 | 黄色 |
| 重点难点 | 考试重点且难度大 | 红色 |

### 响应式与暗色模式

- 支持移动端（720px断点）
- 支持平板端（900px断点）
- 支持暗色模式（CSS变量切换）
- 支持打印（隐藏交互元素，展开折叠内容）

---

## 技术实现参考

### 文件结构

```
course-review-skill/
├── skill.json              # Skill配置（含费曼法理念和模块系统）
├── README.md               # 本文档（AI阅读指南）
├── template.html           # 参考模板（不是固定模板，仅供参考）
├── assets/
│   └── js/
│       └── quiz.js         # 题库系统参考实现
├── docs/
│   └── ai-pitfalls.md      # AI生成代码避坑指南（Markdown）
└── examples/
    └── data-structure.html # 示例：数据结构复习页
```

### 题库数据结构

```javascript
const questionBank = {
  choice: [{
    id: 1,
    question: "题目内容",
    options: ["A", "B", "C", "D"],
    answer: 0,
    explanation: "解析",
    hint: "提示",  // 费曼法：不会做时先看提示
    score: 10,
    chapter: 1,     // 主章节号（用于关联知识点跳转）
    relatedChapters: [1, 2],  // 可选：相关章节数组（多章节综合题）
    source: '往年试卷'  // v2.2新增：题目来源（往年试卷/平时作业/AI生成等）
  }],
  tf: [...],
  calc: [...],
  short: [...],
  material: [...]
};
```

### 题库-知识点关联定位功能（核心特性）

每道题可以关联到一个或多个章节的知识点，学生做题时可以一键跳转到对应概念精讲区。

**三处跳转入口：**
1. **题目展示区**：题目下方显示"查看第X章概念精讲"按钮
2. **错题反馈区**：答错时在解析下方显示"回看第X章概念精讲 →"按钮，引导即时复习
3. **错题回顾列表**：考试结束后的总结页面，每道错题都带跳转按钮

**智能定位效果：**
- 自动展开折叠的章节
- 目标章节高亮闪烁2秒，帮助快速定位
- 平滑滚动到对应位置

**多章节综合题支持：**
- 如果题目关联多个章节（`relatedChapters` 数组），显示"📚 相关概念："标签和多个跳转按钮
- 单章节题只显示一个简洁的跳转按钮

**使用前提：**
1. 概念精讲区的每个 `accordion-item` 必须添加 `id="concept-ch{N}"`
2. 每道题添加 `chapter` 字段（主章节号）
3. 综合题可选添加 `relatedChapters` 字段（数组）
4. 定义 `chapterNames` 章节名称映射对象

### 本地存储

```javascript
// 保存进度
localStorage.setItem('course_slug_checks', JSON.stringify(states));
localStorage.setItem('course_slug_quiz', JSON.stringify(quizData));
```

---

## 使用指南

### 给AI的提示词模板

```
请使用 course-review skill 为【课程名称】创建交互式复习方案。

课程信息：
- 课程名称：【名称】
- 课程类型：【概念型/计算型/实践型/混合型】
- 章节范围：【第X章到第Y章】
- 考试形式：【选择题/简答题/计算题/论文/混合】
- 学生基础：【完全零基础/有一定基础】
- 复习时间：【1天/2天/3天】

核心概念（列出3-5个最重要的概念）：
1. 【概念1】
2. 【概念2】
3. 【概念3】

参考材料（v2.2新增·如有请提供）：
- 往年试卷/期末卷：【上传文件或粘贴题目】
- 平时作业/练习题：【上传文件或粘贴题目】
- 上课课件/PPT：【上传文件】
- 教学大纲/考试范围：【粘贴内容或描述】
- 老师强调的重点/考点描述：【文字描述】

要求：
1. 【v2.2】首先询问参考材料，有参考材料时优先据此校准考点和题目
2. 贯彻费曼学习法：每个概念都要有白话版、生活类比、常见误区
3. 知识关系图要体现知识点间的逻辑关系（因果/对比/递进/总分等）
4. 根据课程类型自主选择模块，不要照搬全部模块
5. 面向基础薄弱+短时间复习的学生
6. 生成单个自包含HTML文件
7. 【v2.2】在页面中标注内容来源（往年试卷/课件/AI推测）
```

---

## 示例

### 宏观经济学复习页（原始参考）

特点：8章、3大模型、因果+循环反馈关系图、66道题

### 数据结构复习页

参考文件：`examples/data-structure.html`

特点：10章、前提依赖+递进关系图、8种排序算法对比表

---

## 许可证

MIT License

---

**这个skill的灵魂是费曼学习法，骨架是灵活的模块系统，血肉是知识关系图，校准器是参考材料。v2.2要求AI在生成方案前主动收集参考材料，确保考点与学校实际一致。AI在创建复习方案时，请始终问自己：基础薄弱的学生看得懂吗？短时间能看完吗？知识点之间的关系清楚吗？考点和学校实际一致吗？**
