# Appunti di Database e SQL

Corso completo su **Database Management Systems (DBMS)**, modellazione dati e linguaggio **SQL** per studenti di istituti tecnici e professionali.

---

## Descrizione

Materiale didattico completo per imparare a progettare, implementare e interrogare database relazionali. Il corso copre l'intero ciclo di vita: dalla modellazione concettuale (Entity-Relationship) alla normalizzazione, dall'implementazione fisica alle query SQL avanzate.

**Stato**: Versione 1.0 Completa (13 capitoli + appendice)

**PDF**: main.pdf (compilazione in corso)

**Per approfondimenti**:
- Consulta [PIANO_SVILUPPO.md](PIANO_SVILUPPO.md) per la roadmap
- Consulta [TODO.md](TODO.md) per i task di sviluppo

---

## Capitoli del Corso (13 + Appendice)

### Parte I - Teoria e Modellazione (Capitoli 1-5)

| Cap | Titolo | Argomenti Principali |
|-----|--------|---------------------|
| 01 | Introduzione DBMS | Sistemi informativi, DBMS vs File System, ACID, architettura |
| 02 | Modello Concettuale | Diagrammi ER, entità, attributi, relazioni, cardinalità |
| 03 | Modello Logico | Modello relazionale, tabelle, chiavi, integrità referenziale |
| 04 | Normalizzazione | 1NF, 2NF, 3NF, BCNF, dipendenze funzionali, anomalie |
| 05 | Modello Fisico | Indici (B-tree, hash), viste materializzate, partizionamento |

### Parte II - Linguaggio SQL (Capitoli 6-12)

| Cap | Titolo | Argomenti Principali |
|-----|--------|---------------------|
| 06 | SQL DDL | CREATE, ALTER, DROP, PRIMARY KEY, FOREIGN KEY, vincoli |
| 07 | SQL DML - SELECT | WHERE, ORDER BY, LIMIT, funzioni, operatori |
| 08 | SQL DML - Modifiche | INSERT, UPDATE, DELETE, transazioni base |
| 09 | SQL Join | INNER, LEFT, RIGHT, FULL OUTER, CROSS, self-join |
| 10 | Funzioni Aggregate | COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING |
| 11 | Subquery e Viste | Subquery scalari/riga/tabella, EXISTS, CREATE VIEW |
| 12 | Transazioni | START TRANSACTION, COMMIT, ROLLBACK, livelli isolamento |

### Parte III - Pratica (Capitolo 13 + Appendice)

| Cap | Titolo | Contenuto |
|-----|--------|----------|
| 13 | Esercizi Completi | 20 esercizi progressivi (base → intermedio → avanzato) |
| App | Soluzioni | Soluzioni dettagliate con spiegazioni |
| 99 | Bibliografia | 50+ risorse: libri, corsi, tool, comunità |

**Totale**: ~400 pagine | 58+ esercizi capitoli | 20 esercizi completi | 150+ query SQL

---

## Obiettivi di Apprendimento

Al termine del corso sarai in grado di:

1. ✅ Progettare database con diagrammi Entity-Relationship
2. ✅ Trasformare modelli ER in schemi relazionali
3. ✅ Normalizzare tabelle per eliminare anomalie
4. ✅ Implementare database con SQL DDL
5. ✅ Interrogare database con SQL DML (SELECT)
6. ✅ Eseguire operazioni CRUD (Create, Read, Update, Delete)
7. ✅ Usare join per query su tabelle multiple
8. ✅ Applicare funzioni aggregate e raggruppamenti
9. ✅ Scrivere subquery e creare viste
10. ✅ Gestire transazioni con ACID

---

## Struttura del Progetto

```
Database/
├── README.md                    # Questo file (descrizione corso)
├── TODO.md                      # Task attuali e priorità
├── PIANO_SVILUPPO.md            # Roadmap futura
├── main.tex                     # File LaTeX principale
├── main.pdf                     # PDF compilato
├── capitoli/                    # 16 file LaTeX
│   ├── 00_prefazione.tex
│   ├── 01_introduzione_dbms.tex
│   ├── 02_modello_concettuale.tex
│   ├── 03_modello_logico.tex
│   ├── 04_normalizzazione.tex
│   ├── 05_modello_fisico.tex
│   ├── 06_sql_ddl.tex
│   ├── 07_sql_dml_select.tex
│   ├── 08_sql_dml_modifiche.tex
│   ├── 09_sql_join.tex
│   ├── 10_sql_aggregate.tex
│   ├── 11_sql_subquery_viste.tex
│   ├── 12_transazioni.tex
│   ├── 13_esercizi.tex
│   ├── appendice_soluzioni.tex
│   └── 99_bibliografia.tex
├── immagini/                    # Diagrammi e screenshot
└── logs/                        # Log di aggiornamento
```

