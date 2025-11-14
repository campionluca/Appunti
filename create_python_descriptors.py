#!/usr/bin/env python3
"""
Generatore descrittori Python con FOCUS PYTHONIC.
18 categorie, 20-25 descriptors, formato JSON.
Output: PYTHON_DESCRIPTORS_REPORT.json, PYTHON_COVERAGE_ANALYSIS.md
"""

import json
from typing import Any
from datetime import datetime

# ============================================================================
# DESCRITTORI PYTHON - 18 CATEGORIE
# ============================================================================

DESCRIPTORS = [
    # ---- PY-BASICS: Variabili, tipi, operatori ----
    {
        "concept_id": "PY-BASICS-001",
        "topic": "Variabili e Binding",
        "category": "PY-BASICS",
        "difficulty_level": "Beginner",
        "explanation": "In Python, le variabili non hanno tipo dichiarato; sono riferimenti a oggetti. L'assegnazione crea un binding tra nome e oggetto.",
        "code_example": "nome = 'Ada'\nanni = 27\nprint(type(nome), type(anni))  # <class 'str'>, <class 'int'>",
        "pythonic_way": "Usa nomi espliciti in snake_case (nome, anni, is_active). Evita nomi single-letter se non è loop/math.",
        "common_mistakes": "Confondere variabile con tipo; assegnare con nomi generici (x, y, data); mutare inaspettatamente.",
        "best_practices": "PEP 8: snake_case per variabili, UPPER_CASE per costanti. Usa type hints per chiarezza.",
        "learning_objectives": "Capire binding dinamico, nomi espliciti, immutabilità di tipi base (int, str, tuple).",
        "related_concepts": ["PY-BASICS-002", "PY-BASICS-003", "PY-OOP-BASIC-001"]
    },
    {
        "concept_id": "PY-BASICS-002",
        "topic": "Tipi di Dato Primitivi",
        "category": "PY-BASICS",
        "difficulty_level": "Beginner",
        "explanation": "Python dispone di tipi built-in: int, float, str, bool, None. Immutabili e con operazioni native ottimizzate.",
        "code_example": "x: int = 42\ny: float = 3.14\nmsg: str = 'hello'\nflag: bool = True\nval: None = None",
        "pythonic_way": "Usa type hints (Python 3.5+) per chiarezza. Converti esplicitamente: int(s), float(s), str(obj).",
        "common_mistakes": "Usare == con None (usa 'is None'). Confondere 0/False con 'falsy'. Non gestire ValueError in conversioni.",
        "best_practices": "Type hints nel codice moderno. Usa 'in' per membership. Preferisci immutabilità quando possibile.",
        "learning_objectives": "Conoscere i tipi base, operazioni, conversioni, valori 'falsy', short-circuit evaluation.",
        "related_concepts": ["PY-BASICS-001", "PY-CONTROL-001"]
    },
    {
        "concept_id": "PY-BASICS-003",
        "topic": "Operatori Aritmetici e Logici",
        "category": "PY-BASICS",
        "difficulty_level": "Beginner",
        "explanation": "Operatori aritmetici (+, -, *, /, //, %, **), confronto (==, <, >), logici (and, or, not) con short-circuit evaluation.",
        "code_example": "a, b = 10, 3\nprint(a + b, a * b, a ** b)  # 13, 30, 1000\nprint(a > 5 and b < 10)  # True (short-circuit)",
        "pythonic_way": "Usa 'and'/'or' per logica, non bitwise. Usa in per membership. Parentesi per chiarezza, non per ambiguità.",
        "common_mistakes": "Confondere = (assegnazione) con == (confronto). Usare 'and'/'or' per bitwise. Omettere parentesi.",
        "best_practices": "Short-circuit: 'a and expensive_call()' valuta lazy. Usa 'in' (O(1) su set/dict) prima di cicli.",
        "learning_objectives": "Precedenza operatori, short-circuit, differenza tra '==' e 'is', uso idiomatico in/not in.",
        "related_concepts": ["PY-BASICS-002", "PY-CONTROL-001", "PY-DATA-004"]
    },

    # ---- PY-CONTROL: if/elif/else, for, while ----
    {
        "concept_id": "PY-CONTROL-001",
        "topic": "Condizioni: if, elif, else",
        "category": "PY-CONTROL",
        "difficulty_level": "Beginner",
        "explanation": "Strutture decisionali. Usa 'if' per primo branch, 'elif' per alternanze, 'else' per default.",
        "code_example": "eta = 18\nif eta < 18:\n    status = 'minore'\nelif eta == 18:\n    status = 'appena_magg'\nelse:\n    status = 'maggiore'",
        "pythonic_way": "Guard clauses: early return/raise per semplificare logica. Evita annidamento profondo (max 2-3 livelli).",
        "common_mistakes": "Condizioni complicate con annidamento. 'if x == True' invece di 'if x'. Omettere else quando necessario.",
        "best_practices": "PEP 8: indentazione 4 spazi. Usa 'in' per membership. Preferisci ternary al posto di if per assignment semplici.",
        "learning_objectives": "Catene if/elif/else, boolean short-circuit, guard patterns, ternary operator (x if cond else y).",
        "related_concepts": ["PY-BASICS-002", "PY-CONTROL-002", "PY-LAMBDA-001"]
    },
    {
        "concept_id": "PY-CONTROL-002",
        "topic": "Cicli: for e while",
        "category": "PY-CONTROL",
        "difficulty_level": "Beginner",
        "explanation": "for itera su iterabili (liste, range, stringhe). while ripete finché condizione è vera.",
        "code_example": "# for idiomatico\nfor i, item in enumerate(lista):\n    print(i, item)\n\n# while con break\ncount = 0\nwhile count < 10:\n    if count == 5: break\n    count += 1",
        "pythonic_way": "for over iterabili; enumerate() per indice+valore. Preferisci range(len(x)) solo se necessario. Usa 'for...else' per logica post-loop.",
        "common_mistakes": "while True con break (usa range/iterabile). Modificare lista mentre si itera. Off-by-one in range.",
        "best_practices": "for itera su iterabili direttamente (no indici se non servono). break/continue per early exit/skip.",
        "learning_objectives": "Iterazione su sequenze, range, enumerate, zip. Break, continue, else clause su loop. List comprehension intro.",
        "related_concepts": ["PY-DATA-001", "PY-COMP-001"]
    },

    # ---- PY-FUNC: def, args, kwargs, decorators ----
    {
        "concept_id": "PY-FUNC-001",
        "topic": "Definizione Funzioni Semplici",
        "category": "PY-FUNC",
        "difficulty_level": "Beginner",
        "explanation": "Funzioni definite con 'def', parametri, return. Docstring con triple-quote per documentazione.",
        "code_example": "def add(a: int, b: int) -> int:\n    \"\"\"Somma due interi.\"\"\"\n    return a + b\n\nresult = add(2, 3)  # 5",
        "pythonic_way": "Type hints per parametri/return. Docstring (PEP 257) sintetico: one-liner o multi-linea con descrizione, args, return.",
        "common_mistakes": "Docstring assente o troppo verboso. Nomi parametri poco chiari. Funzioni che fanno troppo (SRP).",
        "best_practices": "Una funzione = una responsabilità. Parametri con valori default. Docstring conciso. Return esplicito o None.",
        "learning_objectives": "Firma funzioni, parametri, return types, docstring, pure vs impure functions, scope LEGB.",
        "related_concepts": ["PY-FUNC-002", "PY-FUNC-003", "PY-DECORATOR-001"]
    },
    {
        "concept_id": "PY-FUNC-002",
        "topic": "*args e **kwargs",
        "category": "PY-FUNC",
        "difficulty_level": "Intermediate",
        "explanation": "*args raccoglie posizionali variabili in tupla. **kwargs raccoglie nominati in dizionario.",
        "code_example": "def function(*args, **kwargs):\n    print(args)      # tupla\n    print(kwargs)    # dizionario\n\nfunction(1, 2, 3, name='Ada', age=27)",
        "pythonic_way": "Usa per API flessibili. Nome 'args'/'kwargs' per convenzione. Sempre dopo parametri fissi.",
        "common_mistakes": "Ordine sbagliato (args deve precedere kwargs). Nominare male (*a, **k). Usare quando non serve.",
        "best_practices": "Espandi con *args, **kwargs per forward; docstring chiarisce signature effettiva. Usa signature per introspezione.",
        "learning_objectives": "Unpacking posizionale/nominale. Composizione funzioni. Forwarding argomenti. Introspezione con inspect.",
        "related_concepts": ["PY-FUNC-001", "PY-LAMBDA-001"]
    },
    {
        "concept_id": "PY-FUNC-003",
        "topic": "Scope e Closure",
        "category": "PY-FUNC",
        "difficulty_level": "Intermediate",
        "explanation": "LEGB: Local, Enclosing, Global, Built-in. Closure cattura variabili dall'outer scope.",
        "code_example": "factor = 10  # Global\ndef multiply(x):\n    return x * factor  # Accede a Global\n\nresult = multiply(5)  # 50",
        "pythonic_way": "Preferisci parametri a variabili globali. Usa nonlocal/global solo se necessario. Closure utili per factory.",
        "common_mistakes": "Variabili globali mutabili. Confondere scope locale con globale. Modificare default mutabile (liste, dict).",
        "best_practices": "Evita global se possibile. Default parameter per immutabili. nonlocal per modifiche in closure.",
        "learning_objectives": "Scope LEGB, nonlocal/global keywords, closure pattern, default mutable trap, introspezione scope.",
        "related_concepts": ["PY-FUNC-001", "PY-DECORATOR-001", "PY-LAMBDA-001"]
    },

    # ---- PY-DATA: list, tuple, dict, set ----
    {
        "concept_id": "PY-DATA-001",
        "topic": "Liste (Mutable Sequences)",
        "category": "PY-DATA",
        "difficulty_level": "Beginner",
        "explanation": "Liste mutabili, ordinazione preservata (3.7+), operazioni veloci: append, extend, pop, slice.",
        "code_example": "nums = [1, 2, 3]\nnums.append(4)\nnums.extend([5, 6])\nquadrati = [n*n for n in nums]  # Comprehension",
        "pythonic_way": "List comprehension per trasformazioni. enumerate() per indice. Slice per sottosequenze. sorted() non mutate.",
        "common_mistakes": "Modificare lista mentre si itera. Assegnazione per riferimento ([a, a, a] diventa [id, id, id]). Copia superficiale.",
        "best_practices": "Comprensioni pythonic. .copy() esplicita. Evita mutazioni globali. Usa tuple/set per immutabilità.",
        "learning_objectives": "Operazioni lista (append, pop, extend, slice). List comprehension. enumerate, zip. Mutabilità.",
        "related_concepts": ["PY-DATA-002", "PY-DATA-003", "PY-COMP-001"]
    },
    {
        "concept_id": "PY-DATA-002",
        "topic": "Tuple e Unpacking",
        "category": "PY-DATA",
        "difficulty_level": "Beginner",
        "explanation": "Tuple immutabili, usabili come chiavi. Unpacking assegna posizionalmente. Swap senza temp variable.",
        "code_example": "coords = (10, 20)\nx, y = coords  # Unpacking\na, b = 1, 2; a, b = b, a  # Swap\nx, *rest = [1, 2, 3, 4]  # Extended unpacking",
        "pythonic_way": "Tuple per record fissi e chiavi dict. Unpacking per assegnamento multiplo. Extended (*) per rest.",
        "common_mistakes": "Confondere tupla singolo-elemento: (x) è int, (x,) è tupla. Unpacking cardinalità mismatch.",
        "best_practices": "Usa tuple per dati fissi. Unpacking rende codice leggibile. Named tuple per strutture.",
        "learning_objectives": "Tuple immutabilità. Unpacking, extended unpacking, swap idiomatico. Named tuples intro.",
        "related_concepts": ["PY-DATA-001", "PY-DATA-003", "PY-OOP-ADV-001"]
    },
    {
        "concept_id": "PY-DATA-003",
        "topic": "Dizionari (Key-Value Mapping)",
        "category": "PY-DATA",
        "difficulty_level": "Beginner",
        "explanation": "Dizionari ordinati (3.7+), O(1) lookup medio. Chiavi hashable, valori qualunque. .items(), .keys(), .values().",
        "code_example": "user = {'name': 'Ada', 'age': 27}\nfor k, v in user.items():\n    print(f'{k}: {v}')\nage = user.get('age', 0)  # Default 0 se assente",
        "pythonic_way": ".get(key, default) al posto di try/except. Comprensioni dict. .items() per iterare k,v. setdefault() raro.",
        "common_mistakes": "Iterare su dict (itera su chiavi). Accesso senza default (KeyError). Chiavi mutabili (no liste).",
        "best_practices": "Usa .get() per accesso sicuro. Dict comprehension per trasformazioni. defaultdict per aggregazioni.",
        "learning_objectives": "Dizionari mutabili, lookup O(1), .items()/.keys()/.values(). Dict comprehension. Ordine preservato.",
        "related_concepts": ["PY-DATA-001", "PY-DATA-004", "PY-COMP-001"]
    },
    {
        "concept_id": "PY-DATA-004",
        "topic": "Insiemi (Set e Unicità)",
        "category": "PY-DATA",
        "difficulty_level": "Intermediate",
        "explanation": "Insiemi non ordinati di elementi unici hashable. Operazioni insiemistiche: unione, intersezione, differenza.",
        "code_example": "a = {1, 2, 3}\nb = {3, 4, 5}\nprint(a | b)  # Unione\nprint(a & b)  # Intersezione\nprint(a - b)  # Differenza",
        "pythonic_way": "Set per unicità/membership. Operatori |, &, -, ^ per insiemistica. frozenset per immutabile.",
        "common_mistakes": "Confondere set() con {}  (dict vuoto). Elementi non hashable. Usare quando lista basta.",
        "best_practices": "Set per membership veloce (O(1)). Insiemistica per filtraggio. frozenset come chiavi dict.",
        "learning_objectives": "Unicità elemento. Operazioni insiemistiche. membership O(1). discard/remove. frozenset.",
        "related_concepts": ["PY-DATA-001", "PY-DATA-003", "PY-BASICS-003"]
    },

    # ---- PY-STRING: f-strings, formatting, slicing ----
    {
        "concept_id": "PY-STRING-001",
        "topic": "F-strings e Formattazione Moderna",
        "category": "PY-STRING",
        "difficulty_level": "Beginner",
        "explanation": "F-strings (PEP 498, Python 3.6+) interpolano variabili inline. Format specifiers per numeri/testo/date.",
        "code_example": "name = 'Ada'\nscore = 99.5\nprint(f'{name} scored {score:.1f}')\nprint(f'{100:.2%}')  # Percentuale",
        "pythonic_way": "F-strings per leggibilità. Format specifiers (:.2f, :>20, :#x) inline. Logica separata da formattazione.",
        "common_mistakes": "Usare % o .format() in code nuovo. Format specifiers complessi inline (estrarre logica). Quote nesting.",
        "best_practices": "F-strings per output moderni. Logica pura separata da formattazione. Template per risorse esterne.",
        "learning_objectives": "F-string syntax, format specifiers, alignment, padding, numero decimali, conversioni.",
        "related_concepts": ["PY-STRING-002", "PY-STRING-003", "PY-BASICS-002"]
    },
    {
        "concept_id": "PY-STRING-002",
        "topic": "Slicing e Operazioni String",
        "category": "PY-STRING",
        "difficulty_level": "Beginner",
        "explanation": "Stringhe immutabili. Slicing [start:stop:step], metodi strip/split/join/replace, ricerca.",
        "code_example": "s = 'Python'\nprint(s[1:4])      # 'yth'\nprint(s[::-1])     # 'nohtyP' (reverse)\nparts = 'a,b,c'.split(',')\njoined = '-'.join(parts)",
        "pythonic_way": "Slice leggibile (indici su variabili).  join() per concatenazione multipla. strip/replace per pulizia.",
        "common_mistakes": "Concatenazione con +  in loop (inefficiente). Mancanza di .split()/.join(). Slice negativo confuso.",
        "best_practices": "join() per performance. Slice per sottosequenze. strip() per input pulizia. Immutabilità = pipeline.",
        "learning_objectives": "Slice syntax, negative indices, slice notation [start:stop:step], metodi comuni, immutabilità.",
        "related_concepts": ["PY-STRING-001", "PY-DATA-001", "PY-FUNC-001"]
    },
    {
        "concept_id": "PY-STRING-003",
        "topic": "Normalizzazione e Parsing String",
        "category": "PY-STRING",
        "difficulty_level": "Intermediate",
        "explanation": "Pulizia, normalizzazione, estrazione da stringhe. Unicode, encoding, regex basics.",
        "code_example": "text = '  Hello World  '\ncleaned = text.strip().lower()\nif 'World' in cleaned:\n    print('Found')\nparts = cleaned.split()",
        "pythonic_way": "Pipeline di metodi. strip/lower/replace. startswith/endswith. find/index rarely. regex per pattern complex.",
        "common_mistakes": "Non strippare input. Case sensitivity. Regex quando semplice string method basta.",
        "best_practices": "Pipeline di metodi per leggibilità. strip() per input. Regex per pattern non trivial. 're' modulo.",
        "learning_objectives": "Metodi string comuni. Pipeline. Unicode basics. Encoding (UTF-8 default). Regex intro.",
        "related_concepts": ["PY-STRING-001", "PY-STRING-002", "PY-MODULE-005"]
    },

    # ---- PY-FILE: open(), with, context managers ----
    {
        "concept_id": "PY-FILE-001",
        "topic": "Context Managers e 'with' Statement",
        "category": "PY-FILE",
        "difficulty_level": "Intermediate",
        "explanation": "Gestione automatica risorse con 'with': acquisizione/rilascio garantiti. No try/finally manuale.",
        "code_example": "with open('file.txt', 'r') as f:\n    content = f.read()\n# File chiuso automaticamente, anche se errore",
        "pythonic_way": "Sempre 'with' per file/risorse. Supporta __enter__/__exit__ protocol. ExitStack per multipli.",
        "common_mistakes": "open() senza with (file non chiuso). Try/finally per risorse (use with instead).",
        "best_practices": "with statement è idiomatico Python. Implementa __enter__/__exit__ per risorse custom.",
        "learning_objectives": "Context manager protocol. with statement. Gestione risorse. ExitStack per composizione.",
        "related_concepts": ["PY-FILE-002", "PY-ERROR-001"]
    },
    {
        "concept_id": "PY-FILE-002",
        "topic": "Lettura/Scrittura File",
        "category": "PY-FILE",
        "difficulty_level": "Beginner",
        "explanation": "I/O file: read(), write(), readline(), iterazione righe. Encoding (UTF-8 default). Modi: r, w, a, rb, wb.",
        "code_example": "with open('data.txt', 'r', encoding='utf-8') as f:\n    for line in f:  # Iterazione linea per linea\n        process(line.strip())",
        "pythonic_way": "Itera file direttamente (lazy). Specifica encoding. strip() per newline. context manager always.",
        "common_mistakes": "Non specificare encoding. Carica intero file in memoria. Dimentica close (use with).",
        "best_practices": "with statement. Iterazione lazy. UTF-8 encoding esplicito. Piccoli file: .read(), grandi: iterazione.",
        "learning_objectives": "Apertura file, modi, encoding, iterazione lazy, readlines/read, write/writelines.",
        "related_concepts": ["PY-FILE-001", "PY-STRING-002", "PY-ERROR-001"]
    },

    # ---- PY-ERROR: try/except, custom exceptions ----
    {
        "concept_id": "PY-ERROR-001",
        "topic": "Gestione Eccezioni: try/except/finally",
        "category": "PY-ERROR",
        "difficulty_level": "Intermediate",
        "explanation": "try/except cattura errori. finally garantisce cleanup. Eccezioni gerarchiche.",
        "code_example": "try:\n    x = int(input('Numero: '))\nexcept ValueError:\n    print('Non è numerico')\nfinally:\n    print('Cleanup')",
        "pythonic_way": "Cattura eccezioni specifiche, non Exception. Usa else per 'no error' logic. finally per cleanup.",
        "common_mistakes": "Bare 'except:'. Cattura troppo generale. Ignorare eccezioni (silenzio). Exception vs BaseException.",
        "best_practices": "Cattura specifico. Re-raise con 'raise'. else per logic post-try. finally per cleanup garantito.",
        "learning_objectives": "Gerarchia eccezioni. try/except/else/finally. Specificity. Re-raise. Context manager vs try/finally.",
        "related_concepts": ["PY-ERROR-002", "PY-FILE-001", "PY-OOP-ADV-001"]
    },
    {
        "concept_id": "PY-ERROR-002",
        "topic": "Eccezioni Personalizzate",
        "category": "PY-ERROR",
        "difficulty_level": "Intermediate",
        "explanation": "Definisci Exception custom ereditando da Exception. Usa per segnalare errori specifici del dominio.",
        "code_example": "class InsufficientFundsError(Exception):\n    pass\n\nraise InsufficientFundsError('Account overdraft')",
        "pythonic_way": "Eredita da Exception. Nome termina con 'Error'. Docstring per contratto. Usa specifiche nel codice.",
        "common_mistakes": "Eredita da BaseException. Nome generico. Passaggio messaggio mancato.",
        "best_practices": "Gerarchia: Exception > Custom parent > Specifico. Docstring. __init__ per attributi custom.",
        "learning_objectives": "Eccezioni custom. Gerarchia. Ereditarietà. Uso di raise con messaggi chiari.",
        "related_concepts": ["PY-ERROR-001", "PY-OOP-BASIC-001", "PY-OOP-ADV-001"]
    },

    # ---- PY-MODULE: import, __name__, packages ----
    {
        "concept_id": "PY-MODULE-001",
        "topic": "Import e Moduli",
        "category": "PY-MODULE",
        "difficulty_level": "Beginner",
        "explanation": "import nome, from x import y, import x as z. Moduli = file .py. Packages = cartelle con __init__.py.",
        "code_example": "import os\nfrom pathlib import Path\nfrom collections import defaultdict as dd\n\nprint(os.getcwd())\npath = Path('.')",
        "pythonic_way": "Import specifici da moduli. Relative imports in packages. Evita 'from x import *'. PEP 8: import order.",
        "common_mistakes": "'from x import *' (namespace pollution). Circular imports. Import in funzioni (slow).",
        "best_practices": "Import top-file. Ordine: stdlib, third-party, local. Uno import per riga (per merge clarity).",
        "learning_objectives": "Import syntax. Moduli. Packages. sys.path. __init__.py. Relative imports.",
        "related_concepts": ["PY-MODULE-002", "PY-MODULE-003", "PY-OOP-BASIC-001"]
    },
    {
        "concept_id": "PY-MODULE-002",
        "topic": "__name__ e Main Block",
        "category": "PY-MODULE",
        "difficulty_level": "Beginner",
        "explanation": "'if __name__ == \"__main__\":' esegue solo se lo script è invocato direttamente, non importato.",
        "code_example": "def hello():\n    print('Hello')\n\nif __name__ == '__main__':\n    hello()",
        "pythonic_way": "Main block per codice di test/esecuzione. Permette sia import sia esecuzione.",
        "common_mistakes": "Codice globale fuori main (effetti side-effect su import). Ignorare __name__.",
        "best_practices": "Sempre main block per moduli eseguibili. Facilita testing e riuso.",
        "learning_objectives": "Differenza __name__ == '__main__' vs importato. Main execution pattern.",
        "related_concepts": ["PY-MODULE-001", "PY-MODULE-003"]
    },
    {
        "concept_id": "PY-MODULE-003",
        "topic": "Packages e Namespace",
        "category": "PY-MODULE",
        "difficulty_level": "Intermediate",
        "explanation": "Packages = cartelle con __init__.py. Namespace organizzato. Subpackages con gerarchia.",
        "code_example": "# Struttura: myapp/__init__.py, myapp/utils/__init__.py, myapp/utils/helpers.py\nfrom myapp.utils.helpers import process\n\n# __init__.py può esporre API pubblica\n# from .helpers import process as __all__",
        "pythonic_way": "__all__ per API pubblica. Relative import dentro package. __init__.py minimalista.",
        "common_mistakes": "Circular imports (refactor moduli). Namespace pollution (use __all__).",
        "best_practices": "__all__ list per esportazione. __init__.py thin (import per convenienza, non logica).",
        "learning_objectives": "Package structure. __all__. Relative import. Namespace organization.",
        "related_concepts": ["PY-MODULE-001", "PY-MODULE-002"]
    },

    # ---- PY-OOP-BASIC: class, __init__, self ----
    {
        "concept_id": "PY-OOP-BASIC-001",
        "topic": "Classi e Istanze",
        "category": "PY-OOP-BASIC",
        "difficulty_level": "Beginner",
        "explanation": "Classi definiscono tipi. __init__ inizializza, self è istanza. Metodi operano su istanza.",
        "code_example": "class Dog:\n    def __init__(self, name: str):\n        self.name = name\n    \n    def bark(self) -> str:\n        return f'{self.name} says Woof!'\n\ndog = Dog('Rex')\nprint(dog.bark())",
        "pythonic_way": "Type hints in __init__. Docstring per classe. self sempre primo parametro. Attributi in __init__.",
        "common_mistakes": "Dimentica self. Attributi globali. __init__ senza docstring. Logica nel __init__ (separare in metodi).",
        "best_practices": "Classe = un concetto. __init__ solo per setup. Metodi piccoli (SRP). Docstring classe e metodi.",
        "learning_objectives": "Classe definizione. __init__. self. Istanze vs classe. Metodi vs funzioni.",
        "related_concepts": ["PY-OOP-ADV-001", "PY-OOP-ADV-002", "PY-OOP-ADV-003"]
    },
    {
        "concept_id": "PY-OOP-BASIC-002",
        "topic": "Attributi e Metodi",
        "category": "PY-OOP-BASIC",
        "difficulty_level": "Beginner",
        "explanation": "Attributi = dati su istanza. Metodi = funzioni su istanza (primo arg = self).",
        "code_example": "class Counter:\n    def __init__(self):\n        self.count = 0\n    \n    def increment(self):\n        self.count += 1\n        return self.count\n\nc = Counter()\nprint(c.increment())  # 1",
        "pythonic_way": "Attributi via self.name in __init__. Metodi per operazioni. Usa property() per getter/setter complessi.",
        "common_mistakes": "Attributi non dichiarati in __init__ (confusione). Logica in getter/setter. Modifiche globali.",
        "best_practices": "Attributi in __init__. Metodi per comportamento. Underscore prefix per 'private' (Python convention).",
        "learning_objectives": "Attributi istanza. Metodi istanza. self binding. Constructor, destructor (__del__ rare).",
        "related_concepts": ["PY-OOP-BASIC-001", "PY-OOP-ADV-002", "PY-OOP-ADV-003"]
    },

    # ---- PY-OOP-ADV: inheritance, property, @staticmethod ----
    {
        "concept_id": "PY-OOP-ADV-001",
        "topic": "Ereditarietà",
        "category": "PY-OOP-ADV",
        "difficulty_level": "Intermediate",
        "explanation": "Sottoclasse eredita da superclasse. super() chiama metodo genitore. MRO (Method Resolution Order).",
        "code_example": "class Animal:\n    def speak(self):\n        return 'Some sound'\n\nclass Dog(Animal):\n    def speak(self):\n        return 'Woof!'\n\ndog = Dog()\nprint(dog.speak())",
        "pythonic_way": "super() per override. Single inheritance semplice. Multiple inheritance rara (MRO complesso).",
        "common_mistakes": "super() call mancato. Ereditarietà profonda (>3 livelli). Name shadowing accidentale.",
        "best_practices": "super() invece di parent class name. Liskov Substitution Principle. Preferi composizione a ereditarietà.",
        "learning_objectives": "Classe base/derivata. super(). Override metodi. MRO (C3 linearization).",
        "related_concepts": ["PY-OOP-BASIC-001", "PY-OOP-ADV-002", "PY-OOP-ADV-003"]
    },
    {
        "concept_id": "PY-OOP-ADV-002",
        "topic": "Property e Getter/Setter",
        "category": "PY-OOP-ADV",
        "difficulty_level": "Intermediate",
        "explanation": "@property decorator crea getter. @name.setter per setter. Accesso come attributo, logica come metodo.",
        "code_example": "class Circle:\n    def __init__(self, radius: float):\n        self._radius = radius\n    \n    @property\n    def area(self) -> float:\n        return 3.14159 * self._radius ** 2\n\nc = Circle(5)\nprint(c.area)  # Accesso come attributo",
        "pythonic_way": "Property per getter semplici. Setter raro (mutabilità segnalata). Underscore prefix _radius.",
        "common_mistakes": "Property su calcoli expensive (cache externally). Setter con logica pesante. Accesso diretto vs property.",
        "best_practices": "Property per interfaccia stabile. Calcoli semplici in property. Logica pesante in metodi.",
        "learning_objectives": "Decorator @property. @name.setter. Attributi computati. Lazy evaluation.",
        "related_concepts": ["PY-OOP-BASIC-001", "PY-OOP-ADV-001", "PY-DECORATOR-001"]
    },
    {
        "concept_id": "PY-OOP-ADV-003",
        "topic": "@staticmethod e @classmethod",
        "category": "PY-OOP-ADV",
        "difficulty_level": "Intermediate",
        "explanation": "@staticmethod non accede self/cls. @classmethod riceve cls come primo arg. Utili per factory/utility.",
        "code_example": "class Math:\n    @staticmethod\n    def add(a, b):\n        return a + b\n    \n    @classmethod\n    def from_string(cls, s):\n        return cls(*map(int, s.split(',')))",
        "pythonic_way": "@staticmethod per utility puri. @classmethod per factory/alternate constructors.",
        "common_mistakes": "Usare quando funzione globale basta. Mescolare con istanza (confusione self).",
        "best_practices": "staticmethod = funzione correlata, non istanza. classmethod = alternate constructor, factory.",
        "learning_objectives": "@staticmethod, @classmethod. cls vs self. Factory pattern. Utility methods.",
        "related_concepts": ["PY-OOP-BASIC-001", "PY-OOP-ADV-001", "PY-DECORATOR-001"]
    },

    # ---- PY-DECORATOR: @decorator syntax ----
    {
        "concept_id": "PY-DECORATOR-001",
        "topic": "Decoratori Funzioni",
        "category": "PY-DECORATOR",
        "difficulty_level": "Intermediate",
        "explanation": "@decorator avvolge funzione per estendere comportamento. Sostituisce funzione con wrapper.",
        "code_example": "def log_calls(fn):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {fn.__name__}')\n        return fn(*args, **kwargs)\n    return wrapper\n\n@log_calls\ndef greet(name):\n    return f'Hello, {name}!'",
        "pythonic_way": "Usa functools.wraps per preservare metadati. Decoratori semplici per una responsabilità.",
        "common_mistakes": "Dimenticare functools.wraps (perde __name__, __doc__). Decoratore complesso (separare in classi).",
        "best_practices": "functools.wraps sempre. Decoratore per cross-cutting concern (logging, timing, caching).",
        "learning_objectives": "Decorator pattern. Closure. functools.wraps. Composizione decoratori.",
        "related_concepts": ["PY-DECORATOR-002", "PY-FUNC-003", "PY-OOP-ADV-002"]
    },
    {
        "concept_id": "PY-DECORATOR-002",
        "topic": "Decoratori con Argomenti",
        "category": "PY-DECORATOR",
        "difficulty_level": "Advanced",
        "explanation": "Decoratore factory: @decorator(arg) richiede outer function che ritorna decorator.",
        "code_example": "def repeat(times):\n    def decorator(fn):\n        def wrapper(*args, **kwargs):\n            results = []\n            for _ in range(times):\n                results.append(fn(*args, **kwargs))\n            return results\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef say_hi():\n    return 'Hi!'",
        "pythonic_way": "Decoratore factory per parametrizzazione. Usa functools.wraps in innermost wrapper.",
        "common_mistakes": "Ordine nesting confuso. Argomenti decoratore vs funzione decorata.",
        "best_practices": "Leggibilità: docstring chiaro. Factory pattern per parametri decoratore.",
        "learning_objectives": "Decoratore factory. Triple nesting (factory, decorator, wrapper). Parametri.",
        "related_concepts": ["PY-DECORATOR-001", "PY-FUNC-003"]
    },

    # ---- PY-ITER: yield, generators, itertools ----
    {
        "concept_id": "PY-ITER-001",
        "topic": "Generator e yield",
        "category": "PY-ITER",
        "difficulty_level": "Intermediate",
        "explanation": "yield produce valori lazily. Genera iteratore senza lista in memoria. Usato in for loop.",
        "code_example": "def count_up(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\n\nfor num in count_up(5):\n    print(num)  # 0, 1, 2, 3, 4",
        "pythonic_way": "Generator per flussi. yield per produce-consume pattern. Generator expression (x for x in seq).",
        "common_mistakes": "Generator esaurimento (iterare due volte). Confondere con list (crea una volta).",
        "best_practices": "Generator per grandi dataset. Composizione con itertools. Generator expression leggibile.",
        "learning_objectives": "yield semantica. Generator come iteratore. send() e close(). Generator expression.",
        "related_concepts": ["PY-ITER-002", "PY-COMP-001", "PY-FUNC-003"]
    },
    {
        "concept_id": "PY-ITER-002",
        "topic": "itertools e Composizione",
        "category": "PY-ITER",
        "difficulty_level": "Intermediate",
        "explanation": "itertools: chain, cycle, repeat, islice, filterfalse, accumulate. Composizione di iteratori.",
        "code_example": "from itertools import chain, islice, cycle\n\ndata = chain([1, 2], [3, 4], [5, 6])\nfirst_three = list(islice(data, 3))  # [1, 2, 3]\nrepeated = cycle([1, 2])  # Infinito",
        "pythonic_way": "itertools per pipeline lazy. Composizione di generatori. Avoid materializing (list) se possibile.",
        "common_mistakes": "Materializzare presto (list). Itertools con dati piccoli (overkill).",
        "best_practices": "itertools per logica lazy e composizionale. chain, islice, map, filter comune.",
        "learning_objectives": "itertools principali (chain, cycle, repeat, islice, combinations, permutations).",
        "related_concepts": ["PY-ITER-001", "PY-LAMBDA-001", "PY-COMP-001"]
    },

    # ---- PY-COMP: list/dict comprehension ----
    {
        "concept_id": "PY-COMP-001",
        "topic": "List and Dict Comprehensions",
        "category": "PY-COMP",
        "difficulty_level": "Intermediate",
        "explanation": "[expr for item in seq if cond]. Comprensione di lista/dict/set. Più leggibile di map/filter.",
        "code_example": "nums = [1, 2, 3, 4, 5]\nsquares = [n*n for n in nums if n % 2 == 0]\ndata = {i: i*i for i in range(5)}\n\n# Equivalente a:\nsquares = list(map(lambda n: n*n, filter(lambda n: n % 2 == 0, nums)))",
        "pythonic_way": "Comprensioni per trasformazione leggibile. Nidificazione max 2 livelli. Usa nome chiaro per item.",
        "common_mistakes": "Nidificazione profonda (estrarre in funzione). Logica complessa in comprensione.",
        "best_practices": "Leggibilità priorità. if clause per filtro semplice. Estrarre logica complessa.",
        "learning_objectives": "Sintassi comprensione. if clause. Nidificazione. Dict/set comprehension. Generator expression.",
        "related_concepts": ["PY-COMP-002", "PY-LAMBDA-001", "PY-DATA-001"]
    },
    {
        "concept_id": "PY-COMP-002",
        "topic": "Set and Generator Comprehensions",
        "category": "PY-COMP",
        "difficulty_level": "Intermediate",
        "explanation": "{expr for item in seq} per set. (expr for item in seq) per generator expression.",
        "code_example": "unique = {n for n in [1, 1, 2, 2, 3]}\ngen = (n*n for n in range(10))\nfirst = next(gen)  # Lazy evaluation",
        "pythonic_way": "Set comprehension per unicità. Generator expression per lazy evaluation e memoria.",
        "common_mistakes": "Generatore vs lista esaurimento. Set comprehension con dati piccoli.",
        "best_practices": "Generator expression per grandi dataset/infinite. Set per unicità.",
        "learning_objectives": "Set comprehension. Generator expression. Lazy evaluation. next() e StopIteration.",
        "related_concepts": ["PY-COMP-001", "PY-ITER-001", "PY-DATA-004"]
    },

    # ---- PY-LAMBDA: lambda, map/filter/reduce ----
    {
        "concept_id": "PY-LAMBDA-001",
        "topic": "Lambda e Funzioni Anonime",
        "category": "PY-LAMBDA",
        "difficulty_level": "Intermediate",
        "explanation": "lambda x: x*2 crea funzione anonima. Utile per callback brevi. Preferire def per logica complessa.",
        "code_example": "nums = [1, 2, 3]\nsquares = list(map(lambda x: x*x, nums))\nsorted_by_len = sorted(['a', 'bb', 'ccc'], key=lambda s: len(s))",
        "pythonic_way": "Lambda per callback semplici. Preferir def se multi-statement. Comprehension over map/filter.",
        "common_mistakes": "Lambda complessa (usa def). map/filter quando comprehension più leggibile.",
        "best_practices": "Lambda semplice one-liner. key= argument in sorted/max/min. Comprehension per chiarezza.",
        "learning_objectives": "Lambda sintassi. map/filter/reduce principi. Comprehension vs map/filter.",
        "related_concepts": ["PY-LAMBDA-002", "PY-COMP-001", "PY-FUNC-001"]
    },
    {
        "concept_id": "PY-LAMBDA-002",
        "topic": "map, filter, reduce",
        "category": "PY-LAMBDA",
        "difficulty_level": "Intermediate",
        "explanation": "map/filter/reduce applicano funzione su iterabile. Meno leggibile che comprehension in Python moderno.",
        "code_example": "from functools import reduce\n\nnums = [1, 2, 3, 4]\nsum_result = reduce(lambda a, b: a + b, nums)  # 10\n\n# Preferito in Python moderno:\nsum_result = sum(nums)",
        "pythonic_way": "Comprehension preferred. map/filter rare (legacy, funzionale). reduce() via functools.",
        "common_mistakes": "map/filter quando comprehension più chiaro. reduce() quando funzione built-in sufficit.",
        "best_practices": "Comprehension per readability. sum/min/max/any/all per aggregazioni comuni.",
        "learning_objectives": "map/filter/reduce semantica. Preferenza comprehension. Built-in function (sum, min, max).",
        "related_concepts": ["PY-LAMBDA-001", "PY-COMP-001"]
    },

    # ---- PY-WEB: Flask routes, templates ----
    {
        "concept_id": "PY-WEB-001",
        "topic": "Flask: Route e Decorator",
        "category": "PY-WEB",
        "difficulty_level": "Intermediate",
        "explanation": "@app.route('/path') mappa URL a funzione. Flask lightweight web framework. Request/Response via decorators.",
        "code_example": "from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n@app.route('/hello', methods=['GET'])\ndef hello():\n    name = request.args.get('name', 'World')\n    return jsonify({'message': f'Hello, {name}!'})",
        "pythonic_way": "Decorator per route. jsonify per JSON response. Blueprint per moduli. type hint su view function.",
        "common_mistakes": "Logica business in view (separare in moduli). No error handling. CORS issues.",
        "best_practices": "Blueprint per struttura moduli. Separare routing da logica. Error handler decorator.",
        "learning_objectives": "Flask app, route, request context. GET/POST/PUT/DELETE. jsonify e response.",
        "related_concepts": ["PY-WEB-002", "PY-MODULE-001", "PY-ERROR-001"]
    },
    {
        "concept_id": "PY-WEB-002",
        "topic": "Template e Jinja2",
        "category": "PY-WEB",
        "difficulty_level": "Intermediate",
        "explanation": "Jinja2 templating in Flask. Separazione HTML da logica. {{ var }}, {% if %}, {% for %}.",
        "code_example": "from flask import Flask, render_template\napp = Flask(__name__)\n\n@app.route('/users/<name>')\ndef user(name):\n    return render_template('user.html', username=name, items=[1, 2, 3])\n\n# user.html:\n# <h1>{{ username }}</h1>\n# {% for item in items %}\n#   <p>{{ item }}</p>\n# {% endfor %}",
        "pythonic_way": "render_template per logica separata. Eredità template (base.html). Template filter per format.",
        "common_mistakes": "Logica nel template (muovi in view). Template injection (sanitize input). Hardcode in HTML.",
        "best_practices": "Base template per layout. Block inheritance. Context dictionary per dati.",
        "learning_objectives": "Jinja2 syntax. Block inheritance. Filter, macro. Template anti-pattern.",
        "related_concepts": ["PY-WEB-001", "PY-STRING-001"]
    },

    # ---- PY-DB: sqlite3, SQLAlchemy basics ----
    {
        "concept_id": "PY-DB-001",
        "topic": "SQLite3 e Query Basiche",
        "category": "PY-DB",
        "difficulty_level": "Intermediate",
        "explanation": "sqlite3 modulo per database SQLite. Connect, cursor, execute, commit, close.",
        "code_example": "import sqlite3\n\nconn = sqlite3.connect(':memory:')\ncursor = conn.cursor()\ncursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\ncursor.execute('INSERT INTO users (name) VALUES (?)', ('Ada',))\nconn.commit()\n\nresults = cursor.execute('SELECT * FROM users').fetchall()\nconn.close()",
        "pythonic_way": "Parametrized query (?) per SQL injection prevention. Context manager per connection.",
        "common_mistakes": "String concatenation per query (SQL injection). Not commit(). Non chiudere connection.",
        "best_practices": "with statement per auto-close. Parametrized query sempre. Transazione per consistency.",
        "learning_objectives": "sqlite3 connect/cursor/execute. Transaction, commit, rollback. Fetch results.",
        "related_concepts": ["PY-DB-002", "PY-FILE-001", "PY-ERROR-001"]
    },
    {
        "concept_id": "PY-DB-002",
        "topic": "SQLAlchemy ORM Basics",
        "category": "PY-DB",
        "difficulty_level": "Advanced",
        "explanation": "SQLAlchemy ORM mappa classi Python a tabelle. Query fluido. Relationship management automatico.",
        "code_example": "from sqlalchemy import create_engine, Column, Integer, String\nfrom sqlalchemy.orm import declarative_base, Session\n\nBase = declarative_base()\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    name = Column(String)\n\nengine = create_engine('sqlite:///:memory:')\nBase.metadata.create_all(engine)\n\nwith Session(engine) as session:\n    user = User(name='Ada')\n    session.add(user)\n    session.commit()",
        "pythonic_way": "Declarative model. Session context manager. Query API fluido. Relazione lazy loading.",
        "common_mistakes": "N+1 query (eager load con joinedload). Session scope gestione. DetachedInstanceError.",
        "best_practices": "Session per transazione. eager_load per join. Relationship back_populates. Lazy='joined'.",
        "learning_objectives": "Declarative base. Column type. Relationship (ForeignKey, backref). Query API. Session lifecycle.",
        "related_concepts": ["PY-DB-001", "PY-OOP-BASIC-001", "PY-ERROR-001"]
    },

    # ---- PY-NAO: NAOqi API, motion, vision ----
    {
        "concept_id": "PY-NAO-001",
        "topic": "Introduzione NAOqi e Motion",
        "category": "PY-NAO",
        "difficulty_level": "Advanced",
        "explanation": "NAOqi è SDK per robot NAO. Motion ALProxy per movimenti. Gait, animation, joint control.",
        "code_example": "from nao import ALProxy\n\nmotion = ALProxy('ALMotion', '127.0.0.1', 9559)\npostureProxy = ALProxy('ALRobotPosture', '127.0.0.1', 9559)\n\n# Postura iniziale\npostureProxy.goToPosture('StandInit', 0.5)\n\n# Movimento forward\nmotion.moveToward(0.5, 0, 0)  # x, y, theta",
        "pythonic_way": "NAOqi proxy pattern. Gestione errori per connessione fallita. Context manager per resource cleanup.",
        "common_mistakes": "Postura non iniziale. Non attendere movimento. IP/port sbagliato.",
        "best_practices": "Inizializzazione postura. Stiffness management. Timeout su operazioni blocking.",
        "learning_objectives": "ALProxy pattern. Postura iniziale. moveToward, turn, motion parameter. Joint control.",
        "related_concepts": ["PY-NAO-002", "PY-OOP-BASIC-001", "PY-ERROR-001"]
    },
    {
        "concept_id": "PY-NAO-002",
        "topic": "NAOqi Vision e Audio",
        "category": "PY-NAO",
        "difficulty_level": "Advanced",
        "explanation": "ALVideoDevice per visione (frame camera). ALAudioPlayer per suoni. Face/object detection.",
        "code_example": "from nao import ALProxy\n\nvideo = ALProxy('ALVideoDevice', '127.0.0.1', 9559)\naudio = ALProxy('ALAudioPlayer', '127.0.0.1', 9559)\n\n# Cattura frame\nclient_name = video.subscribe('test_client', 2, 4, 15)\nimage_remote = video.getImageRemote(client_name)\nvideo.unsubscribe(client_name)\n\n# Riproduzione audio\naudio.playFile('/data/sound/hello.wav')",
        "pythonic_way": "Camera subscription per frame acquisition. Unsubscribe al termine. Gestione buffer immagini.",
        "common_mistakes": "Memory leak (non unsubscribe). Frame processing bloccante (usar thread). Formato immagine mismatch.",
        "best_practices": "Subscribe/unsubscribe pattern. Threading per frame processing. Resize per performance.",
        "learning_objectives": "ALVideoDevice subscribe/unsubscribe. Frame format. Camera parameter. Audio playback.",
        "related_concepts": ["PY-NAO-001", "PY-FILE-001", "PY-ITER-001"]
    }
]

