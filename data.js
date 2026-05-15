// ── VŠETKY LEKCIE ─────────────────────────────────────────────────────────────
const UNITS = [
  {
    id: 1,
    title: "Základy sporenia",
    desc: "Nauč sa, ako a prečo sporiť každý deň",
    color: "green",
    lessons: [
      {
        id: "1-1", title: "Čo je sporenie?", icon: "💰",
        questions: [
          { q: "Čo znamená pojem 'nouzový fond'?", answers: ["Peniaze na luxusné nákupy","Rezerva na neočakávané výdavky","Investícia do akcií","Výplata vopred"], correct: 1, explanation: "Nouzový fond je rezerva 3–6 mesačných výdavkov pre prípad výpadku príjmu, opravy auta alebo chorôb." },
          { q: "Aké je odporúčané pravidlo pre mesačné sporenie?", answers: ["Sporiť 2 % príjmu","Sporiť len keď zostanú peniaze","Sporiť 10–20 % príjmu","Nesporiť, investovať všetko"], correct: 2, explanation: "Odborníci odporúčajú 10–20 % mesačného príjmu. Kľúčová je pravidelnosť." },
          { q: "Čo je výhodnejšie – bežný alebo sporiaci účet?", answers: ["Bežný účet","Sporiaci účet – ponúka vyšší úrok","Je to jedno","Hotovosť doma"], correct: 1, explanation: "Sporiaci účet zhodnotí peniaze o úrok. Na bežnom účte nič nezarobiš." },
          { q: "Prečo je dobré mať konkrétne finančné ciele?", answers: ["Nie sú potrebné","Motivujú a určia sumu sporenia","Sú len pre bohatých","Zvyšujú dane"], correct: 1, explanation: "Konkrétny cieľ (napr. 1 000 € za 10 mesiacov) ťa motivuje – ľahko si vypočítaš 100 € mesačne." }
        ]
      },
      {
        id: "1-2", title: "Nouzový fond", icon: "🛡️",
        questions: [
          { q: "Koľko mesačných výdavkov by mal mať nouzový fond?", answers: ["1 mesiac","2 mesiace","3–6 mesiacov","12 mesiacov"], correct: 2, explanation: "Odporúča sa 3–6 mesačných výdavkov. Dá ti čas nájsť nové zamestnanie alebo pokryť nečakané výdavky." },
          { q: "Kde by si mal mať uložený nouzový fond?", answers: ["V hotovosti doma","Na sporiacom účte – dostupný kedykoľvek","V akciách","V kryptomenách"], correct: 1, explanation: "Nouzový fond musí byť rýchlo dostupný. Sporiaci účet je ideálny – bezpečný a zarába malý úrok." },
          { q: "Čo by si mal použiť z nouzového fondu?", answers: ["Dovolenku","Nový telefón","Opravu auta po nehode","Vianočné darčeky"], correct: 2, explanation: "Nouzový fond je pre skutočné núdzové situácie – výpadok príjmu, oprava, zdravie. Nie pre plánované výdavky." },
          { q: "Máš mesačné výdavky 800 €. Aký by mal byť tvoj minimálny nouzový fond?", answers: ["800 €","1 600 €","2 400 €","8 000 €"], correct: 2, explanation: "Minimálne 3 mesiace × 800 € = 2 400 €. Ideálne 6 mesiacov = 4 800 €." }
        ]
      },
      {
        id: "1-3", title: "Úrok a inflácia", icon: "📈",
        questions: [
          { q: "Čo je inflácia?", answers: ["Rast cien tovarov a služieb","Pokles hodnoty akcií","Zvyšovanie miezd","Znižovanie daní"], correct: 0, explanation: "Inflácia = rast cien. Za rovnaké peniaze kúpiš menej. Ak sporenie zarába menej ako inflácia, úspory strácajú hodnotu." },
          { q: "Čo je zložený úrok?", answers: ["Úrok platený štátom","Úrok z úroku – zarábate aj zo svojich úrokov","Pokuta za neskoré platenie","Poplatok za účet"], correct: 1, explanation: "Zložený úrok rastie exponenciálne! 1 000 € → 1 050 € → ďalší rok 5 % z 1 050 €, nie z 1 000 €." },
          { q: "Máš 500 € s ročným úrokom 3 %. Koľko budeš mať po 1 roku?", answers: ["500 €","503 €","515 €","550 €"], correct: 2, explanation: "500 × 0,03 = 15 €. Po roku = 515 €. Pri väčších sumách a dlhšom čase je efekt obrovský." },
          { q: "Reálny výnos sporenia je kladný, keď...", answers: ["Úrok je vyšší ako inflácia","Máš viac ako 10 účtov","Sporenie trvá menej ako rok","Úrok je nulový"], correct: 0, explanation: "Reálny výnos = úrok − inflácia. Úrok 4 % − inflácia 2 % = reálny zisk 2 %." }
        ]
      },
      {
        id: "1-4", title: "Finančné ciele", icon: "🎯",
        questions: [
          { q: "Čo je SMART cieľ?", answers: ["Cieľ ktorý je ťažký","Konkrétny, merateľný, dosiahnuteľný, relevantný a časovo ohraničený","Cieľ bez termínu","Cieľ pre iných ľudí"], correct: 1, explanation: "SMART = Specific, Measurable, Achievable, Relevant, Time-bound. Napr. 'Ušetrím 1 000 € do 10 mesiacov'." },
          { q: "Chceš auto za 5 000 € o 2 roky. Koľko musíš sporiť mesačne?", answers: ["100 €","150 €","208 €","500 €"], correct: 2, explanation: "5 000 € ÷ 24 mesiacov = ~208 € mesačne. Takto si rozložíš veľký cieľ na malé kroky." },
          { q: "Aký je rozdiel medzi krátkodobým a dlhodobým cieľom?", answers: ["Žiadny","Krátkodobý do 1 roka, dlhodobý nad 5 rokov","Krátkodobý je drahší","Dlhodobý je jednoduchší"], correct: 1, explanation: "Krátkodobé (dovolenka, telefón) sú do 1 roka. Dlhodobé (dôchodok, dom) sú na 5+ rokov." },
          { q: "Prečo je dôležité zapisovať si finančné ciele?", answers: ["Nie je to dôležité","Zvyšuje pravdepodobnosť ich dosiahnutia","Aby si ich ukázal ostatným","Kvôli daniam"], correct: 1, explanation: "Štúdie ukazujú, že písomné ciele sa plnia až 42 % častejšie." }
        ]
      }
    ]
  },
  {
    id: 2,
    title: "Investovanie",
    desc: "ETF fondy, akcie a pasívny príjem",
    color: "blue",
    lessons: [
      {
        id: "2-1", title: "Čo je investovanie?", icon: "📊",
        questions: [
          { q: "Aký je hlavný rozdiel medzi sporením a investovaním?", answers: ["Žiadny rozdiel","Sporenie je bezpečnejšie, investovanie má vyšší potenciálny výnos aj riziko","Investovanie je vždy lepšie","Sporenie je len pre starých"], correct: 1, explanation: "Sporenie = bezpečné, nízky výnos. Investovanie = vyššie riziko, ale aj vyšší potenciálny výnos dlhodobo." },
          { q: "Čo je akcia?", answers: ["Pôžička firme","Podiel vo vlastníctve firmy","Vládny dlhopis","Bankový vklad"], correct: 1, explanation: "Keď kúpiš akciu, stávaš sa spoluvlastníkom firmy. Ak sa firme darí, rastie hodnota tvojej akcie." },
          { q: "Čo je ETF fond?", answers: ["Jeden druh akcie","Košík mnohých akcií – diverzifikovaná investícia","Bankový produkt","Kryptomena"], correct: 1, explanation: "ETF je košík stoviek akcií. Kúpou jedného ETF investuješ do mnohých firiem naraz – nízke riziko, nízke poplatky." },
          { q: "Prečo je dôležitý dlhodobý horizont pri investovaní?", answers: ["Nie je dôležitý","Krátkodobé výkyvy sa vyrovnajú a historicky trhy rastú","Kvôli daniam","Lebo banky to vyžadujú"], correct: 1, explanation: "Historicky akciové trhy rastú priemerne 7–10 % ročne. Kto drží dlho, zvyčajne vyhráva." }
        ]
      },
      {
        id: "2-2", title: "Riziko a výnos", icon: "⚖️",
        questions: [
          { q: "Čo znamená diverzifikácia?", answers: ["Investovať všetko do jednej akcie","Rozložiť investície medzi rôzne aktíva","Predávať akcie každý deň","Investovať len do zlata"], correct: 1, explanation: "Diverzifikácia = 'nedávaj všetky vajcia do jedného košíka'. Rozložením znižuješ dopad zlého výkonu jednej investície." },
          { q: "Čo je volatilita?", answers: ["Stály rast hodnoty","Miera kolísania ceny investície","Bankový poplatok","Druh dlhopisu"], correct: 1, explanation: "Volatilita meria, ako veľmi cena kolíše. Vysoká volatilita = veľké výkyvy. Akcie sú volatilnejšie ako dlhopisy." },
          { q: "Ktorá investícia je všeobecne najbezpečnejšia?", answers: ["Kryptomeny","Jednotlivé akcie","Štátne dlhopisy","Komodity"], correct: 2, explanation: "Štátne dlhopisy sú považované za najbezpečnejšie – nízke riziko, ale aj nízky výnos." },
          { q: "1 000 € na 20 rokov pri 7 % ročne. Koľko budeš mať?", answers: ["1 400 €","2 140 €","3 870 €","7 000 €"], correct: 2, explanation: "Vďaka zloženému úroku: 1 000 × (1,07)^20 ≈ 3 870 €. Peniaze sa za 20 rokov takmer 4-násobne zväčšia!" }
        ]
      }
    ]
  }
];
