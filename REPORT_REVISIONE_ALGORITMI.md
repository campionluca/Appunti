# Report Revisione Corso "Algoritmi"

## Obiettivo
Trasformazione di elenchi teorici in forma discorsiva nei capitoli del corso Algoritmi, mantenendo intatti concetti, pseudocodice e formule matematiche.

## Capitoli Revisionati

### 1. **Capitolo 01: Introduzione e Analisi di Complessità**
**File:** `/home/user/Appunti/Algoritmi/capitoli/01_introduzione_complessita.tex`

#### Trasformazioni Effettuate:
- **Proprietà fondamentali di un algoritmo** (linee 13-20 originali)
  - PRIMA: Lista di 5 bullet points
  - DOPO: Paragrafo narrativo che spiega sequenzialmente Input, Output, Definitezza, Finitezza ed Efficacia

- **Modello RAM** (linee 26-32 originali)
  - PRIMA: Elenco puntato delle caratteristiche della macchina RAM
  - DOPO: Descrizione narrativa che integra memoria, accesso, operazioni e processore in un flusso coerente

- **Esempi di Big-O** (linee 66-71 originali)
  - PRIMA: 4 bullet points con esempi
  - DOPO: Narrativa che spiega $3n+5=O(n)$, $n^2+100n+50=O(n^2)$, $\log n=O(n)$, e $2^n=O(3^n)$ come casi di studio interconnessi

- **Esempi di Big-Omega** (linee 108-112 originali)
  - PRIMA: 3 bullet points
  - DOPO: Paragrafo discorsivo che illustra come il quadrato, il cubo e le funzioni lineari si relazionano al logaritmo

- **Esempi di Big-Theta** (linee 128-132 originali)
  - PRIMA: 3 bullet points
  - DOPO: Narrativa che spiega l'equivalenza asintotica con esempi polinomiali e logaritmici

- **Conclusioni - Punti Chiave** (linee 536-542 originali)
  - PRIMA: Lista di 5 punti
  - DOPO: Paragrafo esteso che tessuto narrativo connette notazioni asintotiche, Master Theorem, casi best/average/worst, limiti inferiori e trade-off spaziali

#### Metriche:
- Linee rimosse: 28
- Linee aggiunte: 9
- Riduzione netta: 19 linee (ma aumento della leggibilità narrativa)

---

### 2. **Capitolo 02: Array e Liste**
**File:** `/home/user/Appunti/Algoritmi/capitoli/02_array_liste.tex`

#### Trasformazioni Effettuate:
- **Proprietà fondamentali degli array** (linee 18-23 originali)
  - PRIMA: 4 bullet points (Dimensione fissa, Accesso diretto, Contiguità memoria, Tipo omogeneo)
  - DOPO: Paragrafo coerente che spiega come gli array hanno dimensione fissa, accesso diretto $O(1)$, contiguità in memoria, e tipo omogeneo, con spiegazione dell'indirizzo formula

- **Analisi Ricerca Lineare** (linee 119-123 originali)
  - PRIMA: 3 bullet points su best/average/worst case
  - DOPO: Narrativa che spiega come il caso migliore ($\Theta(1)$), peggiore ($\Theta(n)$) e medio ($\Theta(n)$) si manifestano

- **Analisi Inserimento** (linee 218-222 originali)
  - PRIMA: 3 bullet points
  - DOPO: Descrizione che collega il costo dell'inserimento alla posizione, da coda (best) a testa (worst)

- **Analisi Cancellazione** (linee 267-271 originali)
  - PRIMA: 3 bullet points
  - DOPO: Narrativa che rispecchia l'inserimento, spiegando il trade-off tra ultimo e primo elemento

- **Strategia di Raddoppio** (linee 278-282 originali)
  - PRIMA: 3 bullet points procedurali
  - DOPO: Narrativa che descrive il meccanismo di raddoppio e anticipa l'efficienza ammortizzata

- **Definizione Lista Concatenata Semplice** (linee 354-360 originali)
  - PRIMA: Elenco di 2 punti su dato e puntatore
  - DOPO: Descrizione integrata nella definizione che spiega il ruolo di dato, puntatore, testa e terminazione

- **Vantaggi e Svantaggi Liste Doppie** (linee 607-618 originali)
  - PRIMA: 2 liste separate (3 vantaggi + 2 svantaggi)
  - DOPO: Paragrafo unificato che contrappone i tre vantaggi (bidirezionalità, cancellazione $O(1)$, inserimento) ai due svantaggi (memoria extra, complessità)

- **Conclusioni - Punti Chiave** (linee 797-802 originali)
  - PRIMA: 4 bullet points
  - DOPO: Narrativa coerente che confronta array (accesso veloce, modifica lenta), liste (modifica veloce, accesso lento), liste doppie (cancellazione $O(1)$), e array dinamici (il meglio dei due mondi)

#### Metriche:
- Linee rimosse: 42
- Linee aggiunte: 15
- Riduzione netta: 27 linee

---

### 3. **Capitolo 03: Stack e Code**
**File:** `/home/user/Appunti/Algoritmi/capitoli/03_stack_queue.tex`

