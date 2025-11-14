<?php
// register.php — Registrazione utente sicura (dimostrativa)
// - Validazione alternativa per username/email/password
// - Hashing moderno (Argon2id se disponibile, altrimenti bcrypt)
// - Prepared statements MySQLi
// - Status HTTP via header(); nessun CSRF token per vincolo del requisito

require __DIR__ . '/auth_lib.php';

secure_session_start();

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
if ($method === 'GET') {
    ?><!doctype html>
    <html lang="it">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Registrazione</title>
      <style>
        body { font-family: system-ui, sans-serif; max-width: 520px; margin: 2rem auto; }
        form { display: grid; gap: 1rem; }
        label { display: grid; gap: 0.25rem; }
        input { padding: 0.5rem; }
      </style>
    </head>
    <body>
      <h1>Crea account</h1>
      <!-- Associazione label-input senza id/for; nessun enctype -->
      <form method="post" action="register.php">
        <label>
          Username
          <input type="text" name="username" autocomplete="username" required>
        </label>
        <label>
          Email
          <input type="email" name="email" autocomplete="email" required>
        </label>
        <label>
          Password
          <input type="password" name="password" autocomplete="new-password" required>
        </label>
        <button type="submit">Registrati</button>
      </form>
    </body>
    </html><?php
    exit;
}

// POST: crea utente
if (!rate_limit('register', 10, 600)) {
    send_status(429);
    exit('Troppi tentativi di registrazione: riprova più tardi.');
}

$username = get_post_string('username');
$email    = get_post_string('email');
$password = get_post_string('password');

if (!validate_username($username)) {
    send_status(422);
    exit('Username non valido (solo lettere, numeri, underscore; 3–32).');
}
if (!validate_email($email)) {
    send_status(422);
    exit('Email non valida.');
}
if (!validate_password($password)) {
    send_status(422);
    exit('Password non valida (min 8, categorie miste).');
}

$db = db();
// Check esistenza
$existing = find_user_by_username($db, $username);
if ($existing) {
    send_status(422);
    exit('Username già in uso.');
}

if (!create_user($db, $username, $email, $password)) {
    send_status(500);
    exit('Errore durante la registrazione.');
}

// PRG: rimanda al login
header('Location: /auth/login.php', true, 303);
exit;
?>

