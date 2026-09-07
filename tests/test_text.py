"""Unit-Tests für validkit.text."""

import pytest

from validkit.text import mask_secret, slugify, strip_accents


def test_strip_accents_removes_diacritics():
    assert strip_accents("café") == "cafe"
    assert strip_accents("Héllo Wörld") == "Hello World"


def test_strip_accents_handles_empty_string():
    assert strip_accents("") == ""


def test_strip_accents_leaves_ascii_unchanged():
    assert strip_accents("plain text") == "plain text"


def test_strip_accents_handles_multiple_diacritics():
    assert strip_accents("àèìòù") == "aeiou"


def test_strip_accents_rejects_non_string():
    with pytest.raises(TypeError):
        strip_accents(123)


def test_slugify_lowercases_and_replaces_specials():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_collapses_consecutive_separators():
    assert slugify("a   b") == "a-b"


def test_slugify_strips_leading_and_trailing_separators():
    assert slugify("  hello  ") == "hello"


def test_slugify_handles_empty_string():
    assert slugify("") == ""


def test_slugify_rejects_non_string():
    with pytest.raises(TypeError):
        slugify(None)


def test_mask_secret_masks_all_but_last_keep():
    assert mask_secret("geheim", 2) == "****im"


def test_mask_secret_defaults_to_four():
    assert mask_secret("geheimnis") == "*****mnis"


def test_mask_secret_returns_unchanged_when_keep_exceeds_length():
    assert mask_secret("abc", 5) == "abc"


def test_mask_secret_returns_unchanged_when_keep_equals_length():
    assert mask_secret("abc", 3) == "abc"


def test_mask_secret_zero_keep_masks_everything():
    assert mask_secret("abc", 0) == "***"


def test_mask_secret_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("abc", -1)


def test_mask_secret_rejects_non_string():
    with pytest.raises(TypeError):
        mask_secret(123, 2)


def test_mask_secret_rejects_non_integer_keep():
    with pytest.raises(TypeError):
        mask_secret("abc", "2")
