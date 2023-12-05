#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file
    
    Args:
        filename (str): name of the file to write
        text (str): text to write to the file

    Returns:
        number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as txt:
        return txt.write(text)
