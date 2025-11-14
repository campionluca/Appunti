# Appunti di Programmazione PHP

Corso pratico di PHP orientato allo sviluppo web moderno: form e input, cookie e sessioni, upload di file e interazione con database MySQL (mysqli), con contenuti strutturati in LaTeX e codice di esempio pronto all’uso.

---

## Descrizione del progetto

Questo progetto raccoglie appunti, esempi e esercizi per imparare PHP in modo progressivo. I capitoli sono pensati per essere consultati come guida pratica, con focus su:
- Gestione input e form HTML con validazioni server-side
- Cookie sicuri e gestione preferenze
- Sessioni robuste (rigenerazione ID, contatori, sicurezza)
- Upload di file con controlli su dimensione e MIME
- Accesso a database MySQL tramite `mysqli` con prepared statements

In aggiunta, la struttura del libro PHP rispecchia la gerarchia del corso Java:
- Prefazione e backmatter (Appendice Quick Reference, Bibliografia)
- Cartella `quick_reference/` con schede riassuntive
- Template per nuovi capitoli (`_template_capitolo.tex`)

Il materiale è organizzato in LaTeX (PDF compilabile) con inclusione diretta di snippet di codice dai file nella cartella `esempi/`.

---

## Requisiti di sistema e dipendenze

### Ambiente di sviluppo
- PHP: 8.1 o superiore (CLI e/o server web)
- Web server: Apache/Nginx con PHP-FPM oppure server integrato `php -S`
- Database: MySQL/MariaDB (per gli esempi `mysqli`)
- LaTeX: distribuzione completa (TeX Live/MiKTeX) per il PDF
- Editor: VS Code, PhpStorm o similari

### Dipendenze opzionali
- Composer (facoltativo, non richiesto dagli esempi di base)
- Estensioni PHP: `mysqli` abilitata per gli esempi DB
 - LaTeX: `tcolorbox`, `listingsutf8`, `microtype` presenti nel preambolo

---

## Installazione e configurazione

### Codice di esempio (server integrato)
Puoi usare il server integrato di PHP per eseguire gli esempi:

```powershell
cd PHP\esempi
php -S localhost:8005
```

Quindi apri in browser `http://localhost:8005/form.html`, `http://localhost:8005/processa.php`, `http://localhost:8005/session_demo.php`, `http://localhost:8005/upload.php`.

### Configurazione database
Aggiorna le credenziali in `esempi/mysqli_select.php` e `esempi/mysqli_insert.php`:

```php
$host = 'localhost';
$user = 'utente';
$pass = 'password';
$db   = 'nome_database';
```

Assicurati che la tabella di esempio esista e che l’utente abbia permessi di `SELECT`/`INSERT`.

### Compilazione del PDF (LaTeX)
Nel folder `PHP/`:

```powershell
xelatex main.tex
xelatex main.tex
xelatex main.tex
```

Oppure con `latexmk`:

```powershell
latexmk -xelatex -pdf main.tex
```

Il PDF risultante è `PHP/main.pdf`.

Quick Reference (documento separato):

```powershell
cd PHP\quick_reference
xelatex main.tex
```

---

## Guida all’utilizzo con esempi pratici

### Form e validazione
- File: `esempi/form.html` → pagina con form HTML
- File: `esempi/processa.php` → validazione server-side (email)

Come provare:
1. Avvia server integrato
2. Apri `form.html`
3. Invia il form e verifica i messaggi di validazione

### Cookie sicuri
- File: `esempi/router.php` (gestione preferenze) e cookie con flag `secure`, `httponly`, `samesite`
1. Imposta preferenze
2. Ricarica la pagina e verifica la persistenza

### Sessioni
- File: `esempi/session_demo.php`
1. Avvia server
2. Apri la pagina e verifica il contatore visite e la rigenerazione di session ID

### Upload file
- File: `esempi/upload.php`
1. Carica un file (limiti di dimensione e MIME)
2. Controlla l’esito e i messaggi di errore

### Database MySQL (mysqli)
- File: `esempi/mysqli_select.php`, `esempi/mysqli_insert.php`
1. Configura credenziali
2. Esegui query di `SELECT` e `INSERT` con prepared statements

---

## Struttura del progetto

