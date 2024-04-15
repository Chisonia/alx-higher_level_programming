#!/usr/bin/python3
'''This is Square module'''


class Square:
    '''defines a square'''
    def __init__(self, size=0):
        '''initializes an instance of a square
        with a default value for size'''

        self.size = size
        '''initial value for instance variable'''

    @property
    def size(self):
        '''getter method to retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter method to set the size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''public function to find the area of the square'''
        return (self.__size ** 2)
