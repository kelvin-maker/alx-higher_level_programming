#!/usr/bin/python3
""" Provides a class to represent rectangles
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Definition of fixed-size rectangle
    """
    def __init__(self, width, height):
        """ Instantiate a rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
                                                         