```
PHP/
├── README.md                # Questo documento
├── PIANO_SVILUPPO.md        # Roadmap, changelog, testing
├── main.tex                 # File LaTeX principale
├── main.pdf                 # PDF compilato
├── capitoli/                # Capitoli LaTeX
│   ├── 00_prefazione.tex
│   ├── 01_Introduzione.tex
│   ├── 02_Form.tex
│   ├── 03_Array.tex
│   ├── 04_Cookie.tex
│   ├── 07_File_Testo.tex
│   ├── 08_Upload_File.tex
│   ├── 09_Sessioni.tex
│   ├── appendice_qr.tex
│   └── 99_bibliografia.tex
├── esempi/                  # Codice di esempio eseguibile
│   ├── form.html
│   ├── processa.php
│   ├── hello.php
│   ├── router.php
│   ├── session_demo.php
│   ├── upload.php
│   ├── mysqli_select.php
│   └── mysqli_insert.php
├── quick_reference/         # Schede riassuntive
│   └── main.tex
└── esercizi/                # Tracce di esercizi
```

---

## Licenza e contributi

### Licenza
Uso didattico. La licenza definitiva verrà definita (proposta: CC BY‑NC‑SA 4.0). In assenza di indicazioni, il materiale è utilizzabile per studio personale e in classe con attribuzione all’autore.

### Contributi
Sono benvenuti miglioramenti e correzioni:
- Apri una issue con descrizione chiara del problema
- Proponi una pull request con modifiche minime e ben motivate
- Mantieni coerenza stilistica (PSR‑12 per PHP, convenzioni LaTeX del progetto)

Consulta anche `PIANO_SVILUPPO.md` per allinearti con roadmap e procedure di testing.


Materiale strutturato per un libro completo su PHP. Include capitoli teorico-pratici, esempi, esercizi, quick reference, immagini e linee guida di qualità.

## Struttura del progetto

```
PHP/
├── capitoli/              # Capitoli del libro in formato Markdown
├── esempi/                # Esempi di codice completi (file .php)
├── esercizi/              # Tracce esercizi e soluzioni
├── immagini/              # Screenshot e diagrammi
└── README.md              # Descrizione generale e linee guida
```

## Indice capitoli

- 01 — Introduzione: `capitoli/01_Introduzione.md`
- 02 — Form HTML, GET/POST: `capitoli/02_Form.md`
- 03 — Array e strutture dati: `capitoli/03_Array.md`
- 04 — Cookie: `capitoli/04_Cookie.md`
- 05 — Server e Request: `capitoli/05_Server_e_Request.md`
- 06 — Passaggio parametri: `capitoli/06_Passaggio_Parametri.md`
- 07 — File di testo (I/O): `capitoli/07_File_Testo.md`
- 08 — Upload di file: `capitoli/08_Upload_File.md`
- 09 — Sessioni: `capitoli/09_Sessioni.md`
- 10 — Database (MySQLi): `capitoli/10_Database_MySQLi.md`
- 11 — Altri argomenti utili: `capitoli/11_Altri_Argomenti_Utili.md`
 
Nota: i capitoli stanno progressivamente migrando da `.md` a `.tex` per garantire un PDF integrato e uniforme. Vedi anche `manuale/` per il materiale discorsivo.

## Requisiti e configurazione ambiente

- PHP 8.1+ consigliato (funziona con 7.4+, ma alcuni esempi usano novità recenti)
- Server: Apache/Nginx oppure PHP built‑in (`php -S localhost:8000`)
- Database: MySQL/MariaDB (per capitolo MySQLi)
- Estensioni: `mysqli`, `mbstring`, `openssl`, `json`
- Debug: Xdebug (facoltativo), `error_reporting(E_ALL)` in sviluppo
- Composer (facoltativo) per dipendenze e autoload

### Esecuzione esempi
- Avvia un server locale nella cartella `PHP/esempi`:
  - `php -S localhost:8000 -t PHP/esempi`
- Apri nel browser:
  - `http://localhost:8000/hello.php`
  - `http://localhost:8000/form.html`
  - `http://localhost:8000/router.php?path=/saluto`
  - `http://localhost:8000/session_demo.php`
  - Upload: crea un form che punti a `upload.php` e invia `documento`

## Linee guida di qualità

- PSR‑12 per stile del codice; vietato `declare(strict_types=1)` in tutto il codice
- Validazione input con `filter_input` e escape output con `htmlspecialchars`
- Prepared statements per query SQL, mai concatenare input dell’utente
- Protezioni per sicurezza: XSS, SQL injection, session fixation
- Gestione errori e logging: livelli coerenti, niente errori esposti in produzione
- Uso di `move_uploaded_file`, verifica MIME/estensione e limiti dimensione per upload

### Convenzione operatori di confronto

- Usa `==` e `!=` come standard per confronti di valore.
- Riserva `===` e `!==` solo quando è necessario verificare sia tipo che valore:
  - sicurezza critica o hashing/comparazioni temporally-safe
  - trattamento specifico di valori ambigui (`0`, `false`, `null`)
  - protocolli/flag dove il tipo è parte del contratto
- Prima di ogni confronto, assicurati che i tipi siano compatibili (normalizzazione a stringhe/numeri dove utile).

