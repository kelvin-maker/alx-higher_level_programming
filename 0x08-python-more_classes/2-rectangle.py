#!/usr/bin/python3
""" Provides a class 'Rectangle' to represent a rectangle
"""


class Rectangle():

    """ definition of the rectangle class
    """

    def __init__ (self, width = 0, height=0):
        """instantiate the rectangle
        """

        self.height = height
        self.width = width

    def width(self):
        """ Get triangle width
        """
        return self.__width

    def width(self, value):
        """Set the rectangles' width
        """
        if not isinstance(value, int):
           """checks if value is not an integer using is isinstance()
           """
           raise TypeError("width must be an integer")
        if value <0:
           raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        """Get the height of a rectangle
        """
        return self.__height


    def height(self, value):
        """set the height of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self._height = value

    def area(self):
        """ returns the area 
        """
        return self.height * self.width
    def perimeter(self):
        """Perimeter of rectangle
        """

        return (self.height * 2) + (self.width * 2)
