import pytest
from montykit.analysis import (
    text_polarity,
    word_freq,
    text_difficulty,
    text_is_difficult
)


@pytest.mark.parametrize("text, expected_range", [
    ("I love this! It is wonderful and happy.", (0.1, 1.0)),
    ("I hate this. It is terrible and sad.", (-1.0, -0.1)),
    ("The chair is brown.", (-0.1, 0.1)),
])
def test_text_polarity(text, expected_range):
    low, high = expected_range
    assert low <= text_polarity(text) <= high


def test_word_freq():
    text = "Apple apple Banana"
    result = word_freq(text)
    assert result["apple"] == 2
    assert result["banana"] == 1
    assert "Apple" not in result


def test_text_difficulty_structure():
    text = "The quick brown fox jumps over the lazy dog."
    metrics = text_difficulty(text)

    expected_keys = [
        "flesch_reading_ease",
        "flesch_kincaid_grade",
        "gunning_fog",
        "smog_index",
        "automated_readability_index",
        "consensus_grade"
    ]
    for key in expected_keys:
        assert key in metrics


@pytest.mark.parametrize("text, expected_bool", [
    ("This is a simple sentence.", False),
    ("The ontological ramifications of existentialism are inherently multifaceted.", True),
])
def test_text_is_difficult(text, expected_bool):
    assert text_is_difficult(text) == expected_bool