<?php
// app.php — Applicazione di elaborazione file di testo con approccio C-like
// Vincoli: niente mb_*, niente ??, niente preg_*, niente ENT_* e 'UTF-8', nessuna return type declaration
// Documentato con commenti su flusso di controllo e gestione memoria simulata

require __DIR__ . '/buffer.php';
require __DIR__ . '/io.php';
require __DIR__ . '/encoding.php';

// Configurazione di elaborazione
$BLOCK_SIZE = 4096;          // dimensione del blocco di lettura
$TAB_SPACES = 4;             // numero di spazi per TAB
$REPLACE_NON_ASCII = true;   // sanifica caratteri non ASCII

// Determinazione del file di input
$inputPath = '';
if (PHP_SAPI === 'cli') {
    // Uso CLI: php app.php input.txt [output.txt]
    if (isset($argv) && isset($argv[1])) {
        $inputPath = $argv[1];
        $outputPath = (isset($argv[2])) ? $argv[2] : (dirname(__FILE__) . '/output.txt');
    } else {
        fwrite(STDERR, "Uso: php app.php <input> [output]\n");
        exit(1);
    }
} else {
    // Uso web: app.php?file=...
    if (isset($_GET['file'])) { $inputPath = $_GET['file']; } else { $inputPath = __DIR__ . '/input_sample.txt'; }
    $outputPath = __DIR__ . '/output.txt';
}

// Apertura input e output in modalità binaria
$in = io_open($inputPath, 'rb');
if (!$in['ok']) {
    $msg = 'Errore apertura input: ' . $inputPath;
    if (PHP_SAPI === 'cli') { fwrite(STDERR, $msg . "\n"); } else { echo html_escape_basic($msg); }
    exit(1);
}

$out = io_open($outputPath, 'wb');
if (!$out['ok']) {
    $msg = 'Errore apertura output: ' . $outputPath;
    if (PHP_SAPI === 'cli') { fwrite(STDERR, $msg . "\n"); } else { echo html_escape_basic($msg); }
    io_close($in['fp']);
    exit(1);
}

// Buffer di linea per costruire righe fino a LF
$lineBuf = buf_create(1024);
$bytesProcessed = 0;
$linesProcessed = 0;

// Lettura a blocchi e normalizzazione
for (;;) {
    $r = io_read_block($in['fp'], $BLOCK_SIZE);
    if (!$r['ok']) { break; }
    $chunk = $r['data'];
    if ($chunk === '') { break; } // EOF

    // Normalizza newlines CRLF/CR -> LF
    $chunk = normalize_newlines($chunk);
    // Opzionale: sanifica non-ASCII
    if ($REPLACE_NON_ASCII) { $chunk = ascii_sanitize($chunk); }

    // Scansione dei byte per comporre righe
    $L = strlen($chunk);
    for ($i = 0; $i < $L; $i++) {
        $ch = $chunk[$i];
        if ($ch === "\n") {
            // Fine riga: post-process (trim e tab->spazi) e scrivi
            $line = trim_right_spaces($lineBuf['data']);
            $line = replace_tabs_with_spaces($line, $TAB_SPACES);
            $line = $line . "\n"; // preserva newline
            io_write_block($out['fp'], $line);
            $bytesProcessed += strlen($line);
            $linesProcessed += 1;
            buf_clear($lineBuf);
        } else {
            // Appendi carattere alla riga
            buf_append($lineBuf, $ch);
        }
    }
}

// Scrivi eventuale ultima riga senza LF finale
if ($lineBuf['length'] > 0) {
    $line = trim_right_spaces($lineBuf['data']);
    $line = replace_tabs_with_spaces($line, $TAB_SPACES);
    io_write_block($out['fp'], $line);
    $bytesProcessed += strlen($line);
    $linesProcessed += 1;
}

// Chiusura file e deallocazione buffer
io_close($in['fp']);
io_close($out['fp']);
buf_free($lineBuf);

// Report esecuzione
$stats = mem_stats();
$report = "Processati $linesProcessed linee, $bytesProcessed byte. " .
          "allocs=" . $stats['allocs'] . ", frees=" . $stats['frees'] . ", reallocs=" . $stats['reallocs'];

if (PHP_SAPI === 'cli') {
    fwrite(STDOUT, $report . "\nOutput: " . $outputPath . "\n");
} else {
    // Escape basilare per HTML
    echo '<pre>' . html_escape_basic($report) . "\nOutput: " . html_escape_basic($outputPath) . '</pre>';
}

?>

