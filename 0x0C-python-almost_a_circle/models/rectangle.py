#!/usr/bin/python3
"""Provides a class to represent a rectangle
"""

from models.base import Base

class Rectangle(Base):
    """Representation of a rectangle
    """
    HEADERS = ('id', 'width', 'height', 'x', 'y')


    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
