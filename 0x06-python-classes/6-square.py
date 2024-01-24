#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    this is a Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, position):
        """setter"""
        if isinstance(position, tuple) is False or len(position) != 2 or (
                isinstance(position[0], int) and isinstance(position[1], int) is False
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """calculate area"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for y in range(0, self.__position[1]):
                print("")
            for a in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for b in range(0, self.__size):
                    print("#", end="")
                print("")
