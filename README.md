# Course Review Skill v5.0

一个面向 AI Agent 的课程复习应用生成 Skill：在参考资料可能不足、时间有限的情况下，为基础薄弱或考前焦虑的学习者生成有依据、有不确定性标注的最小有效学习路径。

## v5.0 的核心变化

- 用“最小核心 / 标准覆盖 / 扩展提升”替代 60/80/90 分结果暗示；
- 优先考虑剩余时间、资料证据、前置杠杆和真实学习记录；
- 没有参考资料也能生成路径，但不会声称高频、必考、押题或预计分数；
- 使用统一、版本化的 `learning_profile` 保存概念级学习记忆；
- AI 出题提示词读取概念级表现、提示使用、近期结果和已确认错因；
- 外部 AI 题目默认只进入练习区，不直接决定掌握状态或学习路径；
- 复制提示词前预览将发送的数据，默认匿名且不包含完整历史；
- 当前版本不承担教师审题、正式命题和成绩预测。

## 使用方式

向支持 Skill 的 AI 提供课程信息，例如：

```text
请使用 course-review skill 为高等数学创建复习应用。
我还有 8 小时，只有章节目录，没有往年试卷。
请优先建立最小核心路径，并生成一个单文件 HTML。
```

AI 会先判断资料证据等级，再选择覆盖模式和课程类型 Profile。资料不足不会阻塞生成，但会显示不确定性说明。

## 核心文件

- `SKILL.md`：Agent 的简洁入口和执行流程；
- `references/path-generation.md`：证据等级、覆盖模式和路径优先级；
- `references/learning-profile.md`：统一学习记忆；
- `references/question-generation.md`：外部 AI 出题与可信度隔离；
- `references/course-profiles.md`：不同课程的学习循环；
- `references/accessibility.md`：无障碍与低刺激体验；
- `schemas/learning-profile.schema.json`：学习档案 Schema；
- `schemas/question.schema.json`：生成题目 Schema；
- `template.html`：可运行参考模板。

## AI 出题助手

AI 出题助手执行以下闭环：

```text
学习事件 → LearningProfile → 选择 1-3 个学习目标
→ 预览匿名提示词 → 外部 AI 生成并自检
→ Schema 校验 → 练习区 → 用户确认错因 → 写回学习档案
```

没有可靠考试资料时，提示词只允许生成通用基础练习，不允许生成“押题卷”或模拟真实考试的内容。

## 验证

```bash
python scripts/validate_repo.py
```

然后在浏览器中打开 `template.html`，检查状态迁移、答题记录、提示词预览、题目导入、键盘操作、移动端、深色模式和打印模式。

## License

MIT
