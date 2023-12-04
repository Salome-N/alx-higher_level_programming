#!/usr/bin/python3

"""Defines a check class function"""


def is_same_class(obj, a_class):
    """ Checks if an object is exactly an instance of the specified class
    Args:
        odj (any): the object to be checked
        a_class (type): class to match the obj type

    Returns:
        if obj is exactly an instance of specified class - True
        else - False
    """

    if type(obj) == a_class:
        return True
    else:
        return False
