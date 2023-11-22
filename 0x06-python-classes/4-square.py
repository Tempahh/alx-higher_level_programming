#!/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        return self.__size * self.__size
    @property
    def size(self):
        return self.__size
    @setattr
    def size(self, value):
        self.__size = value