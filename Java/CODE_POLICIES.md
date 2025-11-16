# Code Policies - Java

> Standard, convenzioni e politiche di scrittura del codice per il libro su Java

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

### Formattazione
- **Indentazione**: 4 spazi (no tab)
- **Lunghezza linea**: max 120 caratteri
- **Encoding**: UTF-8
- **Fine riga**: LF (Unix)
- **Parentesi graffe**: Egyptian brackets (apertura sulla stessa riga)

### Stile del Codice
```java
// Esempio di stile preferito
public class Example {
    private static final int MAX_SIZE = 100;
    private String name;

    public Example(String name) {
        this.name = name;
    }

    public void processData() {
        if (name != null && !name.isEmpty()) {
            System.out.println("Processing: " + name);
        } else {
            throw new IllegalStateException("Name cannot be null or empty");
        }
    }
}
```

### Regole Generali
- [ ] Una classe per file (eccetto inner classes)
- [ ] Usare @Override sempre quando si fa override
- [ ] Preferire composizione a ereditarietà
- [ ] Evitare wildcard imports (import java.util.*)
- [ ] Ordinare imports: java.*, javax.*, org.*, com.*, custom

---

## Convenzioni di Nomenclatura

### Variabili e Campi
- **Locali**: `camelCase` - Esempio: `userName`, `totalCount`
- **Campi privati**: `camelCase` - Esempio: `firstName`, `isActive`
- **Costanti**: `UPPER_SNAKE_CASE` - Esempio: `MAX_USERS`, `DEFAULT_TIMEOUT`
- **Parametri**: `camelCase` - Esempio: `userId`, `inputData`

### Metodi
- **Metodi**: `camelCase` - Esempio: `calculateTotal()`, `getUserById()`
- **Getter**: `getSomething()` - Esempio: `getName()`, `getAge()`
- **Setter**: `setSomething()` - Esempio: `setName()`, `setAge()`
- **Boolean getter**: `isSomething()` o `hasSomething()` - Esempio: `isValid()`, `hasPermission()`

### Classi e Interfacce
- **Classi**: `PascalCase` - Esempio: `UserManager`, `DatabaseConnection`
- **Interfacce**: `PascalCase` - Esempio: `Serializable`, `Comparable`
- **Abstract classes**: `PascalCase` con prefisso Abstract - Esempio: `AbstractRepository`
- **Enum**: `PascalCase` - Esempio: `UserRole`, `HttpStatus`
- **Exception**: `PascalCase` con suffisso Exception - Esempio: `UserNotFoundException`

### Package
- **Naming**: `lowercase.separated` - Esempio: `com.example.project.module`
- **Organizzazione**: per feature o per layer (scegliere uno stile consistente)

---

## Template di Codice

### Template Classe
```java
package com.example.module;

import java.util.Objects;

/**
 * Breve descrizione della classe
 * <p>
 * Descrizione dettagliata del comportamento e responsabilità
 * della classe.
 *
 * @author Nome Autore
 * @version 1.0
 * @since 2025-11-16
 */
public class ClassName {

    // === CONSTANTS ===
    private static final int DEFAULT_CAPACITY = 10;

    // === FIELDS ===
    private String name;
    private int value;

    // === CONSTRUCTORS ===

    /**
     * Costruttore di default
     */
    public ClassName() {
        this("default", 0);
    }

    /**
     * Costruttore con parametri
     *
     * @param name il nome dell'oggetto
     * @param value il valore iniziale
     * @throws IllegalArgumentException se name è null
     */
    public ClassName(String name, int value) {
        this.name = Objects.requireNonNull(name, "name cannot be null");
        this.value = value;
    }

    // === PUBLIC METHODS ===

    /**
     * Descrizione del metodo
     *
     * @param param descrizione parametro
     * @return descrizione ritorno
     */
    public String publicMethod(int param) {
        // Implementation
        return name + param;
    }

    // === GETTERS/SETTERS ===

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = Objects.requireNonNull(name, "name cannot be null");
    }

    // === OBJECT METHODS ===

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ClassName that = (ClassName) o;
        return value == that.value && Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, value);
    }

    @Override
    public String toString() {
        return "ClassName{" +
                "name='" + name + '\'' +
                ", value=" + value +
                '}';
    }

    // === PRIVATE METHODS ===

    private void helperMethod() {
        // Implementation
    }
}
```

