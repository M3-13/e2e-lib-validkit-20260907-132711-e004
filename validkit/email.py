"""Validierung von E-Mail-Adressen."""

import re

# ReDoS-sicheres Muster ohne verschachtelte Quantoren: Jeder Quantor wirkt hier
# ausschließlich auf eine Zeichenklasse bzw. ein einzelnes Zeichen, niemals auf
# eine Gruppe. Die Feinstruktur der Domain (Punkttrennung, Label-Länge, keine
# Bindestriche an den Rändern) wird anschließend deterministisch und linear in
# Python geprüft — ohne Backtracking-Potenzial.
_LOCAL_PART_RE = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+$")
_DOMAIN_RE = re.compile(r"^[A-Za-z0-9.-]+$")

_MAX_LENGTH = 254
_MAX_LABEL_LENGTH = 63


def is_valid_email(text: str) -> bool:
    """Prüft, ob ``text`` eine syntaktisch gültige E-Mail-Adresse ist."""
    if not isinstance(text, str):
        raise TypeError("is_valid_email erwartet eine Zeichenkette (str)")
    if len(text) > _MAX_LENGTH:
        return False

    if "@" not in text:
        return False
    local_part, _, domain = text.partition("@")
    if "@" in domain:
        return False

    if not local_part or not domain:
        return False
    if _LOCAL_PART_RE.fullmatch(local_part) is None:
        return False
    if _DOMAIN_RE.fullmatch(domain) is None:
        return False

    labels = domain.split(".")
    if len(labels) < 2:
        return False
    for label in labels:
        if not label or len(label) > _MAX_LABEL_LENGTH:
            return False
        if label.startswith("-") or label.endswith("-"):
            return False
    return True
