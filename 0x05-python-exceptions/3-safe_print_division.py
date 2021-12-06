#!/usr/bin/python3
def safe_print_division(a, b):
    """ Divide two integers and print the result
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        try:
            print("Inside result: {}".format(result))
        except NameError:
            pass
    return result
