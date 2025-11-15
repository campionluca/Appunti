# PIANO DI SVILUPPO — Assembly 8086

**Versione**: 1.0
**Data Creazione**: 14 Novembre 2025
**Ultimo Aggiornamento**: 14 Novembre 2025

---

## 📊 Stato Attuale (14 Nov 2025)

### Completamento Generale: 85%

| Componente | Stato | % |
|------------|-------|---|
| Struttura repository | ✅ Completo | 100% |
| Capitoli LaTeX | ✅ Completo | 100% |
| Esempi codice | ✅ Completo | 100% |
| Esercizi | ✅ Completo | 100% |
| Appendici | ✅ Completo | 100% |
| PDF compilato | ⏳ Pending | 0% |
| Descrittori AI | ⏳ Pianificati | 0% |
| Testing esempi | 🟡 Parziale | 20% |
| Soluzioni complete | 🟡 Parziale | 30% |

---

## 🎯 Obiettivi del Corso

### Obiettivi Didattici

1. **Architettura Low-Level**
   - Comprendere funzionamento CPU 8086
   - Registri, flag, segmentazione memoria
   - Bus dati/indirizzi, pipeline BIU/EU

2. **Programmazione Assembly**
   - Scrivere programmi in Assembly x86
   - Usare assembler (NASM, MASM, TASM)
   - Debugging con EMU8086, Debug.exe, GDB

3. **Tecniche Avanzate**
   - Procedure con stack frame
   - Operazioni su stringhe (REP prefix)
   - Gestione interrupt software/hardware
   - I/O con porte e periferiche

4. **Applicazioni Pratiche**
   - Implementare algoritmi (sort, search)
   - Creare utilità (calcolatrice, editor)
   - Sviluppare giochi (Snake)
   - Scrivere bootloader

### Competenze Acquisite

- **Reverse Engineering**: Analisi binari, disassemblaggio
- **System Programming**: Comprensione OS, driver, firmware
- **Embedded Systems**: Programmazione microcontrollori
- **Performance Optimization**: Scrittura codice ad alte prestazioni
- **Security**: Buffer overflow, shellcode, exploit development

---

## 📚 Roadmap Contenuti

### Fase 1: Fondamenti (Completata ✅)

**Capitoli 1-3**: Architettura, Registri, Indirizzamento

**Contenuti**:
- Architettura 8086: CPU specs, BIU/EU, segmentazione
- Registri: AX-DX, SP/BP/SI/DI, CS/DS/SS/ES, FLAGS
- Modalità indirizzamento: 7 modalità complete

**Esempi**: 30+ esempi commentati
**Esercizi**: 15 esercizi base

### Fase 2: Istruzioni (Completata ✅)

**Capitoli 4-7**: Trasferimento Dati, Aritmetiche, Logiche, Controllo Flusso

**Contenuti**:
- Istruzioni dati: MOV, XCHG, LEA, PUSH/POP, IN/OUT
- Aritmetiche: ADD/SUB, MUL/DIV, INC/DEC, multi-precisione
- Logiche: AND/OR/XOR, shift, rotate
- Controllo: JMP, Jcc, LOOP, CALL/RET, INT

**Esempi**: 50+ esempi
**Esercizi**: 20 esercizi

### Fase 3: Tecniche Avanzate (Completata ✅)

**Capitoli 8-11**: Procedure, Stringhe, Interrupt, I/O Hardware

**Contenuti**:
- Procedure: Stack frame, parametri, ricorsione
- Stringhe: MOVSB/W, LODSB/W, STOSB/W, REP
- Interrupt: IVT, INT 21h/10h/16h, handler custom
- Hardware: PIC, PIT, UART, tastiera, VGA

**Esempi**: 40+ esempi
**Esercizi**: 20 esercizi

### Fase 4: Progetti (Completata ✅)

**Capitoli 12-13**: Progetti Completi, Esercizi Progressivi

**Contenuti**:
- 5 progetti completi (calcolatrice, sort, editor, Snake, bootloader)
- 80+ esercizi progressivi (base, intermedi, avanzati, sfide)
- Appendici: soluzioni, quick reference, bibliografia

**Progetti**: 5 completi
**Esercizi**: 80+

---

## 🔧 Fasi di Sviluppo

### ✅ Fase 1: Setup Iniziale (14 Nov 2025) — COMPLETATA

- [x] Creazione struttura `Assembly/` e `capitoli/`
- [x] File `main.tex` con pacchetti LaTeX
- [x] Definizione linguaggio Assembly per syntax highlighting
- [x] Template box colorati (definizione, attenzione, nota, esempio)

### ✅ Fase 2: Contenuti Teorici (14 Nov 2025) — COMPLETATA

- [x] Capitoli 1-13 (teoria completa)
- [x] Esempi di codice commentati (150+)
- [x] Esercizi per ogni capitolo (80+)
- [x] Diagrammi TikZ (pipeline, stack frame, etc.)

### ✅ Fase 3: Appendici (14 Nov 2025) — COMPLETATA

- [x] Appendice Soluzioni (parziale, 30%)
- [x] Appendice Quick Reference (tabelle complete)
- [x] Bibliografia e Risorse (50+ link)

### ⏳ Fase 4: Build e Testing (15-21 Nov 2025) — IN CORSO

- [ ] Compilare PDF con `latexmk -pdf main.tex`
- [ ] Risolvere errori/warning LaTeX
- [ ] Testare esempi con EMU8086
- [ ] Validare sintassi NASM

### ⏳ Fase 5: Descrittori AI (22 Nov - 10 Dic 2025) — PIANIFICATA

