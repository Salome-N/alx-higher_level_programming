#!/usr/bin/python3
"""Defines a subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize square

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area of square"""
        return (self.__size ** 2)
