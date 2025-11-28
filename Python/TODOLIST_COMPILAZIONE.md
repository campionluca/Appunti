# 📋 TODOLIST Completa - Appunti Python
**Ultimo aggiornamento**: 28 Novembre 2025
**Stato generale**: 🔴 PDF non compila - Correzioni critiche in corso

---

## 🎯 PRIORITÀ MASSIMA: Risoluzione Errori Compilazione

### ✅ Completato (Oggi 28/11/2025)

#### 1. Correzioni LaTeX Critiche
- [x] **Carattere Unicode non supportato**
  - File: `capitoli/11_gui_tkinter.tex:1082`
  - Problema: `↔` non riconosciuto da LaTeX
  - Soluzione: Sostituito con `$\leftrightarrow$`
  - Commit: `0afec50`

- [x] **Stili TikZ non definiti**
  - File: `main.tex`
  - Problema: Stili `arrow`, `box`, `template` usati ma non definiti
  - Soluzione: Aggiunti stili globali nel preambolo con `\tikzset{}`
  - Impatto: Risolve errori in 15+ diagrammi TikZ
  - Commit: `0afec50`

- [x] **Sintassi colori errata tcolorbox**
  - File: `capitoli/07_moduli_package.tex`, `capitoli/15_database_sqlite_sqlalchemy.tex`
  - Problema: `colback=black!5!white, colframe=black!75!black` causa loop infinito
  - Soluzione: Semplificato a `colback=black!5, colframe=black!75`
  - Commit: `0afec50`

- [x] **Package mancante per tabelle colorate**
  - File: `main.tex`
  - Problema: `\rowcolor` richiede package `colortbl`
  - Soluzione: Aggiunto `\usepackage{colortbl}`
  - Commit: `0afec50`

- [x] **Ambiente center non bilanciato**
  - File: `capitoli/04_stringhe_formattazione.tex:329-360`
  - Problema: `\begin{center}` prima di `\begin{table}` (ridondante)
  - Soluzione: Rimosso `\begin{center}` duplicato
  - Commit: `0afec50`

### 🔴 BLOCCANTI - Da Risolvere URGENTEMENTE

#### 2. Errori Tabella Regex (Capitolo 04)
- [ ] **Errori `\cr` multipli in tabella pattern regex**
  - File: `capitoli/04_stringhe_formattazione.tex:332-357`
  - Errore: "Missing \cr inserted" + "Misplaced \cr" (18+ occorrenze)
  - Causa probabile: Caratteri speciali nelle regex non escapati correttamente
  - Riga problematica: Pattern regex con backslash e metacaratteri
  - Impatto: **BLOCCA completamente la compilazione PDF**
  - Priorità: 🔴 CRITICA
  - Tempo stimato: 30-45 min

#### 3. Capitoli con Possibili Errori (Da Verificare)
- [ ] **Capitolo 15 - Database SQLite/SQLAlchemy**
  - Stato: Compilazione testata separatamente - FALLISCE
  - Errori noti: Problemi con verbatim/listings + colori
  - Azione: Isolare e correggere dopo cap 04
  - Priorità: 🟡 ALTA

- [ ] **Capitoli 16-18 - Robot NAO**
  - Stato: Non testati individualmente
  - Errore precedente: "Socket 'refstepcounter/target'" + capacity exceeded
  - Causa: Possibile conflitto package o loop LaTeX
  - Azione: Verificare dopo correzione cap 04 e 15
  - Priorità: 🟡 ALTA

---

## 📚 STATO CAPITOLI (19 totali + 2 appendici)

### ✅ Capitoli Probabilmente Funzionanti (00-14)
- [x] 00 - Fondamenti Python
- [x] 01 - Controllo Flusso
- [x] 02 - Funzioni
- [x] 03 - Strutture Dati
- [~] 04 - Stringhe e Formattazione ⚠️ **TABELLA REGEX DA CORREGGERE**
- [x] 05 - File I/O
- [x] 06 - Gestione Errori
- [x] 07 - Moduli e Package ✅ (corretto colori)
- [x] 08 - Programmazione Oggetti
- [x] 09 - Decoratori, Iteratori, Generatori
- [x] 10 - Standard Library Avanzata
- [x] 11 - GUI Tkinter ✅ (corretto Unicode ↔)
- [x] 12 - Web Flask
- [x] 13 - Automazione e Web Scraping
- [x] 14 - Testing e Debugging

