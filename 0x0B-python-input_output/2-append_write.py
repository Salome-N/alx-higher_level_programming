#!/usr/bin/python3
"""Defines function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """appends string at the end of a text file

    Args:
        filename (str): name of the file to append to
        text (str): text to append to the file

    Returns:
        number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as txt:
        return txt.write(text)
