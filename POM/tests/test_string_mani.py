def test_string_title():
    assert "Domain" in "Example Domain"
def test_string_presence():
    assert "illustrative" in "This domain is for use in illustrative examples."
def test_string_length():
    assert len("example") <= 10
def test_case_sensitivity():
    assert "Example" != "example"