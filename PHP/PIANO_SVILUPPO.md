# PIANO DI SVILUPPO — Appunti di Programmazione PHP

Roadmap, risorse, dettagli tecnici e procedure di qualità per il corso PHP.

**Ultima modifica**: 2025-11-14

---

## Task Urgenti

**Scadenza**: 2025-11-18 (deadline intermedia)
**Obiettivo**: Completare migrazione a LaTeX e consolidare documentazione

- [x] **[PHP-DOC-01]** Sincronizzare PIANO_SVILUPPO.md con TODO.md e README.md
  - Responsabile: `@assistant`
  - Scadenza: 2025-11-14
  - Azione: Allineare roadmap con stato attuale
  - Tempo stimato: 30-45 minuti
  - Note: Aggiornato header, sezioni urgenti/medio/future, timeline e changelog (v0.36)
  - Data completamento: 2025-11-14

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

## Task A Medio Termine

**Scadenza**: 2025-11-28 (deadline completamento progetto)
**Obiettivo**: Consolidare contenuti e migliorare qualità PDF

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

## Task Future

**Priorità**: Bassa (backlog)
**Obiettivo**: Estensioni e ottimizzazioni avanzate

- [ ] Pipeline PlantUML per diagrammi (generazione automatica)
  - Responsabile: `@assistant`

- [ ] Alternative PDO a MySQLi negli esempi
  - Responsabile: `@campi`

- [ ] Capitolo performance/ottimizzazione (OPcache, caching)
  - Responsabile: `@campi`

---

## Roadmap del progetto

### Fasi e milestone

- Fase 0 — Setup (Completata)
  - Struttura LaTeX e inclusione listings
  - Esempi base in `esempi/`

- Fase 1 — Fondamentali Web (In corso)
  - Form e validazione (server‑side)
  - Cookie sicuri e preferenze
  - Sessioni robuste (rigenerazione ID, contatori)

- Fase 2 — Upload e File I/O (In corso)
  - Upload con controlli MIME e dimensione
  - Log testuale e lettura file

- Fase 3 — Database (Pianificata)
  - `mysqli` con prepared statements (SELECT/INSERT)
  - Best practices per error handling

- Fase 4 — Rifinitura e Qualità (In corso)
  - Allineamento documentazione (urgente)
  - Esercizi e soluzioni (medio termine)
  - Ottimizzazioni tipografiche LaTeX (medio termine)

### Milestone

- v0.1 — Base LaTeX + Esempi (completata)
- v0.2 — Form/Cookie/Sessioni stabili (in corso)
- v0.3 — Upload + File I/O consolidati (in corso)
- v0.35 — Sincronizzazione documentazione completa (scadenza 2025-11-18)
- v0.4 — MySQLi con prepared (pianificata per 2025-11-19)
- v1.0 — PDF stabile e validato (target 2025-11-28)

---

## Cronologia versioni e changelog

| Versione | Data | Contenuti |
|----------|------|-----------|
| 0.1 | 2025‑11‑10 | Struttura `main.tex`, capitoli base e esempi |
| 0.2 | 2025‑11‑12 | Fix path listings, compilazione XeLaTeX, sessioni+upload |
| 0.35 | 2025‑11‑13 | Mirror struttura Java: prefazione, appendice QR, bibliografia, quick reference; aggiornati include |
| 0.36 | 2025‑11‑14 | Sincronizzazione PIANO_SVILUPPO.md con TODO.md e README.md (PHP-DOC-01); aggiornate sezioni urgenti/medio/future e timeline |
| 0.4 | 2025‑11‑18 | Migrazione manuale discorsivo `.md` → `.tex`, aggiornamento `agent_instructions.json` (previsto) |
| 1.0 | 2025‑11‑28 | PDF stabile e validato, completamento progetto PHP (target) |

Note: il changelog viene aggiornato ad ogni modifica di rilievo (capitoli, esempi, tool di qualità).

---

## Pianificazione risorse e tempistiche

- Persone
  - Autore/Manutentore principale: `@campi`
  - Supporto operativo: `@assistant` (documentazione/tooling)

