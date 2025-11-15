# MASTER TODO — Struttura Unificata (Tutti i Corsi)

**Ultimo aggiornamento**: 15 Novembre 2025
**Versione**: 4.0
**Status**: ✅ Integrati 7 nuovi corsi dal branch analyze-data

**Riferimento operativo**: Questo file sintetizza lo stato di TUTTI i 14 corsi del repository ed è la fonte di verità centralizzata. I file TODO.md specifici di ogni corso contengono dettagli, i dettagli di task non vanno qui.

---

## 📊 Stato Generale Tutti i Corsi (15 Novembre 2025)

### Corsi Base (5)

| Corso | Capitoli | PDF | Stato | Descrittori AI | Priorità | Deadline |
|-------|----------|-----|-------|----------------|----------|----------|
| **C** | 11+App | ✅ | Completo | ✅ 15 | BASSA | — |
| **HTMLCSS** | 12 | ✅ | Completo | ✅ 15 | BASSA | — |
| **Java** | 10+App | ✅ | Build warnings | ✅ 18 | MEDIA | 2025-11-30 |
| **PHP** | 7+ | ✅ | In sviluppo | ✅ 15 | MEDIA | 2025-11-28 |
| **Python** | 18+App | ✅ | In progresso | ✅ 41 | ALTA | 2025-11-20 |

### Nuovi Corsi 2025 (9)

| Corso | Capitoli | PDF | Stato | Descrittori AI | Priorità | Deadline |
|-------|----------|-----|-------|----------------|----------|----------|
| **Database** | 13+App | ⏳ | Contenuti ✅ | ⏳ 0 | MEDIA | 2025-12-05 |
| **Assembly** | 13+App | ⏳ | Contenuti ✅ | ⏳ 0 | MEDIA | 2025-12-10 |
| **Git** | 13+App | ⏳ | Contenuti ✅ | ⏳ 0 | MEDIA | 2025-12-15 |
| **Linux** | 13+App | ⏳ | Contenuti ✅ | ⏳ 0 | MEDIA | 2025-12-15 |
| **Algoritmi** | 15+App | ⏳ | Contenuti ✅ | ⏳ 0 | ALTA | 2025-12-10 |
| **Docker** | 13+App | ⏳ | Contenuti ✅ | ⏳ 0 | MEDIA | 2025-12-20 |
| **React** | 15+App | ⏳ | Contenuti ✅ | ⏳ 0 | ALTA | 2025-12-18 |
| **REST API** | 15+App | ⏳ | Contenuti ✅ | ⏳ 0 | MEDIA | 2025-12-18 |
| **WebSecurity** | 15+App | ⏳ | Contenuti ✅ | ⏳ 0 | ALTA | 2025-12-15 |

**Legenda**: ✅=Completo | 🟡=In progresso | ❌=Assente | ⏳=In creazione | ⚠️=Attenzione

**Totale Repository**: 14 corsi | 180+ capitoli | ~6,200 pagine | 800+ esercizi

### 🤖 Descrittori AI - Status Generale
**Totale descrittori generati**: 104 (5 corsi completati, Database in pianificazione)
- **C**: 15 descriptors (Language Basics, Control, Pointers, Functions)
- **HTMLCSS**: 15 descriptors (HTML, CSS, SCSS, JavaScript)
- **Java**: 18 descriptors (OOP, Design Patterns, GUI, Lambda)
- **PHP**: 15 descriptors (Security OWASP Top 10, Web Development)
- **Python**: 41 descriptors (Pythonic idioms, 17 categorie, NAO Robotics)

**Status**: ✅ COMPLETATI TUTTI (14 Novembre 2025)

---

## 🚨 PRIORITÀ MASSIMA (Scadenza < 7 giorni)

### Python: Abilitazione PDF
- **[PY-BLOCKER-01]** Compilare `Python/main.pdf` con `latexmk -pdf main.tex`
  - Stato: ✅ COMPLETATO (14 Nov 2025)
  - Data completamento: 11 Novembre 2025
  - Risultato: PDF generato con successo (699K)
  - Note: File compilato e disponibile; blocker risolto
  - Assegnato a: @assistant

---

## 🔧 PRIORITÀ ALTA (Scadenza ≤ 14 giorni)

