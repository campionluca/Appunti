#!/usr/bin/env python3
"""
Genera screenshot dimostrativi per il libro
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


class TerminalScreenshot:
    """Genera screenshot in stile terminale"""

    def __init__(self):
        self.width = 800
        self.height = 600
        self.bg_color = "#282c34"
        self.text_color = "#abb2bf"
        self.font_size = 14
        self.padding = 20

        try:
            self.font = ImageFont.truetype("/System/Library/Fonts/Monaco.dfont", self.font_size)
            self.title_font = ImageFont.truetype("/System/Library/Fonts/Monaco.dfont", 12)
        except:
            self.font = ImageFont.load_default()
            self.title_font = self.font

    def create(self, output_text, title, output_path):
        """Crea screenshot"""
        lines = output_text.split('\n')
        line_height = self.font_size + 4
        needed_height = len(lines) * line_height + self.padding * 2 + 40
        height = max(self.height, needed_height)

        # Immagine
        img = Image.new('RGB', (self.width, height), self.bg_color)
        draw = ImageDraw.Draw(img)

        # Header terminale
        draw.rectangle([0, 0, self.width, 30], fill="#21252b")

        # Pallini macOS
        colors = ["#ff5f56", "#ffbd2e", "#27c93f"]
        for i, color in enumerate(colors):
            x = 15 + i * 20
            draw.ellipse([x, 10, x + 10, 20], fill=color)

        # Titolo
        bbox = draw.textbbox((0, 0), title, font=self.title_font)
        title_width = bbox[2] - bbox[0]
        title_x = (self.width - title_width) // 2
        draw.text((title_x, 8), title, fill="#8a8a8a", font=self.title_font)

        # Contenuto
        y = 40 + self.padding
        for line in lines:
            draw.text((self.padding, y), line, fill=self.text_color, font=self.font)
            y += line_height

        img.save(output_path)
        print(f"✓ {output_path.name}")
        return output_path


def main():
    """Genera screenshot dimostrativi"""
    output_dir = Path("immagini/screenshots")
    output_dir.mkdir(parents=True, exist_ok=True)

    gen = TerminalScreenshot()

    print("=== GENERAZIONE SCREENSHOT DIMOSTRATIVI ===\n")

    # Hello World
    gen.create(
        "=== HELLO WORLD ===\nHello, World!\n\n=== PRINT CON SEPARATORI ===\nPython - è - fantastico!",
        "Hello World",
        output_dir / "terminal_01_hello_world.png"
    )

    # Variabili
    gen.create(
        "=== VARIABILI E TIPI ===\nVariabile int: 42 (type: <class 'int'>)\nVariabile float: 3.14 (type: <class 'float'>)\nVariabile str: Python (type: <class 'str'>)\nVariabile bool: True (type: <class 'bool'>)",
        "Variabili e Tipi",
        output_dir / "terminal_02_variabili.png"
    )

    # If-Else
    gen.create(
        "=== IF-ELSE ===\nvoto = 85\nVoto: Ottimo (B)\n\n=== OPERATORE TERNARIO ===\nrisultato = promosso\nRisultato: promosso",
        "Controllo Flusso If-Else",
        output_dir / "terminal_03_if_else.png"
    )

    # List Comprehension
    gen.create(
        "=== LIST COMPREHENSION ===\nQuadrati: [1, 4, 9, 16, 25]\nPari: [0, 2, 4, 6, 8]\n\n=== NESTED COMPREHENSION ===\nMatrice piatta: [1, 2, 3, 4, 5, 6, 7, 8, 9]",
        "List Comprehension",
        output_dir / "terminal_04_comprehension.png"
    )

    # Dizionari
    gen.create(
        "=== DIZIONARI ===\nPersona: {'nome': 'Alice', 'eta': 25, 'citta': 'Roma'}\n\n=== ACCESSO ===\nNome: Alice\nEtà: 25\n\n=== ITERAZIONE ===\nnome: Alice\neta: 25\ncitta: Roma",
        "Dizionari",
        output_dir / "terminal_05_dizionari.png"
    )

    # F-Strings
    gen.create(
        "=== F-STRINGS ===\nNome: Alice, Età: 25\n\n=== FORMATTAZIONE NUMERI ===\nPi (2 decimali): 3.14\nPrezzo: €1,234.56\n\n=== PADDING ===\n|        Python        |",
        "Formattazione F-Strings",
        output_dir / "terminal_06_fstrings.png"
    )

    # JSON
    gen.create(
        "=== SCRITTURA JSON ===\nJSON scritto\n\n=== LETTURA JSON ===\nLoaded: {'nome': 'Alice', 'eta': 25}\nTipo: <class 'dict'>\n\n=== PRETTY PRINT ===\n{\n  \"nome\": \"Alice\",\n  \"eta\": 25\n}",
        "JSON",
        output_dir / "terminal_07_json.png"
    )

    # Try-Except
    gen.create(
        "=== TRY/EXCEPT ===\nErrore: divisione per zero!\nIl programma continua...\n\n=== CATTURARE ECCEZIONE ===\nErrore catturato: division by zero\nTipo: <class 'ZeroDivisionError'>",
        "Gestione Errori",
        output_dir / "terminal_08_try_except.png"
    )

    # Classi OOP
    gen.create(
        "=== CLASSE BASE ===\nCiao, sono Alice\nEtà: 25\n\n=== METODI SPECIALI ===\nstr: Punto(1, 2)\np1 == p2: True\n\n=== PROPERTY ===\nArea: 50",
        "Classi e OOP",
        output_dir / "terminal_09_oop.png"
    )

    print(f"\n✓ Screenshot generati in: {output_dir}")


if __name__ == "__main__":
    main()
