#!/usr/bin/python3
""" Check if a an object is in a certain class
"""


def inherits_from(obj, a_class):
    """ Check if obj is an instance of a subclass of a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
