#!/usr/bin/python3


def print_last_digit(number):
        """
    Prints and returns the last digit of a number.
    If given something that's not a number, this returns None.
    """
    number = (abs(number) % 10)
    print("{}".format(number), end="")
    return (int(number))
                
