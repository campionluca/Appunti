# 📚 Appunti - Repository Didattico ITS Antonio Scarpa

[![LaTeX](https://img.shields.io/badge/LaTeX-PDF-green.svg)](https://www.latex-project.org/)
[![License](https://img.shields.io/badge/License-Educational-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com)
[![Last Update](https://img.shields.io/badge/Last%20Update-November%202025-informational.svg)](MASTER-TODO.md)

Repository educativo completo contenente materiali didattici per **5 corsi di programmazione** dell'Istituto Tecnico Antonio Scarpa, organizzati in formato LaTeX per la generazione di manuali PDF professionali.

---

## 🎓 Corsi Disponibili

| Corso | Anno | Capitoli | PDF | Stato | Pagine | Descrizione |
|-------|------|----------|-----|-------|--------|-------------|
| **[C](C/)** | 3° | 11 + App | ✅ | Completo | ~300 | Programmazione procedurale, puntatori, memoria |
| **[HTML/CSS](HTMLCSS/)** | 4° | 12 | ✅ | Completo | ~100 | Web development, responsive design, JavaScript |
| **[Java](Java/)** | 4° | 10 + App | ✅ | Completo | ~280 | OOP, GUI, MVC, design patterns |
| **[PHP](PHP/)** | 4° | 7+ | ✅ | In sviluppo | ~160 | Web backend, sicurezza, database |
| **[Python](Python/)** | 5° | 18+ | ✅ | In progresso | ~200 | Python avanzato, GUI, web, robotics |
| **[Database](Database/)** | 4°/5° | 13 + App | ⏳ | Nuovo corso | ~400 | DBMS, ER, SQL, normalizzazione, transazioni |

**Totale**: ~1,440 pagine di contenuti didattici | 280+ esercizi | 450+ esempi di codice

---

## 🚀 Quick Start

### Clona la repository

```bash
git clone https://github.com/tuousername/Appunti.git
cd Appunti
```

### Compila un PDF

```bash
# Esempio: compilare il corso C
cd C
latexmk -pdf main.tex

# Oppure con pdflatex (3 passate)
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

### Visualizza i PDF pre-compilati

I PDF sono già disponibili in ogni directory del corso:
- `C/main.pdf`
- `HTMLCSS/main.pdf`
- `Java/main.pdf`
- `PHP/main.pdf`
- `Python/main.pdf`

---

## 📂 Struttura del Progetto

```
Appunti/
├── C/                              # Corso Programmazione C (Terza)
│   ├── main.tex                    # File LaTeX principale
│   ├── main.pdf                    # PDF compilato (1.1 MB)
│   ├── capitoli/                   # 11 capitoli + appendici
│   ├── README.md                   # Documentazione corso
│   ├── TODO.md                     # Task e priorità
│   └── PIANO_SVILUPPO.md           # Roadmap
│
├── HTMLCSS/                        # Corso HTML5, CSS3, JavaScript (Quarta)
│   ├── main.tex
│   ├── main.pdf                    # PDF compilato (330 KB)
│   ├── capitoli/                   # 12 capitoli
│   └── ...
│
├── Java/                           # Corso Java OOP (Quarta)
│   ├── main.tex
│   ├── main.pdf                    # PDF compilato (171 KB)
│   ├── capitoli/                   # 10 capitoli + appendici
│   ├── Makefile                    # Build automation
│   └── ...
│
├── PHP/                            # Corso PHP Web Development
│   ├── main.tex
│   ├── main.pdf                    # PDF compilato (161 KB)
│   ├── capitoli/                   # 7+ capitoli
│   ├── esempi/                     # Codice PHP eseguibile
│   ├── quick_reference/            # Schede riassuntive
│   └── ...
│
├── Python/                         # Corso Python Avanzato (Quinta)
│   ├── main.tex
│   ├── main.pdf                    # PDF compilato (638 KB)
│   ├── capitoli/                   # 18+ moduli
│   └── ...
│
├── tools/                          # Strumenti di supporto e automazione
│
├── MASTER-TODO.md                  # Task centralizzato (v3.0)
├── agent_instructions.json         # Configurazione agenti AI (v4.0)
├── istruzioni_agenti.md            # Documentazione per agenti
├── C_COVERAGE_ANALYSIS.md          # Analisi copertura corso C
├── C_CONCEPT_IDS.md                # Concetti chiave corso C
└── agenti_descrittori.json         # Descrittori per agenti AI
```

---

## 🎯 Caratteristiche Principali

### 📖 Contenuti Didattici di Qualità

- **Teoria approfondita**: Spiegazioni chiare e dettagliate in italiano
- **Esempi pratici**: 300+ esempi di codice testati e commentati
- **Esercizi graduati**: Base → Intermedio → Avanzato
- **Soluzioni complete**: Appendici con codice risolto e commentato
- **Box informativi**: Attenzione, Note, Errori comuni evidenziati

### 🛠️ Gestione Avanzata

- **Sistema agenti AI**: Configurato per automazione e sincronizzazione
- **Task tracking**: MASTER-TODO.md centralizzato con priorità e deadline
- **Triple documentazione**: README, TODO, PIANO_SVILUPPO per ogni corso
- **Versionamento**: Git con branch strutturati
- **Build automation**: Makefile e script di compilazione

### 🎨 Formattazione Professionale

- **LaTeX professionale**: Layout tipografico di alta qualità
- **Box colorati**: Evidenziazione visiva di concetti chiave
- **Syntax highlighting**: Codice colorato per ogni linguaggio
- **Diagrammi**: TikZ per visualizzazioni UML, flowchart, memoria
- **Hyperlink**: Navigazione interna con indici e riferimenti

---

## 🔧 Requisiti Tecnici

### Software Necessario

#### Per Compilare i PDF LaTeX

- **LaTeX Distribution**: TeX Live (Linux/macOS) o MiKTeX (Windows)
- **Compilatori**: `pdflatex`, `xelatex`, o `latexmk` (consigliato)
- **Pacchetti LaTeX**:
  - `babel` (supporto italiano)
  - `geometry` (margini e layout)
  - `listings` (syntax highlighting)
  - `hyperref` (link e riferimenti)
  - `tcolorbox` (box colorati)
  - `tikz` (diagrammi)
  - `amsmath` (formule matematiche)

#### Per Eseguire gli Esempi di Codice

- **C**: GCC 7+ (Build Essential, Xcode, MinGW)
- **Java**: JDK 8+ (preferibilmente 11 o superiore)
- **Python**: Python 3.10+
- **PHP**: PHP 8.1+ con estensione `mysqli`
- **Web**: Browser moderno (Chrome, Firefox, Safari)

#### Editor Consigliati

- **LaTeX**: TeXstudio, Overleaf, VS Code + LaTeX Workshop
- **Programmazione**: VS Code, IntelliJ IDEA, PyCharm, PhpStorm

---

## 📝 Come Usare Questo Materiale

### Per Studenti

1. **Scegli il corso**: Naviga nella directory del corso di interesse
2. **Consulta il README**: Leggi `README.md` per panoramica e obiettivi
3. **Studia dal PDF**: Apri `main.pdf` per il contenuto completo
4. **Segui gli esempi**: Digita personalmente il codice (non copiare!)
5. **Fai gli esercizi**: Prova autonomamente prima di vedere le soluzioni
6. **Compila e testa**: Verifica che il codice funzioni
7. **Sperimenta**: Modifica gli esempi per comprenderne il funzionamento

### Per Docenti

- Materiale pronto per l'uso in aula
- Personalizzabile modificando i file `.tex`
- Esercizi utilizzabili come verifiche formative
- Progetti guidati per laboratorio
- Soluzioni disponibili per correzione rapida

### Per Contributori

1. Fork della repository
2. Crea un branch per le modifiche (`git checkout -b feature/miglioramento`)
3. Modifica i file `.tex` seguendo le convenzioni
4. Testa la compilazione (`latexmk -pdf main.tex`)
5. Commit con messaggi descrittivi
6. Push e crea una Pull Request

---

## 📊 Stato del Progetto

### Completamento Corsi

| Corso | Contenuti | Esercizi | PDF | Priorità | Deadline |
|-------|-----------|----------|-----|----------|----------|
| C | ✅ 100% | ✅ 120+ | ✅ | Bassa | — |
| HTMLCSS | ✅ 100% | ✅ 24+ | ✅ | Bassa | — |
| Java | ✅ 100% | ✅ 60+ | ⚠️ warnings | Media | 2025-11-30 |
| PHP | 🟡 85% | 🟡 15+ | ✅ | Media | 2025-11-28 |
| Python | 🟡 75% | 🟡 30+ | ✅ | Alta | 2025-11-20 |

### Task Attivi (da MASTER-TODO.md v3.0)

**🚨 Priorità Alta**:
- [PY-BUILD-02] Automatizzare conteggio moduli Python
- [PY-BUILD-03] Creare Makefile per Python
- [JAVA-BUG-01] Risolvere warning LaTeX Java

**📌 Priorità Media**:
- [PY-CONTENT-06] Completare esercizi Python
- [JAVA-CONTENT-02] Aggiungere diagrammi UML
- [PHP-CONTENT-01] Convertire manuale PHP

Vedi [MASTER-TODO.md](MASTER-TODO.md) per dettagli completi.

---

## 🎓 Percorso Didattico Completo

### Anno 3° - Fondamenti

**C - Programmazione Procedurale**
- Sintassi base, tipi di dato, operatori
- Controllo di flusso, funzioni
- Array, puntatori, gestione memoria
- Struct, file I/O
- 11 capitoli + 120+ esercizi

### Anno 4° - Sviluppo Web e OOP

**Java - Object-Oriented Programming**
- Classi, oggetti, ereditarietà
- Interfacce, eccezioni, collections
- GUI con Swing, pattern MVC
- Lambda expressions
- 10 capitoli + progetti

**HTML/CSS - Frontend Development**
- HTML5 semantico, form, accessibilità
- CSS3, Flexbox, Grid, responsive
- SASS/SCSS preprocessori
- JavaScript basics e DOM
- 12 capitoli + 6 progetti

**PHP - Backend Development**
- Form processing, validazione
- Cookie, sessioni, upload file
- Database MySQL (mysqli)
- Sicurezza web (XSS, SQL injection)
- 7+ capitoli + esempi sicurezza

### Anno 5° - Programmazione Avanzata

**Python - Sviluppo Completo**
- Fondamenti Python, OOP avanzato
- Decoratori, iteratori, generatori
- GUI con Tkinter, web con Flask
- Automazione e web scraping
- Database, testing, debugging
- Robotics NAO V6
- 18+ moduli + progetti NAO

---

## 🤖 Sistema di Gestione con Agenti AI

Il progetto utilizza un sistema avanzato di agenti AI per:

- **Sincronizzazione**: MASTER-TODO.md centralizzato
- **Metadata extraction**: Da README, TODO, PIANO_SVILUPPO
- **Compilazione automatica**: LaTeX build automation
- **Quality assurance**: Error checking e validazione
- **Content generation**: Documentazione e descrittori
- **Priority management**: Gestione deadline e task

Configurazione in `agent_instructions.json` (v4.0)

---

## 📐 Convenzioni di Codifica

### C
- Variabili: `snake_case` o `camelCase`
- Costanti: `MAIUSCOLO_UNDERSCORE`
- Commenti dettagliati in italiano

### Java
- Classi: `PascalCase`
- Metodi/variabili: `camelCase`
- Costanti: `MAIUSCOLO_UNDERSCORE`
- Package: `minuscolo.punto.separato`

### Python
- Stile: PEP 8
- Variabili/funzioni: `snake_case`
- Classi: `PascalCase`
- Costanti: `MAIUSCOLO_UNDERSCORE`

### PHP
- Stile: PSR-12
- Variabili: `$camelCase`
- Classi: `PascalCase`
- Funzioni: `camelCase`

### HTML/CSS
- HTML ID: `camelCase`
- CSS classi: `kebab-case`
- Variabili SCSS: `$camelCase`

---

## 🔗 Risorse Utili

### Documentazione Online

- **C**: [C Reference](https://en.cppreference.com/w/c)
- **Java**: [Oracle Java Docs](https://docs.oracle.com/en/java/)
- **Python**: [Python.org Docs](https://docs.python.org/3/)
- **PHP**: [PHP Manual](https://www.php.net/manual/it/)
- **HTML/CSS**: [MDN Web Docs](https://developer.mozilla.org/)

### Compilatori Online

- **C**: [Online GDB](https://www.onlinegdb.com/online_c_compiler)
- **Java**: [JDoodle](https://www.jdoodle.com/online-java-compiler)
- **Python**: [Repl.it](https://replit.com/languages/python3)
- **PHP**: [PHP Sandbox](https://onlinephp.io/)
- **HTML/CSS**: [CodePen](https://codepen.io/)

### Strumenti di Validazione

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [WebAIM Accessibility Checker](https://wave.webaim.org/)

---

## 📄 Licenza

Materiale didattico per uso educativo.

**Istituto Tecnico Antonio Scarpa ITS** - Anno Scolastico 2025-2026

---

## 👥 Contributori

- **Docenti**: Istituto Tecnico Antonio Scarpa
- **Studenti**: Contributi e feedback
- **Community**: Correzioni e miglioramenti

---

## 📞 Contatti e Supporto

- **Issues**: Apri una issue per segnalare errori o proporre miglioramenti
- **Pull Requests**: Contribuisci con modifiche e aggiunte
- **Documentazione**: Consulta i README specifici di ogni corso

---

## 📈 Statistiche Repository

- **Corsi**: 5
- **Capitoli**: 60+
- **Pagine totali**: ~1,040
- **Esercizi**: 200+
- **Esempi codice**: 300+
- **Progetti guidati**: 10+
- **Dimensione repository**: ~3 MB (PDF inclusi)
- **Ultimo aggiornamento**: 14 Novembre 2025

---

## 🗓️ Roadmap Futura

### Completamento (2025-11-20 / 2025-11-30)
- ✅ Finalizzare corso Python
- ✅ Risolvere warning LaTeX Java
- ✅ Completare esercizi e soluzioni

### Espansioni Opzionali
- 📚 Nuovi capitoli avanzati (design patterns, concurrency)
- 🎬 Video tutorial integrati
- 🧪 Quiz interattivi per ogni capitolo
- 📱 Versione mobile-friendly dei contenuti
- 🌐 Piattaforma web per consultazione online

### Manutenzione
- 🔄 Sincronizzazione periodica documentazione
- 🐛 Bug fixes e correzioni
- 📝 Aggiornamento esempi con nuove versioni linguaggi
- 🎨 Miglioramenti tipografici LaTeX

---

## ⭐ Se Questo Progetto Ti È Utile

- ⭐ Lascia una stella su GitHub
- 🔄 Condividi con altri studenti
- 📝 Contribuisci con miglioramenti
- 💬 Fornisci feedback e suggerimenti

---

<div align="center">

**[⬆ Torna su](#-appunti---repository-didattico-its-antonio-scarpa)**

Made with ❤️ for education | Powered by LaTeX & Open Source

**Versione**: 1.0 | **Data**: 14 Novembre 2025

</div>
