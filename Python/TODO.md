# TODO – Appunti di Programmazione Python

Elenco delle attività di sviluppo e manutenzione del progetto.

**Ultima modifica**: 14 Novembre 2025
**Stato generale**: 🟡 Moduli 00–15 in bozza; priorità ALTA su completamento PDF

---

## 📦 Stato Generale Progetto

### ✅ Completato
- [x] Struttura repository iniziale
- [x] Creazione moduli `.tex` (00–15 + NAO 16-18)
- [x] Template LaTeX definito
- [x] Cartelle `immagini/`, `logs/` create
- [x] Introduzioni moduli ampliate
- [x] Appendice soluzioni creata
- [x] Build PDF principale (main.pdf, 638KB) ✅ 2025-11-14
- [x] Script automatico conteggio moduli (update_module_count.sh) ✅ 2025-11-14

### ⏳ In Progresso
- [ ] Completamento esercizi (8+ per modulo)
- [ ] Validazione esempi di codice  

---

## 🔧 Task di Build & Compilazione (Priorità ALTA)

- [x] **[PY-BLOCKER-01]** Compilare PDF principale (`main.pdf`) ✅ COMPLETATO 2025-11-14
  - Stato: DONE | Tempo effettivo: ~45 min | Scadenza: 2025-11-20
  - Note: Compilato con successo (638KB, 103 pagine, PDF v1.7). Corretti errori LaTeX:
    - Escapati caratteri speciali `&` in texttt (file 03_strutture_dati.tex)
    - Escapati underscore `_` in texttt (file 03_strutture_dati.tex, 07_moduli_package.tex, 08_programmazione_oggetti.tex, 09_decoratori_iteratori_generatori.tex, 12_web_flask.tex)
    - Escapati doppi underscore `__` in texttt (file 07_moduli_package.tex, 08_programmazione_oggetti.tex, 12_web_flask.tex)
  - Risultato: PDF pronto per distribuzione agli studenti

- [x] **[PY-BUILD-02]** Automatizzare conteggio moduli nel README ✅ COMPLETATO 2025-11-14
  - Stato: DONE | Tempo effettivo: ~15 min
  - Script: creato `update_module_count.sh` che conta automaticamente i file .tex in capitoli/
  - Risultato: 20 moduli conteggiati e aggiornati nel README.md

- [ ] **[PY-BUILD-03]** Creare Makefile per `make pdf`, `make clean`
  - Stato: TODO | Tempo: 20 min  

---

## 🧠 Contenuti Moduli (Priorità ALTA → MEDIA)

### Completati (Bozza)
- [x] **[PY-CONTENT-01–04]** Moduli 00–03 con introduzioni ampliate
- [x] **[PY-CONTENT-07]** Approfondimenti in tutti i moduli (00–15)
- [x] **[PY-CONTENT-08]** Moduli NAO (V6) – Introduzione, Setup, Movimento/Visione

### In Progresso / TODO
- [ ] **[PY-CONTENT-06]** Completare esercizi (≥8 per modulo 00–15)
  - Stato: TODO | Tempo: 3-4 ore | Priorità: ALTA
  - Moduli 00–15: aggiungere 3-5 esercizi per modulo dove mancanti  
 
---
 
## 📄 Documentazione (Priorità MEDIA)

### Completati
- [x] **[PY-DOCS-01]** Log aggiornamento (`logs/log_2025.md`)
- [x] **[PY-DOCS-02]** README con istruzioni compilazione
- [x] **[PY-DOCS-03]** Documentazione struttura e PEP 8
- [x] **[PY-DOCS-04]** Descrizioni moduli (00–15)
- [x] **[PY-DOCS-05]** Sezione Capitoli NAO (V6)

### In Progresso / TODO
- [ ] **[PY-DOCS-06]** Aggiornare README: stato build e avvisi LaTeX
  - Stato: TODO | Tempo: 15 min

- [ ] **[PY-DOCS-08]** Integrare `tools/check_build.py` in CI
  - Stato: TODO | Tempo: 30 min  

---

## 🧼 Refactoring (Priorità Bassa)

- [ ] **[REFACTOR-01]** Uniformare indentazione e commenti nei file `.tex`  
- [ ] **[REFACTOR-02]** Consolidare import di pacchetti comuni in `main.tex`  

---

## 🧪 Test e Validazione

- [ ] **[TEST-01]** Eseguire codice di esempio di ogni modulo  
- [ ] **[TEST-02]** Validare gli esercizi e generare soluzioni in appendice  

---

## 🧼 Refactoring & Pulizia (Priorità BASSA)

- [ ] **[PY-REFACTOR-01]** Uniformare indentazione e commenti nei `.tex`
  - Stato: TODO | Tempo: 1 ora

- [ ] **[PY-REFACTOR-02]** Consolidare import pacchetti comuni in `main.tex`
  - Stato: TODO | Tempo: 30 min

---

## 🧪 Test & Validazione (Priorità MEDIA)

- [ ] **[PY-TEST-01]** Eseguire codice di esempio di ogni modulo
  - Stato: TODO | Tempo: 2 ore | Priorità: MEDIA

- [ ] **[PY-TEST-02]** Validare esercizi e generare soluzioni in appendice
  - Stato: TODO | Tempo: 2 ore | Priorità: MEDIA

---

## ✍️ Convenzioni LaTeX (Priorità MEDIA)

- [ ] **[PY-FORMAT-01]** Sostituire backtick con `\verb|...|`/`\texttt{...}`
- [ ] **[PY-FORMAT-02]** Escapare underscore fuori da `\verb`/`\texttt` (es. `exist\_ok`)
- [ ] **[PY-FORMAT-03]** Normalizzare titoli `tcolorbox` con `{title=...}`
- [ ] **[PY-FORMAT-04]** Sostituire `\textrightarrow{}` con `$(\rightarrow)$`
- [ ] **[PY-FORMAT-05]** Mitigare Overfull/Underfull \hbox

---

## 📊 Riepilogo Task

| Categoria | Alta | Media | Bassa | Totale |
|-----------|------|-------|-------|--------|
| Build | 3 | 0 | 0 | 3 |
| Contenuti | 1 | 0 | 0 | 1 |
| Documentazione | 0 | 2 | 0 | 2 |
| Refactoring | 0 | 0 | 2 | 2 |
| Convenzioni | 0 | 5 | 0 | 5 |
| Test | 0 | 2 | 0 | 2 |
| **Totale** | **4** | **9** | **2** | **15** |

---

---

## 📌 File di Riferimento

- **[PIANO_SVILUPPO.md](PIANO_SVILUPPO.md)** — Roadmap e fasi di sviluppo
- **[README.md](README.md)** — Descrizione corso e requisiti
- **logs/log_2025.md** — Log aggiornamenti sessioni

---

**Ultimo aggiornamento**: 14 Novembre 2025
**Autore**: Istituto Tecnico Antonio Scarpa ITS
