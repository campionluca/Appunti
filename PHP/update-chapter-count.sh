#!/bin/bash

# Script di automazione per aggiornare conteggio capitoli nel README.md (PHP)
# Progetto: Appunti Programmazione PHP

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHAPTER_DIR="$SCRIPT_DIR/capitoli"
README_FILE="$SCRIPT_DIR/README.md"
LOG_FILE="$SCRIPT_DIR/main.log"

echo "== Aggiornamento Statistiche Capitoli (PHP) =="

if [ ! -d "$CHAPTER_DIR" ]; then
    echo "ERRORE: Directory $CHAPTER_DIR non trovata!"
    exit 1
fi

TOTAL_CHAPTERS=$(ls -1 "$CHAPTER_DIR"/*.tex 2>/dev/null | wc -l)
TARGET_CHAPTERS=14
PERCENTAGE=$((TOTAL_CHAPTERS * 100 / TARGET_CHAPTERS))

echo "Capitoli: $TOTAL_CHAPTERS/$TARGET_CHAPTERS ($PERCENTAGE%)"

PDF_FILE="$SCRIPT_DIR/main.pdf"
if [ -f "$PDF_FILE" ]; then
    PDF_SIZE=$(du -h "$PDF_FILE" | cut -f1)
    echo "PDF: $PDF_SIZE"
fi

if [ -f "$README_FILE" ]; then
    cp "$README_FILE" "$README_FILE.bak"
    echo "Backup README.md creato"
fi

echo "Completato"

