# Piano di Sviluppo - Appunti Java (Quarta)

Roadmap futura, nuovi capitoli, e miglioramenti al materiale didattico.

**Ultima modifica**: 8 Novembre 2025 | **Stato**: In espansione

---

## Stato Attuale (10 capitoli completati)

| Cap. | Titolo | Pagine | Stato |
|------|--------|--------|-------|
| 00 | Classi, Oggetti, Ereditarietà e Package | ~30 | ✅ |
| 01 | Stream e Buffer | ~25 | ✅ |
| 02 | Interfacce e Classi Astratte | ~20 | ✅ |
| 03 | Eccezioni | ~20 | ✅ |
| 04 | ArrayList | ~25 | ✅ |
| 05 | Interfacce Grafiche | ~25 | ✅ |
| 06 | Model View Controller | ~15 | ✅ |
| 07 | Lambda Expressions | ~10 | ✅ |
| 08 | Esercizi | ~20 | ✅ |
| App | Soluzioni | ~45 | ✅ |
| **Totale** | | **~280-300** | **✅** |

---

## Roadmap Futura

### Fase 1: ALTA Priorità (Fondamentali OOP avanzata)

#### 09 - Generics (Tipi Parametrici)
- **Pagine stimate**: 20-25 | **Esercizi**: 8-10
- Introduzione ai Generics, classi generiche, metodi generici
- Bounded type parameters, Wildcards (`?`, `? extends`, `? super`)
- Type erasure e limitazioni, esempi pratici (Box, Pair, Stack)
- **Dipendenze**: Cap. 04 (ArrayList)

#### 10 - Collections Framework
- **Pagine stimate**: 35-40 | **Esercizi**: 12-15
- List (ArrayList vs LinkedList), Set, Map, Queue
- Iterator, foreach, algoritmi Collections (sort, reverse, etc.)
- Comparable vs Comparator, best practices
- **Dipendenze**: Cap. 09 (Generics), Cap. 02 (Interfacce)

#### 11 - File I/O Avanzato
- **Pagine stimate**: 25-30 | **Esercizi**: 10-12
- Path/Paths, Files utility, NIO.2 (java.nio.file)
- Serializzazione oggetti (ObjectInputStream/ObjectOutputStream)
- Serializable, transient, try-with-resources
- **Dipendenze**: Cap. 01 (Stream), Cap. 03 (Eccezioni)

**Fase 1 Output**: Programmazione Java di base/intermedia completa

---

### Fase 2: MEDIA Priorità (Software professionale)

#### 12 - Multithreading e Concorrenza
- **Pagine stimate**: 30-35 | **Esercizi**: 8-10
- Thread e Runnable, ciclo di vita, sincronizzazione
- wait/notify, ExecutorService, thread pool
- Race conditions, deadlock, java.util.concurrent
- **Dipendenze**: OOP avanzata

#### 13 - Enum e Annotations
- **Pagine stimate**: 15-20 | **Esercizi**: 6-8
- Enum types, values(), valueOf(), costruttori custom
- @Override, @Deprecated, @SuppressWarnings
- Custom annotations, Retention, Target
- **Dipendenze**: Cap. 00 (OOP base)

#### 14 - Design Patterns
- **Pagine stimate**: 35-40 | **Esercizi**: 10-12
- Creational: Singleton, Factory Method, Builder
- Structural: Adapter, Decorator
- Behavioral: Observer, Strategy, Template Method
- **Dipendenze**: Tutti i cap. OOP base

**Fase 2 Output**: Competenze per sviluppo software professionale

---

### Fase 3: BASSA Priorità (Avanzati e opzionali)

#### 15 - Stream API e Optional
- **Pagine stimate**: 25-30 | **Esercizi**: 10-12
- Stream pipeline, operazioni intermedie (filter, map, sorted)
- Operazioni terminali (collect, forEach, reduce), Collectors
- Parallel streams, Optional class, programmazione funzionale
- **Dipendenze**: Cap. 07 (Lambda), Cap. 10 (Collections)

#### 16 - Testing con JUnit
- **Pagine stimate**: 20-25 | **Esercizi**: 8-10
- Struttura test, assertions, @Test, @Before, @After
- Test parametrizzati, mocking (cenni), code coverage
- TDD (cenni)
- **Dipendenze**: Nessuna particolare

