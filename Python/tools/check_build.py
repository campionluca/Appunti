import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN_TEX = ROOT / "main.tex"
MAIN_LOG = ROOT / "main.log"


ERROR_PATTERNS = [
    "LaTeX Error:",
    "Emergency stop",
    "Undefined control sequence",
    "Missing \\end",
    "Fatal error occurred",
]

WARNING_PATTERNS = [
    "Overfull \\hbox",
    "Underfull \\hbox",
]


def run_build() -> int:
    latexmk = shutil.which("latexmk")
    if latexmk:
        cmd = [latexmk, "-pdf", "-interaction=nonstopmode", str(MAIN_TEX)]
        print(f"[build] Running: {' '.join(cmd)}")
        return subprocess.run(cmd).returncode
    pdflatex = shutil.which("pdflatex")
    if not pdflatex:
        print("[error] pdflatex non trovato. Installa TeX Live o MiKTeX.")
        return 127
    rc1 = subprocess.run([pdflatex, "-interaction=nonstopmode", str(MAIN_TEX)]).returncode
    rc2 = subprocess.run([pdflatex, "-interaction=nonstopmode", str(MAIN_TEX)]).returncode
    return rc1 or rc2


def scan_log(log_path: Path):
    if not log_path.exists():
        print(f"[warn] Log non trovato: {log_path}")
        return [], []
    content = log_path.read_text(encoding="utf-8", errors="ignore")
    errors = [line for line in content.splitlines() if any(p in line for p in ERROR_PATTERNS)]
    warnings = [line for line in content.splitlines() if any(p in line for p in WARNING_PATTERNS)]
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Analisi compilazione LaTeX: riassunto errori/avvisi")
    parser.add_argument("--skip-build", action="store_true", help="Non eseguire la compilazione, analizza solo il log")
    parser.add_argument("--strict", action="store_true", help="Esci non-zero se presenti avvisi")
    args = parser.parse_args()

    if not MAIN_TEX.exists():
        print(f"[error] File non trovato: {MAIN_TEX}")
        return 1

    code = 0
    if not args.skip_build:
        code = run_build()
    errors, warnings = scan_log(MAIN_LOG)
    print("\n[summary] Compilazione LaTeX")
    print(f"  Exit code: {code}")
    print(f"  Errori: {len(errors)}")
    print(f"  Avvisi: {len(warnings)}")
    if errors:
        print("\n[errors]")
        for e in errors[:20]:
            print("  ", e)
    if warnings:
        print("\n[warnings]")
        for w in warnings[:20]:
            print("  ", w)
    # Policy di uscita:
    # - fallisci se ci sono errori LaTeX
    # - se --strict, fallisci anche con avvisi
    if errors:
        return 2
    if args.strict and warnings:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())