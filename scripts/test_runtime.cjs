/* Exercise the actual template modules, without a browser or external service. */
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const html = fs.readFileSync(path.join(__dirname, '../template.html'), 'utf8');
const contract = JSON.parse(html.match(/id="courseReviewContract">\s*([\s\S]*?)<\/script>/)[1]);
function code(start, end) {
  const a=html.indexOf(start), b=html.indexOf(end,a);
  assert(a>=0 && b>a, `Missing module ${start}`); return html.slice(a,b);
}
function setup() {
  const store=new Map();
  const ctx={Date,Math,JSON,console, REVIEW_CONTRACT:contract,
    COURSE_META:{courseName:'Test course',courseSlug:'test',courseType:'quantitative',evidenceLevel:'generic',coverageMode:'standard-coverage',remainingMinutes:60},
    knowledgeGraph:[{id:'c1',name:'Concept one',chapter:1,prereqs:[]},{id:'c2',name:'Concept two',chapter:2,prereqs:['c1']},{id:'c3',name:'Excluded concept',chapter:3,prereqs:[]}],
    LS:k=>'test_'+k,
    lsGet:(k,d)=>store.has('test_'+k)?JSON.parse(store.get('test_'+k)):d,
    lsSet:(k,v)=>store.set('test_'+k,JSON.stringify(v)),
    localStorage:{getItem:k=>store.get(k)||null,setItem:(k,v)=>store.set(k,v)},
    window:{},scrollToSection:id=>{ctx.scrolled=id;},setTimeout:()=>{ctx.timers++;},timers:0};
  vm.createContext(ctx);
  vm.runInContext(code('var LearningMemory = (function(){','(function renderEvidenceNotice'),ctx);
  vm.runInContext(code('var PromptGeneratorV5 = {','var QuestionImporter ='),ctx);
  vm.runInContext(code('var LearningFlow = {','(function setupLearningFlow'),ctx);
  return ctx;
}
function attempt(c,id='q1',correct=false,hint=false,source='source',concept='c1') {
  c.LearningMemory.recordAttempt({id,conceptIds:[concept],chapter:1,difficulty:'easy',sourceBasis:source},correct,hint,true);
}
test('all prompt ranges use finite concept summaries, exclude opted-out topics',()=>{
  const c=setup();attempt(c);c.LearningMemory.confirmError('q1','concept');
  attempt(c,'excluded-wrong',false,false,'source','c3');c.LearningMemory.confirmError('excluded-wrong','concept');
  c.LearningMemory.recordMastery('c3','excluded','not examined');
  for(const range of ['weak','wrong','all']) {
    const context=c.PromptGenerator.collectContext({range});
    assert(context.targets.every(t=>Number.isFinite(t.independentAccuracy)||t.independentAccuracy===null));
    assert(!context.targets.some(t=>t.id==='c3'));
    for(const output of ['dialogue','agent-json']) {
      const prompt=c.PromptGenerator.build({range,output});
      assert(!/undefined|NaN|Infinity/.test(prompt));
    }
  }
});
test('empty history is unknown, not an invented accuracy or weakness',()=>{
  const c=setup(),ctx=c.PromptGenerator.collectContext({range:'wrong'});
  assert.equal(ctx.observedAccuracy,null);assert(ctx.targets.every(t=>t.state==='unseen'));
  assert(c.PromptGenerator.build({}).includes('insufficient data'));
});
test('default dialogue does not demand return, JSON, or an answer dump',()=>{
  const c=setup(),p=c.PromptGenerator.build({});
  assert(p.includes('一次只出一道'));assert(p.includes('等待我作答'));
  assert(p.includes('无需返回HTML'));assert(p.includes('不会自动更新'));
  assert(!p.includes('Return only a valid JSON array'));
  assert(c.PromptGenerator.build({output:'agent-json'}).includes('Return only a valid JSON array'));
});
test('help intents differ, shared problem needs opt-in, anonymous by default',()=>{
  const c=setup();c.COURSE_META.studentName='PRIVATE_NAME';c.COURSE_META.school='PRIVATE_SCHOOL';
  const explain=c.PromptGenerator.build({intent:'explain',problemText:'PRIVATE_PROBLEM'});
  const prereq=c.PromptGenerator.build({intent:'prerequisite'});
  assert(explain.includes('解释我卡住的一步'));assert(prereq.includes('最小前置知识'));
  assert(!explain.includes('PRIVATE_'));
  assert(c.PromptGenerator.build({intent:'explain',shareProblem:true,problemText:'SHARED_STEP'}).includes('SHARED_STEP'));
});
test('local errors and hints change the next handoff, without erasing attempts',()=>{
  const c=setup(),before=c.PromptGenerator.build({});
  attempt(c,'q1',false,true);c.LearningMemory.confirmError('q1','concept');
  const after=c.PromptGenerator.build({});assert.notEqual(before,after);
  assert(after.includes('hint uses=1'));assert(after.includes('concept:1'));
  assert.equal(c.LearningMemory.get().attempts.length,1);
});
test('AI practice events and error selections cannot change concept evidence',()=>{
  const c=setup();attempt(c);const before=JSON.stringify(c.LearningMemory.get().concepts);
  attempt(c,'ai1',true,false,'ai-import');c.LearningMemory.confirmError('ai1','concept');
  assert.equal(JSON.stringify(c.LearningMemory.get().concepts),before);
  assert.equal(c.LearningMemory.get().attempts.length,2);
  assert.equal(c.LearningMemory.get().attempts[1].affectsMastery,false);
});
test('single answer or explicit promotion cannot manufacture mastery',()=>{
  const c=setup();attempt(c,'q1',true);
  c.LearningMemory.recordMastery('c1','provisional','micro-check');assert.equal(c.LearningMemory.get().concepts.c1.state,'learning');
  c.LearningMemory.recordMastery('c1','mastered');assert.equal(c.LearningMemory.get().concepts.c1.state,'learning');
  attempt(c,'q2',true);attempt(c,'q3',true);
  assert.notEqual(c.LearningMemory.get().concepts.c1.state,'mastered');
});
test('mastery can advance with real independent successes over the required gap',()=>{
  const c=setup();let now=Date.now();c.Date={now:()=>now};
  attempt(c,'q1',true);now+=6*60*1000;attempt(c,'q2',true);
  assert.equal(c.LearningMemory.get().concepts.c1.state,'provisional');
  now+=25*60*1000;attempt(c,'q3',true);assert.equal(c.LearningMemory.get().concepts.c1.state,'mastered');
});
test('canonical evidence drives recommendations and saved local task wins',()=>{
  const c=setup();attempt(c,'q2',false,false,'source','c2');
  assert.equal(c.LearningFlow.recommend(c.LearningMemory.get()).id,'c2');
  const profile=c.LearningMemory.get();profile.preferences.resumeObjectiveId='c1';c.LearningMemory.save(profile);
  assert.equal(c.LearningFlow.recommend(c.LearningMemory.get()).id,'c1');
  c.LearningMemory.recordMastery('c1','excluded');assert.equal(c.LearningFlow.recommend(c.LearningMemory.get()).id,'c2');
});
test('starting a chapter saves the task without scheduling a popup',()=>{
  const c=setup();vm.runInContext(code('window.startLearn = function(nodeId){','function showMicroQuiz'),c);
  c.window.startLearn('c2');assert.equal(c.timers,0);assert.equal(c.scrolled,'concept-ch2');
  assert.equal(c.LearningMemory.get().preferences.resumeObjectiveId,'c2');
  assert.equal(c.LearningMemory.get().preferences.resumeSection,'concept-ch2');
});
test('legacy state migrates once and later legacy mutations cannot override canonical state',()=>{
  const c=setup();c.lsSet('ap',{c1:'mastered'});const first=c.LearningMemory.get();
  assert.notEqual(first.concepts.c1.state,'mastered');
  c.lsSet('ap',{c2:'mastered'});assert.equal(c.LearningMemory.get().concepts.c2.state,'unseen');
  assert.equal(c.LearningMemory.get().preferences.feedbackMode,'quiet');
});
