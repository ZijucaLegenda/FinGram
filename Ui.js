// ── NAVIGÁCIA ─────────────────────────────────────────────────────────────────
function goTo(screen) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + screen).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const navEl = document.getElementById('nav-' + screen);
  if (navEl) navEl.classList.add('active');
 
  // Pri otvorení learn – prerendruj cestu
  if (screen === 'learn') renderLearnPath();
}
 
// ── TOPBAR ────────────────────────────────────────────────────────────────────
function updateTopbar() {
  document.querySelectorAll('.js-streak').forEach(el => el.textContent = appState.streak);
  document.querySelectorAll('.js-xp').forEach(el => el.textContent = appState.xp);
}
 
// ── LEARN PATH ────────────────────────────────────────────────────────────────
function renderLearnPath() {
  const container = document.getElementById('learn-path');
  container.innerHTML = '';
 
  UNITS.forEach(unit => {
    const unlocked = isUnitUnlocked(appState, unit.id);
    const progress = getUnitProgress(appState, unit);
 
    // Unit header
    const header = document.createElement('div');
    header.className = `unit-header ${unit.color} ${!unlocked ? 'locked-unit' : ''}`;
    header.innerHTML = `
      <div>
        <h2>Jednotka ${unit.id} – ${unit.title}</h2>
        <p>${unit.desc}</p>
      </div>
      <span class="unit-badge">${progress.done} / ${progress.total} lekcií</span>
    `;
    container.appendChild(header);
 
    // Lessons path
    const pathDiv = document.createElement('div');
    pathDiv.className = 'path' + (!unlocked ? ' path-locked' : '');
 
    unit.lessons.forEach((lesson, idx) => {
      const done      = isLessonDone(appState, lesson.id);
      const lesUnlocked = isLessonUnlocked(appState, unit.id, idx);
      const isCurrent = lesUnlocked && !done;
 
      // Connector above (except first)
      if (idx > 0) {
        const conn = document.createElement('div');
        const prevDone = isLessonDone(appState, unit.lessons[idx - 1].id);
        conn.className = 'connector' + (prevDone ? ' done' : '');
        pathDiv.appendChild(conn);
      }
 
      // Offset alternating nodes left/right
      const rowDiv = document.createElement('div');
      rowDiv.className = 'path-row';
 
      if (idx % 2 === 1) {
        // Add spacer on left for offset effect
        const spacer = document.createElement('div');
        spacer.style.width = '56px';
        rowDiv.appendChild(spacer);
      }
 
      const nodeWrap = document.createElement('div');
      nodeWrap.className = 'node-wrap';
      if (lesUnlocked) nodeWrap.onclick = () => startLesson(unit.id, idx);
 
      const node = document.createElement('div');
      node.className = 'node ' + (done ? 'done' : isCurrent ? 'current' : 'locked');
      node.textContent = done ? '✓' : isCurrent ? lesson.icon : '🔒';
 
      const label = document.createElement('span');
      label.className = 'node-label' + (isCurrent ? ' active-lbl' : '');
      label.textContent = lesson.title;
 
      nodeWrap.appendChild(node);
      nodeWrap.appendChild(label);
      rowDiv.appendChild(nodeWrap);
 
      if (idx % 2 === 1) {
        const spacer2 = document.createElement('div');
        spacer2.style.width = '56px';
        rowDiv.appendChild(spacer2);
      }
 
      pathDiv.appendChild(rowDiv);
    });
 
    container.appendChild(pathDiv);
 
    // Gap between units
    const gap = document.createElement('div');
    gap.style.height = '24px';
    container.appendChild(gap);
  });
}
 
// ── PROFIL ────────────────────────────────────────────────────────────────────
function renderProfile() {
  const user = JSON.parse(localStorage.getItem('fg_user') || '{"name":"Hosť"}');
  const initials = user.name.split(' ').map(p => p[0]).join('').toUpperCase().slice(0, 2);
 
  document.getElementById('prof-avatar').textContent = initials;
  document.getElementById('prof-name').textContent   = user.name;
  document.getElementById('stat-xp').textContent     = appState.xp;
  document.getElementById('stat-streak').textContent = appState.streak;
 
  const totalLessons = UNITS.reduce((sum, u) => sum + u.lessons.length, 0);
  const doneLessons  = appState.completedLessons.length;
  document.getElementById('stat-lessons').textContent = doneLessons;
 
  // Streak kalendár – posledných 7 dní
  const calDiv = document.getElementById('streak-cal');
  calDiv.innerHTML = '';
  const days = ['Po','Ut','St','Šv','Pi','So','Ne'];
  const today = new Date();
  for (let i = 6; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(today.getDate() - i);
    const hit = i < appState.streak;
    const dayDiv = document.createElement('div');
    dayDiv.className = 'sday';
    dayDiv.innerHTML = `
      <div class="sday-circle ${hit ? 'hit' : 'miss'}">${hit ? '✓' : ''}</div>
      <div class="sday-label">${days[d.getDay() === 0 ? 6 : d.getDay() - 1]}</div>
    `;
    calDiv.appendChild(dayDiv);
  }
 
  // Odznaky
  const badges = [
    { icon: '🌱', label: 'Začiatočník',   unlocked: doneLessons >= 1 },
    { icon: '🔥', label: '5 dní v sérii', unlocked: appState.streak >= 5 },
    { icon: '💡', label: 'Prvá lekcia',   unlocked: doneLessons >= 1 },
    { icon: '🎯', label: 'Presný strelec',unlocked: doneLessons >= 3 },
    { icon: '🏆', label: 'Top žiak',      unlocked: appState.xp >= 200 },
    { icon: '📈', label: 'Investor',      unlocked: appState.completedUnits.includes(2) },
    { icon: '💎', label: 'Diamant',       unlocked: appState.xp >= 500 },
  ];
 
  const badgeRow = document.getElementById('badge-row');
  badgeRow.innerHTML = '';
  badges.forEach(b => {
    const div = document.createElement('div');
    div.className = 'badge' + (b.unlocked ? '' : ' locked');
    div.innerHTML = `<div class="bi">${b.icon}</div><div class="bl">${b.label}</div>`;
    badgeRow.appendChild(div);
  });
}