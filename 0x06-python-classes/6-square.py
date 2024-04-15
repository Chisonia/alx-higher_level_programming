#!/usr/bin/python3
'''This is square module'''


class Square:

    def __init__(self, size=0, position=(0, 0)):
        '''Initializing an instance of class square'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''retrieving the size value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setting the value of size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''retrieving the position value'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setting the position'''
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''calculating the area of square'''
        return self.__size ** 2

    def my_print(self):
        '''print the square with charace #'''
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

# Example usage:
if __name__ == "__main__":
    my_square = Square(3, (1, 1))
    my_square.my_print()
