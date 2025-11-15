# Appunti di HTML e CSS - 4° Anno

Corso completo di HTML5, CSS3, SCSS e JavaScript per lo sviluppo web moderno.

---

## Descrizione

Materiale didattico organizzato come guida pratica interattiva per il web. Copre i fondamenti di HTML5, CSS3, SCSS e JavaScript, con focus su creazione di pagine web responsive, accessibili e interattive. Include esercizi pratici completi e progetti guidati.

**Stato**: Versione 1.0+ Completa (12 capitoli con 4 progetti dettagliati). Vedi [PIANO_SVILUPPO.md](PIANO_SVILUPPO.md) per espansioni future.

**PDF**: main.pdf (796 KB, 103 pagine)

---

## Argomenti trattati

### HTML Fondamentali
- Struttura documento HTML5
- Tag semantici e organizzazione
- Form e input
- Attributi globali
- Accessibilità base (WCAG)

### CSS Base e Avanzato
- Selettori e specificity
- Modello a blocchi (box model)
- Flexbox e Grid
- Responsive design (mobile-first)
- Animazioni e transizioni

### Preprocessori (SASS/SCSS)
- Variabili e nesting
- Mixin e funzioni
- Import e modularità
- Compilazione SCSS→CSS

### JavaScript Essenziale
- Variabili, tipi e funzioni
- Manipolazione del DOM
- Event listeners
- Array e oggetti
- Fetch API e async/await

### JavaScript Avanzato
- Promise e callback
- LocalStorage
- Classi e OOP
- Debouncing e throttling
- Moduli ES6

### Framework e Deployment
- Introduzione React e Vue
- Netlify e Vercel
- GitHub Pages
- Ottimizzazione performance
- SEO basics

---

## 🤖 Descrittori AI

Il corso è supportato da **15 descrittori AI** che sintetizzano i concetti chiave per ogni capitolo, facilitando la generazione automatica di esercizi e verifiche.

### Distribuzione Descrittori

**Totale**: 15 descrittori | **Coverage**: ~95% del materiale | **Data generazione**: 14 Nov 2025

#### Per Argomento
- **HTML Fondamentali** (3): Semantica, Form HTML5, Input Types + Accessibilità
- **CSS Base** (2): Selettori CSS, Pseudo-classi
- **CSS Avanzato** (4): Box Model, Flexbox, Grid, Responsive Design
- **SCSS** (2): Variabili & Nesting, Mixins
- **JavaScript** (3): DOM Manipulation, Event Handling, Fetch API & Async/Await

#### Elenco Descrittori
1. **HTML-SEM-001**: HTML Semantico (tag semantici, struttura logica)
2. **HTML-FORM-001**: Form HTML5 (raccolta dati, method GET/POST)
3. **HTML-INPUT-001**: Input Types HTML5 (email, number, date, checkbox, radio)
4. **HTML-ACCESSO-001**: Accessibilità HTML (alt tag, ARIA, screen reader)
5. **CSS-SEL-001**: Selettori CSS (elemento, classe, ID, attributo, specificity)
6. **CSS-PSEUDO-001**: Pseudo-classi CSS (:hover, :focus, :nth-child)
7. **CSS-BOX-001**: Box Model CSS (margin, padding, border, box-sizing)
8. **CSS-FLEX-001**: Flexbox Layout (flex-direction, justify-content, align-items)
9. **CSS-GRID-001**: CSS Grid Layout (grid-template-columns, fr unit)
10. **CSS-RESP-001**: Design Responsivo (mobile-first, @media queries, viewport)
11. **SCSS-VAR-001**: SCSS Variabili e Nesting (variabili, nesting, organizzazione)
12. **SCSS-MIX-001**: SCSS Mixins (mixin parametrici, riutilizzabilità)
13. **JS-DOM-001**: DOM Manipulation (querySelector, classList, appendChild)
14. **JS-EVENT-001**: Event Handling (addEventListener, delegation, preventDefault)
15. **JS-FETCH-001**: Fetch API e Async/Await (Promise, async/await, JSON parsing)

### File Generati
- `HTMLCSS_DESCRIPTORS_REPORT.json` - Report completo con spiegazioni e code examples
- `HTMLCSS_COVERAGE_ANALYSIS.md` - Analisi dettagliata della copertura per capitolo

