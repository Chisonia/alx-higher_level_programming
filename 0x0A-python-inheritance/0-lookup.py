#!/usr/bin/python3

"""
This module checks attributes
and methods of an object and returns them
"""


def lookup(obj):
    """
    This function inherits an object and returns the
    attribute and method of the object

    Parameters:
    obj:  object to be checked and returns its attributes and methods.

    Returns:
    Attributes and Methods of obj

    """
    return dir(obj)
