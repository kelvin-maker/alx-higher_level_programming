#!/usr/bin/python3
"""Provides a function to get a JSON representation of an object"""

import json


def to_json_string(my_obj):
    """Get a JSON representation of an object"""
    return json.dumps(my_obj)
