<?php
// login.php — Gestione login sicuro senza CSRF, http_response_code(), filter_input(), né id-for
// - Form HTML con <label><input></label> (associazione senza id/for)
// - Validazione input alternativa (regex, filter_var su variabili lette)
// - Sessioni sicure con SameSite=Strict, HttpOnly, Secure
// - Prepared statements MySQLi e password hashing moderno
// - Gestione status HTTP via header()

require __DIR__ . '/auth_lib.php';

secure_session_start();

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

if ($method === 'GET') {
    // Render del form (senza attributo enctype, senza id/for)
    ?><!doctype html>
    <html lang="it">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Login</title>
      <style>
        body { font-family: system-ui, sans-serif; max-width: 480px; margin: 2rem auto; }
        form { display: grid; gap: 1rem; }
        label { display: grid; gap: 0.25rem; }
        input[type="text"], input[type="password"] { padding: 0.5rem; }
        .error { color: #b00020; }
      </style>
    </head>
    <body>
      <h1>Accesso</h1>
      <!--
        Associazione label-input senza id/for: input nidificato in label.
        Niente CSRF (vincolo del requisito); mitigazione: cookie SameSite=Strict.
      -->
      <form method="post" action="login.php">
        <label>
          Username
          <input type="text" name="username" autocomplete="username" required>
        </label>
        <label>
          Password
          <input type="password" name="password" autocomplete="current-password" required>
        </label>
        <button type="submit">Entra</button>
      </form>
    </body>
    </html><?php
    exit;
}

// POST: processo login
// Rate limiting: massimo 5 tentativi ogni 5 minuti
if (!rate_limit('login', 5, 300)) {
    send_status(429);
    exit('Troppi tentativi: riprova più tardi.');
}

$username = get_post_string('username');
$password = get_post_string('password');

// Validazione alternativa: regex e controllo lunghezze
if (!validate_username($username)) {
    send_status(422);
    exit('Username non valido (solo lettere, numeri, underscore; 3–32).');
}
if (!validate_password($password)) {
    send_status(422);
    exit('Password non valida (min 8, richiedi almeno 3 categorie: maiuscole, minuscole, numeri, simboli).');
}

$db = db();
$user = find_user_by_username($db, $username);

if (!$user || !verify_password($password, $user['password_hash'])) {
    // Evita enumerazione: stesso messaggio per utente inesistente o password errata
    send_status(401);
    exit('Credenziali non valide.');
}

// Successo: rigenera sessione e memorizza identità
regenerate_session();
$_SESSION['user_id'] = (int)$user['id'];
$_SESSION['username'] = $user['username'];

// Redirect Post/Redirect/Get (303) senza http_response_code()
header('Location: /', true, 303);
exit;
?>