### Template Interfaccia
```java
package com.example.module;

/**
 * Descrizione dell'interfaccia
 *
 * @author Nome Autore
 * @version 1.0
 */
public interface InterfaceName {

    /**
     * Descrizione metodo
     *
     * @param param descrizione parametro
     * @return descrizione ritorno
     */
    String methodName(int param);

    /**
     * Default method con implementazione
     *
     * @return valore di default
     */
    default int defaultMethod() {
        return 0;
    }
}
```

### Template Enum
```java
package com.example.module;

/**
 * Descrizione enum
 */
public enum Status {
    ACTIVE("Active", 1),
    INACTIVE("Inactive", 0),
    PENDING("Pending", 2);

    private final String displayName;
    private final int code;

    Status(String displayName, int code) {
        this.displayName = displayName;
        this.code = code;
    }

    public String getDisplayName() {
        return displayName;
    }

    public int getCode() {
        return code;
    }
}
```

---

## Struttura dei File

### Organizzazione Classe
```
1. Package statement
2. Import statements (raggruppati e ordinati)
3. Class/Interface JavaDoc
4. Class declaration
5. Constants (static final)
6. Static fields
7. Instance fields
8. Constructors
9. Public methods
10. Protected methods
11. Package-private methods
12. Private methods
13. Getters/Setters (alla fine)
14. Inner classes/enums
```

### Organizzazione Package
```
com.example.project/
├── model/          # Entità e domain objects
├── repository/     # Accesso ai dati
├── service/        # Business logic
├── controller/     # Presentation layer
├── util/           # Utility classes
├── exception/      # Custom exceptions
└── config/         # Configuration
```

---

## Best Practices

### Principi SOLID
- **S**ingle Responsibility: Una classe = una responsabilità
- **O**pen/Closed: Aperta all'estensione, chiusa alla modifica
- **L**iskov Substitution: Sottoclassi sostituibili alle superclassi
- **I**nterface Segregation: Interfacce piccole e specifiche
- **D**ependency Inversion: Dipendere da astrazioni, non da implementazioni

### Codice Pulito
- [ ] Metodi max 20-30 righe
- [ ] Parametri max 3-4 per metodo
- [ ] Nesting max 3 livelli
- [ ] Nomi descrittivi (evitare abbreviazioni)
- [ ] Evitare magic numbers e strings

### Immutabilità
- [ ] Preferire final per variabili locali e parametri
- [ ] Usare final per campi quando possibile
- [ ] Creare classi immutabili quando appropriato
- [ ] Usare Collections.unmodifiable* per collections

### Null Safety
- [ ] Usare Objects.requireNonNull per validazione
- [ ] Preferire Optional<T> per return values opzionali
- [ ] Documentare con @Nullable/@NonNull quando necessario
- [ ] Evitare return null quando possibile

### Performance
- [ ] Evitare premature optimization
- [ ] Usare StringBuilder per concatenazioni multiple
- [ ] Considerare stream() vs for-loop in base al contesto
- [ ] Chiudere risorse con try-with-resources

---

## Pattern di Programmazione

### Pattern Consigliati

```java
// Pattern 1: Builder per oggetti complessi
public class User {
    private final String name;
    private final int age;
    private final String email;

    private User(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
        this.email = builder.email;
    }

    public static class Builder {
        private String name;
        private int age;
        private String email;

        public Builder name(String name) {
            this.name = name;
            return this;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder email(String email) {
            this.email = email;
            return this;
        }

        public User build() {
            return new User(this);
        }
    }
}

// Usage:
User user = new User.Builder()
    .name("John")
    .age(30)
    .email("john@example.com")
    .build();

// Pattern 2: Factory Method
public interface Shape {
    void draw();
}

public class ShapeFactory {
    public static Shape createShape(String type) {
        return switch (type.toLowerCase()) {
            case "circle" -> new Circle();
            case "square" -> new Square();
            default -> throw new IllegalArgumentException("Unknown shape: " + type);
        };
    }
}

// Pattern 3: Singleton (thread-safe)
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}

// Pattern 4: Strategy
public interface PaymentStrategy {
    void pay(double amount);
}

public class CreditCardPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paid " + amount + " with credit card");
    }
}
```

