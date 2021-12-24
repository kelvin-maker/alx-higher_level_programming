#!/usr/bin/python3
"""Provides a base class for all other classes in this module
"""

class Base():
    """Base class for all other classes in this module
    """
    HEADERS = ('id',)

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a base object
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id
            
