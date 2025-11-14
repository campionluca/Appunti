<?php
/**
 * Generatore PDF didattico con Dompdf o TCPDF.
 *
 * Scopo
 * - Generare documenti PDF con contenuti dinamici, formattazione professionale, intestazioni/piè di pagina
 * - Esporre opzioni: download diretto, inline, oppure salvataggio su disco
 * - Validare input e gestire errori in modo robusto
 *
 * Dipendenze
 * - Dompdf (consigliato) oppure TCPDF
 * - Installazione tipica (composer):
 *   - Dompdf: `composer require dompdf/dompdf`
 *   - TCPDF:  `composer require tecnickcom/tcpdf`
 * - Autoload: il file tenta `vendor/autoload.php` dal progetto
 *
 * Avvertenze
 * - Se le librerie non sono installate, restituisce errore 501 con istruzioni
 * - L’opzione salvataggio scrive in `exports/` (creata se mancante) accanto a questo script
 * - Non usare `declare(strict_types=1)` per mantenere compatibilità con esempi esistenti
 *
 * Uso
 * - GET /pdf?title=T&author=A&content=HTML&mode=inline|download|save&filename=doc.pdf
 * - POST /pdf con gli stessi campi nel body
 *
 * Esempi
 * - Inline:  /pdf?title=Report&author=Campi&content=<b>Ciao</b>&mode=inline
 * - Download: /pdf?title=Report&author=Campi&content=Ciao&mode=download&filename=report.pdf
 * - Salva:   /pdf?title=Report&author=Campi&content=Ciao&mode=save&filename=report.pdf
 */

// Carica Composer autoload se presente (Dompdf/TCPDF)
$autoloadPaths = [
    dirname(__DIR__, 2) . '/vendor/autoload.php',        // repo root/vendor
    dirname(__DIR__) . '/vendor/autoload.php',            // PHP/vendor
    __DIR__ . '/vendor/autoload.php',                     // esempi/vendor
];
foreach ($autoloadPaths as $p) {
    if (file_exists($p)) {
        require_once $p;
        break;
    }
}

/**
 * Validazione semplice dei parametri input.
 * @param array $src Fonte (GET o POST)
 * @return array{title:string,author:string,content:string,mode:string,filename:string}
 */
function validateInput(array $src): array
{
    $title = trim((string)($src['title'] ?? 'Documento'));
    $author = trim((string)($src['author'] ?? 'Autore'));
    $content = (string)($src['content'] ?? '<p>Contenuto non fornito.</p>');
    $mode = strtolower((string)($src['mode'] ?? 'download'));
    $filename = trim((string)($src['filename'] ?? 'documento.pdf'));

    // Limiti basilari
    if ($title === '' || strlen($title) > 120) {
        header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 400 Bad Request', true, 400);
        header('Content-Type: application/json');
        echo json_encode(['error' => 'Titolo non valido']);
        exit;
    }
    if ($author === '' || strlen($author) > 80) {
        header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 400 Bad Request', true, 400);
        header('Content-Type: application/json');
        echo json_encode(['error' => 'Autore non valido']);
        exit;
    }
    // Confronto non stretto coerente con convenzione; $mode è string
    if (!in_array($mode, ['inline', 'download', 'save'], false)) {
        header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 400 Bad Request', true, 400);
        header('Content-Type: application/json');
        echo json_encode(['error' => 'Modalità non valida']);
        exit;
    }
    if ($filename == '' || !preg_match('/^[A-Za-z0-9._-]+\.pdf$/', $filename)) {
        header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 400 Bad Request', true, 400);
        header('Content-Type: application/json');
        echo json_encode(['error' => 'Filename non valido (deve terminare con .pdf)']);
        exit;
    }

    // Sanitizzazione prudente del contenuto: consentiamo HTML base
    // Rimuove script e oggetti potenzialmente pericolosi
    $content = preg_replace('#<(script|style|iframe|object)[^>]*>.*?</\1>#is', '', $content);

    return [
        'title' => $title,
        'author' => $author,
        'content' => $content,
        'mode' => $mode,
        'filename' => $filename,
    ];
}

/**
 * Genera HTML completo con header e footer.
 * @param string $title
 * @param string $author
 * @param string $contentHtml
 * @return string
 */
