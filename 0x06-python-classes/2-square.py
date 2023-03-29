#!/usr/bin/python3
"""This module creates a square instance with a
size and validates it is an int >= 0"""


class Square:
    """
    Square Class that holds size
    Attributes:
        __size (integer): the size of the square instance
    """
    def __init__(self, new_size=0):
        """
        Initializes a square of size new_size
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

