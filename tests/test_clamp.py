"""Unit-Tests für validkit.clamp.clamp."""

import pytest

from validkit.clamp import clamp


def test_value_within_interval_returns_unchanged():
    assert clamp(5, 0, 10) == 5


def test_value_below_interval_returns_low():
    assert clamp(-5, 0, 10) == 0


def test_value_above_interval_returns_high():
    assert clamp(15, 0, 10) == 10


def test_value_exactly_on_low():
    assert clamp(0, 0, 10) == 0


def test_value_exactly_on_high():
    assert clamp(10, 0, 10) == 10


def test_float_values():
    assert clamp(3.5, 0.0, 10.0) == 3.5
    assert clamp(-1.5, 0.0, 10.0) == 0.0
    assert clamp(12.75, 0.0, 10.0) == 10.0


def test_negative_bounds():
    assert clamp(-3, -10, -1) == -3
    assert clamp(-20, -10, -1) == -10
    assert clamp(0, -10, -1) == -1


def test_low_equal_high_returns_that_value():
    assert clamp(5, 5, 5) == 5
    assert clamp(0, 5, 5) == 5
    assert clamp(7, 5, 5) == 5


def test_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_error_message_does_not_contain_input():
    with pytest.raises(ValueError) as exc_info:
        clamp(1, 10, 0)
    message = str(exc_info.value)
    assert "1" not in message
    assert "10" not in message
    assert "0" not in message
