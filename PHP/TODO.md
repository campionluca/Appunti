# TODO – Appunti di Programmazione PHP

Elenco attività aggiornato in base alle ultime modifiche e allineamenti strutturali.

---

## Urgenti

- [x] **[PHP-DOC-01]** Sincronizzare PIANO_SVILUPPO.md con TODO.md e README.md
  - Responsabile: `@assistant`
  - Scadenza: 2025-11-14
  - Note: Sincronizzato PIANO_SVILUPPO.md con TODO.md e README.md - Aggiornati header, sezioni urgenti/medio/future, timeline e changelog (v0.36)
  - Data completamento: 2025-11-14
- [x] Mirror struttura Java in PHP (prefazione, appendice QR, bibliografia, quick_reference)
  - Responsabile: `@assistant`
  - Note: completati file `_template_capitolo.tex`, `quick_reference/main.tex`, inclusioni in `main.tex`
- [ ] Convertire manuale discorsivo da `.md` a `.tex`
  - Responsabile: `@assistant`
  - Scadenza: 2025-11-18
  - Note: Indice e capitoli 01–04 già creati; migrare contenuti in LaTeX
- [ ] Aggiornare `agent_instructions.json` per preferenza LaTeX nel libro PHP
  - Responsabile: `@assistant`
  - Scadenza: 2025-11-18
  - Note: aggiornare `supported_formats`/`output_format.primary` coerenti
- [ ] Rimuovere residui CSRF da capitoli/esercizi
  - Responsabile: `@assistant`
  - Note: completata rimozione principale; ricontrollo su `02_Form.tex`, `08_Upload_File.tex`, esercizi
- [ ] Verificare coerenza link README e riferimenti capitoli
  - Responsabile: `@assistant`

---

## A medio termine

- [ ] Aggiungere `capitoli/appendice_glossario.tex` e `capitoli/appendice_soluzioni.tex`
  - Responsabile: `@campi`
- [ ] Integrare quick reference nel PDF (backmatter dedicato)
  - Responsabile: `@assistant`
- [ ] Mitigare Overfull/Underfull \hbox, normalizzare layout
  - Responsabile: `@campi`
- [ ] Migliorare `update-chapter-count.sh` con supporto PowerShell/Windows
  - Responsabile: `@assistant`
- [ ] E2E percorso studente: form → sessione → upload → db (test)
  - Responsabile: `@campi`

---

## Future

- [ ] Pipeline PlantUML per diagrammi (generazione automatica)
  - Responsabile: `@assistant`
- [ ] Alternative PDO a MySQLi negli esempi
  - Responsabile: `@campi`
- [ ] Capitolo performance/ottimizzazione (OPcache, caching)
  - Responsabile: `@campi`

---

## Attività completate recenti

- [x] Creazione `quick_reference/` con `main.tex`
- [x] Aggiunta `capitoli/00_prefazione.tex`
- [x] Aggiunta `capitoli/appendice_qr.tex` e `capitoli/99_bibliografia.tex`
- [x] Aggiornato `main.tex` per includere prefazione e backmatter
- [x] Rimozione `declare(strict_types=1)` dagli esempi PHP

---

## Storico modifiche

- 2025-11-14: [PHP-DOC-01] Sincronizzato PIANO_SVILUPPO.md con TODO.md e README.md; allineati task urgenti/medio/future e timeline (v0.36).
- 2025-11-13: Mirror struttura Java; aggiunti file di prefazione/appendici; quick reference; aggiornato `main.tex`.
- 2025-11-12: Consolidamento esempi sessioni/upload; pulizia documentazione.
- 2025-11-10: Setup base LaTeX; primi capitoli ed esempi.
