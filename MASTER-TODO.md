# MASTER TODO — Struttura Unificata (Tutti i Corsi)

**Ultimo aggiornamento**: 14 Novembre 2025
**Versione**: 3.0
**Status**: 🟡 Sincronizzazione completata tra tutti i TODO.md di corso

**Riferimento operativo**: Questo file sintetizza lo stato di TUTTI i corsi (C, HTMLCSS, Java, PHP, Python) ed è la fonte di verità centralizzata. I file TODO.md specifici di ogni corso contengono dettagli, i dettagli di task non vanno qui.

---

## 📊 Stato Generale Tutti i Corsi (14 Novembre 2025)

| Corso | Capitoli | PDF | Stato | Priorità | Deadline |
|-------|----------|-----|-------|----------|----------|
| **C (Terza)** | 11+App | ✅ | Completo | BASSA | — |
| **HTMLCSS** | 12 | ✅ | Completo | BASSA | — |
| **Java (Quarta)** | 10+App | ✅ | Build warnings | MEDIA | 2025-11-30 |
| **PHP** | 7+ | ✅ | In sviluppo | MEDIA | 2025-11-28 |
| **Python (Quinta)** | 18+App | ✅ | In progresso | ALTA | 2025-11-20 |

**Legenda**: ✅=Completo | 🟡=In progresso | ❌=Assente | ⚠️=Attenzione

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

## 📋 Task Completati Recenti (13-14 Novembre 2025)

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

### Cronologia Recente
- 2025-11-14: Consolidamento post-execution: Python PDF ✅, Java CONTENT-01 ✅, status aggiornati
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