### 🔴 Capitoli con Errori Noti (15-18)
- [~] 15 - Database SQLite/SQLAlchemy ⚠️ **ERRORI COMPILAZIONE**
- [~] 16 - Robot NAO Intro ⚠️ **NON TESTATO**
- [~] 17 - Robot NAO Setup API ⚠️ **NON TESTATO**
- [~] 18 - Robot NAO Motion/Vision ⚠️ **CAPACITY EXCEEDED ERROR**

### 📎 File Speciali
- [x] \_guida\_non\_python.tex (warning/info tra capitoli NAO)
- [ ] appendice\_soluzioni.tex (commentata in main.tex)

---

## 🛠️ PROSSIMI PASSI (Ordine di Esecuzione)

### Fase 1: Sblocco Compilazione Base ⏱️ 1-2 ore
1. [ ] **Correggere tabella regex capitolo 04** (30-45 min)
   - Escapare correttamente `\`, `{`, `}`, `$`, `^` nelle celle
   - Testare compilazione cap 00-04 isolati
   - Verificare con `pdflatex -interaction=nonstopmode`

2. [ ] **Testare compilazione progressiva cap 00-14** (15-30 min)
   - Abilitare capitoli uno alla volta
   - Identificare eventuali altri errori nascosti
   - Documentare problemi per capitolo

3. [ ] **Risolvere errori capitolo 15** (30-45 min)
   - Verificare sintassi verbatim/listings
   - Controllare caratteri speciali SQL
   - Testare isolatamente

### Fase 2: Capitoli NAO e Completamento ⏱️ 1-2 ore
4. [ ] **Diagnosticare errori capitoli NAO (16-18)** (30-60 min)
   - Compilare singolarmente ogni capitolo
   - Identificare causa "capacity exceeded"
   - Verificare conflitti package

5. [ ] **Generare PDF finale completo** (15-30 min)
   - Compilazione completa con tutti i capitoli
   - Verificare TOC e hyperlink
   - Test qualità output

### Fase 3: Ottimizzazione e Pulizia ⏱️ 2-3 ore
6. [ ] **Risolvere warning LaTeX** (45-60 min)
   - Overfull/Underfull hbox (estetica)
   - Package warnings non critici
   - Migliorare layout tabelle

7. [ ] **Aggiungere contenuti mancanti** (1-2 ore)
   - Completare esercizi (≥8 per modulo)
   - Verificare codici esempio
   - Integrare appendice soluzioni

---

## 📊 STATISTICHE PROGETTO

### Contenuti
- **Capitoli totali**: 21 file .tex
- **Capitoli core**: 16 (00-15)
- **Capitoli NAO**: 3 (16-18)
- **Appendici**: 2 (_guida_non_python, appendice_soluzioni)

### Build Status
- **PDF compilato**: ❌ NO (bloccato da errori cap 04)
- **Ultima build riuscita**: 14 Novembre 2025 (638KB, prima delle correzioni odierne)
- **Errori critici rimanenti**: 3 (cap 04 tabella, cap 15, cap 16-18)
- **Correzioni oggi**: 5 ✅

### File Modificati (Commit `0afec50`)
```
M  capitoli/04_stringhe_formattazione.tex  (correzione center)
M  capitoli/07_moduli_package.tex          (correzione colori)
M  capitoli/11_gui_tkinter.tex             (correzione Unicode)
M  capitoli/15_database_sqlite_sqlalchemy.tex (correzione colori)
M  main.tex                                 (stili TikZ + colortbl)
```

---

## 🔧 TASK TECNICI COMPLEMENTARI

### Build System
- [ ] **[BUILD-01]** Creare Makefile completo
  - Target: `pdf`, `clean`, `test-chapter`, `watch`
  - Tempo: 20-30 min
  - Priorità: 🟢 BASSA

- [ ] **[BUILD-02]** Script diagnostico errori LaTeX
  - Parser log per identificare errori comuni
  - Report leggibile con numeri riga
  - Tempo: 45-60 min
  - Priorità: 🟡 MEDIA

### Qualità Codice LaTeX
- [ ] **[QUALITY-01]** Normalizzare escape sequences
  - Uniformare `\texttt{}` vs `\verb||`
  - Verificare escape `_`, `&`, `%`, `#`
  - Tempo: 1-2 ore
  - Priorità: 🟢 BASSA

