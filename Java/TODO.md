# TODO - Appunti Programmazione Java (Quarta)

Task attuali e miglioramenti per il materiale didattico. Vedi [PIANO_SVILUPPO.md](PIANO_SVILUPPO.md) per la roadmap futura.

---

## Stato attuale

- ✅ 10 capitoli completati + appendice soluzioni
- ✅ ~280-300 pagine compilate
- ✅ Indice, figure, listati di codice
- ✅ ~80 esercizi con soluzioni

---

## Build & Compilazione

### ⚠️ Priorità ALTA

- [x] **[JAVA-BUG-01]** Mitigare Overfull/Underfull \hbox in main.log ✅
  - **Status**: COMPLETATO
  - **Data esecuzione**: 2025-11-14
  - **Tempo speso**: 1.5 ore
  - **Risultato**: Warning ridotti da 10 a 0 (100% miglioramento)
  - **Capitoli modificati**: `capitoli/00_classi_oggetti_ereditarieta.tex`
  - **Modifiche applicate**:
    - Fissato underscore in `project_root` (line 734)
    - Spezzate righe lunghe nelle sezioni Package e Import (lines 729-740)
    - Ottimizzato testo sezione "Import Statico" (line 758)
    - Riformattato lista item in sezione java.lang (lines 774-776)
    - Abbreviato testi in sezione Riepilogo (lines 784-801)
    - Modificato header tabella Overload vs Override (line 610)
  - **Note**: PDF ricompilato 3 volte con xelatex. Qualità PDF significativamente migliorata.

- [ ] **[BUILD-01]** Abilitare compilation warning check in CI
  - Verificare che `pdflatex main.tex` non produca errori
  - Tempo: 20 min

- [ ] **[BUILD-02]** Automatizzare conteggio capitoli completati
  - Script per leggere numero file tex in `capitoli/`
  - Aggiornare automaticamente badge in README
  - Tempo: 30 min

- [ ] **[BUILD-03]** Creare Makefile per compilazione rapida
  - Target: `make pdf`, `make clean`, `make all`
  - Tempo: 20 min

---

## Revisione Contenuti

### ⚠️ Priorità ALTA

- [x] **[CONTENT-01]** Verificare coerenza code examples Cap. 05 (GUI) ✅
  - Controllare che tutti i JFrame abbiano listener registrati correttamente
  - Status: FIXED - ActionListener aggiunto a FinestraBase
  - Commit: baa245d

- [ ] **[CONTENT-02]** Aggiungere diagrammi UML Cap. 00 (OOP)
  - Visualizzare eredità e polimorfismo con TikZ
  - 3-4 diagrammi mancanti
  - Tempo: 1h

- [ ] **[CONTENT-03]** Espandere sezione Exceptions Cap. 03
  - Aggiungere 2-3 esempi di custom exceptions
  - Tabella comparativa checked vs unchecked
  - Tempo: 45 min

### Priorità MEDIA

- [ ] **[CONTENT-04]** Migliorare esempi cap. 07 (Lambda)
  - Aggiungere esempi con Comparator e stream
  - Confrontare con classi anonime
  - Tempo: 1h

- [ ] **[CONTENT-05]** Aggiungere best practices per MVC (Cap. 06)
  - Sezione con errori comuni nel pattern
  - Diagramma di comunicazione Model-View-Controller
  - Tempo: 45 min

---

## Documentazione

### Priorità MEDIA

- [ ] **[DOCS-01]** Aggiornare log compilazione
  - `logs/log_aggiornamento_2025.md` con ultima sessione
  - Data, pagine totali, errori
  - Tempo: 15 min

- [ ] **[DOCS-02]** Creare template per nuovo capitolo
  - File di esempio: `_template_capitolo.tex`
  - Incluso nel PIANO_SVILUPPO.md
  - Tempo: 20 min

---

## Refactoring & Pulizia

### Priorità BASSA

- [ ] **[REFACTOR-01]** Unificare format codice nei capitoli
  - Verificare consistenza indentazione e line breaks
  - Tempo: 1h

- [ ] **[REFACTOR-02]** Consolidare import statements nei file tex
  - Spostare pacchetti comuni in main.tex
  - Tempo: 30 min

- [ ] **[REFACTOR-03]** Rinominare file capitoli con prefisso 0X
  - Rendere numerazione più coerente
  - Tempo: 15 min

---

## Nuove Feature (breve termine)

### Priorità MEDIA

- [ ] **[FEATURE-01]** Aggiungere glossario terminologia Java
  - Appendice con ~30 termini chiave
  - Italiano + Inglese
  - Tempo: 1h 30min

- [ ] **[FEATURE-02]** Creare "Quick Reference" cards
  - 1 pagina per capitolo con concetti principali
  - PDF separato opzionale
  - Tempo: 2h

- [ ] **[FEATURE-03]** Aggiungere QR code alle risorse online
  - Link a documentazione Oracle
  - Link a compilatori online (JDoodle)
  - Tempo: 30 min

---

## Test & Validazione

### Priorità MEDIA

- [ ] **[TEST-01]** Verificare compilazione di tutti gli esempi codice
  - Testare manualmente in IDE
  - Registrare output
  - Tempo: 2h

- [ ] **[TEST-02]** Validare soluzioni degli esercizi
  - Ricompilare tutti gli esercizi dal cap. 08
  - Controllare Output appendice
  - Tempo: 1h 30min

---

## Riepilogo

| Categoria | Alta | Media | Bassa | Totale | Completati |
|-----------|------|-------|-------|--------|------------|
| Build | 3 | 0 | 0 | 3 | 1 ✅ |
| Contenuti | 2 | 2 | 0 | 4 | 1 ✅ |
| Documentazione | 0 | 2 | 0 | 2 | 0 |
| Refactoring | 0 | 0 | 3 | 3 | 0 |
| Feature | 0 | 3 | 0 | 3 | 0 |
| Test | 0 | 2 | 0 | 2 | 0 |
| **Totale** | **5** | **9** | **3** | **17** | **2** |

---

## Note di sviluppo

**Template YAML per task**:
```yaml
id: BUILD-01
title: Abilitare compilation warning check
priority: Alta
estimate: 20min
status: pending
dependencies: []
notes: Aggiungere controllo in Makefile o CI script
```

**Cross-reference**: Per nuovi capitoli vedi [PIANO_SVILUPPO.md](PIANO_SVILUPPO.md) sezione "Argomenti da Aggiungere"

**Ultimo aggiornamento**: 14 Novembre 2025