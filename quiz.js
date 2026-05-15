// ── KVÍZ LOGIKA ───────────────────────────────────────────────────────────────
let quizLesson = null;
let quizQ = 0;
let quizCorrect = 0;
let quizXP = 0;
let quizAnswered = false;
const LETTERS = ['A', 'B', 'C', 'D'];
 
function startLesson(unitId, lessonIndex) {
  const unit   = UNITS.find(u => u.id === unitId);
  const lesson = unit.lessons[lessonIndex];
 
  if (!isLessonUnlocked(appState, unitId, lessonIndex)) return;
 
  quizLesson   = lesson;
  quizQ        = 0;
  quizCorrect  = 0;
  quizXP       = 0;
  quizAnswered = false;
 
  goTo('quiz');
  renderQuestion();
}
 
function renderQuestion() {
  const q     = quizLesson.questions[quizQ];
  const total = quizLesson.questions.length;
  const pct   = Math.round((quizQ / total) * 100);
 
  document.getElementById('qprog').style.width = pct + '%';
  document.getElementById('q-xp').textContent  = quizXP;
  document.getElementById('q-num').textContent = `${quizQ + 1} / ${total}`;
  document.getElementById('q-text').textContent = q.q;
 
  const fb = document.getElementById('q-feedback');
  fb.style.display = 'none';
  fb.className = 'feedback';
  document.getElementById('q-next').style.display = 'none';
  quizAnswered = false;
 
  const div = document.getElementById('q-answers');
  div.innerHTML = '';
  q.answers.forEach((a, i) => {
    const btn = document.createElement('button');
    btn.className = 'ans-btn';
    btn.innerHTML = `<span class="ans-letter">${LETTERS[i]}</span><span>${a}</span>`;
    btn.onclick = () => selectAnswer(i);
    div.appendChild(btn);
  });
}
 
function selectAnswer(idx) {
  if (quizAnswered) return;
  quizAnswered = true;
 
  const q    = quizLesson.questions[quizQ];
  const btns = document.querySelectorAll('.ans-btn');
  btns.forEach(b => b.disabled = true);
 
  const isCorrect = idx === q.correct;
  btns[idx].classList.add(isCorrect ? 'correct' : 'wrong');
  if (!isCorrect) btns[q.correct].classList.add('correct');
 
  if (isCorrect) {
    quizCorrect++;
    quizXP += 10;
    document.getElementById('q-xp').textContent = quizXP;
  }
 
  const fb = document.getElementById('q-feedback');
  fb.style.display = 'block';
  fb.className = 'feedback ' + (isCorrect ? 'fb-ok' : 'fb-bad');
  fb.innerHTML = (isCorrect ? '✅ <strong>Správne!</strong> ' : '❌ <strong>Nesprávne.</strong> ') + q.explanation;
  document.getElementById('q-next').style.display = 'block';
}
 
function nextQ() {
  quizQ++;
  if (quizQ >= quizLesson.questions.length) {
    finishLesson();
  } else {
    renderQuestion();
  }
}
 
function replayLesson() {
  quizQ        = 0;
  quizCorrect  = 0;
  quizXP       = 0;
  quizAnswered = false;
  goTo('quiz');
  renderQuestion();
}
 
function finishLesson() {
  appState = completeLesson(appState, quizLesson.id, quizXP);
  appState = updateStreak(appState);
 
  // Aktualizuj UI hodnoty
  updateTopbar();
 
  const acc = Math.round((quizCorrect / quizLesson.questions.length) * 100);
  document.getElementById('d-xp').textContent     = '+' + quizXP;
  document.getElementById('d-acc').textContent    = acc + '%';
  document.getElementById('d-streak').textContent = '🔥 ' + appState.streak;
 
  goTo('done');
}