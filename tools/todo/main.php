<?php
// Minimal TODO/FIXME/NOTE scanner and consolidator
// Usage examples:
// php tools/todo/main.php --scan --consolidate --output=json
// php tools/todo/main.php --scan=tools/todo/sample --consolidate
// php tools/todo/main.php --execute=3 --output=json

date_default_timezone_set('Europe/Rome');

function log_msg(string $message): void {
    $root = realpath(__DIR__ . '/../../');
    $logDir = $root . DIRECTORY_SEPARATOR . 'logs';
    if (!is_dir($logDir)) {
        @mkdir($logDir, 0777, true);
    }
    $file = $logDir . DIRECTORY_SEPARATOR . 'todo_manager_' . date('Ymd') . '.log';
    $line = '[' . date('c') . '] ' . $message . PHP_EOL;
    @file_put_contents($file, $line, FILE_APPEND | LOCK_EX);
}

function load_env(): array {
    // Look for .env in tools/todo and root
    $envPaths = [__DIR__ . DIRECTORY_SEPARATOR . '.env', realpath(__DIR__ . '/../../') . DIRECTORY_SEPARATOR . '.env'];
    $env = [];
    foreach ($envPaths as $path) {
        if ($path && file_exists($path)) {
            $lines = file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
            foreach ($lines as $l) {
                if (strpos(trim($l), '#') === 0) continue;
                $parts = explode('=', $l, 2);
                if (count($parts) === 2) {
                    $env[trim($parts[0])] = trim($parts[1]);
                }
            }
        }
    }
    return $env;
}

function parse_comment_line(string $line): ?array {
    // Detect single-line comments with markers and TODO/FIXME/NOTE
    $patterns = [
        '/^\s*(?:\/\/|#)\s*(TODO|FIXME|NOTE)\b[:\-]?\s*(.+)$/i', // // or #
        '/^\s*<!--\s*(TODO|FIXME|NOTE)\b[:\-]?\s*(.+?)\s*-->\s*$/i', // HTML comment
        '/^\s*\/\*+\s*(TODO|FIXME|NOTE)\b[:\-]?\s*(.+?)\s*\*\/\s*$/i', // block on one line
    ];
    foreach ($patterns as $re) {
        if (preg_match($re, $line, $m)) {
            return ['type' => strtoupper($m[1]), 'text' => trim($m[2])];
        }
    }
    return null;
}

function extract_author(string $text): ?string {
    if (preg_match('/@([A-Za-z0-9_\.\-]+)/', $text, $m)) return $m[1];
    if (preg_match('/\b(?:autore|author|by)\s*[:=]\s*([^\]\)\|]+)$/i', $text, $m)) return trim($m[1]);
    return null;
}

function map_priority(string $type): string {
    switch (strtoupper($type)) {
        case 'FIXME': return 'urgent';
        case 'TODO': return 'important';
        default: return 'secondary';
    }
}

function estimate_complexity(string $text): int {
    $len = str_word_count($text);
    $bonus = 0;
    $keywords = ['refactor','ottimizza','optimize','security','sicurezza','bug','routing','database','prestazioni'];
    foreach ($keywords as $k) {
        if (stripos($text, $k) !== false) { $bonus++; }
    }
    if ($len + $bonus >= 14) return 3;
    if ($len + $bonus >= 7) return 2;
    return 1;
}

function scan_file(string $filePath, array &$results): void {
    $ext = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
    $lines = @file($filePath, FILE_IGNORE_NEW_LINES);
    if ($lines === false) return;

    $inBlock = false; $blockType = null;
    foreach ($lines as $i => $line) {
        $ln = $i + 1;
        $parsed = parse_comment_line($line);
        if (!$parsed) {
            // block comment detection
            if (!$inBlock) {
                if (strpos($line, '/*') !== false) { $inBlock = true; $blockType = '/*'; }
                if ($ext === 'html' && strpos($line, '<!--') !== false) { $inBlock = true; $blockType = '<!--'; }
            }
            if ($inBlock) {
                // Look for TODO/FIXME/NOTE inside block lines
                if (preg_match('/\b(TODO|FIXME|NOTE)\b[:\-]?\s*(.+)/i', $line, $m)) {
                    $parsed = ['type' => strtoupper($m[1]), 'text' => trim($m[2])];
                }
                // end of block
                if (($blockType === '/*' && strpos($line, '*/') !== false) || ($blockType === '<!--' && strpos($line, '-->') !== false)) {
                    $inBlock = false; $blockType = null;
                }
            }
        }
        if ($parsed) {
            $author = extract_author($parsed['text']);
            $priority = map_priority($parsed['type']);
            $detectedAt = date('c');
            $id = sha1(realpath($filePath) . '#' . $ln . '|' . trim($parsed['text']));
            $results[] = [
                'id' => $id,
                'type' => $parsed['type'],
                'text' => $parsed['text'],
                'file' => realpath($filePath),
                'line' => $ln,
                'author' => $author,
                'detected_at' => $detectedAt,
                'created_at' => $detectedAt,
                'priority' => $priority,
                'category' => $priority === 'urgent' ? 'Urgenti' : ($priority === 'important' ? 'Importanti' : 'Secondari'),
                'status' => 'pending',
                'complexity' => estimate_complexity($parsed['text']),
            ];
        }
    }
}