function buildHtml(string $title, string $author, string $contentHtml): string
{
    $date = date('Y-m-d H:i');
    $css = <<<CSS
    @page { margin: 80px 50px; }
    body { font-family: DejaVu Sans, Arial, sans-serif; font-size: 12px; color: #222; }
    h1 { font-size: 20px; margin: 0 0 10px; color: #0a5; }
    .header { position: fixed; top: -60px; left: 0; right: 0; height: 50px; border-bottom: 1px solid #ccc; font-size: 11px; color:#555; }
    .footer { position: fixed; bottom: -60px; left: 0; right: 0; height: 50px; border-top: 1px solid #ccc; font-size: 11px; color:#555; }
    .container { page-break-inside: auto; }
    .meta { margin: 6px 0; font-size: 11px; color: #666; }
    .content { margin-top: 10px; }
CSS;
    $html = <<<HTML
    <html>
    <head>
        <meta charset="utf-8" />
        <style>{$css}</style>
        <title>{$title}</title>
    </head>
    <body>
        <div class="header">{$title} — generato il {$date}</div>
        <div class="footer">© {$date} — Autore: {$author} — Pagina <span class="pageNumber"></span>/<span class="totalPages"></span></div>
        <div class="container">
            <h1>{$title}</h1>
            <div class="meta">Autore: {$author} • Data: {$date}</div>
            <div class="content">{$contentHtml}</div>
        </div>
        <script type="text/php">
            if (isset($pdf)) {
                // Dompdf: numerazione pagina nella footer
                $font = $fontMetrics->getFont("DejaVu Sans", "normal");
                $pdf->page_text(520, 810, "{PAGE_NUM}/{PAGE_COUNT}", $font, 10, array(0,0,0));
            }
        </script>
    </body>
    </html>
HTML;
    return $html;
}

/**
 * Output del PDF in base alla modalità richiesta.
 * @param string $filename
 * @param string $mode inline|download|save
 * @param string $pdfBytes
 * @return void
 */
function outputPdf(string $filename, string $mode, string $pdfBytes): void
{
    if ($mode == 'save') {
        $dir = __DIR__ . '/exports';
        if (!is_dir($dir)) {
            @mkdir($dir, 0775, true);
        }
        $path = $dir . '/' . $filename;
        $ok = @file_put_contents($path, $pdfBytes);
        // Eccezione giustificata: file_put_contents può restituire 0 (bytes) o false.
        // Usiamo confronto stretto per distinguere fallimento (false) da scrittura di 0 bytes.
        if ($ok === false) {
            header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 500 Internal Server Error', true, 500);
            header('Content-Type: application/json');
            echo json_encode(['error' => 'Salvataggio fallito']);
            return;
        }
        header('Content-Type: application/json');
        echo json_encode(['saved' => true, 'path' => $path]);
        return;
    }

    // Invio al client: inline o download
    header('Content-Type: application/pdf');
    header('Content-Length: ' . strlen($pdfBytes));
    $disposition = $mode == 'inline' ? 'inline' : 'attachment';
    header('Content-Disposition: ' . $disposition . '; filename="' . $filename . '"');
    echo $pdfBytes;
}

/**
 * Prova a generare PDF con Dompdf, altrimenti TCPDF. Se mancano entrambe, errore 501.
 * @param array $input
 * @return void
 */
function generatePdf(array $input): void
{
    $title = $input['title'];
    $author = $input['author'];
    $content = $input['content'];
    $mode = $input['mode'];
    $filename = $input['filename'];

    try {
        if (class_exists('Dompdf\\Dompdf')) {
            // Dompdf
            $dompdf = new Dompdf\Dompdf([
                'isRemoteEnabled' => false,
                'chroot' => __DIR__,
            ]);
            $html = buildHtml($title, $author, $content);
            $dompdf->loadHtml($html);
            $dompdf->setPaper('A4', 'portrait');
            $dompdf->render();
            $pdfBytes = $dompdf->output();
            outputPdf($filename, $mode, $pdfBytes);
            return;
        }

        if (class_exists('TCPDF')) {
            // TCPDF
            $pdf = new TCPDF();
            $pdf->SetCreator(PDF_CREATOR);
            $pdf->SetAuthor($author);
            $pdf->SetTitle($title);
            $pdf->SetSubject('Documento generato');
            $pdf->SetKeywords('PDF, TCPDF');
            $pdf->setPrintHeader(true);
            $pdf->setPrintFooter(true);
            $pdf->SetHeaderData('', 0, $title, 'Generato con TCPDF');
            $pdf->setHeaderFont(['dejavusans', '', 10]);
            $pdf->setFooterFont(['dejavusans', '', 9]);
            $pdf->SetMargins(15, 27, 15);
            $pdf->SetHeaderMargin(5);
            $pdf->SetFooterMargin(10);
            $pdf->SetAutoPageBreak(TRUE, 25);
            $pdf->SetFont('dejavusans', '', 11);
            $pdf->AddPage();
            $html = buildHtml($title, $author, $content);
            $pdf->writeHTML($html, true, false, true, false, '');
            $pdfBytes = $pdf->Output($filename, 'S'); // S = return as string
            outputPdf($filename, $mode, $pdfBytes);
            return;
        }

        // Nessuna libreria disponibile
        header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 501 Not Implemented', true, 501);
        header('Content-Type: application/json');
        echo json_encode([
            'error' => 'Libreria PDF non disponibile',
            'hint' => 'Installa dompdf/dompdf o tecnickcom/tcpdf con Composer e assicurati vendor/autoload.php',
        ]);
    } catch (Throwable $e) {
        header(($_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1') . ' 500 Internal Server Error', true, 500);
        header('Content-Type: application/json');
        echo json_encode(['error' => 'Generazione fallita', 'message' => $e->getMessage()]);
    }
}

// Entry-point: decide fonte input e invoca generazione
$source = $_SERVER['REQUEST_METHOD'] == 'POST' ? $_POST : $_GET;
$input = validateInput($source);
generatePdf($input);