---

## Requisiti Tecnici

### Software Necessario

**DBMS (scegli uno)**:
- **MySQL/MariaDB** (consigliato) - Open source, standard industriale
- **PostgreSQL** - Open source avanzato
- **SQLite** - Embedded, ottimo per esercitazioni
- **SQL Server Express** - Microsoft, gratuito
- **Oracle XE** - Oracle, versione gratuita

**Tool Grafici**:
- **MySQL Workbench** - Modellazione, query, amministrazione
- **phpMyAdmin** - Interfaccia web per MySQL
- **DBeaver** - Client universale multi-database
- **DataGrip** - IDE professionale JetBrains

**Modellazione ER**:
- **draw.io** (diagrams.net) - Gratuito online
- **MySQL Workbench** - Modellazione integrata
- **Lucidchart** - Professionale con trial gratuito

### Per Compilare il PDF LaTeX

```bash
# Distribuzione LaTeX completa
sudo apt-get install texlive-full  # Linux
brew install --cask mactex          # macOS
# Windows: MiKTeX da https://miktex.org/

# Pacchetti richiesti
# babel, fontspec, geometry, listings, hyperref
# tcolorbox, tikz, tikz-er2, booktabs
```

---

## Compilazione

### Metodo 1: latexmk (consigliato)

```bash
cd Database
latexmk -pdf main.tex
```

### Metodo 2: xelatex (3 passate)

```bash
cd Database
xelatex main.tex
xelatex main.tex
xelatex main.tex
```

### Pulizia File Temporanei

```bash
rm -f *.aux *.log *.out *.toc *.lof *.lol *.fls *.fdb_latexmk capitoli/*.aux
```

---

## Come Usare Questo Materiale

### Per lo Studente

1. **Studia la teoria**: Leggi i capitoli 1-5 per capire i fondamenti
2. **Disegna diagrammi ER**: La modellazione si impara praticando
3. **Installa un DBMS**: MySQL Workbench è ideale per iniziare
4. **Scrivi le query SQL**: Digita personalmente, non copiare
5. **Testa sul database**: Crea database di prova, verifica i risultati
6. **Risolvi gli esercizi**: Prova autonomamente prima delle soluzioni
7. **Progetta casi reali**: Applica i concetti a scenari concreti

### Per il Docente

- Materiale pronto per lezioni in aula o laboratorio
- Esempi SQL eseguibili immediatamente
- Esercizi progressivi per verifiche formative
- Diagrammi ER modificabili con TikZ
- Soluzioni disponibili per correzione rapida
- Casi di studio per progetti di gruppo

---

## Caratteristiche del Materiale

### Box Informativi Colorati

Il documento usa box `tcolorbox` per evidenziare:

- **Attenzione** (arancione): Punti critici, errori frequenti
- **Nota** (blu): Suggerimenti, best practices
- **Errore Comune** (rosso): Errori da evitare assolutamente
- **Esempio** (verde): Casi pratici e dimostrazioni

### Diagrammi

- **Diagrammi ER**: Entità, relazioni, cardinalità con TikZ
- **Diagrammi Venn**: Per spiegare i join
- **Diagrammi architetturali**: DBMS, client-server
- **Schemi relazionali**: Tabelle con chiavi e vincoli

### Codice SQL

Tutti gli esempi SQL:
- Sintassi MySQL 8.0+ (compatibile con la maggior parte dei DBMS)
- Syntax highlighting colorato
- Commenti in italiano per spiegare ogni passaggio
- Query eseguibili su database reali
- Best practices seguite

---

## Convenzioni Utilizzate

### SQL

- **Parole chiave**: MAIUSCOLO (SELECT, FROM, WHERE)
- **Nomi tabelle**: PascalCase (Studente, Corso, IscrizioneCorso)
- **Nomi colonne**: snake_case (id_studente, data_nascita, voto_finale)
- **Commenti**: `--` per linea singola, `/* */` per blocchi

### Diagrammi ER

- **Entità**: Rettangoli
- **Attributi**: Ovali
- **Relazioni**: Rombi
- **Cardinalità**: Notazione (min,max) o crow's foot

---

## Percorso Didattico Consigliato

### Settimana 1-2: Fondamenti
- Capitoli 1-3: DBMS, modello ER, modello relazionale
- Obiettivo: Disegnare diagrammi ER semplici

