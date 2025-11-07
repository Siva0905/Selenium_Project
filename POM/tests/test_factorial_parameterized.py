
import pytest
from calculator import Calculator
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '....')))
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120),
    (7, 5040)
])
def test_factorial(n, expected):
    calc = Calculator()
    result = calc.factorial(n)
    print("From factorial program:")
    assert result == expected