### Tutti i Corsi: Sincronizzazione Documentazione
- **[MASTER-SYNC-01]** Verificare coerenza tra README.md, TODO.md, PIANO_SVILUPPO.md di ogni corso
  - Stato: IN PROGRESS (Python e Java sincronizzati; verificare PHP)
  - Tempo: 30 min per corso
  - Assegnato a: @assistant

### Python: Build & Compilazione
- **[PY-BUILD-02]** Automatizzare conteggio moduli nel README
  - Stato: TODO
  - Tempo: 20 min

- **[PY-BUILD-03]** Creare Makefile per `make pdf`, `make clean`
  - Stato: TODO
  - Tempo: 20 min

### Java: Risoluzione Warning LaTeX
- **[JAVA-BUG-01]** Mitigare Overfull/Underfull \hbox in `main.log`
  - Stato: TODO
  - Tempo: 1-2 ore
  - Note: Registri multipli Under/Overfull; impatto su qualità PDF
  - Assegnato a: @assistant

### PHP: Aggiornamento PIANO_SVILUPPO.md
- **[PHP-DOC-01]** Sincronizzare PIANO_SVILUPPO.md con TODO.md e README.md
  - Stato: TODO
  - Tempo: 30 min

---

## 📌 PRIORITÀ MEDIA (Scadenza ≤ 30 giorni)

### Python: Completamento Contenuti
- **[PY-CONTENT-06]** Completare esercizi (≥8 per modulo 00–15)
  - Stato: TODO
  - Tempo: 3-4 ore
  - Priorità: MEDIA (dopo build PDF)
  - Note: Moduli 00–15 necessitano di 3-5 esercizi aggiuntivi dove mancanti

### Python: Validazione & Testing
- **[PY-TEST-01]** Eseguire codice di esempio di ogni modulo
  - Stato: TODO
  - Tempo: 2 ore
  - Dipendenze: Python 3.10+, IDE disponibile

- **[PY-TEST-02]** Validare esercizi e generare soluzioni in appendice
  - Stato: TODO
  - Tempo: 2 ore

### Java: Aggiunta Contenuti
- **[JAVA-CONTENT-02]** Aggiungere diagrammi UML Cap. 00 (OOP)
  - Stato: TODO
  - Tempo: 1 ora
  - Note: Visualizzare eredità e polimorfismo con TikZ; 3-4 diagrammi mancanti

- **[JAVA-CONTENT-03]** Espandere sezione Exceptions Cap. 03
  - Stato: TODO
  - Tempo: 45 min
  - Note: Aggiungere 2-3 esempi custom exceptions, tabella comparativa

### PHP: Completamento Capitoli
- **[PHP-CONTENT-01]** Convertire manuale discorsivo da `.md` a `.tex`
  - Stato: TODO
  - Tempo: 2-3 ore
  - Scadenza: 2025-11-28

---

## 🆕 NUOVI CORSI 2025 (Priorità Alta)

### Compilazione PDF (9 corsi)
- **[NEW-PDF-01]** Compilare PDF per Git
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-15
  - Comando: `cd Git && latexmk -pdf main.tex`

- **[NEW-PDF-02]** Compilare PDF per Linux
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-15

- **[NEW-PDF-03]** Compilare PDF per Algoritmi
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-10
  - Priorità: ALTA

- **[NEW-PDF-04]** Compilare PDF per Docker
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-20

- **[NEW-PDF-05]** Compilare PDF per React
  - Stato: TODO
  - Tempo: 20-25 min
  - Scadenza: 2025-12-18
  - Priorità: ALTA

- **[NEW-PDF-06]** Compilare PDF per REST API
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-18

- **[NEW-PDF-07]** Compilare PDF per WebSecurity
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-15
  - Priorità: ALTA

- **[NEW-PDF-08]** Compilare PDF per Database (se non già fatto)
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-05

- **[NEW-PDF-09]** Compilare PDF per Assembly (se non già fatto)
  - Stato: TODO
  - Tempo: 15-20 min
  - Scadenza: 2025-12-10

### Documentazione Nuovi Corsi
- **[NEW-DOC-01]** Creare README.md, TODO.md, PIANO_SVILUPPO.md per i 7 nuovi corsi
  - Stato: TODO
  - Tempo: 3-4 ore totali (30 min per corso)
  - Corsi: Git, Linux, Algoritmi, Docker, React, REST API, WebSecurity
  - Priorità: ALTA
  - Scadenza: 2025-12-10