#### Registro eccezioni operatori stretti (===/!==)

- `PHP/esempi/pdf_demo.php`: controllo dell’esito di `file_put_contents`
  - Motivo tecnico: l’API restituisce `false` su errore e un intero (anche `0`) su successo; serve `=== false` per distinguere fallimento da 0 bytes.
- In tutti gli altri file: i confronti sono stati allineati a `==`/`!=` con tipi normalizzati (stringhe per path e metodi HTTP).
  - Qualsiasi uso futuro di `===`/`!==` deve essere accompagnato da commento esplicativo prima della riga.

## Esercizi

Ogni capitolo ha esercizi dedicati in `esercizi/`:
- Introduzione: `esercizi/01_Introduzione.md`
- Form: `esercizi/02_Form.md`
- Array: `esercizi/03_Array.md`
- Cookie: `esercizi/04_Cookie.md`
- Server/Request: `esercizi/05_Server_e_Request.md`
- Passaggio parametri: `esercizi/06_Passaggio_Parametri.md`
- File di testo: `esercizi/07_File_Testo.md`
- Upload: `esercizi/08_Upload_File.md`
- Sessioni: `esercizi/09_Sessioni.md`
- Database (MySQLi): `esercizi/10_Database_MySQLi.md`
- Argomenti utili: `esercizi/11_Altri_Argomenti_Utili.md`

## 🔒 Descrittori Sicurezza Web

**Status**: ✅ COMPLETATO (14 Novembre 2025)

Il corso PHP integra una copertura **eccellente della sicurezza web** con 15 security descriptors allineati a **OWASP Top 10 2021**:

### Copertura OWASP: 10/10 categorie (88% score)

| OWASP Category | Livello | Pattern Implementato |
|---|---|---|
| **A01** Broken Access Control | ⭐⭐⭐⭐⭐ | Session regeneration, CSRF token, timeout |
| **A02** Cryptographic Failures | ⭐⭐⭐⭐⭐ | Argon2id hashing, HTTPS, secure cookies |
| **A03** Injection (XSS, SQLi) | ⭐⭐⭐⭐⭐ | Prepared statements, htmlspecialchars |
| **A04** Insecure Design | ⭐⭐⭐⭐ | PRG pattern, validation, rate limiting |
| **A05** Security Misconfiguration | ⭐⭐⭐⭐ | Secure flags, permissions, MIME detection |
| **A06** Vulnerable Components | ⭐⭐⭐ | PHP 8.1+ recommended, dependency audit |
| **A07** Identification/Auth Failures | ⭐⭐⭐⭐⭐ | Password hashing, rate limiting, timing-safe |
| **A08** Software/Data Integrity | ⭐⭐⭐⭐⭐ | MIME validation, file hashing, integrity |
| **A09** Logging Failures | ⭐⭐⭐ | error_log integrated, structured logging planned |
| **A10** SSRF | ⭐⭐⭐ | Path validation, directory traversal prevention |

### 15 Security Descriptors

1. **PHP-FORMS-001** — Form validation & sanitization (OWASP A07)
2. **PHP-ARRAY-001** — Array manipulation security (OWASP A03)
3. **PHP-COOKIE-001** — Secure cookie flags & validation (OWASP A02, A05)
4. **PHP-SESSION-001** — Session regeneration & timeouts (OWASP A01)
5. **PHP-UPLOAD-001** — File upload MIME & size checks (OWASP A08)
6. **PHP-MYSQLI-001** — Prepared statements & binding (OWASP A03)
7. **PHP-SECURITY-XSS-001** — Output encoding & CSP (OWASP A03)
8. **PHP-SECURITY-SQLI-001** — SQL injection defense (OWASP A03)
9. **PHP-SECURITY-CSRF-001** — CSRF token & SameSite (OWASP A01)
10. **PHP-AUTH-001** — Password hashing & rate limiting (OWASP A07)
11. **PHP-FILE-001** — Directory traversal prevention (OWASP A10)
12. **PHP-ROUTER-001** — Rate limiting middleware (OWASP A04)
13. **PHP-BASICS-001** — Input validation patterns (OWASP A04)

**+ 2 descriptors** in appendici di supporto.

### Pattern Unsafe vs Safe (Documentati)

Tutti gli esempi seguono il template:

```php
// ============================================
// VULNERABILE - Problema di sicurezza
// ============================================
$name = $_GET['name'];
echo "<h1>$name</h1>";  // ❌ XSS risk
// Attack: ?name=<script>alert(1)</script>

// ============================================
// SICURO - Mitigazione
// ============================================
$name = htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8');
echo "<h1>$name</h1>";  // ✅ Encoded
```

