#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    this is a Square class
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
