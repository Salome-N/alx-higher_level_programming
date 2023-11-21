#!/usr/bin/python3

"""Size validation."""

class Square:
    """Class Square."""

    def __init__(self, size=0):
        """Initialize class.
        
            Args:
                size (int): size of the square.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
