# 📘 Guida Compilazione PDF - Nuovi Corsi 2025

**Data**: 15 Novembre 2025
**Versione**: 1.0
**Status**: Pronti per compilazione

---

## ✅ Stato Preparazione Corsi

Tutti i 9 nuovi corsi sono pronti per la compilazione LaTeX:

| Corso | main.tex | Capitoli | Status | Priorità |
|-------|----------|----------|--------|----------|
| **Algoritmi** | ✅ 104 linee | 15 | Pronto | 🔴 ALTA |
| **Git** | ✅ 92 linee | 13 | Pronto | 🟡 Media |
| **Linux** | ✅ 92 linee | 13 | Pronto | 🟡 Media |
| **Docker** | ✅ 91 linee | 13 | Pronto | 🟡 Media |
| **React** | ✅ 94 linee | 15 | Pronto | 🔴 ALTA |
| **RestAPI** | ✅ 93 linee | 15 | Pronto | 🟡 Media |
| **WebSecurity** | ✅ 93 linee | 15 | Pronto | 🔴 ALTA |
| **Database** | ✅ 204 linee | 16 | Pronto | 🟡 Media |
| **Assembly** | ✅ 247 linee | 17 | Pronto | 🟡 Media |

**Totale**: 9 corsi | 136 capitoli | Tutti pronti per compilazione

---

## 🛠️ Requisiti Sistema

### Software Necessario

#### Linux/macOS
```bash
sudo apt-get install texlive-full          # Debian/Ubuntu
sudo yum install texlive-scheme-full       # RedHat/CentOS
brew install --cask mactex                 # macOS
```

#### Windows
- Installa **MiKTeX**: https://miktex.org/download
- Oppure **TeX Live**: https://tug.org/texlive/

### Pacchetti LaTeX Richiesti

Tutti i corsi utilizzano:
- `babel` (italiano)
- `geometry` (margini)
- `listings`, `listingsutf8` (codice)
- `hyperref` (link)
- `tcolorbox` (box colorati)
- `tikz`, `pgfplots` (diagrammi)
- `amsmath`, `amssymb` (matematica)
- `graphicx` (immagini)
- `xcolor` (colori)

---

## 📝 Comandi Compilazione

### Metodo 1: latexmk (Consigliato)

```bash
# Compilazione singola
cd Algoritmi
latexmk -pdf main.tex

# Pulizia file ausiliari
latexmk -c

# Pulizia completa (incluso PDF)
latexmk -C
```

### Metodo 2: pdflatex (3 passaggi)

```bash
cd Algoritmi
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
```

**Nota**: 3 passaggi sono necessari per:
1. Prima passata: genera struttura e riferimenti
2. Seconda passata: risolve riferimenti incrociati
3. Terza passata: finalizza indici e TOC

### Metodo 3: Script Automatico

Creare file `compile_all.sh`:

```bash
#!/bin/bash

CORSI=(
    "Algoritmi"
    "Database"
    "Assembly"
    "Git"
    "Linux"
    "Docker"
    "React"
    "RestAPI"
    "WebSecurity"
)

for corso in "${CORSI[@]}"; do
    echo "================================================"
    echo "Compilazione $corso..."
    echo "================================================"

    cd "$corso" || continue

    # Usa latexmk se disponibile, altrimenti pdflatex
    if command -v latexmk &> /dev/null; then
        latexmk -pdf -interaction=nonstopmode main.tex
    else
        pdflatex -interaction=nonstopmode main.tex
        pdflatex -interaction=nonstopmode main.tex
        pdflatex -interaction=nonstopmode main.tex
    fi

    # Verifica successo
    if [ -f "main.pdf" ]; then
        size=$(du -h main.pdf | cut -f1)
        echo "✅ $corso: PDF generato ($size)"
    else
        echo "❌ $corso: Errore compilazione"
    fi

    cd ..
done

echo "================================================"
echo "Compilazione completata!"
echo "================================================"
```

