# Concept IDs Creati per il Corso C

Questo documento elenca tutti i concept_id creati nel file agenti_descrittori.json per il corso C (Terza).

## Language Basics (5 concepts)

### C-VARS-001: Dichiarazione e inizializzazione di variabili
- **Livello**: Beginner
- **Capitolo**: 02_variabili_tipi
- **Concetti**: Dichiarazione, inizializzazione, tipi base
- **Esempio**: Dichiarare e inizializzare variabili int, float, char

### C-TYPES-001: Tipi di dati in C
- **Livello**: Beginner
- **Capitolo**: 02_variabili_tipi
- **Concetti**: int, float, double, char, short, long, unsigned, sizeof()
- **Esempio**: Uso di tutti i tipi con stampa dimensioni e range

### C-OPS-001: Operatori aritmetici
- **Livello**: Beginner
- **Capitolo**: 03_operatori_espressioni
- **Concetti**: +, -, *, /, %, ++, --, divisione intera, cast
- **Esempio**: Operazioni aritmetiche con gestione divisione intera

### C-IO-001: Input/Output con scanf e printf
- **Livello**: Beginner
- **Capitolo**: 02_variabili_tipi
- **Concetti**: scanf, printf, specificatori formato (%d, %f, %c, %s), &
- **Esempio**: Lettura input utente e stampa formattata

### C-CONST-001: Costanti con #define e const
- **Livello**: Beginner
- **Capitolo**: 02_variabili_tipi
- **Concetti**: #define, const, differenze, scope
- **Esempio**: Costanti con entrambi i metodi e loro utilizzo

---

## Control Structures (4 concepts)

### C-IF-001: Istruzioni condizionali if/else
- **Livello**: Beginner
- **Capitolo**: 04_controllo_flusso
- **Concetti**: if, else, else if, operatore ternario, condizioni multiple
- **Esempio**: Valutazione voto con if/else if/else

### C-SWITCH-001: Istruzione switch-case
- **Livello**: Beginner
- **Capitolo**: 04_controllo_flusso
- **Concetti**: switch, case, break, default, fall-through
- **Esempio**: Menu con switch e raggruppamento case

### C-LOOP-001: Cicli for, while, do-while
- **Livello**: Beginner
- **Capitolo**: 04_controllo_flusso
- **Concetti**: for, while, do-while, cicli annidati, iterazioni
- **Esempio**: Vari tipi di ciclo con tabella pitagorica

### C-BREAK-001: Controllo cicli con break e continue
- **Livello**: Intermediate
- **Capitolo**: 04_controllo_flusso
- **Concetti**: break, continue, controllo flusso, cicli infiniti
- **Esempio**: Ricerca con break e filtro con continue

---

## Pointers & Memory (3 concepts)

### C-PTR-001: Puntatori: concetti base e dereferenziazione
- **Livello**: Intermediate
- **Capitolo**: 07_puntatori
- **Concetti**: *, &, dereferenziazione, NULL, indirizzi memoria
- **Esempio**: Dichiarazione puntatori, dereferenziazione, modifica tramite puntatore

### C-PTR-002: Puntatori e funzioni: passaggio per riferimento
- **Livello**: Intermediate
- **Capitolo**: 07_puntatori, 05_funzioni
- **Concetti**: Passaggio per valore vs riferimento, scambio valori, valori multipli
- **Esempio**: Funzioni con puntatori per modificare variabili e ritornare più valori

### C-MEM-001: Allocazione dinamica: malloc, calloc, realloc, free
- **Livello**: Intermediate
- **Capitolo**: 07_puntatori
- **Concetti**: malloc, calloc, realloc, free, NULL check, memory leak
- **Esempio**: Allocazione array dinamico con ridimensionamento

---

## Functions & Scope (2 concepts)

### C-FUNC-001: Definizione e chiamata di funzioni
- **Livello**: Beginner
- **Capitolo**: 05_funzioni
- **Concetti**: Dichiarazione, definizione, parametri, return, ricorsione
- **Esempio**: Funzioni varie incluso fattoriale ricorsivo

### C-SCOPE-001: Scope delle variabili: locali, globali, static
- **Livello**: Intermediate
- **Capitolo**: 05_funzioni
- **Concetti**: Scope locale, globale, static, lifetime variabili
- **Esempio**: Confronto tra variabili locali, static e globali

---

## Riepilogo Statistiche

- **Totale concept_id**: 15
- **Livello Beginner**: 9 concepts
- **Livello Intermediate**: 6 concepts
- **Livello Advanced**: 0 concepts

## Distribuzione per Categoria

- **Language Basics**: 5 concepts (33.3%)
- **Control Structures**: 4 concepts (26.7%)
- **Pointers & Memory**: 3 concepts (20.0%)
- **Functions & Scope**: 2 concepts (13.3%)

## Capitoli Coperti

Tutti gli 11 capitoli principali sono stati analizzati:
1. Introduzione al C
2. Variabili e Tipi ✓
3. Operatori ed Espressioni ✓
4. Controllo di Flusso ✓
5. Funzioni ✓
6. Array (integrato)
7. Puntatori ✓
8. Stringhe (integrato)
9. Struct (esempi)
10. File (esempi)
11. Esercizi (referenziati)

## Note

- Gli array e le stringhe non hanno concept_id dedicati perché sono integrati negli esempi di puntatori e struct
- Gli argomenti avanzati (Makefile, GDB) sono stati volutamente esclusi per concentrarsi sui fondamentali
- Tutti i concept_id seguono la convenzione: C-CATEGORIA-NNN
