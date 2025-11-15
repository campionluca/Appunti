# Appunti di Programmazione Python - 5° Anno

Corso avanzato di **Programmazione Python** per studenti, autodidatti o professionisti che desiderano una comprensione completa del linguaggio, dalle basi fino ad argomenti di sviluppo pratico (applicazioni GUI, web e automazione).

---

## Descrizione

Materiale didattico organizzato in forma di libro LaTeX. Copre i fondamenti della programmazione Python fino a pattern applicativi avanzati.

**Stato del progetto**: In sviluppo (moduli 00–15 in bozza con introduzioni ampliate; PDF compilato).
**PDF**: main.pdf (638KB, compilato il 2025-11-14)

Per approfondimenti:
- Consulta [PIANO_SVILUPPO.md](PIANO_SVILUPPO.md) per la roadmap
- Consulta [TODO.md](TODO.md) per i task di sviluppo

---

## Struttura prevista

```
Python/
├── README.md
├── PIANO_SVILUPPO.md
├── TODO.md
├── main.tex
├── capitoli/
│   ├── 00_fondamenti_python.tex
│   ├── 01_controllo_flusso.tex
│   ├── 02_funzioni.tex
│   ├── 03_strutture_dati.tex
│   ├── 04_stringhe_formattazione.tex
│   ├── 05_file_io.tex
│   ├── 06_gestione_errori.tex
│   ├── 07_moduli_package.tex
│   ├── 08_programmazione_oggetti.tex
│   ├── 09_decoratori_iteratori_generatori.tex
│   ├── 10_standard_library_avanzata.tex
│   ├── 11_gui_tkinter.tex
│   ├── 12_web_flask.tex
│   ├── 13_automazione_web_scraping.tex
│   ├── 14_testing_debugging.tex
│   ├── 15_database_sqlite_sqlalchemy.tex
│   └── appendice_soluzioni.tex
├── immagini/
│   └── .gitkeep
└── logs/
    └── log_2025.md
```

---

## Obiettivi del corso

- Acquisire padronanza della sintassi e degli idiomi Pythonic  
- Utilizzare correttamente funzioni, classi e moduli  
- Scrivere codice leggibile, mantenibile e conforme a **PEP 8**  
- Gestire file, eccezioni, strutture dati e flussi di controllo  
- Introdurre concetti avanzati: OOP, decoratori, context manager  
- Creare applicazioni pratiche (CLI, GUI, web)

---

## Requisiti tecnici

### Per studiare il corso
- **Python**: 3.10 o superiore
- **Editor**: VS Code, PyCharm, Thonny o IDLE

### Per compilare il PDF LaTeX
- **LaTeX**: distribuzione completa (TeX Live o MiKTeX)
- Pacchetti principali: `babel`, `geometry`, `listings`, `hyperref`, `tcolorbox`, `tikz`

---

## Compilazione

### Metodo 1: pdflatex (3 passate)
```bash
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

### Metodo 2: latexmk (automatico - consigliato)
```bash
latexmk -pdf main.tex
```

### Pulizia file temporanei
```bash
rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk capitoli/*.aux
```

## Stato build (LaTeX)

- Ultima esecuzione: 14 Novembre 2025
- Errori: 0
- Avvisi: ~5 (Underfull \hbox)
- Note: gli avvisi sono tipici e non bloccanti; si possono mitigare con micro-ottimizzazioni tipografiche.
- Correzioni applicate: escapati caratteri speciali (&, _, __) in tutti i texttt

Verifica rapida da Windows:

```
python tools\check_build.py
```

## Linee guida LaTeX (convenzioni)

- Inline code con underscore: usare `\verb|...|` o `\texttt{...}`; evitare backtick `` `...` ``.
- Underscore in testo/\textbf: escapare (`exist\_ok`) oppure preferire `\verb`.
- Frecce: usare `$(\rightarrow)$` in modalità matematica, non `\textrightarrow`.
- Titoli `tcolorbox` con virgole: racchiudere il titolo tra `{...}`.
- Percorsi/metodi: mantenere coerenza con `pathlib` e esempi brevi (spezzare righe troppo lunghe).
```

---

## Stato del progetto

| Categoria | Stato |
|------------|--------|
| Struttura repository | ✅ Definita |
| Contenuti teorici | 🟡 Avviati (Moduli 00–15 in bozza, introduzioni ampliate) |
| Esempi ed esercizi | 🟡 In arricchimento (00–15 aggiornati) |
| Soluzioni | 🟡 Bozza (Appendice creata) |
| PDF principale | ✅ Compilato |
| **Descrittori Python** | **✅ COMPLETATO** |

---

## ✅ Descrittori Python - Completato

**Status**: ✅ **COMPLETATO** (14 Novembre 2025)

Progetto per generare descrittori strutturati di concetti Python con coverage analysis.

### Dati Reali Generati
- **Descrittori generati**: 41 descriptors (vs 20-25 stimati)
- **Categorie**: 17 aree tematiche
- **Idiomi Pythonic documentati**: 14
- **Livelli di difficoltà**:
  - Beginner: 16 descriptors
  - Intermediate: 21 descriptors
  - Advanced: 4 descriptors

### File Generati
- **PYTHON_DESCRIPTORS_REPORT.json** — Report completo con 41 descrittori strutturati
- **PYTHON_COVERAGE_ANALYSIS.md** — Analisi coverage per categoria
- **create_python_descriptors.py** — Script di generazione automatica
- **Data generazione**: 14 Novembre 2025

### Categorie di Descrittori (17 Aree)
1. Basics (variabili, tipi, operatori)
2. Control Flow (if, for, while)
3. Functions (def, argomenti, scope)
4. Data Structures (list, tuple, dict, set)
5. String Operations
6. File I/O
7. Error Handling
8. Modules & Packages
9. OOP Fundamentals
10. OOP Advanced
11. Decorators
12. Iterators & Generators
13. List Comprehensions
14. Lambda & Higher-Order Functions
15. GUI Tkinter
16. Web Flask
17. Database SQLite

Per dettagli consultare [TODO.md](TODO.md#-descrittori-python---completato).

---

**Versione**: 0.4 | **Aggiornato**: 14 Novembre 2025 | **Autore**: Istituto Tecnico Antonio Scarpa ITS

Moduli inclusi nel PDF: <!--MODULE_COUNT-->20<!--/MODULE_COUNT-->

---

## Capitoli su NAO (V6)

- Introduzione a NAO e NAOqi: concetti, servizi, sessione `qi`.
- Setup Ambiente e API NAOqi: rete, virtualenv, struttura progetto.
- Movimento e Visione: posture, giunti, `ALMotion`, `ALRobotPosture`, `ALVideoDevice`.

Prerequisiti: accesso a un NAO V6 in rete (IP/hostname), SDK NAOqi Python disponibile, e permessi per test di movimento e acquisizione immagini.

---

## Flusso di lavoro

- Ogni modulo segue il template: Introduzione, Obiettivi, Concetti, Esempi, Esercizi, Riepilogo, Approfondimenti.
- Dopo l’aggiunta/aggiornamento di un modulo:
  - Aggiorna stato in `PIANO_SVILUPPO.md` e micro-task in `TODO.md`.
  - Compila il PDF: `latexmk -pdf main.tex` (Windows/macOS/Linux).
  - Aggiorna il log in `logs/log_2025.md` con una breve descrizione.
