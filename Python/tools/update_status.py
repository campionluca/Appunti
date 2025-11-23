import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN_TEX = ROOT / "main.tex"
README = ROOT / "README.md"


def countIncludedModules() -> int:
    text = MAIN_TEX.read_text(encoding="utf-8")
    includes = re.findall(r"\\include\{capitoli/([\w_\-]+)\}", text)
    includes = [inc for inc in includes if inc != "appendice_soluzioni"]
    return len(includes)


def updateReadme(count: int) -> None:
    md = README.read_text(encoding="utf-8")
    marker_re = r"(<!--MODULE_COUNT-->)(\d+)(<!--/MODULE_COUNT-->)"
    if re.search(marker_re, md):
        md = re.sub(marker_re, lambda m: f"{m.group(1)}{count}{m.group(3)}", md)
    else:
        # Inserisci una riga sotto la tabella Stato se il marker non esiste
        inject = f"\n\nModuli inclusi nel PDF: <!--MODULE_COUNT-->{count}<!--/MODULE_COUNT-->\n"
        md += inject
    README.write_text(md, encoding="utf-8")


def main():
    cnt = countIncludedModules()
    updateReadme(cnt)
    print(f"[status] Moduli inclusi aggiornati a: {cnt}")


if __name__ == "__main__":
    main()
