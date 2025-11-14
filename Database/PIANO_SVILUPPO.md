# Piano di Sviluppo - Database e SQL

**Versione**: 1.0
**Ultimo aggiornamento**: 14 Novembre 2025
**Stato**: 🟢 Corso base completo, pianificazione espansioni

---

## 📊 Riepilogo Stato Attuale

| Componente | Status | Note |
|------------|--------|------|
| **Capitoli Teorici** | ✅ 100% | 13 capitoli + appendice completi |
| **Esercizi** | ✅ 100% | 78+ esercizi con soluzioni |
| **PDF** | 🟡 In compilazione | Primo build previsto 14 Nov |
| **Script SQL** | ⏳ TODO | Database di esempio da creare |
| **Descrittori AI** | ⏳ TODO | 20-25 descriptors pianificati |
| **Documentazione** | ✅ 100% | README, TODO, PIANO completati |

**Completamento complessivo**: 80%

---

## 🎯 Obiettivi del Corso

### Obiettivi Formativi

Il corso si propone di formare studenti capaci di:

1. **Analizzare requisiti** e progettare database relazionali
2. **Modellare dati** con diagrammi Entity-Relationship
3. **Normalizzare schemi** per garantire integrità e ridurre ridondanza
4. **Implementare database** con SQL DDL
5. **Interrogare database** con SQL DML (query SELECT avanzate)
6. **Manipolare dati** con INSERT, UPDATE, DELETE
7. **Gestire transazioni** con proprietà ACID
8. **Ottimizzare performance** con indici e query tuning

### Competenze Trasversali

- **Problem solving**: Analisi e risoluzione problemi di progettazione
- **Pensiero logico**: Algebra relazionale e logica SQL
- **Attenzione ai dettagli**: Normalizzazione e vincoli di integrità
- **Capacità progettuale**: Dal modello concettuale all'implementazione
- **Debugging**: Identificare e risolvere errori SQL

---

## 📚 Struttura Didattica

### Parte I - Teoria (40% del corso)

**Capitoli 1-5: Fondamenti e Modellazione**

| Cap | Argomenti | Ore | Difficoltà |
|-----|-----------|-----|------------|
| 01 | DBMS, sistemi informativi, ACID | 3h | Beginner |
| 02 | Modello ER, entità, relazioni, cardinalità | 5h | Beginner |
| 03 | Modello relazionale, chiavi, integrità | 5h | Intermediate |
| 04 | Normalizzazione (1NF-BCNF), dipendenze | 6h | Intermediate |
| 05 | Modello fisico, indici, ottimizzazione | 4h | Advanced |

**Totale**: 23 ore teoria | **Prerequisiti**: Logica, algoritmi base

---

### Parte II - SQL (50% del corso)

**Capitoli 6-12: Linguaggio SQL**

| Cap | Argomenti | Ore | Difficoltà |
|-----|-----------|-----|------------|
| 06 | SQL DDL (CREATE, ALTER, DROP) | 4h | Beginner |
| 07 | SQL SELECT (WHERE, ORDER BY, LIMIT) | 6h | Beginner |
| 08 | INSERT, UPDATE, DELETE | 4h | Intermediate |
| 09 | Join (INNER, LEFT, RIGHT, CROSS) | 6h | Intermediate |
| 10 | Funzioni aggregate, GROUP BY, HAVING | 5h | Intermediate |
| 11 | Subquery, viste (CREATE VIEW) | 5h | Advanced |
| 12 | Transazioni, COMMIT, ROLLBACK | 4h | Advanced |

**Totale**: 34 ore SQL pratico | **Tool**: MySQL Workbench

---

### Parte III - Pratica (10% del corso)

**Capitoli 13 + Appendice: Esercizi e Progetti**

| Componente | Contenuto | Ore |
|------------|-----------|-----|
| Cap. 13 | 20 esercizi completi (base → avanzato) | 8h |
| Appendice | Soluzioni dettagliate con spiegazioni | 3h |
| Progetti | Casi di studio reali (e-commerce, social) | 6h |

**Totale**: 17 ore pratica guidata | **Output**: 6 database completi

---

## 🗓️ Timeline di Sviluppo

### Fase 1: Core Content (COMPLETATA ✅)
**Durata**: 14 Novembre 2025
**Status**: ✅ COMPLETATO

- [x] Struttura directory e main.tex
- [x] 13 capitoli LaTeX scritti (6,000+ righe)
- [x] 78+ esercizi con soluzioni
- [x] Bibliografia con 50+ risorse
- [x] README.md, TODO.md, PIANO_SVILUPPO.md