### Utilizzo Descrittori
I descrittori includono:
- Spiegazione del concetto
- Codice di esempio funzionante
- Errori comuni da evitare
- Best practices e learning objectives
- Concetti correlati per approfondimento

---

## Struttura del progetto

```
HTMLCSS/
├── README.md                    # Questo file (descrizione corso)
├── TODO.md                      # Task attuali e priorità
├── PIANO_SVILUPPO.md            # Roadmap futura e argomenti
├── main.tex                     # File LaTeX principale
├── main.pdf                     # PDF compilato
├── capitoli/                    # Contenuti LaTeX
│   ├── 00_prefazione.tex
│   ├── 01_intro_html.tex
│   ├── 02_tag_blocco_riga.tex
│   ├── 03_form_input.tex
│   ├── 04_css_base.tex
│   ├── 05_flexbox_grid.tex
│   ├── 06_responsive.tex
│   ├── 07_sass_scss.tex
│   ├── 08_esercizi.tex
│   ├── 09_javascript_basics.tex
│   ├── 10_javascript_avanzato.tex
│   ├── 11_framework_deployment.tex
│   └── 12_bibliografia.tex
├── immagini/                    # Risorse grafiche
└── logs/                        # Log di aggiornamento
```

---

## Obiettivi di apprendimento

Al termine del corso lo studente sarà in grado di:

1. Strutturare correttamente documenti HTML5 semantici
2. Applicare CSS per styling e layout avanzati
3. Creare form funzionali e accessibili
4. Implementare design responsive e mobile-first
5. Usare Flexbox e CSS Grid per layout moderni
6. Lavorare con SASS/SCSS per CSS modulare e mantenibile
7. Scrivere JavaScript per interattività web
8. Manipolare il DOM e gestire eventi
9. Lavorare con API async/await e Fetch
10. Deployare siti web su piattaforme cloud (Netlify, Vercel)
11. Ottimizzare pagine web (performance, accessibilità, SEO)

---

## Requisiti tecnici

### Per seguire il corso
- **Editor di testo**: VS Code, Sublime Text, Atom
- **Browser moderno**: Chrome, Firefox, Safari (ultima versione)
- **Node.js** (facoltativo): Per compilare SCSS
- **LaTeX**: Per compilare il PDF degli appunti

### Per compilare il PDF LaTeX
```bash
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
```

O automaticamente:
```bash
latexmk -pdf main.tex
```

---

## Come usare il materiale

### Per lo studente

1. **Leggi la teoria**: Inizia dagli obiettivi di apprendimento
2. **Scrivi il codice**: Copia gli esempi in editor e browser
3. **Sperimenta**: Modifica gli attributi per vedere gli effetti
4. **Completa gli esercizi**: Prova autonomamente prima di controllare soluzioni
5. **Crea progetti**: Applica i concetti in pagine reali
6. **Ripassa**: Usa i riepiloghi alla fine di ogni sezione

### Per l'insegnante

- Adatta il contenuto al ritmo della classe
- Usa gli esercizi come verifiche formative
- Proposte di progetti pratici da svolgere in laboratorio
- Condividi link a risorse esterne

---

## Caratteristiche del materiale

### Box informativi

Evidenziano informazioni importanti:

- **Attenzione** (arancione): Punti critici, compatibilità browser
- **Nota** (blu): Best practices, suggerimenti
- **Errore Comune** (rosso): Errori frequenti da evitare

### Codice di esempio

Tutti gli esempi:
- Sono funzionanti e testati nei browser
- Includono commenti esplicativi in italiano
- Seguono convenzioni HTML/CSS moderne
- Sono accompagnati da spiegazioni visive

### Responsività e Accessibilità

- Focus su mobile-first design
- WCAG 2.1 AA compliance
- Semantica HTML corretta
- Testing su diversi dispositivi

---

## Convenzioni utilizzate

### Nomenclatura

- **Classi CSS**: `kebab-case` (es. `header-main`, `card-content`)
- **ID**: `camelCase` (es. `mainMenu`, `heroSection`)
- **Variabili SCSS**: `$camelCase` (es. `$colorPrimary`, `$spacingBase`)
- **Mixin SCSS**: `@mixin nomeMinuscolo` (es. `@mixin flexCenter`)