# ============================================================================
# COVERAGE ANALYSIS
# ============================================================================

COVERAGE_DATA = {
    "PY-BASICS": {"descriptors": 3, "topics": ["Variabili", "Tipi", "Operatori"], "pythonic_focus": "Type hints, snake_case, falsy values"},
    "PY-CONTROL": {"descriptors": 2, "topics": ["if/elif/else", "for/while"], "pythonic_focus": "Guard clauses, enumerate(), short-circuit"},
    "PY-FUNC": {"descriptors": 3, "topics": ["def basics", "*args/**kwargs", "Scope/closure"], "pythonic_focus": "Docstring, type hints, pure functions"},
    "PY-DATA": {"descriptors": 4, "topics": ["Liste", "Tuple", "Dizionari", "Insiemi"], "pythonic_focus": "Unpacking, comprehension, .get(), set operations"},
    "PY-STRING": {"descriptors": 3, "topics": ["F-strings", "Slicing", "Parsing"], "pythonic_focus": "F-string idiomatico, .join(), method chaining"},
    "PY-FILE": {"descriptors": 2, "topics": ["with statement", "I/O file"], "pythonic_focus": "Context manager, encoding UTF-8, lazy iteration"},
    "PY-ERROR": {"descriptors": 2, "topics": ["try/except", "Custom exceptions"], "pythonic_focus": "Specific exception catch, EAFP, re-raise"},
    "PY-MODULE": {"descriptors": 3, "topics": ["import", "__name__", "Packages"], "pythonic_focus": "__all__, relative import, main block"},
    "PY-OOP-BASIC": {"descriptors": 2, "topics": ["class/__init__", "Attributi/metodi"], "pythonic_focus": "self idiomatico, SRP, docstring"},
    "PY-OOP-ADV": {"descriptors": 3, "topics": ["Ereditarietà", "property", "@staticmethod/@classmethod"], "pythonic_focus": "super(), Liskov, factory pattern"},
    "PY-DECORATOR": {"descriptors": 2, "topics": ["@decorator", "@decorator(args)"], "pythonic_focus": "functools.wraps, cross-cutting concern"},
    "PY-ITER": {"descriptors": 2, "topics": ["yield/generator", "itertools"], "pythonic_focus": "Lazy evaluation, pipeline composizione"},
    "PY-COMP": {"descriptors": 2, "topics": ["List/dict comprehension", "Set/generator"], "pythonic_focus": "Leggibilità, max nesting 2, if clause"},
    "PY-LAMBDA": {"descriptors": 2, "topics": ["lambda", "map/filter/reduce"], "pythonic_focus": "Comprehension over map/filter, key=lambda"},
    "PY-WEB": {"descriptors": 2, "topics": ["Flask route", "Jinja2 template"], "pythonic_focus": "@app.route, Blueprint, template inheritance"},
    "PY-DB": {"descriptors": 2, "topics": ["sqlite3", "SQLAlchemy ORM"], "pythonic_focus": "Parametrized query, Session context, eager load"},
    "PY-NAO": {"descriptors": 2, "topics": ["Motion", "Vision/Audio"], "pythonic_focus": "ALProxy pattern, subscribe/unsubscribe, error handling"},
}

