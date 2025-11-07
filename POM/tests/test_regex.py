import re

def test_email_regex():
    assert re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", "test@example.com")
def test_phone_regex():
    assert re.match(r"^\+?\d{10,13}$", "+12345678901")
def test_password_strength():
    assert re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", "StrongPass1")
def test_url_validation():
    assert re.match(r"^https?://[\w\.-]+$", "https://example.com")
