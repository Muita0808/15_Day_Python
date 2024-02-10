#!/usr/bin/python3

"""
program checks if a number is even or odd
"""

def _checknum(num):
    """
    function determines if a number is odd ofr even
    """
    if not num:
        return
    if num % 2:
        print ("{} is odd".format(num))
    else:
        print("{} is even".format(num))
