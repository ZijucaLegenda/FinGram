with open('/mnt/user-data/outputs/fingram/app.html', 'r', encoding='utf-8') as f:
    existing = f.read()
 
# Extract just the UNITS array start through whatever we have
# Find start of const UNITS
units_start = existing.index('const UNITS = [')
partial_units = existing[units_start:]
 
# We need to complete units 5 lessons 2-5, add REAL_LIFE, and all logic
# Build the completion
completion = r"""
    { id:"5-2", title:"II. a III. pilier", icon:"💼", questions:[
      {q:"Čo je II. pilier?", answers:["Dobrovoľné sporenie","5,5 % z hrubej mzdy ide na tvoj osobný účet v DSS","Štátna dávka","Životné poistenie"], correct:1, explanation:"II. pilier: 5,5 % z hrubej mzdy ide do DSS na tvoj osobný účet. Peniaze sú tvoje – zdedia sa a nie sú v štátnom systéme."},
      {q:"Čo je III. pilier?", answers:["Štátny dôchodok","Dobrovoľné doplnkové dôchodkové sporenie s daňovým odpočtom 180 € ročne","Povinné sporenie","Životné poistenie"], correct:1, explanation:"III. pilier je dobrovoľný. Príspevky do 180 € ročne si môžeš odpočítať od základu dane. Ak prispieva aj zamestnávateľ – dvojitá výhoda."},
      {q:"Čo sa stane s peniazmi v II. pilieri ak zomrieš?", answers:["Prepadnú štátu","Zdedia sa – stávajú sa súčasťou dedičstva","Vrátia sa do Sociálnej poisťovne","Dostane ich zamestnávateľ"], correct:1, explanation:"Na rozdiel od I. piliera, peniaze v II. pilieri sú tvoje osobné – zdedia sa. Môžeš určiť oprávnenú osobu."},
      {q:"Kedy môžeš vybrať peniaze z III. piliera bez penalizácie?", answers:["Kedykoľvek","Po dovŕšení 55 rokov a min. 10 rokoch sporenia","Len pri odchode do dôchodku","Po 65 rokoch"], correct:1, explanation:"Peniaze z III. piliera môžeš vybrať bez penalizácie po 55 rokoch ak si sporil aspoň 10 rokov. Predčasný výber = 19 % daň."},
      {q:"Aká je optimálna dôchodková stratégia?", answers:["Len I. pilier stačí","II. pilier + III. pilier 180 € ročne + vlastné ETF investovanie","Len III. pilier","Len nehnuteľnosti"], correct:1, explanation:"Tri zdroje dôchodkového príjmu: II. pilier (povinné) + III. pilier (daňový odpočet) + vlastné ETF investovanie. Diversifikovaná stratégia."},
      {q:"Čo je indexový fond v DSS?", answers:["Fond s garantovaným výnosom","Fond kopírujúci akciový index s nízkymi poplatkami – historicky najlepšie výsledky","Bezrizikový fond","Fond investujúci len do SR"], correct:1, explanation:"Indexový fond v DSS má nízke poplatky a historicky prekonáva aktívne riadené fondy. Pre mladých ľudí s dlhým horizontom je to najlepšia voľba."},
      {q:"Koľko percent z hrubej mzdy ide do II. piliera?", answers:["2 %","3,5 %","5,5 %","10 %"], correct:2, explanation:"5,5 % z hrubej mzdy ide automaticky do tvojho účtu v DSS ak si vstúpil do II. piliera. Je to súčasť odvodov – neplatíš navyše."}
    ]},
    { id:"5-3", title:"Finančná sloboda", icon:"🦅", questions:[
      {q:"Čo je finančná sloboda?", answers:["Mať milión eur","Stav keď pasívny príjem pokrýva výdavky a nemusíš pracovať","Bezplatné bankové služby","Žiadne dlhy"], correct:1, explanation:"Finančná sloboda = tvoje investície generujú dostatok pasívneho príjmu. Nemusíš predávať čas za peniaze. Môžeš pracovať zo záľuby."},
      {q:"Čo je pravidlo 4 %?", answers:["Sporiť 4 % príjmu","Môžeš každý rok vybrať 4 % portfólia a s 95 % pravdepodobnosťou ti peniaze vydržia 30+ rokov","Úrok na sporiacom účte","DPH sadzba"], correct:1, explanation:"Pravidlo 4 % (Trinity Study): 500 000 € v akciách → môžeš ročne vybrať 20 000 € (4 %) a portfólio vydrží 30+ rokov."},
      {q:"Koľko potrebuješ pri výdavkoch 1 500 € mesačne?", answers:["180 000 €","300 000 €","450 000 €","1 500 000 €"], correct:2, explanation:"Pravidlo 4 %: ročné výdavky × 25 = cieľ. 1 500 × 12 = 18 000 × 25 = 450 000 €."},
      {q:"Čo je FIRE?", answers:["Požiar portfólia","Financial Independence Retire Early – agresívne sporenie na skorý dôchodok","Typ ETF","Daňová úspora"], correct:1, explanation:"FIRE: sporíš 50–70 % príjmu, investuješ do ETF, cielíš na finančnú slobodu v 35–50 rokoch."},
      {q:"Čo je pasívny príjem?", answers:["Príjem za menej práce","Príjem z investícií bez aktívnej práce – dividendy, nájom, úroky","Plat za nočné zmeny","Sociálne dávky"], correct:1, explanation:"Pasívny príjem: dividendy, nájom, úroky. Cieľ = vybudovať dostatok pasívneho príjmu na pokrytie výdavkov."},
      {q:"Ako vypočítaš mieru sporenia?", answers:["Úspory / výdavky","Úspory / príjem × 100 %","Príjem / výdavky","Výdavky / príjem × 100 %"], correct:1, explanation:"Miera sporenia = (úspory / príjem) × 100. Ak zarábaš 1 200 € a odložíš 240 €, miera sporenia = 20 %. FIRE cieľ je 50 %+."},
      {q:"Aký je rozdiel medzi finančnou slobodou a bohatstvom?", answers:["Sú to isté veci","Finančná sloboda = pasívny príjem ≥ výdavky. Bohatstvo = vysoká čistá hodnota majetku","Bohatstvo je dôležitejšie","Finančná sloboda vyžaduje milióny"], correct:1, explanation:"Niekto s 2 000 € pasívneho príjmu a 1 500 € výdavkov je finančne slobodný. Niekto s 5 mil. € majetku ale 20 000 € výdavkami nie."}
    ]},
    { id:"5-4", title:"Poistenie", icon:"🔒", questions:[
      {q:"Prečo je poistenie dôležité?", answers:["Nie je – len biznis poisťovní","Chráni pred katastrofickými stratami ktoré by zničili roky sporenia","Len kvôli zákonnej povinnosti","Len pre bohatých"], correct:1, explanation:"Poistenie je ochrana pred nízkopravdepodobnými ale vysokonákladnými udalosťami. Jeden úraz môže zničiť roky sporenia."},
      {q:"Čo je PZP?", answers:["Poistenie zdravia","Povinné zmluvné poistenie zodpovednosti za škodu spôsobenú motorovým vozidlom","Poistenie domácnosti","Životné poistenie"], correct:1, explanation:"PZP je povinné pre každé auto. Kryje škody spôsobené tvojím autom iným osobám. Bez PZP hrozí pokuta a nemôžeš legálne jazdiť."},
      {q:"Kedy potrebuješ životné poistenie?", answers:["Vždy a pre každého","Keď máš hypotéku alebo závislých od tvojho príjmu – deti, partner","Nikdy","Len po 50 rokoch"], correct:1, explanation:"Životné poistenie má zmysel ak: máš hypotéku, závisí od teba rodina. Slobodný 25-ročník bez záväzkov ho nepotrebuje."},
      {q:"Čo je spoluúčasť?", answers:["Mesačný poplatok","Suma ktorú platíš sám pri poistnej udalosti","Ročná prémia","Výška plnenia"], correct:1, explanation:"Vyššia spoluúčasť = nižšie poistné. Logika: drobné škody riešiš sám, poisťovňa kryje katastrofy."},
      {q:"Aká je zlaté pravidlo poistenia?", answers:["Poistiť všetko na maximum","Poistiť len riziká ktoré by ťa finančne zruinovali","Nekupovať žiadne poistenie","Kúpiť poistenie len raz"], correct:1, explanation:"Poistenie je na katastrofy nie maličkosti. Poistenie mobilu za 10 €/mesiac je zlá investícia. Poistenie pri trvalej invalidite s hypotékou je rozumné."},
      {q:"Čo je poistenie domácnosti vs poistenie nehnuteľnosti?", answers:["Sú to isté","Domácnosť kryje obsah (nábytok, elektronika), nehnuteľnosť kryje stavbu","Domácnosť je povinná","Nehnuteľnosť kryje obsah"], correct:1, explanation:"Oboje je odporúčané. Poistenie stavby kryje požiar, povodeň. Poistenie domácnosti kryje krádež, škody na obsahu."}
    ]},
    { id:"5-5", title:"Nehnuteľnosti", icon:"🏘️", questions:[
      {q:"Prečo sú nehnuteľnosti populárna investícia?", answers:["Lebo sú lacné","Hmatateľné aktívum, ochrana pred infláciou, pasívny príjem z nájmu","Lebo banky ich odporúčajú","Sú bez rizika"], correct:1, explanation:"Výhody: fyzický majetok, historický rast, príjem z nájmu, možnosť páky (hypotéka). Nevýhody: nízka likvidita, správa, vysoký vstupný kapitál."},
      {q:"Čo je hrubý výnos z prenájmu?", answers:["Príjem po všetkých výdavkoch","Ročný nájom / cena nehnuteľnosti × 100 %","Len nájom bez energií","Cena bytu za rok"], correct:1, explanation:"Byt 150 000 € s nájmom 700 €/mes = hrubý výnos (700×12)/150 000 = 5,6 %. Čistý výnos po daniach a výdavkoch bude 3–4 %."},
      {q:"Čo je páka (leverage) pri nehnuteľnostiach?", answers:["Zariadenie na sťahovanie","Investovanie cudzích peňazí (hypotéky) – zosilňuje zisky aj straty","Typ prenájmu","Daňová úspora"], correct:1, explanation:"Kúpiš byt za 100 000 €, vlastné 20 000 €, hypotéka 80 000 €. Byt zdraží o 10 % = zarobíš 10 000 € na 20 000 € = výnos 50 %!"},
      {q:"Čo je REIT?", answers:["Typ hypotéky","Real Estate Investment Trust – fond investujúci do nehnuteľností obchodovaný na burze","Daňový odpočet","Typ poistenia"], correct:1, explanation:"REIT ti umožňuje investovať do nehnuteľností aj za 100 €, bez hypotéky a správy. Diverzifikácia do stoviek nehnuteľností."},
      {q:"Čo je due diligence pri kúpe nehnuteľnosti?", answers:["Právna prehliadka","Dôkladná preverka – právny stav, technický stav, záložné práva, dlhy","Bankové schválenie","Notárske overenie"], correct:1, explanation:"Pred kúpou: over kataster (záložné práva, vecné bremená), nechaj urobiť technický posudok, over dlhy na nehnuteľnosti."},
      {q:"Oplatí sa kúpiť byt na prenájom dnes?", answers:["Vždy áno","Závisí od lokality a čísel – treba prerátať čistý výnos a porovnať s alternatívami","Vždy nie","Len v Bratislave"], correct:1, explanation:"V 2024 sú ceny vysoké a hypotéky drahé. Čistý výnos môže byť 2–3 %, ETF dáva 7–8 %. Treba prerátať konkrétne čísla."},
      {q:"Čo je neobsadenosť a ako ovplyvňuje výnos?", answers:["Byt bez nábytku","Čas keď nehnuteľnosť negeneruje nájom – realisticky 1-2 mesiace ročne","Počet izieb","Typ hypotéky"], correct:1, explanation:"Realita: počítaj s 1–2 mesiacmi bez nájomníka ročne. 700 € × 11 = 7 700 € namiesto 8 400 €. Toto znižuje reálny výnos."}
    ]}
  ]}
];
 
const REAL_LIFE = [
  { situation:"Dostal si prvú výplatu z brigády – 450 €. Kamaráti ťa volajú na výlet za 380 €.", amount:"450 €", question:"Čo spravíš?", answers:["Idem na výlet, miniem takmer všetko","Odložím 90 € (20 %), zvyšok na výlet","Celých 450 € odložím","Požičiam si na výlet"], correct:1, explanation:"Pravidlo 20 % – odlož aspoň pätinu každej výplaty. Zvyšok môžeš slobodne použiť."},
  { situation:"Tvoja práčka sa pokazila. Oprava 180 €, nová 350 €. Na sporiacom účte máš 600 €.", amount:"600 € úspory", question:"Čo spravíš?", answers:["Kúpim novú na splátky","Opravím starú za 180 € z nouzového fondu","Počkám kým sa situácia vyrieši","Požičiam si od kamaráta"], correct:1, explanation:"Presne na toto slúži nouzový fond! Oprava je lacnejšia a úspory zostanú."},
  { situation:"Zamestnávateľ ti ponúka zvýšenie platu o 200 € mesačne.", amount:"+200 € / mesiac", question:"Ako naložíš s príplatkom?", answers:["Celých 200 € miniem","100 € investujem, 100 € na lepší životný štandard","Celých 200 € odložím","Kúpim drahší telefón na splátky"], correct:1, explanation:"Pri každom zvýšení príjmu zvýš aj sporenie. Polovica na budúcnosť, polovica na kvalitu života teraz."},
  { situation:"Online reklama: 'Investuj 500 € a za mesiac máš 2 000 €! Zaručený výnos 300 %!'", amount:"Sľub: 300 % výnos", question:"Čo spravíš?", answers:["Investujem, znie to skvelo!","Investujem len 100 €","Ignorujem – zaručený vysoký výnos je vždy podvod","Pýtam sa kamarátov"], correct:2, explanation:"Ak to znie príliš dobre, je to podvod. Reálne investície vynášajú 5–10 % ročne."},
  { situation:"Kreditná karta, limit 1 500 €, dlh 800 €. Nemôžeš splatiť celý dlh, len minimum 25 €.", amount:"Dlh: 800 €, úrok 20 % ročne", question:"Čo spravíš?", answers:["Zaplatím len minimum 25 €","Zaplatím čo najviac môžem","Ignorujem to","Veziem si ďalší úver"], correct:1, explanation:"20 % ročný úrok je extrémne drahý! Vždy splať čo najviac."},
  { situation:"Kamarát ťa pozýva do MLM biznisu. Vstupný poplatok 300 €, provízie za nábor ľudí.", amount:"Vstupný poplatok: 300 €", question:"Čo spravíš?", answers:["Vstúpim","Požičiam si na vstup","Odmietnem – 99 % MLM účastníkov stráca peniaze","Vstúpim len ak vstúpi kamarát"], correct:2, explanation:"99 % účastníkov MLM prichádza o peniaze. Ak zisk závisí od náboru nie od produktu – je to pyramída."},
  { situation:"Prvá práca, zamestnávateľ ponúka III. pilier s príspevkom firmy 50 €/mesiac.", amount:"Firma prispeje 50 €/mesiac", question:"Čo spravíš?", answers:["Nezapíšem sa, dôchodok je ďaleko","Zapíšem sa, prispievam aj ja 20 €/mesiac","Počkám kým budem mať viac peňazí","Dôchodok rieši štát"], correct:1, explanation:"Nikdy neodmietaj zadarmo peniaze! 50 € + 20 € = 70 €/mes. Za 40 rokov pri 5 % = ~106 000 €!"},
  { situation:"Potraviny: balenie 500g za 2,40 € a balenie 1kg za 4,20 €.", amount:"500g = 2,40 € | 1kg = 4,20 €", question:"Čo je výhodnejšie?", answers:["500g – je lacnejšie","1kg – cena za gram je nižšia","Je to jedno","Kúpim oboje"], correct:1, explanation:"500g = 0,48 €/100g. 1kg = 0,42 €/100g. Väčšie balenie je lacnejšie o 12,5 %."},
  { situation:"Email: 'Tvoj bankový účet bol zablokovaný. Kliknite tu a zadajte údaje.'", amount:"Podozrivý email", question:"Čo spravíš?", answers:["Kliknem na link a zadám údaje","Zavolám priamo banke na overenom čísle","Odpoviem emailom","Posuniem kamarátovi"], correct:1, explanation:"Klasický phishing! Banky nikdy nežiadajú údaje emailom. Volaj na číslo z rubnej strany karty."},
  { situation:"Máš 1 000 € úspory. Kamarát ťa pozýva investovať do kryptomien.", amount:"1 000 € úspory", question:"Čo urobíš?", answers:["Investujem všetko","Investujem max 10 % (100 €), zvyšok do ETF","Nekupujem vôbec","Pôžičiam si viac a investujem 5 000 €"], correct:1, explanation:"Krypto je vysoko špekulatívne. Max 5–10 % portfólia ako špekulatívna časť. Zvyšok do diverzifikovaných ETF."}
];
 
const MAX_HEARTS = 5;
function loadState(){const s=localStorage.getItem('fg_state');if(s)return JSON.parse(s);return{xp:0,streak:0,hearts:MAX_HEARTS,lastActiveDate:null,lastRLDate:null,rlIndex:0,completedLessons:[],completedUnits:[]};}
function saveState(s){localStorage.setItem('fg_state',JSON.stringify(s));}
function updateStreak(state){
  const today=new Date().toDateString();
  const yesterday=new Date(Date.now()-86400000).toDateString();
  if(state.lastActiveDate===today)return state;
  state.streak=(state.lastActiveDate===yesterday)?state.streak+1:1;
  state.lastActiveDate=today;saveState(state);return state;
}
function isLessonDone(s,id){return s.completedLessons.includes(id);}
function isUnitUnlocked(s,uid){
  if(uid===1)return true;
  const prev=UNITS.find(u=>u.id===uid-1);
  return prev?prev.lessons.every(l=>isLessonDone(s,l.id)):false;
}
function isLessonUnlocked(s,uid,idx){
  if(!isUnitUnlocked(s,uid))return false;
  if(idx===0)return true;
  const unit=UNITS.find(u=>u.id===uid);
  return isLessonDone(s,unit.lessons[idx-1].id);
}
function completeLesson(s,lessonId,xpEarned){
  if(!s.completedLessons.includes(lessonId))s.completedLessons.push(lessonId);
  s.xp+=xpEarned;
  if(s.hearts<MAX_HEARTS)s.hearts++;
  UNITS.forEach(u=>{if(u.lessons.every(l=>s.completedLessons.includes(l.id))&&!s.completedUnits.includes(u.id))s.completedUnits.push(u.id);});
  s.lastActiveDate=new Date().toDateString();saveState(s);return s;
}
function getUnitProgress(s,unit){const done=unit.lessons.filter(l=>isLessonDone(s,l.id)).length;return{done,total:unit.lessons.length};}
 
function renderHearts(id){
  const el=document.getElementById(id);if(!el)return;
  el.innerHTML='';
  for(let i=0;i<MAX_HEARTS;i++){const h=document.createElement('span');h.className='heart'+(i<appState.hearts?'':' empty');h.textContent='❤️';el.appendChild(h);}
}
function loseHeart(){if(appState.hearts>0)appState.hearts--;saveState(appState);renderAllHearts();}
function renderAllHearts(){renderHearts('topbar-hearts');renderHearts('quiz-hearts');renderHearts('rl-hearts');}
 
function showNoHeartsModal(){
  const m=document.createElement('div');m.className='modal-overlay';m.id='hearts-modal';
  m.innerHTML='<div class="modal-box"><div class="modal-icon">💔</div><div class="modal-title">Nemáš srdcia!</div><div class="modal-hearts-display">💔💔💔💔💔</div><div class="modal-sub">Srdcia ti minuli. Môžeš si zarobiť nové v sekcii <strong>🌍 Real Life</strong> alebo počkaj do zajtrajška.</div><button class="modal-btn-primary" onclick="closeModal();goTo(\'reallife\')">🌍 Ísť na Real Life</button><button class="modal-btn-secondary" onclick="closeModal()">Zavrieť</button></div>';
  document.body.appendChild(m);
}
function closeModal(){const m=document.getElementById('hearts-modal');if(m)m.remove();}
 
let quizLesson=null,quizQ=0,quizCorrect=0,quizXP=0,quizAnswered=false;
const LETTERS=['A','B','C','D'];
 
function startLesson(uid,idx){
  const unit=UNITS.find(u=>u.id===uid);
  if(!isLessonUnlocked(appState,uid,idx))return;
  if(appState.hearts<=0){showNoHeartsModal();return;}
  quizLesson=unit.lessons[idx];quizQ=0;quizCorrect=0;quizXP=0;quizAnswered=false;
  goTo('quiz');renderQuestion();
}
function renderQuestion(){
  const q=quizLesson.questions[quizQ];const total=quizLesson.questions.length;
  document.getElementById('qprog').style.width=Math.round((quizQ/total)*100)+'%';
  document.getElementById('q-num').textContent=(quizQ+1)+'/'+total;
  document.getElementById('q-text').textContent=q.q;
  const fb=document.getElementById('q-feedback');fb.style.display='none';fb.className='feedback';
  document.getElementById('q-next').style.display='none';quizAnswered=false;
  const div=document.getElementById('q-answers');div.innerHTML='';
  q.answers.forEach((a,i)=>{
    const btn=document.createElement('button');btn.className='ans-btn';
    btn.innerHTML='<span class="ans-letter">'+LETTERS[i]+'</span><span>'+a+'</span>';
    btn.onclick=()=>selectAnswer(i);div.appendChild(btn);
  });
  renderHearts('quiz-hearts');
}
function selectAnswer(idx){
  if(quizAnswered)return;quizAnswered=true;
  const q=quizLesson.questions[quizQ];
  const btns=document.querySelectorAll('.ans-btn');btns.forEach(b=>b.disabled=true);
  const ok=idx===q.correct;
  btns[idx].classList.add(ok?'correct':'wrong');
  if(!ok){btns[q.correct].classList.add('correct');loseHeart();}
  if(ok){quizCorrect++;quizXP+=10;}
  const fb=document.getElementById('q-feedback');fb.style.display='block';
  fb.className='feedback '+(ok?'fb-ok':'fb-bad');
  fb.innerHTML=(ok?'✅ <strong>Správne!</strong> ':'❌ <strong>Nesprávne.</strong> ')+q.explanation;
  document.getElementById('q-next').style.display='block';
  if(!ok&&appState.hearts<=0){
    setTimeout(()=>{showNoHeartsModal();},800);
  }
}
function nextQ(){quizQ++;if(quizQ>=quizLesson.questions.length)finishLesson();else renderQuestion();}
function replayLesson(){quizQ=0;quizCorrect=0;quizXP=0;quizAnswered=false;goTo('quiz');renderQuestion();}
function finishLesson(){
  appState=completeLesson(appState,quizLesson.id,quizXP);
  appState=updateStreak(appState);updateTopbar();
  const acc=Math.round((quizCorrect/quizLesson.questions.length)*100);
  document.getElementById('d-xp').textContent='+'+quizXP;
  document.getElementById('d-acc').textContent=acc+'%';
  document.getElementById('d-streak').textContent='🔥 '+appState.streak;
  goTo('done');
}
 
function renderRealLife(){
  const container=document.getElementById('rl-content');
  const today=new Date().toDateString();
  if(appState.lastRLDate===today){
    container.innerHTML='<div class="rl-done-today"><div class="rl-done-icon">✅</div><div class="rl-done-title">Dnes si to zvládol!</div><div class="rl-done-sub">Vráť sa zajtra pre novú situáciu</div><div class="rl-streak-info">🔥 Tvoja séria: <strong>'+appState.streak+' dní</strong></div></div>';
    return;
  }
  const idx=(appState.rlIndex||0)%REAL_LIFE.length;const rl=REAL_LIFE[idx];let answered=false;
  container.innerHTML='<div class="rl-badge">🌍 Real Life výzva · +1 ❤️ za správnu odpoveď</div><h1 class="page-title">Čo by si spravil?</h1><p class="page-sub">Skutočné životné situácie – správna odpoveď zarába srdce</p><div class="rl-situation"><div class="rl-situation-label">📍 Situácia</div><div class="rl-situation-text">'+rl.situation+'</div><div class="rl-situation-amount">'+rl.amount+'</div></div><p style="font-size:16px;font-weight:800;color:#1c1c1c;margin-bottom:16px;">'+rl.question+'</p><div id="rl-answers"></div><div id="rl-feedback" style="display:none;"></div><button class="next-btn" id="rl-next" style="display:none;" onclick="goTo(\'learn\')">Späť na lekcie</button>';
  renderHearts('rl-hearts');
  const answersDiv=document.getElementById('rl-answers');
  rl.answers.forEach((a,i)=>{
    const btn=document.createElement('button');btn.className='ans-btn';
    btn.innerHTML='<span class="ans-letter">'+LETTERS[i]+'</span><span>'+a+'</span>';
    btn.onclick=()=>{
      if(answered)return;answered=true;
      document.querySelectorAll('#rl-answers .ans-btn').forEach(b=>b.disabled=true);
      const ok=i===rl.correct;btn.classList.add(ok?'correct':'wrong');
      if(!ok)document.querySelectorAll('#rl-answers .ans-btn')[rl.correct].classList.add('correct');
      const fb=document.getElementById('rl-feedback');fb.style.display='block';
      fb.className='rl-reward '+(ok?'rl-reward-ok':'rl-reward-bad');
      fb.innerHTML=(ok?'✅ <strong>Správne! +1 ❤️</strong><br>':'❌ <strong>Nesprávne.</strong><br>')+rl.explanation;
      if(ok&&appState.hearts<MAX_HEARTS)appState.hearts++;
      appState.lastRLDate=new Date().toDateString();
      appState.rlIndex=(appState.rlIndex||0)+1;
      appState=updateStreak(appState);saveState(appState);updateTopbar();renderAllHearts();
      document.getElementById('rl-next').style.display='block';
    };
    answersDiv.appendChild(btn);
  });
}
 
function goTo(screen){
  document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
  document.getElementById('screen-'+screen).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  const el=document.getElementById('nav-'+screen);if(el)el.classList.add('active');
  if(screen==='learn')renderLearnPath();
  if(screen==='reallife')renderRealLife();
}
function updateTopbar(){
  document.querySelectorAll('.js-streak').forEach(el=>el.textContent=appState.streak);
  document.querySelectorAll('.js-xp').forEach(el=>el.textContent=appState.xp);
  renderAllHearts();
}
 
const DECOS=['💰','💵','🪙','💳','📈','🏦','💎','🤑','💴','📊'];
function renderLearnPath(){
  const container=document.getElementById('learn-path');container.innerHTML='';
  UNITS.forEach((unit,ui)=>{
    const unlocked=isUnitUnlocked(appState,unit.id);
    const progress=getUnitProgress(appState,unit);
    // Unit header - just title, no "Jednotka X"
    const header=document.createElement('div');
    header.className='unit-header '+unit.color+(!unlocked?' locked-unit':'');
    header.innerHTML='<div><h2>'+unit.title+'</h2><p>'+unit.desc+'</p></div><span class="unit-badge">'+progress.done+'/'+progress.total+'</span>';
    container.appendChild(header);
    const pathDiv=document.createElement('div');
    pathDiv.className='path'+(!unlocked?' path-locked':'');
    // Zigzag positions: center, right, center, left, center, right...
    const positions=['offset-center','offset-right','offset-center','offset-left','offset-center','offset-right','offset-left'];
    unit.lessons.forEach((lesson,idx)=>{
      const done=isLessonDone(appState,lesson.id);
      const lesUnlocked=isLessonUnlocked(appState,unit.id,idx);
      const isCurrent=lesUnlocked&&!done;
      // Connector with curve
      if(idx>0){
        const conn=document.createElement('div');
        const prevDone=isLessonDone(appState,unit.lessons[idx-1].id);
        const prevPos=positions[(idx-1)%positions.length];
        const curPos=positions[idx%positions.length];
        conn.style.cssText='width:100%;height:32px;display:flex;align-items:center;justify-content:center;';
        // Show curved arrow based on direction
        let arrow='⬇️';
        if(prevPos==='offset-left'&&curPos==='offset-right')arrow='↘️';
        else if(prevPos==='offset-right'&&curPos==='offset-left')arrow='↙️';
        else if(prevPos==='offset-center'&&curPos==='offset-right')arrow='↘️';
        else if(prevPos==='offset-center'&&curPos==='offset-left')arrow='↙️';
        else if(prevPos==='offset-right'&&curPos==='offset-center')arrow='↙️';
        else if(prevPos==='offset-left'&&curPos==='offset-center')arrow='↘️';
        conn.innerHTML='<span style="font-size:20px;opacity:'+(prevDone?'0.6':'0.25')+';">'+arrow+'</span>';
        pathDiv.appendChild(conn);
      }
      const rowDiv=document.createElement('div');
      rowDiv.className='path-row '+(positions[idx%positions.length]);
      const nodeWrap=document.createElement('div');nodeWrap.className='node-wrap';
      if(lesUnlocked)nodeWrap.onclick=()=>startLesson(unit.id,idx);
      const node=document.createElement('div');
      node.className='node '+(done?'done':isCurrent?'current':'locked');
      // Node content
      if(done){
        node.innerHTML='<span style="font-size:28px;color:#fff;">✓</span>';
      } else if(isCurrent){
        node.innerHTML='<span style="font-size:28px;">'+lesson.icon+'</span>';
        // Pulsing glow for current
        node.style.animation='pulse 2s ease-in-out infinite';
      } else {
        node.innerHTML='<span style="font-size:24px;opacity:0.5;">🔒</span>';
      }
      const label=document.createElement('span');
      label.className='node-label'+(isCurrent?' active-lbl':done?' done-lbl':'');
      label.textContent=lesson.title;
      nodeWrap.appendChild(node);nodeWrap.appendChild(label);rowDiv.appendChild(nodeWrap);
      pathDiv.appendChild(rowDiv);
    });
    container.appendChild(pathDiv);
    const gap=document.createElement('div');gap.style.height='8px';container.appendChild(gap);
  });
}
 
function renderProfile(){
  const user=JSON.parse(localStorage.getItem('fg_user')||'{"name":"Hosť"}');
  const initials=user.name.split(' ').map(p=>p[0]).join('').toUpperCase().slice(0,2);
  document.getElementById('prof-avatar').textContent=initials;
  document.getElementById('prof-name').textContent=user.name;
  document.getElementById('stat-xp').textContent=appState.xp;
  document.getElementById('stat-streak').textContent=appState.streak;
  document.getElementById('stat-lessons').textContent=appState.completedLessons.length;
  document.getElementById('stat-hearts').textContent=appState.hearts+'/'+MAX_HEARTS;
  document.getElementById('prof-streak-num').textContent=appState.streak;
  const msgs=['Začni dnes svoju sériu!','Skvelý štart!','Tak držať!','Úžasné!','Neprekonateľný!','Legenda! 🔥'];
  document.getElementById('prof-streak-msg').textContent=appState.streak===0?msgs[0]:appState.streak<3?msgs[1]:appState.streak<7?msgs[2]:appState.streak<14?msgs[3]:appState.streak<30?msgs[4]:msgs[5];
  const calDiv=document.getElementById('streak-cal');calDiv.innerHTML='';
  const days=['Po','Ut','St','Šv','Pi','So','Ne'];
  const today=new Date();
  for(let i=6;i>=0;i--){
    const d=new Date(today);d.setDate(today.getDate()-i);
    const hit=i<appState.streak;
    const dd=document.createElement('div');dd.className='sday';
    dd.innerHTML='<div class="sday-circle '+(hit?'hit':'miss')+'">'+(hit?'✓':'')+'</div><div class="sday-label">'+days[d.getDay()===0?6:d.getDay()-1]+'</div>';
    calDiv.appendChild(dd);
  }
  const totalLessons=UNITS.reduce((s,u)=>s+u.lessons.length,0);
  const badges=[
    {icon:'🌱',label:'Začiatočník',ok:appState.completedLessons.length>=1},
    {icon:'🔥',label:'5 dní v sérii',ok:appState.streak>=5},
    {icon:'🎯',label:'5 lekcií',ok:appState.completedLessons.length>=5},
    {icon:'🏆',label:'Top žiak',ok:appState.xp>=500},
    {icon:'🌍',label:'Real Life hrdina',ok:(appState.rlIndex||0)>=3},
    {icon:'📈',label:'Investor',ok:appState.completedUnits.includes(2)},
    {icon:'🧾',label:'Daňový expert',ok:appState.completedUnits.includes(4)},
    {icon:'💎',label:'Diamant',ok:appState.completedLessons.length>=totalLessons},
  ];
  const row=document.getElementById('badge-row');row.innerHTML='';
  badges.forEach(b=>{const div=document.createElement('div');div.className='badge'+(b.ok?'':' locked');div.innerHTML='<div class="bi">'+b.icon+'</div><div class="bl">'+b.label+'</div>';row.appendChild(div);});
}
 
let appState=loadState();
appState=updateStreak(appState);
const user=JSON.parse(localStorage.getItem('fg_user')||'{"name":"Host","email":"guest"}');
const initials=user.name.split(' ').map(p=>p[0]).join('').toUpperCase().slice(0,2);
document.getElementById('sb-name').textContent=user.name;
document.getElementById('sb-avatar').textContent=initials;
updateTopbar();renderLearnPath();
 
// Pulse animation
const style=document.createElement('style');
style.textContent='@keyframes pulse{0%,100%{box-shadow:0 6px 24px rgba(88,204,2,0.4)}50%{box-shadow:0 6px 32px rgba(88,204,2,0.7)}}';
document.head.appendChild(style);
 
function logout(){localStorage.removeItem('fg_user');window.location.href='index.html';}
</script>
</body>
</html>
"""
 
