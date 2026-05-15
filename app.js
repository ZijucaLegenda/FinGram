// ── DATA ──────────────────────────────────────────────────────────────────────
const lessons = [
  {
    title: "Čo je sporenie?",
    category: "Základy financií",
    questions: [
      {
        q: "Čo znamená pojem 'nouzový fond'?",
        answers: [
          "Peniaze na luxusné nákupy",
          "Rezerva na neočakávané výdavky (oprava, choroba)",
          "Investícia do akcií",
          "Výplata vopred od zamestnávateľa"
        ],
        correct: 1,
        explanation: "Správne! Nouzový fond je rezerva zvyčajne 3–6 mesačných výdavkov pre prípad výpadku príjmu, opravy auta alebo chorôb."
      },
      {
        q: "Aké je odporúčané pravidlo pre mesačné sporenie?",
        answers: [
          "Sporiť 2 % príjmu",
          "Sporiť len keď zostanú peniaze",
          "Sporiť 10–20 % príjmu",
          "Nesporiť, investovať všetko"
        ],
        correct: 2,
        explanation: "Odborníci odporúčajú odkladať 10–20 % mesačného príjmu. Kľúčová je pravidelnosť – hoci len 10 € mesačne je lepšie ako nič."
      },
      {
        q: "Čo je výhodnejšie – sporenie na bežnom alebo sporiacom účte?",
        answers: [
          "Bežný účet, lebo je prístupnejší",
          "Sporiaci účet, lebo ponúka vyšší úrok",
          "Je to úplne jedno",
          "Lepšie je mať hotovosť doma"
        ],
        correct: 1,
        explanation: "Sporiaci účet zhodnotí peniaze o úrok. Na bežnom účte nič nezarobiš. Oba sú dostupné, ale sporiaci ti pomáha rásť."
      },
      {
        q: "Prečo je dobré mať konkrétne finančné ciele?",
        answers: [
          "Nie sú potrebné, stačí sporiť naslepo",
          "Pomáhajú motivovať a určiť sumu sporenia",
          "Finančné ciele sú len pre bohatých",
          "Ciele zvyšujú daňovú povinnosť"
        ],
        correct: 1,
        explanation: "Konkrétny cieľ (napr. '1 000 € za 10 mesiacov') ťa motivuje a ľahko si vypočítaš 100 € mesačne."
      }
    ]
  },
  {
    title: "Úrok a inflácia",
    category: "Sporenie",
    questions: [
      {
        q: "Čo je inflácia?",
        answers: [
          "Rast cien tovarov a služieb v čase",
          "Pokles hodnoty akcií",
          "Zvyšovanie miezd",
          "Znižovanie daní"
        ],
        correct: 0,
        explanation: "Inflácia = rast cien. Za rovnaké peniaze kúpiš menej ako predtým. Ak sporenie zarába menej ako inflácia, tvoje úspory reálne strácajú hodnotu."
      },
      {
        q: "Čo je zložený úrok (compound interest)?",
        answers: [
          "Úrok platený štátom",
          "Úrok z úroku – zarábate aj zo svojich úrokov",
          "Pokuta za neskoré platenie",
          "Poplatok za vedenie účtu"
        ],
        correct: 1,
        explanation: "Zložený úrok rastie exponenciálne! 1 000 € → po roku 1 050 € → ďalší rok 5 % z 1 050 €, nie z 1 000 €. Časom je efekt obrovský!"
      },
      {
        q: "Máš 500 € na sporiacom účte s ročným úrokom 3 %. Koľko budeš mať po 1 roku?",
        answers: ["500 €", "503 €", "515 €", "550 €"],
        correct: 2,
        explanation: "500 × 0,03 = 15 €. Po roku = 515 €. Pri väčších sumách a dlhšom čase je efekt obrovský."
      },
      {
        q: "Reálny výnos sporenia je kladný, keď...",
        answers: [
          "Úroková sadzba je vyššia ako inflácia",
          "Máš viac ako 10 účtov",
          "Sporenie trvá menej ako rok",
          "Úroková sadzba je nulová"
        ],
        correct: 0,
        explanation: "Reálny výnos = úrok − inflácia. Úrok 4 % − inflácia 2 % = reálny zisk 2 %. Úrok 1 % − inflácia 3 % = reálna strata 2 %."
      }
    ]
  }
];
 
