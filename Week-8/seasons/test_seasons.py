from seasons import minutes
import pytest


def test_known_past_date():
    result = minutes("2000-01-01")
    assert isinstance(result, str)
    assert "minutes" in result


def test_capitalization():
    result = minutes("1998-12-25")
    assert result[0].isupper()


def test_invalid_format_raises_exit():
    with pytest.raises(SystemExit):
        minutes("not-a-real-date")


def test_invalid_date_values_raises_exit():
    with pytest.raises(SystemExit):
        minutes("2023-13-45")
