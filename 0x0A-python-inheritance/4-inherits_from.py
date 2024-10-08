#!/usr/bin/python3

"""
This module has a function that assess if an object is an
instance of a class that inherits (directly or indirectly) from the specified
class.

Attributes:
    None

Functions:
    inherits_from - Checks if an object is an instance of a class that inherits
    from the specified class.
"""


def inherits_from(obj, a_class):
    """This function checks if an object
    is an instance of a class that inherits
    from the specified class.

    Args:
        obj (object): Object to be examined
        a_class (class): Class to compare with object

    Returns:
        boolean: True if object is an instance
        of a class that inherits from the
        specified class; else False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
