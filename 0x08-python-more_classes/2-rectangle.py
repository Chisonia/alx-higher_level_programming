#!/usr/bin/python3
'''This is the rectangle module'''


class Rectangle:
    '''This defines the rectangle'''
    def __init__(self, width=0, height=0):
        '''initializing an instance of class rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''This retrieves the value of width'''
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
        '''This retrieves the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This sets the value of height'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        '''Calculate area of the rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Calculate the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
