"""
Utilities for basic ciphers and encoding methods.
"""

import string


def shift_cipher(text: str, shift: int) -> str:
    """Applies a rotational shift to each letter in the text.

    Parameters
    ----------
    text : str
        The input string to be shifted
    shift : int
        The number of positions to shift each character

    Returns
    -------
    str
        The text with the specified shift applied
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift % 26:] + alphabet[:shift % 26]

    table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(table)


def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """Encrypts or decrypts text using the Caesar cipher method.

    Parameters
    ----------
    text : str
        The input string to process
    shift : int
        The shift amount (key) for the cipher
    decrypt : bool, optional
        If True, reverses the shift to decrypt the text, by default False

    Returns
    -------
    str
        The processed string
    """
    if decrypt:
        shift = -shift
    return shift_cipher(text, shift)


def rot13(text: str) -> str:
    """Applies the ROT13 cipher (shift of 13) to the text.

    Parameters
    ----------
    text : str
        The input string to process

    Returns
    -------
    str
        The text with the ROT13 transformation applied
    """
    return shift_cipher(text, 13)


def atbash_cipher(text: str) -> str:
    """Encrypts or decrypts text using the Atbash substitution cipher.

    Parameters
    ----------
    text : str
        The input string to process

    Returns
    -------
    str
        The text with the Atbash cipher applied
    """
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]

    table = str.maketrans(
        alphabet + alphabet.upper(),
        reversed_alphabet + reversed_alphabet.upper()
    )

    return text.translate(table)


def reverse_cipher(text: str) -> str:
    """Reverses the order of characters in the string.

    Parameters
    ----------
    text : str
        The input string to reverse

    Returns
    -------
    str
        The reversed string
    """
    return text[::-1]


def a1z26_cipher(text: str) -> str:
    """Converts letters to their numeric positions in the alphabet (A=1, Z=26).

    Parameters
    ----------
    text : str
        The input string to encode

    Returns
    -------
    str
        The numeric representation of the text
    """
    results = []
    for char in text.upper():
        if char.isalpha():
            results.append(str(ord(char) - 64))
        elif char.isspace():
            results.append(" ")
        else:
            results.append(char)

    final_output = ""
    for i in range(len(results)):
        final_output += results[i]
        if i < len(results) - 1:
            if results[i].isdigit() and results[i+1].isdigit():
                final_output += "-"
    return final_output


def bacon_cipher(text: str) -> str:
    """Encodes text using the Baconian cipher (5-bit binary substitution).

    Parameters
    ----------
    text : str
        The input string to encode

    Returns
    -------
    str
        The Baconian encoded string
    """
    BACON_DICT = {
        'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
        'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaaa',
        'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
        'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
        'U': 'baabb', 'V': 'baabb', 'W': 'babaa', 'X': 'babab', 'Y': 'babba',
        'Z': 'babbb'
    }
    return "".join(BACON_DICT.get(char.upper(), "") if char.isalpha() else char for char in text)


def substitution_cipher(text: str, alphabet_key: str) -> str:
    """Encrypts text using a custom 26-character substitution key.

    Parameters
    ----------
    text : str
        The input string to encrypt
    alphabet_key : str
        A 26-character string representing the mapping of the alphabet

    Returns
    -------
    str
        The encrypted text

    Raises
    ------
    ValueError
        If the alphabet_key is not exactly 26 characters long
    """
    if len(alphabet_key) != 26:
        raise ValueError("alphabet_key variable must be exactly 26 characters long.")
    full_key = alphabet_key.lower() + alphabet_key.upper()
    table = str.maketrans(
        string.ascii_letters,
        full_key
    )
    return text.translate(table)


def rail_fence_2_cipher(text: str) -> str:
    """Applies a 2-rail fence (zigzag) transposition cipher.

    Parameters
    ----------
    text : str
        The input string to process

    Returns
    -------
    str
        The transposed string
    """
    evens = text[::2]
    odds = text[1::2]
    return evens + odds


def eng_to_morse(text: str) -> str:
    """Converts English text to International Morse Code.

    Parameters
    ----------
    text : str
        The input string to encode

    Returns
    -------
    str
        The Morse code representation
    """
    MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..',
        "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
        '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    return " ".join(MORSE_DICT[char] for char in text.upper() if char in MORSE_DICT)


def morse_to_eng(text: str) -> str:
    """Converts International Morse Code back to English text.

    Parameters
    ----------
    text : str
        The Morse code string to decode

    Returns
    -------
    str
        The decoded English text
    """
    MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..',
        "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
        '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    REVERSE_DICT = {v: k for k, v in MORSE_DICT.items()}
    return "".join(REVERSE_DICT[code] for code in text.split(" ") if code in REVERSE_DICT)


def eng_to_imct(text: str) -> str:
    """Converts English text to International Morse Code Timing (IMCT) binary.

    Parameters
    ----------
    text : str
        The input string to encode

    Returns
    -------
    str
        A binary string representing Morse code timings
    """
    morse_text = eng_to_morse(text)
    parts = []
    for word in morse_text.split(' / '):
        word_parts = []
        for letter in word.split(' '):
            pulses = '0'.join(['111' if symbol == '-' else '1' for symbol in letter])
            word_parts.append(pulses)
        parts.append('000'.join(word_parts))
    return '0000000'.join(parts)
