#!/usr/bin/python3
""" Provides a (mostly empty) base class for geometric objects
"""


class BaseGeometry:
    """ Implement a base class for geometric objects
    """
    def area(self):
        """ Calculate the area of a geometric object
        """
        raise Exception("area() is not implemented")
    
