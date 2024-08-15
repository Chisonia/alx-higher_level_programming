#!/usr/bin/python3

"""
This module creates a class that inherits list object
"""


class MyList(list):
    """
    This class inherits the list object

    Attributes:
    No attribute

    Method:
    print_sorted which prints a sorted list

    """
    def print_sorted(self):
        print(sorted(self))
