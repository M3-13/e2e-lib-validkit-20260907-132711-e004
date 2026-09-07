"""Allgemeine Validatoren: Luhn-Prüfsumme und ISBN-13."""


def luhn_check(digits: str) -> bool:
    """Prüft eine Ziffernfolge gegen den Luhn-Algorithmus."""
    if not isinstance(digits, str):
        raise TypeError("Erwartet wird eine Zeichenkette aus Ziffern.")
    if not digits:
        raise ValueError("Die Eingabe darf nicht leer sein.")
    if not digits.isascii() or not digits.isdigit():
        raise ValueError("Erlaubt sind ausschließlich Ziffern (0-9).")

    total = 0
    parity = len(digits) % 2
    for index, char in enumerate(digits):
        digit = int(char)
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0


def is_valid_isbn13(text: str) -> bool:
    """Prüft, ob ``text`` eine gültige ISBN-13 ist."""
    if not isinstance(text, str):
        raise TypeError("Erwartet wird eine Zeichenkette.")
    if len(text) != 13:
        raise ValueError("Eine ISBN-13 muss genau 13 Zeichen lang sein.")
    if not text.isascii() or not text.isdigit():
        raise ValueError("Eine ISBN-13 darf nur Ziffern (0-9) enthalten.")

    total = 0
    for index in range(12):
        digit = int(text[index])
        total += digit if index % 2 == 0 else digit * 3
    check_digit = (10 - total % 10) % 10
    return check_digit == int(text[12])
