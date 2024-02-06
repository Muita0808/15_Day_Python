#!/usr/bin/python3
import sys
sys.path.append('..')
"""
program checks if a number is even or odd
"""

def checknum(num):
    """
    function determines if a number is odd ofr even
    """
    if not num:
        return
    if num % 2:
        print ("{} is odd".format(num))
    else:
        print("{} is even".format(num))
#if __name__ == "__main__":
 #   checknum(int(sys.argv[1])) 
