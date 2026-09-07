"""Validierung von E-Mail-Adressen."""

import re

# ReDoS-sicheres Muster ohne verschachtelte Quantoren: die Zeichenklassen der
# Teilausdrücke sind disjunkt, und der äußere ``+`` greift nur auf die durch
# ``.`` getrennten Domain-Labels zu, sodass der Rückverfolgungsaufwand linear
# bleibt (HTML5-Spezifikationsmuster).
_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)

_MAX_LENGTH = 254


def is_valid_email(text: str) -> bool:
    """Prüft, ob ``text`` eine syntaktisch gültige E-Mail-Adresse ist."""
    if not isinstance(text, str):
        raise TypeError("is_valid_email erwartet eine Zeichenkette (str)")
    if len(text) > _MAX_LENGTH:
        return False
    return _EMAIL_RE.fullmatch(text) is not None