- Tempistiche (indicative)
  - Fase 1: 3–5 giorni (in corso)
  - Fase 2: 2–3 giorni (in corso)
  - Fase 3: 3–4 giorni (avvio 2025‑11‑19)
  - Fase 4: In corso (deadline 2025-11-28 per v1.0)

- **Timeline critica**:
  - **2025-11-14**: Sincronizzazione PIANO_SVILUPPO.md (PHP-DOC-01)
  - **2025-11-18**: Completamento task urgenti (migrazione LaTeX, agent_instructions)
  - **2025-11-28**: Deadline completamento progetto PHP (v1.0 PDF stabile)

---

## Dettagli tecnici sull’architettura

### Struttura cartelle

```
PHP/
├── main.tex          # Preambolo LaTeX + inclusioni capitoli (prefazione, appendici)
├── capitoli/         # Capitoli e backmatter (appendice_qr, 99_bibliografia)
├── quick_reference/  # Schede riassuntive (documento separato)
├── esempi/           # Codice PHP/HTML per dimostrazioni
├── esercizi/         # Tracce per esercitazioni
└── immagini/         # Risorse grafiche (se presenti)
```

### Convenzioni
- Inclusioni listings: percorsi relativi `esempi/<file>`
- Sicurezza applicativa: validazione input, escape output, cookie con flag `Secure`/`HttpOnly`/`SameSite`
- Database: operazioni con prepared statements, gestione errori minimale
- Stile PHP: PSR‑12 (indentazione, naming, spaziatura); evitare `declare(strict_types=1)` negli esempi

---

## Procedure di testing e qualità

### Testing PHP
- Esecuzione locale con server integrato (`php -S localhost:8005 -t esempi`)
- Verifiche:
  - Form: validazione email e messaggi di errore
  - Cookie: lettura/scrittura con flag di sicurezza
  - Sessioni: `session_start`, `session_regenerate_id`, contatori, scadenza
  - Upload: limiti MIME/dimensione, gestione errori
  - DB: `SELECT`/`INSERT` con prepared e controllo risultati

### Qualità documentazione
- Coerenza tra capitoli e file in `esempi/`
- Compilazione PDF con XeLaTeX (`xelatex` o `latexmk -xelatex`)
- Riduzione warning tipografici (microtype, line break)
- Aggiornamento continuo di `README.md`, `TODO.md` e `PIANO_SVILUPPO.md`

### Tool di supporto
- Scanner TODO/FIXME/NOTE (`tools/todo/scan.py`)
  - Consolidamento `MASTER-TODO.json`
  - Report giornaliero HTML (`logs/todo_reports/report_<data>.html`)

---

## Note operative
- Tutte le modifiche dovrebbero mantenere coerenza con gli esempi e con i riferimenti nei capitoli LaTeX.
- Prima di rilasciare una versione: ricompilare il PDF, rieseguire esempi critici, aggiornare changelog.

---

## Modifiche architetturali rilevanti

- Aggiunta backmatter nel libro: `appendice_qr.tex`, `99_bibliografia.tex` con inclusione in `main.tex`.
- Creata cartella `quick_reference/` con documento autonomo di schede riassuntive.
- Introdotto `_template_capitolo.tex` per standardizzare nuovi capitoli.
- Aggiunto `main0-plantuml.txt` (placeholder diagrammi) per futura integrazione.

## Nuove dipendenze/requisiti tecnici

- LaTeX: `tcolorbox`, `listingsutf8`, `microtype` già in uso; nessuna dipendenza aggiuntiva.
- Build: preferenza XeLaTeX (Unicode), compatibile MiKTeX/TeX Live.

## Criteri di accettazione aggiornati

- Struttura PHP rispecchia la gerarchia del libro Java (directory e include).
- PDF compila con capitoli e backmatter inclusi, senza errori bloccanti.
- README/TODO/PIANO aggiornati e coerenti tra loro.
- Residui CSRF rimossi dalla documentazione; esempi senza `strict_types`.
