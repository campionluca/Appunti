<?php
// auth_lib.php — Libreria di autenticazione sicura senza CSRF, http_response_code(), filter_input(), né id-for
// Obiettivi:
// - Sessioni sicure (HttpOnly, Secure, SameSite=Strict), rigenerazione ID
// - Validazione input alternativa (regex, filter_var su variabili già lette)
// - Gestione delle risposte HTTP via header() senza http_response_code()
// - Accesso al DB tramite MySQLi con prepared statements e utf8mb4
// - Rate limiting basilare per tentativi di login

// ================================
// Configurazione database
// ================================
// Nota: sostituire con credenziali reali; in produzione usare variabili d’ambiente.
const DB_HOST = 'localhost';
const DB_USER = 'user';
const DB_PASS = 'pass';
const DB_NAME = 'appdb';

// ================================
// Gestione HTTP status senza http_response_code()
// ================================
function send_status(int $code): void {
    // Mappa minimale di codici e testi standard
    static $texts = [
        200 => 'OK',
        303 => 'See Other',
        400 => 'Bad Request',
        401 => 'Unauthorized',
        403 => 'Forbidden',
        404 => 'Not Found',
        422 => 'Unprocessable Entity',
        429 => 'Too Many Requests',
        500 => 'Internal Server Error',
    ];
    $text = $texts[$code] ?? 'Unknown';
    // Imposta la linea di stato HTTP manualmente
    header(sprintf('HTTP/1.1 %d %s', $code, $text));
}

// ================================
// Sessioni sicure (senza token CSRF): mitigazioni con SameSite e HttpOnly
// ================================
function secure_session_start(): void {
    $isHttps = !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on';

    // Imposta parametri cookie della sessione in modo sicuro
    if (PHP_VERSION_ID >= 70300) {
        // PHP >= 7.3 supporta l’array con samesite
        session_set_cookie_params([
            'lifetime' => 0,
            'path' => '/',
            'domain' => '',
            'secure' => $isHttps,
            'httponly' => true,
            'samesite' => 'Strict', // mitigazione CSRF via cookie, senza token
        ]);
    } else {
        // Fallback: imposta ini; SameSite potrebbe non essere disponibile
        ini_set('session.cookie_lifetime', '0');
        ini_set('session.cookie_path', '/');
        ini_set('session.cookie_secure', $isHttps ? '1' : '0');
        ini_set('session.cookie_httponly', '1');
        // Nota: SameSite non garantito su versioni precedenti
    }
    ini_set('session.use_strict_mode', '1');

    session_start();
}

function regenerate_session(): void {
    // Rigenera l’ID per prevenire session fixation; true elimina l’ID precedente
    session_regenerate_id(true);
}

// ================================
// Rate limiting semplice su base sessione
// ================================
function rate_limit(string $key, int $maxAttempts, int $windowSeconds): bool {
    $now = time();
    if (!isset($_SESSION['_rate'][$key])) {
        $_SESSION['_rate'][$key] = [];
    }
    // Pulisci tentativi oltre la finestra temporale (senza array_filter)
    $filtered = [];
    foreach ($_SESSION['_rate'][$key] as $t) {
        $tt = (int)$t;
        if (($now - $tt) <= $windowSeconds) {
            $filtered[] = $tt;
        }
    }
    $_SESSION['_rate'][$key] = $filtered;
    // Controlla numero tentativi
    if (count($_SESSION['_rate'][$key]) >= $maxAttempts) {
        return false; // limit hit
    }
    // Registra tentativo
    $_SESSION['_rate'][$key][] = $now;
    return true;
}

// ================================
// Validazione input alternativa (senza filter_input())
// ================================
function get_post_string(string $key): string {
    // Legge direttamente da $_POST, normalizza come stringa e trim
    $raw = $_POST[$key] ?? '';
    return trim(is_string($raw) ? $raw : '');
}

function validate_username(string $username): bool {
    // Solo lettere, numeri, underscore; lunghezza 3–32
    if ($username === '' || strlen($username) < 3 || strlen($username) > 32) {
        return false;
    }
    return (bool)preg_match('/^[A-Za-z0-9_]+$/', $username);
}

function validate_email(string $email): bool {
    // Usa filter_var sulla variabile già letta (alternativa a filter_input)
    return (bool)filter_var($email, FILTER_VALIDATE_EMAIL);
}

function validate_password(string $password): bool {
    // Minimo 8 caratteri, massimo 72 (limite bcrypt), richiede classi diverse
    $len = strlen($password);
    if ($len < 8 || $len > 72) return false;
    $hasLower = (bool)preg_match('/[a-z]/', $password);
    $hasUpper = (bool)preg_match('/[A-Z]/', $password);
    $hasDigit = (bool)preg_match('/\d/', $password);
    $hasOther = (bool)preg_match('/[^A-Za-z0-9]/', $password);
    // Richiedi almeno tre categorie per robustezza
    $categories = $hasLower + $hasUpper + $hasDigit + $hasOther;
    return $categories >= 3;
}

function esc_html(string $s): string {
    // Escaping sicuro per output HTML
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

// ================================
// Password hashing e verifica
// ================================
function hash_password(string $password): string {
    // Preferisci Argon2id se disponibile, altrimenti fallback a PASSWORD_DEFAULT
    if (defined('PASSWORD_ARGON2ID')) {
        return password_hash($password, PASSWORD_ARGON2ID);
    }
    // PASSWORD_DEFAULT è tipicamente bcrypt; imposta cost moderata
    return password_hash($password, PASSWORD_DEFAULT, ['cost' => 12]);
}

function verify_password(string $password, string $hash): bool {
    return password_verify($password, $hash);
}

// ================================
// Connessione DB e operazioni utente
// ================================
function db(): mysqli {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($mysqli->connect_errno) {
        // Non usare http_response_code; logga e invia 500
        error_log('DB connect error: ' . $mysqli->connect_error);
        send_status(500);
        exit('Database non disponibile');
    }
    // Charset utf8mb4 per sicurezza e correttezza
    $mysqli->set_charset('utf8mb4');
    return $mysqli;
}

function find_user_by_username(mysqli $db, string $username): ?array {
    $stmt = $db->prepare('SELECT id, username, password_hash FROM users WHERE username = ? LIMIT 1');
    if (!$stmt) { return null; }
    $stmt->bind_param('s', $username);
    $stmt->execute();
    $res = $stmt->get_result();
    $row = $res ? $res->fetch_assoc() : null;
    $stmt->close();
    return $row ?: null;
}

function create_user(mysqli $db, string $username, string $email, string $password): bool {
    $hash = hash_password($password);
    $stmt = $db->prepare('INSERT INTO users(username, email, password_hash) VALUES(?,?,?)');
    if (!$stmt) { return false; }
    $stmt->bind_param('sss', $username, $email, $hash);
    $ok = $stmt->execute();
    if (!$ok) {
        error_log('Create user error: ' . $stmt->error);
    }
    $stmt->close();
    return $ok;
}

// ================================
// Accessibilità dei label senza id-for
// ================================
// Suggerimento: incapsulare <input> all’interno di <label> per associare testo e campo
// Esempio:
// <label>Username <input type="text" name="username" autocomplete="username" required></label>
// <label>Password <input type="password" name="password" autocomplete="current-password" required></label>
// Questo mantiene l’associazione semantica clic-label → focus input senza usare id/for.

?>