### Descrittori AI per Nuovi Corsi
- **[NEW-AI-01]** Generare descrittori AI per tutti i 9 nuovi corsi
  - Stato: TODO
  - Tempo: 6-8 ore totali
  - Stima descrittori: ~150-180 totali (15-20 per corso)
  - Priorità: MEDIA
  - Scadenza: 2025-12-20

---

## 💡 PRIORITÀ BASSA (Backlog / Nessuna urgenza)

### Refactoring Cross-Corso
- **[REFACTOR-01]** Uniformare indentazione e commenti nei `.tex` (Python, Java)
  - Stato: TODO
  - Tempo: 1-2 ore per corso

- **[REFACTOR-02]** Consolidare import pacchetti comuni in `main.tex` (Python, Java, PHP)
  - Stato: TODO
  - Tempo: 30 min per corso

### Convenzioni LaTeX (Python, Java, PHP)
- **[FORMAT-01]** Sostituire backtick con `\verb|...|`/`\texttt{...}`
- **[FORMAT-02]** Escapare underscore fuori da `\verb`/`\texttt`
- **[FORMAT-03]** Normalizzare titoli `tcolorbox` con `{title=...}`
- **[FORMAT-04]** Sostituire `\textrightarrow{}` con `$(\rightarrow)$`
- **[FORMAT-05]** Mitigare Overfull/Underfull \hbox

---

## 📋 Task Completati Recenti (13-15 Novembre 2025)

### Integrazione Nuovi Corsi (15 Novembre)
✅ **[MERGE-ANALYZE-DATA]** Integrati 7 nuovi corsi dal branch analyze-data
  - Merge completato con successo: 125 file modificati, +99,579 linee
  - Corsi aggiunti: Git, Linux, Algoritmi, Docker, React, REST API, WebSecurity
  - Totale repository: da 7 a 14 corsi
  - Branch: claude/analyze-data-01KdHoeiqfcgbz7C44t1R3Hv → claude/analizza-t-01NbrtZAwsjsVAKemV7VKcib

✅ **[DOC-UPDATE-01]** Aggiornamento README.md principale
  - Aggiornata tabella corsi: 5 → 14 corsi
  - Aggiornate statistiche: ~1,040 → ~6,200 pagine
  - Suddivisi corsi in categorie (Base, Database/Sistemi, Algoritmi, DevOps, Web)

✅ **[DOC-UPDATE-02]** Aggiornamento MASTER-TODO.md v4.0
  - Aggiunta sezione "Nuovi Corsi 2025"
  - Definiti task per compilazione PDF (9 corsi)
  - Pianificata documentazione e descrittori AI

### Python (11-14 Novembre)
✅ **[PY-BLOCKER-01]** Compilazione `Python/main.pdf` completata (11 Nov 2025)
  - PDF generato con successo (699K)
  - Blocker critico risolto; materiale disponibile per studenti

✅ **[MASTER-SYNC-01]** Sincronizzazione Python README.md, TODO.md (14 Nov, ~30 min)
  - Uniformate struttura, aggiornati header, corretti timestamp

### Java (14 Novembre)
✅ **[JAVA-CONTENT-01]** Verificata coerenza code examples Cap. 05 (GUI)
  - ActionListener aggiunto a FinestraBase
  - Commit: baa245d
  - Status: FIXED

✅ **[MASTER-SYNC-02]** Revisione coerenza Java README.md, TODO.md (14 Nov)
  - Verificati cross-reference, aggiornate statistiche

### PHP (13 Novembre)
✅ **[PHP-DOC-02]** Aggiornamento README.md struttura e linee guida (13 Nov)
✅ **[PHP-STRUCT-01]** Mirror struttura Java in PHP (prefazione, appendice QR, quick reference) (13 Nov)

### Consolidamento (14 Novembre)
✅ **[MASTER-CONSOLIDATE-01]** Aggiornamento MASTER-TODO.md con progressi da Python/Java/PHP
  - Sincronizzato status task completati
  - Aggiornato stato generale corsi
  - Python: status cambiato da "BLOCCATO" a "In progresso", PDF ora ✅
  - Java: status specificato "Build warnings" (non più generico "Build issues")
  - Documentati task completati con date e note