// ── STATE ──────────────────────────────────────────────────────────────────────
let streak = 6;
let xp = 320;
let currentLesson = 0;
let currentQ = 0;
let correctCount = 0;
let earnedXP = 0;
let answered = false;
 
const letters = ['A', 'B', 'C', 'D'];
 
// ── NAVIGATION ─────────────────────────────────────────────────────────────────
function goTo(screen) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + screen).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const navEl = document.getElementById('nav-' + screen);
  if (navEl) navEl.classList.add('active');
}
 
// ── QUIZ ───────────────────────────────────────────────────────────────────────
function startLesson(idx) {
  currentLesson = idx;
  currentQ = 0;
  correctCount = 0;
  earnedXP = 0;
  answered = false;
  goTo('quiz');
  renderQuestion();
}
 
function replayLesson() {
  startLesson(currentLesson);
}
 
function renderQuestion() {
  const lesson = lessons[currentLesson];
  const q = lesson.questions[currentQ];
  const total = lesson.questions.length;
  const pct = Math.round((currentQ / total) * 100);
 
  document.getElementById('qprog').style.width = pct + '%';
  document.getElementById('q-xp').textContent = earnedXP;
  document.getElementById('q-cat').textContent = lesson.category;
  document.getElementById('q-text').textContent = q.q;
 
  const fb = document.getElementById('q-feedback');
  fb.style.display = 'none';
  fb.className = 'feedback';
 
  document.getElementById('q-next').style.display = 'none';
  answered = false;
 
  const answersDiv = document.getElementById('q-answers');
  answersDiv.innerHTML = '';
  q.answers.forEach((a, i) => {
    const btn = document.createElement('button');
    btn.className = 'ans-btn';
    btn.innerHTML = `<span class="ans-letter">${letters[i]}</span><span>${a}</span>`;
    btn.onclick = () => selectAnswer(i);
    answersDiv.appendChild(btn);
  });
}
 
function selectAnswer(idx) {
  if (answered) return;
  answered = true;
 
  const q = lessons[currentLesson].questions[currentQ];
  const btns = document.querySelectorAll('.ans-btn');
  btns.forEach(b => b.disabled = true);
 
  const isCorrect = idx === q.correct;
  btns[idx].classList.add(isCorrect ? 'correct' : 'wrong');
  if (!isCorrect) btns[q.correct].classList.add('correct');
 
  if (isCorrect) {
    correctCount++;
    earnedXP += 10;
    document.getElementById('q-xp').textContent = earnedXP;
  }
 
  const fb = document.getElementById('q-feedback');
  fb.style.display = 'block';
  fb.className = 'feedback ' + (isCorrect ? 'fb-ok' : 'fb-bad');
  fb.innerHTML = (isCorrect ? '✅ <strong>Správne!</strong> ' : '❌ <strong>Nesprávne.</strong> ') + q.explanation;
 
  document.getElementById('q-next').style.display = 'block';
}
 
function nextQ() {
  const lesson = lessons[currentLesson];
  currentQ++;
  if (currentQ >= lesson.questions.length) {
    finishLesson();
  } else {
    renderQuestion();
  }
}
 
function finishLesson() {
  streak++;
  xp += earnedXP;
 
  document.getElementById('s-streak').textContent = streak;
  document.getElementById('s-xp').textContent = xp;
  document.getElementById('p-streak').textContent = streak;
  document.getElementById('p-xp').textContent = xp;
  document.getElementById('m-xp').textContent = xp;
 
  document.getElementById('d-xp').textContent = '+' + earnedXP;
  const acc = Math.round((correctCount / lessons[currentLesson].questions.length) * 100);
  document.getElementById('d-acc').textContent = acc + '%';
  document.getElementById('d-streak').textContent = '🔥 ' + streak;
 
  goTo('done');
}