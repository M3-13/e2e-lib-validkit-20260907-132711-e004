"""Allgemeine Validatoren: Luhn-Prüfsumme und ISBN-13."""


def luhn_check(digits: str) -> bool:
    """Prüft eine Ziffernfolge gegen den Luhn-Algorithmus."""
    raise NotImplementedError


def is_valid_isbn13(text: str) -> bool:
    """Prüft, ob ``text`` eine gültige ISBN-13 ist."""
    raise NotImplementedError