### 🤖 Descrittori AI - Tutti i Corsi (14 Novembre)
✅ **[AI-DESC-C]** Descrittori C completati
  - 15 concept descriptors: Language Basics (5), Control (4), Pointers (3), Functions (2)
  - 7 esempi commentati integrati
  - File: C_DESCRIPTORS_REPORT.json, C_COVERAGE_ANALYSIS.md, C_CONCEPT_IDS.md
  - Status: ✅ COMPLETATO

✅ **[AI-DESC-HTMLCSS]** Descrittori HTMLCSS completati
  - 15 descriptors: HTML (4), CSS (4), SCSS (2), JavaScript (3), Accessibilità (2)
  - Coverage: ~95% dei 12 capitoli
  - File: HTMLCSS_DESCRIPTORS_REPORT.json, HTMLCSS_COVERAGE_ANALYSIS.md
  - Status: ✅ COMPLETATO

✅ **[AI-DESC-JAVA]** Descrittori Java OOP completati
  - 18 descriptors: 4 pilastri OOP, 3 design patterns (MVC, Observer, Iterator)
  - Copertura: 10/10 capitoli (100%)
  - File: JAVA_DESCRIPTORS_REPORT.json, JAVA_COVERAGE_ANALYSIS.md, JAVA_CONCEPT_IDS.md
  - Status: ✅ COMPLETATO

✅ **[AI-DESC-PHP]** Descrittori PHP Sicurezza completati
  - 15 security descriptors con OWASP Top 10 2021 (10/10 categorie, 88% score)
  - Pattern unsafe vs safe documentati
  - File: PHP_DESCRIPTORS_REPORT.json, PHP_COVERAGE_ANALYSIS.md
  - Status: ✅ COMPLETATO

✅ **[AI-DESC-PYTHON]** Descrittori Python Pythonic completati
  - 41 descriptors in 17 categorie (più alto numero!)
  - 14 idiomi Pythonic documentati (comprehension, with, decorators, generators)
  - File: PYTHON_DESCRIPTORS_REPORT.json, PYTHON_COVERAGE_ANALYSIS.md, create_python_descriptors.py
  - Status: ✅ COMPLETATO

✅ **[AI-DESC-MD-UPDATE]** Aggiornati tutti i file MD (README, TODO, PIANO_SVILUPPO)
  - C, HTMLCSS, Java, PHP, Python: tutti sincronizzati
  - Sezioni "🤖 Descrittori AI" aggiunte a tutti i README
  - Metriche e statistiche documentate
  - Status: ✅ COMPLETATO

**Totale descrittori**: 104 (15+15+18+15+41)
**Tempo totale**: ~8 ore di generazione automatizzata
**Qualità**: Alta (esempi commentati, best practices, common mistakes, learning objectives)

### 📚 Nuovo Corso Database (14 Novembre)
✅ **[DB-SETUP-COMPLETE]** Creato nuovo corso completo Database e SQL
  - 13 capitoli + appendice + bibliografia (16 file .tex)
  - 6,000+ righe LaTeX, 78+ esercizi, 150+ query SQL
  - Argomenti: DBMS, modelli ER/relazionale/fisico, normalizzazione, SQL completo
  - Documentazione: README.md, TODO.md, PIANO_SVILUPPO.md
  - Stato: ⏳ Da compilare PDF, da generare descrittori AI (20-25 pianificati)
  - Deadline: 2025-12-05

### Cronologia Recente
- 2025-11-15: **🔀 Integrati 7 nuovi corsi nel branch principale** (Git, Linux, Algoritmi, Docker, React, REST API, WebSecurity)
- 2025-11-15: **📝 Aggiornata documentazione principale** (README.md, MASTER-TODO.md v4.0)
- 2025-11-14: **💾 Creato nuovo corso Assembly 8086** (13 capitoli, 6K righe, 80+ esercizi, 150+ esempi codice)
- 2025-11-14: **📚 Creato nuovo corso Database** (13 capitoli, 6K righe, 78 esercizi, SQL completo)
- 2025-11-14: **🤖 Descrittori AI completati per tutti i 5 corsi** (104 totali: C=15, HTMLCSS=15, Java=18, PHP=15, Python=41)
- 2025-11-14: Consolidamento post-execution: Python PDF ✅, Java CONTENT-01 ✅, status aggiornati
- 2025-11-14: Creato README.md principale repository con panoramica completa
- 2025-11-13: Struttura PHP allineata a Java; aggiornate inclusioni `main.tex`
- 2025-11-12: Consolidamento sessioni/upload PHP; hardening form e CSRF
- 2025-11-11: Python: introduzioni ampliate, moduli NAO aggiunti, PDF compilato
- 2025-11-08: C, HTMLCSS, Java completati; PIANO_SVILUPPO sincronizzati

