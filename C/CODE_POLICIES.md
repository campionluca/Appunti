# Code Policies - C Programming

> Standard, convenzioni e politiche di scrittura del codice per il libro sul linguaggio C

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
- **Lunghezza linea**: max 80 caratteri
- **Encoding**: UTF-8
- **Fine riga**: LF (Unix)
- **Parentesi graffe**: K&R style (apertura sulla stessa riga)

### Stile del Codice
```c
// Esempio di stile preferito
int main(void) {
    int result = 0;

    if (result == 0) {
        printf("Success\n");
    } else {
        fprintf(stderr, "Error\n");
        return 1;
    }

    return 0;
}
```

### Regole Generali
- [ ] Sempre dichiarare variabili all'inizio del blocco (C89) o dove necessario (C99+)
- [ ] Usare const per valori immutabili
- [ ] Evitare variabili globali quando possibile
- [ ] Preferire static per funzioni non esportate
- [ ] Includere sempre headers necessari esplicitamente

---

## Convenzioni di Nomenclatura

### Variabili
- **Locali**: `snake_case` - Esempio: `buffer_size`, `user_input`
- **Globali**: `g_snake_case` - Esempio: `g_config`, `g_error_count`
- **Costanti**: `UPPER_SNAKE_CASE` - Esempio: `MAX_BUFFER_SIZE`, `PI`
- **Static**: `s_snake_case` - Esempio: `s_internal_counter`

### Funzioni
- **Pubbliche**: `snake_case` - Esempio: `calculate_sum()`, `parse_input()`
- **Private/Static**: `snake_case` con prefisso - Esempio: `_internal_helper()`
- **Callback**: `on_event_name` - Esempio: `on_signal_received()`

### Tipi
- **Struct**: `snake_case_t` - Esempio: `user_data_t`, `config_t`
- **Enum**: `UPPER_SNAKE_CASE` - Esempio: `enum ERROR_CODE`
- **Typedef**: `snake_case_t` - Esempio: `callback_func_t`
- **Union**: `snake_case_u` - Esempio: `data_value_u`

### File
- **Header**: `nome_modulo.h`
- **Source**: `nome_modulo.c`
- **Organizzazione**: raggruppare file correlati in sottodirectory

---

## Template di Codice

### Template Header File (.h)
```c
/**
 * @file nome_modulo.h
 * @brief Breve descrizione del modulo
 * @description Descrizione dettagliata delle funzionalità fornite
 * @author Nome Autore
 * @date Data creazione
 */

#ifndef NOME_MODULO_H
#define NOME_MODULO_H

#include <stdio.h>
/* Altri includes necessari */

/* === CONSTANTS === */
#define MAX_SIZE 1024

/* === TYPE DEFINITIONS === */
typedef struct {
    int field1;
    char field2[MAX_SIZE];
} data_t;

/* === FUNCTION DECLARATIONS === */

/**
 * @brief Breve descrizione funzione
 * @param param1 Descrizione parametro 1
 * @param param2 Descrizione parametro 2
 * @return Valore di ritorno (0 success, -1 error)
 */
int function_name(int param1, const char *param2);

#endif /* NOME_MODULO_H */
```

### Template Source File (.c)
```c
/**
 * @file nome_modulo.c
 * @brief Implementazione del modulo
 * @author Nome Autore
 * @date Data creazione
 */

#include "nome_modulo.h"
#include <stdlib.h>
#include <string.h>

/* === PRIVATE CONSTANTS === */
#define INTERNAL_BUFFER 256

/* === PRIVATE TYPES === */
typedef struct {
    /* campi privati */
} internal_data_t;

/* === PRIVATE VARIABLES === */
static int s_init_flag = 0;

/* === PRIVATE FUNCTION DECLARATIONS === */
static int _helper_function(void);

/* === PUBLIC FUNCTION IMPLEMENTATIONS === */

int function_name(int param1, const char *param2) {
    /* Input validation */
    if (param2 == NULL) {
        return -1;
    }

    /* Implementation */

    return 0;
}

/* === PRIVATE FUNCTION IMPLEMENTATIONS === */

static int _helper_function(void) {
    /* Implementation */
    return 0;
}
```

### Template Main
```c
/**
 * @file main.c
 * @brief Entry point del programma
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    /* Argument validation */
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <arg>\n", argv[0]);
        return EXIT_FAILURE;
    }

    /* Main logic */

    return EXIT_SUCCESS;
}
```

---

## Struttura dei File

### Organizzazione Header (.h)
```
1. Header guard (#ifndef)
2. Includes di sistema (<...>)
3. Includes locali ("...")
4. Macro e costanti (#define)
5. Typedef e struct
6. Dichiarazioni funzioni pubbliche
7. Chiusura header guard (#endif)
```

### Organizzazione Source (.c)
```
1. Include del proprio header
2. Altri includes
3. Macro e costanti private
4. Tipi e struct private
5. Variabili static
6. Dichiarazioni funzioni private
7. Implementazioni funzioni pubbliche
8. Implementazioni funzioni private
```

---

## Best Practices

### Principi Generali
- **DRY**: Evitare duplicazione di codice, usare funzioni helper
- **KISS**: Funzioni semplici e focalizzate su un compito
- **YAGNI**: Non implementare funzionalità non richieste
- **Separation of Concerns**: Un file/modulo per ogni responsabilità

