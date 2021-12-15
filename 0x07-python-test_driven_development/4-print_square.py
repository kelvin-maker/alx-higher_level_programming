#!/usr/bin/python3
"""Provides a function 'print_square' that prints a square"""


def print_square(size):
        """Print a square of the specified dimensions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if size > 0:
            print(*(['#' * size] * size), sep='\n')
            
