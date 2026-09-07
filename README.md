# validkit

`validkit` ist eine eigenständige, schlanke Python-Bibliothek mit neun kleinen,
voneinander unabhängigen, reinen Prüf- und Normalisierungsfunktionen. Es gibt
keine CLI, keine UI und keinen Netzwerkzugriff — jede Funktion ist rein und
nebenwirkungsfrei: gleiche Eingabe ergibt stets gleiche Ausgabe.

## Tech-Stack

- **Sprache:** Python
- **Laufzeit:** Python 3.10+
- **Abhängigkeiten:** ausschließlich Python-Standardbibliothek (keine Laufzeit-Abhängigkeiten)
- **Testing:** pytest (einzige Entwicklungsabhängigkeit)

## Installation

```bash
pip install -e .
```

Die Entwicklungsabhängigkeiten (pytest) installierst du zusätzlich mit:

```bash
pip install -e ".[dev]"
```

## Tests ausführen

```bash
pytest
```

## Verwendung

Alle neun Funktionen sind über die öffentliche API aus `validkit` importierbar:

```python
from validkit import (
    is_valid_email,
    luhn_check,
    is_valid_iban,
    is_valid_isbn13,
    normalize_phone,
    strip_accents,
    mask_secret,
    slugify,
    clamp,
)
```

### Beispiele pro Funktion

```python
is_valid_email("test@example.com")  # True

luhn_check("4111111111111111")  # True (Visa-Testnummer)

is_valid_iban("DE89370400440532013000")  # True

is_valid_isbn13("9780306406157")  # True

normalize_phone("+49 170 1234567", "DE")  # "+491701234567"

strip_accents("café")  # "cafe"

slugify("Hello World!")  # "hello-world"

mask_secret("1234567890", keep=4)  # "******7890"

clamp(15.0, 0.0, 10.0)  # 10.0
```

## Fehlerverhalten

- Falscher Eingabetyp führt zu einem `TypeError`.
- Ungültiger Wert, ungültiges Format oder ungültiger Ländercode führt zu einem
  `ValueError`.
- Fehlermeldungen nennen ausschließlich die Fehlerart und die erwartete Form,
  niemals den übergebenen Eingabewert.

## Funktionen

| Funktion | Modul | Signatur |
| --- | --- | --- |
| `is_valid_email` | `validkit.email` | `(text: str) -> bool` |
| `luhn_check` | `validkit.validators` | `(digits: str) -> bool` |
| `is_valid_isbn13` | `validkit.validators` | `(text: str) -> bool` |
| `is_valid_iban` | `validkit.iban` | `(text: str) -> bool` |
| `normalize_phone` | `validkit.phone` | `(text: str, country_code: str) -> str` |
| `strip_accents` | `validkit.text` | `(text: str) -> str` |
| `slugify` | `validkit.text` | `(text: str) -> str` |
| `mask_secret` | `validkit.text` | `(text: str, keep: int = 4) -> str` |
| `clamp` | `validkit.clamp` | `(value: float, low: float, high: float) -> float` |
