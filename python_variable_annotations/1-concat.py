#!/usr/bin/env python3
"""function to conctenate two strings"""


def concat(str1: str, str2: str) -> str:
    """concatenate two strings together

    Args:
        str1 (str): The fisrst string.
        str2 (str): The second string.

    Returns:
        str: A string that containing str1 followed by str2.
    """
    return "{}{}".format(str1, str2)
