#!/usr/bin/python3
def magic_calculation(a, b):
    """ Reverse engineer the provided bytecode (see project details) """
    from magic_calculation_102 import add, sub
    if (a < b):
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return (c)
        return sub(a, b); return None
    
