# Course Review Skill v5.3.1

一个面向 AI Agent 的课程复习应用生成 Skill：在参考资料可能不足、时间有限的情况下，为基础薄弱或考前焦虑的学习者生成有依据、有不确定性标注的最小有效学习路径。

## v5.3.1 的核心变化

- 求助时自动带入当前题目／选中文字和知识点，提示词即时准备；一次点击复制并打开常用 AI，其余设置折叠；
- 默认外部 AI 对话接力，无需题目回流；支持解释步骤、补基础和逐题练习；
- 统一提示词各范围的数据与排除规则，增加运行行为测试；
- 需求询问、短任务、自主检测、安静反馈及本地任务续接；

- 用“最小核心 / 标准覆盖 / 扩展提升”替代 60/80/90 分结果暗示；
- 优先考虑剩余时间、资料证据、前置杠杆和真实学习记录；
- 没有参考资料也能生成路径，但不会声称高频、必考、押题或预计分数；
- 使用统一、版本化的 `learning_profile` 保存概念级学习记忆；
- 外部 AI 求助提示词读取概念级表现、提示使用、近期结果和已确认错因；
- 可选导入的外部 AI 题目只进入练习区，不直接决定掌握状态或学习路径；
- 复制提示词前预览将发送的数据，默认匿名且不包含完整历史；
- 当前版本不承担教师审题、正式命题和成绩预测。
- 每个生成方案必须携带机器可读的 `courseReviewContract`；
- `validate_output.py` 会阻止缺少证据说明、保过承诺、单题掌握或 AI 题影响掌握的产物交付。

## 使用方式

向支持 Skill 的 AI 提供课程信息，例如：

```text
请使用 course-review skill 为高等数学创建复习应用。
我还有 8 小时，只有章节目录，没有往年试卷。
请优先建立最小核心路径，并生成一个单文件 HTML。
```

如果用户首次只说“帮我生成某课程的复习方案”，AI 必须先用不超过三组简短问题了解：学习目的和可用时间、当前基础与困难、课程范围与考核资料，收到回答后再生成 HTML。已有答案不重复询问，只对会改变方案的关键歧义继续追问；信息足够后直接推进，不例行要求再次确认。

回答必须实际改变复习范围、必做任务量、讲解深度、练习难度和学习节奏，不能只替换页面标题。必做任务的预计总时长应计入学习、练习和回顾，适配已知时间预算；放不下的内容说明取舍并列为可选。页面简要显示“本方案依据”，区分已知情况、用户自述与未确认假设。

用户说“不知道”、没有资料，或明确要求“不用问，直接生成”时，仍可继续，但要标明未知和假设；不能擅自认定零基础、编造考试日期或考试重点。时间未知时提供带时长估计的任务顺序，不虚构每日计划。AI 根据这些信息判断资料证据等级，再选择覆盖模式和课程类型 Profile。

## 核心文件

- `SKILL.md`：Agent 的简洁入口和执行流程；
- `references/learner-intake.md`：首次询问、用户情况到 HTML 的调整规则及行为验收场景；
- `references/path-generation.md`：证据等级、覆盖模式和路径优先级；
- `references/learning-profile.md`：统一学习记忆；
- `references/question-generation.md`：外部 AI 出题与可信度隔离；
- `references/course-profiles.md`：不同课程的学习循环；
- `references/accessibility.md`：无障碍与低刺激体验；
- `schemas/learning-profile.schema.json`：学习档案 Schema；
- `schemas/question.schema.json`：生成题目 Schema；
- `schemas/review-plan.schema.json`：生成复习方案的强制输出契约；
- `scripts/validate_output.py`：任意生成 HTML 的发布门校验器；
- `template.html`：可运行参考模板。

## 外部 AI 学习接力

默认流程：点击题目旁的求助 → 自动带入当前题目、知识点及学习摘要 → 点击“复制并打开常用AI” → 在外部 AI 粘贴发送。无需重填题目、选知识点、勾选分享或分别生成／确认；其余设置默认折叠。常用平台会记住，下次沿用。

外部 AI 的对话不会自动回写本 HTML。回来时可继续上次的本地章节或题目，无需补录外部学习过程。按钮上方说明将复制的当前题目／选中文字与匿名摘要，可移除原题或展开全文；点击“复制并打开”才复制。复制或弹窗受限时提供手动后备入口，不声称已自动粘贴或发送。

有文件修改能力的 Agent 可使用可选的结构化题目导入；普通用户不需要走这条路线。导入题目保持未核验练习材料，不直接改变掌握判断。

## 注意力与继续学习

默认安静模式，可切换鼓励／冲刺；取消固定 30 秒弹出检测，改为自主点击章节检测。下一步与知识图谱共用学习档案，保存上次本地任务，并允许直接阅读前置尚未确认的章节。没有用户研究时不声称提升专注时长或成绩。

## 示例版本

`template.html` 是当前 v5.3.1 可运行示例（使用演示高数数据，未绑定真实试卷）；`examples/calculus2.html`、`data-structure.html` 是历史生成样本，不能视为已具备全部新功能。生成实际课程方案时必须替换演示内容并重新验证。

## 验证

```bash
python scripts/validate_repo.py
python scripts/validate_output.py template.html
python scripts/test_validate_output.py
node scripts/test_runtime.cjs
```

浏览器回归（使用独立测试会话，会清空该测试来源的本地学习记录）：先在仓库目录运行 `python -m http.server 8792 --bind 127.0.0.1`，另开终端执行：

```bash
npx --package @playwright/cli playwright-cli --session review-check open http://127.0.0.1:8792/template.html
npx --package @playwright/cli playwright-cli --session review-check run-code --filename scripts/check_browser.js
```

此检查覆盖桌面与390px页面、外部求助、可选导入、暂停续学、反馈模式、键盘退出、深色及打印模式。测试不会向外部 AI 平台发送内容，也不证明实际学习效果。

其他 AI 生成新的 HTML 后，必须把第二条命令中的 `template.html` 替换为实际产物路径。产物校验失败时不得交付。然后在浏览器中检查状态迁移、答题记录、提示词预览、题目导入、键盘操作、移动端、深色模式和打印模式。

还须按 `references/learner-intake.md` 核对实际内容是否适配用户情况。自动校验通过只证明其覆盖的结构与可信度边界，不能证明 AI 已完成询问或方案适合本人。“60 秒内开始学习”从打开生成的 HTML 起算，不用于跳过生成前的必要澄清。

## License

MIT
