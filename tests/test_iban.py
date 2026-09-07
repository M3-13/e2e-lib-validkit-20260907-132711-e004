"""Unit-Tests für validkit.iban.is_valid_iban."""

import pytest

from validkit.iban import is_valid_iban


def test_valid_german_iban():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_german_iban_without_spaces():
    assert is_valid_iban("DE89370400440532013000") is True


def test_invalid_checksum():
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False


def test_valid_gb_iban():
    assert is_valid_iban("GB82 WEST 1234 5698 7654 32") is True


def test_valid_french_iban():
    assert is_valid_iban("FR14 2004 1010 0505 0001 3M02 606") is True


def test_lowercase_is_normalized():
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_tabs_are_normalized_like_spaces():
    assert is_valid_iban("DE89\t3704\t0044\t0532\t0130\t00") is True


def test_mixed_case_and_spacing():
    assert is_valid_iban("de89\t3704 0044 0532 0130 00") is True


def test_malformed_too_short_raises():
    with pytest.raises(ValueError):
        is_valid_iban("123")


def test_empty_string_raises():
    with pytest.raises(ValueError):
        is_valid_iban("")


def test_whitespace_only_raises():
    with pytest.raises(ValueError):
        is_valid_iban("   ")


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(123)  # type: ignore[arg-type]


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(None)  # type: ignore[arg-type]


def test_invalid_characters_raise():
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704 0044 0532 0130 0!")


def test_missing_country_code_raises():
    with pytest.raises(ValueError):
        is_valid_iban("89370400440532013000")


def test_unknown_country_code_raises():
    with pytest.raises(ValueError):
        is_valid_iban("XX00 1234 5678 9012 3456 78")


def test_non_digit_check_digits_raise():
    with pytest.raises(ValueError):
        is_valid_iban("DEAA 3704 0044 0532 0130 00")


def test_wrong_length_for_country_raises():
    # Deutsche IBAN hat exakt 22 Zeichen.
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704 0044 0532 0130 0000")


def test_exact_length_boundary_min():
    # NO (Norwegen) hat mit 15 Zeichen die kürzeste zulässige IBAN.
    assert is_valid_iban("NO93 8601 1117 947") is True


def test_pure_function_returns_consistent_result():
    text = "DE89 3704 0044 0532 0130 00"
    assert is_valid_iban(text) == is_valid_iban(text)
