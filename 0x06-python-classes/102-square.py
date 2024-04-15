#!/usr/bin/python3
''' This is Squaer module'''


class Square:
    def __init__(self, size=0):
        '''initializing an instance of class square'''
        self.size = size

    @property
    def size(self):
        '''retrieving the value of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setting the value of size'''

        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''calculate the area of the square'''
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
