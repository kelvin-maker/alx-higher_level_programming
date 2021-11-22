#!/usr/bin/python3


def no_c(my_string):
    if my_string is not None:
        return ''.join(filter(lambda c: c.lower() != 'c', my_string))
    return None
