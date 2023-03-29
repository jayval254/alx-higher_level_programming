#!/usr/bin/python3
"""This module sets the positions of square instances"""

class Square:
    """
    Square Class that holds size
    Attributes:
        __size (integer): the size of the square instance
    """
    def __init__(self, new_size=0, new_position=(0, 0)):
        """
        Initializes a square class instance
        Args:
            new_size: the size for the new square instance
        """
        self.size = new_size
        self.position = new_position

    def area(self):
        """Returns the area of the base square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square instance's size in #s"""
        if self.__size is 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.position[0]):
                print(" ", end='')
            for i in range(self.__size):
                print("#", end='')
            print()

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

    @property
    def position(self):
        """property that returns private instance attribute position"""
        return self.__position

    @position.setter
    def position(self, new_position=(0, 0)):
        """
        Sets the position of a square if it's of valid type and value
        Args:
            new_position: the position for the new square instance
        """
        if isinstance(new_position, tuple) is True:
            if len(new_position) is 2:
                if isinstance(new_position[0], int) is True \
                        and new_position[0] >= 0:
                    if isinstance(new_position[1], int) is True \
                            and new_position[1] >= 0:
                        self.__position = new_position
                        return
        raise TypeError("position must be a tuple of 2 positive integers")
