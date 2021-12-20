#!/usr/bin/python3
""" Check if a an object is in a certain class
"""


def is_kind_of_class(obj, a_class):
    """ Check if obj's type is either a_class or a subclass of a_class
    """
    return isinstance(obj, a_class)
