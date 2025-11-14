# Piano di Sviluppo - HTML e CSS

**Versione**: 1.0 (In Sviluppo)
**Data**: 8 Novembre 2025
**Status**: 🚀 Fase 1 - Fondamenti

---

## Stato Attuale

### Completamento
```
Capitoli LaTeX:      0/10 (0%)
Esercizi:            0/20+ (0%)
Progetti guidati:    0/4 (0%)
PDF compilato:       NO
```

---

## FASE 1 - Fondamenti HTML e CSS (ALTA PRIORITÀ)

**Timeline**: Settimane 1-2
**Obiettivo**: Insegnare struttura HTML5 e CSS base

### 00_prefazione.tex
**Argomenti**: Intro corso, obiettivi, requisiti
**Esercizi**: -
**Pagine stimate**: 2-3

### 01_intro_html.tex
**Argomenti**: Struttura HTML5, semantica, meta tag, DOCTYPE
**Esercizi**: 2 (base, intermedio)
**Cross-reference**: Java classi/oggetti (\ref{cap:classi_oggetti_ereditarieta})
**Pagine stimate**: 4-5

### 02_tag_blocco_riga.tex
**Argomenti**: Tag blocco vs inline, layout semplice, display CSS
**Esercizi**: 2 (base, intermedio)
**Pagine stimate**: 4

### 03_form_input.tex
**Argomenti**: Form, input types, validazione HTML5, label e accessibilità
**Esercizi**: 2 (base, intermedio)
**Pagine stimate**: 5

### 04_css_base.tex
**Argomenti**: Selettori CSS, specificity, box model, unità di misura
**Esercizi**: 3 (base, intermedio, avanzato)
**Pagine stimate**: 6

---

## FASE 2 - Layout Avanzato (MEDIA PRIORITÀ)

**Timeline**: Settimane 3-4
**Obiettivo**: Insegnare layout responsive moderno

### 05_flexbox_grid.tex
**Argomenti**: Flexbox container/item, CSS Grid, layout responsive
**Esercizi**: 3 (base, intermedio, avanzato)
**Pagine stimate**: 6

### 06_responsive.tex
**Argomenti**: Media queries, mobile-first, breakpoints (320px, 768px, 1024px)
**Esercizi**: 3 (base, intermedio, avanzato)
**Pagine stimate**: 6

### 07_sass_scss.tex
**Argomenti**: Variabili SCSS, nesting, mixin e funzioni, compilazione
**Esercizi**: 2 (base, intermedio)
**Pagine stimate**: 5

---

## FASE 3 - Esercizi e Progetti (BASSA PRIORITÀ)

**Timeline**: Settimana 5+

### 08_esercizi.tex
**Contenuti**: 20+ esercizi totali
**Livelli**: base, intermedio, avanzato
**Progetti guidati**:
1. Portfolio Personale (Cap. 01-04)
2. E-commerce Landing (Cap. 05-06)
3. Blog Responsivo (Cap. 07)
4. Dashboard Admin (Integrazione 01-07)
**Pagine stimate**: 20-30

### 99_bibliografia.tex
**Contenuti**: Risorse, link MDN, tutorial, tool online
**Pagine stimate**: 2-3

---

## Struttura LaTeX

```latex
\chapter{Titolo Capitolo}
\label{cap:nome_capitolo}

\section{Sezione 1}
Testo esplicativo...

\subsection{Sottosezione}
Più dettagli...

\begin{lstlisting}[language=HTML]
<!-- Codice di esempio -->
\end{lstlisting}

\begin{attenzione}
Punto critico
\end{attenzione}

\begin{nota}
Best practice
\end{nota}

\section{Esercizi}
\subsection{Esercizio 1 (Base)}
...
\subsection{Esercizio 2 (Intermedio)}
...

\section{Riepilogo}
\begin{itemize}
  \item Punto 1
  \item Punto 2
\end{itemize}
```

---

## Mapping HTML/CSS ↔ Java/C

| Concetto Java | Equivalente HTML/CSS | Equivalente C |
|---|---|---|
| Classe | Tag + classe HTML | struct |
| Attributi | Attributi HTML + proprietà CSS | campi struct |
| Metodi | Funzioni SCSS (@mixin) | funzioni |
| Ereditarietà | @extend CSS, cascade | - |
| Polimorfismo | Media queries, CSS overrides | - |

---

## Checklist di Completamento Globale

### Fase 1 (Fondamenti)
- [ ] 5 capitoli completati
- [ ] Almeno 10 esercizi creati
- [ ] Almeno 15 esempi di codice
- [ ] All cross-reference a Java/C aggiunti
- [ ] main.pdf compilato e valido
- [ ] Indice generato correttamente

### Fase 2 (Layout Avanzato)
- [ ] 3 capitoli completati
- [ ] Almeno 8 esercizi creati
- [ ] Almeno 15 esempi di codice
- [ ] Testing breakpoint responsivo

### Fase 3 (Esercizi/Progetti)
- [ ] Capitolo esercizi completato
- [ ] 4 progetti guidati descritti
- [ ] Bibliografia completa

---

## Statistiche Finali Stimate

```
Capitoli LaTeX:        10 file
Pagine totali:         150-200
Esercizi:              20+ esercizi
Progetti:              4 progetti
Esempi di codice:      30+ esempi
Immagini/diagrammi:    10+ risorse
Tempo stima:           5-7 settimane (full-time)
```

---

## Timeline Suggerita

| Settimana | Milestone | Deliverables |
|-----------|-----------|---|
| 1 | Capitoli 01-02 | Bozza LaTeX completata |
| 2 | Capitoli 03-04 | Fondamenti OK |
| 3 | Capitoli 05-06 | Layout avanzato OK |
| 4 | Capitolo 07 | SCSS completato |
| 5 | Capitolo 08 | Esercizi e progetti |
| 6 | Revisione | Cross-reference, indice |
| 7 | Finalizzazione | PDF compilato e testato |

---

## Risorse Esterne Utilizzate

### Documentazione
- [MDN HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [W3C CSS Specifications](https://www.w3.org/Style/CSS/)
- [Can I Use](https://caniuse.com/)

### Playground
- [CodePen](https://codepen.io/)
- [JSFiddle](https://jsfiddle.net/)
- [Sass Compiler](https://www.sassmeister.com/)

---

**Prossimo Aggiornamento**: Dopo creazione primi 5 capitoli
**Responsabile**: Docente/Sviluppatore
**Versione**: 1.0 | **Data**: 8 Novembre 2025
