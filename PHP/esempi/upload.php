<?php
// Nota tecnica: rimosso strict_types per compatibilità degli esempi.

/**
 * Script di upload file per studenti - Versione didattica
 * 
 * FUNZIONE E SCOPO:
 * Questo script gestisce l'upload sicuro di file dimostrando le tecniche
 * fondamentali di validazione e sicurezza per l'upload file in PHP.
 * 
 * SPIEGAZIONE FUNZIONI UTILIZZATE:
 * 
 * $_FILES - Superglobale PHP che contiene informazioni sui file caricati
 *   - 'tmp_name': percorso temporaneo del file sul server
 *   - 'size': dimensione del file in bytes
 *   - 'error': codice errore dell'operazione di upload
 * 
 * UPLOAD_ERR_OK - Costante che indica upload completato con successo (valore 0)
 * finfo_open() - Funzione che apre una risorsa per l'analisi del tipo MIME
 * FILEINFO_MIME_TYPE - Costante che specifica di restituire solo il tipo MIME
 * finfo_file() - Analizza un file e restituisce informazioni sul tipo
 * move_uploaded_file() - Sposta il file caricato in una posizione permanente
 */

// Avvio sessione (compatibilità con altri esempi; non usato per CSRF)
session_start();

if (!isset($_FILES['documento']) || $_FILES['documento']['error'] !== UPLOAD_ERR_OK) {
    header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 400 Bad Request', true, 400);
    exit('Upload non valido');
}

$tmp = $_FILES['documento']['tmp_name'];
$size = (int)$_FILES['documento']['size'];
if ($size > 2 * 1024 * 1024) {
    exit('File troppo grande');
}

$finfo = finfo_open(FILEINFO_MIME_TYPE);
$mime = finfo_file($finfo, $tmp) ?: 'application/octet-stream';
finfo_close($finfo);

$allowed = ['application/pdf', 'image/png', 'image/jpeg'];
if (!in_array($mime, $allowed, true)) {
    exit('Tipo di file non consentito');
}

$destDir = __DIR__ . '/uploads';
@mkdir($destDir);
$dest = $destDir . '/' . bin2hex(random_bytes(8)) . '.bin';

if (!move_uploaded_file($tmp, $dest)) {
    exit('Spostamento fallito');
}

echo 'Upload riuscito';
