# Template Documentazione - Guida all'Uso

Questa directory contiene i template standardizzati per creare la documentazione dei corsi nel repository Appunti.

**Data creazione**: 15 Novembre 2025
**Versione**: 1.0

---

## 📁 File Template Disponibili

### 1. TEMPLATE_README.md
Template per il file README.md principale di ogni corso.

**Sezioni incluse**:
- Header con badges
- Descrizione corso
- Tabella capitoli completati
- Struttura progetto
- Obiettivi di apprendimento
- Descrittori AI (se generati)
- Prerequisiti
- Istruzioni compilazione PDF
- Statistiche corso
- Risorse aggiuntive
- Convenzioni di codifica
- Stato del corso

**Quando usare**: Per ogni nuovo corso o per aggiornare README esistenti.

---

### 2. TEMPLATE_TODO.md
Template per il file TODO.md di task tracking per ogni corso.

**Sezioni incluse**:
- Stato attuale
- Task priorità MASSIMA (urgenti)
- Task priorità ALTA (≤14 giorni)
- Task priorità MEDIA (≤30 giorni)
- Task priorità BASSA (backlog)
- Descrittori AI
- Task completati recenti
- Metriche di progresso
- Timeline e scadenze

**Tag system standardizzato**:
- `[BUILD-XX]`: Compilazione e build automation
- `[CONTENT-XX]`: Contenuti teorici ed esempi
- `[EXERCISE-XX]`: Esercizi e soluzioni
- `[TEST-XX]`: Testing e validazione
- `[DOC-XX]`: Documentazione
- `[GRAPHICS-XX]`: Diagrammi e immagini
- `[REFACTOR-XX]`: Refactoring
- `[FORMAT-XX]`: Formattazione LaTeX
- `[AI-DESC-XX]`: Descrittori AI

**Quando usare**: Per gestire task e priorità di ogni corso.

---

### 3. TEMPLATE_PIANO_SVILUPPO.md
Template per il file PIANO_SVILUPPO.md di roadmap futura.

**Sezioni incluse**:
- Stato attuale (riepilogo)
- Descrittori AI status
- Roadmap futura (Fase 1, 2, 3)
- Appendici pianificate
- Miglioramenti capitoli esistenti
- Strumenti e automazione
- Timeline dettagliata
- Metriche di progresso target
- Riferimenti e risorse
- Idee e proposte

**Quando usare**: Per pianificare espansioni e miglioramenti futuri.

---

## 🚀 Come Usare i Template

### Metodo 1: Copia e Personalizza

```bash
# 1. Entra nella directory del corso
cd /home/user/Appunti/[NOME_CORSO]

# 2. Copia i template
cp ../templates/TEMPLATE_README.md ./README.md
cp ../templates/TEMPLATE_TODO.md ./TODO.md
cp ../templates/TEMPLATE_PIANO_SVILUPPO.md ./PIANO_SVILUPPO.md

# 3. Modifica i file sostituendo i placeholder
# Cerca e sostituisci i placeholder indicati tra [PARENTESI_QUADRE]
```

### Metodo 2: Script Automatico (Futuro)

```bash
# Da implementare: Script che genera automaticamente i 3 file
# ./tools/generate_course_docs.sh [NOME_CORSO] [ANNO]
```

---

## 📝 Placeholder da Sostituire

Quando personalizzi i template, cerca e sostituisci questi placeholder:

### Comuni a tutti i file:
- `[NOME_CORSO]`: Nome del corso (es. "Java", "Python", "Database")
- `[ANNO]`: Anno scolastico (es. "3", "4", "5")
- `[DATA]`: Data attuale in formato GG Mese AAAA
- `[NUMERO]`: Numeri vari (pagine, capitoli, esercizi, ecc.)
- `[PERCENTUALE]`: Percentuali di completamento

### Specifici README:
- `[DESCRIZIONE_BREVE_ARGOMENTI]`: Descrizione di 1-2 righe
- `[TITOLO_CAPITOLO_XX]`: Titolo di ogni capitolo
- `[NUMERO_PAGINE]`: Numero totale di pagine
- `[SIZE]`: Dimensione file PDF
- `[ID-XXX]`: ID descrittori AI
- `[CATEGORIA_X]`: Categoria di descrittori

### Specifici TODO:
- `[TAG-XXX]`: Tag del task (es. BUILD-01, CONTENT-02)
- `[Stima]`: Stima tempo in ore/minuti
- `[AAAA-MM-GG]`: Date in formato ISO

### Specifici PIANO:
- `[N1]-[N2]`: Range di numeri (es. "20-25 pagine")
- `[ORE]`: Stime in ore
- `[Q1/Q2/Q3/Q4]`: Quarter dell'anno
- `[X.Y]`: Versione (es. "1.0")

---

## ✅ Checklist Personalizzazione

### README.md

- [ ] Sostituito `[NOME_CORSO]` con nome reale
- [ ] Sostituito `[ANNO]` con anno corretto
- [ ] Compilata tabella capitoli con titoli reali
- [ ] Aggiornato numero totale pagine
- [ ] Inseriti obiettivi di apprendimento specifici
- [ ] Aggiornata sezione descrittori AI (se generati)
- [ ] Verificati prerequisiti software
- [ ] Aggiornate convenzioni di codifica
- [ ] Inserite risorse aggiuntive pertinenti
- [ ] Verificata struttura directory corretta

