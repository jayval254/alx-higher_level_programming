#!/usr/bin/python3
"""Is same Class module"""


def is_same_class(obj, a_class):
    """Returns True if an object is an instance of the given class
    Args:
        obj (object): the given object
        a_class (class): the given class
    Returns:
        True if the obj is an instance of a_class
        False otherwise
    """
    return type(obj) == 