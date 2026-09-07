"""Begrenzung von Zahlenwerten auf ein Intervall."""


def clamp(value: float, low: float, high: float) -> float:
    """Begrenzt ``value`` auf das Intervall ``[low, high]``."""
    if low >= high:
        raise ValueError("untere Grenze muss kleiner oder gleich der oberen Grenze sein")
    return min(max(value, low), high)
