#!/bin/bash

################################################################################
# Script di Compilazione Batch PDF - Repository Appunti
#
# Compila automaticamente i PDF di tutti i 9 nuovi corsi (2025)
# con gestione errori, logging e report finale
#
# Autore: ITS Antonio Scarpa
# Data: 15 Novembre 2025
# Versione: 1.0
################################################################################

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directory principale
BASE_DIR="/home/user/Appunti"

# Directory di log
LOG_DIR="$BASE_DIR/logs"
mkdir -p "$LOG_DIR"

# File di log principale
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
MAIN_LOG="$LOG_DIR/compile_batch_$TIMESTAMP.log"
ERROR_LOG="$LOG_DIR/compile_errors_$TIMESTAMP.log"
REPORT_FILE="$LOG_DIR/compile_report_$TIMESTAMP.md"

# Corsi da compilare (ordinati per deadline)
declare -a COURSES=(
    "Database:2025-12-05:MEDIA"
    "Algoritmi:2025-12-10:ALTA"
    "Assembly:2025-12-10:MEDIA"
    "WebSecurity:2025-12-15:ALTA"
    "Git:2025-12-15:MEDIA"
    "Linux:2025-12-15:MEDIA"
    "React:2025-12-18:ALTA"
    "RestAPI:2025-12-18:MEDIA"
    "Docker:2025-12-20:MEDIA"
)

# Contatori
TOTAL_COURSES=${#COURSES[@]}
SUCCESS_COUNT=0
FAIL_COUNT=0
SKIP_COUNT=0

# Array per risultati
declare -a SUCCESS_LIST
declare -a FAIL_LIST
declare -a SKIP_LIST

################################################################################
# Funzione: Print Header
################################################################################
print_header() {
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                                                                ║${NC}"
    echo -e "${BLUE}║           COMPILAZIONE BATCH PDF - REPOSITORY APPUNTI          ║${NC}"
    echo -e "${BLUE}║                                                                ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${YELLOW}Data avvio:${NC} $(date '+%d/%m/%Y %H:%M:%S')"
    echo -e "${YELLOW}Corsi da compilare:${NC} $TOTAL_COURSES"
    echo -e "${YELLOW}Log principale:${NC} $MAIN_LOG"
    echo -e "${YELLOW}Log errori:${NC} $ERROR_LOG"
    echo ""
}

################################################################################
# Funzione: Compila singolo PDF
################################################################################
compile_pdf() {
    local course_name=$1
    local deadline=$2
    local priority=$3
    local course_dir="$BASE_DIR/$course_name"
    local main_tex="$course_dir/main.tex"
    local main_pdf="$course_dir/main.pdf"

    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}Corso:${NC} $course_name"
    echo -e "${YELLOW}Deadline:${NC} $deadline | ${YELLOW}Priorità:${NC} $priority"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

    # Verifica directory corso
    if [ ! -d "$course_dir" ]; then
        echo -e "${RED}✗ ERRORE: Directory non trovata: $course_dir${NC}"
        SKIP_LIST+=("$course_name (directory non trovata)")
        ((SKIP_COUNT++))
        return 1
    fi

    # Verifica main.tex
    if [ ! -f "$main_tex" ]; then
        echo -e "${RED}✗ ERRORE: File main.tex non trovato in $course_dir${NC}"
        SKIP_LIST+=("$course_name (main.tex assente)")
        ((SKIP_COUNT++))
        return 1
    fi

    # Se PDF esiste già, chiedi conferma (modalità interattiva può essere disabilitata)
    if [ -f "$main_pdf" ]; then
        echo -e "${YELLOW}⚠ PDF già esistente: $main_pdf${NC}"
        echo -e "${YELLOW}  Verrà sovrascritto...${NC}"
    fi

    # Entra nella directory del corso
    cd "$course_dir" || return 1

    echo -e "${BLUE}→ Avvio compilazione con latexmk...${NC}"

    # Compilazione con latexmk
    START_TIME=$(date +%s)

    if latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >> "$MAIN_LOG" 2>&1; then
        END_TIME=$(date +%s)
        DURATION=$((END_TIME - START_TIME))

        # Verifica che il PDF sia stato generato
        if [ -f "$main_pdf" ]; then
            PDF_SIZE=$(du -h "$main_pdf" | cut -f1)
            echo -e "${GREEN}✓ SUCCESSO${NC}"
            echo -e "  Tempo: ${DURATION}s | Dimensione PDF: $PDF_SIZE"
            SUCCESS_LIST+=("$course_name ($PDF_SIZE, ${DURATION}s)")
            ((SUCCESS_COUNT++))

            # Controlla warning nel log
            if grep -q "LaTeX Warning" main.log 2>/dev/null; then
                WARNING_COUNT=$(grep -c "LaTeX Warning" main.log)
                echo -e "${YELLOW}  ⚠ Warning trovati: $WARNING_COUNT${NC}"
            fi
        else
            echo -e "${RED}✗ ERRORE: PDF non generato nonostante compilazione riuscita${NC}"
            FAIL_LIST+=("$course_name (PDF non generato)")
            ((FAIL_COUNT++))
        fi
    else
        END_TIME=$(date +%s)
        DURATION=$((END_TIME - START_TIME))

        echo -e "${RED}✗ ERRORE DI COMPILAZIONE${NC}"
        echo -e "  Tempo: ${DURATION}s"

        # Estrai errori dal log
        if [ -f "main.log" ]; then
            echo -e "\n═══ ERRORI: $course_name ═══" >> "$ERROR_LOG"
            grep -A 5 "^!" main.log >> "$ERROR_LOG" 2>/dev/null || echo "Nessun errore specifico trovato" >> "$ERROR_LOG"
            echo -e "═══════════════════════════════════\n" >> "$ERROR_LOG"
        fi

        FAIL_LIST+=("$course_name (compilazione fallita)")
        ((FAIL_COUNT++))
    fi

    # Torna alla directory base
    cd "$BASE_DIR" || exit 1
}

