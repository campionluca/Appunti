# Makefile per compilazione Appunti Programmazione Java (Quarta)
# Utilizza XeLaTeX per supporto UTF-8 e caratteri accentati italiani

# Variabili configurabili
LATEX = xelatex
SOURCE = main.tex
OUTPUT = main.pdf

# Opzioni compilatore
# -interaction=nonstopmode: non fermarsi per domande interattive
# Rimosso -halt-on-error per permettere compilazione anche con warning TikZ
LATEX_FLAGS = -interaction=nonstopmode

# File temporanei da rimuovere
TEMP_FILES = *.aux *.out *.toc *.lof *.lot *.log *.lol *.synctex*

# Definizione target PHONY (non corrispondono a file reali)
.PHONY: all pdf clean distclean preview check-warnings warnings-only update-stats pre-commit

# Target di default: compila il PDF
all: pdf

# Target principale: compila il documento PDF con XeLaTeX
pdf:
	@echo "=================================================="
	@echo "Compilazione documento: $(SOURCE)"
	@echo "Compilatore: $(LATEX)"
	@echo "=================================================="
	@echo ""
	@echo "[1/3] Prima compilazione..."
	-$(LATEX) $(LATEX_FLAGS) $(SOURCE)
	@echo ""
	@echo "[2/3] Seconda compilazione (aggiornamento riferimenti)..."
	-$(LATEX) $(LATEX_FLAGS) $(SOURCE)
	@echo ""
	@echo "[3/3] Terza compilazione (finalizzazione TOC e indici)..."
	-$(LATEX) $(LATEX_FLAGS) $(SOURCE)
	@echo ""
	@echo "=================================================="
	@echo "Controllo warning e errori..."
	@echo "=================================================="
	@$(MAKE) check-warnings
	@echo ""
	@echo "=================================================="
	@echo "Pulizia file temporanei..."
	@rm -f $(TEMP_FILES)
	@echo "File temporanei rimossi."
	@echo "=================================================="
	@echo ""
	@if [ -f $(OUTPUT) ]; then \
		SIZE=$$(du -h $(OUTPUT) | cut -f1); \
		echo "Compilazione completata con successo!"; \
		echo "PDF generato: $(OUTPUT) ($$SIZE)"; \
	else \
		echo "ERRORE: Compilazione fallita - $(OUTPUT) non generato."; \
		exit 1; \
	fi
	@echo ""

# Target check-warnings: analizza il log e blocca su errori critici
check-warnings:
	@echo "Analisi log di compilazione: main.log"
	@echo ""
	@if [ ! -f main.log ]; then \
		echo "ERRORE: main.log non trovato."; \
		echo "Esegui prima la compilazione con 'make pdf'."; \
		exit 1; \
	fi
	@ERRORS=$$(grep -c "^! " main.log 2>/dev/null || echo 0); \
	WARNINGS=$$(grep -c "Warning" main.log 2>/dev/null || echo 0); \
	TIKZ_WARN=$$(grep -c "Package tikz Warning" main.log 2>/dev/null || echo 0); \
	echo "--- REPORT ANALISI LOG ---"; \
	echo "Errori critici (!)    : $$ERRORS"; \
	echo "Warning LaTeX         : $$WARNINGS"; \
	echo "TikZ Warning          : $$TIKZ_WARN"; \
	echo "--------------------------"; \
	echo ""; \
	if [ $$ERRORS -gt 0 ]; then \
		echo "❌ $$ERRORS ERRORI TROVATI - BUILD BLOCCATA"; \
		echo ""; \
		echo "Dettaglio errori critici:"; \
		grep "^! " main.log | head -10; \
		exit 1; \
	elif [ $$WARNINGS -gt 0 ] || [ $$TIKZ_WARN -gt 0 ]; then \
		echo "⚠️  WARNING RILEVATI ($$WARNINGS LaTeX, $$TIKZ_WARN TikZ)"; \
		if [ $$TIKZ_WARN -gt 0 ]; then \
			echo ""; \
			echo "Dettaglio TikZ Warning:"; \
			grep "Package tikz Warning" main.log | head -5; \
		fi; \
		echo ""; \
		echo "Build continua - controlla i warning se necessario."; \
	else \
		echo "✅ BUILD OK - 0 errori"; \
	fi
	@echo ""

