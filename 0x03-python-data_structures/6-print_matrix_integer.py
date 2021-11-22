#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    print('\n'.join([' '.join(['{:d}'.format(x) for x in y]) for y in matrix]))
    
