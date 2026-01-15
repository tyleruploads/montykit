import pytest
from montykit.converters import (
    base64_encode,
    base64_decode,
    text_to_binary,
    binary_to_text,
    text_to_hex,
    hex_to_text,
    text_to_url,
    url_to_text,
    to_snake_case,
    to_camel_case
)


@pytest.mark.parametrize("text,expected_b64", [
    ("hello", "aGVsbG8="),
    ("12345", "MTIzNDU="),
    ("", ""),
])
def test_base64_encoding(text, expected_b64):
    assert base64_encode(text) == expected_b64
    assert base64_decode(expected_b64) == text


def test_binary_round_trip():
    original = "Python 2026"
    binary = text_to_binary(original)
    assert binary_to_text(binary) == original


def test_hex_round_trip():
    original = "Test String"
    hex_val = text_to_hex(original)
    assert hex_to_text(hex_val) == original


@pytest.mark.parametrize("text,expected_url", [
    ("hello world", "hello%20world"),
    ("user@domain.com", "user%40domain.com"),
])
def test_url_conversion(text, expected_url):
    assert text_to_url(text) == expected_url
    assert url_to_text(expected_url) == text


@pytest.mark.parametrize("input_str,expected_snake", [
    ("CamelCase", "camel_case"),
    ("already_snake", "already_snake"),
    ("Simple", "simple"),
    ("HTTPResponse", "http_response"),
])
def test_to_snake_case(input_str, expected_snake):
    assert to_snake_case(input_str) == expected_snake


@pytest.mark.parametrize("input_str,expected_camel", [
    ("snake_case_text", "snakeCaseText"),
    ("simple", "simple"),
    ("test_case", "testCase"),
])
def test_to_camel_case(input_str, expected_camel):
    assert to_camel_case(input_str) == expected_camel
