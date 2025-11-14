# TODO - Database e SQL

**Ultimo aggiornamento**: 14 Novembre 2025
**Versione**: 1.0
**Status**: 🟢 Corso completo, in fase di revisione

---

## 📊 Stato Generale

| Categoria | Status | Completamento |
|-----------|--------|---------------|
| Capitoli teorici | ✅ | 13/13 (100%) |
| Esercizi | ✅ | 78+ creati |
| Soluzioni | ✅ | Appendice completa |
| PDF | 🟡 | In compilazione |
| Descrittori AI | ⏳ | Da generare |
| Script SQL | ⏳ | Da creare |

---

## 🚀 PRIORITÀ ALTA (Scadenza ≤ 7 giorni)

### Build e Compilazione

- **[DB-BUILD-01]** Compilare `Database/main.pdf` con latexmk
  - Stato: 🟡 TODO
  - Tempo: 30 min
  - Note: Verificare compilazione TikZ diagrams e tikz-er2
  - Comando: `latexmk -pdf main.tex`

- **[DB-BUILD-02]** Risolvere eventuali warning LaTeX
  - Stato: ⏳ PENDING (dopo BUILD-01)
  - Tempo: 1 ora
  - Focus: Overfull/Underfull hbox, riferimenti mancanti

### Validazione Contenuti

- **[DB-VALID-01]** Testare tutte le query SQL (150+ query)
  - Stato: 🟡 TODO
  - Tempo: 2-3 ore
  - Tool: MySQL Workbench
  - Note: Creare database di test per ogni esempio

- **[DB-VALID-02]** Verificare diagrammi ER (TikZ compilation)
  - Stato: 🟡 TODO
  - Tempo: 1 ora
  - Focus: Capitoli 02, 03, 13

---

## 📌 PRIORITÀ MEDIA (Scadenza ≤ 30 giorni)

### Script SQL Eseguibili

- **[DB-SCRIPT-01]** Creare script DDL per database di esempio
  - Stato: ⏳ TODO
  - Tempo: 4 ore
  - Database: Biblioteca, E-commerce, Ospedale, Scuola, Azienda, Social
  - Output: `esempi/biblioteca.sql`, `esempi/ecommerce.sql`, etc.

- **[DB-SCRIPT-02]** Creare script INSERT con dati di test
  - Stato: ⏳ TODO
  - Tempo: 3 ore
  - Quantità: 50-100 record per tabella
  - Note: Dati realistici ma fittizi

- **[DB-SCRIPT-03]** Creare script query di esempio
  - Stato: ⏳ TODO
  - Tempo: 2 ore
  - Per ogni capitolo SQL (06-12)
  - File: `esempi/cap06_ddl.sql`, `esempi/cap07_select.sql`, etc.

### Documentazione

- **[DB-DOC-01]** Aggiungere sezione "Quick Reference SQL"
  - Stato: ⏳ TODO
  - Tempo: 2 ore
  - Contenuto: Cheat sheet comandi SQL principali
  - File: `quick_reference/sql_cheatsheet.pdf`

- **[DB-DOC-02]** Creare guida installazione MySQL
  - Stato: ⏳ TODO
  - Tempo: 1 ora
  - Piattaforme: Windows, macOS, Linux
  - File: `docs/installazione_mysql.md`

### Descrittori AI

- **[DB-DESC-01]** Generare descrittori AI per concetti Database
  - Stato: ⏳ TODO
  - Tempo: 4-5 ore (agent)
  - Categorie: 12-15 (Modellazione, Normalizzazione, SQL DDL/DML, Transazioni)
  - Target: 20-25 descriptors
  - File: `DATABASE_DESCRIPTORS_REPORT.json`, `DATABASE_COVERAGE_ANALYSIS.md`

---

## 💡 PRIORITÀ BASSA (Backlog / Enhancements)

### Contenuti Aggiuntivi

- **[DB-CONTENT-01]** Aggiungere capitolo su NoSQL (opzionale)
  - Tempo: 6-8 ore
  - Argomenti: MongoDB, Redis, document stores, key-value
  - File: `capitoli/14_nosql.tex`

- **[DB-CONTENT-02]** Aggiungere capitolo su Performance Tuning
  - Tempo: 4-6 ore
  - Argomenti: EXPLAIN, indici, query optimization, caching
  - File: `capitoli/15_performance.tex`

- **[DB-CONTENT-03]** Aggiungere capitolo su Sicurezza Database
  - Tempo: 3-4 ore
  - Argomenti: SQL injection, prepared statements, GRANT/REVOKE, backup
  - File: `capitoli/16_sicurezza.tex`

### Esercizi Interattivi

- **[DB-EXERCISE-01]** Creare quiz SQLZoo-style
  - Tempo: 8-10 ore
  - Formato: HTML/JavaScript interattivo
  - Capitoli: Tutti (13)

### Diagrammi e Visualizzazioni

