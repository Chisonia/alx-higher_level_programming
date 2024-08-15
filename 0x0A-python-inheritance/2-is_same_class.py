#!/usr/bin/python3

"""
This module assess if an object
is an instance of a specified
class and return boolean

"""


def is_same_class(obj, a_class):
    """
    This function assess if the obj is an instance
    of a specified class

    Parameters:
    obj: The object
    a_class : This is the class

    Returns:
    True: if obj is an instance of a class
    False: if obj is not an instance of a class

    """
    return isinstance(obj, a_class)
