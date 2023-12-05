#!/usr/bin/python3
"""Define a function that reads a text file"""


def read_file(filename=""):
    """Prints file contents to stdout"""
    with open(filename, encoding="utf-8") as txt:
        print(txt.read(), end="")
