"""Validierung internationaler Bankkontonummern (IBAN)."""

from string import ascii_uppercase, digits

# Länge (Gesamtlänge inkl. Ländercode und Prüfziffern) je Land nach ISO 13616.
_COUNTRY_LENGTHS = {
    "AD": 24,
    "AE": 23,
    "AL": 28,
    "AT": 20,
    "AZ": 28,
    "BA": 20,
    "BE": 16,
    "BG": 22,
    "BH": 22,
    "BI": 27,
    "BR": 29,
    "BY": 28,
    "CH": 21,
    "CR": 22,
    "CY": 28,
    "CZ": 24,
    "DE": 22,
    "DJ": 27,
    "DK": 18,
    "DO": 28,
    "EE": 20,
    "EG": 29,
    "ES": 24,
    "FI": 18,
    "FO": 18,
    "FR": 27,
    "GB": 22,
    "GE": 22,
    "GI": 23,
    "GL": 18,
    "GR": 27,
    "GT": 28,
    "HR": 21,
    "HU": 28,
    "IE": 22,
    "IL": 23,
    "IQ": 23,
    "IS": 26,
    "IT": 27,
    "JO": 30,
    "KW": 30,
    "KZ": 20,
    "LB": 28,
    "LC": 32,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "LV": 21,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "MK": 19,
    "MR": 27,
    "MT": 31,
    "MU": 30,
    "NL": 18,
    "NO": 15,
    "PK": 24,
    "PL": 28,
    "PS": 29,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "RS": 22,
    "SA": 24,
    "SC": 31,
    "SE": 24,
    "SI": 19,
    "SK": 24,
    "SM": 27,
    "ST": 25,
    "SV": 28,
    "TL": 23,
    "TN": 24,
    "TR": 26,
    "UA": 29,
    "VA": 22,
    "VG": 24,
    "XK": 20,
}

_MIN_LENGTH = 15
_MAX_LENGTH = 34
_ALPHANUM = ascii_uppercase + digits


def _to_integer(letter: str) -> int:
    """Wandelt einen alphanumerischen Zeichenwert in seine Zahlendarstellung um."""
    if letter in digits:
        return int(letter)
    return ord(letter) - ord("A") + 10


def is_valid_iban(text: str) -> bool:
    """Prüft, ob ``text`` eine gültige IBAN ist."""
    if not isinstance(text, str):
        raise TypeError(
            "is_valid_iban erwartet einen String; die Eingabe muss als Text übergeben werden."
        )

    normalized = text.replace(" ", "").replace("\t", "").upper()

    if not normalized:
        raise ValueError(
            "IBAN ist leer; erwartet wird ein Ländercode, zwei Prüfziffern und eine BBAN."
        )

    if len(normalized) < _MIN_LENGTH or len(normalized) > _MAX_LENGTH:
        raise ValueError("IBAN hat eine unzulässige Länge; erwartet werden 15 bis 34 Zeichen.")

    if not all(c in _ALPHANUM for c in normalized):
        raise ValueError("IBAN enthält ungültige Zeichen; erlaubt sind nur Buchstaben und Ziffern.")

    if normalized[0] not in ascii_uppercase or normalized[1] not in ascii_uppercase:
        raise ValueError(
            "IBAN beginnt nicht mit einem gültigen Ländercode; erwartet "
            "werden zwei Buchstaben am Anfang."
        )

    if not (normalized[2].isdigit() and normalized[3].isdigit()):
        raise ValueError(
            "IBAN hat keine gültigen Prüfziffern; erwartet werden zwei Ziffern an Position 3 und 4."
        )

    country = normalized[:2]
    if country not in _COUNTRY_LENGTHS:
        raise ValueError(
            "IBAN verwendet einen unbekannten Ländercode; der Ländercode "
            "muss einem bekannten Land entsprechen."
        )

    if len(normalized) != _COUNTRY_LENGTHS[country]:
        raise ValueError("IBAN hat eine für den Ländercode unzulässige Länge.")

    rearranged = normalized[4:] + normalized[:4]
    numeric = "".join(str(_to_integer(c)) for c in rearranged)

    return int(numeric) % 97 == 1
