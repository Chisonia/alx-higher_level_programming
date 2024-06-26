#!/usr/bin/python3
'''This is the rectangle module'''


class Rectangle:
    '''this defines the rectangle'''
    def __init__(self, width=0, height=0):
        '''Initializing an instance og class rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieves the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''This sets the value of width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieves the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This sets the value of height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
