#!/usr/bin/python3
'''This is Square module'''


class Square:
    '''This represents a  square'''

    def __init__(self, size=0):
        '''initialiazing an instance of the square class
        with a default value for size'''
        if not isinstance(size, int):
            '''checking if the value passed for size is an integer'''
            raise TypeError("size must be an integer")
        elif size < 0:
            '''checking if value passed for size is a positive number'''
            raise ValueError("size must be >= 0")
        self.__size = size
