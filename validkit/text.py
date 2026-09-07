"""Textnormalisierung: Akzente, Slugs und Maskierung."""


def strip_accents(text: str) -> str:
    """Entfernt diakritische Zeichen (Akzente) aus ``text``."""
    raise NotImplementedError


def slugify(text: str) -> str:
    """Erzeugt einen URL-freundlichen Slug aus ``text``."""
    raise NotImplementedError


def mask_secret(text: str, keep: int = 4) -> str:
    """Maskiert ``text`` und lässt die letzten ``keep`` Zeichen sichtbar."""
    raise NotImplementedError
