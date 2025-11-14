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

## Timeline indicativa

| Fase | Periodo stimato | Output previsto |
|------|------------------|-----------------|
| Fase 1 | 2–3 settimane | Basi del linguaggio |
| Fase 2 | 3–4 settimane | Python intermedio |
| Fase 3 | 3–5 settimane | Applicazioni pratiche |

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
