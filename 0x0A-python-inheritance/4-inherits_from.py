#!/usr/bin/python3
"""Defines a check class function"""


def inherits_from(obj, a_class):
    """Checks if the obj is an instance of a class that inherited
    (directly or indirectly)

    Args:
        obj (any): obj to be checked
        a_class (type): class to check the obj type

    Returns:
        if the obj is an instance of a class that inherited - True
        else - False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
