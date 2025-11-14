<?php
// Nota tecnica: rimosso strict_types per compatibilità degli esempi.

/**
 * Script di elaborazione form per studenti - Versione didattica
 * 
 * FUNZIONE E SCOPO:
 * Questo script riceve e valida un'email da un form HTML, dimostrando
 * le tecniche fondamentali di validazione input in PHP.
 * 
 * SPIEGAZIONE FUNZIONI UTILIZZATE:
 * 
 * Validazione manuale via superglobali:
 *   - Recupera da $_POST
 *   - Normalizza e verifica formato con regex
 * 
 * htmlspecialchars() - Funzione che converte caratteri speciali in entità HTML
 *   Previene attacchi XSS (Cross-Site Scripting) escapando caratteri pericolosi
 *   ENT_QUOTES: flag che converte sia apici singoli che doppi
 *   ENT_SUBSTITUTE: sostituisce caratteri non validi invece di eliminarli
 *   'UTF-8': specifica la codifica caratteri
 */

// Recupera e valida l'email dal form
$email = $_POST['email'] ?? null;
if (is_string($email)) {
    $email = trim($email);
}
// Verifica formato e presenza con regex semplice
if ($email === null || $email === '' || !preg_match('/^[^@\s]+@[^@\s]+\.[^@\s]+$/', $email)) {
    exit('Email non valida: assicurati di inserire un indirizzo email valido');
}

// Output sicuro: mostra l'email ricevuta dopo averla sanitizzata
// Nota: in contesti reali, qui si potrebbe salvare in database o inviare per email
echo 'Email ricevuta e validata: ' . htmlspecialchars($email, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
