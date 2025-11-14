# 🖥️ Programmazione Assembly 8086

[![LaTeX](https://img.shields.io/badge/LaTeX-PDF-green.svg)](https://www.latex-project.org/)
[![Status](https://img.shields.io/badge/Status-Nuovo_Corso-blue.svg)](../MASTER-TODO.md)
[![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red.svg)](#)
[![Pages](https://img.shields.io/badge/Pages-~450-informational.svg)](#)

Corso completo di programmazione Assembly 8086 per l'Istituto Tecnico Superiore Antonio Scarpa. Copre architettura hardware, set di istruzioni, tecniche avanzate e progetti pratici.

---

## 📋 Informazioni Generali

| **Proprietà** | **Valore** |
|---------------|------------|
| **Anno Scolastico** | 2025-2026 |
| **Livello** | Avanzato (5° anno) |
| **Prerequisiti** | C, Java, Architettura dei Calcolatori |
| **Durata Stimata** | 60 ore (teoria + laboratorio) |
| **Capitoli** | 13 + Appendici |
| **Esercizi** | 80+ |
| **Progetti** | 5 progetti completi |

---

## 🎯 Obiettivi del Corso

Al termine del corso, lo studente sarà in grado di:

1. **Comprendere l'architettura 8086**: registri, segmenti, memoria, flag
2. **Programmare in Assembly**: scrivere, assemblare ed eseguire programmi
3. **Gestire procedure e stack**: chiamate a funzione, passaggio parametri
4. **Manipolare stringhe**: operazioni MOVSB, LODSB, STOSB, REP
5. **Programmare interrupt**: INT 21h (DOS), INT 10h (BIOS), handler custom
6. **Interfacciarsi con hardware**: porte I/O, PIC, PIT, UART, VGA
7. **Ottimizzare codice**: tecniche per massimizzare performance
8. **Debugging avanzato**: analisi con debugger, disassemblaggio

---

## 📚 Struttura del Corso

### Parte I: Fondamenti dell'Architettura 8086

| Capitolo | Titolo | Argomenti | Esercizi |
|----------|--------|-----------|----------|
| **Cap. 1** | Architettura del Microprocessore 8086 | CPU specs, BIU/EU, memoria segmentata, flag register, pinout | 5 |
| **Cap. 2** | Registri e Organizzazione della Memoria | AX-DX, SP/BP/SI/DI, CS/DS/SS/ES, layout .COM/.EXE | 5 |
| **Cap. 3** | Modalità di Indirizzamento | Immediate, register, direct, indirect, based, indexed | 5 |

### Parte II: Set di Istruzioni 8086

| Capitolo | Titolo | Argomenti | Esercizi |
|----------|--------|-----------|----------|
| **Cap. 4** | Istruzioni di Trasferimento Dati | MOV, XCHG, LEA, PUSH/POP, IN/OUT, XLAT | 5 |
| **Cap. 5** | Istruzioni Aritmetiche | ADD/SUB, MUL/DIV, INC/DEC, NEG, CMP, multi-precisione | 5 |
| **Cap. 6** | Istruzioni Logiche e Bit Manipulation | AND/OR/XOR/NOT, TEST, shift (SHL/SHR), rotate (ROL/ROR) | 5 |
| **Cap. 7** | Istruzioni di Controllo di Flusso | JMP, Jcc (conditional), LOOP, CALL/RET, INT/IRET | 5 |

### Parte III: Tecniche di Programmazione

| Capitolo | Titolo | Argomenti | Esercizi |
|----------|--------|-----------|----------|
| **Cap. 8** | Procedure e Gestione dello Stack | Stack frame, passaggio parametri, variabili locali, ricorsione | 5 |
| **Cap. 9** | Operazioni su Stringhe | MOVSB/W, LODSB/W, STOSB/W, CMPSB/W, SCASB/W, REP, CLD/STD | 5 |
| **Cap. 10** | Sistema di Interrupt | IVT, INT 21h (DOS), INT 10h/16h/13h (BIOS), handler custom | 5 |
| **Cap. 11** | I/O e Interfacciamento Hardware | PIC 8259, PIT 8253/54, LPT, UART 16550, tastiera, VGA | 5 |

### Parte IV: Progetti e Applicazioni

| Capitolo | Titolo | Argomenti | Esercizi |
|----------|--------|-----------|----------|
| **Cap. 12** | Progetti Applicativi | Calcolatrice, sorting, editor, gioco Snake, bootloader | 5 |
| **Cap. 13** | Esercizi Progressivi | 80+ esercizi: base (20), intermedi (20), avanzati (20), progetti (20) | 80+ |

### Appendici

| Appendice | Titolo | Descrizione |
|-----------|--------|-------------|
| **App. A** | Soluzioni agli Esercizi | Soluzioni dettagliate con spiegazioni passo-passo |
| **App. B** | Quick Reference | Tabelle riassuntive: registri, istruzioni, interrupt, ASCII |
| **App. C** | Bibliografia e Risorse | Manuali, libri, tutorial, tool, comunità online |

---

## 🛠️ Strumenti e Software

### Assembler

- **EMU8086** (consigliato): Emulatore con IDE integrato
  - Download: https://emu8086-microprocessor-emulator.en.softonic.com/
  - Features: assembler, debugger, visualizzazione registri/memoria
- **NASM**: Netwide Assembler, open-source multi-piattaforma
  - Install: `sudo apt-get install nasm` (Linux)
  - Sintassi: Intel syntax
- **MASM**: Microsoft Macro Assembler
  - Integrato in Visual Studio
- **TASM**: Turbo Assembler (Borland)

### Emulatori

- **DOSBox**: Emulatore DOS per eseguire programmi .COM e .EXE
  - Install: `sudo apt-get install dosbox`
  - Run: `dosbox`, poi `mount c ~/assembly`
- **QEMU**: Emulatore completo x86
- **Bochs**: Emulatore x86 con debugging avanzato

### Debugger

- **Debug.exe**: Debugger DOS integrato
- **TD (Turbo Debugger)**: Debugger Borland con interfaccia
- **GDB**: GNU Debugger (con supporto x86)
- **OllyDbg**: Debugger Windows per reverse engineering

### Editor

- **VS Code** con estensione **ASM Code Lens**
- **Notepad++** con syntax highlighting Assembly
- **EMU8086 IDE** (built-in)
- **TASM IDE**

---

## 🚀 Quick Start

### Compilare il PDF

```bash
cd Assembly
latexmk -pdf main.tex

# Oppure con pdflatex (3 passate)
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

### Primo Programma: Hello World (.COM)

```asm
ORG 100h               ; Offset per programma .COM

start:
    MOV AH, 09h        ; Funzione DOS: stampa stringa
    MOV DX, OFFSET msg
    INT 21h            ; Chiama DOS

    MOV AH, 4Ch        ; Funzione DOS: termina programma
    INT 21h

msg DB 'Hello, Assembly!$'
```

**Assemblare ed eseguire** (EMU8086):
1. Aprire EMU8086
2. Copia codice nell'editor
3. Clicca **Compile** → **Run**

**Con NASM**:
```bash
nasm -f bin hello.asm -o hello.com
dosbox hello.com
```

### Primo Programma: Hello World (.EXE)

```asm
.MODEL SMALL
.STACK 100h

.DATA
msg DB 'Hello, Assembly!$'

.CODE
main PROC
    MOV AX, @DATA
    MOV DS, AX         ; Inizializza segmento dati

    MOV AH, 09h
    MOV DX, OFFSET msg
    INT 21h

    MOV AH, 4Ch
    INT 21h
main ENDP

END main
```

---

## 📊 Contenuti Dettagliati

### Argomenti Fondamentali

#### Architettura
- Modello Bus Interface Unit (BIU) / Execution Unit (EU)
- Pipeline a 2 stadi con instruction queue (6 byte)
- Bus dati 16 bit, bus indirizzi 20 bit
- Memoria indirizzabile: 1 MB (2^20)
- Calcolo indirizzo fisico: `Segmento × 16 + Offset`

#### Registri
- **General Purpose**: AX, BX, CX, DX (divisibili in H/L)
- **Pointer/Index**: SP, BP, SI, DI, IP
- **Segment**: CS, DS, SS, ES
- **FLAGS**: CF, ZF, SF, OF, PF, AF, IF, DF, TF

#### Set di Istruzioni
- **Trasferimento dati**: MOV, XCHG, LEA, PUSH/POP, IN/OUT
- **Aritmetiche**: ADD, SUB, MUL, DIV, INC, DEC, NEG, CMP
- **Logiche**: AND, OR, XOR, NOT, TEST, SHL/SHR, ROL/ROR
- **Controllo flusso**: JMP, Jcc, LOOP, CALL/RET, INT
- **Stringhe**: MOVSB/W, LODSB/W, STOSB/W, CMPSB/W, SCASB/W

### Tecniche Avanzate

#### Procedure
- Convenzioni di chiamata (caller/callee)
- Passaggio parametri via stack
- Stack frame con BP
- Variabili locali
- Ricorsione (fattoriale, Fibonacci, Hanoi)

#### Gestione Interrupt
- Interrupt Vector Table (IVT) a 0000:0000
- Software interrupt (INT n)
- Hardware interrupt (IRQ con PIC 8259)
- Handler personalizzati
- INT 21h (DOS): funzioni 01h, 02h, 09h, 4Ch
- INT 10h (Video): funzioni 00h, 0Eh
- INT 16h (Tastiera): funzione 00h

#### Hardware I/O
- Porte I/O (IN/OUT)
- PIC 8259: mascheratura interrupt (IMR)
- PIT 8253/54: timer programmabile, generazione beep
- UART 16550: comunicazione seriale COM1/COM2
- Porta parallela LPT1
- Controller tastiera 8042
- VGA: accesso diretto memoria video B800:0000

### Progetti Completi

1. **Calcolatrice 16 bit**: +, -, *, / con input/output decimale
2. **Algoritmi di ordinamento**: Bubble sort, Quick sort
3. **Editor di testo minimale**: Buffer 256 char, insert/delete
4. **Gioco Snake**: Modalità testo 80×25, movimento, crescita
5. **Bootloader**: Boot sector 512 byte con firma 0xAA55

---

## 🎓 Percorso di Apprendimento

### Livello Base (Settimane 1-4)

**Obiettivi**:
- Comprendere architettura 8086
- Scrivere programmi semplici con MOV, ADD, SUB
- Usare LOOP e salti condizionali
- Input/output con INT 21h

**Esercizi consigliati**: B.1-B.6

### Livello Intermedio (Settimane 5-8)

**Obiettivi**:
- Procedure con CALL/RET
- Operazioni su stringhe
- Moltiplicazione/divisione
- Array e struct

**Esercizi consigliati**: I.1-I.7

### Livello Avanzato (Settimane 9-12)

**Obiettivi**:
- Ricorsione
- Interrupt personalizzati
- I/O hardware
- Ottimizzazione codice

**Esercizi consigliati**: A.1-A.7, Progetti P.1-P.5

---

## 📖 Convenzioni di Codifica

### Sintassi Intel (NASM/MASM/TASM)

```asm
; Commento su singola riga

MOV dest, src          ; Destinazione a sinistra

; Segmento dati
.DATA
var1 DW 1234h          ; Word (16 bit)
array DB 1,2,3,4,5     ; Byte array
msg DB 'Hello$'        ; Stringa terminata con $

; Segmento codice
.CODE
main PROC
    ; Corpo procedura
    RET
main ENDP
```

### Naming Conventions

- **Label**: `snake_case` o `camelCase` (es: `loop_start`, `printNumber`)
- **Costanti**: `MAIUSCOLO_UNDERSCORE` (es: `MAX_SIZE`, `BUFFER_LEN`)
- **Variabili**: `snake_case` (es: `counter`, `user_input`)

### Commenti

```asm
; Commento breve inline
MOV AX, 10             ; Carica 10 in AX

; Blocco di commento:
; Questa procedura calcola il fattoriale di AX
; Input: AX = n
; Output: AX = n!
; Modifica: AX, CX
factorial PROC
    ; ...
    RET
factorial ENDP
```

---

## 🔗 Risorse Utili

### Documentazione Ufficiale

- **Intel 8086/8088 User's Manual**: https://www.intel.com/
- **NASM Documentation**: https://www.nasm.us/docs.php
- **OSDev Wiki**: https://wiki.osdev.org/

### Tutorial Online

- **Tutorialspoint Assembly**: https://www.tutorialspoint.com/assembly_programming/
- **x86 Assembly Guide (Yale)**: https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html

### Compilatori Online

- **Online x86 Assembler**: https://defuse.ca/online-x86-assembler.htm
- **Compiler Explorer (Godbolt)**: https://godbolt.org/

### Community

- **Stack Overflow** [assembly] tag
- **Reddit r/asm**: https://www.reddit.com/r/asm/
- **OSDev Forums**: https://forum.osdev.org/

---

## 📈 Statistiche del Corso

- **Capitoli**: 13 + 3 appendici = 16 file `.tex`
- **Pagine stimate**: ~450
- **Esercizi**: 80+ (20 base + 20 intermedi + 20 avanzati + 20 progetti)
- **Esempi di codice**: 150+
- **Diagrammi TikZ**: 20+
- **Tabelle riassuntive**: 30+
- **Progetti completi**: 5

---

## 🤖 Descrittori AI (Pianificati)

**Status**: ⏳ **DA GENERARE** (previsti 20-25 descrittori)

Categorie pianificate:
1. **Architecture** (3-4 descriptors): Registri, segmentazione, modalità indirizzamento
2. **Instruction Set** (8-10 descriptors): Gruppi istruzioni (data, arithmetic, logical, control, string)
3. **Advanced Techniques** (4-5 descriptors): Procedure, interrupt, I/O
4. **Optimization** (2-3 descriptors): Performance tuning, code golf
5. **Hardware Interfacing** (3-4 descriptors): PIC, PIT, UART, VGA

**Deadline**: 2025-12-10

---

## 📝 Esercizi per Capitolo

### Riepilogo Tipologia

| Livello | Numero | Esempi |
|---------|--------|--------|
| **Base** | 20 | Hello World, somma numeri, pari/dispari, massimo, copia stringa |
| **Intermedio** | 20 | Fattoriale, Fibonacci, numeri primi, ricerca binaria, palindromo |
| **Avanzato** | 20 | Torre di Hanoi, matrici, parser espressioni, allocatore memoria, compressione |
| **Progetti** | 20 | Calcolatrice, sorting, editor, Snake, bootloader, OS minimale |

### Esercizi Sfida

- **Code Golf**: Programmi più corti possibili
- **Performance**: Ottimizzazione per velocità massima
- **Reverse Engineering**: Analisi binari forniti
- **Real Mode OS**: Sistema operativo completo

---

## 🔄 Storico Modifiche

- **2025-11-14**: Creazione corso Assembly 8086 completo (16 file LaTeX, 80+ esercizi)

---

## 📄 Licenza

Materiale didattico per uso educativo.

**Istituto Tecnico Superiore Antonio Scarpa** — Anno Scolastico 2025-2026

---

## 👥 Contributori

- **Docenti**: Istituto Tecnico Superiore Antonio Scarpa
- **Studenti**: Feedback e testing

---

**Versione**: 1.0 | **Data**: 14 Novembre 2025 | **Ultima Compilazione PDF**: ⏳ Pending

---

## ⭐ Note Finali

L'Assembly 8086 è la base per comprendere:
- Funzionamento interno dei processori moderni
- Reverse engineering e sicurezza informatica
- Sviluppo di sistemi operativi
- Programmazione embedded
- Ottimizzazione di codice ad alte prestazioni

**L'Assembly è difficile ma incredibilmente formativo!** 💪

---

[⬆ Torna su](#-programmazione-assembly-8086)