### TODO.md

- [ ] Inseriti task reali priorità MASSIMA
- [ ] Inseriti task reali priorità ALTA
- [ ] Compilata sezione descrittori AI
- [ ] Aggiornate metriche di progresso
- [ ] Inserite scadenze realistiche
- [ ] Verificati tag corretti per task
- [ ] Compilata timeline prossime settimane
- [ ] Rimossi task non applicabili

### PIANO_SVILUPPO.md

- [ ] Compilata tabella stato attuale
- [ ] Definita Fase 1 con capitoli concreti
- [ ] Definita Fase 2 (se applicabile)
- [ ] Definita Fase 3 (se applicabile)
- [ ] Pianificate appendici
- [ ] Inseriti miglioramenti specifici
- [ ] Compilata timeline Q4 2025 - Q1 2026
- [ ] Aggiornati target metriche
- [ ] Inserite risorse bibliografiche

---

## 🎯 Best Practices

### Consistenza
- Usa sempre lo stesso formato per date: GG Mese AAAA (es. "15 Novembre 2025")
- Mantieni lo stesso stile di emoji in tutti i file
- Usa gli stessi tag system in TODO e riferimenti in PIANO

### Sincronizzazione
- Quando aggiorni README, verifica che TODO sia allineato
- Quando completi task in TODO, aggiorna metriche in README
- Quando pianifichi in PIANO, crea task corrispondenti in TODO

### Aggiornamenti
- Aggiorna README quando:
  - Completi un capitolo
  - Compili nuovo PDF
  - Generi descrittori AI
  - Cambi stato generale del corso

- Aggiorna TODO quando:
  - Inizi un nuovo task (TODO → IN PROGRESS)
  - Completi un task (IN PROGRESS → DONE → sposta in "Completati")
  - Emergono nuovi problemi o task
  - Cambiano le priorità

- Aggiorna PIANO quando:
  - Completi una fase
  - Modifichi la roadmap
  - Aggiungi nuove idee o proposte
  - Ricevi feedback da studenti/docenti

---

## 📊 Integrazione con MASTER-TODO.md

I file TODO.md dei singoli corsi devono essere sincronizzati con il MASTER-TODO.md principale:

1. **Task bloccanti** dei corsi → Vanno in MASTER-TODO priorità MASSIMA/ALTA
2. **Stato generale** → Aggiorna tabella corsi in MASTER-TODO
3. **Task completati** → Documenta in MASTER-TODO sezione changelog
4. **Scadenze** → Mantieni allineate tra TODO corso e MASTER-TODO

**Frequenza sincronizzazione suggerita**: Settimanale

---

## 🔧 Strumenti Utili

### Ricerca e Sostituzione Massiva (VS Code)
```
1. Apri file template
2. Cmd/Ctrl + H (Find and Replace)
3. Cerca: [NOME_CORSO]
4. Sostituisci: Java (o altro)
5. Replace All
```

### Validazione Markdown
- **Strumento**: markdownlint
- **Comando**: `markdownlint README.md TODO.md PIANO_SVILUPPO.md`

### Generazione Automatica Indici
- **Strumento**: doctoc
- **Comando**: `doctoc README.md` (genera TOC automatico)

---

## 📚 Esempi Completi

### Corsi con Documentazione Completa

Vedi questi corsi come riferimento per documentazione ben strutturata:

- **Java**: `/home/user/Appunti/Java/`
  - README.md: Completo con descrittori AI
  - TODO.md: Sistema tag ben definito
  - PIANO_SVILUPPO.md: Roadmap dettagliata

- **Python**: `/home/user/Appunti/Python/`
  - README.md: Include sezione NAO Robotics
  - TODO.md: Task management dettagliato
  - PIANO_SVILUPPO.md: 18+ moduli pianificati

- **C**: `/home/user/Appunti/C/`
  - README.md: Struttura base solida
  - TODO.md: Task chiari e concisi
  - PIANO_SVILUPPO.md: Espansioni future

---

## 🔄 Versioning dei Template

**Versione attuale**: 1.0 (15 Novembre 2025)

### Changelog Template

**v1.0 (15 Nov 2025)**:
- ✅ Creazione iniziale template README.md
- ✅ Creazione iniziale template TODO.md
- ✅ Creazione iniziale template PIANO_SVILUPPO.md
- ✅ Documentazione guida all'uso

### Prossime Versioni (Pianificate)

**v1.1**:
- [ ] Script automatico generazione documenti
- [ ] Template per log di compilazione
- [ ] Template per quick reference

**v2.0**:
- [ ] Integrazione con sistema CI/CD
- [ ] Automazione sincronizzazione MASTER-TODO
- [ ] Template multilingua (EN/IT)

---

## 📞 Supporto

Per domande o problemi con i template:

1. Consulta esempi nei corsi esistenti (Java, Python, C)
2. Verifica MASTER-TODO.md per linee guida generali
3. Apri una issue nel repository

---

**Autore**: Istituto Tecnico Antonio Scarpa ITS
**Ultima modifica**: 15 Novembre 2025
**Riferimento**: [MASTER-TODO.md](../MASTER-TODO.md)