# Target warnings-only: mostra tutti i warning senza bloccare
warnings-only:
	@echo "=================================================="
	@echo "Analisi warning - Solo lettura (non blocca)"
	@echo "=================================================="
	@echo ""
	@if [ ! -f main.log ]; then \
		echo "ERRORE: main.log non trovato."; \
		echo "Esegui prima la compilazione."; \
		exit 1; \
	fi
	@ERRORS=$$(grep -c "^! " main.log 2>/dev/null || echo 0); \
	WARNINGS=$$(grep -c "Warning" main.log 2>/dev/null || echo 0); \
	TIKZ_WARN=$$(grep -c "Package tikz Warning" main.log 2>/dev/null || echo 0); \
	echo "--- STATISTICHE ---"; \
	echo "Errori critici (!)    : $$ERRORS"; \
	echo "Warning LaTeX         : $$WARNINGS"; \
	echo "TikZ Warning          : $$TIKZ_WARN"; \
	echo "-------------------"; \
	echo ""; \
	if [ $$ERRORS -gt 0 ]; then \
		echo "ERRORI CRITICI RILEVATI:"; \
		grep "^! " main.log; \
		echo ""; \
	fi; \
	if [ $$WARNINGS -gt 0 ]; then \
		echo "WARNING LATEX RILEVATI:"; \
		grep "Warning" main.log | grep -v "Package tikz Warning"; \
		echo ""; \
	fi; \
	if [ $$TIKZ_WARN -gt 0 ]; then \
		echo "TIKZ WARNING RILEVATI:"; \
		grep "Package tikz Warning" main.log; \
		echo ""; \
	fi; \
	if [ $$ERRORS -eq 0 ] && [ $$WARNINGS -eq 0 ] && [ $$TIKZ_WARN -eq 0 ]; then \
		echo "✅ Nessun warning o errore rilevato."; \
	fi
	@echo ""

# Target clean: rimuove solo i file temporanei (mantiene il PDF)
clean:
	@echo "Rimozione file temporanei..."
	@rm -f $(TEMP_FILES)
	@echo "File temporanei rimossi. PDF preservato."

# Target distclean: rimuove file temporanei E il PDF finale
distclean: clean
	@echo "Rimozione PDF finale..."
	@rm -f $(OUTPUT)
	@echo "Pulizia completa effettuata."

# Target preview: apre il PDF con l'applicazione predefinita (macOS)
preview:
	@if [ -f $(OUTPUT) ]; then \
		echo "Apertura $(OUTPUT)..."; \
		open $(OUTPUT); \
	else \
		echo "ERRORE: $(OUTPUT) non trovato."; \
		echo "Esegui 'make pdf' prima di usare preview."; \
		exit 1; \
	fi

# Target update-stats: aggiorna le statistiche del progetto nel README
update-stats:
	@echo "=================================================="
	@echo "Aggiornamento statistiche progetto..."
	@echo "=================================================="
	@if [ -f update-chapter-count.sh ]; then \
		bash update-chapter-count.sh; \
	else \
		echo "ERRORE: Script update-chapter-count.sh non trovato."; \
		exit 1; \
	fi

# Target pre-commit: prepara il repo per il commit (clean, update-stats, pdf)
pre-commit: clean
	@echo "=================================================="
	@echo "Preparazione pre-commit..."
	@echo "=================================================="
	@echo ""
	@echo "[1/3] Aggiornamento statistiche..."
	@$(MAKE) update-stats
	@echo ""
	@echo "[2/3] Compilazione PDF..."
	@$(MAKE) pdf
	@echo ""
	@echo "=================================================="
	@echo "Pre-commit completato!"
	@echo "Repository pronto per il commit."
	@echo "=================================================="
