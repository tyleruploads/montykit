import pytest
import hashlib
from montykit.hash import generate_hash


def test_generate_hash_default():
    input_text = "This is a unit test!"
    expected = hashlib.sha256(input_text.encode()).hexdigest()
    assert generate_hash(input_text) == expected


@pytest.mark.parametrize("algo, text, expected", [
    ("md5", "hello", "5d41402abc4b2a76b9719d911017c592"),
    ("sha1", "hello", "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"),
])
def test_generate_hash_algorithms(algo, text, expected):
    assert generate_hash(text, algorithm=algo) == expected


def test_generate_hash_invalid():
    with pytest.raises(ValueError, match="Algorithm invalid_algo is not supported."):
        generate_hash("This should NOT WORK!", algorithm="invalid_algo")