**Output**: Corso completo in formato LaTeX

---

### Fase 2: Build & Validation (IN CORSO 🟡)
**Durata**: 14-20 Novembre 2025
**Status**: 🟡 IN PROGRESS

**Task**:
- [ ] Compilare `Database/main.pdf` con latexmk
- [ ] Risolvere warning LaTeX (se presenti)
- [ ] Testare tutte le query SQL (150+) su MySQL
- [ ] Verificare compilazione diagrammi TikZ

**Deliverables**:
- PDF compilato (~400 pagine)
- Log di compilazione pulito
- Query SQL validate

---

### Fase 3: Scripts & Examples (PIANIFICATA ⏳)
**Durata**: 21-27 Novembre 2025
**Status**: ⏳ TODO

**Task**:
- [ ] Creare script DDL per 6 database di esempio
- [ ] Popolare database con dati di test (50-100 record/tabella)
- [ ] Creare script query per ogni capitolo SQL
- [ ] Testare script su MySQL 8.0+

**Database da creare**:
1. **Biblioteca**: Libri, autori, prestiti, utenti (20 tabelle)
2. **E-commerce**: Prodotti, ordini, clienti, pagamenti (25 tabelle)
3. **Ospedale**: Pazienti, medici, appuntamenti, diagnosi (18 tabelle)
4. **Scuola**: Studenti, corsi, iscrizioni, voti (15 tabelle)
5. **Azienda**: Dipendenti, dipartimenti, progetti, stipendi (12 tabelle)
6. **Social Media**: Utenti, post, commenti, like, follower (22 tabelle)

**Deliverables**:
- `/esempi/biblioteca.sql` (DDL + INSERT + SELECT)
- `/esempi/ecommerce.sql`
- `/esempi/ospedale.sql`
- `/esempi/scuola.sql`
- `/esempi/azienda.sql`
- `/esempi/social.sql`

---

### Fase 4: AI Descriptors (PIANIFICATA ⏳)
**Durata**: 28 Novembre - 4 Dicembre 2025
**Status**: ⏳ TODO

**Task**:
- [ ] Generare 20-25 concept descriptors
- [ ] Coverage analysis per capitolo
- [ ] Integrare descrittori in README/TODO

**Categorie descrittori** (12-15):
1. **DB-MODEL-ER**: Modellazione ER, entità, attributi
2. **DB-MODEL-REL**: Modello relazionale, tabelle, chiavi
3. **DB-NORM**: Normalizzazione (1NF, 2NF, 3NF, BCNF)
4. **DB-DDL**: SQL DDL (CREATE, ALTER, DROP)
5. **DB-SELECT**: SQL SELECT (WHERE, ORDER BY)
6. **DB-DML**: INSERT, UPDATE, DELETE
7. **DB-JOIN**: INNER/LEFT/RIGHT JOIN
8. **DB-AGG**: COUNT, SUM, AVG, GROUP BY
9. **DB-SUB**: Subquery e viste
10. **DB-TRANS**: Transazioni ACID
11. **DB-INDEX**: Indici e ottimizzazione
12. **DB-SECURITY**: SQL injection, GRANT/REVOKE

**Deliverables**:
- `DATABASE_DESCRIPTORS_REPORT.json`
- `DATABASE_COVERAGE_ANALYSIS.md`
- `DATABASE_CONCEPT_IDS.md`

---

### Fase 5: Enhancements (BACKLOG 📋)
**Durata**: Dicembre 2025 - Gennaio 2026
**Status**: 📋 BACKLOG

**Espansioni opzionali**:

#### Contenuti Aggiuntivi
- [ ] Capitolo 14: NoSQL (MongoDB, Redis) - 6-8 ore
- [ ] Capitolo 15: Performance Tuning (EXPLAIN, query optimization) - 4-6 ore
- [ ] Capitolo 16: Sicurezza Database (SQL injection, backup) - 3-4 ore
- [ ] Capitolo 17: Database Distribuiti (replication, sharding) - 5-6 ore

#### Quick Reference
- [ ] SQL Cheat Sheet (PDF 2-4 pagine)
- [ ] ER Modeling Quick Guide
- [ ] Normalizzazione Decision Tree
- [ ] Join Types Visual Guide

#### Video Tutorial
- [ ] 10-15 screencast per query complesse
- [ ] Walkthrough progetti completi
- [ ] Tips & tricks MySQL Workbench

