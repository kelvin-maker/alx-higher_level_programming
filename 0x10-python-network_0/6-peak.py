#!/usr/bin/python3
"""
Provides a function to find a peak element in an unsorted list of integers
"""

def find_peak(integers):
    """
    Finds a peak element in an unsorted list of integers
    """
    if integers:
        if len(integers) == 1:
            return integers[0]
        if len(integers) == 2:
            if integers[0] > integers[1]:
                return integers[0]
            else:
                return integers[1]
        
             
        mid = len(integers) // 2
        
        if integers[mid] < integers[mid - 1]:
            return find_peak(integers[:mid])
        if integers[mid] < integers[mid + 1]:
            return find_peak(integers[mid + 1:])
        return integers[mid]
    
