# Code Policies - Python

> Standard, convenzioni e politiche di scrittura del codice per il libro su Python

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Codice](#template-di-codice)
- [Struttura dei File](#struttura-dei-file)
- [Best Practices](#best-practices)
- [Pattern di Programmazione](#pattern-di-programmazione)
- [Gestione Errori](#gestione-errori)
- [Commenti e Documentazione](#commenti-e-documentazione)

---

## Standard di Scrittura

### Formattazione (PEP 8)
- **Indentazione**: 4 spazi (no tab)
- **Lunghezza linea**: max 88 caratteri (Black) o 79 (PEP 8 strict)
- **Encoding**: UTF-8
- **Fine riga**: LF (Unix)
- **Blank lines**: 2 linee vuote tra classi/funzioni top-level, 1 tra metodi

### Stile del Codice
```python
# Esempio di stile preferito
def calculate_total(items: list[dict], tax_rate: float = 0.2) -> float:
    """Calculate total with tax."""
    if not items:
        return 0.0

    subtotal = sum(item["price"] for item in items)
    total = subtotal * (1 + tax_rate)

    return round(total, 2)


class ShoppingCart:
    """Shopping cart implementation."""

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        self.items: list[dict] = []

    def add_item(self, item: dict) -> None:
        """Add item to cart."""
        self.items.append(item)
```

### Regole Generali
- [ ] Seguire PEP 8 (Style Guide for Python Code)
- [ ] Usare type hints (PEP 484)
- [ ] Preferire list comprehension a map/filter
- [ ] Usare f-strings per formattazione (Python 3.6+)
- [ ] Import assoluti preferiti ai relativi

---

## Convenzioni di Nomenclatura

### Variabili e Funzioni
- **Variabili**: `snake_case` - Esempio: `user_name`, `total_count`
- **Costanti**: `UPPER_SNAKE_CASE` - Esempio: `MAX_SIZE`, `API_KEY`
- **Funzioni**: `snake_case` - Esempio: `calculate_total()`, `get_user_by_id()`
- **Private**: `_leading_underscore` - Esempio: `_internal_method()`
- **Dunder**: `__double_underscore__` - Solo per metodi speciali

### Classi e Moduli
- **Classi**: `PascalCase` - Esempio: `UserManager`, `HttpClient`
- **Exceptions**: `PascalCase` con suffisso Error - Esempio: `ValidationError`
- **Moduli**: `snake_case` - Esempio: `user_service.py`, `data_processor.py`
- **Packages**: `snake_case` - Esempio: `my_package`

### Type Variables
- **Type vars**: `PascalCase` - Esempio: `T`, `KT`, `VT`

---

## Template di Codice

### Template Modulo
```python
"""
Module for user management operations.

This module provides functionality for creating, updating, and managing
user accounts in the system.

Example:
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com")
"""

from __future__ import annotations

import logging
from typing import Optional, List
from dataclasses import dataclass
from pathlib import Path

# Third-party imports
import requests

# Local imports
from .models import User
from .exceptions import UserNotFoundError

__version__ = "1.0.0"
__author__ = "Nome Autore"

logger = logging.getLogger(__name__)

# Constants
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3


@dataclass
class Config:
    """Configuration for user manager."""

    api_url: str
    timeout: int = DEFAULT_TIMEOUT
    retries: int = MAX_RETRIES


class UserManager:
    """Manage user operations."""

    def __init__(self, config: Config) -> None:
        """
        Initialize UserManager.

        Args:
            config: Configuration object

        Raises:
            ValueError: If config is invalid
        """
        self.config = config
        self._cache: dict[str, User] = {}

    def get_user(self, user_id: str) -> Optional[User]:
        """
        Retrieve user by ID.

        Args:
            user_id: The unique user identifier

        Returns:
            User object if found, None otherwise

        Raises:
            UserNotFoundError: If user doesn't exist
        """
        # Implementation
        pass

    def _internal_method(self) -> None:
        """Private helper method."""
        pass


def standalone_function(param: str) -> int:
    """
    Standalone function example.

    Args:
        param: Input parameter

    Returns:
        Processed result
    """
    return len(param)


if __name__ == "__main__":
    # Example usage or tests
    manager = UserManager(Config(api_url="http://api.example.com"))
    print(f"Manager initialized: {manager}")
```

### Template Classe
```python
from typing import Optional, ClassVar
from dataclasses import dataclass, field


class BaseClass:
    """Base class example."""

    class_variable: ClassVar[int] = 0

    def __init__(self, name: str, value: int = 0) -> None:
        """Initialize base class."""
        self.name = name
        self.value = value
        self._internal_state: Optional[str] = None

    def public_method(self) -> str:
        """Public method accessible from outside."""
        return self._process_data()

    def _process_data(self) -> str:
        """Private method for internal use."""
        return f"{self.name}: {self.value}"

    def __str__(self) -> str:
        """String representation."""
        return f"BaseClass(name={self.name!r}, value={self.value})"

    def __repr__(self) -> str:
        """Official representation."""
        return f"BaseClass({self.name!r}, {self.value})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        if not isinstance(other, BaseClass):
            return NotImplemented
        return self.name == other.name and self.value == other.value


@dataclass
class DataClass:
    """Example using dataclass."""

    name: str
    age: int
    email: Optional[str] = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validation after initialization."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
```

### Template Script
```python
#!/usr/bin/env python3
"""
Script description.

Usage:
    python script.py --input file.txt --output result.txt
"""

import argparse
import logging
import sys
from pathlib import Path


def setup_logging(verbose: bool = False) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Input file path",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output file path",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()
    setup_logging(args.verbose)

    logger = logging.getLogger(__name__)
    logger.info(f"Processing {args.input}")

    try:
        # Main logic here
        logger.info(f"Output written to {args.output}")
        return 0
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

---

## Struttura dei File

### Organizzazione Modulo
```
1. Shebang (#!/usr/bin/env python3) - solo per script
2. Module docstring
3. Future imports (from __future__ import)
4. Standard library imports
5. Third-party imports
6. Local application imports
7. __all__ (se necessario)
8. Constants
9. Module-level variables
10. Classes
11. Functions
12. if __name__ == "__main__" block
```

### Organizzazione Package
```
my_package/
├── __init__.py
├── core/
│   ├── __init__.py
│   └── models.py
├── services/
│   ├── __init__.py
│   └── user_service.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── exceptions.py
└── constants.py
```

---

## Best Practices

### Pythonic Code
- **Use comprehensions**: `[x*2 for x in range(10)]` invece di loop
- **Use context managers**: `with open() as f:` per gestione risorse
- **Use generators**: Per iterazione efficiente su grandi dataset
- **Use enumerate**: `for i, item in enumerate(items):` invece di range(len())
- **Use zip**: `for a, b in zip(list1, list2):` per iterare parallele

### Codice Pulito
- [ ] Funzioni max 20-30 righe
- [ ] Parametri max 5 per funzione
- [ ] Usare type hints ovunque
- [ ] Preferire immutabilità quando possibile
- [ ] Usare dataclasses per strutture dati

### Type Hints
```python
from typing import Optional, Union, List, Dict, Callable, TypeVar

# Basic types
def greet(name: str) -> str:
    return f"Hello, {name}"

# Optional
def find_user(user_id: str) -> Optional[User]:
    pass

# Union
def process(value: Union[int, str]) -> bool:
    pass

# Collections (Python 3.9+)
def process_items(items: list[dict[str, int]]) -> None:
    pass

# Callable
def apply(func: Callable[[int], str], value: int) -> str:
    return func(value)

# TypeVar for generics
T = TypeVar("T")

def first(items: list[T]) -> Optional[T]:
    return items[0] if items else None
```

### Performance
- [ ] Usare list comprehension invece di append in loop
- [ ] Preferire set per membership test (O(1) vs O(n))
- [ ] Usare generators per lazy evaluation
- [ ] Evitare concatenazioni string in loop (usare join)
- [ ] Profilare prima di ottimizzare (cProfile, line_profiler)

---

## Pattern di Programmazione

### Pattern Consigliati

```python
# Pattern 1: Context Manager
from contextlib import contextmanager

@contextmanager
def managed_resource(name: str):
    """Context manager example."""
    resource = acquire_resource(name)
    try:
        yield resource
    finally:
        release_resource(resource)

# Usage:
with managed_resource("db") as db:
    db.query()

# Pattern 2: Decorator
from functools import wraps
import time

def timing_decorator(func):
    """Decorator to measure execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)

# Pattern 3: Property
class Temperature:
    """Temperature with validation."""

    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

# Pattern 4: Factory
def create_processor(processor_type: str):
    """Factory pattern."""
    processors = {
        "text": TextProcessor,
        "image": ImageProcessor,
        "video": VideoProcessor,
    }

    processor_class = processors.get(processor_type)
    if processor_class is None:
        raise ValueError(f"Unknown processor type: {processor_type}")

    return processor_class()

# Pattern 5: Singleton (usando module)
# singleton.py
class _Singleton:
    def __init__(self):
        self.value = 0

instance = _Singleton()  # Una sola istanza

# Usage in other modules:
from singleton import instance
```

### Anti-Pattern da Evitare

```python
# ❌ EVITARE: Mutable default arguments
def bad_function(items=[]):  # MALE! Lista condivisa tra chiamate
    items.append(1)
    return items

# ✅ PREFERIRE:
def good_function(items=None):
    if items is None:
        items = []
    items.append(1)
    return items

# ❌ EVITARE: Bare except
try:
    risky_operation()
except:  # Cattura anche KeyboardInterrupt, SystemExit!
    pass

# ✅ PREFERIRE:
try:
    risky_operation()
except Exception as e:
    logger.error(f"Error: {e}")

# ❌ EVITARE: String concatenation in loop
result = ""
for item in items:
    result += str(item)  # Inefficiente!

# ✅ PREFERIRE:
result = "".join(str(item) for item in items)
```

---

## Gestione Errori

### Exception Handling

```python
# Specifiche exceptions
try:
    data = fetch_data()
    process(data)
except ConnectionError as e:
    logger.error(f"Connection failed: {e}")
    retry()
except ValueError as e:
    logger.error(f"Invalid data: {e}")
    handle_invalid_data()
except Exception as e:
    logger.error(f"Unexpected error: {e}", exc_info=True)
    raise
finally:
    cleanup()

# Custom exceptions
class ApplicationError(Exception):
    """Base exception for application."""
    pass

class ValidationError(ApplicationError):
    """Raised when validation fails."""

    def __init__(self, field: str, message: str) -> None:
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

# Raise with context
try:
    external_operation()
except ExternalError as e:
    raise ApplicationError("Operation failed") from e

# Suppressing exceptions (use sparingly)
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("optional_file.txt")
```

### Assertions
```python
# Use for internal checks (disabled with -O)
def calculate_percentage(value: int, total: int) -> float:
    assert total > 0, "Total must be positive"
    assert 0 <= value <= total, "Value out of range"
    return (value / total) * 100

# Don't use assertions for input validation!
# Use explicit checks instead:
if total <= 0:
    raise ValueError("Total must be positive")
```

---

## Commenti e Documentazione

### Docstrings (Google Style)

```python
def function_with_types_in_docstring(param1: int, param2: str) -> bool:
    """
    Summary line in one sentence.

    Extended description of function. Can span multiple lines and
    explain the purpose and behavior in detail.

    Args:
        param1: The first parameter, represents count
        param2: The second parameter, user name

    Returns:
        True if successful, False otherwise

    Raises:
        ValueError: If param1 is negative
        TypeError: If param2 is not a string

    Examples:
        >>> function_with_types_in_docstring(10, "test")
        True

    Note:
        This function is not thread-safe.

    See Also:
        - other_function(): Related functionality
    """
    if param1 < 0:
        raise ValueError("param1 must be non-negative")
    return True


class ExampleClass:
    """
    Summary of class purpose.

    Detailed description of the class, what it represents,
    and how it should be used.

    Attributes:
        attr1: Description of attr1
        attr2: Description of attr2

    Examples:
        >>> obj = ExampleClass("value")
        >>> obj.method()
        'result'
    """

    def __init__(self, value: str) -> None:
        """Initialize with value."""
        self.value = value
```

### Commenti Inline

```python
# TODO(username): Implement caching for better performance
# FIXME: This breaks with Unicode characters
# HACK: Workaround for library bug #12345
# NOTE: This algorithm assumes sorted input

# Commenta il "perché", non il "cosa"
# ✅ BUONO:
# Using 60-second timeout because the API can be slow under load
TIMEOUT = 60

# ❌ CATTIVO:
# Set timeout to 60
TIMEOUT = 60

# Type ignore quando necessario
result = some_untyped_library_function()  # type: ignore[no-untyped-call]
```

---

## Note Aggiuntive

### Versione Python
- **Target**: Python 3.10+ (specificare versione minima)
- **Features moderne**: Match/case, union types (|), dataclasses, type hints

### Tool e Linter
- **Formatter**: Black, isort
- **Linter**: Ruff (o Flake8, Pylint)
- **Type checker**: mypy, pyright
- **Testing**: pytest, unittest
- **Coverage**: pytest-cov

### Requirements File
```txt
# requirements.txt
requests>=2.28.0,<3.0.0
numpy>=1.24.0
pandas>=2.0.0

# requirements-dev.txt
black==23.0.0
ruff==0.1.0
mypy==1.7.0
pytest==7.4.0
pytest-cov==4.1.0
```

### Configurazione Tools

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py310']

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.10"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

### Riferimenti
- PEP 8 – Style Guide for Python Code
- PEP 257 – Docstring Conventions
- PEP 484 – Type Hints
- Google Python Style Guide
- The Hitchhiker's Guide to Python

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
