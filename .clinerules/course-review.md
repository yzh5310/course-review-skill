# Course Review Skill v3.1 — 学习科学驱动的课程速通复习应用生成器

> **版本**: v3.1.0 | **核心理念**: 不是文档，是学习应用。精准急救，而非全面灌输。

---

## 快速指引

本skill的**完整权威文档是 `SKILL.md`**（位于skill根目录），请阅读该文件获取所有设计指南、代码示例、符号写法参考和最佳实践。本文档提供快速摘要。

## v3.1 十大核心要点

1. **9大学习科学理论系统融合**：费曼+主动回忆+间隔重复+最近发展区+认知负荷+掌握学习+元认知+自我效能感+情境认知
2. **精准急救而非全面灌输**：考前冲刺工具，诊断前置
3. **单文件HTML应用**：零构建零后端，12+localStorage持久化
4. **三层深度选择器**：🆘60分/✅80分/🚀90+
5. **自适应学习路径**：知识图谱+前置依赖+微检测门控+撒花庆祝
6. **例题驱动七段式**：题目→思路→解题(遮挡)→提炼→变式→小测
7. **错因6分类**：概念/公式/计算/方法/审题/前置
8. **情感设计**：撒花+Toast+CTA脉冲+心理建设
9. **纸质输出全场景（v3.1）**：一页纸打印+移动端适配+ScrollSpy+可行动Toast
10. **知识点屏蔽系统（v3.1新增）**：一键标记不考知识点，概念/例题/题目联动隐藏，进度自动修正

## 数学/物理/化学符号显示重要提醒

1. **禁止直接打Unicode数学符号**：必须用LaTeX命令写在`$...$`内
2. **化学课程必加mhchem扩展**：化学式用`$\ce{}$`语法
3. **物理课程推荐physics扩展**：矢量`$\vb{F}$`、导数`$\dv{y}{x}$`
4. **KaTeX四重渲染兜底**：300ms/500ms/1.5s/3s
5. **完整速查表**：见SKILL.md"数学/物理/化学符号完整写法参考"

## 知识点屏蔽系统规范（v3.1新增）

1. 每个accordion-item必须加`data-topic-id="c{N}"`（与knowledgeGraph.id一致）
2. accordion-header用`<div role="button" tabindex="0">`而非`<button>`
3. 标题用`.accordion-title-wrap > .accordion-title-text`包裹
4. 添加屏蔽按钮：`<button class="topic-exclude-btn" data-topic-id="c{N}" data-topic-name="名称" onclick="event.stopPropagation();excludeTopic(this)">🚫 不考</button>`
5. 题库题目必须加`data-topic-ids="c1,c2"`属性
6. Header中hero-actions添加🚫不考项管理按钮（带红色角标）
7. 打印时被屏蔽内容自动恢复显示

## 代码生成红线（28条，详见SKILL.md）

1. 字符串统一单引号
2. KaTeX strict:false, trust:true，数学模式禁中文
3. **禁止直接使用Unicode数学/科学符号**
4. TreeWalker跳过.katex区域
5. IIFE模块化
6. 函数劫持扩展，不破坏原函数
7. 动态内容后setTimeout(renderMath,80)
8. **化学必加mhchem，用$\ce{}$**
9. **物理单位用\text{}正体，数字单位间加\,**
10. 单文件HTML，零外部依赖（除KaTeX CDN）
11. 打印双保险恢复（afterprint+15s）
12. 移动端正文≥15px，触摸≥44px
13. localStorage加前缀，try-catch包裹
14. Canvas处理devicePixelRatio，仅冲刺档加载
15. 撒花每次40片
16. IIFE结尾分号
17. **每个accordion-item加data-topic-id；header用div非button；题目加data-topic-ids**
18. TreeWalker跳过表单元素

## 第一步：收集参考材料（必须执行）

生成复习方案前，**必须先询问用户**是否有：往年试卷/期末卷、平时作业、上课课件、教学大纲等参考材料。

---

**完整设计指南、代码示例、模块详解、符号速查表、屏蔽系统详细规范请阅读skill根目录下的 `SKILL.md`。**
