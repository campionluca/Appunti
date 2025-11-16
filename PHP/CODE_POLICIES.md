# Code Policies - PHP

> Standard, convenzioni e politiche di scrittura del codice per il libro su PHP

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Codice](#template-di-codice)
- [Struttura dei File](#struttura-dei-file)
- [Best Practices](#best-practices)
- [Pattern di Programmazione](#pattern-di-programmazione)
- [Gestione Errori](#gestione-errori)
- [Commenti e Documentazione](#commenti-e-documentazione)

---

## Standard di Scrittura

### Formattazione (PSR-12)
- **Indentazione**: 4 spazi (no tab)
- **Lunghezza linea**: max 120 caratteri
- **Encoding**: UTF-8 without BOM
- **Fine riga**: LF (Unix)
- **PHP Tags**: Sempre `<?php`, mai short tags `<?`

### Stile del Codice
```php
<?php

declare(strict_types=1);

namespace App\Service;

use App\Model\User;
use App\Exception\UserNotFoundException;

/**
 * User service implementation
 */
class UserService
{
    private const DEFAULT_LIMIT = 10;

    private UserRepository $repository;
    private LoggerInterface $logger;

    public function __construct(
        UserRepository $repository,
        LoggerInterface $logger
    ) {
        $this->repository = $repository;
        $this->logger = $logger;
    }

    public function getUserById(int $id): User
    {
        $user = $this->repository->find($id);

        if ($user === null) {
            throw new UserNotFoundException("User not found: {$id}");
        }

        return $user;
    }

    public function getAllUsers(int $limit = self::DEFAULT_LIMIT): array
    {
        return $this->repository->findAll($limit);
    }
}
```

### Regole Generali
- [ ] Sempre usare `declare(strict_types=1);`
- [ ] Un file = una classe (eccetto piccole helper classes)
- [ ] Sempre specificare visibility (public, private, protected)
- [ ] Usare type declarations per parametri e return values
- [ ] File deve terminare con una newline

---

## Convenzioni di Nomenclatura

### Variabili e Proprietà
- **Variabili**: `$camelCase` - Esempio: `$userName`, `$totalCount`
- **Proprietà**: `$camelCase` - Esempio: `$firstName`, `$isActive`
- **Costanti di classe**: `UPPER_SNAKE_CASE` - Esempio: `MAX_USERS`, `API_VERSION`
- **Costanti globali**: `UPPER_SNAKE_CASE` - Esempio: `APP_ENV`, `DB_HOST`

### Funzioni e Metodi
- **Funzioni**: `camelCase()` o `snake_case()` - Esempio: `calculateTotal()` o `calculate_total()`
- **Metodi**: `camelCase()` - Esempio: `getUserById()`, `processPayment()`
- **Getter**: `getSomething()` - Esempio: `getName()`, `getAge()`
- **Setter**: `setSomething()` - Esempio: `setName()`, `setAge()`
- **Boolean getter**: `isSomething()` o `hasSomething()` - Esempio: `isValid()`, `hasPermission()`

### Classi e Interfacce
- **Classi**: `PascalCase` - Esempio: `UserManager`, `DatabaseConnection`
- **Interfacce**: `PascalCase` con suffisso Interface - Esempio: `UserRepositoryInterface`
- **Abstract classes**: `PascalCase` con prefisso Abstract - Esempio: `AbstractController`
- **Traits**: `PascalCase` - Esempio: `TimestampTrait`, `ValidationTrait`
- **Exceptions**: `PascalCase` con suffisso Exception - Esempio: `ValidationException`

### Namespace e File
- **Namespace**: `PascalCase` - Esempio: `App\Service\User`
- **File**: `PascalCase.php` (match class name) - Esempio: `UserService.php`

---

## Template di Codice

### Template Classe
```php
<?php

declare(strict_types=1);

namespace App\Model;

use DateTime;

/**
 * Represents a user in the system
 *
 * This class handles user data and basic user operations.
 *
 * @author Nome Autore
 * @version 1.0.0
 */
class User
{
    // === CONSTANTS ===
    private const MIN_AGE = 18;
    private const MAX_NAME_LENGTH = 100;

    // === PROPERTIES ===
    private int $id;
    private string $name;
    private string $email;
    private ?DateTime $createdAt;

    // === CONSTRUCTOR ===

    /**
     * Create a new User instance
     *
     * @param int $id User ID
     * @param string $name User's full name
     * @param string $email User's email address
     * @throws \InvalidArgumentException If email is invalid
     */
    public function __construct(int $id, string $name, string $email)
    {
        $this->id = $id;
        $this->setName($name);
        $this->setEmail($email);
        $this->createdAt = new DateTime();
    }

    // === PUBLIC METHODS ===

    /**
     * Get user's full name
     *
     * @return string
     */
    public function getName(): string
    {
        return $this->name;
    }

    /**
     * Set user's name with validation
     *
     * @param string $name
     * @return void
     * @throws \InvalidArgumentException If name is too long
     */
    public function setName(string $name): void
    {
        if (strlen($name) > self::MAX_NAME_LENGTH) {
            throw new \InvalidArgumentException(
                "Name exceeds maximum length of " . self::MAX_NAME_LENGTH
            );
        }

        $this->name = trim($name);
    }

    /**
     * Check if user is active
     *
     * @return bool
     */
    public function isActive(): bool
    {
        return $this->createdAt !== null;
    }

    /**
     * Convert user to array representation
     *
     * @return array<string, mixed>
     */
    public function toArray(): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'created_at' => $this->createdAt?->format('Y-m-d H:i:s'),
        ];
    }

    // === PRIVATE METHODS ===

    /**
     * Validate email address
     *
     * @param string $email
     * @return void
     * @throws \InvalidArgumentException If email is invalid
     */
    private function setEmail(string $email): void
    {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException("Invalid email address: {$email}");
        }

        $this->email = $email;
    }
}
```

### Template Interfaccia
```php
<?php

declare(strict_types=1);

namespace App\Repository;

use App\Model\User;

/**
 * Interface for user repository operations
 */
interface UserRepositoryInterface
{
    /**
     * Find user by ID
     *
     * @param int $id
     * @return User|null
     */
    public function find(int $id): ?User;

    /**
     * Find all users with optional limit
     *
     * @param int $limit
     * @return User[]
     */
    public function findAll(int $limit = 10): array;

    /**
     * Save user to storage
     *
     * @param User $user
     * @return bool
     */
    public function save(User $user): bool;

    /**
     * Delete user by ID
     *
     * @param int $id
     * @return bool
     */
    public function delete(int $id): bool;
}
```

### Template Controller
```php
<?php

declare(strict_types=1);

namespace App\Controller;

use App\Service\UserService;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

/**
 * User controller
 */
class UserController extends AbstractController
{
    private UserService $userService;

    public function __construct(UserService $userService)
    {
        $this->userService = $userService;
    }

    /**
     * Show user by ID
     *
     * @param ServerRequestInterface $request
     * @param array<string, mixed> $args
     * @return ResponseInterface
     */
    public function show(ServerRequestInterface $request, array $args): ResponseInterface
    {
        try {
            $userId = (int) $args['id'];
            $user = $this->userService->getUserById($userId);

            return $this->json($user->toArray());
        } catch (\Exception $e) {
            return $this->error($e->getMessage(), 404);
        }
    }

    /**
     * List all users
     *
     * @param ServerRequestInterface $request
     * @return ResponseInterface
     */
    public function index(ServerRequestInterface $request): ResponseInterface
    {
        $users = $this->userService->getAllUsers();

        return $this->json([
            'data' => array_map(fn($user) => $user->toArray(), $users),
            'count' => count($users),
        ]);
    }
}
```

---

## Struttura dei File

### Organizzazione File PHP
```
1. <?php tag di apertura
2. declare(strict_types=1);
3. Namespace declaration
4. Use statements (raggruppati: vendor, app)
5. Class/Interface DocBlock
6. Class/Interface declaration
7. Constants
8. Properties
9. Constructor
10. Public methods
11. Protected methods
12. Private methods
```

### Organizzazione Progetto (PSR-4)
```
src/
├── Controller/
│   └── UserController.php
├── Service/
│   └── UserService.php
├── Repository/
│   ├── UserRepositoryInterface.php
│   └── UserRepository.php
├── Model/
│   └── User.php
├── Exception/
│   └── UserNotFoundException.php
└── Util/
    └── Validator.php

config/
tests/
public/
    └── index.php
```

---

## Best Practices

### Principi SOLID
- **S**ingle Responsibility: Una classe = una responsabilità
- **O**pen/Closed: Aperta all'estensione, chiusa alla modifica
- **L**iskov Substitution: Sottoclassi sostituibili alle superclassi
- **I**nterface Segregation: Interfacce piccole e specifiche
- **D**ependency Inversion: Dipendere da astrazioni

### Type Safety
- [ ] Sempre usare `declare(strict_types=1);`
- [ ] Dichiarare tipi per tutti i parametri
- [ ] Dichiarare return types per tutti i metodi
- [ ] Usare `?Type` per valori nullable
- [ ] Usare union types in PHP 8.0+ (`int|string`)

### Null Safety
```php
// Usare null coalescing operator
$value = $data['key'] ?? 'default';

// Usare nullsafe operator (PHP 8.0+)
$city = $user?->getAddress()?->getCity();

// Type hint nullable
public function find(int $id): ?User
{
    return $this->users[$id] ?? null;
}
```

### Sicurezza
- [ ] Sempre validare e sanitize input utente
- [ ] Usare prepared statements per query SQL
- [ ] Escapare output HTML con `htmlspecialchars()`
- [ ] Usare password_hash() per password
- [ ] Validare e verificare file uploads

```php
// SQL Injection Prevention
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = :id');
$stmt->execute(['id' => $userId]);

// XSS Prevention
echo htmlspecialchars($userInput, ENT_QUOTES, 'UTF-8');

// Password Hashing
$hash = password_hash($password, PASSWORD_DEFAULT);
if (password_verify($inputPassword, $hash)) {
    // Password correct
}
```

---

## Pattern di Programmazione

### Pattern Consigliati

```php
// Pattern 1: Dependency Injection
class UserService
{
    public function __construct(
        private UserRepositoryInterface $repository,
        private LoggerInterface $logger
    ) {}

    public function processUser(int $id): void
    {
        $user = $this->repository->find($id);
        $this->logger->info("Processing user: {$id}");
    }
}

// Pattern 2: Factory
class UserFactory
{
    public static function create(array $data): User
    {
        return new User(
            id: $data['id'] ?? 0,
            name: $data['name'] ?? '',
            email: $data['email'] ?? ''
        );
    }

    public static function createFromDatabase(array $row): User
    {
        return new User(
            id: (int) $row['id'],
            name: $row['full_name'],
            email: $row['email_address']
        );
    }
}

// Pattern 3: Repository
class UserRepository implements UserRepositoryInterface
{
    public function __construct(private PDO $pdo) {}

    public function find(int $id): ?User
    {
        $stmt = $this->pdo->prepare('SELECT * FROM users WHERE id = :id');
        $stmt->execute(['id' => $id]);
        $row = $stmt->fetch();

        return $row ? UserFactory::createFromDatabase($row) : null;
    }
}

// Pattern 4: Fluent Interface
class QueryBuilder
{
    private array $select = [];
    private string $from = '';
    private array $where = [];

    public function select(string ...$columns): self
    {
        $this->select = array_merge($this->select, $columns);
        return $this;
    }

    public function from(string $table): self
    {
        $this->from = $table;
        return $this;
    }

    public function where(string $condition): self
    {
        $this->where[] = $condition;
        return $this;
    }

    public function build(): string
    {
        $sql = 'SELECT ' . implode(', ', $this->select);
        $sql .= ' FROM ' . $this->from;

        if (!empty($this->where)) {
            $sql .= ' WHERE ' . implode(' AND ', $this->where);
        }

        return $sql;
    }
}

// Usage:
$query = (new QueryBuilder())
    ->select('id', 'name', 'email')
    ->from('users')
    ->where('active = 1')
    ->where('age > 18')
    ->build();

// Pattern 5: Singleton (evitare quando possibile)
class Database
{
    private static ?self $instance = null;

    private function __construct(private PDO $pdo) {}

    public static function getInstance(): self
    {
        if (self::$instance === null) {
            self::$instance = new self(new PDO(/* ... */));
        }

        return self::$instance;
    }
}
```

### Anti-Pattern da Evitare

```php
// ❌ EVITARE: Variabili superglobali dirette
$userId = $_GET['id'];  // No validation!

// ✅ PREFERIRE: Validazione e sanitizzazione
$userId = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($userId === false || $userId === null) {
    throw new InvalidArgumentException('Invalid user ID');
}

// ❌ EVITARE: SQL Injection
$sql = "SELECT * FROM users WHERE id = {$_GET['id']}";

// ✅ PREFERIRE: Prepared Statements
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = :id');
$stmt->execute(['id' => $userId]);

// ❌ EVITARE: Error suppression
$data = @file_get_contents($file);  // Nasconde errori!

// ✅ PREFERIRE: Gestione esplicita errori
try {
    $data = file_get_contents($file);
} catch (\Exception $e) {
    // Handle error properly
}
```

---

## Gestione Errori

### Exception Handling

```php
<?php

// Custom exception
namespace App\Exception;

class ApplicationException extends \Exception
{
    public function __construct(
        string $message = '',
        int $code = 0,
        ?\Throwable $previous = null
    ) {
        parent::__construct($message, $code, $previous);
    }
}

class ValidationException extends ApplicationException {}

// Try-catch
try {
    $user = $userService->getUserById($id);
    $user->activate();
} catch (UserNotFoundException $e) {
    // Handle not found
    $logger->warning("User not found: {$id}");
    return null;
} catch (ValidationException $e) {
    // Handle validation error
    $logger->error("Validation failed: {$e->getMessage()}");
    throw $e;
} catch (\Exception $e) {
    // Handle generic error
    $logger->error("Unexpected error", ['exception' => $e]);
    throw new ApplicationException('Operation failed', 0, $e);
} finally {
    // Cleanup
    $connection->close();
}

// Error handling in production
set_error_handler(function ($severity, $message, $file, $line) {
    throw new \ErrorException($message, 0, $severity, $file, $line);
});

set_exception_handler(function (\Throwable $e) {
    error_log($e->getMessage());
    // Show generic error to user
    http_response_code(500);
    echo json_encode(['error' => 'Internal server error']);
});
```

---

## Commenti e Documentazione

### PHPDoc

```php
<?php

/**
 * Calculate user's total score
 *
 * This method aggregates all scores from user activities
 * and applies bonus multipliers based on user level.
 *
 * @param User $user The user to calculate score for
 * @param array<string, int> $activities Map of activity scores
 * @param float $multiplier Score multiplier (default: 1.0)
 *
 * @return int Total calculated score
 *
 * @throws \InvalidArgumentException If multiplier is negative
 * @throws UserNotFoundException If user doesn't exist
 *
 * @see User::getLevel()
 * @since 1.2.0
 *
 * @example
 * $score = calculateScore($user, ['quiz' => 100, 'homework' => 50], 1.5);
 */
public function calculateScore(
    User $user,
    array $activities,
    float $multiplier = 1.0
): int {
    // Implementation
}

/**
 * User model class
 *
 * @property-read int $id User ID
 * @property string $name User's name
 *
 * @method bool isActive() Check if user is active
 * @method void activate() Activate the user
 */
class User
{
    // ...
}
```

### Commenti Inline

```php
// TODO: Implement caching mechanism
// FIXME: Memory leak when processing large files
// HACK: Workaround for PHP bug #12345
// NOTE: This method assumes UTC timezone

// Commenta il "perché", non il "cosa"
// ✅ BUONO:
// We use 60-second timeout because the API can be slow during peak hours
private const TIMEOUT = 60;

// ❌ CATTIVO:
// Set timeout to 60 seconds
private const TIMEOUT = 60;
```

---

## Note Aggiuntive

### Versione PHP
- **Target**: PHP 8.1+ (o specificare versione minima)
- **Features moderne**: Constructor property promotion, named arguments, enums, readonly properties

### Tool e Linter
- **Formatter**: PHP CS Fixer, PHP_CodeSniffer
- **Static Analysis**: PHPStan, Psalm
- **Testing**: PHPUnit, Pest
- **Debugging**: Xdebug

### Composer Configuration
```json
{
    "require": {
        "php": ">=8.1"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0",
        "phpstan/phpstan": "^1.10",
        "friendsofphp/php-cs-fixer": "^3.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

### Riferimenti
- PSR-1: Basic Coding Standard
- PSR-4: Autoloading Standard
- PSR-12: Extended Coding Style Guide
- PHP The Right Way (phptherightway.com)

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
