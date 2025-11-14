# Piano di Sviluppo – Appunti di Programmazione Python

Roadmap futura e strategia di sviluppo per il corso completo di Python.

**Ultima modifica**: 11 Novembre 2025  
**Stato generale**: 🟡 Tutti i moduli in bozza (PDF di prova generato)

---

## Moduli Previsti

| # | Titolo | Pagine stimate | Stato |
|---|--------|----------------|-------|
| 00 | Fondamenti Python | ~25 | 🟡 In bozza |
| 01 | Controllo del Flusso | ~25 | 🟡 In bozza |
| 02 | Funzioni | ~25 | 🟡 In bozza |
| 03 | Strutture Dati | ~30 | 🟡 In bozza |
| 04 | Stringhe e Formattazione | ~20 | 🟡 In bozza |
| 05 | File e Gestione I/O | ~25 | 🟡 In bozza |
| 06 | Gestione Errori | ~20 | 🟡 In bozza |
| 07 | Moduli e Package | ~25 | 🟡 In bozza |
| 08 | Programmazione a Oggetti (OOP) | ~35 | 🟡 In bozza |
| 09 | Decoratori, Iteratori e Generator | ~25 | 🟡 In bozza |
| 10 | Standard Library Avanzata | ~30 | 🟡 In bozza |
| 11 | GUI con Tkinter | ~30 | 🟡 In bozza |
| 12 | Web Development con Flask | ~40 | 🟡 In bozza |
| 13 | Automazione e Web Scraping | ~30 | 🟡 In bozza |
| 14 | Testing e Debugging | ~25 | 🟡 In bozza |
| 15 | Database con SQLite e SQLAlchemy | ~30 | 🟡 In bozza |
| App | Soluzioni e Appendici | ~40 | 🟡 In bozza |
| 16 | NAO (V6) – Introduzione e NAOqi | ~20 | 🟡 In bozza |
| 17 | NAO (V6) – Setup Ambiente e API | ~20 | 🟡 In bozza |
| 18 | NAO (V6) – Movimento e Visione | ~25 | 🟡 In bozza |

---

## Priorità di sviluppo

### 🔹 Fase 1 — Base (Fondamentali)
Moduli 00–07: sintassi, controllo, funzioni, strutture dati, file, errori, moduli.

### 🔹 Fase 2 — Intermedio
Moduli 08–10: OOP, funzioni avanzate, libreria standard.

### 🔹 Fase 3 — Applicazioni pratiche
Moduli 11–15: GUI, Web, Database, Testing, Automazione.

### 🔹 Fase 4 — Robotica NAO (V6)
Moduli 16–18: NAOqi, setup ambiente, API principali, movimento e visione.

### 🔹 Fase 5 — Descrittori Python (In Parallel)
Generazione di descrittori strutturati per concetti Python con coverage analysis.

---

## Template per modulo (LaTeX)

Ogni modulo dovrà seguire la struttura standard:

```latex
\chapter{Titolo Modulo}
\section{Introduzione}
\section{Obiettivi di Apprendimento}
\section{Concetti Fondamentali}
\section{Esempi Pratici}
\section{Esercizi}
\section{Riepilogo}
\section{Approfondimenti}
```

Checklist completamento:
- [ ] Teoria chiara e completa  
- [ ] Almeno 3 esempi funzionanti  
- [ ] 8–10 esercizi graduati  
- [ ] Soluzioni in appendice  
- [ ] Compilazione LaTeX senza errori  

---

## Descrittori Python — Roadmap Dettagliata (Fase 5)

**Status**: 🟡 IN PROGRESS | **Deadline**: 2025-11-20

Progetto parallelo di generazione di descrittori strutturati per concetti Python con coverage analysis completa.

### Obiettivi
- Creare PYTHON_DESCRIPTORS_REPORT.json nella root repository
- Definire 20-25 descrittori coperenti 18 categorie tematiche
- Analizzare coverage tra moduli LaTeX e descrittori
- Fornire base per future analisi di completamento

