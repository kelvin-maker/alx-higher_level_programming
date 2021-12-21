#!/usr/bin/python3
"""Provides a function to append text to a file"""


def append_write(filename="", text=""):
    """Append text to a file"""
    with open(filename, 'a') as ostream:
        return ostream.write(text)
    
