#!/usr/bin/python3
'''This is Square module'''


class Square:
    '''defines a square'''
    def __init__(self, size=0):
        '''initializes an instance of a square
        with a default value for size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        '''instance variable'''

    def area(self):
        '''public function to find the area of the square'''
        return (self.__size ** 2)
