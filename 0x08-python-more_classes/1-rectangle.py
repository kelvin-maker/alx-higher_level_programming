#!/usr/bin/python3
""" Provides a class 'Rectangle' to represent a rectangle
"""


class Rectangle():
        """ Definition of a class to represent a rectangle
    """
            def __init__(self, width=0, height=0):
                        """ Instantiate a rectangle
        """
                                self.height = height
                                        self.width = width

                                            @property
                                                def width(self):
                                                            """ Get the width of a rectangle
        """
                                                                    return self.__width

                                                                    @width.setter
                                                                        def width(self, value):
                                                                                    """ Set the width of a rectangle
        """
                                                                                            if not isinstance(value, int):
                                                                                                            raise TypeError("width must be an integer")
                                                                                                                if value < 0:
                                                                                                                                raise ValueError("width must be >= 0")
                                                                                                                                    self.__width = value

                                                                                                                                        @property
                                                                                                                                            def height(self):
                                                                                                                                                        """ Get the height of a rectangle
        """
                                                                                                                                                                return self.__height

                                                                                                                                                                @height.setter
                                                                                                                                                                    def height(self, value):
                                                                                                                                                                                """ Set the height of a rectangle
        """
                                                                                                                                                                                        if not isinstance(value, int):
                                                                                                                                                                                                        raise TypeError("height must be an integer")
                                                                                                                                                                                                            if value < 0:
                                                                                                                                                                                                                            raise ValueError("height must be >= 0")
                                                                                                                                                                                                                                self.__height = value