### Vulnerabilità Mappate

- **XSS**: Script injection via GET/POST, stored XSS from DB
- **SQL Injection**: OR '1'='1 bypass, UNION SELECT, DROP TABLE
- **Session Fixation**: Reuse of old session ID
- **CSRF**: Cross-site form submission without token
- **Upload Attacks**: MIME spoofing, directory traversal, RCE
- **Brute-force**: Timing attacks on auth endpoints
- **Information Disclosure**: Detailed error messages in production

### Best Practices Implementate

✅ **XSS Prevention**
   - `htmlspecialchars()` con `ENT_QUOTES | ENT_SUBSTITUTE`
   - Content Security Policy headers
   - No eval() o dynamic script execution

✅ **SQL Injection Defense**
   - Prepared statements con `bind_param()`
   - No string concatenation in queries
   - Least privilege DB user

✅ **Session Security**
   - `session_regenerate_id(true)` dopo login
   - Cookie `HttpOnly`, `Secure`, `SameSite=Strict`
   - Timeout inattività (20 minuti default)

✅ **File Upload Protection**
   - MIME detection con `finfo_file()` (non `$_FILES['type']`)
   - Whitelist tipi permessi
   - Randomized filenames per prevenire directory traversal
   - Size limits (2MB default)

✅ **Authentication**
   - Argon2id password hashing (fallback bcrypt)
   - Rate limiting: 5 tentativi in 15 minuti
   - Timing-safe comparison (`hash_equals()`)
   - Password strength: 8-72 chars, 3 classi

✅ **Cookie Security**
   - `Secure`: HTTPS only
   - `HttpOnly`: No JavaScript access
   - `SameSite=Strict`: Cross-site protection

### Risorse e Referenze

- **Analisi completa**: `/home/user/Appunti/PHP_COVERAGE_ANALYSIS.md`
- **Descrittori**: `/home/user/Appunti/PHP_DESCRIPTORS_REPORT.json`
- **Esempi pratici**: `/home/user/Appunti/PHP/esempi/` (15+ file)
- **OWASP Top 10**: https://owasp.org/Top10/
- **PHP Security Handbook**: https://www.php.net/manual/it/security.php

---

## Sicurezza (panoramica)

- XSS: sanificare sempre l'output HTML (`htmlspecialchars`, Content Security Policy)
- SQL Injection: `mysqli`/`PDO` con prepared statements e binding
- Sessioni: `session_regenerate_id(true)`, cookie `HttpOnly`, `Secure`, `SameSite=Lax`

## Performance

- Abilitare OPcache in produzione
- Ridurre I/O non necessario; caching di risultati frequenti
- Usare `array_*` funzionali (`array_map`, `array_filter`) per operazioni in memoria

## Integrazione con HTML/CSS/JS

- Templating semplice con PHP o motori dedicati
- Separare la logica (controller) dalla presentazione (view)
- Validazioni lato client opzionali, ma mai sostitutive di quelle lato server

## Versionamento (Git)

- Branching semplice: `main` stabile, `feature/*` per nuovi argomenti
- Commit piccoli e descrittivi; includere esempi e immagini associati
- Aggiornare questo README quando si aggiungono capitoli o esercizi

## Glossario (selezione)

- XSS: Cross‑Site Scripting, iniezione di script nell’output HTML
- OPcache: cache bytecode per migliorare performance di PHP
- Prepared statement: query SQL precompilate con parametri (sicurezza/performance)

## Riferimenti

- Manuale PHP: https://www.php.net/manual/it/
- Sicurezza OWASP: https://owasp.org/
- PSR‑12: https://www.php-fig.org/psr/psr-12/
## Manuale discorsivo

Il repository include un manuale di PHP scritto in prosa, con esempi integrati e riferimenti incrociati tra capitoli. Il manuale evita elenchi puntati non necessari e adotta un tono tecnico ma accessibile. I primi capitoli si trovano nella cartella `PHP/manuale/` e coprono l’introduzione al linguaggio e al modello di esecuzione, la sintassi e i tipi, l’organizzazione del codice con funzioni e namespace, e la gestione delle richieste HTTP con form e risposte. I capitoli successivi approfondiscono sessioni e cookie, file e upload, database con PDO, gestione degli errori, sicurezza applicativa e performance. Ogni sezione rimanda alle correlate per favorire una comprensione organica.
---

## Storico modifiche

- 2025-11-13 — Struttura PHP allineata alla gerarchia del libro Java: prefazione, appendice QR, bibliografia, quick reference; aggiornati include in `main.tex`.
- 2025-11-12 — Consolidamento esempi sessioni/upload; aggiornamento qualità documentazione.
- 2025-11-10 — Setup base LaTeX e primi capitoli.
