#!/usr/bin/python3
"""Is kind of class module"""


def is_kind_of_class(obj, a_class):
    """Returns True  if the object is an instance of, or if the object is an instance of a class
     that inherited from, the specified class
    Args:
        obj (object): the given object
        a_class (class): the given inspected class
    Returns:
        True if the obj is an instance of the class or inherited
        False otherwise
    """
    return isinstance(obj, a_class)
