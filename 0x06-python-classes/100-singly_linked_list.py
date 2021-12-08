#!/usr/bin/python3
""" Module providing a 'Node' class for a singly-linked list
"""


class Node():
    """ Definition of a singly-linked list node
    """
        def __init__(self, data, next_node=None):
        """ Instantiate a node
        """
        self.data, self.next_node = data, next_node

    @property
        def data(self):
        """ Get the data stored in a node
        """
        return self.__data

    @data.setter
    def data(self, data):
        """ Set the data stored in a node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """ Get the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """ Set the next node
        """
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList():
    """ Definition of a singly-linked list
    """
    def __init__(self):
        """ Instantiate a singly-linked list
        """
        self.__head = None

    def __str__(self):
        """ Generate a visual representation of a list
        """

    def sorted_insert(self, value):
        """ Inset a Node into a list sorted in ascending order
        """
