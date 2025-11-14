<?php
// io.php — Operazioni di I/O in stile C su file
// Usa esclusivamente fopen/fread/fwrite/fclose, modalità binaria, gestione errori senza eccezioni

function io_open($path, $mode)
{
    // Apertura file in modalità specificata; ritorna array risultato
    $fp = @fopen($path, $mode);
    if ($fp === false) {
        return [ 'ok' => false, 'err' => 'open_failed', 'msg' => 'Impossibile aprire: ' . $path ];
    }
    return [ 'ok' => true, 'fp' => $fp ];
}

function io_close($fp)
{
    // Chiusura sicura del file pointer
    if (is_resource($fp)) { @fclose($fp); return [ 'ok' => true ]; }
    return [ 'ok' => false, 'err' => 'invalid_fp' ];
}

function io_read_block($fp, $size)
{
    // Lettura blocco binario; ritorna stringa o errore
    if (!is_resource($fp)) { return [ 'ok' => false, 'err' => 'invalid_fp' ]; }
    $data = @fread($fp, $size);
    if ($data === false) { return [ 'ok' => false, 'err' => 'read_failed' ]; }
    return [ 'ok' => true, 'data' => $data ];
}

function io_write_block($fp, $data)
{
    // Scrittura blocco; ritorna numero di byte scritti
    if (!is_resource($fp)) { return [ 'ok' => false, 'err' => 'invalid_fp' ]; }
    $n = @fwrite($fp, $data);
    if ($n === false) { return [ 'ok' => false, 'err' => 'write_failed' ]; }
    return [ 'ok' => true, 'written' => $n ];
}

function io_seek($fp, $offset, $whence)
{
    // Spostamento del puntatore
    if (!is_resource($fp)) { return [ 'ok' => false, 'err' => 'invalid_fp' ]; }
    $r = @fseek($fp, $offset, $whence);
    if ($r !== 0) { return [ 'ok' => false, 'err' => 'seek_failed' ]; }
    return [ 'ok' => true ];
}

function io_tell($fp)
{
    // Posizione corrente del puntatore
    if (!is_resource($fp)) { return [ 'ok' => false, 'err' => 'invalid_fp' ]; }
    $pos = @ftell($fp);
    if ($pos === false) { return [ 'ok' => false, 'err' => 'tell_failed' ]; }
    return [ 'ok' => true, 'pos' => $pos ];
}

?>

