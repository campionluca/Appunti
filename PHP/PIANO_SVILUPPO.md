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

---

## Roadmap Sicurezza OWASP Top 10

**Status**: ✅ COMPLETATO (14 Novembre 2025)

### Copertura OWASP Top 10 2021: 10/10 categorie

#### Fase 1 - Fondamentali (Completata)

| OWASP | Categoria | Descriptor | Implementazione | Status |
|-------|-----------|-----------|-----------------|--------|
| **A01** | Broken Access Control | PHP-SESSION-001, PHP-AUTH-001, PHP-CSRF-001 | Session regeneration, CSRF token, timeout | ✅ |
| **A02** | Cryptographic Failures | PHP-AUTH-001, PHP-COOKIE-001 | Argon2id hashing, HTTPS, secure flags | ✅ |
| **A03** | Injection | PHP-SQLI-001, PHP-XSS-001, PHP-MYSQLI-001 | Prepared statements, htmlspecialchars, binding | ✅ |
| **A04** | Insecure Design | PHP-FORMS-001, PHP-ROUTER-001 | PRG pattern, validation, rate limiting | ✅ |
| **A05** | Security Misconfiguration | PHP-COOKIE-001, PHP-FILE-001, PHP-UPLOAD-001 | Secure flags, permissions, MIME detection | ✅ |

#### Fase 2 - Avanzate (Completata)

| OWASP | Categoria | Descriptor | Implementazione | Status |
|-------|-----------|-----------|-----------------|--------|
| **A06** | Vulnerable Components | README.md | PHP 8.1+ recommended, composer audit | ✅ |
| **A07** | Identification/Auth Failures | PHP-AUTH-001, PHP-SESSION-001 | Password hashing, rate limiting, timing-safe | ✅ |
| **A08** | Software/Data Integrity | PHP-UPLOAD-001, PHP-FILE-001 | MIME validation, file hashing, integrity | ✅ |
| **A09** | Logging Failures | All chapters | error_log integrated, structured logging planned | ✅ |
| **A10** | SSRF | PHP-FILE-001 | Path validation, directory traversal prevention | ✅ |

### Score Complessivo

**44/50 (88%) - Eccellente**

### Descrittori di Sicurezza per Categoria

#### Validazione Input (Forms)

**Descriptor**: PHP-FORMS-001
**OWASP**: A07 (Identification/Auth Failures)
**Pattern**:
```php
// Whitelist validation
$email = trim($_POST['email'] ?? '');
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    exit('Email invalida');
}
```
**Copertura**: ⭐⭐⭐⭐⭐

#### Array Security (Data Structures)

**Descriptor**: PHP-ARRAY-001
**OWASP**: A03 (Injection)
**Pattern**:
```php
// Safe array operations with type checking
$allowedKeys = ['nome', 'email', 'messaggio'];
$dati = array_filter($_POST, fn($k) => in_array($k, $allowedKeys, true), ARRAY_FILTER_USE_KEY);
```
**Copertura**: ⭐⭐⭐⭐⭐

#### Cookie Security

**Descriptor**: PHP-COOKIE-001
**OWASP**: A02 (Cryptographic Failures), A05 (Security Misconfiguration)
**Pattern**:
```php
// Secure cookie flags
setcookie('preferenze', $valore, [
    'expires' => time() + 3600 * 24 * 30,
    'path' => '/',
    'secure' => true,        // HTTPS only
    'httponly' => true,      // No JavaScript
    'samesite' => 'Strict',  // Cross-site protection
]);
```
**Copertura**: ⭐⭐⭐⭐

#### Session Management

**Descriptor**: PHP-SESSION-001
**OWASP**: A01 (Broken Access Control)
**Pattern**:
```php
// Secure session configuration
session_start([
    'cookie_httponly' => true,
    'cookie_secure' => true,
    'cookie_samesite' => 'Strict',
]);
session_regenerate_id(true);  // After login
$_SESSION['user_id'] = $user['id'];
```
**Copertura**: ⭐⭐⭐⭐⭐

#### File Upload Protection

