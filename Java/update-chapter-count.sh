#!/bin/bash

# Script di automazione per aggiornare conteggio capitoli nel README.md
# Progetto: Appunti Programmazione Java (Quarta)
# Data: 8 Novembre 2025

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHAPTER_DIR="$SCRIPT_DIR/capitoli"
README_FILE="$SCRIPT_DIR/README.md"
LOG_FILE="$SCRIPT_DIR/main.log"

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}Script: Aggiornamento Statistiche Capitoli${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# 1. Conteggio capitoli
echo -e "${YELLOW}[1/3] Conteggio capitoli in $CHAPTER_DIR...${NC}"
if [ ! -d "$CHAPTER_DIR" ]; then
    echo -e "${RED}ERRORE: Directory $CHAPTER_DIR non trovata!${NC}"
    exit 1
fi

TOTAL_CHAPTERS=$(ls -1 "$CHAPTER_DIR"/*.tex 2>/dev/null | wc -l)
TARGET_CHAPTERS=14
PERCENTAGE=$((TOTAL_CHAPTERS * 100 / TARGET_CHAPTERS))

echo -e "${GREEN}✅ Capitoli trovati: $TOTAL_CHAPTERS/$TARGET_CHAPTERS (${PERCENTAGE}%)${NC}"
echo ""

# 2. Analisi PDF se esiste
echo -e "${YELLOW}[2/3] Analisi PDF principale...${NC}"
PDF_FILE="$SCRIPT_DIR/main.pdf"

if [ -f "$PDF_FILE" ]; then
    PDF_SIZE=$(du -h "$PDF_FILE" | cut -f1)
    # Estrai numero pagine dal log se disponibile
    PAGE_COUNT="N/A"
    if [ -f "$LOG_FILE" ]; then
        PAGE_COUNT=$(grep "Output written on main.pdf" "$LOG_FILE" 2>/dev/null | grep -oE "[0-9]+ pages" | grep -oE "[0-9]+" | head -1 || echo "N/A")
    fi
    echo -e "${GREEN}✅ PDF trovato: $PDF_SIZE ($PAGE_COUNT pagine)${NC}"
else
    echo -e "${YELLOW}⚠️  PDF non trovato - sarà aggiornato al prossimo 'make pdf'${NC}"
    PDF_SIZE="N/A"
    PAGE_COUNT="N/A"
fi
echo ""

# 3. Aggiornamento README.md
echo -e "${YELLOW}[3/3] Aggiornamento README.md...${NC}"

if [ ! -f "$README_FILE" ]; then
    echo -e "${RED}ERRORE: File $README_FILE non trovato!${NC}"
    exit 1
fi

# Backup del README originale
cp "$README_FILE" "$README_FILE.bak"

# Aggiorna pattern: "Capitoli: XX/14" oppure "XX/14 capitoli"
sed -i '' "s/Capitoli: [0-9]\+\/${TARGET_CHAPTERS}/Capitoli: ${TOTAL_CHAPTERS}\/${TARGET_CHAPTERS}/g" "$README_FILE"
sed -i '' "s/\([0-9]\+\)\/${TARGET_CHAPTERS} capitoli/${TOTAL_CHAPTERS}\/${TARGET_CHAPTERS} capitoli/g" "$README_FILE"

# Aggiorna badge completamento percentuale se presente
sed -i '' "s/badge.*${PERCENTAGE}[^-]*-/badge-${PERCENTAGE}%-/g" "$README_FILE"

# Aggiorna PDF size se trovato
if [ "$PDF_SIZE" != "N/A" ]; then
    # Cerca pattern "main.pdf (XXX MB)" e aggiorna
    CURRENT_SIZE=$(grep -oE "main\.pdf.*\([^)]*\)" "$README_FILE" | head -1 || echo "")
    if [ ! -z "$CURRENT_SIZE" ]; then
        sed -i '' "s|$CURRENT_SIZE|main.pdf ($PDF_SIZE)|g" "$README_FILE"
    fi
fi

echo -e "${GREEN}✅ README.md aggiornato con successo${NC}"
echo ""

# 4. Report finale
echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}REPORT FINALE${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""
echo "Statistica Capitoli:"
echo "  • Capitoli compilati: ${TOTAL_CHAPTERS}/${TARGET_CHAPTERS}"
echo "  • Percentuale completamento: ${PERCENTAGE}%"
echo ""
echo "Statistica PDF:"
echo "  • Dimensione: $PDF_SIZE"
echo "  • Numero pagine: $PAGE_COUNT"
echo ""
echo "File modificati:"
echo "  • README.md (backup: README.md.bak)"
echo ""
echo -e "${GREEN}✅ Script completato con successo!${NC}"
echo ""
