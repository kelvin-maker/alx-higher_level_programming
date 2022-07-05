#!/usr/bin/python3
"""Provides a function to read and print a file"""
def read_file(filename=""):
    """Print the contents of a file"""
    with open(filename, "r") as istream:
        print(istream.read(), end="")
    
