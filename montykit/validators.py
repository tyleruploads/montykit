"""
Utilities for basic validation
"""

import json
import re


def json_validator(data: str) -> bool:
    """Checks if a string is a valid JSON format.

    Parameters
    ----------
    data : str
        The string to be validated as JSON

    Returns
    -------
    bool
        True if the string is valid JSON, False otherwise
    """
    try:
        json.loads(data)
        return True
    except (ValueError, TypeError):
        return False


def is_email(email: str) -> bool:
    """Validates an email address using a standard regex pattern.

    Parameters
    ----------
    email : str
        The email address string to validate

    Returns
    -------
    bool
        True if the email matches the standard format, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_strong_pass(password: str) -> bool:
    """Checks if a password meets specific strength requirements.

    Requirements:
    - Minimum length of 12 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character

    Parameters
    ----------
    password : str
        The password string to evaluate

    Returns
    -------
    bool
        True if the password meets all complexity requirements, False otherwise
    """
    if len(password) < 12:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return all([has_upper, has_lower, has_digit, has_special])