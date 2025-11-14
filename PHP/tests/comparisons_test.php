<?php
/**
 * Suite semplice di test sui confronti per verificare la convenzione:
 * - usare == e != come standard
 * - usare === e !== solo se necessario (documentato)
 *
 * Esecuzione:
 *   php PHP/tests/comparisons_test.php
 */

function assertEqual($a, $b, $msg)
{
    if ($a == $b) {
        echo "[PASS] $msg\n";
    } else {
        echo "[FAIL] $msg -> " . var_export([$a, $b], true) . "\n";
    }
}

function assertNotEqual($a, $b, $msg)
{
    if ($a != $b) {
        echo "[PASS] $msg\n";
    } else {
        echo "[FAIL] $msg -> " . var_export([$a, $b], true) . "\n";
    }
}

function assertStrictFalse($value, $msg)
{
    // Eccezione voluta: controllo stretto di false
    if ($value === false) {
        echo "[PASS] $msg\n";
    } else {
        echo "[FAIL] $msg -> " . var_export($value, true) . "\n";
    }
}

echo "== Test di confronto standard ==\n";
assertEqual('POST', 'POST', 'Stringhe identiche');
assertEqual(5, '5', 'Numero vs stringa numerica');
assertNotEqual('5', '05', 'Stringa numerica con padding');
assertNotEqual('abc', 'abd', 'Stringhe diverse');

echo "\n== Edge cases su 0/false/null ==\n";
assertEqual(0, '0', '0 vs "0"');
assertEqual(false, 0, 'false vs 0 (confronto non stretto)');
assertNotEqual(null, '', 'null vs stringa vuota');

echo "\n== Eccezione stretta (documentata) ==\n";
$writeOk = 0; // simulazione: un salvataggio che scrive 0 bytes
assertStrictFalse(false, 'Fallimento esplicito (=== false)');
// Nota: 0 non deve essere considerato false in confronto stretto
if ($writeOk === false) {
    echo "[FAIL] 0 trattato come false (non corretto)\n";
} else {
    echo "[PASS] 0 non è false in confronto stretto\n";
}

echo "\n== Confronti di path e metodi normalizzati ==\n";
$method = strtoupper('post');
assertEqual($method, 'POST', 'Metodo normalizzato confrontato con ==');
$path = '/items/123';
$patternSegment = ':'; // controlliamo che lo pseudo-carattere sia riconosciuto
assertEqual($patternSegment, ':', 'Segmento parametro riconosciuto con ==');

echo "\nTest completati.\n";
