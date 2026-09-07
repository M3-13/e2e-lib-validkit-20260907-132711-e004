"""Unit-Tests für validkit.phone.normalize_phone."""

import pytest

from validkit.phone import normalize_phone


def test_national_number_with_spaces():
    assert normalize_phone("030 1234567", "DE") == "+49301234567"


def test_national_number_with_hyphens():
    assert normalize_phone("030-123-45-67", "DE") == "+49301234567"


def test_national_number_with_parentheses():
    assert normalize_phone("(030) 1234567", "DE") == "+49301234567"


def test_national_number_with_mixed_separators():
    assert normalize_phone(" 030 - 123 (4567) ", "DE") == "+49301234567"


def test_national_number_without_separators():
    assert normalize_phone("0301234567", "DE") == "+49301234567"


def test_already_international_number_stays_unchanged():
    assert normalize_phone("+49 30 1234567", "DE") == "+49301234567"


def test_already_international_number_without_separators():
    assert normalize_phone("+49301234567", "DE") == "+49301234567"


def test_international_number_ignores_country_code():
    assert normalize_phone("+1 555 123 4567", "DE") == "+15551234567"


def test_other_country_code():
    assert normalize_phone("01 234 5678", "AT") == "+4312345678"


def test_us_country_code_without_leading_zero():
    assert normalize_phone("555 123 4567", "US") == "+15551234567"


def test_lowercase_country_code_is_accepted():
    assert normalize_phone("030 1234567", "de") == "+49301234567"


def test_leading_zero_is_replaced_by_country_code():
    assert normalize_phone("0221 123456", "DE") == "+49221123456"


def test_unknown_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "ZZ")


def test_unknown_country_code_lowercase_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "zz")


def test_empty_input_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", "DE")


def test_only_separators_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone(" - ( ) ", "DE")


def test_only_leading_zero_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0", "DE")


def test_only_plus_sign_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("+", "DE")


def test_invalid_characters_raise_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 abc", "DE")


def test_international_number_with_invalid_characters_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("+49 30 abc", "DE")


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(123, "DE")


def test_non_string_country_code_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", 49)


def test_unknown_country_code_message_contains_no_input_value():
    with pytest.raises(ValueError) as exc_info:
        normalize_phone("030 1234567", "ZZ")
    assert "ZZ" not in str(exc_info.value)


def test_invalid_character_message_contains_no_input_value():
    with pytest.raises(ValueError) as exc_info:
        normalize_phone("030 abc", "DE")
    assert "abc" not in str(exc_info.value)


def test_is_pure_and_deterministic():
    assert normalize_phone("030 1234567", "DE") == normalize_phone("030 1234567", "DE")
