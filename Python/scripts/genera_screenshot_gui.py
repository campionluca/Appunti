#!/usr/bin/env python3
"""
Script per generare screenshot di GUI Tkinter
"""

import tkinter as tk
from pathlib import Path
import time
from PIL import ImageGrab
import platform


class GUIScreenshotGenerator:
    """Genera screenshot di applicazioni Tkinter"""

    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def capture_window(self, root, filename, delay=0.5):
        """Cattura screenshot di finestra Tkinter"""
        # Aspetta rendering
        root.update()
        time.sleep(delay)

        # Ottieni coordinate finestra
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        w = root.winfo_width()
        h = root.winfo_height()

        # Cattura screenshot
        if platform.system() == "Darwin":  # macOS
            # Su macOS potrebbe richiedere permessi
            try:
                screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h))
                output_path = self.output_dir / filename
                screenshot.save(output_path)
                print(f"✓ Screenshot GUI salvato: {output_path}")
                return output_path
            except Exception as e:
                print(f"✗ Errore screenshot (serve permesso schermo): {e}")
                return None
        else:
            screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h))
            output_path = self.output_dir / filename
            screenshot.save(output_path)
            print(f"✓ Screenshot GUI salvato: {output_path}")
            return output_path

    def esempio_gui_base(self):
        """Crea e screenshotta GUI base"""
        root = tk.Tk()
        root.title("Esempio Tkinter Base")
        root.geometry("400x300")

        # Widgets
        tk.Label(root, text="Benvenuto in Tkinter!", font=("Arial", 16)).pack(pady=20)

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5)
        tk.Entry(frame).grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(frame).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(root, text="Invia", bg="#4CAF50", fg="white", padx=20, pady=10).pack(pady=10)
        tk.Button(root, text="Annulla", bg="#f44336", fg="white", padx=20, pady=10).pack()

        # Screenshot
        root.after(500, lambda: self.capture_window(root, "gui_base.png"))
        root.after(1500, root.quit)

        root.mainloop()

    def esempio_calcolatrice(self):
        """Crea e screenshotta calcolatrice"""
        root = tk.Tk()
        root.title("Calcolatrice")
        root.resizable(False, False)

        # Display
        display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        display.insert(0, "123 + 456")

        # Bottoni
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            bg_color = "#4CAF50" if button == "=" else "#f0f0f0"
            fg_color = "white" if button == "=" else "black"

            tk.Button(
                root, text=button, width=5, height=2,
                font=("Arial", 14), bg=bg_color, fg=fg_color
            ).grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Screenshot
        root.after(500, lambda: self.capture_window(root, "gui_calcolatrice.png"))
        root.after(1500, root.quit)

        root.mainloop()

    def esempio_form_completo(self):
        """Form completo con vari widget"""
        root = tk.Tk()
        root.title("Form Registrazione")
        root.geometry("450x400")

        # Titolo
        tk.Label(root, text="Registrazione Utente", font=("Arial", 18, "bold")).pack(pady=10)

        # Frame principale
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        # Nome
        tk.Label(frame, text="Nome Completo:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=30).grid(row=0, column=1, pady=5)

        # Email
        tk.Label(frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=30).grid(row=1, column=1, pady=5)

        # Età
        tk.Label(frame, text="Età:").grid(row=2, column=0, sticky="w", pady=5)
        tk.Spinbox(frame, from_=18, to=100, width=28).grid(row=2, column=1, pady=5)

        # Genere
        tk.Label(frame, text="Genere:").grid(row=3, column=0, sticky="w", pady=5)
        gender_var = tk.StringVar(value="M")
        gender_frame = tk.Frame(frame)
        gender_frame.grid(row=3, column=1, sticky="w", pady=5)
        tk.Radiobutton(gender_frame, text="Maschile", variable=gender_var, value="M").pack(side=tk.LEFT)
        tk.Radiobutton(gender_frame, text="Femminile", variable=gender_var, value="F").pack(side=tk.LEFT)

        # Interessi
        tk.Label(frame, text="Interessi:").grid(row=4, column=0, sticky="w", pady=5)
        interest_frame = tk.Frame(frame)
        interest_frame.grid(row=4, column=1, sticky="w", pady=5)
        tk.Checkbutton(interest_frame, text="Sport").pack(side=tk.LEFT)
        tk.Checkbutton(interest_frame, text="Musica").pack(side=tk.LEFT)
        tk.Checkbutton(interest_frame, text="Lettura").pack(side=tk.LEFT)

        # Paese
        tk.Label(frame, text="Paese:").grid(row=5, column=0, sticky="w", pady=5)
        from tkinter import ttk
        ttk.Combobox(frame, values=["Italia", "Francia", "Germania", "Spagna"], width=27).grid(row=5, column=1, pady=5)

        # Bottoni
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Registra", bg="#4CAF50", fg="white", padx=20, pady=5).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Annulla", bg="#9E9E9E", fg="white", padx=20, pady=5).pack(side=tk.LEFT, padx=5)

        # Screenshot
        root.after(500, lambda: self.capture_window(root, "gui_form_completo.png"))
        root.after(1500, root.quit)

        root.mainloop()

    def genera_tutti(self):
        """Genera tutti gli screenshot GUI"""
        print("=== GENERAZIONE SCREENSHOT GUI ===\n")

        print("1. GUI Base...")
        self.esempio_gui_base()

        print("2. Calcolatrice...")
        self.esempio_calcolatrice()

        print("3. Form Completo...")
        self.esempio_form_completo()

        print(f"\n✓ Screenshot GUI generati in: {self.output_dir}")


if __name__ == "__main__":
    output_dir = "/Users/campion.luca/Documents/Appunti/Python/immagini/screenshots"
    generator = GUIScreenshotGenerator(output_dir)

    print("NOTA: Su macOS potrebbe richiedere permesso 'Registrazione Schermo'")
    print("      Vai in: Preferenze di Sistema > Sicurezza > Privacy > Registrazione Schermo\n")

    generator.genera_tutti()
