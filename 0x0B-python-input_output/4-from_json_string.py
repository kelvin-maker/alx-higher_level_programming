#!/usr/bin/python3
"""Provides a function to create an object from a JSON string"""

import json


def from_json_string(my_str):
    """Create an object from a JSON string"""
    return json.loads(my_str)
