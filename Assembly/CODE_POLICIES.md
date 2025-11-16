# Code Policies - Assembly

> Standard, convenzioni e politiche di scrittura del codice per il libro su Assembly

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Codice](#template-di-codice)
- [Struttura dei File](#struttura-dei-file)
- [Best Practices](#best-practices)
- [Pattern di Programmazione](#pattern-di-programmazione)
- [Ottimizzazione](#ottimizzazione)
- [Commenti e Documentazione](#commenti-e-documentazione)

---

## Standard di Scrittura

### Formattazione
- **Indentazione**: 4 spazi o 1 tab per livelli di scope
- **Allineamento**: Colonne per label, instruction, operands, comments
- **Case**: Preferire lowercase per istruzioni (o UPPERCASE, ma consistente)
- **Encoding**: UTF-8 or ASCII
- **Fine riga**: LF (Unix)

### Stile del Codice (x86-64 NASM Syntax)
```asm
; ============================================================================
; File: example.asm
; Description: Example assembly program
; Author: Nome Autore
; Date: 2025-11-16
; ============================================================================

section .data
    ; === DATA CONSTANTS ===
    msg         db      'Hello, World!', 0x0A
    msg_len     equ     $ - msg
    newline     db      0x0A

section .bss
    ; === UNINITIALIZED DATA ===
    buffer      resb    256
    counter     resd    1

section .text
    global _start

; ============================================================================
; Function: _start
; Description: Program entry point
; Parameters: None
; Returns: Exit code in RAX
; ============================================================================
_start:
    ; === Print message ===
    mov     rax, 1              ; sys_write
    mov     rdi, 1              ; stdout
    mov     rsi, msg            ; message buffer
    mov     rdx, msg_len        ; message length
    syscall

    ; === Exit program ===
    mov     rax, 60             ; sys_exit
    xor     rdi, rdi            ; exit code 0
    syscall

; ============================================================================
; Function: strlen
; Description: Calculate string length
; Parameters: RSI = pointer to null-terminated string
; Returns: RAX = string length
; Clobbers: RCX, RDI
; ============================================================================
strlen:
    push    rbx                 ; Save callee-saved register

    xor     rax, rax            ; length = 0
    mov     rdi, rsi            ; Copy pointer

.loop:
    cmp     byte [rdi], 0       ; Check for null terminator
    je      .done               ; If null, we're done
    inc     rax                 ; Increment length
    inc     rdi                 ; Next character
    jmp     .loop

.done:
    pop     rbx                 ; Restore register
    ret
```

### Regole Generali
- [ ] Sempre commentare istruzioni non ovvie
- [ ] Preservare registri callee-saved
- [ ] Allineare dati quando appropriato
- [ ] Usare macro per codice ripetitivo
- [ ] Documentare convenzioni di chiamata

---

## Convenzioni di Nomenclatura

### Labels e Simboli
- **Global labels**: `snake_case` - Esempio: `main`, `print_string`
- **Local labels**: `.name` - Esempio: `.loop`, `.done`, `.error`
- **Constants**: `UPPER_SNAKE_CASE` - Esempio: `BUFFER_SIZE`, `MAX_VALUE`
- **Section labels**: descrittivi - Esempio: `.data`, `.text`, `.rodata`

### Variabili e Dati
- **Variables**: `snake_case` - Esempio: `user_input`, `total_count`
- **Constants (equ)**: `UPPER_SNAKE_CASE` - Esempio: `MSG_LEN`, `NULL`
- **Buffers**: `_buf` suffix - Esempio: `input_buf`, `output_buf`

### Funzioni
- **Funzioni**: `snake_case` - Esempio: `calculate_sum`, `read_input`
- **Syscall wrappers**: `sys_` prefix - Esempio: `sys_read`, `sys_write`
- **Helper functions**: `_` prefix - Esempio: `_internal_helper`

### Registri (Documentare Uso)
```asm
; Convenzione System V AMD64 (Linux):
; RAX    - return value, syscall number
; RBX    - callee-saved
; RCX    - 4th argument
; RDX    - 3rd argument
; RSI    - 2nd argument
; RDI    - 1st argument
; RBP    - base pointer (callee-saved)
; RSP    - stack pointer
; R8-R9  - 5th, 6th arguments
; R10-R11- temporary
; R12-R15- callee-saved
```

---

## Template di Codice

### Template File Base (NASM x86-64)
```asm
; ============================================================================
; File: program.asm
; Description: Brief description of the program
; Architecture: x86-64
; Assembler: NASM
; OS: Linux
; Author: Nome Autore
; Date: 2025-11-16
; ============================================================================

; === CONSTANTS ===
%define BUFFER_SIZE     256
%define SYS_READ        0
%define SYS_WRITE       1
%define SYS_EXIT        60
%define STDIN           0
%define STDOUT          1
%define STDERR          2

section .data
    ; === READ-ONLY DATA ===
    welcome_msg     db      'Welcome!', 0x0A
    welcome_len     equ     $ - welcome_msg

section .bss
    ; === UNINITIALIZED DATA ===
    buffer          resb    BUFFER_SIZE

section .text
    global _start

; ============================================================================
; Function: _start
; Description: Program entry point
; ============================================================================
_start:
    ; === Initialize ===
    call    init

    ; === Main logic ===
    call    main_loop

    ; === Exit ===
    mov     rax, SYS_EXIT
    xor     rdi, rdi
    syscall

; ============================================================================
; Function: init
; Description: Initialize program state
; Parameters: None
; Returns: None
; ============================================================================
init:
    ; Initialization code
    ret

; ============================================================================
; Function: main_loop
; Description: Main program loop
; Parameters: None
; Returns: None
; ============================================================================
main_loop:
    ; Main logic
    ret
```

### Template Funzione
```asm
; ============================================================================
; Function: function_name
; Description: Detailed description of what this function does
;
; Parameters:
;   RDI - First parameter (description)
;   RSI - Second parameter (description)
;   RDX - Third parameter (description)
;
; Returns:
;   RAX - Return value (description)
;
; Clobbers: RCX, R8, R9
; Preserves: RBX, R12-R15
;
; Example:
;   mov     rdi, buffer
;   mov     rsi, 10
;   call    function_name
; ============================================================================
function_name:
    ; === Function prologue ===
    push    rbp
    mov     rbp, rsp
    push    rbx                 ; Save callee-saved registers
    push    r12

    ; === Local variables ===
    sub     rsp, 16             ; Reserve stack space

    ; === Function body ===
    ; ... implementation ...

    ; === Function epilogue ===
    add     rsp, 16             ; Restore stack
    pop     r12
    pop     rbx
    pop     rbp
    ret
```

### Template Macro
```asm
; ============================================================================
; Macro: print_string
; Description: Print a null-terminated string to stdout
; Parameters:
;   %1 - Address of string
; ============================================================================
%macro print_string 1
    push    rax
    push    rdi
    push    rsi
    push    rdx

    mov     rsi, %1             ; String address
    call    strlen              ; Get length in RAX
    mov     rdx, rax            ; Length
    mov     rax, SYS_WRITE
    mov     rdi, STDOUT
    syscall

    pop     rdx
    pop     rsi
    pop     rdi
    pop     rax
%endmacro
```

---

## Struttura dei File

### Organizzazione File Assembly
```
1. File header comment
2. Constant definitions (%define, equ)
3. External declarations (extern)
4. Macro definitions
5. .data section (initialized data)
6. .rodata section (read-only data)
7. .bss section (uninitialized data)
8. .text section
   - global declarations
   - _start or main
   - Public functions
   - Private functions
   - Helper functions
```

### Organizzazione Progetto
```
project/
├── src/
│   ├── main.asm
│   ├── utils.asm
│   └── syscalls.asm
├── include/
│   ├── constants.inc
│   └── macros.inc
├── lib/
│   └── stdlib.asm
├── build/
│   └── (object files)
├── Makefile
└── README.md
```

### Include File
```asm
; ============================================================================
; File: constants.inc
; Description: Common constants and definitions
; ============================================================================

%ifndef CONSTANTS_INC
%define CONSTANTS_INC

; === System call numbers ===
%define SYS_READ        0
%define SYS_WRITE       1
%define SYS_OPEN        2
%define SYS_CLOSE       3
%define SYS_EXIT        60

; === File descriptors ===
%define STDIN           0
%define STDOUT          1
%define STDERR          2

; === Buffer sizes ===
%define SMALL_BUF       64
%define MEDIUM_BUF      256
%define LARGE_BUF       1024

%endif ; CONSTANTS_INC
```

---

## Best Practices

### Gestione Registri
- [ ] Documentare quali registri sono modificati
- [ ] Salvare e ripristinare registri callee-saved (RBX, R12-R15, RBP)
- [ ] Non assumere valore dei registri caller-saved
- [ ] Usare push/pop per salvare registri
- [ ] Allineare stack a 16 byte prima di chiamate

### Stack Management
```asm
; Corretto stack alignment (System V AMD64)
function:
    push    rbp
    mov     rbp, rsp
    ; Stack è 16-byte aligned qui (dopo push rbp + call)

    ; Se servono variabili locali, allineare a 16
    sub     rsp, 32             ; Multiple di 16

    ; ... codice ...

    leave                       ; mov rsp, rbp; pop rbp
    ret
```

### Sicurezza
- [ ] Validare input
- [ ] Controllare buffer overflow
- [ ] Azzerare dati sensibili dopo l'uso
- [ ] Non eseguire codice su stack (NX bit)
- [ ] Evitare shellcode patterns se non necessario

### Performance
- [ ] Usare registri invece di memoria quando possibile
- [ ] Minimizzare accessi a memoria
- [ ] Allineare dati a boundary appropriati
- [ ] Usare istruzioni SIMD quando appropriato
- [ ] Evitare branch misprediction

---

## Pattern di Programmazione

### Pattern 1: String Length
```asm
strlen:
    xor     rax, rax            ; counter = 0
    mov     rcx, -1             ; max count
    mov     rdi, rsi            ; string pointer
    xor     al, al              ; search for null
    repne   scasb               ; repeat while not equal
    not     rcx                 ; invert count
    dec     rcx                 ; adjust for null
    mov     rax, rcx            ; return length
    ret
```

### Pattern 2: Memory Copy
```asm
; memcpy(dest=RDI, src=RSI, count=RDX)
memcpy:
    push    rcx
    push    rsi
    push    rdi

    mov     rcx, rdx            ; count
    rep     movsb               ; copy byte by byte

    pop     rdi
    pop     rsi
    pop     rcx
    ret
```

### Pattern 3: Loop Pattern
```asm
array_sum:
    xor     rax, rax            ; sum = 0
    xor     rcx, rcx            ; index = 0

.loop:
    cmp     rcx, rsi            ; index < count?
    jge     .done               ; if not, exit

    add     rax, [rdi + rcx*4]  ; sum += array[i]
    inc     rcx                 ; i++
    jmp     .loop

.done:
    ret
```

### Pattern 4: Conditional Execution
```asm
; if (a > b) return 1; else return 0;
compare:
    xor     rax, rax            ; default return 0
    cmp     rdi, rsi            ; compare a, b
    jle     .done               ; if a <= b, return 0
    inc     rax                 ; else return 1
.done:
    ret
```

---

## Ottimizzazione

### Ottimizzazioni Comuni
```asm
; === Zeroing register ===
; Lento:
mov     rax, 0

; Veloce (più corto e veloce):
xor     rax, rax

; === Test for zero ===
; Lento:
cmp     rax, 0
je      .zero

; Veloce:
test    rax, rax
jz      .zero

; === Multiply by power of 2 ===
; Lento:
imul    rax, 8

; Veloce:
shl     rax, 3

; === Loop unrolling ===
; Normale:
.loop:
    mov     [rdi], eax
    add     rdi, 4
    dec     rcx
    jnz     .loop

; Unrolled (4x):
.loop:
    mov     [rdi], eax
    mov     [rdi+4], eax
    mov     [rdi+8], eax
    mov     [rdi+12], eax
    add     rdi, 16
    sub     rcx, 4
    jnz     .loop
```

### SIMD Example (SSE/AVX)
```asm
; Somma vettoriale con SSE
vector_add:
    ; RDI = dest, RSI = src1, RDX = src2, RCX = count
    shr     rcx, 2              ; count / 4 (4 floats at time)

.loop:
    movups  xmm0, [rsi]         ; Load 4 floats from src1
    movups  xmm1, [rdx]         ; Load 4 floats from src2
    addps   xmm0, xmm1          ; Add packed singles
    movups  [rdi], xmm0         ; Store result

    add     rsi, 16
    add     rdx, 16
    add     rdi, 16
    dec     rcx
    jnz     .loop

    ret
```

---

## Commenti e Documentazione

### Header File
```asm
; ============================================================================
; File: program.asm
; Description: Detailed description of the program's purpose
;
; Purpose:
;   - Main objective 1
;   - Main objective 2
;
; Architecture: x86-64 (AMD64)
; Assembler: NASM 2.15+
; Linker: ld
; OS: Linux
;
; Build:
;   nasm -f elf64 program.asm -o program.o
;   ld program.o -o program
;
; Author: Nome Autore
; Date: 2025-11-16
; Version: 1.0.0
;
; Dependencies:
;   - Linux kernel 3.0+
;   - None (standalone)
;
; Notes:
;   - Uses System V AMD64 calling convention
;   - Requires 16-byte stack alignment
; ============================================================================
```

### Commenti Inline
```asm
; === SECTION HEADER ===
section .text

; Commento su istruzione specifica
mov     rax, 1              ; sys_write syscall number

; Commento multi-linea
; This section implements the Euclidean algorithm for computing
; the greatest common divisor (GCD) of two integers.
; Algorithm: gcd(a,b) = gcd(b, a mod b), with base case gcd(a,0) = a

; TODO: Optimize with SSE instructions
; FIXME: Stack alignment issue on some systems
; NOTE: This code assumes little-endian architecture
; HACK: Workaround for NASM bug #1234
```

### Documentazione Algoritmo
```asm
; ============================================================================
; Algorithm: Bubble Sort
; Complexity: O(n²) average and worst case, O(n) best case
; Space: O(1)
;
; Description:
;   Repeatedly steps through the array, compares adjacent elements and swaps
;   them if they are in wrong order. Pass through the array is repeated until
;   the array is sorted.
;
; Pseudocode:
;   for i = 0 to n-1:
;       for j = 0 to n-i-1:
;           if array[j] > array[j+1]:
;               swap(array[j], array[j+1])
; ============================================================================
bubble_sort:
    ; Implementation
```

---

## Note Aggiuntive

### Architetture Target
- **x86-64 (AMD64)**: Principale (64-bit)
- **x86 (IA-32)**: Legacy (32-bit)
- **ARM64**: Mobile/embedded

### Assembler
- **NASM**: Netwide Assembler (Intel syntax)
- **GAS**: GNU Assembler (AT&T syntax)
- **MASM**: Microsoft Macro Assembler
- **YASM**: NASM-compatible

### Tool
- **Debugger**: GDB, radare2, x64dbg
- **Disassembler**: objdump, IDA Pro, Ghidra
- **Emulator**: QEMU, Bochs
- **Profiler**: perf, VTune

### Build Example (Makefile)
```makefile
AS = nasm
ASFLAGS = -f elf64 -g -F dwarf
LD = ld
LDFLAGS =

TARGET = program
SOURCES = main.asm utils.asm
OBJECTS = $(SOURCES:.asm=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(LD) $(LDFLAGS) -o $@ $^

%.o: %.asm
	$(AS) $(ASFLAGS) -o $@ $<

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: all clean
```

### Riferimenti
- Intel® 64 and IA-32 Architectures Software Developer's Manual
- AMD64 Architecture Programmer's Manual
- System V AMD64 ABI
- NASM Documentation

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
