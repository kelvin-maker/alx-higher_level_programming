#!/usr/bin/python3
print(*(', '.join("{}{}".format(tens, ones) for ones in range(tens+1, 10)) for tens in range(9)), sep=', ')
