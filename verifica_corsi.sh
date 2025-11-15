#!/bin/bash
# Script di verifica struttura corsi
# Data: 15 Novembre 2025

echo "================================================"
echo "VERIFICA STRUTTURA NUOVI CORSI"
echo "================================================"
echo ""

CORSI=(
    "Algoritmi"
    "Git"
    "Linux"
    "Docker"
    "React"
    "RestAPI"
    "WebSecurity"
    "Database"
    "Assembly"
)

total_capitoli=0
total_linee=0

for corso in "${CORSI[@]}"; do
    echo "----------------------------------------"
    echo "📚 $corso"
    echo "----------------------------------------"

    # Verifica main.tex
    if [ -f "$corso/main.tex" ]; then
        linee_main=$(wc -l < "$corso/main.tex")
        echo "  ✅ main.tex: $linee_main linee"
    else
        echo "  ❌ main.tex: NON TROVATO"
        continue
    fi

    # Conta capitoli
    if [ -d "$corso/capitoli" ]; then
        num_capitoli=$(find "$corso/capitoli" -name "*.tex" | wc -l)
        echo "  ✅ Capitoli: $num_capitoli file .tex"
        total_capitoli=$((total_capitoli + num_capitoli))
    else
        echo "  ❌ Directory capitoli: NON TROVATA"
        continue
    fi

    # Conta linee totali capitoli
    linee_capitoli=$(find "$corso/capitoli" -name "*.tex" -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}')
    if [ -n "$linee_capitoli" ]; then
        echo "  📝 Linee totali: $linee_capitoli"
        total_linee=$((total_linee + linee_capitoli))
    fi

    # Verifica PDF esistente
    if [ -f "$corso/main.pdf" ]; then
        pdf_size=$(du -h "$corso/main.pdf" | cut -f1)
        echo "  ✅ PDF: Esistente ($pdf_size)"
    else
        echo "  ⏳ PDF: Da compilare"
    fi

    echo ""
done

echo "================================================"
echo "RIEPILOGO TOTALE"
echo "================================================"
echo "  Corsi verificati: ${#CORSI[@]}"
echo "  Capitoli totali: $total_capitoli"
echo "  Linee di codice LaTeX: ~$total_linee"
echo ""

# Verifica documentazione principale
echo "================================================"
echo "DOCUMENTAZIONE PRINCIPALE"
echo "================================================"

if [ -f "README.md" ]; then
    readme_lines=$(wc -l < README.md)
    echo "  ✅ README.md: $readme_lines linee"
else
    echo "  ❌ README.md: NON TROVATO"
fi

if [ -f "MASTER-TODO.md" ]; then
    todo_lines=$(wc -l < MASTER-TODO.md)
    echo "  ✅ MASTER-TODO.md: $todo_lines linee"
else
    echo "  ❌ MASTER-TODO.md: NON TROVATO"
fi

if [ -f "INTEGRATION_REPORT_2025-11-15.md" ]; then
    report_lines=$(wc -l < INTEGRATION_REPORT_2025-11-15.md)
    echo "  ✅ INTEGRATION_REPORT: $report_lines linee"
else
    echo "  ⏳ INTEGRATION_REPORT: Non ancora creato"
fi

if [ -f "COMPILAZIONE_PDF_GUIDA.md" ]; then
    guida_lines=$(wc -l < COMPILAZIONE_PDF_GUIDA.md)
    echo "  ✅ COMPILAZIONE_PDF_GUIDA: $guida_lines linee"
else
    echo "  ⏳ COMPILAZIONE_PDF_GUIDA: Non ancora creato"
fi

echo ""
echo "================================================"
echo "STATO GENERALE"
echo "================================================"

# Conta corsi con PDF
corsi_con_pdf=0
corsi_senza_pdf=0

for corso in "${CORSI[@]}"; do
    if [ -f "$corso/main.pdf" ]; then
        corsi_con_pdf=$((corsi_con_pdf + 1))
    else
        corsi_senza_pdf=$((corsi_senza_pdf + 1))
    fi
done

echo "  Corsi con PDF: $corsi_con_pdf / ${#CORSI[@]}"
echo "  Corsi senza PDF: $corsi_senza_pdf / ${#CORSI[@]}"

if [ $corsi_senza_pdf -eq 0 ]; then
    echo "  Status: ✅ TUTTI I PDF COMPILATI"
else
    echo "  Status: ⏳ $corsi_senza_pdf PDF da compilare"
fi

echo ""
echo "================================================"
echo "VERIFICA COMPLETATA"
echo "================================================"