# ============================================================================
# GENERATORE REPORT
# ============================================================================

def generate_python_descriptors_json():
    """Genera report JSON descrittori Python."""
    report = {
        "metadata": {
            "title": "Python Descriptors Report - Pythonic Focus",
            "description": "Descrittori Python con focus su idiomi pythonic, PEP 8, best practices",
            "generated_at": datetime.now().isoformat(),
            "total_descriptors": len(DESCRIPTORS),
            "total_categories": len(COVERAGE_DATA),
            "language": "it",
            "format_version": "1.0"
        },
        "descriptors": DESCRIPTORS,
        "statistics": {
            "categories": list(COVERAGE_DATA.keys()),
            "descriptors_per_category": {cat: data["descriptors"] for cat, data in COVERAGE_DATA.items()},
            "total_pythonic_idioms": sum(1 for d in DESCRIPTORS if "pythonic_way" in d and d["pythonic_way"]),
            "difficulty_distribution": {
                "Beginner": sum(1 for d in DESCRIPTORS if d["difficulty_level"] == "Beginner"),
                "Intermediate": sum(1 for d in DESCRIPTORS if d["difficulty_level"] == "Intermediate"),
                "Advanced": sum(1 for d in DESCRIPTORS if d["difficulty_level"] == "Advanced"),
            }
        }
    }
    return report