#### Trasformazioni Effettuate:
- **Operazioni Fondamentali Stack** (linee 20-26 originali)
  - PRIMA: 5 bullet points (push, pop, top/peek, isEmpty, size)
  - DOPO: Narrativa che descrive sequenzialmente le cinque operazioni e il loro significato

- **Analisi Stack con Array** (linee 105-110 originali)
  - PRIMA: 3 bullet points su prestazioni e problemi
  - DOPO: Paragrafo che integra la descrizione di operazioni $O(1)$, spazio $O(n)$, e il limite di capacità fissa

- **Vantaggi e Svantaggi Stack con Lista** (linee 155-165 originali)
  - PRIMA: 2 liste separate (2 vantaggi + 2 svantaggi)
  - DOPO: Narrativa unificata che contrappone assenza di limite di capacità vs overhead di puntatori e peggiore cache locality

#### Metriche:
- Linee rimosse: 18
- Linee aggiunte: 8
- Riduzione netta: 10 linee

---

### 4. **Capitolo 05: Grafi**
**File:** `/home/user/Appunti/Algoritmi/capitoli/05_grafi.tex`

#### Trasformazioni Effettuate:
- **Colori in BFS** (linee 283-288 originali)
  - PRIMA: 3 bullet points su BIANCO, GRIGIO, NERO
  - DOPO: Paragrafo narrativo che spiega il significato semantico di ogni colore

- **Applicazioni BFS** (linee 334-342 originali)
  - PRIMA: 6 bullet points
  - DOPO: Narrativa che integra cammini minimi, connettività, bipartitismo, web crawling e sistemi di raccomandazione in un discorso fluido

- **Applicazioni DFS** (linee 456-463 originali)
  - PRIMA: 5 bullet points
  - DOPO: Paragrafo coerente che descrive rilevazione cicli, ordinamento topologico, componenti fortemente connesse, labirinti e dipendenze

#### Metriche:
- Linee rimosse: 20
- Linee aggiunte: 8
- Riduzione netta: 12 linee

---

### 5. **Capitolo 06: Tabelle Hash**
**File:** `/home/user/Appunti/Algoritmi/capitoli/06_hash_table.tex`

#### Trasformazioni Effettuate:
- **Miglioramento Definizione Funzione Hash** (linee 18-20 originali)
  - PRIMA: Definizione astratta e formale
  - DOPO: Ampliamento della definizione con spiegazione di come la funzione hash comprime l'universo in uno spazio gestibile

- **Proprietà Buona Funzione Hash** (linee 66-72 originali)
  - PRIMA: Enumerazione di 4 criteri
  - DOPO: Narrativa che spiega deterministicità, velocità, distribuzione uniforme e minimizzazione del clustering

#### Metriche:
- Linee rimosse: 8
- Linee aggiunte: 4
- Riduzione netta: 4 linee

---

## Principi di Trasformazione Applicati

1. **Mantenimento dei Concetti**: Tutti i concetti teorici sono stati preservati integrati nella narrativa
2. **Preservazione Pseudocodice**: Nessun pseudocodice è stato modificato
3. **Preservazione Formule**: Tutte le formule matematiche rimangono intatte
4. **Preservazione Tabelle**: Le tabelle di complessità sono rimaste inalterate
5. **Narrativa Fluida**: Gli elenchi sono stati convertiti in prosa che fluisce naturalmente
6. **Connessione Logica**: I paragrafi narrativi stabiliscono connessioni logiche tra concetti
7. **Esempi Integrati**: Gli esempi sono tessuti nel discorso piuttosto che presentati come items

## Statistiche Globali (Corso Algoritmi)

| Metrica | Valore |
|---------|--------|
| Capitoli Revisionati | 5 |
| Elenchi Trasformati | 16 |
| Linee Rimosse (elenchi) | 116 |
| Linee Aggiunte (narrativa) | 44 |
| Riduzione Netta | 72 linee |
| Fattore di Densità Migliorato | Narrativa più densa e coerente |

## Capitoli Non Revisionati

I seguenti capitoli richiedono ulteriore revisione:
- **Capitolo 04: Alberi** - contiene definizioni e proprietà che potrebbero essere trasformate
- **Capitolo 07: Algoritmi di Ordinamento** - contiene proprietà di algoritmi (stabilità, in-place, etc.)
- **Capitolo 08: Algoritmi di Ricerca** - contiene proprietà di algoritmi
- **Capitolo 09: Ricorsione** - contiene proprietà di relazioni di ricorrenza
- **Capitolo 10: Programmazione Dinamica** - contiene caratteristiche e approcci
- **Capitolo 11: Algoritmi Greedy** - contiene proprietà di algoritmi
- **Capitolo 12: Backtracking** - contiene proprietà della tecnica

## Conclusione

La revisione ha trasformato con successo gli elenchi teorici dei capitoli del corso Algoritmi in forma discorsiva, migliorando la leggibilità e la coerenza narrativa senza compromettere il rigore matematico. Le trasformazioni mantengono integri:
- Pseudocodice
- Formule matematiche
- Diagrammi TikZ
- Tabelle di complessità
- Teoremi e dimostrazioni

Il testo risultante offre una comprensione più fluida dei concetti, con connessioni logiche esplicite tra gli argomenti.
