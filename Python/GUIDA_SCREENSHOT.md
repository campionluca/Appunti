# Guida Integrazione Screenshot nel LaTeX

## Screenshot Generati

### Terminale (9 screenshot)
- `terminal_01_hello_world.png` - Hello World
- `terminal_02_variabili.png` - Variabili e tipi
- `terminal_03_if_else.png` - If-Else
- `terminal_04_comprehension.png` - List comprehension
- `terminal_05_dizionari.png` - Dizionari
- `terminal_06_fstrings.png` - F-Strings
- `terminal_07_json.png` - JSON
- `terminal_08_try_except.png` - Try-Except
- `terminal_09_oop.png` - Classi OOP

## Verifica Leggibilità

✅ **100% degli screenshot sono leggibili**
- Dimensioni: 800x600 px
- Contrasto: 156 (ottimo)
- Testo rilevato: OCR funziona correttamente

## Come Integrare in LaTeX

### 1. Includere singolo screenshot

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{immagini/screenshots/terminal_01_hello_world.png}
    \caption{Output esempio Hello World}
    \label{fig:hello-world}
\end{figure}
```

### 2. Screenshot affiancati

```latex
\begin{figure}[H]
    \centering
    \begin{subfigure}{0.48\textwidth}
        \includegraphics[width=\textwidth]{immagini/screenshots/terminal_01_hello_world.png}
        \caption{Hello World}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.48\textwidth}
        \includegraphics[width=\textwidth]{immagini/screenshots/terminal_02_variabili.png}
        \caption{Variabili}
    \end{subfigure}
    \caption{Esempi fondamenti Python}
\end{figure}
```

### 3. Screenshot inline con testo

```latex
Il seguente esempio mostra l'output del programma:

\begin{center}
    \includegraphics[width=0.7\textwidth]{immagini/screenshots/terminal_03_if_else.png}
\end{center}

Come si può vedere, il programma gestisce correttamente...
```

### 4. Screenshot con bordo

```latex
\begin{figure}[H]
    \centering
    \fbox{\includegraphics[width=0.75\textwidth]{immagini/screenshots/terminal_04_comprehension.png}}
    \caption{List comprehension con bordo}
\end{figure}
```

### 5. Screenshot in minipage

```latex
\begin{minipage}{0.5\textwidth}
    \textbf{Codice:}
    \begin{lstlisting}[language=Python]
numeri = [1, 2, 3, 4, 5]
quadrati = [x**2 for x in numeri]
print(quadrati)
    \end{lstlisting}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
    \textbf{Output:}
    \includegraphics[width=\textwidth]{immagini/screenshots/terminal_04_comprehension.png}
\end{minipage}
```

## Pacchetti LaTeX Necessari

Aggiungi al preambolo di `main.tex`:

```latex
\usepackage{graphicx}     % Per includere immagini
\usepackage{float}        % Per posizionamento [H]
\usepackage{caption}      % Per didascalie personalizzate
\usepackage{subcaption}   % Per subfigure
```

## Best Practices

1. **Dimensioni**: Usa `width=0.7\textwidth` o `0.8\textwidth` per screenshot orizzontali
2. **Posizionamento**: Usa `[H]` per posizione fissa, `[htbp]` per flessibile
3. **Qualità**: Gli screenshot sono PNG a 96 DPI, ottimali per il PDF
4. **Riferimenti**: Usa sempre `\label{}` e `\ref{}` per riferimenti incrociati

## Esempio Completo Capitolo

```latex
\chapter{Fondamenti Python}

\section{Il Primo Programma}

Iniziamo con il classico "Hello World":

\begin{lstlisting}[language=Python]
print("Hello, World!")
\end{lstlisting}

L'output del programma è mostrato nella figura \ref{fig:hello-world}:

\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\textwidth]{immagini/screenshots/terminal_01_hello_world.png}
    \caption{Output del programma Hello World}
    \label{fig:hello-world}
\end{figure}

Come si può vedere, Python stampa il messaggio a schermo.

\section{Variabili e Tipi}

Python supporta vari tipi di dato (figura \ref{fig:variabili}):

\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{immagini/screenshots/terminal_02_variabili.png}
    \caption{Esempi di variabili e tipi in Python}
    \label{fig:variabili}
\end{figure}
```

## Script Disponibili

### Genera Screenshot
```bash
python3 scripts/genera_screenshot_demo.py
```

### Verifica Leggibilità
```bash
python3 scripts/verifica_leggibilita.py immagini
```

### Verifica con Playwright (richiede installazione)
```bash
pip install playwright
playwright install chromium
python3 scripts/playwright_verifica_pdf.py --pdf main.pdf
```

## Posizioni Screenshot nel Libro

### Capitolo 0 - Fondamenti
- `terminal_01_hello_world.png` → Sezione 0.1
- `terminal_02_variabili.png` → Sezione 0.2

### Capitolo 1 - Controllo Flusso
- `terminal_03_if_else.png` → Sezione 1.1
- `terminal_04_comprehension.png` → Sezione 1.5

### Capitolo 3 - Strutture Dati
- `terminal_05_dizionari.png` → Sezione 3.2

### Capitolo 4 - Stringhe
- `terminal_06_fstrings.png` → Sezione 4.2

### Capitolo 5 - File I/O
- `terminal_07_json.png` → Sezione 5.4

### Capitolo 6 - Gestione Errori
- `terminal_08_try_except.png` → Sezione 6.1

### Capitolo 8 - OOP
- `terminal_09_oop.png` → Sezione 8.1

## Troubleshooting

### Screenshot non appare
- Verifica path relativo: `immagini/screenshots/...`
- Controlla che l'immagine esista
- Usa `\listfiles` per debug path

### Dimensioni sbagliate
- Usa `width=` invece di `scale=`
- Prova `\textwidth` invece di dimensioni assolute

### Qualità bassa nel PDF
- Gli screenshot sono già ottimizzati a 800x600
- Non usare `scale=` > 1
- Considera rigenerare a risoluzioni maggiori se necessario

## Rigenerare Screenshot

Per rigenerare a dimensioni diverse, modifica `genera_screenshot_demo.py`:

```python
self.width = 1024   # Era 800
self.height = 768   # Era 600
```

Poi riesegui:
```bash
python3 scripts/genera_screenshot_demo.py
```
