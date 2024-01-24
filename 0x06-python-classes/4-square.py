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

    def size(self):
        """getter"""
        return self.__size

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
