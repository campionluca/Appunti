#!/usr/bin/env python3
"""
Script per generare screenshot di output terminale
"""

import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

class TerminalScreenshot:
    """Genera screenshot in stile terminale"""

    def __init__(self, width=800, height=600, bg_color="#282c34", text_color="#abb2bf"):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_size = 14
        self.padding = 20

        # Carica font monospace
        try:
            self.font = ImageFont.truetype("/System/Library/Fonts/Monaco.dfont", self.font_size)
        except:
            try:
                self.font = ImageFont.truetype("/Library/Fonts/Courier New.ttf", self.font_size)
            except:
                self.font = ImageFont.load_default()

    def execute_and_capture(self, script_path):
        """Esegue script Python e cattura output"""
        try:
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "Error: Script timeout"
        except Exception as e:
            return f"Error: {e}"

    def create_screenshot(self, output_text, output_path, title="Terminal Output"):
        """Crea immagine screenshot da testo"""
        # Prepara testo
        lines = output_text.split('\n')

        # Calcola altezza necessaria
        line_height = self.font_size + 4
        needed_height = len(lines) * line_height + self.padding * 2 + 40
        height = max(self.height, needed_height)

        # Crea immagine
        img = Image.new('RGB', (self.width, height), self.bg_color)
        draw = ImageDraw.Draw(img)

        # Header (barra titolo terminale)
        draw.rectangle([0, 0, self.width, 30], fill="#21252b")

        # Pallini rosso/giallo/verde (stile macOS)
        colors = ["#ff5f56", "#ffbd2e", "#27c93f"]
        for i, color in enumerate(colors):
            x = 15 + i * 20
            draw.ellipse([x, 10, x + 10, 20], fill=color)

        # Titolo
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Monaco.dfont", 12)
        except:
            title_font = self.font

        # Calcola larghezza testo per centrare
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = bbox[2] - bbox[0]
        title_x = (self.width - title_width) // 2

        draw.text((title_x, 8), title, fill="#8a8a8a", font=title_font)

        # Contenuto
        y = 40 + self.padding
        for line in lines:
            # Wrapping se linea troppo lunga
            if len(line) > 100:
                wrapped = textwrap.fill(line, width=100)
                for wrapped_line in wrapped.split('\n'):
                    draw.text((self.padding, y), wrapped_line, fill=self.text_color, font=self.font)
                    y += line_height
            else:
                draw.text((self.padding, y), line, fill=self.text_color, font=self.font)
                y += line_height

        # Salva
        img.save(output_path)
        print(f"✓ Screenshot salvato: {output_path}")
        return output_path


def genera_screenshot_esempi():
    """Genera screenshot per esempi chiave"""

    screenshot_gen = TerminalScreenshot()

    # Directory
    esempi_dir = Path("/Users/campion.luca/Documents/Appunti/Python/esempi_codice")
    output_dir = Path("/Users/campion.luca/Documents/Appunti/Python/immagini/screenshots")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Esempi da screenshottare
    esempi = [
        ("cap00_fondamenti/01_hello_world.py", "Hello World"),
        ("cap00_fondamenti/02_variabili_tipi.py", "Variabili e Tipi"),
        ("cap01_controllo_flusso/01_if_else.py", "If-Else"),
        ("cap01_controllo_flusso/05_list_comprehension.py", "List Comprehension"),
        ("cap02_funzioni/01_definizione_funzioni.py", "Funzioni"),
        ("cap02_funzioni/04_lambda_map_filter.py", "Lambda Map Filter"),
        ("cap03_strutture_dati/02_dizionari.py", "Dizionari"),
        ("cap03_strutture_dati/03_set.py", "Set"),
        ("cap04_stringhe_formattazione/02_formattazione.py", "F-Strings"),
        ("cap05_file_io/04_json.py", "JSON"),
        ("cap06_gestione_errori/01_try_except.py", "Try-Except"),
        ("cap08_oop/01_classi_oggetti.py", "Classi OOP"),
    ]

    print("=== GENERAZIONE SCREENSHOT TERMINALE ===\n")

    for script_rel_path, title in esempi:
        script_path = esempi_dir / script_rel_path

        if not script_path.exists():
            print(f"✗ Script non trovato: {script_path}")
            continue

        # Esegui e cattura output
        print(f"Esecuzione: {script_rel_path}")
        output = screenshot_gen.execute_and_capture(str(script_path))

        # Tronca output se troppo lungo
        lines = output.split('\n')
        if len(lines) > 40:
            output = '\n'.join(lines[:40]) + f'\n\n... (troncato, {len(lines)-40} righe omesse)'

        # Genera screenshot
        output_filename = f"terminal_{script_rel_path.replace('/', '_').replace('.py', '.png')}"
        output_path = output_dir / output_filename

        screenshot_gen.create_screenshot(output, str(output_path), title)

    print(f"\n✓ Screenshot terminale generati in: {output_dir}")


if __name__ == "__main__":
    genera_screenshot_esempi()
