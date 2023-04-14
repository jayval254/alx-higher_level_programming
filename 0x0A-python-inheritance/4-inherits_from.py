#!/usr/bin/python3
"""Is inherit from module"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly)from the specified class ; otherwise False
    Args:
        obj (object): the given object
        a_class (class): the given class
    Return:
        (True) if a subclass
        (False) otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
