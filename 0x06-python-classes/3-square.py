#!/usr/bin/python3

"""Area of a square"""

class Square:
    """Class square"""

    def __init__(self, size=0):
        """Initialize class

            Args:
                size (int): size of square

            Returns:
                None

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of square.

            Args:
                None

            Returns:
                Area of square

        """

        return (self.__size ** 2)
