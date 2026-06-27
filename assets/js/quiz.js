// ==================== 题库系统核心代码 ====================
// 通用课程复习方案 - 题库系统模块

class QuizSystem {
  constructor(questionBank, courseSlug) {
    this.questionBank = questionBank;
    this.courseSlug = courseSlug;
    this.currentMode = 'practice';
    this.currentFilter = 'all';
    this.currentQuestionIndex = 0;
    this.questions = [];
    this.answers = {};
    this.score = 0;
    this.totalQuestions = 0;
    this.correctCount = 0;
    
    // DOM元素
    this.elements = {
      modeTabs: document.querySelectorAll('.qb-mode-tab'),
      filterBtns: document.querySelectorAll('[data-qfilter]'),
      progress: document.getElementById('qbProgress'),
      correct: document.getElementById('qbCorrect'),
      scoreEl: document.getElementById('qbScore'),
      card: document.getElementById('qbCard'),
      typeTag: document.getElementById('qbTypeTag'),
      text: document.getElementById('qbText'),
      content: document.getElementById('qbContent'),
      feedback: document.getElementById('qbFeedback'),
      prevBtn: document.getElementById('qbPrev'),
      submitBtn: document.getElementById('qbSubmit'),
      nextBtn: document.getElementById('qbNext'),
      restartBtn: document.getElementById('qbRestart'),
      summary: document.getElementById('qbSummary')
    };
    
    this.init();
  }
  
