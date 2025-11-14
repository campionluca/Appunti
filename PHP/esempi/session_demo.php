<?php
// Nota tecnica: rimosso strict_types per compatibilità degli esempi.

session_start([
    'cookie_httponly' => true,
    'cookie_secure' => false, // metti true su HTTPS
    'cookie_samesite' => 'Lax',
]);

// Prevenzione session fixation: inizializza e rigenera ID alla prima richiesta
if (!isset($_SESSION['initialized'])) {
    session_regenerate_id(true);
    $_SESSION['initialized'] = true;
}

// Timeout inattività (es. 20 minuti)
$timeoutSeconds = 20 * 60;
$now = time();
if (isset($_SESSION['last_activity']) && ($now - (int)$_SESSION['last_activity'] > $timeoutSeconds)) {
    // scade la sessione per inattività
    session_unset();
    session_destroy();
    session_start([
        'cookie_httponly' => true,
        'cookie_secure' => false,
        'cookie_samesite' => 'Lax',
    ]);
    session_regenerate_id(true);
    $_SESSION['initialized'] = true;
}
$_SESSION['last_activity'] = $now;

if (!isset($_SESSION['counter'])) {
    $_SESSION['counter'] = 0;
}

$_SESSION['counter']++;
echo 'Visite nella sessione: ' . (int)$_SESSION['counter'];
