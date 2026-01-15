"""
Utilities for basic hashing
"""

import hashlib


def generate_hash(text: str, algorithm: str = "sha256") -> str:
    """Generates a hexadecimal hash of the input text using the specified algorithm.

    Parameters
    ----------
    text : str
        The input string to be hashed
    algorithm : str, optional
        The hashing algorithm to use (e.g., 'md5', 'sha1', 'sha256'), 
        by default "sha256"

    Returns
    -------
    str
        The resulting hexadecimal hash string

    Raises
    ------
    ValueError
        If the specified algorithm is not supported by the system's 
        hashlib implementation
    """
    algo = algorithm.lower()
    if algo in hashlib.algorithms_available:
        return hashlib.new(algo, text.encode()).hexdigest()

    raise ValueError(f"Algorithm {algorithm} is not supported.")