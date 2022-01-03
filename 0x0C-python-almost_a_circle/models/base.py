#!/usr/bin/python3
"""Provides a base class for all other classes in this module
"""
import json

class Base():
    """Base class for all other classes in this module
    """
    HEADERS = ('id',)

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a base object
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id
            
        
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON representation a list of dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a JSON representation of list_objs to <class-name>.json
        """
        with open("{}.json".format(cls.__name__), 'w') as ofile:
            if list_objs:
                ofile.write(cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                ))
            else:
                ofile.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Return the list defined by a JSON string
        """
        if json_string is None:
            return []
        return json.loads(json_string)
    

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance of cls with its attributes set
        """
        args = []
        while True:
            try:
                obj = cls(*args)
            except TypeError:
                args.append(1)
            else:
                break
        obj.update(**dictionary)
        return obj
