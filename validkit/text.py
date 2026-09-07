"""Textnormalisierung: Akzente, Slugs und Maskierung."""

import re
import unicodedata


def strip_accents(text: str) -> str:
    """Entfernt diakritische Zeichen (Akzente) aus ``text``."""
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")
    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def slugify(text: str) -> str:
    """Erzeugt einen URL-freundlichen Slug aus ``text``."""
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")
    stripped = strip_accents(text).lower()
    replaced = re.sub(r"[^a-z0-9]+", "-", stripped)
    return replaced.strip("-")


def mask_secret(text: str, keep: int = 4) -> str:
    """Maskiert ``text`` und lässt die letzten ``keep`` Zeichen sichtbar."""
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")
    if not isinstance(keep, int):
        raise TypeError("keep muss eine ganze Zahl sein")
    if keep < 0:
        raise ValueError("keep darf nicht negativ sein")
    if keep >= len(text):
        return text
    if keep == 0:
        return "*" * len(text)
    return "*" * (len(text) - keep) + text[-keep:]