#### 17 - JDBC e Database
- **Pagine stimate**: 30-35 | **Esercizi**: 8-10
- DriverManager, Connection, Statement vs PreparedStatement
- ResultSet, transazioni, connection pooling
- DAO Pattern, esempio pratico completo
- **Dipendenze**: Cap. 03 (Eccezioni), Cap. 11 (File I/O)

#### 18 - Reflection API
- **Pagine stimate**: 15-20 | **Esercizi**: 5-7
- Class object, inspezionare classi, invocare metodi dinamicamente
- Accedere a campi privati, creare istanze dinamicamente
- Casi d'uso pratici
- **Dipendenze**: OOP avanzata

**Fase 3 Output**: Corso Java livello avanzato

---

## Miglioramenti ai Capitoli Esistenti

Vedi [TODO.md](TODO.md) per i task prioritari. Sommario:

- **ALTA**: Aggiungere diagrammi UML Cap. 00, verificare GUI Cap. 05, espandere Exceptions Cap. 03
- **MEDIA**: Migliorare Lambda Cap. 07, aggiungere best practices MVC Cap. 06
- **BASSA**: Refactoring code format, consolidare imports

---

## Template per Nuovo Capitolo

Ogni capitolo deve seguire questa struttura (usa come template):

```latex
\chapter{Titolo Capitolo}

\section{Introduzione}
% Motivazione e contesto

\section{Obiettivi di Apprendimento}
\begin{itemize}
    \item Obiettivo 1
    \item Obiettivo 2
\end{itemize}

\section{Concetti Fondamentali}
% Teoria con esempi

\section{Sintassi}
% Dettagli tecnici

\section{Esempi Pratici}
% 3-5 esempi progressivi

\section{Best Practices}
% Consigli e convenzioni

\section{Errori Comuni}
% Box con \begin{errore}...\end{errore}

\section{Caso di Studio Completo}
% Esempio complesso che integra tutto

\section{Esercizi}
% 8-12 esercizi Base/Intermedio/Avanzato

\section{Riepilogo}
% Punti chiave

\section{Approfondimenti}
% Link e riferimenti
```

### Checklist completamento capitolo

- [ ] Struttura standard seguita
- [ ] Almeno 3 esempi completi e funzionanti
- [ ] Almeno 8 esercizi con soluzione
- [ ] Almeno 1 box attenzione, 1 nota, 1 errore
- [ ] Diagrammi/figure dove necessario
- [ ] Riepilogo finale e riferimenti
- [ ] Codice testato in IDE
- [ ] Revisione ortografica
- [ ] Compilazione LaTeX senza errori

---

## Comandi di Sviluppo

```bash
# Compilazione
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex

# Oppure (automatico)
latexmk -pdf main.tex

# Pulizia
rm -f *.aux *.log *.out *.toc *.lof *.lol *.fls *.fdb_latexmk *.synctex.gz capitoli/*.aux

# Conteggio pagine
pdfinfo main.pdf | grep Pages

# Controllo errori
grep -i "error\|warning" main.log | head -20
```

---

## Timeline Suggerita

- **Fase 1** (2-3 sett): Generics, Collections, File I/O Avanzato
- **Fase 2** (2-3 sett): Multithreading, Enum, Design Patterns, Testing
- **Fase 3** (2-3 sett): Stream API, JDBC, Reflection
- **Revisione finale** (1 sett): Integrazioni, esercizi, PDF finale

---

## Log Modifiche

### 2025-11-08
- ✅ Ristrutturato PIANO_SVILUPPO.md per coerenza con TODO.md e README.md
- ✅ Aggiunti cross-reference tra file
- ✅ Semplificato layout, rimossi dettagli ridondanti
- ✅ Aggiunto template standard per nuovi capitoli

### 2025-11-07
- ✅ Creato PIANO_SVILUPPO.md iniziale
- ✅ Analizzato stato attuale (10 capitoli + appendice)
- ✅ Identificati 10 argomenti per espansione futura
- ✅ Definite priorità e timeline

---

## Prossimi Passi

1. **Immediato**: Fare revisione contenuti (vedi TODO.md priorità ALTA)
2. **Prossima sessione**: Iniziare Cap. 09 (Generics) seguendo template
3. **Mantenimento**: Aggiornare questo file dopo ogni sessione

**Quando riprendi il lavoro**: Leggi README.md → TODO.md → questo file!
