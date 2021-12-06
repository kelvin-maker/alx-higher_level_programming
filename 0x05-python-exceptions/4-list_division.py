#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Divide each element of a list by the corresponding element of another
    """
    results = list()
    for index in range(list_length):
        try:
            r = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
            r = 0
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        finally:
            results.append(r)
    return results
