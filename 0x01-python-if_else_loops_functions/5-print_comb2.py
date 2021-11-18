#!/usr/bin/python3
print(*(map("{:02d}".format, range(100))), sep=", ")
