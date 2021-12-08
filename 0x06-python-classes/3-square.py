#!/usr/bin/python3
""" Module providing a definition of a class 'Square'
"""


class Square():
    """ Definition of a 'Square'
    """
    def __init__(self, size=0):
        """ Instantiate a 'Square'
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Compute the area of a 'Square'
        """
        return self.__size ** 2
    
