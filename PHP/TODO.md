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

---

## 📊 Stato Descrittori e Sicurezza

**Status**: ✅ COMPLETATO (14 Novembre 2025)

### Copertura Sicurezza Web

- **15 Security Descriptors** creati con focus OWASP Top 10
- **OWASP Top 10 2021**: Copertura **10/10 categorie** (88% score complessivo)
- **Pattern documentati**: Unsafe vs Safe side-by-side
- **Vulnerabilità mappate**: 20+ attack vectors con mitigazioni

### Categorie Descrittori

| Categoria | Descriptor | OWASP Map | Copertura |
|-----------|-----------|-----------|-----------|
| **Forms** | PHP-FORMS-001 | A07 (Auth Failures) | ⭐⭐⭐⭐⭐ |
| **Array** | PHP-ARRAY-001 | A03 (Injection) | ⭐⭐⭐⭐⭐ |
| **Cookie** | PHP-COOKIE-001 | A02 (Crypto) | ⭐⭐⭐⭐ |
| **Session** | PHP-SESSION-001 | A01 (Access Control) | ⭐⭐⭐⭐⭐ |
| **Upload** | PHP-UPLOAD-001 | A08 (Data Integrity) | ⭐⭐⭐⭐⭐ |
| **MySQLi** | PHP-MYSQLI-001 | A03 (Injection) | ⭐⭐⭐⭐⭐ |
| **XSS** | PHP-SECURITY-XSS-001 | A03 (Injection) | ⭐⭐⭐⭐⭐ |
| **SQL Injection** | PHP-SECURITY-SQLI-001 | A03 (Injection) | ⭐⭐⭐⭐⭐ |
| **CSRF** | PHP-SECURITY-CSRF-001 | A01 (Access Control) | ⭐⭐⭐⭐ |
| **Authentication** | PHP-AUTH-001 | A07 (Auth Failures) | ⭐⭐⭐⭐⭐ |
| **File I/O** | PHP-FILE-001 | A10 (SSRF) | ⭐⭐⭐⭐ |
| **Router** | PHP-ROUTER-001 | A04 (Insecure Design) | ⭐⭐⭐⭐ |
| **Basics** | PHP-BASICS-001 | A04 (Insecure Design) | ⭐⭐⭐⭐⭐ |

### OWASP Top 10 2021 - Mappatura Completa

| Categoria OWASP | Copertura | Descriptors | Implementazione |
|-----------------|-----------|------------|-----------------|
| **A01** Broken Access Control | ⭐⭐⭐⭐⭐ | SESSION-001, AUTH-001, CSRF-001 | Session regeneration, CSRF token, timeouts |
| **A02** Cryptographic Failures | ⭐⭐⭐⭐⭐ | AUTH-001, COOKIE-001 | Argon2id hashing, HTTPS, secure flags |
| **A03** Injection | ⭐⭐⭐⭐⭐ | SQLI-001, XSS-001, MYSQLI-001 | Prepared statements, htmlspecialchars, binding |
| **A04** Insecure Design | ⭐⭐⭐⭐ | FORMS-001, SESSION-001, ROUTER-001 | PRG pattern, rate limiting, validation |
| **A05** Security Misconfiguration | ⭐⭐⭐⭐ | COOKIE-001, FILE-001, UPLOAD-001 | Secure flags, permissions, MIME checks |
| **A06** Vulnerable Components | ⭐⭐⭐ | README.md docs | PHP 8.1+ recommended |
| **A07** Identification/Auth Failures | ⭐⭐⭐⭐⭐ | AUTH-001, SESSION-001 | Password strength, rate limiting, hashing |
| **A08** Software/Data Integrity | ⭐⭐⭐⭐⭐ | UPLOAD-001, FILE-001 | MIME validation, file hashing, integrity checks |
| **A09** Logging Failures | ⭐⭐⭐ | All chapters | error_log present, structured logging planned |
| **A10** SSRF | ⭐⭐⭐ | FILE-001 | Path validation, directory traversal prevention |

**Score**: 44/50 (88%) - Eccellente

### Pattern Sicuri Documentati

✅ **XSS Prevention**: htmlspecialchars output encoding, CSP headers
✅ **SQL Injection**: Prepared statements con bind_param, no concatenation
✅ **Session Security**: regenerate_id, HttpOnly/Secure/SameSite flags, timeouts
✅ **Cookie Security**: Secure/HttpOnly/SameSite mitigation
✅ **File Upload**: MIME detection con finfo_file, whitelist, randomized names
✅ **Authentication**: Argon2id hashing, rate limiting, timing-safe comparison
✅ **CSRF Protection**: Token generation/verification, SameSite cookies
✅ **Input Validation**: Whitelist approach, type normalization
✅ **File System**: Directory traversal prevention, locking, permissions
✅ **Router Security**: Rate limiting middleware, parameter validation

### Vulnerabilità Mappate

- **XSS**: Script injection via GET/POST, stored XSS from DB
- **SQL Injection**: OR '1'='1 bypass, UNION attacks, DROP TABLE
- **Session Fixation**: Cookie reuse, missing regeneration
- **CSRF**: Cross-site form submission
- **Upload Attacks**: MIME spoofing, directory traversal, RCE
- **Brute-force**: Missing rate limiting on auth endpoints
- **Timing Attacks**: Username enumeration via response time

### Risorse

- **Analisi**: `/home/user/Appunti/PHP_COVERAGE_ANALYSIS.md`
- **Descrittori**: `/home/user/Appunti/PHP_DESCRIPTORS_REPORT.json`
- **Esempi**: `/home/user/Appunti/PHP/esempi/` (15+ file)
- **Capitoli**: `/home/user/Appunti/PHP/capitoli/` (7+ LaTeX files)

---

## Storico modifiche

- 2025-11-14: Aggiunta sezione "📊 Stato Descrittori e Sicurezza" con copertura OWASP completa e 15 descriptors
- 2025-11-14: [PHP-DOC-01] Sincronizzato PIANO_SVILUPPO.md con TODO.md e README.md; allineati task urgenti/medio/future e timeline (v0.36).
- 2025-11-13: Mirror struttura Java; aggiunti file di prefazione/appendici; quick reference; aggiornato `main.tex`.
- 2025-11-12: Consolidamento esempi sessioni/upload; pulizia documentazione.
- 2025-11-10: Setup base LaTeX; primi capitoli ed esempi.
