import pytest
from montykit.ciphers import (
    shift_cipher,
    caesar_cipher,
    rot13,
    atbash_cipher,
    reverse_cipher,
    morse_to_eng,
    eng_to_morse
)


@pytest.mark.parametrize("text, shift, expected", [
    ("abc", 1, "bcd"),
    ("XYZ", 3, "ABC"),
    ("Hello, World!", 5, "Mjqqt, Btwqi!"),
    ("abc", 27, "bcd"),
])
def test_shift_cipher(text, shift, expected):
    assert shift_cipher(text, shift) == expected


def test_caesar_round_trip():
    original = "Secret Message 123!"
    encrypted = caesar_cipher(original, 10)
    decrypted = caesar_cipher(encrypted, 10, decrypt=True)
    assert original == decrypted


def test_rot13():
    text = "Pytest is Cool"
    assert rot13(rot13(text)) == text


@pytest.mark.parametrize("text, expected", [
    ("abc", "zyx"),
    ("ABC", "ZYX"),
    ("Hello!", "Svool!"),
])
def test_atbash_cipher(text, expected):
    assert atbash_cipher(text) == expected


def test_reverse_cipher():
    text = "Python"
    assert reverse_cipher(text) == "nohtyP"
    assert reverse_cipher(reverse_cipher(text)) == text


def test_morse_encryption():
    assert eng_to_morse("SOS") == "... --- ..."


def test_morse_decryption():
    assert morse_to_eng("... --- ...") == "SOS"


def test_morse_round_trip():
    original = "HELLO 2026"
    encoded = eng_to_morse(original)
    decoded = morse_to_eng(encoded)
    assert decoded == original