### Categorie Pianificate
| # | Categoria | Descrittori Stimati | Moduli Correlati |
|---|-----------|-------------------|-----------------|
| 1 | Basics | 2 | 00, 04 |
| 2 | Control Flow | 2 | 01 |
| 3 | Functions | 2 | 02 |
| 4 | Data Structures | 2 | 03 |
| 5 | String Operations | 1 | 04 |
| 6 | File I/O | 1 | 05 |
| 7 | Error Handling | 1 | 06 |
| 8 | Modules & Packages | 1 | 07 |
| 9 | OOP Fundamentals | 2 | 08 |
| 10 | OOP Advanced | 1 | 08 |
| 11 | Decorators | 1 | 09 |
| 12 | Iterators & Generators | 1 | 09 |
| 13 | List Comprehensions | 1 | 03 |
| 14 | Lambda & Higher-Order | 1 | 02 |
| 15 | GUI Tkinter | 1 | 11 |
| 16 | Web Flask | 1 | 12 |
| 17 | Database SQLite | 1 | 15 |
| 18 | NAO Robotics | 1 | 16, 17, 18 |

### Fase di Implementazione
1. **Creazione infrastruttura** (0.75 ore)
   - Script generazione PYTHON_DESCRIPTORS_REPORT.json
   - Validazione struttura JSON

2. **Popolamento descrittori** (4.5 ore)
   - Categorie 1-6: Basics, Control, Functions, Data Structures, String, File I/O
   - Categorie 7-12: Error, Modules, OOP (Fundamental & Advanced), Decorators, Iterators
   - Categorie 13-18: Comprehensions, Lambda, GUI, Web, Database, NAO

3. **Coverage Analysis & Testing** (0.5 ore)
   - Validazione descrittori
   - Analisi coverage tra moduli e descrittori
   - Generazione report statistics

### Deliverables Attesi
- ✅ PYTHON_DESCRIPTORS_REPORT.json (20-25 descriptors)
- ✅ PYTHON_COVERAGE_ANALYSIS.md (coverage report)
- ✅ PYTHON_CONCEPT_IDS.md (mapping concetti-moduli)
- ✅ Aggiornamento TODO.md e PIANO_SVILUPPO.md

---

## Timeline indicativa

| Fase | Periodo stimato | Output previsto |
|------|------------------|-----------------|
| Fase 1 | 2–3 settimane | Basi del linguaggio |
| Fase 2 | 3–4 settimane | Python intermedio |
| Fase 3 | 3–5 settimane | Applicazioni pratiche |
| Fase 4 | 2–3 settimane | Robotica NAO (V6) |
| **Fase 5** | **1 settimana** (2025-11-14 a 2025-11-20) | **Descrittori Python + Coverage Analysis** |

---

## Note finali

- Dopo ogni sessione, aggiornare il numero di moduli completati nel README.  
- Ogni commit dovrebbe corrispondere a un modulo o sezione coerente.  
- Il file [TODO.md](TODO.md) deve mantenere la lista aggiornata di micro-task e bug.
- Annotare nel log (`logs/log_2025.md`) una descrizione sintetica delle attività svolte.

---

## Qualità tipografica e convenzioni

- Stato compilazione principale: **senza errori** (avvisi tipografici residui).
- Linee guida operative:
  - Inline code con underscore: usare `\verb|...|` o `\texttt{...}` (evitare backtick).
  - Escapare underscore in testo/\textbf (es. `exist\_ok`) o preferire `\verb`.
  - Frecce: usare `$(\rightarrow)$` in matematica (no `\textrightarrow`).
  - Titoli `tcolorbox` con virgole: racchiudere in `{...}`.
  - Spezzare righe troppo lunghe in box/testo per ridurre Overfull/Underfull \hbox.
