<?php
// Nota tecnica: rimosso strict_types per compatibilità degli esempi.

/**
 * Router didattico senza dipendenze per esempi PHP - Versione per studenti
 *
 * FUNZIONE E SCOPO:
 * Questo router dimostra i concetti fondamentali del routing web in PHP puro,
 * senza dipendenze esterne. È progettato specificamente per scopi didattici.
 *
 * CARATTERISTICHE PRINCIPALI:
 * - Gestione richieste HTTP (GET, POST, etc.)
 * - Sistema middleware modulare
 * - Supporto parametri di percorso
 * - Helper per risposte JSON/HTML
 * - Gestione errori centralizzata
 *
 * UTILIZZO (server built-in PHP):
 * - Avvia: `php -S localhost:8080 router.php`
 * - Visita: `http://localhost:8080/` per elenco rotte
 *
 * DIPENDENZE:
 * - Estensioni PHP standard: session, json, fileinfo (upload), mysqli (DB)
 * - Nessuna libreria esterna richiesta
 *
 * SPIEGAZIONE DECLARE(STRICT_TYPES=1):
 * Questa direttiva abilita la modalità strict types, che forza il controllo
 * rigoroso dei tipi di dato. In modalità strict:
 * - I parametri funzione devono corrispondere esattamente ai tipi dichiarati
 * - I valori restituiti devono corrispondere esattamente ai tipi dichiarati
 * - Migliora la sicurezza e previene bug sottili di tipo
 */

// Avvio sessione per esempi dimostrativi
if (session_status() !== PHP_SESSION_ACTIVE) {
    session_start();
}

/**
 * Classe Request - Rappresenta la richiesta HTTP
 * 
 * SPIEGAZIONE:
 * Questa classe incapsula tutti i dati della richiesta HTTP in un oggetto
 * orientato agli oggetti, rendendo il codice più leggibile e testabile.
 * 
 * FUNZIONI PRINCIPALI:
 * - fromGlobals(): factory method che crea Request dalle superglobali PHP
 * - isPost(): verifica se il metodo HTTP è POST
 * - getParam(): recupera parametri dal percorso (es. /user/:id)
 *
 * @property array $params Parametri estratti dal path (es. /user/:id)
 */
class Request
{
    /** @var string Metodo HTTP (GET/POST/...) */
    public string $method;
    /** @var string Path richiesto (es. /saluto) */
    public string $path;
    /** @var array Query string (chiave => valore) */
    public array $query = [];
    /** @var array Parametri POST */
    public array $post = [];
    /** @var array Header HTTP */
    public array $headers = [];
    /** @var array Parametri di route */
    public array $params = [];

    /**
     * Costruisce Request dai superglobali PHP
     * 
     * SPIEGAZIONE FUNZIONE:
     * Questo è un factory method statico che crea un'istanza di Request
     * popolando le proprietà con i valori delle superglobali PHP ($_SERVER, $_GET, $_POST).
     * 
     * SUPERGLOBALI UTILIZZATE:
     * - $_SERVER: contiene informazioni sul server e sull'ambiente di esecuzione
     * - $_GET: parametri della query string (dopo il ? nell'URL)
     * - $_POST: dati inviati tramite form con metodo POST
     * 
     * @return Request Istanza configurata della richiesta
     */
    public static function fromGlobals(): Request
    {
        $r = new self();
        $r->method = strtoupper($_SERVER['REQUEST_METHOD'] ?? 'GET');
        $r->path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?? '/';
        $r->query = $_GET ?? [];
        $r->post = $_POST ?? [];
        // Estrae gli header dalla superglobale
        if (function_exists('getallheaders')) {
            $r->headers = getallheaders();
        }
        return $r;
    }

    /** Restituisce true se la richiesta è POST. */
    public function isPost(): bool
    {
        // Uso confronto non stretto (==) coerente con convenzione; method è normalizzato a string
        return $this->method == 'POST';
    }

