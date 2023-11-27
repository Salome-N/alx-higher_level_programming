#!/usr/bin/python3

"""Rectangle class module."""

class Rectangle:

    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrive width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle.
        
        Args:
            value (int): width of rectangle.

        Returns:
            None.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrive height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle.

        Args:
            value (int): height of rectangle.

        Returns:
            None.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """Area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of rectangle."""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (self.__width + self.__height) * 2
