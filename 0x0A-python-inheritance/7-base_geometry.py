#!/usr/bin/python3
""" Provides a base class for geometric objects
"""


class BaseGeometry:
    """ Definition of a base class for geometric objects
    """
    def area(self):
        """ Calculate the area of a geometric object
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Verify that a value is a positive integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
        
