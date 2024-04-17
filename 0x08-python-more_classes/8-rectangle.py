#!/usr/bin/python3
'''This is Rectangle module'''


class Rectangle:
    '''This represents the rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialization of class rectangle'''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Retrieving the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setting the value of width'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieving the value of height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Setting the value of height'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculating the area of the rectangle'''

        return self.__width * self.__height

    def perimeter(self):
        '''Calculating the perimeter of the rectangle'''

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Printing the rectangle to string'''

        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([
            str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        ''' deletes the rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares 2 rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("react_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