# Build the HTML header part (everything before const UNITS)
html_header = """<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FinGram – Učiť sa</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="app">
  <aside class="sidebar">
    <div class="logo">💸 FinGram</div>
    <div class="nav-item active" id="nav-learn" onclick="goTo('learn')"><span class="nav-icon">📚</span> Učiť sa</div>
    <div class="nav-item" id="nav-reallife" onclick="goTo('reallife')"><span class="nav-icon">🌍</span> Real Life</div>
    <div class="nav-item" id="nav-profile" onclick="goTo('profile');renderProfile();"><span class="nav-icon">👤</span> Profil</div>
    <div class="nav-sep"></div>
    <div class="sidebar-bottom">
      <div class="user-chip" onclick="logout()">
        <div class="user-avatar" id="sb-avatar">?</div>
        <div><div class="user-name" id="sb-name">Načítavam...</div><div class="user-level">Odhlásiť sa</div></div>
      </div>
    </div>
  </aside>
  <div class="main">
    <div id="screen-learn" class="screen active">
      <div class="topbar">
        <div class="pill pill-fire">🔥 <span class="js-streak">0</span> dní</div>
        <div class="pill pill-xp">⚡ <span class="js-xp">0</span> XP</div>
        <div class="hearts" id="topbar-hearts"></div>
      </div>
      <h1 class="page-title">Tvoja cesta</h1>
      <p class="page-sub">Ovládni svoje peniaze krok za krokom</p>
      <div id="learn-path"></div>
    </div>
    <div id="screen-quiz" class="screen">
      <div class="quiz-wrap">
        <div class="quiz-topbar">
          <button class="close-btn" onclick="goTo('learn')">✕</button>
          <div class="prog-outer" style="flex:1;"><div class="prog-inner" id="qprog" style="width:0%;"></div></div>
          <span style="font-size:13px;color:#aaa;font-weight:700;" id="q-num">1/7</span>
          <div class="hearts" id="quiz-hearts"></div>
        </div>
        <p class="q-text" id="q-text"></p>
        <div id="q-answers"></div>
        <div id="q-feedback" class="feedback" style="display:none;"></div>
        <button class="next-btn" id="q-next" style="display:none;" onclick="nextQ()">Pokračovať</button>
      </div>
    </div>
    <div id="screen-done" class="screen">
      <div class="done-wrap">
        <div class="done-emoji">🎉</div>
        <h1 class="done-title">Lekcia splnená!</h1>
        <p class="done-sub">Výborná práca! +1 ❤️ za dokončenie</p>
        <div class="stat-row">
          <div class="stat-box"><div class="stat-num" id="d-xp">+0</div><div class="stat-lbl">XP získané</div></div>
          <div class="stat-box"><div class="stat-num" id="d-acc">100%</div><div class="stat-lbl">presnosť</div></div>
          <div class="stat-box"><div class="stat-num" id="d-streak">🔥 1</div><div class="stat-lbl">séria dní</div></div>
        </div>
        <button class="btn-green" onclick="goTo('learn')">Späť na mapu</button>
        <button class="btn-outline" onclick="replayLesson()">Zopakovať lekciu</button>
      </div>
    </div>
    <div id="screen-reallife" class="screen">
      <div class="rl-wrap">
        <div class="topbar">
          <div class="pill pill-fire">🔥 <span class="js-streak">0</span> dní</div>
          <div class="pill pill-xp">⚡ <span class="js-xp">0</span> XP</div>
          <div class="hearts" id="rl-hearts"></div>
        </div>
        <div id="rl-content"></div>
      </div>
    </div>
    <div id="screen-profile" class="screen">
      <div class="topbar">
        <div class="pill pill-fire">🔥 <span class="js-streak">0</span> dní</div>
        <div class="pill pill-xp">⚡ <span class="js-xp">0</span> XP</div>
      </div>
      <div style="display:flex;align-items:center;gap:20px;margin-bottom:28px;">
        <div class="avatar" id="prof-avatar">?</div>
        <div>
          <h1 class="page-title" style="margin-bottom:4px;" id="prof-name">Načítavam...</h1>
          <p style="color:#aaa;font-size:14px;font-weight:600;">Základná úroveň</p>
        </div>
      </div>
      <div class="streak-big">
        <div class="streak-big-num">🔥 <span id="prof-streak-num">0</span></div>
        <div class="streak-big-label">dní v sérii</div>
        <div class="streak-big-msg" id="prof-streak-msg">Začni dnes svoju sériu!</div>
      </div>
      <div class="profile-grid">
        <div class="pcard"><h3>Séria posledných 7 dní</h3><div class="streak-cal" id="streak-cal"></div></div>
        <div class="pcard"><h3>Štatistiky</h3>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
            <div><div style="font-size:24px;font-weight:800;" id="stat-xp">0</div><div style="font-size:12px;color:#aaa;margin-top:2px;">celkové XP</div></div>
            <div><div style="font-size:24px;font-weight:800;" id="stat-lessons">0</div><div style="font-size:12px;color:#aaa;margin-top:2px;">lekcie</div></div>
            <div><div style="font-size:24px;font-weight:800;" id="stat-streak">0</div><div style="font-size:12px;color:#aaa;margin-top:2px;">dní streak</div></div>
            <div><div style="font-size:24px;font-weight:800;" id="stat-hearts">0</div><div style="font-size:12px;color:#aaa;margin-top:2px;">❤️ srdcia</div></div>
          </div>
        </div>
      </div>
      <div class="pcard"><h3>Odznaky</h3><div class="badge-row" id="badge-row"></div></div>
    </div>
  </div>
</div>
<script>
"""
 
# Get the partial UNITS data (lines 1-208 of the raw extract)
# But we need to find where it cuts off and complete it
# The existing file has units 1-5 lesson 1 only, rest is cut
# We need to close out the existing partial data properly
 
# Find the last complete lesson in existing data
# Last complete lesson found was 5-1 (partial)
# We need to close 5-1 and add 5-2 through 5-5
 
# Get everything up to and including the last complete questions array
# Find index of the last complete unit bracket pattern
existing_units = existing[units_start:]
 
# Find where unit 5 lesson 1 questions array ends - look for the last complete question
# The file cuts off mid-question, so we need to find the last complete q:{...} block
import re
# Find all complete question objects
complete_q_end = 0
for m in re.finditer(r'explanation:"[^"]+"\}', existing_units):
    complete_q_end = m.end()
 
print(f"Last complete question ends at position {complete_q_end} in units data")
print("Preview:", existing_units[complete_q_end-30:complete_q_end+50])
 
PYEOF