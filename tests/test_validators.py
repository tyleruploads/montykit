import pytest
from montykit.validators import json_validator, is_email, is_strong_pass


@pytest.mark.parametrize("data, expected", [
    ('{"name": "Alice", "age": 30}', True),
    ('["item1", "item2"]', True),
    ('invalid string', False),
    ('{name: "Alice"}', False),
    ('', False),
])
def test_json_validator(data, expected):
    assert json_validator(data) == expected


@pytest.mark.parametrize("email, expected", [
    ("tyleruploads@yahoo.com", True),
    ("tyleruploadspython@gmail.com", True),
    ("no", False),
    ("tyleruploads@yahoo.com", True),
    ("https://github.com/tyleruploads/montykit", False),
    ("https://github.com/tyleruploads/tylereq", False),
    ("@icloud.com", False),
    ("tyler@.com", False),
])
def test_is_email(email, expected):
    assert is_email(email) == expected


@pytest.mark.parametrize("password, expected", [
    ("Str0ng!Pass2026", True),
    ("short1!", False),
    ("NOSPECIALCHARS123", False),
    ("onlylowercase!!!", False),
    ("NoDigits!", False),
])
def test_is_strong_pass(password, expected):
    assert is_strong_pass(password) == expected
