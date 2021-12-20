#!/usr/bin/python3
""" Manipulate lists of integers
"""


class MyList(list):
    """ Manage a list of integers
    """
    def print_sorted(self):
        """ Print a list sorted in ascending order
        """
        print(sorted(self))
                                
