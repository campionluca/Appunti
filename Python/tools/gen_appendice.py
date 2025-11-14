import sys
from pathlib import Path


def find_solution_files(root: Path):
    candidates = []
    # Prefer dedicated directory if exists
    sol_dir = root / "appendice_soluzioni"
    if sol_dir.exists():
        candidates.extend(sorted(sol_dir.glob("*.tex")))
    # Fallback: cerca file *soluzioni.tex nei moduli
    for tex in sorted((root / "moduli").glob("*_soluzioni.tex")):
        candidates.append(tex)
    return candidates


def generate_appendix(root: Path, files):
    out_dir = root / "appendice_soluzioni"
    out_dir.mkdir(exist_ok=True)
    out_tex = out_dir / "generated_appendice.tex"
    lines = [
        "% File generato automaticamente: non modificare a mano",
        "\\chapter{Appendice: Soluzioni e Approfondimenti}",
        "",
    ]
    if not files:
        lines.append("% Nessun file di soluzioni trovato.")
    else:
        for f in files:
            rel = f.relative_to(root).as_posix()
            lines.append(f"% include: {rel}")
            lines.append(f"\\input{{{rel}}}")
            lines.append("")
    out_tex.write_text("\n".join(lines), encoding="utf-8")
    return out_tex


def main():
    root = Path(__file__).resolve().parents[1]
    files = find_solution_files(root)
    out = generate_appendix(root, files)
    print(f"[appendice] Generato: {out} (files: {len(files)})")
    print("Aggiungi a main.tex: \n  \\input{appendice_soluzioni/generated_appendice.tex}")
    return 0


if __name__ == "__main__":
    sys.exit(main())