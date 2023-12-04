#!/usr/bin/python3
"""Defines functio that adds new attribute"""


def add_attribute(obj, att, value):
    """Adds new attribute to obj

    Args:
        obj (any): object to add new attribute
        att (str): name of attribute to be added
        value (any): value of att

    Raises:
        TypeError: if attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