- **[DB-DIAGRAM-01]** Esportare diagrammi ER come PNG/SVG
  - Tempo: 2 ore
  - Tool: TikZ → PDF → ImageMagick
  - Uso: README.md, presentazioni

- **[DB-DIAGRAM-02]** Creare diagrammi animati (optional)
  - Tempo: 5-6 ore
  - Tool: Manim o D3.js
  - Concetti: Normalizzazione, join, transazioni

### Video Tutorial

- **[DB-VIDEO-01]** Registrare screencast per query complesse
  - Tempo: 10-12 ore
  - Capitoli: 09 (Join), 10 (Aggregate), 11 (Subquery)
  - Durata: 10-15 min per video

---

## 🐛 Bug e Correzioni

Al momento nessun bug noto. Segnalazioni benvenute.

---

## ✅ Task Completate (14 Novembre 2025)

### Struttura e Setup
✅ **[DB-SETUP-01]** Creata struttura directory (capitoli, immagini, logs)
✅ **[DB-SETUP-02]** Creato main.tex con preambolo e inclusioni
✅ **[DB-SETUP-03]** Configurato listings per SQL syntax highlighting
✅ **[DB-SETUP-04]** Definiti box colorati (attenzione, nota, errore, esempio)

### Contenuti Teorici
✅ **[DB-CONTENT-00]** Prefazione scritta (10 sezioni)
✅ **[DB-CONTENT-01]** Capitolo 01: Introduzione DBMS (163 righe, 5 esercizi)
✅ **[DB-CONTENT-02]** Capitolo 02: Modello Concettuale ER (231 righe, 5 esercizi)
✅ **[DB-CONTENT-03]** Capitolo 03: Modello Logico Relazionale (343 righe, 5 esercizi)
✅ **[DB-CONTENT-04]** Capitolo 04: Normalizzazione (281 righe, 5 esercizi)
✅ **[DB-CONTENT-05]** Capitolo 05: Modello Fisico (321 righe, 6 esercizi)

### Contenuti SQL
✅ **[DB-CONTENT-06]** Capitolo 06: SQL DDL (392 righe, 5 esercizi)
✅ **[DB-CONTENT-07]** Capitolo 07: SQL DML SELECT (354 righe, 6 esercizi)
✅ **[DB-CONTENT-08]** Capitolo 08: SQL DML Modifiche (350 righe, 6 esercizi)
✅ **[DB-CONTENT-09]** Capitolo 09: SQL Join (406 righe, 7 esercizi)
✅ **[DB-CONTENT-10]** Capitolo 10: SQL Aggregate (386 righe, 8 esercizi)
✅ **[DB-CONTENT-11]** Capitolo 11: Subquery e Viste (435 righe, 7 esercizi)
✅ **[DB-CONTENT-12]** Capitolo 12: Transazioni (405 righe, 6 esercizi)

### Esercizi e Appendici
✅ **[DB-CONTENT-13]** Capitolo 13: Esercizi Completi (905 righe, 20 esercizi)
✅ **[DB-APPENDIX-01]** Appendice Soluzioni (609 righe, soluzioni dettagliate)
✅ **[DB-APPENDIX-02]** Bibliografia (440 righe, 50+ risorse)

### Documentazione
✅ **[DB-DOC-00]** README.md creato (500+ righe, completo)
✅ **[DB-DOC-01]** TODO.md creato (questo file)
✅ **[DB-DOC-02]** PIANO_SVILUPPO.md creato

---

## 📈 Metriche Progetto

| Metrica | Valore |
|---------|--------|
| Capitoli | 13 + Appendice + Bibliografia |
| File LaTeX | 16 |
| Righe LaTeX | 6,000+ |
| Esercizi | 78+ (58 capitoli + 20 completi) |
| Query SQL | 150+ esempi commentati |
| Diagrammi TikZ | 30+ |
| Database esempio | 6 schemi completi |
| Risorse bibliografia | 50+ |

---

## 🔄 Procedura Aggiornamento

1. Leggere questo TODO.md per priorità
2. Completare task in ordine di priorità
3. Testare contenuti modificati
4. Aggiornare status task (TODO → IN PROGRESS → DONE)
5. Committare con messaggio descrittivo
6. Aggiornare README.md se necessario
7. Compilare PDF per verificare output finale

---

## 📅 Timeline Suggerita

### Settimana 1 (14-20 Nov 2025)
- [x] Completare tutti i capitoli LaTeX
- [ ] Compilare PDF principale
- [ ] Testare query SQL su MySQL

### Settimana 2 (21-27 Nov 2025)
- [ ] Creare script SQL eseguibili
- [ ] Generare descrittori AI
- [ ] Validare contenuti completi

### Settimana 3 (28 Nov - 4 Dic 2025)
- [ ] Quick reference SQL
- [ ] Guida installazione
- [ ] Revisione finale

---

**Prossimo aggiornamento previsto**: 21 Novembre 2025
