#!/usr/bin/python3
"""Provides a function 'matrix_divided' that divides a matrix by a number"""


def matrix_divided(matrix, div):
        """Divide each element of a matrix by a number"""
        if not (matrix and
                isinstance(matrix, list) and
                all(isinstance(row, list) and
                    all(isinstance(item, (float, int))
                        for item in row) for row in matrix)):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                                    )
        if not all(len(a) == len(b) for a, b in zip(matrix, matrix[1:])):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (float, int)):
            raise TypeError("div must be a number")
        try:

            return [[round(n / div, 2) for n in row] for row in matrix]
        except ZeroDivisionError:
            raise ZeroDivisionError("division by zero")
        
