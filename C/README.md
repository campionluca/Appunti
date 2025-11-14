# Appunti di Programmazione C

Materiale didattico per il corso di Programmazione C - 3° Anno Istituto Tecnico

## Descrizione

Questo repository contiene gli appunti completi del corso di Programmazione C (11 capitoli), organizzati in forma di libro LaTeX compilabile. Il materiale copre argomenti fondamentali della programmazione procedurale in linguaggio C, con focus su concetti pratici e applicabili.

## 11 Capitoli del Corso

1. **Cap. 00 - Prefazione** - Introduzione al corso, come usare il materiale
2. **Cap. 01 - Introduzione al C** - Storia, caratteristiche, primo programma, main con argc/argv
3. **Cap. 02 - Variabili e Tipi di Dati** - Dichiarazione, tipi base, costanti, scanf/printf
4. **Cap. 03 - Operatori ed Espressioni** - Aritmetici, logici, bit a bit, precedenza, conversioni (✅ COMPLETO)
5. **Cap. 04 - Controllo di Flusso** - if, switch, cicli (for, while, do-while) (✅ COMPLETO)
6. **Cap. 05 - Funzioni** - Definizione, parametri, ricorsione, scope (✅ COMPLETO)
7. **Cap. 06 - Array** - Monodimensionali, multidimensionali, ordinamento (✅ COMPLETO)
8. **Cap. 07 - Puntatori** - Operatori &/*, aritmetica, malloc/free, liste dinamiche (✅ COMPLETO)
9. **Cap. 08 - Stringhe** - Array di char, funzioni standard, manipolazione (✅ COMPLETO)
10. **Cap. 09 - Struct** - Definizione, accesso, typedef, allocazione dinamica (✅ COMPLETO)
11. **Cap. 10 - File** - I/O, modalità, formattato/binario, gestione errori (✅ COMPLETO)

## Contenuti Bonus
- **Cap. 11 - Esercizi Completi** - 120+ esercizi, 5 progetti integrati (✅ COMPLETO)
- **Appendice - Soluzioni** - ~25 soluzioni commentate (✅ COMPLETO)
- **Bibliografia** - Risorse, libri, piattaforme di pratica (✅ COMPLETO)

## Struttura del progetto

```
.
├── main.tex                    # File principale LaTeX
├── main.pdf                    # PDF compilato
├── capitoli/                   # Cartella con i capitoli
│   ├── 00_prefazione.tex
│   ├── 01_introduzione_c.tex
│   ├── 02_variabili_tipi.tex
│   ├── 03_operatori_espressioni.tex
│   ├── 04_controllo_flusso.tex
│   ├── 05_array.tex
│   ├── 06_funzioni.tex
│   ├── 07_puntatori.tex
│   ├── 08_stringhe.tex
│   ├── 09_struct.tex
│   ├── 10_file.tex
│   ├── 11_preprocessore.tex
│   ├── appendice_soluzioni.tex
│   └── 99_bibliografia.tex
├── immagini/                   # Risorse grafiche
├── logs/                       # Log di generazione
│   └── log_generazione.md
├── README.md                   # Questo file
├── TODO.md                     # Task da completare
└── PIANO_SVILUPPO.md          # Piano di sviluppo del progetto
```

## Requisiti

Per compilare il documento LaTeX:

- **LaTeX**: Distribuzione completa (TeX Live, MiKTeX o MacTeX)
- **Pacchetti richiesti**:
  - `babel` (supporto italiano)
  - `geometry` (impostazione margini)
  - `graphicx` (immagini)
  - `listings` (codice sorgente)
  - `xcolor` (colori)
  - `hyperref` (link e riferimenti)
  - `tcolorbox` (box colorati)
  - `tikz` (diagrammi)
  - `amsmath` (formule matematiche)

Per compilare ed eseguire gli esempi di codice:

- **GCC**: Compilatore C (parte di Build Essential su Linux, Xcode su macOS, MinGW su Windows)
- **IDE consigliati**: Code::Blocks, Dev-C++, Visual Studio Code, CLion

## Compilazione

### Compilazione del PDF

#### Metodo 1: pdflatex (consigliato)

```bash
# Prima compilazione (genera indici)
pdflatex main.tex

# Seconda compilazione (aggiorna riferimenti)
pdflatex main.tex

# Terza compilazione (finalizza tutto)
pdflatex main.tex
```

**Nota**: Sono necessarie 2-3 compilazioni per generare correttamente l'indice dei contenuti, l'elenco delle figure e l'elenco dei codici.

#### Metodo 2: latexmk (automatico)

```bash
latexmk -pdf main.tex
```

Questo comando esegue automaticamente tutte le compilazioni necessarie.

#### Pulizia file temporanei

```bash
# Rimuovi file ausiliari
rm -f *.aux *.log *.out *.toc *.lof *.lol *.fls *.fdb_latexmk *.synctex.gz

# Rimuovi anche nei capitoli
rm -f capitoli/*.aux
```

### Compilazione ed esecuzione codice C

```bash
# Compilare un programma
gcc programma.c -o programma

# Eseguire il programma
./programma
```

### Visualizzazione del PDF

Il file compilato `main.pdf` può essere aperto con qualsiasi lettore PDF:
- **Linux**: Evince, Okular
- **macOS**: Preview, Skim
- **Windows**: Adobe Acrobat Reader, Sumatra PDF

## Come usare gli appunti

### Per lo studente

1. **Leggi il capitolo**: Inizia dagli obiettivi di apprendimento
2. **Studia gli esempi**: Digita personalmente il codice, non copiare-incollare
3. **Compila ed esegui**: Verifica che il codice funzioni
4. **Sperimenta**: Modifica gli esempi per comprenderne il funzionamento
5. **Risolvi gli esercizi**: Prova prima autonomamente, poi consulta le soluzioni
6. **Ripassa**: Usa il riepilogo alla fine di ogni capitolo

### Livelli degli esercizi

- **Base**: Applicazione diretta dei concetti
- **Intermedio**: Combinazione di più concetti
- **Avanzato**: Problemi complessi che richiedono ragionamento

## Caratteristiche del materiale

### Box informativi

Il documento usa box colorati per evidenziare informazioni importanti:

- **Attenzione** (arancione): Punti critici e concetti da ricordare
- **Nota** (blu): Suggerimenti e best practices
- **Errore Comune** (rosso): Errori frequenti da evitare

### Codice sorgente

Tutti gli esempi di codice:
- Sono sintatticamente corretti e testati
- Includono commenti esplicativi in italiano
- Seguono le convenzioni C standard
- Sono accompagnati da spiegazioni dettagliate

### Diagrammi e figure

Il documento include:
- Diagrammi di flusso per algoritmi
- Schemi per la gestione della memoria
- Tabelle comparative
- Rappresentazioni visive di concetti complessi

## Convenzioni utilizzate

### Nomenclatura

- **Variabili e funzioni**: snake_case o camelCase (es. `numero_studenti`, `numeroStudenti`)
- **Costanti**: MAIUSCOLO_UNDERSCORE (es. `MAX_STUDENTI`, `PI_GRECO`)
- **Macro**: MAIUSCOLO_UNDERSCORE (es. `DEBUG_MODE`)

### Terminologia

- Si preferisce l'italiano quando possibile
- I termini tecnici consolidati rimangono in inglese (pointer, struct, array)
- Le parole chiave C sono sempre in inglese e formattate come codice

## Contribuire

Se trovi errori o hai suggerimenti:

1. Annota la pagina e la sezione specifica
2. Descrivi l'errore o il miglioramento proposto
3. Se possibile, fornisci una correzione

## Licenza

Questo materiale è distribuito per scopi didattici.

## Autore

Materiale didattico per il corso di Programmazione C
Istituto Tecnico - Anno Scolastico 2025-2026

---

## Riferimenti utili

### Documentazione e guide

- [C Reference](https://en.cppreference.com/w/c)
- [The C Programming Language](https://www.amazon.it/C-Programming-Language-2nd/dp/0131103628) - Kernighan & Ritchie (K&R)
- [C Tutorial - Learn C](https://www.learn-c.org/)

### Strumenti online

- [Online GDB](https://www.onlinegdb.com/online_c_compiler) - Compilatore C online
- [Compiler Explorer](https://godbolt.org/) - Visualizza assembly generato
- [StackOverflow](https://stackoverflow.com/questions/tagged/c) - Community di supporto

### Libri consigliati

- "The C Programming Language" - Brian W. Kernighan, Dennis M. Ritchie
- "C Programming: A Modern Approach" - K. N. King
- "C Primer Plus" - Stephen Prata
- "Expert C Programming: Deep C Secrets" - Peter van der Linden

---

**Data ultimo aggiornamento**: 8 Novembre 2025

**Versione documento**: 1.0 - COMPLETO

**Stato**: ✅ PROGETTO COMPLETATO - Tutti i 11 capitoli + appendici

---

## Collegamento con Quarta (Java)

Il materiale Terza prepara efficacemente per il corso Java:
- **Sintassi procedurale**: Base per OOP
- **Gestione memoria**: Contrasto con garbage collection Java
- **Puntatori**: Preparazione per i riferimenti Java
- **Funzioni**: Preparazione per i metodi
- **Struct**: Preparazione per le classi