Esecuzione:
```bash
chmod +x compile_all.sh
./compile_all.sh
```

---

## 📋 Procedura Passo-Passo

### Per Ogni Corso

1. **Navigare nella directory**
   ```bash
   cd /home/user/Appunti/Algoritmi
   ```

2. **Verificare file main.tex**
   ```bash
   ls -lh main.tex
   ls capitoli/*.tex
   ```

3. **Compilare PDF**
   ```bash
   latexmk -pdf main.tex
   # oppure
   pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
   ```

4. **Verificare risultato**
   ```bash
   ls -lh main.pdf
   ```

5. **Visualizzare PDF**
   ```bash
   xdg-open main.pdf     # Linux
   open main.pdf         # macOS
   start main.pdf        # Windows
   ```

6. **Pulizia file temporanei** (opzionale)
   ```bash
   latexmk -c
   # oppure
   rm -f *.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk
   ```

---

## 🎯 Ordine di Compilazione Consigliato

### Priorità ALTA (compilare prima)

1. **Algoritmi** (scadenza: 10 Dic)
   ```bash
   cd Algoritmi && latexmk -pdf main.tex
   ```

2. **React** (scadenza: 18 Dic)
   ```bash
   cd React && latexmk -pdf main.tex
   ```

3. **WebSecurity** (scadenza: 15 Dic)
   ```bash
   cd WebSecurity && latexmk -pdf main.tex
   ```

### Priorità Media

4. **Database** (scadenza: 5 Dic)
   ```bash
   cd Database && latexmk -pdf main.tex
   ```

5. **Assembly** (scadenza: 10 Dic)
   ```bash
   cd Assembly && latexmk -pdf main.tex
   ```

6. **Git** (scadenza: 15 Dic)
   ```bash
   cd Git && latexmk -pdf main.tex
   ```

7. **Linux** (scadenza: 15 Dic)
   ```bash
   cd Linux && latexmk -pdf main.tex
   ```

8. **REST API** (scadenza: 18 Dic)
   ```bash
   cd RestAPI && latexmk -pdf main.tex
   ```

9. **Docker** (scadenza: 20 Dic)
   ```bash
   cd Docker && latexmk -pdf main.tex
   ```

---

## ⚠️ Possibili Problemi e Soluzioni

### Problema: Pacchetti mancanti

**Sintomo**:
```
! LaTeX Error: File `tcolorbox.sty' not found.
```

**Soluzione**:
```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-extra

# MiKTeX (Windows)
# Apri MiKTeX Console → Packages → Cerca "tcolorbox" → Install
```

### Problema: Font mancanti

**Sintomo**:
```
! Font \T1/lmr/m/n/10=lmr10 at 10.0pt not loadable
```

**Soluzione**:
```bash
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
```

### Problema: Overfull/Underfull hbox warnings

**Sintomo**:
```
Overfull \hbox (12.34567pt too wide) in paragraph at lines 123--456
```

**Soluzione**:
- Questi sono solo warning, non errori
- Il PDF viene comunque generato
- Per risolvere: aggiustare manualmente il testo o usare `\sloppy`

### Problema: Memoria insufficiente

**Sintomo**:
```
TeX capacity exceeded, sorry [main memory size=5000000]
```

**Soluzione**:
```bash
# Aumenta la memoria TeX in texmf.cnf
main_memory = 12000000
```

---

## 📊 Stima Tempi Compilazione

| Corso | Capitoli | Tempo stimato |
|-------|----------|---------------|
| Algoritmi | 15 | 2-3 min |
| Database | 16 | 2-3 min |
| Assembly | 17 | 3-4 min |
| Git | 13 | 1-2 min |
| Linux | 13 | 1-2 min |
| Docker | 13 | 1-2 min |
| React | 15 | 2-3 min |
| REST API | 15 | 2-3 min |
| WebSecurity | 15 | 2-3 min |

**Totale stimato**: 18-26 minuti per tutti i 9 corsi

---

## ✅ Checklist Post-Compilazione

Per ogni corso compilato:

- [ ] PDF generato senza errori
- [ ] Dimensione file ragionevole (> 100KB)
- [ ] TOC (Table of Contents) presente
- [ ] Link interni funzionanti
- [ ] Diagrammi TikZ renderizzati
- [ ] Syntax highlighting codice presente
- [ ] Nessuna pagina bianca indesiderata
- [ ] Numerazione capitoli corretta
- [ ] Riferimenti bibliografici funzionanti

### Comandi verifica rapida:

```bash
# Dimensione PDF
ls -lh main.pdf

