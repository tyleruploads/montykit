"""
Utilities for basic data/text generation
"""

import string
import secrets
import uuid
import json
from importlib import resources


with resources.open_text("montykit", "girl_boy_names.json") as f:
    _FIRST_NAMES = json.load(f)


with resources.open_text("montykit", "middle_names.json") as f:
    _MIDDLE_NAMES = json.load(f)


with resources.open_text("montykit", "last_names.json") as f:
    _LAST_NAMES = json.load(f)


def gen_id(length: int = 12) -> str:
    """Generates a random numerical ID string.

    Parameters
    ----------
    length : int, optional
        The number of digits in the ID, by default 12

    Returns
    -------
    str
        A string of random digits
    """
    return "".join(secrets.choice(string.digits) for _ in range(length))


def gen_uuid() -> str:
    """Generates a random UUID (version 4).

    Returns
    -------
    str
        A string representation of a unique UUID
    """
    return str(uuid.uuid4())


def gen_password(length: int = 12) -> str:
    """Generates a strong random password with mixed characters.

    Parameters
    ----------
    length : int, optional
        The length of the password, by default 12

    Returns
    -------
    str
        A random password containing digits, letters, and punctuation
    """
    chars = string.digits + string.ascii_letters + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


def gen_first_name() -> str:
    """Selects a random first name from the loaded resources.

    Returns
    -------
    str
        A random first name
    """
    return secrets.choice(_FIRST_NAMES[secrets.choice(["girls", "boys"])])


def gen_first_names(amount: int) -> list[str]:
    """Generates a list of random first names.

    Parameters
    ----------
    amount : int
        The number of names to generate

    Returns
    -------
    list of str
        A list containing the requested number of first names
    """
    return [gen_first_name() for _ in range(amount)]


def gen_middle_name() -> str:
    """Selects a random middle name from the loaded resources.

    Returns
    -------
    str
        A random middle name
    """
    return secrets.choice(_MIDDLE_NAMES[secrets.choice(["girls", "boys"])])


def gen_middle_names(amount: int) -> list[str]:
    """Generates a list of random middle names.

    Parameters
    ----------
    amount : int
        The number of names to generate

    Returns
    -------
    list of str
        A list containing the requested number of middle names
    """
    return [gen_middle_name() for _ in range(amount)]


def gen_last_name() -> str:
    """Selects a random last name from the loaded resources.

    Returns
    -------
    str
        A random last name
    """
    return secrets.choice(_LAST_NAMES[secrets.choice(["girls", "boys"])])


def gen_last_names(amount: int) -> list[str]:
    """Generates a list of random last names.

    Parameters
    ----------
    amount : int
        The number of names to generate

    Returns
    -------
    list of str
        A list containing the requested number of last names
    """
    return [gen_last_name() for _ in range(amount)]


def gen_full_name(middle: bool = False) -> str:
    """Generates a random full name.

    Parameters
    ----------
    middle : bool, optional
        Whether to include a middle name, by default False

    Returns
    -------
    str
        A formatted string containing a first, optional middle, and last name
    """
    gender = secrets.choice(["girls", "boys"])
    first = secrets.choice(_FIRST_NAMES[gender])
    last = secrets.choice(_LAST_NAMES)
    if middle:
        mid = secrets.choice(_MIDDLE_NAMES)
        return f"{first} {mid} {last}"
    return f"{first} {last}"


def gen_full_names(middle: bool = False, amount: int = 10) -> list[str]:
    """Generates a list of random full names.

    Parameters
    ----------
    middle : bool, optional
        Whether to include middle names, by default False
    amount : int, optional
        The number of names to generate, by default 10

    Returns
    -------
    list of str
        A list of random full name strings
    """
    return [gen_full_name(middle) for _ in range(amount)]


def gen_phone() -> str:
    """Generates a random phone number in XXXXXXXXXX format.

    Returns
    -------
    str
        A formatted random phone number string
    """
    return "".join(secrets.choice(string.digits) for _ in range(10))
