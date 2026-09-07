"""Unit-Tests für :func:`validkit.email.is_valid_email`."""

import re

import pytest

from validkit.email import is_valid_email


@pytest.mark.parametrize(
    "address",
    [
        "user@example.com",
        "first.last@example.co.uk",
        "a@b.co",
        "name+tag@example.com",
        "user_name@example.com",
        "user-name@example.com",
        "123@example.com",
        "user@sub.domain.example.com",
        "user@example.technology",
    ],
)
def test_valid_addresses(address):
    assert is_valid_email(address) is True


@pytest.mark.parametrize(
    "address",
    [
        "",
        "nicht-valide",
        "plainaddress",
        "user@",
        "@example.com",
        "user@.com",
        "user@example",
        "user name@example.com",
        "user@example..com",
        "user@@example.com",
        "user@exa mple.com",
    ],
)
def test_invalid_formats(address):
    assert is_valid_email(address) is False


def test_empty_string_is_invalid():
    assert is_valid_email("") is False


def test_length_boundary_254_is_accepted():
    local = "a" * 242
    assert len(local + "@example.com") == 254
    assert is_valid_email(local + "@example.com") is True


def test_length_over_254_is_rejected():
    local = "a" * 243
    address = local + "@example.com"
    assert len(address) == 255
    assert is_valid_email(address) is False


@pytest.mark.parametrize(
    "value", [123, 3.14, None, b"user@example.com", ["user@example.com"], True]
)
def test_non_string_raises_type_error(value):
    with pytest.raises(TypeError):
        is_valid_email(value)


def test_type_error_message_never_contains_the_value():
    with pytest.raises(TypeError) as exc_info:
        is_valid_email(123)
    assert "123" not in str(exc_info.value)


def test_regex_has_no_nested_quantifiers():
    from validkit.email import _EMAIL_RE

    pattern = _EMAIL_RE.pattern
    nested = re.compile(r"\([^)]*[+*{][^)]*[+*{][^)]*\)")
    assert nested.search(pattern) is None
