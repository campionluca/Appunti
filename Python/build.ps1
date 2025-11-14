Param(
  [ValidateSet('pdf','clean','status','check','appendice')]
  [string]$Action = 'pdf'
)

function Build-Pdf {
  Write-Host "[build] Compilazione PDF..." -ForegroundColor Cyan
  $latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
  if ($latexmk) {
    latexmk -pdf main.tex
  } else {
    Write-Host "[build] latexmk non trovato, fallback a pdflatex" -ForegroundColor Yellow
    pdflatex main.tex
    pdflatex main.tex
  }
}

function Clean-Build {
  Write-Host "[clean] Pulizia artefatti LaTeX..." -ForegroundColor Cyan
  $latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
  if ($latexmk) {
    latexmk -C
  } else {
    Get-ChildItem -Path . -Include *.aux,*.log,*.out,*.toc,*.fls,*.fdb_latexmk -File | Remove-Item -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path moduli -Include *.aux -File | Remove-Item -Force -ErrorAction SilentlyContinue
  }
}

try {
  switch ($Action) {
    'pdf' { Build-Pdf }
    'clean' { Clean-Build }
    'status' { python tools/update_status.py }
    'check' { python tools/check_build.py }
    'appendice' { python tools/gen_appendice.py }
  }
  Write-Host "[done] Azione completata: $Action" -ForegroundColor Green
  exit 0
} catch {
  Write-Host "[error] $($_.Exception.Message)" -ForegroundColor Red
  exit 1
}