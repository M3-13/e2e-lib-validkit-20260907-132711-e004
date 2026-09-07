"""Tests für die öffentliche API von validkit."""

import validkit

EXPECTED_ALL = [
    "clamp",
    "is_valid_email",
    "is_valid_iban",
    "is_valid_isbn13",
    "luhn_check",
    "mask_secret",
    "normalize_phone",
    "slugify",
    "strip_accents",
]


def test_all_exports_exactly_the_nine_names():
    assert sorted(validkit.__all__) == sorted(EXPECTED_ALL)
    assert len(validkit.__all__) == 9


def test_every_exported_name_is_importable():
    for name in EXPECTED_ALL:
        assert hasattr(validkit, name)
        assert callable(getattr(validkit, name))


def test_from_import_delivers_all_nine_names():
    from validkit import (
        clamp,
        is_valid_email,
        is_valid_iban,
        is_valid_isbn13,
        luhn_check,
        mask_secret,
        normalize_phone,
        slugify,
        strip_accents,
    )

    assert callable(is_valid_email)
    assert callable(luhn_check)
    assert callable(is_valid_iban)
    assert callable(is_valid_isbn13)
    assert callable(normalize_phone)
    assert callable(strip_accents)
    assert callable(mask_secret)
    assert callable(slugify)
    assert callable(clamp)
