#!/usr/bin/env python3
"""
Script per verificare leggibilità schemi usando Playwright e OCR
"""

from pathlib import Path
import json
from PIL import Image
import pytesseract


class VerificatoreLeggibilita:
    """Verifica leggibilità di schemi e diagrammi"""

    def __init__(self, output_file="report_leggibilita.json"):
        self.output_file = output_file
        self.report = {
            "schemi_verificati": 0,
            "schemi_leggibili": 0,
            "schemi_illeggibili": [],
            "dettagli": []
        }

    def analizza_immagine(self, image_path):
        """Analizza leggibilità immagine"""
        try:
            img = Image.open(image_path)

            # Statistiche base
            width, height = img.size
            aspect_ratio = width / height

            # Contrasto e luminosità
            if img.mode == 'RGB':
                stat = img.convert('L').getextrema()
                contrast = stat[1] - stat[0]
            else:
                stat = img.getextrema()
                contrast = stat[1] - stat[0]

            # Tenta OCR per verificare presenza testo
            try:
                text = pytesseract.image_to_string(img)
                text_detected = len(text.strip()) > 10
                word_count = len(text.split())
            except:
                text_detected = False
                word_count = 0

            # Criteri leggibilità
            is_readable = (
                width >= 400 and  # Larghezza minima
                height >= 300 and  # Altezza minima
                contrast >= 100 and  # Contrasto sufficiente
                0.5 <= aspect_ratio <= 3.0  # Ratio ragionevole
            )

            return {
                "path": str(image_path),
                "width": width,
                "height": height,
                "aspect_ratio": round(aspect_ratio, 2),
                "contrast": contrast,
                "text_detected": text_detected,
                "word_count": word_count,
                "is_readable": is_readable,
                "issues": self._identifica_problemi(width, height, contrast, aspect_ratio)
            }

        except Exception as e:
            return {
                "path": str(image_path),
                "error": str(e),
                "is_readable": False
            }

    def _identifica_problemi(self, width, height, contrast, aspect_ratio):
        """Identifica problemi specifici"""
        issues = []

        if width < 400:
            issues.append(f"Larghezza troppo piccola ({width}px < 400px)")
        if height < 300:
            issues.append(f"Altezza troppo piccola ({height}px < 300px)")
        if contrast < 100:
            issues.append(f"Contrasto basso ({contrast} < 100)")
        if aspect_ratio < 0.5 or aspect_ratio > 3.0:
            issues.append(f"Aspect ratio non ottimale ({aspect_ratio})")
        if width > 2000:
            issues.append(f"Larghezza eccessiva ({width}px > 2000px) - potrebbe essere ridotta")

        return issues

    def verifica_directory(self, directory):
        """Verifica tutti gli schemi in una directory"""
        directory = Path(directory)

        print(f"=== VERIFICA LEGGIBILITÀ SCHEMI ===")
        print(f"Directory: {directory}\n")

        # Trova tutte le immagini
        image_extensions = ['.png', '.jpg', '.jpeg', '.pdf']
        images = []
        for ext in image_extensions:
            images.extend(directory.rglob(f"*{ext}"))

        if not images:
            print("✗ Nessuna immagine trovata")
            return

        print(f"Trovate {len(images)} immagini\n")

        # Analizza ogni immagine
        for img_path in sorted(images):
            if img_path.suffix == '.pdf':
                # PDF richiede trattamento speciale
                result = self._analizza_pdf(img_path)
            else:
                result = self.analizza_immagine(img_path)

            self.report["schemi_verificati"] += 1
            self.report["dettagli"].append(result)

            # Stampa risultato
            status = "✓" if result.get("is_readable", False) else "✗"
            print(f"{status} {img_path.name}")

            if result.get("is_readable", False):
                self.report["schemi_leggibili"] += 1
                if result.get("word_count", 0) > 0:
                    print(f"  → Testo rilevato: {result['word_count']} parole")
            else:
                self.report["schemi_illeggibili"].append(str(img_path))

            # Mostra problemi
            if result.get("issues"):
                for issue in result["issues"]:
                    print(f"  ! {issue}")

            # Mostra statistiche
            if "width" in result:
                print(f"  Dimensioni: {result['width']}x{result['height']} px")
                print(f"  Contrasto: {result['contrast']}")

            print()

    def _analizza_pdf(self, pdf_path):
        """Analizza PDF (converte prima pagina in immagine)"""
        try:
            from pdf2image import convert_from_path

            # Converti prima pagina
            images = convert_from_path(str(pdf_path), first_page=1, last_page=1)
            if images:
                # Salva temporaneamente
                temp_path = Path("/tmp/temp_pdf_page.png")
                images[0].save(temp_path)

                # Analizza
                result = self.analizza_immagine(temp_path)
                result["path"] = str(pdf_path)
                result["type"] = "pdf"

                temp_path.unlink()  # Rimuovi temp
                return result
            else:
                return {"path": str(pdf_path), "error": "Nessuna pagina", "is_readable": False}

        except ImportError:
            return {
                "path": str(pdf_path),
                "error": "pdf2image non installato (pip install pdf2image)",
                "is_readable": False
            }
        except Exception as e:
            return {"path": str(pdf_path), "error": str(e), "is_readable": False}

    def genera_report(self):
        """Genera report finale"""
        print("\n" + "=" * 60)
        print("REPORT FINALE")
        print("=" * 60)

        total = self.report["schemi_verificati"]
        leggibili = self.report["schemi_leggibili"]
        illeggibili = total - leggibili

        print(f"\nSchemi verificati: {total}")
        print(f"  ✓ Leggibili: {leggibili} ({leggibili/total*100:.1f}%)")
        print(f"  ✗ Problematici: {illeggibili} ({illeggibili/total*100:.1f}%)")

        if self.report["schemi_illeggibili"]:
            print(f"\nSchemi con problemi:")
            for schema in self.report["schemi_illeggibili"]:
                print(f"  - {Path(schema).name}")

        # Salva JSON
        output_path = Path(self.output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2, ensure_ascii=False)

        print(f"\nReport dettagliato salvato in: {output_path}")

        # Raccomandazioni
        print("\n" + "=" * 60)
        print("RACCOMANDAZIONI")
        print("=" * 60)

        problemi_comuni = {}
        for dettaglio in self.report["dettagli"]:
            for issue in dettaglio.get("issues", []):
                problemi_comuni[issue] = problemi_comuni.get(issue, 0) + 1

        if problemi_comuni:
            print("\nProblemi più frequenti:")
            for problema, count in sorted(problemi_comuni.items(), key=lambda x: x[1], reverse=True):
                print(f"  [{count}x] {problema}")
        else:
            print("\n✓ Nessun problema rilevato!")

        return self.report


def main():
    """Main"""
    import argparse

    parser = argparse.ArgumentParser(description="Verifica leggibilità schemi")
    parser.add_argument(
        "directory",
        nargs="?",
        default="/Users/campion.luca/Documents/Appunti/Python/immagini",
        help="Directory contenente immagini"
    )
    parser.add_argument(
        "-o", "--output",
        default="report_leggibilita.json",
        help="File output report"
    )

    args = parser.parse_args()

    # Verifica dipendenze
    try:
        import pytesseract
    except ImportError:
        print("⚠ pytesseract non installato. Install: pip install pytesseract")
        print("  Su macOS: brew install tesseract")
        return

    # Esegui verifica
    verificatore = VerificatoreLeggibilita(args.output)
    verificatore.verifica_directory(args.directory)
    verificatore.genera_report()


if __name__ == "__main__":
    main()
