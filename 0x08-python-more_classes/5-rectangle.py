#!/usr/bin/python3
""" Provides a class 'Rectangle' to represent a rectangle
"""


class Rectangle():
    """ Definition of a class to represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle
        """
        self.height = height
        self.width = width

    def __del__(self):
        """deletes rectangle 
        """
        print("Bye rectangle ...")
    def __str__(self):
        """ Represent a rectangle as a string
        """
        if self.height and self.width:
            return '\n'.join(['#' * self.width] * self.height)
        return ''
    def __repr__(self):
        """ Represent a rectangle in a form that may be reused as input
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)
    def width(self):
        """ Get the width of a rectangle
        """
        return self.__width
    def width(self, value):
        """ Set the width of a rectangle
                """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def height(self):
        """ Get the height of a rectangle
                        """
        return self.__height
    def height(self, value):
        """ Set the height of a rectangle
                                """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """ Get the area of a rectangle
                                        """
        return self.width * self.height

    def perimeter(self):
        """ Get the perimeter of a rectangle
                                                """
        if self.width and self.height:
            return 2 * (self.width + self.height)
        return 0
    
