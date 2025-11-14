<?php
// encoding.php — Gestione manuale di caratteri e escape HTML senza librerie
// Vietato: ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8', preg_match

function ascii_sanitize($s)
{
    // Sostituisce byte non ASCII stampabili con '?'
    // Mantiene TAB (9), LF (10), CR (13), e spazi (32)
    $out = '';
    $n = strlen($s);
    for ($i = 0; $i < $n; $i++) {
        $c = $s[$i];
        $o = ord($c);
        if ($o === 9 || $o === 10 || $o === 13 || ($o >= 32 && $o <= 126)) {
            $out .= $c;
        } else {
            $out .= '?';
        }
    }
    return $out;
}

function html_escape_basic($s)
{
    // Escape minimale: &, <, >, "
    // Ordine importante: prima &
    $t = str_replace('&', '&amp;', $s);
    $t = str_replace('<', '&lt;', $t);
    $t = str_replace('>', '&gt;', $t);
    $t = str_replace('"', '&quot;', $t); // doppie virgolette
    return $t;
}

function normalize_newlines($s)
{
    // Converte CRLF (\r\n) e CR (\r) in LF (\n)
    $t = str_replace("\r\n", "\n", $s);
    $t = str_replace("\r", "\n", $t);
    return $t;
}

function trim_right_spaces($s)
{
    // Rimuove spazi/tabs finali manualmente (simile a rtrim)
    $n = strlen($s);
    if ($n === 0) { return $s; }
    $i = $n - 1;
    while ($i >= 0) {
        $ch = $s[$i];
        if ($ch === ' ' || $ch === "\t") { $i--; continue; }
        break;
    }
    return substr($s, 0, $i + 1);
}

function replace_tabs_with_spaces($s, $count)
{
    // Sostituisce TAB con un certo numero di spazi
    $spaces = '';
    for ($i = 0; $i < $count; $i++) { $spaces .= ' '; }
    return str_replace("\t", $spaces, $s);
}

?>