- [ ] **[QUALITY-02]** Validare tutti i listing Python
  - Eseguire codice di esempio con Python 3.11+
  - Correggere syntax errors
  - Tempo: 2-3 ore
  - Priorità: 🟡 MEDIA

### Documentazione
- [ ] **[DOCS-01]** Aggiornare README con stato build
  - Rimuovere riferimento "PDF compilato 14/11"
  - Documentare problemi noti
  - Tempo: 10 min
  - Priorità: 🟡 MEDIA

- [ ] **[DOCS-02]** Creare CHANGELOG.md
  - Tracciare tutte le correzioni
  - Versionare modifiche capitoli
  - Tempo: 20 min
  - Priorità: 🟢 BASSA

---

## 📝 NOTE TECNICHE

### Errori LaTeX Comuni Riscontrati
1. **Unicode non supportato**: Usare macro LaTeX (`$\leftrightarrow$` invece di `↔`)
2. **Colori complessi**: Evitare `color!n!color` con 3+ colori (causa loop)
3. **Stili TikZ**: Definire SEMPRE nel preambolo, mai inline
4. **Tabelle**: `\rowcolor` richiede `colortbl`, non solo `xcolor`
5. **Ambienti annidati**: `center` dentro `table` è ridondante

### Comandi Utili
```bash
# Compilazione pulita
rm -f main.aux main.log main.out main.toc
pdflatex -interaction=nonstopmode main.tex

# Verifica errori
grep "! " main.log | tail -20

# Test singolo capitolo (commentare altri in main.tex)
pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -A 5 "Error"

# Conteggio errori per tipo
grep "Missing\|Undefined\|Misplaced" main.log | sort | uniq -c
```

### Package LaTeX Richiesti (main.tex)
- ✅ `babel[italian]` - Localizzazione
- ✅ `xcolor` - Colori base
- ✅ `colortbl` - Colori in tabelle (**aggiunto oggi**)
- ✅ `tikz` + librerie - Diagrammi
- ✅ `tcolorbox[skins,breakable]` - Box colorati
- ✅ `listings` + `listingsutf8` - Codice Python
- ✅ `hyperref` - Link e PDF metadata
- ✅ `geometry` - Margini
- ✅ `amsmath`, `amssymb` - Simboli matematici

---

## 🎯 OBIETTIVI DI BREVE TERMINE (48 ore)

- [ ] **Obiettivo 1**: PDF compila senza errori con capitoli 00-14 ✅
- [ ] **Obiettivo 2**: Capitolo 15 (Database) funzionante ✅
- [ ] **Obiettivo 3**: Capitoli NAO (16-18) funzionanti o commentati ✅
- [ ] **Obiettivo 4**: PDF finale distribuibile (anche senza NAO) ✅

---

## 🏆 TRAGUARDI RAGGIUNTI

- ✅ **14 Novembre 2025**: Prima build PDF riuscita (638KB, 103 pagine)
- ✅ **28 Novembre 2025**: Risolti 5 errori critici LaTeX
  - Unicode, TikZ, colori, package, ambienti
- ✅ **28 Novembre 2025**: Creata documentazione completa stato progetto

---

**Legenda Priorità**:
- 🔴 CRITICA - Blocca compilazione PDF
- 🟡 ALTA - Impedisce distribuzione
- 🟢 MEDIA - Migliora qualità
- ⚪ BASSA - Nice to have

**Legenda Stato**:
- [x] Completato
- [~] Parziale/Con problemi
- [ ] Da fare
