#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if my_list:
        print('\n'.join(['{:d}'.format(n) for n in my_list]))
