#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    this is a Square class
    """
    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        """calculate area"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print('')
