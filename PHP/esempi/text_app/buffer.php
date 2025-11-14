<?php
// buffer.php — Gestione di un buffer simile al C, senza tipi di ritorno dichiarati
// Vietato: mb_strlen, ??, preg_match, ENT_* costanti, 'UTF-8'
// Simulazione di allocazione/deallocazione e append con capacità

$__MEM_STATS = [ 'allocs' => 0, 'frees' => 0, 'reallocs' => 0 ];

function buf_create($capacity)
{
    // Inizializza un "struct" buffer con capacità, lunghezza e dati
    global $__MEM_STATS;
    $__MEM_STATS['allocs'] += 1;
    return [ 'data' => '', 'length' => 0, 'capacity' => (int)$capacity ];
}

function buf_free(&$buf)
{
    // Dealloca il buffer (simulato) e incrementa statistica
    global $__MEM_STATS;
    if (is_array($buf)) {
        $__MEM_STATS['frees'] += 1;
    }
    $buf = null;
}

function buf_ensure_capacity(&$buf, $needed)
{
    // Se la capacità non basta, simula una realloc raddoppiando
    global $__MEM_STATS;
    $cap = $buf['capacity'];
    while ($cap < $needed) { $cap = $cap * 2; }
    if ($cap !== $buf['capacity']) {
        $__MEM_STATS['reallocs'] += 1;
        $buf['capacity'] = $cap;
        // In PHP le stringhe crescono automaticamente; manteniamo solo metadata
    }
}

function buf_append(&$buf, $chunk)
{
    // Appende chunk al buffer gestendo capacità e lunghezza
    $lenBefore = strlen($buf['data']);
    $lenChunk = strlen($chunk);
    $needed = $lenBefore + $lenChunk;
    buf_ensure_capacity($buf, $needed);
    $buf['data'] = $buf['data'] . $chunk;
    $buf['length'] = strlen($buf['data']);
}

function buf_clear(&$buf)
{
    // Svuota i dati ma mantiene la capacità
    $buf['data'] = '';
    $buf['length'] = 0;
}

function mem_stats()
{
    // Restituisce statistiche di allocazione/deallocazione
    global $__MEM_STATS;
    return $__MEM_STATS;
}

?>

