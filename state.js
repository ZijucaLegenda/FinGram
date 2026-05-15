// ── STAV APLIKÁCIE ────────────────────────────────────────────────────────────
// Načíta uložený stav alebo vytvorí nový
 
function loadState() {
  const saved = localStorage.getItem('fg_state');
  if (saved) return JSON.parse(saved);
  return {
    xp: 0,
    streak: 0,
    lastActiveDate: null,
    completedLessons: [],   // ["1-1", "1-2", ...]
    completedUnits: []      // [1, 2, ...]
  };
}
 
function saveState(state) {
  localStorage.setItem('fg_state', JSON.stringify(state));
}
 
// Streak logika – zavolaj raz pri načítaní apky
function updateStreak(state) {
  const today = new Date().toDateString();
  const yesterday = new Date(Date.now() - 86400000).toDateString();
 
  if (state.lastActiveDate === today) {
    // Dnes už aktívny – nič nerob
    return state;
  } else if (state.lastActiveDate === yesterday) {
    // Včera bol aktívny – zvýš streak
    state.streak += 1;
    state.lastActiveDate = today;
  } else if (state.lastActiveDate === null) {
    // Prvýkrát
    state.streak = 1;
    state.lastActiveDate = today;
  } else {
    // Prerušenie série
    state.streak = 1;
    state.lastActiveDate = today;
  }
 
  saveState(state);
  return state;
}
 
// Pomocné funkcie
function isLessonDone(state, lessonId) {
  return state.completedLessons.includes(lessonId);
}
 
function isUnitUnlocked(state, unitId) {
  if (unitId === 1) return true; // Prvá jednotka vždy odomknutá
  const prevUnit = UNITS.find(u => u.id === unitId - 1);
  if (!prevUnit) return false;
  return prevUnit.lessons.every(l => isLessonDone(state, l.id));
}
 
function isLessonUnlocked(state, unitId, lessonIndex) {
  if (!isUnitUnlocked(state, unitId)) return false;
  if (lessonIndex === 0) return true; // Prvá lekcia v jednotke vždy odomknutá
  const unit = UNITS.find(u => u.id === unitId);
  const prevLesson = unit.lessons[lessonIndex - 1];
  return isLessonDone(state, prevLesson.id);
}
 
function completeLesson(state, lessonId, xpEarned) {
  if (!state.completedLessons.includes(lessonId)) {
    state.completedLessons.push(lessonId);
  }
  state.xp += xpEarned;
 
  // Skontroluj či je celá jednotka dokončená
  UNITS.forEach(unit => {
    const allDone = unit.lessons.every(l => state.completedLessons.includes(l.id));
    if (allDone && !state.completedUnits.includes(unit.id)) {
      state.completedUnits.push(unit.id);
    }
  });
 
  const today = new Date().toDateString();
  state.lastActiveDate = today;
  saveState(state);
  return state;
}
 
function getUnitProgress(state, unit) {
  const done = unit.lessons.filter(l => isLessonDone(state, l.id)).length;
  return { done, total: unit.lessons.length, pct: Math.round((done / unit.lessons.length) * 100) };
}