### Terminologia

- Italiano quando possibile
- Termini tecnici consolidati rimangono in inglese (flex, grid, viewport)
- Nomi di proprietà CSS sempre in inglese

---

## Compilazione e Visualizzazione

### PDF LaTeX

```bash
# Prima compilazione (genera indici)
pdflatex main.tex

# Seconda compilazione (aggiorna riferimenti)
pdflatex main.tex

# Terza compilazione (finalizza tutto)
pdflatex main.tex
```

**Nota**: Sono necessarie 2-3 compilazioni per generare correttamente l'indice dei contenuti.

### Pulizia file temporanei

```bash
# Rimuovi file ausiliari
rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz

# Rimuovi anche nei capitoli
rm -f capitoli/*.aux
```

---

## Strumenti consigliati

### Editor e IDE
- **VS Code**: Extensioni (HTML/CSS, Live Server)
- **Sublime Text**: Package manager + syntax
- **WebStorm**: IDE completo per web

### Browser DevTools
- Chrome DevTools (F12)
- Firefox Developer Edition
- Safari Web Inspector

### Validazione
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [WebAIM WCAG Checker](https://wave.webaim.org/)

---

## Esercizi e Progetti

### Livelli di difficoltà

- **Base**: Applicazione diretta dei tag/proprietà
- **Intermedio**: Combinazione di più concetti (form + CSS)
- **Avanzato**: Progetti completi (sito multi-pagina, responsive)

### Progetti Guidati (Inclusi)

1. **Blog Personale** (Cap. 01) - HTML5 semantico con articoli
2. **Card Portfolio** (Cap. 04) - Styling CSS con hover effects
3. **Todo List Interattiva** (Cap. 09) - JavaScript con DOM manipulation
4. **E-commerce Landing** (Cap. 08) - Progetto completo con Flexbox/Grid
5. **Blog Responsivo** (Cap. 08) - Layout SCSS modularizzato
6. **Dashboard Admin** (Cap. 08) - Integrazione HTML/CSS/JavaScript

---

## Risorse esterne

### Documentazione
- [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [W3C Specifications](https://www.w3.org/Style/CSS/)

### Tutorial e Playground
- [CodePen](https://codepen.io/) - Condividi pen/progetti
- [JsFiddle](https://jsfiddle.net/) - Esperimenti rapidi
- [CSS-Tricks](https://css-tricks.com/) - Articoli approfonditi

### Tool Online
- [Sass Playground](https://www.sassmeister.com/)
- [Can I Use](https://caniuse.com/) - Compatibilità browser

---

## File di riferimento

- **[TODO.md](TODO.md)**: Task attuali, capitoli da scrivere, priorità
- **[PIANO_SVILUPPO.md](PIANO_SVILUPPO.md)**: Roadmap, struttura capitoli, timeline
- **logs/**: Log compilazione e aggiornamenti

---

## Contribuire

Se trovi errori o hai suggerimenti:

1. Specifica la sezione e l'errore
2. Suggerisci una correzione
3. Se possibile, fornisci lo screenshot

---

## Collegamento con Terza (C) e Quarta (Java)

Questo corso web completa la formazione tecnica:
- **Terza**: Linguaggio C per logica procedurale e programmazione a basso livello
- **Quarta-Part1**: Java Avanzato per OOP, design patterns e backend
- **Quarta-Part2**: HTML5, CSS3, JavaScript per frontend web moderno

Insieme formano un percorso didattico coerente che spazia dalla programmazione strutturata al web development completo.

---

## Statistiche Corso

| Metrica | Valore |
|---------|--------|
| **Capitoli** | 12 |
| **Pagine PDF** | 70 |
| **Esercizi** | 24+ |
| **Progetti Guidati** | 6 |
| **Esempi di Codice** | 100+ |
| **Box Informativi** | 50+ |

---

**Versione**: 1.0 Completa | **Aggiornato**: 8 Novembre 2025 | **Autore**: Istituto Tecnico Antonio Scarpa ITS - 4AIT
