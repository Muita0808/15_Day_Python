#!/usr/bin/python3
import sys
def checknum(num):
    if not num:
        return
    if num % 2:
        print ("{} is odd".format(num))
    else:
        print("{} is even".format(num))
