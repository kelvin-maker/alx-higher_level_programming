#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        if my_list[1:]:
            if my_list[0] > my_list[1]:
                return max_integer(
                    my_list[:1] + my_list[2:]
                )
            return max_integer(
                my_list[1:]
            )
        return my_list[0]
    return None