#### Esercizi Interattivi
- [ ] Quiz SQLZoo-style (HTML/JavaScript)
- [ ] Sfide Coding (LeetCode-style)
- [ ] Progetti guidati step-by-step

---

## 🎓 Percorso di Apprendimento

### Livello Beginner (Settimane 1-4)

**Obiettivo**: Capire i fondamenti e scrivere query semplici

**Contenuti**:
- Capitoli 01-03: DBMS, modello ER, modello relazionale
- Capitoli 06-07: SQL DDL, SELECT base

**Competenze acquisite**:
- Disegnare diagrammi ER semplici (3-5 entità)
- Creare database con CREATE TABLE
- Scrivere query SELECT con WHERE, ORDER BY

**Progetti pratici**:
- Database biblioteca semplice (5 tabelle)
- 20 query SELECT base

---

### Livello Intermediate (Settimane 5-8)

**Obiettivo**: Normalizzare e scrivere query complesse

**Contenuti**:
- Capitolo 04: Normalizzazione
- Capitoli 08-10: DML modifiche, join, aggregate

**Competenze acquisite**:
- Normalizzare schemi fino a 3NF
- Usare join per query multi-tabella
- Applicare funzioni aggregate e raggruppamenti

**Progetti pratici**:
- Database e-commerce normalizzato (15 tabelle)
- 50 query complesse con join e aggregate

---

### Livello Advanced (Settimane 9-12)

**Obiettivo**: Ottimizzare e gestire transazioni

**Contenuti**:
- Capitolo 05: Modello fisico, indici
- Capitoli 11-12: Subquery, viste, transazioni
- Capitolo 13: Esercizi completi

**Competenze acquisite**:
- Creare indici per ottimizzazione
- Scrivere subquery e viste complesse
- Gestire transazioni con ACID

**Progetti pratici**:
- Database social media completo (20+ tabelle)
- Sistema transazionale bancario
- Report complessi con subquery

---

## 🛠️ Tool e Tecnologie

### DBMS Supportati

| DBMS | Versione | Note | Priorità |
|------|----------|------|----------|
| **MySQL** | 8.0+ | Standard del corso, esempi testati | ⭐⭐⭐⭐⭐ |
| **MariaDB** | 10.5+ | Drop-in replacement per MySQL | ⭐⭐⭐⭐ |
| **PostgreSQL** | 13+ | Avanzato, ottimo per query complesse | ⭐⭐⭐⭐ |
| **SQLite** | 3.35+ | Embedded, ottimo per esercitazioni | ⭐⭐⭐ |
| **SQL Server** | 2019+ | Enterprise Microsoft | ⭐⭐ |

**Raccomandazione**: Iniziare con **MySQL 8.0** + **MySQL Workbench**

---

### Tool Grafici

| Tool | Tipo | Piattaforma | Costo | Uso |
|------|------|-------------|-------|-----|
| **MySQL Workbench** | Modellazione + Query | Win/Mac/Linux | Gratuito | Consigliato |
| **DBeaver** | Client universale | Win/Mac/Linux | Gratuito | Alternativa |
| **DataGrip** | IDE JetBrains | Win/Mac/Linux | Commerciale | Professionale |
| **phpMyAdmin** | Web interface | Browser | Gratuito | Server-side |
| **draw.io** | Diagrammi ER | Browser/Desktop | Gratuito | Modellazione |

---

## 📖 Risorse di Apprendimento

### Libri Consigliati

**Fondamenti**:
- "Database System Concepts" (Silberschatz, Korth, Sudarshan) - Bibbia dei database
- "Fundamentals of Database Systems" (Elmasri, Navathe) - Completo e didattico

