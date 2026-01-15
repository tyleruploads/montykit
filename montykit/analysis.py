"""
Utilities for basic text analysis.
"""

from collections import Counter
import re
from textblob import TextBlob
import textstat


def text_polarity(text: str) -> float:
    """Tests how positive or negative the text is.

    Parameters
    ----------
    text : str
        The text to test the polarity of

    Returns
    -------
    float
        The polarity score ranging from -1.0 (negative) to 1.0 (positive)
    """
    return TextBlob(text).sentiment.polarity


def text_subjectivity(text: str) -> float:
    """Tests how subjective the text is.

    Parameters
    ----------
    text : str
        The text to test the subjectivity of

    Returns
    -------
    float
        The subjectivity score ranging from 0.0 (objective) to 1.0 (subjective)
    """
    return TextBlob(text).sentiment.subjectivity


def word_freq(text: str) -> dict:
    """Makes a dictionary of words and their frequency in the text.

    Parameters
    ----------
    text : str
        The text to analyze

    Returns
    -------
    dict
        Example: {"happy": 10, "sad": 2, "sleep": 1}
    """
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    return dict(Counter(clean_text.split()))


def detect_lang(text: str) -> str:
    """Detects the language of the text.

    Parameters
    ----------
    text : str
        The text to check the language of

    Returns
    -------
    str
        The detected ISO 639-1 language code (e.g., 'en')
    """
    return TextBlob(text).detect_language()


def text_difficulty(text: str) -> dict:
    """Determines the difficulty of text using multiple readability metrics.

    Parameters
    ----------
    text : str
        The text to analyze the difficulty of

    Returns
    -------
    dict
        A dictionary mapping various readability metrics to their values
    """
    return {
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
        "gunning_fog": textstat.gunning_fog(text),
        "smog_index": textstat.smog_index(text),
        "automated_readability_index": textstat.automated_readability_index(text),
        "consensus_grade": textstat.text_standard(text)
    }


def text_is_difficult(text: str) -> bool:
    """Determines if text has a grade level of 13 or over.

    Parameters
    ----------
    text : str
        The text to evaluate against the 13th-grade threshold

    Returns
    -------
    bool
        True if the Flesch-Kincaid grade is 13 or higher, False otherwise
    """
    return textstat.flesch_kincaid_grade(text) >= 13
