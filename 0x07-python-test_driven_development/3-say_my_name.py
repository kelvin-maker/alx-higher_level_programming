#!/usr/bin/python3
"""Provides a function 'say_my_name' that prints your name"""


def say_my_name(first_name, last_name=""):
    """Print someone's name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
                                    