  init() {
    // 绑定模式切换
    this.elements.modeTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        this.elements.modeTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        this.currentMode = tab.dataset.qmode;
        this.reset();
      });
    });
    
    // 绑定题型筛选
    this.elements.filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        this.elements.filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.currentFilter = btn.dataset.qfilter;
        this.reset();
      });
    });
    
    // 绑定按钮事件
    this.elements.prevBtn.addEventListener('click', () => this.prevQuestion());
    this.elements.submitBtn.addEventListener('click', () => this.handleSubmit());
    this.elements.nextBtn.addEventListener('click', () => this.nextQuestion());
    this.elements.restartBtn.addEventListener('click', () => this.reset());
    
    // 恢复进度
    this.restoreProgress();
    
    // 初始化显示
    this.updateStats();
  }
  
  // 获取筛选后的题目
  getFilteredQuestions() {
    let questions = [];
    
    // 合并所有题型
    Object.keys(this.questionBank).forEach(type => {
      this.questionBank[type].forEach(q => {
        questions.push({ ...q, type });
      });
    });
    
    // 按题型筛选
    if (this.currentFilter !== 'all') {
      questions = questions.filter(q => q.type === this.currentFilter);
    }
    
    return questions;
  }
  
  // 开始答题
  start() {
    this.questions = this.getFilteredQuestions();
    this.totalQuestions = this.questions.length;
    this.currentQuestionIndex = 0;
    this.answers = {};
    this.score = 0;
    this.correctCount = 0;
    
    if (this.totalQuestions === 0) {
      this.elements.text.textContent = '没有找到符合条件的题目。';
      return;
    }
    
    // 随机模式打乱顺序
    if (this.currentMode === 'random') {
      this.shuffleArray(this.questions);
      this.questions = this.questions.slice(0, Math.min(10, this.totalQuestions));
      this.totalQuestions = this.questions.length;
    }
    
    this.showQuestion();
    this.updateStats();
    this.updateButtons();
  }
  
  // 重置
  reset() {
    this.questions = [];
    this.answers = {};
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.correctCount = 0;
    
    this.elements.text.textContent = '请选择题型和模式，点击"开始"按钮。';
    this.elements.content.innerHTML = '';
    this.elements.feedback.innerHTML = '';
    this.elements.feedback.className = 'qb-feedback';
    this.elements.summary.innerHTML = '';
    
    this.updateStats();
    this.updateButtons();
    
    // 重置提交按钮
    this.elements.submitBtn.textContent = '开始答题';
    this.elements.submitBtn.disabled = false;
  }
  
  // 显示题目
  showQuestion() {
    if (this.currentQuestionIndex >= this.totalQuestions) {
      this.showSummary();
      return;
    }
    
    const question = this.questions[this.currentQuestionIndex];
    
    // 更新题型标签
    this.updateTypeTag(question.type);
    
    // 显示题目文本
    this.elements.text.textContent = question.question;
    
    // 显示题目内容
    this.renderQuestionContent(question);
    
    // 清空反馈
    this.elements.feedback.innerHTML = '';
    this.elements.feedback.className = 'qb-feedback';
    
    // 恢复之前的答案
    if (this.answers[this.currentQuestionIndex] !== undefined) {
      this.showAnsweredState(question, this.answers[this.currentQuestionIndex]);
    }
    
    this.updateStats();
    this.updateButtons();
  }
  
  // 渲染题目内容
  renderQuestionContent(question) {
    const content = this.elements.content;
    content.innerHTML = '';
    
    switch (question.type) {
      case 'choice':
        this.renderChoiceQuestion(question, content);
        break;
      case 'tf':
        this.renderTFQuestion(question, content);
        break;
      case 'calc':
        this.renderCalcQuestion(question, content);
        break;
      case 'short':
        this.renderShortQuestion(question, content);
        break;
      case 'material':
        this.renderMaterialQuestion(question, content);
        break;
    }
    
    // 添加提示按钮
    if (question.hint) {
      const hintBtn = document.createElement('button');
      hintBtn.className = 'quiz-hint-btn';
      hintBtn.textContent = '💡 看提示';
      hintBtn.addEventListener('click', () => this.showHint(question.hint));
      content.appendChild(hintBtn);
    }
  }
  
  // 渲染选择题
  renderChoiceQuestion(question, container) {
    const optionsDiv = document.createElement('div');
    optionsDiv.className = 'qb-options';
    
    question.options.forEach((option, index) => {
      const optionDiv = document.createElement('div');
      optionDiv.className = 'qb-option';
      optionDiv.dataset.index = index;
      
      const marker = document.createElement('div');
      marker.className = 'qb-option-marker';
      marker.textContent = String.fromCharCode(65 + index); // A, B, C, D
      
      const text = document.createElement('span');
      text.textContent = option;
      
      optionDiv.appendChild(marker);
      optionDiv.appendChild(text);
      
      optionDiv.addEventListener('click', () => {
        if (this.answers[this.currentQuestionIndex] === undefined) {
          this.selectOption(index);
        }
      });
      
      optionsDiv.appendChild(optionDiv);
    });
    
    container.appendChild(optionsDiv);
  }
  
  // 渲染判断题
  renderTFQuestion(question, container) {
    const tfDiv = document.createElement('div');
    tfDiv.className = 'qb-tf-btns';
    
    ['正确', '错误'].forEach((label, index) => {
      const btn = document.createElement('button');
      btn.className = 'qb-tf-btn';
      btn.textContent = label;
      btn.dataset.value = index === 0 ? 'true' : 'false';
      
      btn.addEventListener('click', () => {
        if (this.answers[this.currentQuestionIndex] === undefined) {
          this.selectTF(index === 0);
        }
      });
      
      tfDiv.appendChild(btn);
    });
    
    container.appendChild(tfDiv);
  }
  
  // 渲染计算题
  renderCalcQuestion(question, container) {
    const calcDiv = document.createElement('div');
    calcDiv.className = 'qb-calc-problem';
    
    if (question.given) {
      const givenDiv = document.createElement('div');
      givenDiv.className = 'qb-calc-given';
      givenDiv.innerHTML = `<strong>已知条件：</strong>${question.given}`;
      calcDiv.appendChild(givenDiv);
    }
    
    if (question.steps) {
      const stepsDiv = document.createElement('div');
      stepsDiv.className = 'qb-calc-steps';
      
      question.steps.forEach((step, index) => {
        const stepDiv = document.createElement('div');
        stepDiv.className = 'qb-calc-step';
        stepDiv.innerHTML = `
          <div class="qb-calc-step-title">第${index + 1}步：${step.title}</div>
          <div>${step.content}</div>
        `;
        stepsDiv.appendChild(stepDiv);
      });
      
      calcDiv.appendChild(stepsDiv);
    }
    
    container.appendChild(calcDiv);
  }
  
  // 渲染简答题
  renderShortQuestion(question, container) {
    const shortDiv = document.createElement('div');
    shortDiv.className = 'qb-answer-reveal';
    shortDiv.innerHTML = '<strong>参考答案：</strong><br>' + question.answer;
    shortDiv.style.display = 'none';
    shortDiv.id = 'shortAnswer';
    container.appendChild(shortDiv);
    
    const showBtn = document.createElement('button');
    showBtn.className = 'btn';
    showBtn.textContent = '显示答案';
    showBtn.addEventListener('click', () => {
      shortDiv.style.display = shortDiv.style.display === 'none' ? 'block' : 'none';
      showBtn.textContent = shortDiv.style.display === 'none' ? '显示答案' : '隐藏答案';
    });
    container.appendChild(showBtn);
  }
  
  // 渲染材料分析题
  renderMaterialQuestion(question, container) {
    if (question.material) {
      const materialDiv = document.createElement('div');
      materialDiv.className = 'qb-material-box';
      materialDiv.innerHTML = `
        <div class="qb-material-title">📄 材料</div>
        <div class="qb-material-content">${question.material}</div>
      `;
      container.appendChild(materialDiv);
    }
    
    if (question.subQuestions) {
      const subDiv = document.createElement('div');
      subDiv.className = 'qb-material-questions';
      
      question.subQuestions.forEach((sub, index) => {
        const subItem = document.createElement('div');
        subItem.className = 'qb-material-subq';
        subItem.innerHTML = `
          <div class="qb-material-subq-title">问题${index + 1}：${sub.question}</div>
          <div class="qb-material-answer" id="subAnswer${index}">
            <strong>参考答案：</strong>${sub.answer}
          </div>
          <div class="qb-material-toggle" onclick="this.previousElementSibling.classList.toggle('show')">
            显示/隐藏答案
          </div>
        `;
        subDiv.appendChild(subItem);
      });
      
      container.appendChild(subDiv);
    }
  }
  
  // 选择选项
  selectOption(index) {
    const question = this.questions[this.currentQuestionIndex];
    this.answers[this.currentQuestionIndex] = index;
    
    // 检查答案
    const isCorrect = index === question.answer;
    if (isCorrect) {
      this.correctCount++;
      this.score += question.score || 10;
    }
    
    // 显示答案状态
    this.showAnsweredState(question, index);
    
    // 显示反馈
    this.showFeedback(isCorrect, question.explanation);
    
    // 更新按钮
    this.updateButtons();
  }
  
  // 选择判断
  selectTF(value) {
    const question = this.questions[this.currentQuestionIndex];
    this.answers[this.currentQuestionIndex] = value;
    
    // 检查答案
    const isCorrect = value === question.answer;
    if (isCorrect) {
      this.correctCount++;
      this.score += question.score || 10;
    }
    
    // 显示答案状态
    this.showAnsweredState(question, value);
    
    // 显示反馈
    this.showFeedback(isCorrect, question.explanation);
    
    // 更新按钮
    this.updateButtons();
  }
  
  // 显示已答状态
  showAnsweredState(question, answer) {
    if (question.type === 'choice') {
      const options = this.elements.content.querySelectorAll('.qb-option');
      options.forEach((opt, index) => {
        opt.classList.remove('selected', 'correct', 'wrong');
        if (index === answer) {
          opt.classList.add(answer === question.answer ? 'correct' : 'wrong');
        }
        if (index === question.answer) {
          opt.classList.add('correct');
        }
      });
    } else if (question.type === 'tf') {
      const btns = this.elements.content.querySelectorAll('.qb-tf-btn');
      btns.forEach(btn => {
        btn.classList.remove('selected-true', 'selected-false');
        const isTrue = btn.dataset.value === 'true';
        if (isTrue === answer) {
          btn.classList.add(answer ? 'selected-true' : 'selected-false');
        }
      });
    }
  }
  
  // 显示反馈
  showFeedback(isCorrect, explanation) {
    this.elements.feedback.className = 'qb-feedback ' + (isCorrect ? 'correct' : 'wrong');
    this.elements.feedback.innerHTML = `
      <strong>${isCorrect ? '✅ 回答正确！' : '❌ 回答错误'}</strong>
      ${explanation ? '<br>' + explanation : ''}
    `;
  }
  
  // 显示提示
  showHint(hint) {
    const existingHint = this.elements.content.querySelector('.quiz-hint-content');
    if (existingHint) {
      existingHint.remove();
      return;
    }
    
    const hintDiv = document.createElement('div');
    hintDiv.className = 'quiz-hint-content';
    hintDiv.innerHTML = `<strong>💡 提示：</strong>${hint}`;
    this.elements.content.appendChild(hintDiv);
  }
  
  // 上一题
  prevQuestion() {
    if (this.currentQuestionIndex > 0) {
      this.currentQuestionIndex--;
      this.showQuestion();
    }
  }
  
  // 下一题
  nextQuestion() {
    if (this.currentQuestionIndex < this.totalQuestions - 1) {
      this.currentQuestionIndex++;
      this.showQuestion();
    } else if (this.currentMode === 'exam') {
      this.showSummary();
    }
  }
  
  // 处理提交
  handleSubmit() {
    if (this.questions.length === 0) {
      this.start();
      return;
    }
    
    const question = this.questions[this.currentQuestionIndex];
    
    // 如果已经答过，跳到下一题
    if (this.answers[this.currentQuestionIndex] !== undefined) {
      this.nextQuestion();
      return;
    }
    
    // 对于简答题和材料题，直接显示答案
    if (question.type === 'short' || question.type === 'material') {
      this.answers[this.currentQuestionIndex] = true;
      this.correctCount++;
      this.score += question.score || 10;
      
      if (question.type === 'short') {
        const answerEl = document.getElementById('shortAnswer');
        if (answerEl) answerEl.style.display = 'block';
      }
      
      this.showFeedback(true, '已显示参考答案，请自行对照。');
      this.updateButtons();
    }
  }
  
  // 显示总结
  showSummary() {
    const percent = Math.round((this.correctCount / this.totalQuestions) * 100);
    
    this.elements.summary.innerHTML = `
      <div class="card" style="margin-top:20px;">
        <h3>📊 答题总结</h3>
        <div class="dashboard" style="margin-top:16px;">
          <div class="stat-card">
            <div class="stat-number">${this.totalQuestions}</div>
            <div class="stat-label">总题数</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">${this.correctCount}</div>
            <div class="stat-label">答对题数</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">${percent}%</div>
            <div class="stat-label">正确率</div>
          </div>
        </div>
        <div class="progress-wrap" style="margin-top:16px;">
          <div class="progress-bar" style="width:${percent}%"></div>
        </div>
        <p style="margin-top:16px;">
          ${percent >= 80 ? '🎉 优秀！你已经掌握了这些知识点！' : 
            percent >= 60 ? '👍 不错！继续努力，巩固薄弱环节。' : 
            '💪 加油！建议回顾相关章节，重新学习。'}
        </p>
        <button class="btn" onclick="location.reload()" style="margin-top:12px;">🔄 重新开始</button>
      </div>
    `;
    
    // 保存进度
    this.saveProgress();
    
    // 隐藏题目卡片
    this.elements.card.style.display = 'none';
  }
  
  // 更新统计
  updateStats() {
    this.elements.progress.textContent = `${this.currentQuestionIndex + 1}/${this.totalQuestions}`;
    this.elements.correct.textContent = `${this.correctCount}/${this.totalQuestions}`;
    this.elements.scoreEl.textContent = this.totalQuestions > 0 ? 
      `${Math.round((this.correctCount / this.totalQuestions) * 100)}%` : '—';
  }
  
  // 更新按钮状态
  updateButtons() {
    this.elements.prevBtn.disabled = this.currentQuestionIndex === 0;
    this.elements.nextBtn.disabled = this.currentQuestionIndex >= this.totalQuestions - 1;
    
    if (this.answers[this.currentQuestionIndex] !== undefined) {
      this.elements.submitBtn.textContent = '下一题';
      this.elements.submitBtn.disabled = this.currentQuestionIndex >= this.totalQuestions - 1;
    } else {
      this.elements.submitBtn.textContent = '提交答案';
      this.elements.submitBtn.disabled = false;
    }
  }
  
  // 更新题型标签
  updateTypeTag(type) {
    const typeNames = {
      choice: '选择题',
      tf: '判断题',
      calc: '计算题',
      short: '简答题',
      material: '材料分析题'
    };
    
    this.elements.typeTag.className = `qb-question-type qb-type-${type}`;
    this.elements.typeTag.textContent = typeNames[type] || type;
  }
  
  // 打乱数组
  shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
  
  // 保存进度
  saveProgress() {
    try {
      const data = {
        score: this.score,
        correctCount: this.correctCount,
        totalQuestions: this.totalQuestions,
        timestamp: Date.now()
      };
      localStorage.setItem(this.courseSlug + '_quiz_progress', JSON.stringify(data));
    } catch(e) {}
  }
  
  // 恢复进度
  restoreProgress() {
    try {
      const data = JSON.parse(localStorage.getItem(this.courseSlug + '_quiz_progress'));
      if (data && data.timestamp > Date.now() - 24 * 60 * 60 * 1000) {
        // 24小时内的进度有效
        this.score = data.score;
        this.correctCount = data.correctCount;
        this.totalQuestions = data.totalQuestions;
      }
    } catch(e) {}
  }
}