### Settimana 3-4: Normalizzazione e Implementazione
- Capitoli 4-6: Normalizzazione, fisico, DDL
- Obiettivo: Creare database con SQL DDL

### Settimana 5-7: Query SQL Base
- Capitoli 7-8: SELECT, INSERT, UPDATE, DELETE
- Obiettivo: Interrogare e modificare dati

### Settimana 8-10: Query Avanzate
- Capitoli 9-11: Join, aggregate, subquery, viste
- Obiettivo: Query complesse multi-tabella

### Settimana 11-12: Transazioni e Progetti
- Capitolo 12-13: Transazioni, esercizi completi
- Obiettivo: Progettare e implementare database completi

---

## Database di Esempio

Il corso include schemi completi per:

- **Biblioteca**: Libri, autori, prestiti, utenti
- **E-commerce**: Prodotti, ordini, clienti, pagamenti
- **Ospedale**: Pazienti, medici, appuntamenti, diagnosi
- **Scuola**: Studenti, corsi, iscrizioni, voti
- **Azienda**: Dipendenti, dipartimenti, progetti, stipendi
- **Social Media**: Utenti, post, commenti, like, follower

Tutti gli schemi sono:
- Normalizzati fino a 3NF
- Con vincoli di integrità referenziale
- Accompagnati da query SQL di esempio
- Disponibili come script SQL eseguibili

---

## Risorse Utili

### Documentazione Ufficiale

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQL Standard (ISO/IEC 9075)](https://www.iso.org/standard/63555.html)

### Tutorial Online

- [SQLZoo](https://sqlzoo.net/) - Tutorial interattivi gratuiti
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/)
- [W3Schools SQL](https://www.w3schools.com/sql/)
- [LeetCode Database](https://leetcode.com/problemset/database/)

### Tool Online

- [DB Fiddle](https://www.db-fiddle.com/) - SQL sandbox online
- [SQL Fiddle](http://sqlfiddle.com/) - Testa query SQL
- [dbdiagram.io](https://dbdiagram.io/) - Diagrammi ER online

### Libri Consigliati

- "Database System Concepts" - Silberschatz, Korth, Sudarshan
- "SQL Performance Explained" - Markus Winand
- "Learning SQL" - Alan Beaulieu (O'Reilly)
- "MySQL Cookbook" - Paul DuBois (O'Reilly)

---

## Statistiche Corso

| Metrica | Valore |
|---------|--------|
| **Capitoli** | 13 + Appendice |
| **Pagine** | ~400 (stimate) |
| **Esercizi** | 78+ (58 capitoli + 20 completi) |
| **Query SQL** | 150+ esempi commentati |
| **Diagrammi** | 30+ (ER, Venn, architetturali) |
| **Schemi DB** | 6 database completi |
| **Box Colorati** | 100+ (attenzione, nota, errore, esempio) |

---

## Licenza e Contributi

### Licenza

Materiale didattico per uso educativo.

**Istituto Tecnico Antonio Scarpa ITS** - Anno Scolastico 2025-2026

### Contributi

Sono benvenuti miglioramenti e correzioni:
- Apri una issue per segnalare errori
- Proponi miglioramenti con pull request
- Mantieni coerenza con lo stile esistente
- Testa le query SQL prima di proporre modifiche

---

## Collegamento con Altri Corsi

Questo corso Database si integra perfettamente con:

- **C (Terza)**: Gestione file e strutture dati preparano per i DBMS
- **Java (Quarta)**: JDBC per connessione a database da applicazioni Java
- **PHP (Quarta)**: MySQLi/PDO per web backend con database
- **Python (Quinta)**: sqlite3/SQLAlchemy per applicazioni Python

Insieme formano un percorso completo di **Full-Stack Development**.

---

## File di Riferimento

- **[TODO.md](TODO.md)**: Task attuali, priorità, piccoli miglioramenti
- **[PIANO_SVILUPPO.md](PIANO_SVILUPPO.md)**: Roadmap futura, espansioni
- **logs/**: Log di compilazione e aggiornamenti

---

**Versione**: 1.0 | **Aggiornato**: 14 Novembre 2025 | **Autore**: Prof. Luca Campion - Istituto Tecnico Antonio Scarpa ITS

---

## 🔄 Prossimi Sviluppi

- [ ] Descrittori AI per concetti Database
- [ ] Script SQL per database di esempio
- [ ] Video tutorial per query complesse
- [ ] Quiz interattivi per ogni capitolo
- [ ] Casi di studio aggiuntivi (e-government, fintech)