- [ ] Generare 20-25 descrittori AI strutturati
- [ ] Categorie: Architecture, Instructions, Advanced, Optimization
- [ ] File output: `ASSEMBLY_DESCRIPTORS_REPORT.json`
- [ ] Analisi coverage: `ASSEMBLY_COVERAGE_ANALYSIS.md`

### ⏳ Fase 6: Completamento (Dic 2025)

- [ ] Completare appendice soluzioni (100%)
- [ ] Creare esempi standalone in `esempi/`
- [ ] Implementare progetti completi funzionanti
- [ ] Makefile per build automation

---

## 📅 Timeline Dettagliata

### Novembre 2025

| Settimana | Attività | Deliverable |
|-----------|----------|-------------|
| **14-21 Nov** | Build PDF, testing esempi | `Assembly/main.pdf` compilato |
| **22-28 Nov** | Soluzioni, esempi standalone | Appendice completa |
| **29-05 Dic** | Descrittori AI, validazione | 20-25 descriptors JSON |

### Dicembre 2025

| Settimana | Attività | Deliverable |
|-----------|----------|-------------|
| **06-12 Dic** | Progetti completi, Makefile | 5 progetti funzionanti |
| **13-19 Dic** | Ottimizzazione, correzioni | PDF finale ottimizzato |
| **20-25 Dic** | Release finale, documentazione | Corso pronto per studenti |

---

## 🎓 Percorso di Apprendimento Consigliato

### Modulo 1: Introduzione (Settimane 1-2)

**Obiettivi**:
- Comprendere architettura 8086
- Installare e configurare EMU8086/NASM
- Scrivere primo programma "Hello World"

**Capitoli**: 1-3
**Esercizi**: B.1-B.6

### Modulo 2: Programmazione Base (Settimane 3-5)

**Obiettivi**:
- Usare istruzioni fondamentali (MOV, ADD, SUB)
- Implementare loop con LOOP e Jcc
- Input/output con INT 21h

**Capitoli**: 4-5
**Esercizi**: B.1-B.6, I.1-I.3

### Modulo 3: Controllo e Logica (Settimane 6-7)

**Obiettivi**:
- Operazioni bit-level (AND, OR, XOR, shift)
- Salti condizionali (signed vs unsigned)
- Procedure semplici

**Capitoli**: 6-7
**Esercizi**: I.4-I.7

### Modulo 4: Tecniche Avanzate (Settimane 8-10)

**Obiettivi**:
- Stack frame e procedure con parametri
- Ricorsione
- Operazioni su stringhe con REP

**Capitoli**: 8-9
**Esercizi**: A.1-A.3

### Modulo 5: System Programming (Settimane 11-12)

**Obiettivi**:
- Sistema interrupt (IVT, INT 21h/10h)
- I/O hardware (PIC, PIT, UART)
- Bootloader minimale

**Capitoli**: 10-11
**Esercizi**: A.4-A.7, P.1-P.5

---

## 📊 Metriche di Qualità

### Contenuti

- **Capitoli**: 13 + 3 appendici = 16 file
- **Pagine LaTeX**: ~6.000 righe
- **Esempi codice**: 150+
- **Esercizi**: 80+
- **Progetti**: 5 completi
- **Diagrammi**: 20+ (TikZ)

### Copertura Argomenti

| Argomento | Livello | Capitoli |
|-----------|---------|----------|
| Architettura 8086 | ⭐⭐⭐⭐⭐ | 1-3 |
| Set istruzioni | ⭐⭐⭐⭐⭐ | 4-7 |
| Procedure e stack | ⭐⭐⭐⭐⭐ | 8 |
| Stringhe | ⭐⭐⭐⭐ | 9 |
| Interrupt | ⭐⭐⭐⭐ | 10 |
| Hardware I/O | ⭐⭐⭐ | 11 |
| Progetti | ⭐⭐⭐⭐ | 12-13 |

### Target Studenti

- **Livello**: Avanzato (5° anno)
- **Prerequisiti**: C, Java, Architettura
- **Difficoltà**: 🔴🔴🔴🔴⚪ (4/5)
- **Ore stimate**: 60h (teoria + lab)

---

## 🔄 Integrazioni con Altri Corsi

### Prerequisiti dai Corsi Precedenti

- **C (3° anno)**: Puntatori, memoria, funzioni
- **Java (4° anno)**: OOP, debugging, strutture dati
- **Database (4°/5°)**: Ottimizzazione query (analogia ottimizzazione Assembly)

### Applicazioni Successive

- **Sistemi Operativi**: Comprensione kernel, driver
- **Embedded Systems**: Programmazione microcontrollori (ARM, AVR)
- **Sicurezza**: Reverse engineering, exploit development
- **Real-time Systems**: Ottimizzazione performance-critical code

---

## 🚀 Post-Release (Gen-Feb 2026)

### Manutenzione

- Correzione errori segnalati da studenti
- Aggiornamento esempi per nuovi assembler
- Miglioramento diagrammi

### Espansioni Opzionali

- Capitolo su 80286 (protected mode)
- Capitolo su 80386 (32-bit)
- Integrazione con Arduino/Raspberry Pi
- Video tutorial per concetti chiave

---

## 📞 Contatti e Feedback

- **Issues GitHub**: Segnalazione errori e proposte
- **Email docenti**: Supporto studenti
- **Forum ITS**: Discussioni e Q&A

---

**Responsabile Progetto**: ITS Antonio Scarpa
**Creato**: 14 Novembre 2025
**Target Release**: 25 Dicembre 2025

---

**Note**: L'Assembly 8086 è un linguaggio storico ma estremamente formativo. Obiettivo del corso è fornire basi solide per programmazione low-level e comprensione architetture moderne.