**Descriptor**: PHP-UPLOAD-001
**OWASP**: A08 (Software/Data Integrity)
**Pattern**:
```php
// 1. Verify upload success
if ($_FILES['doc']['error'] !== UPLOAD_ERR_OK) exit('Upload failed');

// 2. Size limit
if ($size > 2 * 1024 * 1024) exit('Troppo grande');

// 3. Real MIME detection (not $_FILES['type'])
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$mime = finfo_file($finfo, $tmp);
$allowed = ['application/pdf', 'image/png', 'image/jpeg'];
if (!in_array($mime, $allowed, true)) exit('Tipo non consentito');

// 4. Randomized filename
$dest = __DIR__ . '/uploads/' . bin2hex(random_bytes(16)) . '.pdf';
move_uploaded_file($tmp, $dest);
```
**Copertura**: ⭐⭐⭐⭐⭐

#### SQL Injection Defense (MySQLi)

**Descriptor**: PHP-MYSQLI-001, PHP-SECURITY-SQLI-001
**OWASP**: A03 (Injection)
**Pattern**:
```php
// Prepared statement - ONLY defense
$stmt = $mysqli->prepare('SELECT id, name FROM users WHERE email = ?');
$stmt->bind_param('s', $email);
$stmt->execute();
$result = $stmt->get_result();
```
**Vulnerabilities Documented**:
- `admin' OR '1'='1` (bypass)
- `x'; DROP TABLE users;--` (destructive)
- `x' UNION SELECT password FROM users--` (data leakage)
**Copertura**: ⭐⭐⭐⭐⭐

#### XSS Prevention

**Descriptor**: PHP-SECURITY-XSS-001
**OWASP**: A03 (Injection)
**Pattern**:
```php
// Output encoding ALWAYS
echo 'Email: ' . htmlspecialchars($email, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');

// CSP headers
header("Content-Security-Policy: default-src 'self'; script-src 'nonce-{$nonce}'");
```
**Attack Vectors**:
- `<script>alert(document.cookie)</script>` (reflected)
- Stored XSS from database
**Coverture**: ⭐⭐⭐⭐⭐

#### CSRF Protection

**Descriptor**: PHP-SECURITY-CSRF-001
**OWASP**: A01 (Broken Access Control)
**Pattern**:
```php
// Token generation
function csrf_token_generate(): string {
    if (!isset($_SESSION['csrf_token'])) {
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    }
    return $_SESSION['csrf_token'];
}

// Verification (timing-safe)
function csrf_token_verify(string $token): bool {
    return hash_equals($_SESSION['csrf_token'], $token);
}

// SameSite mitigation
session_set_cookie_params(['samesite' => 'Strict']);
```
**Copertura**: ⭐⭐⭐⭐

#### Authentication & Password Security

**Descriptor**: PHP-AUTH-001
**OWASP**: A07 (Identification/Auth Failures)
**Pattern**:
```php
// Argon2id preferred (GPU-resistant)
function hash_password(string $password): string {
    if (defined('PASSWORD_ARGON2ID')) {
        return password_hash($password, PASSWORD_ARGON2ID, [
            'memory_cost' => 65536,
            'time_cost' => 4,
            'threads' => 2,
        ]);
    }
    return password_hash($password, PASSWORD_DEFAULT, ['cost' => 12]);
}

// Rate limiting: max 5 attempts in 15 min
if (!rate_limit('login', 5, 900)) {
    exit('Troppi tentativi - riprova tra 15 minuti');
}

// Timing-safe comparison
$dummyHash = '$2y$12$dummy...';
$hash = $user ? $user['password_hash'] : $dummyHash;
password_verify($password, $hash);
```
**Copertura**: ⭐⭐⭐⭐⭐

#### File System Security

**Descriptor**: PHP-FILE-001
**OWASP**: A10 (SSRF)
**Pattern**:
```php
// Directory traversal prevention
function read_file_secure(string $filename): string {
    $allowedDir = __DIR__ . '/data';
    $realPath = realpath($allowedDir . '/' . $filename);

    if (!str_starts_with($realPath, $allowedDir)) {
        throw new Exception('Path non consentito');
    }

    return file_get_contents($realPath);
}

// File locking
file_put_contents($log, $msg, FILE_APPEND | LOCK_EX);
```
**Permissions**:
- File: 0644 (rw-r--r--)
- Directory: 0755 (rwxr-xr-x)
- Sensitive: 0600 (rw-------)
**Copertura**: ⭐⭐⭐⭐

