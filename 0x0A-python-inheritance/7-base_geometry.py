#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Raises an 'area' exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as an int

        Args:
            name (str): name of parameter
            value (int): parameter to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
