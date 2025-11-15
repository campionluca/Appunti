# TODO — Corso Assembly 8086

**Ultimo aggiornamento**: 14 Novembre 2025
**Versione**: 1.0
**Status**: 🆕 NUOVO CORSO (appena creato)

---

## 📊 Stato Generale

| Categoria | Stato | Completamento |
|-----------|-------|---------------|
| Struttura repository | ✅ | 100% |
| Capitoli LaTeX (16 file) | ✅ | 100% |
| Esempi di codice | ✅ | 100% |
| Esercizi | ✅ | 100% (80+) |
| PDF principale | ⏳ | 0% (da compilare) |
| Descrittori AI | ⏳ | 0% (20-25 pianificati) |
| Soluzioni dettagliate | 🟡 | 30% (appendice parziale) |

---

## 🚨 PRIORITÀ ALTA (Scadenza ≤ 7 giorni)

### [ASM-BUILD-01] Compilare PDF principale
- **Stato**: TODO
- **Tempo stimato**: 10 min
- **Comando**: `latexmk -pdf main.tex`
- **Dipendenze**: LaTeX installato
- **Priorità**: ALTA
- **Scadenza**: 2025-11-21
- **Assegnato**: @assistant

### [ASM-VALID-01] Validare tutti gli esempi di codice
- **Stato**: TODO
- **Tempo stimato**: 3-4 ore
- **Tool**: EMU8086, NASM, DOSBox
- **Priorità**: ALTA
- **Scadenza**: 2025-11-25
- **Note**: Testare almeno 1 esempio per capitolo

---

## 📌 PRIORITÀ MEDIA (Scadenza ≤ 30 giorni)

### [ASM-DESC-01] Generare descrittori AI
- **Stato**: TODO
- **Tempo stimato**: 2 ore
- **Numero**: 20-25 descriptors
- **Categorie**:
  - Architecture (4): Registri, segmentazione, indirizzamento, flag
  - Instruction Set (10): Gruppi istruzioni
  - Advanced (5): Procedure, interrupt, I/O
  - Optimization (3): Performance, code golf
- **Priorità**: MEDIA
- **Scadenza**: 2025-12-10

### [ASM-EXAMPLES-01] Creare esempi compilabili separati
- **Stato**: TODO
- **Tempo stimato**: 2 ore
- **Struttura**: `Assembly/esempi/cap01/`, `cap02/`, etc.
- **Formato**: File `.asm` standalone
- **Priorità**: MEDIA

### [ASM-SOLUTIONS-02] Completare appendice soluzioni
- **Stato**: IN PROGRESS (30%)
- **Tempo stimato**: 3 ore
- **Note**: Attualmente solo Cap. 1-9, mancano Cap. 10-13
- **Priorità**: MEDIA

---

## 💡 PRIORITÀ BASSA (Backlog)

### [ASM-PROJECTS-01] Implementare progetti completi
- **Stato**: TODO
- **Progetti**:
  - [ ] Calcolatrice 16 bit (con read_number/print_number)
  - [ ] Bubble sort completo
  - [ ] Editor di testo minimale
  - [ ] Gioco Snake
  - [ ] Bootloader funzionante
- **Priorità**: BASSA

### [ASM-DIAGRAMS-01] Aggiungere diagrammi TikZ
- **Stato**: TODO
- **Target**: 10+ diagrammi aggiuntivi
- **Esempi**:
  - Pipeline BIU/EU dettagliata
  - Stack frame evolution
  - Interrupt handling flow
  - Hardware interfacing
- **Priorità**: BASSA

### [ASM-MAKEFILE-01] Creare Makefile
- **Stato**: TODO
- **Tempo**: 15 min
- **Comandi**: `make pdf`, `make clean`, `make view`
- **Priorità**: BASSA

---

## ✅ COMPLETATI (14 Novembre 2025)

### Struttura e Contenuti
- ✅ **[ASM-STRUCT-01]** Creata struttura directory `Assembly/` e `capitoli/`
- ✅ **[ASM-MAIN-01]** File `main.tex` con syntax highlighting Assembly x86
- ✅ **[ASM-CAP-01-16]** Creati tutti i 16 capitoli (13 + 3 appendici):
  - Parte I: Fondamenti (Cap. 1-3)
  - Parte II: Istruzioni (Cap. 4-7)
  - Parte III: Tecniche (Cap. 8-11)
  - Parte IV: Applicazioni (Cap. 12-13)
  - Appendici: Soluzioni, Quick Reference, Bibliografia
- ✅ **[ASM-EXERCISES-01]** Inseriti 80+ esercizi progressivi (base/intermedi/avanzati)
- ✅ **[ASM-EXAMPLES-CODE]** Creati 150+ esempi di codice commentati

### Documentazione
- ✅ **[ASM-README-01]** README.md completo (500+ righe)
- ✅ **[ASM-TODO-01]** TODO.md con task tracking
- ✅ **[ASM-PIANO-01]** PIANO_SVILUPPO.md con roadmap

---

## 📋 Checklist Pre-Release

### Build
- [ ] Compilare PDF senza errori
- [ ] Verificare indice corretto
- [ ] Controllare hyperlink funzionanti
- [ ] Validare syntax highlighting Assembly

### Contenuti
- [ ] Testare esempi chiave (1 per capitolo)
- [ ] Verificare esercizi solvibili
- [ ] Controllare coerenza cross-reference

### Qualità
- [ ] Correzione ortografica
- [ ] Uniformità formattazione
- [ ] Completezza soluzioni appendice

### Integrazione
- [ ] Aggiornare MASTER-TODO.md
- [ ] Aggiornare README.md principale
- [ ] Generare descrittori AI
- [ ] Git commit e push

---

## 🔄 Linee Guida

### Aggiornamento TODO
- Aggiornare stato task in tempo reale
- Marcare DONE alla completamento
- Aggiungere timestamp per task critici

### Priorità
- **ALTA**: Blocca utilizzo corso (PDF, validazione)
- **MEDIA**: Migliora qualità (descrittori, soluzioni)
- **BASSA**: Nice-to-have (Makefile, diagrammi extra)

### Testing
- Testare esempi con EMU8086 (Windows)
- Validare sintassi NASM (Linux/macOS)
- Verificare compatibilità DOSBox

---

## 📅 Timeline

### Settimana 1 (14-21 Nov)
- [x] Creazione struttura e capitoli
- [ ] Compilazione PDF
- [ ] Validazione esempi chiave

### Settimana 2 (22-28 Nov)
- [ ] Completamento soluzioni
- [ ] Testing completo esempi
- [ ] Creazione esempi standalone

### Settimana 3 (29 Nov - 5 Dic)
- [ ] Generazione descrittori AI
- [ ] Correzione errori
- [ ] Ottimizzazione contenuti

### Settimana 4 (6-12 Dic)
- [ ] Release finale
- [ ] Integrazione con altri corsi
- [ ] Documentazione aggiornata

---

**Prossima revisione**: 21 Novembre 2025
**Responsabile**: @assistant
**Corso target**: 5° anno ITS Antonio Scarpa
