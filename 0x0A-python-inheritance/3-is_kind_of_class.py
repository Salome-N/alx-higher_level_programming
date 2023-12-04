#!/usr/bin/python3

"""Defines a check class function"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited instance of a class

    Args:
        obj (any): obj to be checked
        a_class (type): class to be check the obj type

    Returns:
        if obj is an instance or inherited instance of a class - True
        else - False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
