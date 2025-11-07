import pytest

def test_addition():
    assert 5 + (-3) == 2
def test_division():
    with pytest.raises(ZeroDivisionError):
        _ = 10 / 0
def test_multiplication():
    assert round(2.5 * 4.2, 2) == 10.5
def test_power():
    assert 2 ** 3 == 8