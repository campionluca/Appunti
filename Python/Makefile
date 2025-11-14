PDF := main.pdf
TEX := main.tex

LATEXMK := $(shell command -v latexmk 2>/dev/null)

ifeq ($(LATEXMK),)
  PDF_CMD := pdflatex $(TEX) && pdflatex $(TEX)
CLEAN_CMD := rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk capitoli/*.aux
else
  PDF_CMD := latexmk -pdf $(TEX)
  CLEAN_CMD := latexmk -C
endif

.PHONY: pdf clean status check appendice

pdf:
	$(PDF_CMD)

clean:
	$(CLEAN_CMD)

status:
	python3 tools/update_status.py || python tools/update_status.py

check:
	python3 tools/check_build.py || python tools/check_build.py

appendice:
	python3 tools/gen_appendice.py || python tools/gen_appendice.py
