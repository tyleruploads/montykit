"""
Utilities for basic conversions
"""

import base64
from urllib.parse import quote, unquote
import re


def base64_encode(text: str) -> str:
    """Encodes a string into Base64 format.

    Parameters
    ----------
    text : str
        The plain text to encode

    Returns
    -------
    str
        The Base64 encoded string
    """
    return base64.b64encode(text.encode()).decode()


def base64_decode(text: str) -> str:
    """Decodes a Base64 string back to plain text.

    Parameters
    ----------
    text : str
        The Base64 string to decode

    Returns
    -------
    str
        The decoded plain text, or None if decoding fails
    """
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        print(f"Most likely invalid base64, error: {e}")
        return None


def text_to_binary(text: str) -> str:
    """Converts a string of text into its binary representation.

    Parameters
    ----------
    text : str
        The text to convert

    Returns
    -------
    str
        A string of 8-bit binary values separated by spaces
    """
    return ' '.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary: str) -> str:
    """Converts a string of binary values back into plain text.

    Parameters
    ----------
    binary : str
        A string of space-separated binary values

    Returns
    -------
    str
        The converted plain text, or None if conversion fails
    """
    try:
        binary_values = binary.split(' ')
        return ''.join(chr(int(bv, 2)) for bv in binary_values)
    except Exception as e:
        print(f"Most likely invalid binary, error: {e}")
        return None


def text_to_hex(text: str) -> str:
    """Converts a string of text into its hexadecimal representation.

    Parameters
    ----------
    text : str
        The text to convert

    Returns
    -------
    str
        A string of hex values separated by spaces
    """
    return text.encode().hex(' ')


def hex_to_text(hex_string: str) -> str:
    """Converts a string of hexadecimal values back into plain text.

    Parameters
    ----------
    hex_string : str
        A string of hex values

    Returns
    -------
    str
        The decoded plain text
    """
    return bytes.fromhex(hex_string).decode()


def text_to_url(text: str) -> str:
    """URL-encodes a string for use in a web address.

    Parameters
    ----------
    text : str
        The plain text to encode

    Returns
    -------
    str
        The URL-encoded string
    """
    return quote(text)


def url_to_text(url: str) -> str:
    """Decodes a URL-encoded string back to plain text.

    Parameters
    ----------
    url : str
        The URL-encoded string to decode

    Returns
    -------
    str
        The decoded plain text
    """
    return unquote(url)


def to_snake_case(text: str) -> str:
    """Converts a string (e.g., CamelCase) to snake_case.

    Parameters
    ----------
    text : str
        The string to convert

    Returns
    -------
    str
        The converted snake_case string
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(text: str) -> str:
    """Converts a string (e.g., snake_case) to camelCase.

    Parameters
    ----------
    text : str
        The string to convert

    Returns
    -------
    str
        The converted camelCase string
    """
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
