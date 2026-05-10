from convert import convert
import pytest

def test_int_conversions():
    assert convert(1) == 149597870700

def test_float_conversions():
    assert convert(0.01) == pytest.approx(1495978707.001, abs=1e-1)

def test_errors():
    with pytest.raises(TypeError):
        convert('1')