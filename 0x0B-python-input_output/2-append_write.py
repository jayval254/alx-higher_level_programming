#!/usr/bin/python3
"""AppendWrite module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file 
    Args:
        filename (str): the given filename
        text (str): the given str
    Returns:
        (int): the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