### Anti-Pattern da Evitare

```java
// ❌ EVITARE: Catch generico senza gestione
try {
    riskyOperation();
} catch (Exception e) {
    // Silently ignored - MOLTO MALE!
}

// ✅ PREFERIRE: Gestione specifica o propagazione
try {
    riskyOperation();
} catch (IOException e) {
    log.error("I/O error", e);
    throw new RuntimeException("Operation failed", e);
}

// ❌ EVITARE: Uso eccessivo di null
public String getUserName(int id) {
    User user = findUser(id);
    if (user == null) {
        return null;  // Forza controllo null ovunque
    }
    return user.getName();
}

// ✅ PREFERIRE: Optional
public Optional<String> getUserName(int id) {
    return findUser(id)
        .map(User::getName);
}
```

---

## Gestione Errori

### Strategia Exception Handling

```java
// Checked exceptions per errori recuperabili
public void readFile(String path) throws IOException {
    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        // Read file
    }
}

// Unchecked exceptions per errori di programmazione
public void processUser(User user) {
    Objects.requireNonNull(user, "user cannot be null");
    // Process
}

// Custom exceptions
public class UserNotFoundException extends Exception {
    public UserNotFoundException(String userId) {
        super("User not found: " + userId);
    }
}

// Try-with-resources per auto-close
try (Connection conn = getConnection();
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery(sql)) {
    // Use resources
} catch (SQLException e) {
    log.error("Database error", e);
    throw new DataAccessException("Failed to fetch data", e);
}
```

### Gerarchia Exceptions
- Usare Exception per checked exceptions
- Usare RuntimeException per unchecked exceptions
- Creare gerarchie significative
- Includere sempre un messaggio descrittivo

---

## Commenti e Documentazione

### JavaDoc

```java
/**
 * Calcola la somma di due numeri
 * <p>
 * Questo metodo esegue una semplice addizione di due valori interi.
 * Se il risultato supera {@link Integer#MAX_VALUE}, il comportamento
 * è indefinito a causa di overflow.
 *
 * @param a il primo addendo
 * @param b il secondo addendo
 * @return la somma di a e b
 * @throws IllegalArgumentException se entrambi i parametri sono negativi
 * @see #subtract(int, int)
 * @since 1.0
 * @deprecated Usa {@link #addLong(long, long)} per evitare overflow
 */
@Deprecated(since = "2.0", forRemoval = true)
public int add(int a, int b) {
    if (a < 0 && b < 0) {
        throw new IllegalArgumentException("Both parameters cannot be negative");
    }
    return a + b;
}

/**
 * Rappresenta un utente del sistema
 * <p>
 * Questa classe è immutabile e thread-safe.
 *
 * @author Nome Autore
 * @version 2.1
 * @since 1.0
 */
public final class User {
    // ...
}
```

### Commenti Inline

```java
// TODO: Implementare cache per migliorare performance
// FIXME: Questo metodo ha un bug con valori negativi
// HACK: Workaround temporaneo per bug in libreria X v1.2
// NOTE: Questo algoritmo assume che l'array sia ordinato

// Commenta il "perché", non il "cosa"
// ✅ BUONO:
// Usiamo timeout di 30s perché il servizio esterno può essere lento
private static final int TIMEOUT_SECONDS = 30;

// ❌ CATTIVO:
// Imposta timeout a 30
private static final int TIMEOUT_SECONDS = 30;
```

---

## Note Aggiuntive

### Versione Java
- **Target**: Java 17 LTS (o specificare altra versione)
- **Features moderne**: Records, Pattern Matching, Text Blocks, var

### Tool e Linter
- **Build**: Maven / Gradle
- **Formatter**: Google Java Format / IntelliJ formatter
- **Static Analysis**: SonarQube, SpotBugs, PMD
- **Testing**: JUnit 5, Mockito, AssertJ

### Esempio pom.xml Properties
```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
```

### Riferimenti
- Oracle Java Style Guide
- Google Java Style Guide
- Effective Java (Joshua Bloch)
- Clean Code (Robert C. Martin)

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