# Numero pagine
pdfinfo main.pdf | grep Pages

# Verifica errori compilazione
grep -i "error" main.log
grep -i "undefined" main.log
```

---

## 📁 Struttura File Dopo Compilazione

```
Algoritmi/
├── main.tex                    # Sorgente principale
├── main.pdf                    # ✅ PDF generato
├── main.aux                    # File ausiliario
├── main.log                    # Log compilazione
├── main.out                    # Outline PDF
├── main.toc                    # Table of Contents
├── capitoli/
│   ├── 00_prefazione.tex
│   ├── 01_introduzione_complessita.tex
│   └── ...
└── [altri file ausiliari]
```

### File da committare in Git:
- ✅ `main.tex`
- ✅ `main.pdf` (opzionale, può essere grande)
- ✅ `capitoli/*.tex`
- ❌ `*.aux`, `*.log`, `*.out`, `*.toc` (file temporanei)

---

## 🚀 Quick Start

Per compilare TUTTI i corsi rapidamente:

```bash
cd /home/user/Appunti

# Metodo 1: Loop bash
for corso in Algoritmi Git Linux Docker React RestAPI WebSecurity Database Assembly; do
    echo "Compilazione $corso..."
    cd "$corso"
    latexmk -pdf -interaction=nonstopmode main.tex
    cd ..
done

# Metodo 2: Parallelo (più veloce, richiede GNU parallel)
parallel 'cd {} && latexmk -pdf main.tex' ::: Algoritmi Git Linux Docker React RestAPI WebSecurity Database Assembly
```

---

## 📌 Note Importanti

1. **Prima compilazione**: Può richiedere più tempo per download pacchetti
2. **Compilazioni successive**: Molto più veloci (cache)
3. **File log**: Controllare `main.log` per errori/warning
4. **Backup**: Fare backup prima di modifiche massive
5. **Git**: Committare PDF solo se necessario (file grandi)

---

## 🔗 Risorse Utili

### Documentazione LaTeX
- [LaTeX Project](https://www.latex-project.org/)
- [TeX Stack Exchange](https://tex.stackexchange.com/)
- [Overleaf Documentation](https://www.overleaf.com/learn)

### Pacchetti Specifici
- [tcolorbox Manual](https://ctan.org/pkg/tcolorbox)
- [TikZ & PGF Manual](https://ctan.org/pkg/pgf)
- [listings Package](https://ctan.org/pkg/listings)

### Tools Online
- [Overleaf](https://www.overleaf.com/) - Editor LaTeX online
- [LaTeX Base](https://latexbase.com/) - Compiler online semplice

---

## ✍️ Prossimi Passi

Dopo la compilazione dei PDF:

1. **Verifica qualità PDF** (controllo visivo)
2. **Aggiorna README.md** (cambia status PDF da ⏳ a ✅)
3. **Aggiorna MASTER-TODO.md** (marca task come completati)
4. **Commit e push** modifiche
5. **Genera descrittori AI** per i nuovi corsi
6. **Crea documentazione** (README, TODO, PIANO_SVILUPPO)

---

**Autore**: Claude
**Data**: 15 Novembre 2025
**Versione**: 1.0