    /**
     * Ottiene un parametro della route (es. id da /item/:id)
     * @param string $name Nome del parametro
     * @return string|null Valore se presente
     */
    public function getParam(string $name): ?string
    {
        return $this->params[$name] ?? null;
    }
}

/**
 * Risposta HTTP con helper per header, stato e output.
 */
class Response
{
    /** Imposta lo status code HTTP. */
    public function status(int $code): void
    {
        $proto = $_SERVER['SERVER_PROTOCOL'] ?? 'HTTP/1.1';
        header($proto . ' ' . $code, true, $code);
    }

    /** Imposta un header di risposta. */
    public function header(string $name, string $value): void
    {
        header($name . ': ' . $value);
    }

    /** Invia una risposta JSON. */
    public function json($data, int $code = 200): void
    {
        $this->status($code);
        $this->header('Content-Type', 'application/json');
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
    }

    /** Invia una risposta HTML. */
    public function html(string $html, int $code = 200): void
    {
        $this->status($code);
        $this->header('Content-Type', 'text/html; charset=utf-8');
        echo $html;
    }

    /** Scrive output raw (testo). */
    public function write(string $text, int $code = 200): void
    {
        $this->status($code);
        echo $text;
    }
}

/**
 * Router minimale con supporto middleware e parametri di path.
 */
class Router
{
    /** @var array<string, array<int, array{pattern:string, handler:callable}>> */
    private array $routes = [];
    /** @var array<int, callable> Middleware chain */
    private array $middlewares = [];
    /** @var array Metriche semplici (hit per route) */
    private array $metrics = ['hits' => 0, 'routes' => []];

    /** Registra un handler per metodo e pattern. */
    public function add(string $method, string $pattern, callable $handler): void
    {
        $m = strtoupper($method);
        $this->routes[$m] ??= [];
        $this->routes[$m][] = ['pattern' => $pattern, 'handler' => $handler];
    }

    /** Aggiunge un middleware (Request, Response, next). */
    public function use(callable $middleware): void
    {
        $this->middlewares[] = $middleware;
    }

    /** Restituisce metriche (hit per route). */
    public function metrics(): array
    {
        return $this->metrics;
    }

    /** Esegue la catena middleware e dispatch. */
    public function run(Request $req, Response $res): void
    {
        $index = 0;
        $chain = function () use (&$index, $req, $res, &$chain) {
            // Quando finisce la chain, dispatcha la route
            if ($index >= count($this->middlewares)) {
                $this->dispatch($req, $res);
                return;
            }
            $mw = $this->middlewares[$index++];
            // Esegue middleware; deve chiamare $chain() per proseguire
            $mw($req, $res, $chain);
        };

        try {
            $chain();
        } catch (Throwable $e) {
            // Gestione errori centralizzata
            $res->json(['error' => 'Errore interno', 'message' => $e->getMessage()], 500);
        }
    }

    /**
     * Trova e esegue il primo handler che combacia.
     * Supporta pattern tipo "/items/:id" con estrazione parametri.
     */
    private function dispatch(Request $req, Response $res): void
    {
        $this->metrics['hits']++;
        $methodRoutes = $this->routes[$req->method] ?? [];
        foreach ($methodRoutes as $r) {
            $params = $this->match($r['pattern'], $req->path);
            if ($params !== null) {
                $req->params = $params; // associa parametri alla richiesta
                $this->metrics['routes'][$r['pattern']] = ($this->metrics['routes'][$r['pattern']] ?? 0) + 1;
                $handler = $r['handler'];
                $handler($req, $res);
                return;
            }
        }
        // Nessuna route trovata -> 404 con hint
        $known = [];
        foreach ($methodRoutes as $x) { $known[] = $x['pattern']; }
        $res->json(['error' => 'Non trovato', 'hint' => $known], 404);
    }

