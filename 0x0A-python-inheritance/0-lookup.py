#!/usr/bin/python3
"""Define the lookup function"""


def lookup(obj):
    """Return list of available attributes and methods of an object.

    Args:
        obj (object): an object
    """

    return dir(obj)
