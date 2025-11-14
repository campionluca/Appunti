<?php
// logout.php — Termine sicuro della sessione
// - Sessione avviata con parametri sicuri
// - Rimozione variabili e distruzione sessione
// - Status HTTP via header(), opzionale redirect

require __DIR__ . '/auth_lib.php';

secure_session_start();

// Cancella dati sessione
$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $params = session_get_cookie_params();
    // Invalida il cookie
    setcookie(session_name(), '', time() - 3600, $params['path'], $params['domain'], $params['secure'], $params['httponly']);
}
session_destroy();

// Opzione: redirect alla home con 303 PRG
header('Location: /', true, 303);
exit;
?>