    /**
     * Confronta un pattern (es. "/items/:id") con un path, restituendo i parametri.
     * @return array|null Parametri estratti o null se non combacia
     */
    private function match(string $pattern, string $path): ?array
    {
        // Logica: spezza per "/" e confronta segmento a segmento
        $pp = trim($pattern, '/');
        $sp = trim($path, '/');
        $pSeg = $pp == '' ? [] : explode('/', $pp);
        $sSeg = $sp == '' ? [] : explode('/', $sp);
        if (count($pSeg) != count($sSeg)) {
            return null;
        }
        $params = [];
        foreach ($pSeg as $i => $seg) {
            if (strlen($seg) > 1 && $seg[0] == ':') {
                // Parametro: cattura segmento corrispondente
                $params[substr($seg, 1)] = $sSeg[$i];
                continue;
            }
            if ($seg != $sSeg[$i]) {
                return null;
            }
        }
        return $params;
    }
}

// ---------------------------
// Middleware
// ---------------------------

/**
 * Middleware Rate Limiting: limita richieste per IP a una soglia per minuto.
 * Semplice, in-memory; adatto solo a contesti didattici.
 */
$rateLimitMiddleware = function (Request $req, Response $res, callable $next): void {
    static $bucket = [];
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
    $now = time();
    $window = (int)floor($now / 60);
    $key = $ip . ':' . $window;
    $bucket[$key] = ($bucket[$key] ?? 0) + 1;
    $limit = 120; // massimo 120 richieste/min per IP
    if ($bucket[$key] > $limit) {
        $res->json(['error' => 'Rate limit superato'], 429);
        return;
    }
    $next();
};

// ---------------------------
// Registrazione rotte
// ---------------------------

$router = new Router();
$router->use($rateLimitMiddleware);

// Elenco rotte
    $router->add('GET', '/', function (Request $req, Response $res) use ($router) {
        $res->json([
            'routes' => [
                'GET /',
                'GET /saluto',
                'GET /saluto/json',
                'GET /session',
                'GET /form',
                'POST /processa',
                'POST /upload',
                'GET /pdf',
                'POST /pdf',
                'GET /metrics',
                'GET /api/health',
            ],
            'metrics' => $router->metrics(),
        ]);
});

// Saluti
$router->add('GET', '/saluto', function (Request $req, Response $res) {
    $res->write('Ciao!');
});

$router->add('GET', '/saluto/json', function (Request $req, Response $res) {
    $res->json(['msg' => 'Ciao!']);
});

// Esempi sessione
$router->add('GET', '/session', function (Request $req, Response $res) {
    // Include script di esempio; gestisce output direttamente
    require __DIR__ . '/session_demo.php';
});

// Form
$router->add('GET', '/form', function (Request $req, Response $res) {
    // Include HTML del form
    require __DIR__ . '/form.html';
});

// Elaborazione form (POST)
$router->add('POST', '/processa', function (Request $req, Response $res) {
    // Lo script esegue validazioni e produce output
    require __DIR__ . '/processa.php';
});

// Upload file (POST)
$router->add('POST', '/upload', function (Request $req, Response $res) {
    require __DIR__ . '/upload.php';
});

// Metriche
$router->add('GET', '/metrics', function (Request $req, Response $res) use ($router) {
    $res->json($router->metrics());
});

// Health check
$router->add('GET', '/api/health', function (Request $req, Response $res) {
    $res->json(['status' => 'ok', 'php' => PHP_VERSION]);
});

// Generazione PDF (GET/POST): usa Dompdf o TCPDF se disponibili
$router->add('GET', '/pdf', function (Request $req, Response $res) {
    require __DIR__ . '/pdf_demo.php';
});

$router->add('POST', '/pdf', function (Request $req, Response $res) {
    require __DIR__ . '/pdf_demo.php';
});

// Esecuzione router
$req = Request::fromGlobals();
$res = new Response();
$router->run($req, $res);