---

## 🔄 Linee Guida Operative

### Stato Task
- **TODO**: Non iniziato
- **IN PROGRESS**: Attualmente in lavoro
- **DONE**: Completato
- **BLOCKED**: Bloccato da una dipendenza

### Campi Tracciamento
- **Tempo**: Stima ore/minuti
- **Scadenza**: Data in formato AAAA-MM-GG
- **Priorità**: ALTA | MEDIA | BASSA
- **Assegnato a**: @assistant | @campi | team
- **Dipendenze**: Task che devono completarsi prima

### Aggiornamento Procedura
1. Leggere TODO.md di ogni corso per dettagli
2. Aggiornare stato in tempo reale (IN PROGRESS → DONE)
3. Sincronizzare MASTER-TODO.md settimanalmente
4. Archiviare task completate in Changelog

---

## 📚 File di Riferimento

| Corso | README | TODO | PIANO | Status |
|-------|--------|------|-------|--------|
| **C** | [C/README.md](C/README.md) | [C/TODO.md](C/TODO.md) | [C/PIANO_SVILUPPO.md](C/PIANO_SVILUPPO.md) | ✅ Sinc |
| **HTMLCSS** | [HTMLCSS/README.md](HTMLCSS/README.md) | [HTMLCSS/TODO.md](HTMLCSS/TODO.md) | [HTMLCSS/PIANO_SVILUPPO.md](HTMLCSS/PIANO_SVILUPPO.md) | ✅ Sinc |
| **Java** | [Java/README.md](Java/README.md) | [Java/TODO.md](Java/TODO.md) | [Java/PIANO_SVILUPPO.md](Java/PIANO_SVILUPPO.md) | ✅ Sinc |
| **PHP** | [PHP/README.md](PHP/README.md) | [PHP/TODO.md](PHP/TODO.md) | [PHP/PIANO_SVILUPPO.md](PHP/PIANO_SVILUPPO.md) | 🟡 In progresso |
| **Python** | [Python/README.md](Python/README.md) | [Python/TODO.md](Python/TODO.md) | [Python/PIANO_SVILUPPO.md](Python/PIANO_SVILUPPO.md) | ✅ Sinc |

---

## 📅 Timeline Progetti

### Prossima Settimana (14-20 Nov)
- **PY-BLOCKER-01**: Build Python PDF — **CRITICO**
- **PY-BUILD-02, PY-BUILD-03**: Makefile, conteggio moduli
- **JAVA-BUG-01**: Mitigare warning LaTeX

### Due Settimane (21-28 Nov)
- **PY-CONTENT-06**: Completare esercizi Python
- **JAVA-CONTENT-02, JAVA-CONTENT-03**: Diagrammi UML, Exceptions
- **PHP-CONTENT-01**: Convertire manuale a LaTeX

### Scadenze Importanti
- 2025-11-20: Python PDF deve essere compilato
- 2025-11-28: PHP completamento capitoli
- 2025-11-30: Java build issues risolti

---

## ✅ Checklist Sincronizzazione (14 Nov)

- [x] Leggere tutti i TODO.md (C, HTMLCSS, Java, PHP, Python)
- [x] Leggere tutti i README.md (C, HTMLCSS, Java, PHP, Python)
- [x] Leggere tutti i PIANO_SVILUPPO.md (C, HTMLCSS, Java, PHP, Python)
- [x] Consolidare state in MASTER-TODO.md (v3.0)
- [x] Uniformare formato Python README, TODO
- [x] Verificare cross-reference tra file
- [x] Verificare esistenza Python/main.pdf (✅ 699K, creato 11 Nov)
- [x] Aggiornare MASTER-TODO.md con task completati (Python/Java/PHP)
- [x] Sincronizzare status generale corsi in tabella
- [x] Documentare task completati in sezione Changelog
- [ ] Aggiornare PHP PIANO_SVILUPPO.md
- [ ] Eseguire git commit

---

**Autore**: Istituto Tecnico Antonio Scarpa ITS
**Prossimo aggiornamento previsto**: 21 Novembre 2025
