#!/usr/bin/env python3
"""
Script Playwright per verificare leggibilità PDF e schemi
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import json
import time


class PlaywrightPDFVerifier:
    """Verifica PDF con Playwright"""

    def __init__(self, pdf_path, output_dir="./playwright_screenshots"):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.report = {
            "pdf": str(pdf_path),
            "pages_checked": 0,
            "issues": [],
            "screenshots": []
        }

    def verifica_pdf_browser(self):
        """Apre PDF in browser e verifica leggibilità"""
        print(f"=== VERIFICA PDF CON PLAYWRIGHT ===")
        print(f"PDF: {self.pdf_path}\n")

        with sync_playwright() as p:
            # Lancia browser
            browser = p.chromium.launch(headless=False)  # headless=True per produzione
            page = browser.new_page(viewport={"width": 1920, "height": 1080})

            # Apri PDF
            pdf_url = f"file://{self.pdf_path.absolute()}"
            print(f"Caricamento PDF: {pdf_url}")

            try:
                page.goto(pdf_url, wait_until="networkidle")
                time.sleep(2)  # Aspetta rendering

                # Screenshot prima pagina
                screenshot_path = self.output_dir / "page_1_full.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
                self.report["screenshots"].append(str(screenshot_path))
                print(f"✓ Screenshot pagina 1: {screenshot_path}")

                # Verifica presenza embed viewer PDF
                pdf_viewer = page.locator("embed, iframe, canvas")
                count = pdf_viewer.count()
                print(f"  PDF viewer elements: {count}")

                # Zoom per verificare leggibilità testo
                print("\nTest zoom...")
                for zoom_level in [100, 150, 200]:
                    print(f"  Zoom {zoom_level}%")
                    page.evaluate(f"document.body.style.zoom = '{zoom_level}%'")
                    time.sleep(0.5)

                    screenshot_path = self.output_dir / f"page_1_zoom{zoom_level}.png"
                    page.screenshot(path=str(screenshot_path))
                    self.report["screenshots"].append(str(screenshot_path))

                self.report["pages_checked"] = 1
                print(f"\n✓ Verifica completata")

            except Exception as e:
                print(f"✗ Errore: {e}")
                self.report["issues"].append(str(e))

            finally:
                browser.close()

        return self.report

    def verifica_schemi_directory(self, img_dir):
        """Verifica schemi aprendo in browser"""
        print(f"\n=== VERIFICA SCHEMI CON PLAYWRIGHT ===")
        print(f"Directory: {img_dir}\n")

        img_dir = Path(img_dir)
        images = list(img_dir.glob("*.png")) + list(img_dir.glob("*.jpg"))

        if not images:
            print("✗ Nessuna immagine trovata")
            return

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(viewport={"width": 1920, "height": 1080})

            for img_path in sorted(images)[:5]:  # Prime 5 per test
                print(f"Verifica: {img_path.name}")

                # Crea HTML per visualizzare immagine
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{img_path.name}</title>
                    <style>
                        body {{
                            margin: 0;
                            padding: 20px;
                            background: #f0f0f0;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            min-height: 100vh;
                        }}
                        img {{
                            max-width: 90%;
                            height: auto;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                        }}
                    </style>
                </head>
                <body>
                    <img src="file://{img_path.absolute()}" alt="{img_path.name}">
                </body>
                </html>
                """

                # Salva HTML temporaneo
                temp_html = self.output_dir / "temp_viewer.html"
                temp_html.write_text(html_content)

                # Apri in browser
                page.goto(f"file://{temp_html.absolute()}")
                time.sleep(1)

                # Screenshot
                screenshot_path = self.output_dir / f"verified_{img_path.stem}.png"
                page.screenshot(path=str(screenshot_path))
                self.report["screenshots"].append(str(screenshot_path))

                # Verifica dimensioni immagine con JavaScript
                dimensions = page.evaluate("""
                    () => {
                        const img = document.querySelector('img');
                        return {
                            naturalWidth: img.naturalWidth,
                            naturalHeight: img.naturalHeight,
                            displayedWidth: img.clientWidth,
                            displayedHeight: img.clientHeight
                        };
                    }
                """)

                print(f"  Dimensioni native: {dimensions['naturalWidth']}x{dimensions['naturalHeight']}")
                print(f"  Dimensioni display: {dimensions['displayedWidth']}x{dimensions['displayedHeight']}")

                # Verifica leggibilità
                if dimensions['naturalWidth'] < 400:
                    issue = f"{img_path.name}: larghezza troppo piccola ({dimensions['naturalWidth']}px)"
                    self.report["issues"].append(issue)
                    print(f"  ✗ {issue}")
                else:
                    print(f"  ✓ Dimensioni OK")

                print()

            browser.close()

        return self.report

    def genera_html_report(self, output_file="report_playwright.html"):
        """Genera report HTML con screenshot"""
        html = f"""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Report Verifica Leggibilità</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }}
        .info {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .screenshot {{
            margin: 20px 0;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .screenshot img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
        }}
        .issue {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px;
            margin: 10px 0;
        }}
        .success {{
            background: #d4edda;
            border-left: 4px solid #28a745;
            padding: 10px;
            margin: 10px 0;
        }}
    </style>
</head>
<body>
    <h1>📊 Report Verifica Leggibilità</h1>

    <div class="info">
        <h2>Informazioni</h2>
        <p><strong>PDF:</strong> {self.report['pdf']}</p>
        <p><strong>Pagine verificate:</strong> {self.report['pages_checked']}</p>
        <p><strong>Screenshot generati:</strong> {len(self.report['screenshots'])}</p>
    </div>

    <div class="info">
        <h2>Problemi Rilevati</h2>
"""

        if self.report['issues']:
            for issue in self.report['issues']:
                html += f'        <div class="issue">⚠️ {issue}</div>\n'
        else:
            html += '        <div class="success">✓ Nessun problema rilevato</div>\n'

        html += """    </div>

    <h2>Screenshot</h2>
"""

        for screenshot in self.report['screenshots']:
            screenshot_path = Path(screenshot)
            html += f"""
    <div class="screenshot">
        <h3>{screenshot_path.name}</h3>
        <img src="{screenshot_path.name}" alt="{screenshot_path.name}">
    </div>
"""

        html += """
</body>
</html>
"""

        output_path = self.output_dir / output_file
        output_path.write_text(html, encoding='utf-8')
        print(f"\n✓ Report HTML salvato: {output_path}")

        return output_path


def main():
    """Main"""
    import argparse

    parser = argparse.ArgumentParser(description="Verifica PDF/schemi con Playwright")
    parser.add_argument("--pdf", help="Path al PDF da verificare")
    parser.add_argument("--images", help="Directory con immagini da verificare")
    parser.add_argument("-o", "--output", default="./playwright_output", help="Directory output")

    args = parser.parse_args()

    # Verifica dipendenze
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("✗ Playwright non installato")
        print("  Install: pip install playwright")
        print("  Setup: playwright install chromium")
        return

    verifier = PlaywrightPDFVerifier(
        args.pdf or "/Users/campion.luca/Documents/Appunti/Python/main.pdf",
        args.output
    )

    # Verifica PDF se specificato
    if args.pdf:
        verifier.verifica_pdf_browser()

    # Verifica immagini se specificato
    if args.images:
        verifier.verifica_schemi_directory(args.images)

    # Genera report
    verifier.genera_html_report()

    # Salva JSON
    json_path = Path(args.output) / "report.json"
    with open(json_path, 'w') as f:
        json.dump(verifier.report, f, indent=2)
    print(f"✓ Report JSON salvato: {json_path}")


if __name__ == "__main__":
    main()
