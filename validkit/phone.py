"""Normalisierung von Telefonnummern."""

_COUNTRY_CODES = {
    "DE": "49",
    "AT": "43",
    "CH": "41",
    "FR": "33",
    "GB": "44",
    "US": "1",
    "IT": "39",
    "ES": "34",
    "NL": "31",
    "BE": "32",
    "PL": "48",
    "CZ": "420",
    "DK": "45",
    "SE": "46",
    "NO": "47",
    "FI": "358",
    "PT": "351",
    "GR": "30",
    "IE": "353",
    "LU": "352",
    "JP": "81",
    "CN": "86",
    "IN": "91",
    "BR": "55",
    "AU": "61",
    "CA": "1",
    "RU": "7",
}

_SEPARATORS = "-()"


def normalize_phone(text: str, country_code: str) -> str:
    """Normalisiert ``text`` anhand von ``country_code`` in ein kanonisches E.164-Format.

    Entfernt Leerzeichen, Bindestriche und Klammern, ersetzt eine führende Null durch
    die Landesvorwahl und stellt dem Ergebnis ein ``+`` voran. Bereits internationale
    Nummern (mit ``+``) werden lediglich von Trennzeichen bereinigt.
    """
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")
    if not isinstance(country_code, str):
        raise TypeError("country_code muss ein String sein")

    calling_code = _COUNTRY_CODES.get(country_code.upper())
    if calling_code is None:
        raise ValueError("unbekannter Ländercode; erwartet wird ein ISO-3166-alpha-2-Code")

    cleaned = "".join(ch for ch in text if not ch.isspace() and ch not in _SEPARATORS)

    if not cleaned:
        raise ValueError("Telefonnummer darf nicht leer sein")

    if cleaned.startswith("+"):
        digits = cleaned[1:]
        if not digits or not digits.isdigit():
            raise ValueError("Telefonnummer enthält ungültige Zeichen; erwartet werden Ziffern")
        return "+" + digits

    if cleaned.startswith("0"):
        cleaned = cleaned[1:]

    if not cleaned or not cleaned.isdigit():
        raise ValueError("Telefonnummer enthält ungültige Zeichen; erwartet werden Ziffern")

    return "+" + calling_code + cleaned
