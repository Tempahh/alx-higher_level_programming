#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
        if not isinstance(position, tuple) and len(position) != 2 or not all(isinstance(num, int) and num > 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size * self.__size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
        
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
                print(" " * self.__position[0] + "#" *self.__size)