################################################################################
# Funzione: Genera Report Markdown
################################################################################
generate_report() {
    cat > "$REPORT_FILE" << EOF
# Report Compilazione Batch PDF

**Data**: $(date '+%d/%m/%Y %H:%M:%S')
**Script**: compile_all_pdfs.sh v1.0
**Corsi processati**: $TOTAL_COURSES

---

## 📊 Riepilogo

| Stato | Numero | Percentuale |
|-------|--------|-------------|
| ✅ Successo | $SUCCESS_COUNT | $(awk "BEGIN {printf \"%.1f\", ($SUCCESS_COUNT/$TOTAL_COURSES)*100}")% |
| ❌ Falliti | $FAIL_COUNT | $(awk "BEGIN {printf \"%.1f\", ($FAIL_COUNT/$TOTAL_COURSES)*100}")% |
| ⏭ Saltati | $SKIP_COUNT | $(awk "BEGIN {printf \"%.1f\", ($SKIP_COUNT/$TOTAL_COURSES)*100}")% |
| **Totale** | **$TOTAL_COURSES** | **100%** |

---

## ✅ Compilazioni Riuscite ($SUCCESS_COUNT)

EOF

    if [ ${#SUCCESS_LIST[@]} -gt 0 ]; then
        for item in "${SUCCESS_LIST[@]}"; do
            echo "- $item" >> "$REPORT_FILE"
        done
    else
        echo "*Nessuna compilazione riuscita*" >> "$REPORT_FILE"
    fi

    cat >> "$REPORT_FILE" << EOF

---

## ❌ Compilazioni Fallite ($FAIL_COUNT)

EOF

    if [ ${#FAIL_LIST[@]} -gt 0 ]; then
        for item in "${FAIL_LIST[@]}"; do
            echo "- $item" >> "$REPORT_FILE"
        done
        echo "" >> "$REPORT_FILE"
        echo "**Dettagli errori**: Vedi \`$ERROR_LOG\`" >> "$REPORT_FILE"
    else
        echo "*Nessun fallimento*" >> "$REPORT_FILE"
    fi

    cat >> "$REPORT_FILE" << EOF

---

## ⏭ Corsi Saltati ($SKIP_COUNT)

EOF

    if [ ${#SKIP_LIST[@]} -gt 0 ]; then
        for item in "${SKIP_LIST[@]}"; do
            echo "- $item" >> "$REPORT_FILE"
        done
    else
        echo "*Nessun corso saltato*" >> "$REPORT_FILE"
    fi

    cat >> "$REPORT_FILE" << EOF

---

## 📁 File di Log

- **Log principale**: \`$MAIN_LOG\`
- **Log errori**: \`$ERROR_LOG\`
- **Report**: \`$REPORT_FILE\`

---

## 🔧 Prossimi Passi

### Se ci sono errori di compilazione:

1. Leggere il log errori: \`cat $ERROR_LOG\`
2. Aprire il file \`main.log\` del corso specifico
3. Cercare righe che iniziano con \`!\` (errori LaTeX)
4. Correggere i problemi e ricompilare manualmente:
   \`\`\`bash
   cd [CORSO] && latexmk -pdf main.tex
   \`\`\`

### Se ci sono warning:

1. Leggere \`main.log\` del corso
2. Cercare \`LaTeX Warning\`
3. Valutare se sono bloccanti o solo cosmetici

### Prossime azioni suggerite:

- [ ] Verificare qualità PDF generati
- [ ] Controllare warning LaTeX
- [ ] Aggiornare MASTER-TODO.md con risultati
- [ ] Creare documentazione (README, TODO, PIANO_SVILUPPO) per corsi riusciti
- [ ] Generare descrittori AI per corsi con PDF completi

---

**Fine Report**
EOF
}

################################################################################
# Funzione: Print Summary
################################################################################
print_summary() {
    echo ""
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                     RIEPILOGO FINALE                           ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}✓ Successi:${NC} $SUCCESS_COUNT/$TOTAL_COURSES"
    echo -e "${RED}✗ Falliti:${NC} $FAIL_COUNT/$TOTAL_COURSES"
    echo -e "${YELLOW}⏭ Saltati:${NC} $SKIP_COUNT/$TOTAL_COURSES"
    echo ""
    echo -e "${YELLOW}Report generato:${NC} $REPORT_FILE"
    echo ""

    if [ $SUCCESS_COUNT -eq $TOTAL_COURSES ]; then
        echo -e "${GREEN}🎉 TUTTI I PDF COMPILATI CON SUCCESSO! 🎉${NC}"
    elif [ $SUCCESS_COUNT -gt 0 ]; then
        echo -e "${YELLOW}⚠ Compilazione parziale. Verificare errori.${NC}"
    else
        echo -e "${RED}❌ NESSUN PDF COMPILATO. Verificare configurazione.${NC}"
    fi
    echo ""
}

################################################################################
# MAIN EXECUTION
################################################################################

# Print header
print_header

# Log inizio
echo "═══════════════════════════════════════════════════════════════" > "$MAIN_LOG"
echo "COMPILAZIONE BATCH PDF - $(date)" >> "$MAIN_LOG"
echo "═══════════════════════════════════════════════════════════════" >> "$MAIN_LOG"
echo "" >> "$MAIN_LOG"

echo "" > "$ERROR_LOG"

# Loop attraverso i corsi
for course_info in "${COURSES[@]}"; do
    IFS=':' read -r course_name deadline priority <<< "$course_info"
    compile_pdf "$course_name" "$deadline" "$priority"
done

# Genera report
echo -e "\n${BLUE}→ Generazione report...${NC}"
generate_report

# Print summary
print_summary

# Exit con codice appropriato
if [ $FAIL_COUNT -gt 0 ] || [ $SKIP_COUNT -gt 0 ]; then
    exit 1
else
    exit 0
fi
