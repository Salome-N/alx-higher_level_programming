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
        self.size = size

    @property
    def size(self):
        """Get size of square

            Args:
                None

            Returns:
                Size

        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size of square
            
            Args:
                value (int): size of square

            Returns:
                Size

            Raises:
                TypeError: size must be an integer.
                ValueError: size must be >= 0.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area of square.

            Args:
                None

            Returns:
                Area of square

        """

        return (self.__size ** 2)

    def my_print(self):
        """Printing a square

            Args:
                None

            Returns:
                None

        """

        if self.__size == 0:
            print()
        else:
            for r in range(self.__size):
                for c in range(self.__size):
                    print("#", end="")
                print()