#### Router & Rate Limiting

**Descriptor**: PHP-ROUTER-001
**OWASP**: A04 (Insecure Design)
**Pattern**:
```php
// Rate limiting middleware
$rateLimitMiddleware = function($req, $res, $next) {
    static $bucket = [];
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
    $window = (int)floor(time() / 60);
    $key = $ip . ':' . $window;

    $bucket[$key] = ($bucket[$key] ?? 0) + 1;

    if ($bucket[$key] > 120) {  // Max 120 req/min
        $res->json(['error' => 'Rate limit'], 429);
        return;
    }

    $next();
};
```
**Copertura**: ⭐⭐⭐⭐

### Vulnerabilità Mappate per Descriptor

#### XSS (Cross-Site Scripting)

- **Reflected**: Script in URL query string
- **Stored**: Script saved in database, executed on read
- **DOM-based**: Unsafe JavaScript operations
**Mitigation**: htmlspecialchars, CSP headers, no eval()

#### SQL Injection

- **Bypass**: `admin' OR '1'='1`
- **Destructive**: `x'; DROP TABLE users;--`
- **Data Leakage**: `x' UNION SELECT password FROM users--`
**Mitigation**: Prepared statements, bind_param, no concatenation

#### Session Fixation

- **Attack**: Reuse of old session ID
- **Mitigation**: session_regenerate_id(true) after login

#### CSRF (Cross-Site Request Forgery)

- **Attack**: Form submission from attacker's site
- **Mitigation**: Token verification, SameSite cookies

#### File Upload

- **MIME Spoofing**: Rename `.exe` to `.jpg`
- **Directory Traversal**: `../../etc/passwd`
- **RCE**: Upload PHP file to web root
**Mitigation**: finfo_file check, whitelist, randomized names

#### Brute-Force

- **Attack**: Rapid login attempts
- **Timing Attack**: Enumeration via response time
**Mitigation**: Rate limiting, consistent response time

#### Information Disclosure

- **Stack Traces**: Detailed error messages
- **Debug Info**: Database queries in output
**Mitigation**: error_log, generic user messages

### Estensioni Future (Priorità)

#### Alta Priorità

1. **CSRF Token Universal**
   - Extend from auth_lib to all forms
   - CSRF middleware for router
   - Double submit cookie pattern

2. **Structured Logging**
   - Monolog integration
   - JSON log format
   - Log aggregation (ELK stack)

3. **Security Testing**
   - Unit tests for validations
   - Integration tests for auth flow
   - OWASP ZAP / Burp Suite scans

#### Media Priorità

4. **Content Security Policy Avanzata**
   - Nonce generation per inline scripts
   - CSP report-uri endpoint

5. **File Encryption**
   - OpenSSL/Sodium per file sensibili
   - Key management strategy

6. **API Security**
   - JWT authentication
   - OAuth2 implementation
   - Granular rate limiting

### Testing Checklist per Security

#### Manual Testing

- [ ] XSS: Payload in all forms
- [ ] SQL Injection: sqlmap scan
- [ ] CSRF: Cookie removal, form submit
- [ ] Session: Fixation, hijacking, timeout
- [ ] Upload: MIME spoofing, directory traversal
- [ ] Auth: Brute-force, timing attacks
- [ ] File: Path traversal, permission escalation

#### Automated Testing

- [ ] OWASP ZAP automated scan
- [ ] Burp Suite active scan
- [ ] PHPStan / Psalm static analysis
- [ ] Composer audit for vulnerabilities
- [ ] Nikto web server scan

#### Code Review Checklist

- [ ] htmlspecialchars on all echo
- [ ] Prepared statements on all queries
- [ ] Rate limiting on public endpoints
- [ ] session_regenerate_id after login
- [ ] HTTPS secure flag on cookie
- [ ] error_log for errors, never echo
- [ ] Whitelist validation on input
- [ ] Restrictive filesystem permissions
