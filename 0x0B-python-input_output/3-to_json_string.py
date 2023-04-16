#!/usr/bin/python3
"""ToJsonString module"""
import json


def to_json_string(my_obj):
    """Returns the json represantation of an object
    Args:
        my_obj (object): the given object
    Returns:
        (str): the JSON Representation
    """
    return json.dumps(my_obj)
