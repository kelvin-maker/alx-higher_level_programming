#!/usr/bin/python3
"""Provides a function to write text to a file"""


def write_file(filename="", text=""):
    """Write text to a file"""
    with open(filename, 'w') as ostream:
        return ostream.write(text)
    