### Codice Pulito
- [ ] Funzioni max 50-100 righe
- [ ] Nesting max 3-4 livelli
- [ ] Nomi descrittivi (evitare abbreviazioni criptiche)
- [ ] Evitare magic numbers (usare #define o const)
- [ ] Una funzione fa una cosa sola

### Memory Management
- [ ] Sempre fare free() di ogni malloc()
- [ ] Verificare NULL dopo malloc/calloc
- [ ] Inizializzare puntatori a NULL
- [ ] Evitare memory leaks usando valgrind
- [ ] Usare sizeof(var) invece di sizeof(type)

### Sicurezza
- [ ] Validare sempre input utente
- [ ] Usare funzioni sicure (strncpy vs strcpy)
- [ ] Controllare buffer overflow
- [ ] Non assumere mai size di array
- [ ] Verificare return values di system calls

### Performance
- [ ] Evitare allocazioni in loop
- [ ] Usare const per parametri read-only
- [ ] Preferire stack allocation quando possibile
- [ ] Non ottimizzare prematuramente

---

## Pattern di Programmazione

### Pattern Consigliati

```c
// Pattern 1: Error Handling con goto
int process_data(void) {
    int result = -1;
    char *buffer = NULL;
    FILE *file = NULL;

    buffer = malloc(SIZE);
    if (buffer == NULL) {
        goto cleanup;
    }

    file = fopen("data.txt", "r");
    if (file == NULL) {
        goto cleanup;
    }

    /* Process data */
    result = 0;

cleanup:
    free(buffer);
    if (file != NULL) {
        fclose(file);
    }
    return result;
}

// Pattern 2: Opaque Pointer (Information Hiding)
// In header:
typedef struct object_t object_t;
object_t* object_create(void);
void object_destroy(object_t *obj);

// In source:
struct object_t {
    int private_field;
};

// Pattern 3: Function Pointer per Callbacks
typedef void (*callback_t)(int status, void *user_data);

void async_operation(callback_t callback, void *user_data) {
    /* do work */
    callback(0, user_data);
}
```

### Anti-Pattern da Evitare

```c
// ❌ EVITARE: Modifica parametri di output senza controllo
void bad_function(int *output) {
    *output = 42;  // Crash se output è NULL!
}

// ✅ PREFERIRE: Sempre validare puntatori
int good_function(int *output) {
    if (output == NULL) {
        return -1;
    }
    *output = 42;
    return 0;
}

// ❌ EVITARE: Return di puntatori a variabili locali
char* bad_string(void) {
    char local[10] = "hello";
    return local;  // ERRORE! local è distrutto
}

// ✅ PREFERIRE: Allocazione dinamica o buffer fornito
char* good_string(void) {
    char *result = malloc(10);
    if (result != NULL) {
        strcpy(result, "hello");
    }
    return result;
}
```

---

## Gestione Errori

### Strategia di Error Handling

```c
// Pattern 1: Return code (0 success, -1 error)
int function(void) {
    if (/* error condition */) {
        perror("function");
        return -1;
    }
    return 0;
}

// Pattern 2: Return NULL per puntatori
void* allocate_data(void) {
    void *ptr = malloc(SIZE);
    if (ptr == NULL) {
        perror("malloc");
        return NULL;
    }
    return ptr;
}

// Pattern 3: errno per system calls
#include <errno.h>

int safe_open(const char *path) {
    int fd = open(path, O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "Cannot open %s: %s\n",
                path, strerror(errno));
        return -1;
    }
    return fd;
}
```

### Codici di Errore
```c
// Definire enum per error codes
enum error_code {
    ERR_SUCCESS = 0,
    ERR_INVALID_ARG = -1,
    ERR_OUT_OF_MEMORY = -2,
    ERR_FILE_NOT_FOUND = -3,
    ERR_PERMISSION_DENIED = -4
};
```

---

## Commenti e Documentazione

### Quando Commentare
- ✅ Commenta algoritmi complessi
- ✅ Commenta invarianti e precondizioni
- ✅ Commenta workaround e limitazioni note
- ✅ Documenta API pubbliche
- ❌ Non commentare codice ovvio
- ❌ Non lasciare codice commentato

### Formato Commenti

```c
// Commento singola linea

/*
 * Commento multi-linea
 * per spiegazioni più lunghe
 */

/**
 * @brief Breve descrizione (una riga)
 * @details Descrizione dettagliata della funzione,
 *          del suo comportamento e delle sue responsabilità
 *
 * @param input Puntatore a buffer di input (non NULL)
 * @param size Dimensione del buffer (> 0)
 * @param output Puntatore a buffer di output (può essere NULL)
 *
 * @return 0 in caso di successo, -1 in caso di errore
 *
 * @note Questa funzione non è thread-safe
 * @warning output deve essere allocato dal chiamante
 */
int process(const char *input, size_t size, char *output);

// TODO: Implementare validazione avanzata
// FIXME: Memory leak in caso di errore
// HACK: Workaround temporaneo per bug in libreria X
// NOTE: Questa funzione assume little-endian
```

---

## Note Aggiuntive

### Standard C
- **Standard target**: C99 (o C11 se specificato)
- **Compilatore**: GCC/Clang con -std=c99 -Wall -Wextra -pedantic
- **Features C99**: dichiarazioni variabili ovunque, // comments, inline, bool

### Tool e Linter
- **Formatter**: clang-format
- **Static Analysis**: cppcheck, clang-tidy
- **Memory Check**: valgrind
- **Debugging**: gdb
- **Build**: Make/CMake

### Compilazione
```bash
# Flags raccomandati
gcc -std=c99 -Wall -Wextra -Wpedantic -O2 -o program program.c

# Debug
gcc -std=c99 -Wall -Wextra -g -o program program.c

# Con sanitizers
gcc -std=c99 -Wall -Wextra -fsanitize=address -g -o program program.c
```

### Riferimenti
- C99 Standard (ISO/IEC 9899:1999)
- K&R "The C Programming Language"
- MISRA C (per embedded/critical systems)

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
