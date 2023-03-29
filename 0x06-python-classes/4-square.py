#!/usr/bin/python3
"""This module creates a square instance with a size
and allows it to be changed with getters and setters"""


class Square:
    """
    Square Class that holds size
    Attributes:
        __size (integer): the size of the square instance
    """
    def __init__(self, new_size=0):
        """
        Initializes a square class instance
        Args:
            new_size: the size for the new square instance
        """
        self.size = new_size

    def area(self):
        """Returns the area of the base square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """property that returns private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, new_size=0):
        """
        Sets the size of a square to new_size if it's of valid type and value
        Args:
            new_size: the size for the new square instance
        """
        if isinstance(new_size, int) is True:
            if new_size >= 0:
                self.__size = new_size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