**SQL Pratico**:
- "Learning SQL" (Alan Beaulieu, O'Reilly) - Ottimo per principianti
- "SQL Performance Explained" (Markus Winand) - Ottimizzazione query

**MySQL Specifico**:
- "MySQL Cookbook" (Paul DuBois, O'Reilly) - Ricette pratiche
- "High Performance MySQL" (Schwartz, Zaitsev, Tkachenko) - Performance tuning

---

### Corsi Online

**Gratuiti**:
- [SQLZoo](https://sqlzoo.net/) - Tutorial interattivi progressivi
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) - Query pratiche
- [W3Schools SQL](https://www.w3schools.com/sql/) - Reference veloce
- [Khan Academy - Intro to SQL](https://www.khanacademy.org/computing/computer-programming/sql)

**A pagamento** (con trial):
- [DataCamp - SQL Fundamentals](https://www.datacamp.com/tracks/sql-fundamentals)
- [Udemy - The Complete SQL Bootcamp](https://www.udemy.com/course/the-complete-sql-bootcamp/)
- [Coursera - SQL for Data Science](https://www.coursera.org/learn/sql-for-data-science)

---

### Practice Platforms

| Piattaforma | Tipo | Difficoltà | Note |
|-------------|------|------------|------|
| [LeetCode Database](https://leetcode.com/problemset/database/) | Coding challenges | Easy → Hard | 200+ problemi |
| [HackerRank SQL](https://www.hackerrank.com/domains/sql) | Skill tests | Easy → Expert | Certificazioni |
| [SQLBolt](https://sqlbolt.com/) | Tutorial interattivi | Beginner | Ottimo per iniziare |
| [DB Fiddle](https://www.db-fiddle.com/) | Sandbox online | N/A | Testa query live |

---

## 🔗 Integrazione con Altri Corsi

### Prerequisiti da Altri Corsi

**Da C (Terza)**:
- Strutture dati (preparazione per tabelle relazionali)
- File I/O (concetti base di persistenza)
- Puntatori (comprensione riferimenti e chiavi esterne)

**Da Java (Quarta)**:
- OOP (entità come classi, relazioni come associazioni)
- Collections (parallelo con tabelle e query)
- Exception handling (gestione errori SQL)

---

### Utilizzo in Corsi Successivi

**In PHP (Quarta)**:
- MySQLi/PDO per connessione da web backend
- Prepared statements per sicurezza (SQL injection)
- CRUD operations in applicazioni web

**In Python (Quinta)**:
- `sqlite3` per database embedded
- SQLAlchemy ORM per mapping oggetto-relazionale
- Pandas con SQL per data analysis

---

## 📊 Metriche di Successo

### Obiettivi Quantitativi

| Metrica | Target | Status |
|---------|--------|--------|
| Capitoli completi | 13 | ✅ 13/13 |
| Esercizi creati | 70+ | ✅ 78/70 |
| Query SQL esempi | 100+ | ✅ 150/100 |
| Database completi | 6 | ⏳ 0/6 |
| Diagrammi ER | 25+ | ✅ 30/25 |
| PDF compilato | 1 | 🟡 0/1 |
| Descrittori AI | 20 | ⏳ 0/20 |

### Obiettivi Qualitativi

- [ ] Tutti gli esempi SQL testati e funzionanti
- [ ] Diagrammi ER chiari e ben strutturati
- [ ] Esercizi graduati per difficoltà
- [ ] Soluzioni dettagliate con spiegazioni
- [ ] Codice SQL commentato in italiano
- [ ] Box colorati per evidenziare concetti chiave

---

## 🚀 Roadmap Futura (Post v1.0)

### v1.1 - SQL Avanzato (Q1 2026)
- Stored Procedures e Functions
- Triggers per automazione
- Window Functions (ROW_NUMBER, RANK, LEAD, LAG)
- Common Table Expressions (CTE)

### v1.2 - NoSQL Integration (Q2 2026)
- MongoDB basics
- Redis caching
- Confronto SQL vs NoSQL
- Polyglot persistence

### v2.0 - Full-Stack Integration (Q3 2026)
- JDBC per applicazioni Java
- MySQLi/PDO per applicazioni PHP
- SQLAlchemy per applicazioni Python
- REST API con database backend

---

## 📝 Note di Sviluppo

### Decisioni Progettuali

**Perché MySQL?**
- Standard industriale de facto
- Ampia adozione in aziende e web
- Ottima documentazione e community
- Gratuito e open source
- Compatibilità con MariaDB

**Perché TikZ per diagrammi?**
- Integrazione nativa con LaTeX
- Qualità tipografica professionale
- Versionabile con Git (file di testo)
- Personalizzabile completamente

**Perché 13 capitoli?**
- Coverage completo ma non overwhelming
- Progressione graduale beginner → advanced
- Bilanciamento teoria (5) / pratica (8)
- Tempo didattico: ~60 ore totali

---

## 🤝 Contributori

**Autore principale**: Prof. Luca Campion
**Istituzione**: Istituto Tecnico Antonio Scarpa ITS
**Anno**: 2025-2026

**Contributi benvenuti**:
- Segnalazione errori
- Suggerimenti miglioramenti
- Nuovi esercizi e casi di studio
- Script SQL aggiuntivi

---

**Prossima revisione**: 21 Novembre 2025
**Versione successiva pianificata**: 1.1 (Gennaio 2026)