// ==================== 题库数据结构示例 ====================
/*
const questionBank = {
  choice: [
    {
      id: 1,
      question: "题目内容",
      options: ["A选项", "B选项", "C选项", "D选项"],
      answer: 0, // 正确答案索引（0=A, 1=B, 2=C, 3=D）
      explanation: "解析内容",
      hint: "提示内容",
      score: 10,
      chapter: "第1章",
      difficulty: "easy" // easy, medium, hard
    }
  ],
  tf: [
    {
      id: 1,
      question: "判断题内容",
      answer: true, // true=正确, false=错误
      explanation: "解析内容",
      hint: "提示内容",
      score: 5
    }
  ],
  calc: [
    {
      id: 1,
      question: "计算题题目",
      given: "已知条件",
      steps: [
        { title: "步骤标题", content: "步骤内容" }
      ],
      answer: "最终答案",
      explanation: "解析内容",
      hint: "提示内容",
      score: 20
    }
  ],
  short: [
    {
      id: 1,
      question: "简答题题目",
      answer: "参考答案内容",
      hint: "提示内容",
      score: 15
    }
  ],
  material: [
    {
      id: 1,
      question: "材料分析题题目",
      material: "材料内容",
      subQuestions: [
        {
          question: "子问题1",
          answer: "参考答案1"
        },
        {
          question: "子问题2",
          answer: "参考答案2"
        }
      ],
      score: 25
    }
  ]
};
*/

// ==================== 使用示例 ====================
/*
// 1. 准备题库数据
const myQuestionBank = {
  choice: [...],
  tf: [...],
  calc: [...],
  short: [...],
  material: [...]
};

// 2. 初始化题库系统
const quizSystem = new QuizSystem(myQuestionBank, 'my-course');

// 3. 题库系统会自动绑定DOM元素和事件
// 用户可以通过界面操作进行答题
*/
