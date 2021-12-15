#!/usr/bin/python3
"""Provides a function 'text_indentation' that formats text"""


def text_indentation(text):
    """Format text by splitting lines at special characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in '.:?':
        text = text.replace(char, char + '\n\n')
    print(*(ln.strip() for ln in (text + '\n').splitlines()), sep='\n', end='')
                                        