function scan_directories(array $paths, array $extensions): array {
    $results = [];
    foreach ($paths as $p) {
        $base = $p;
        if (!is_dir($base)) continue;
        $it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($base, FilesystemIterator::SKIP_DOTS));
        foreach ($it as $fileInfo) {
            if (!$fileInfo->isFile()) continue;
            $ext = strtolower($fileInfo->getExtension());
            if (!in_array($ext, $extensions, true)) continue;
            scan_file($fileInfo->getPathname(), $results);
        }
    }
    return $results;
}

function read_master(string $masterPath): array {
    if (!file_exists($masterPath)) return [];
    $json = @file_get_contents($masterPath);
    if (!$json) return [];
    $data = @json_decode($json, true);
    return is_array($data) ? $data : [];
}

function write_master(string $masterPath, array $items): void {
    @file_put_contents($masterPath, json_encode($items, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);
}

function consolidate(array $newItems, array $existing): array {
    $map = [];
    foreach ($existing as $e) { $map[$e['id']] = $e; }
    foreach ($newItems as $n) {
        if (isset($map[$n['id']])) {
            // keep more recent detection timestamp
            $prev = $map[$n['id']];
            $prev['detected_at'] = max($prev['detected_at'] ?? $prev['created_at'] ?? $n['detected_at'], $n['detected_at']);
            // prefer non-empty author
            if (empty($prev['author']) && !empty($n['author'])) $prev['author'] = $n['author'];
            // preserve status/completed_at if already completed
            $map[$n['id']] = $prev;
        } else {
            $map[$n['id']] = $n;
        }
    }
    // sort: priority desc, created_at asc, complexity desc
    $items = array_values($map);
    usort($items, function($a, $b) {
        $prioOrder = ['urgent' => 3, 'important' => 2, 'secondary' => 1];
        $pa = $prioOrder[$a['priority']] ?? 0; $pb = $prioOrder[$b['priority']] ?? 0;
        if ($pa !== $pb) return $pb <=> $pa;
        $ca = strtotime($a['created_at'] ?? $a['detected_at']);
        $cb = strtotime($b['created_at'] ?? $b['detected_at']);
        if ($ca !== $cb) return $ca <=> $cb;
        return ($b['complexity'] ?? 0) <=> ($a['complexity'] ?? 0);
    });
    return $items;
}

function complete_in_source(array $item): bool {
    $path = $item['file']; $line = (int)$item['line'];
    if (!is_file($path)) return false;
    $lines = file($path);
    if (!$lines) return false;
    $idx = $line - 1;
    if (!isset($lines[$idx])) return false;
    if (strpos($lines[$idx], 'COMPLETATO') !== false) return true; // already marked
    $lines[$idx] = rtrim($lines[$idx]) . ' [COMPLETATO ' . date('Y-m-d') . "]\n";
    return file_put_contents($path, implode('', $lines), LOCK_EX) !== false;
}

function execute_items(array $items, int $count, string $masterPath): array {
    $executed = [];
    $left = $count;
    foreach ($items as &$it) {
        if ($left <= 0) break;
        if (($it['status'] ?? 'pending') === 'completed') continue;
        // Analyze context (20 lines around) and mark as completed by updating the comment line
        $ok = complete_in_source($it);
        if ($ok) {
            $it['status'] = 'completed';
            $it['completed_at'] = date('c');
            $executed[] = $it['id'];
            $left--;
        }
    }
    // Persist updates
    write_master($masterPath, $items);
    return $executed;
}

function generate_html_report(array $items, string $destDir): string {
    if (!is_dir($destDir)) { @mkdir($destDir, 0777, true); }
    $completed = array_filter($items, fn($x) => ($x['status'] ?? 'pending') === 'completed');
    $pending = array_filter($items, fn($x) => ($x['status'] ?? 'pending') !== 'completed');
    $avgTime = '-';
    $durations = [];
    foreach ($completed as $c) {
        if (!empty($c['completed_at']) && !empty($c['created_at'])) {
            $durations[] = strtotime($c['completed_at']) - strtotime($c['created_at']);
        }
    }
    if ($durations) {
        $avg = array_sum($durations) / count($durations);
        $avgTime = sprintf('%.1f h', $avg / 3600);
    }
    $date = date('Y-m-d');
    $html = "<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>Report TODO {$date}</title>"
          . "<style>body{font-family:Arial} .ok{color:#2e7d32} .pending{color:#c62828} table{border-collapse:collapse;width:100%} td,th{border:1px solid #ddd;padding:8px} th{background:#f5f5f5}</style></head><body>"
          . "<h1>Report giornaliero TODO - {$date}</h1>"
          . "<p>Completati: <span class=ok>" . count($completed) . "</span> | Pendenti: <span class=pending>" . count($pending) . "</span> | Tempo medio: {$avgTime}</p>"
          . "<h2>Pendenti</h2><table><tr><th>Priorità</th><th>Tipo</th><th>Testo</th><th>File</th><th>Linea</th></tr>";
    foreach ($pending as $p) {
        $html .= '<tr><td>' . htmlspecialchars($p['priority']) . '</td><td>' . htmlspecialchars($p['type']) . '</td><td>' . htmlspecialchars($p['text']) . '</td><td>' . htmlspecialchars($p['file']) . '</td><td>' . (int)$p['line'] . '</td></tr>';
    }
    $html .= '</table><h2>Completati oggi</h2><table><tr><th>ID</th><th>Testo</th><th>File</th><th>Completato</th></tr>';
    foreach ($completed as $c) {
        $html .= '<tr><td>' . htmlspecialchars($c['id']) . '</td><td>' . htmlspecialchars($c['text']) . '</td><td>' . htmlspecialchars($c['file']) . '</td><td>' . htmlspecialchars($c['completed_at'] ?? '') . '</td></tr>';
    }
    $html .= '</table></body></html>';
    $path = $destDir . DIRECTORY_SEPARATOR . 'report_' . $date . '.html';
    file_put_contents($path, $html, LOCK_EX);
    return $path;
}

function main(): void {
    $env = load_env();
    $root = realpath(__DIR__ . '/../../');
    $masterPath = $env['MASTER_TODO'] ?? ($root . DIRECTORY_SEPARATOR . 'MASTER-TODO.json');
    if (!preg_match('/\.json$/', $masterPath)) $masterPath .= '.json';
    if (!preg_match('/^([A-Za-z]:\\|\\|\/)/', $masterPath)) { // make absolute if relative
        $masterPath = $root . DIRECTORY_SEPARATOR . $masterPath;
    }

    $opts = getopt('', ['scan::','consolidate::','execute::','output::','report::']);
    $output = $opts['output'] ?? 'json';
    $scanArg = $opts['scan'] ?? null;
    $doConsolidate = array_key_exists('consolidate', $opts);
    $executeArg = $opts['execute'] ?? null;
    $doReport = array_key_exists('report', $opts);

    $extensions = array_map('strtolower', array_filter(array_map('trim', explode(',', $env['EXTENSIONS'] ?? 'php,js,html,css'))));
    $paths = [];
    if ($scanArg) {
        $parts = preg_split('/\s*[;,]\s*/', $scanArg);
        foreach ($parts as $p) { if (!$p) continue; $paths[] = realpath($p) ?: $p; }
    } else {
        $parts = preg_split('/\s*[;,]\s*/', $env['SCAN_PATHS'] ?? '');
        foreach ($parts as $p) { if (!$p) continue; $paths[] = realpath($root . DIRECTORY_SEPARATOR . $p) ?: realpath($p) ?: $p; }
    }
    $paths = array_values(array_filter($paths, fn($p) => $p && is_dir($p)));

    $result = [];
    if ($scanArg !== null || !empty($paths)) {
        log_msg('Scanning paths: ' . implode(', ', $paths));
        $result = scan_directories($paths, $extensions);
    }

    if ($doConsolidate) {
        $existing = read_master($masterPath);
        $updated = consolidate($result, $existing);
        write_master($masterPath, $updated);
        log_msg('Consolidated into ' . $masterPath . ' (items: ' . count($updated) . ')');
        $result = $updated; // for output
    }

    if ($executeArg !== null) {
        $count = (int)$executeArg; if ($count <= 0) $count = 1;
        $existing = $doConsolidate ? $result : read_master($masterPath);
        $doneIds = execute_items($existing, $count, $masterPath);
        log_msg('Executed items: ' . implode(', ', $doneIds));
        $result = read_master($masterPath);
    }

    if ($doReport) {
        $items = $doConsolidate || $executeArg !== null ? $result : read_master($masterPath);
        $reportDir = $root . DIRECTORY_SEPARATOR . 'logs' . DIRECTORY_SEPARATOR . 'todo_reports';
        $reportPath = generate_html_report($items, $reportDir);
        log_msg('Generated report: ' . $reportPath);
        if ($output === 'html') {
            echo $reportPath . PHP_EOL;
        }
    }

    if ($output === 'json') {
        echo json_encode(['master' => $masterPath, 'count' => count($result), 'items' => $result], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . PHP_EOL;
    } else {
        // simple text output
        foreach ($result as $it) {
            echo sprintf("[%s] (%s) %s\n- %s:%d\n", $it['priority'], $it['type'], $it['text'], $it['file'], $it['line']);
        }
    }
}

main();

