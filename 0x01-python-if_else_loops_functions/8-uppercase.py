#!/usr/bin/python3

def uppercase(str):

""" Prints a string in uppercase (followed by a newline) """
print("{}".format(str.translate({(c | 32): c for c in range(ord('A'), ord('Z') + 1)})))
