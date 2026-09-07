"""Unit-Tests für ``luhn_check`` und ``is_valid_isbn13``."""

import pytest

from validkit.validators import is_valid_isbn13, luhn_check


class TestLuhnCheck:
    def test_known_valid_number(self):
        assert luhn_check("79927398713") is True

    def test_known_invalid_number(self):
        assert luhn_check("79927398710") is False

    def test_single_zero(self):
        assert luhn_check("0") is True

    def test_single_nonzero_digit(self):
        assert luhn_check("5") is False

    def test_even_length_invalid(self):
        assert luhn_check("43") is False

    def test_even_length_valid_check(self):
        assert luhn_check("18") is True

    def test_all_zeros(self):
        assert luhn_check("0000000000000000") is True

    def test_empty_raises_value_error(self):
        with pytest.raises(ValueError):
            luhn_check("")

    def test_non_digit_raises_value_error(self):
        with pytest.raises(ValueError):
            luhn_check("7992739871A")

    def test_whitespace_raises_value_error(self):
        with pytest.raises(ValueError):
            luhn_check("799 27398713")

    def test_wrong_type_raises_type_error(self):
        with pytest.raises(TypeError):
            luhn_check(79927398713)

    def test_error_message_does_not_leak_input(self):
        with pytest.raises(ValueError) as excinfo:
            luhn_check("7992739871A")
        assert "7992739871A" not in str(excinfo.value)


class TestIsValidIsbn13:
    def test_known_valid_isbn(self):
        assert is_valid_isbn13("9780306406157") is True

    def test_known_invalid_isbn(self):
        assert is_valid_isbn13("9780306406158") is False

    def test_another_valid_isbn(self):
        assert is_valid_isbn13("9783161484100") is True

    def test_another_invalid_isbn(self):
        assert is_valid_isbn13("9783161484101") is False

    def test_too_short_raises_value_error(self):
        with pytest.raises(ValueError):
            is_valid_isbn13("978030640615")

    def test_too_long_raises_value_error(self):
        with pytest.raises(ValueError):
            is_valid_isbn13("97803064061571")

    def test_empty_raises_value_error(self):
        with pytest.raises(ValueError):
            is_valid_isbn13("")

    def test_non_digit_raises_value_error(self):
        with pytest.raises(ValueError):
            is_valid_isbn13("978030640615X")

    def test_letters_wrong_length_raises_value_error(self):
        with pytest.raises(ValueError):
            is_valid_isbn13("abcdefghijklm")

    def test_wrong_type_raises_type_error(self):
        with pytest.raises(TypeError):
            is_valid_isbn13(9780306406157)

    def test_error_message_does_not_leak_input(self):
        with pytest.raises(ValueError) as excinfo:
            is_valid_isbn13("978030640615X")
        assert "978030640615X" not in str(excinfo.value)
