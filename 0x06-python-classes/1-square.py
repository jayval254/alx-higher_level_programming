#!/usr/bin/python3
"""This module creates a square instance with a size"""

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
        if new_size is not 0:
            self.__size = new_size

