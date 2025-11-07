import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        open("nonexistent.txt")
def test_invalid_conversion():
    with pytest.raises(ValueError):
        int("abc")
class CustomError(Exception):
    pass
def test_custom_exception():
    with pytest.raises(CustomError, match="Custom error occurred"):
        raise CustomError("Custom error occurred")