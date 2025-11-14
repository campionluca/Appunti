#!/bin/bash
# Script per aggiornare automaticamente il conteggio dei moduli nel README.md
# Uso: ./update_module_count.sh

# Determina la directory dello script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Conta i file .tex nella cartella capitoli (escludendo quelli che iniziano con _)
MODULE_COUNT=$(ls -1 capitoli/*.tex 2>/dev/null | grep -v '/[_]' | wc -l | tr -d ' ')

if [ -z "$MODULE_COUNT" ] || [ "$MODULE_COUNT" -eq 0 ]; then
    echo "ERRORE: Nessun file .tex trovato nella cartella capitoli/"
    exit 1
fi

# Aggiorna il README.md sostituendo il valore tra i tag <!--MODULE_COUNT-->
if [ -f "README.md" ]; then
    # Usa sed compatibile con macOS
    sed -i '' "s/<!--MODULE_COUNT-->[0-9]*<!--\/MODULE_COUNT-->/<!--MODULE_COUNT-->${MODULE_COUNT}<!--\/MODULE_COUNT-->/" README.md
    echo "✓ README.md aggiornato: ${MODULE_COUNT} moduli"
else
    echo "ERRORE: README.md non trovato"
    exit 1
fi

# Mostra il risultato
echo ""
echo "Moduli conteggiati:"
ls -1 capitoli/*.tex | grep -v '/[_]' | sed 's/capitoli\//  - /'
echo ""
echo "Totale: ${MODULE_COUNT} moduli"
