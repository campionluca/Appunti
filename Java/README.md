# Appunti di Programmazione Java - 4° Anno

Corso completo di Programmazione Java per l'Istituto Tecnico, A.S. 2025-2026.

---

## Descrizione

Materiale didattico organizzato in forma di libro LaTeX. Copre i fondamenti della programmazione orientata agli oggetti (OOP) fino a pattern architetturali avanzati.

**Stato**: 10 capitoli completati + appendice soluzioni. Per le roadmap di espansione vedi [PIANO_SVILUPPO.md](PIANO_SVILUPPO.md).

---

## Capitoli completati

| # | Titolo | Stato | Contenuto |
|---|--------|-------|----------|
| 00 | Classi, Oggetti, Ereditarietà e Package | ✅ | OOP foundations, packages, access modifiers |
| 01 | Stream e Buffer | ✅ | File I/O, readers/writers, try-with-resources |
| 02 | Interfacce e Classi Astratte | ✅ | Astrazione, polimorfismo, design principles |
| 03 | Eccezioni | ✅ | Error handling, custom exceptions, try-catch |
| 04 | ArrayList | ✅ | Collezioni dinamiche, iterazione, generics intro |
| 05 | Interfacce Grafiche | ✅ | Swing, layouts, event handling |
| 06 | Model View Controller | ✅ | Pattern MVC, separazione responsabilità |
| 07 | Lambda Expressions | ✅ | Programmazione funzionale, interfaces funzionali |
| 08 | Esercizi | ✅ | Raccolta integrata di problemi |
| App | Soluzioni | ✅ | Soluzioni commentate di tutti gli esercizi |

**Totale**: ~280-300 pagine compilate

---

## Struttura del progetto

```
Quarta/
├── README.md                           # Questo file (descrizione corso)
├── TODO.md                             # Task attuali e priorità
├── PIANO_SVILUPPO.md                   # Roadmap futura e argomenti
├── main.tex                            # File principale LaTeX
├── main.pdf                            # PDF compilato
├── capitoli/                           # Contenuti
│   ├── 00_classi_oggetti_ereditarieta.tex
│   ├── 01_stream_buffer.tex
│   ├── 02_interfacce_classi_astratte.tex
│   ├── 03_eccezioni.tex
│   ├── 04_arraylist.tex
│   ├── 05_interfacce_grafiche.tex
│   ├── 06_model_view_controller.tex
│   ├── 07_lambda_expressions.tex
│   ├── 08_esercizi.tex
│   ├── appendice_soluzioni.tex
│   └── 99_bibliografia.tex
├── immagini/                           # Risorse grafiche
└── logs/                               # Log di aggiornamento
```

---

## Obiettivi di apprendimento

Al termine del corso lo studente sarà in grado di:

1. ✅ Progettare classi con ereditarietà, package e access modifiers
2. ✅ Gestire file e flussi di dati con Stream e Buffer
3. ✅ Usare interfacce e classi astratte per l'astrazione
4. ✅ Implementare gestione robusta degli errori
5. ✅ Lavorare con collezioni dinamiche (ArrayList)
6. ✅ Creare interfacce grafiche interattive
7. ✅ Applicare il pattern MVC
8. ✅ Usare lambda expressions per codice funzionale

**Continuazione in PIANO_SVILUPPO.md**: Generics, Collections, Multithreading, Design Patterns, etc.

---

## Come usare il materiale

### Per lo studente
1. Leggi gli **obiettivi** di apprendimento del capitolo
2. **Studia** gli esempi (digita il codice, non copiare-incollare)
3. **Sperimenta** modificando gli esempi
4. **Risolvi** gli esercizi autonomamente
5. **Verifica** con le soluzioni nell'appendice
6. **Ripassa** con il riepilogo finale

### Per l'insegnante
- Adatta il contenuto al ritmo della classe
- Usa gli esercizi come verifiche formative
- Supplementa con progettini pratici da svolgere in laboratorio

---

## Requisiti tecnici

### Per compilare il PDF
- **LaTeX**: TeX Live, MiKTeX o MacTeX (distribuzione completa)
- **Pacchetti principali**: babel, geometry, listings, hyperref, tcolorbox, tikz, amsmath

### Per eseguire il codice
- **JDK 8+** (preferibilmente JDK 11 o superiore)
- **IDE**: IntelliJ IDEA, Eclipse, NetBeans o VS Code

---

## Compilazione rapida

```bash
# Metodo 1: pdflatex (3 passate)
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex

# Metodo 2: latexmk (automatico)
latexmk -pdf main.tex

# Pulizia file temporanei
rm -f *.aux *.log *.out *.toc *.lof *.lol *.fls *.fdb_latexmk *.synctex.gz capitoli/*.aux
```

Vedi [TODO.md](TODO.md) per task di build e manutenzione.

---

## Caratteristiche del materiale

- **Box informativi colorati**: Attenzione (arancione), Note (blu), Errori comuni (rosso)
- **Codice testato**: Tutti gli esempi sono funzionanti e commentati in italiano
- **Diagrammi UML**: Rappresentazioni visive di classi e relazioni
- **Esercizi graduati**: Base → Intermedio → Avanzato
- **Soluzioni complete**: Appendice con tutti i codici risolti

---

## Convenzioni

- **Classi**: `PascalCase` (es. `Studente`, `GestoreFile`)
- **Metodi/variabili**: `camelCase` (es. `calcolaMedia()`, `numeroStudenti`)
- **Costanti**: `MAIUSCOLO_UNDERSCORE` (es. `MAX_STUDENTI`)
- **Package**: `minuscolo.separato.punto` (es. `it.scuola.gestionale`)

---

## Risorse esterne

- [Oracle Java Documentation](https://docs.oracle.com/en/java/)
- [Java SE API](https://docs.oracle.com/en/java/javase/17/docs/api/)
- [JDoodle Compiler](https://www.jdoodle.com/online-java-compiler)

---

## File di riferimento

- **[TODO.md](TODO.md)**: Task attuali, bug da fixare, piccoli miglioramenti
- **[PIANO_SVILUPPO.md](PIANO_SVILUPPO.md)**: Roadmap futura, nuovi capitoli, enhancements
- **logs/**: Log di compilazione e aggiornamenti

---

**Versione**: 2.2 | **Aggiornato**: Novembre 2025 | **Autore**: Istituto Tecnico - 4AIT
