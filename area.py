#!/usr/bin/python3
"""
Module calculates the area of a rectangle given width and length
"""
#This is a comment
def area(length, width):
    """
    Function calculates area of a rectangle
    Args:
        length: length
        width: width
    """

    if not isinstance(length, int):
        print("{length} Is not an integer")
        return
    if type(width) is not int:
        print("{width} Is not an integer")
        return

    if length == 0 or width == 0:
        return 0
    if length < 0 or width < 0:
        print("Error: No area for negative Length or Width")
        return
    return length * width

