import pytest
from fuel import convert, gauge


def test_convert_correct_fraction():
    assert convert("1/2") == 50


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("2/1")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