def generate_coverage_markdown():
    """Genera coverage analysis in Markdown."""
    md_lines = [
        "# Python Coverage Analysis - Pythonic Focus\n",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        f"**Total Descriptors**: {sum(d['descriptors'] for d in COVERAGE_DATA.values())}\n",
        f"**Total Categories**: {len(COVERAGE_DATA)}\n\n",
        "## Categorie Coperte\n"
    ]

    for category, data in sorted(COVERAGE_DATA.items()):
        md_lines.append(f"\n### {category}\n")
        md_lines.append(f"**Descriptors**: {data['descriptors']}\n\n")
        md_lines.append(f"**Topics**: {', '.join(data['topics'])}\n\n")
        md_lines.append(f"**Pythonic Focus**: _{data['pythonic_focus']}_\n\n")

    md_lines.append("\n## Summary Idiomi Pythonic\n\n")
    md_lines.append("| Idioma Pythonic | Descrizione | Categoria |\n")
    md_lines.append("|---|---|---|\n")

    pythonic_idioms = [
        ("Type Hints", "Dichiarazioni tipo explicit per clarity", "PY-BASICS, PY-FUNC, PY-OOP"),
        ("F-strings", "Interpolazione stringa moderna e leggibile", "PY-STRING"),
        ("List Comprehension", "Trasformazione dati idiomatica", "PY-COMP, PY-DATA"),
        ("with statement", "Context manager per risorse", "PY-FILE, PY-ERROR"),
        ("Unpacking", "Assegnazione multipla e swap", "PY-DATA-002"),
        ("enumerate()", "Iterazione con indice idiomatico", "PY-CONTROL, PY-DATA"),
        ("@decorator", "Pattern per cross-cutting concern", "PY-DECORATOR, PY-OOP"),
        ("Generator & yield", "Lazy evaluation e pipeline", "PY-ITER, PY-COMP"),
        ("Property @property", "Getter/setter come attributo", "PY-OOP-ADV"),
        ("super()", "Ereditarietà idiomatica", "PY-OOP-ADV"),
        (".get() on dict", "Accesso sicuro dizionario", "PY-DATA-003"),
        ("Guard Clause", "Early return per logica semplice", "PY-CONTROL, PY-FUNC"),
        ("__name__ == '__main__'", "Main block pattern", "PY-MODULE"),
        ("EAFP Pattern", "Easier Ask Forgiveness than Permission", "PY-ERROR"),
    ]

    for idiom, desc, cat in pythonic_idioms:
        md_lines.append(f"| `{idiom}` | {desc} | {cat} |\n")

    md_lines.append("\n## Difficulty Distribution\n\n")
    stats = {
        "Beginner": sum(1 for d in DESCRIPTORS if d["difficulty_level"] == "Beginner"),
        "Intermediate": sum(1 for d in DESCRIPTORS if d["difficulty_level"] == "Intermediate"),
        "Advanced": sum(1 for d in DESCRIPTORS if d["difficulty_level"] == "Advanced"),
    }
    for level, count in stats.items():
        md_lines.append(f"- **{level}**: {count} descriptors\n")

    md_lines.append("\n## Note Implementazione\n\n")
    md_lines.append("- Focus su **PEP 8** compliance\n")
    md_lines.append("- Esempi inclusi mostrano **Pythonic way** vs anti-pattern\n")
    md_lines.append("- **best_practices** documentano idiomi Python moderni\n")
    md_lines.append("- **related_concepts** facilitano learning path interconnesso\n")
    md_lines.append("- NAOqi incluso come dominio applicativo avanzato\n")

    return "".join(md_lines)


if __name__ == "__main__":
    # Genera JSON
    report = generate_python_descriptors_json()
    json_path = "/home/user/Appunti/PYTHON_DESCRIPTORS_REPORT.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"✓ JSON salvato: {json_path}")

    # Genera Markdown
    md_content = generate_coverage_markdown()
    md_path = "/home/user/Appunti/PYTHON_COVERAGE_ANALYSIS.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✓ Markdown salvato: {md_path}")

    # Summary
    print(f"\n{'='*60}")
    print("PYTHON DESCRIPTORS - SOMMARIO")
    print(f"{'='*60}")
    print(f"Total Descriptors: {report['metadata']['total_descriptors']}")
    print(f"Total Categories: {report['metadata']['total_categories']}")
    print(f"Difficulty Beginner: {report['statistics']['difficulty_distribution']['Beginner']}")
    print(f"Difficulty Intermediate: {report['statistics']['difficulty_distribution']['Intermediate']}")
    print(f"Difficulty Advanced: {report['statistics']['difficulty_distribution']['Advanced']}")
    print(f"Pythonic Idioms: {report['statistics']['total_pythonic_idioms']}")
    print(f"{'='*60}\n")
