#!/usr/bin/env python3
'''
checks if a year is leap
'''
def leap(year):
    if year % 4 != 0:
            return 1

    if year % 100 == 0:
        if year % 400 == 0:
            return 0
        else:
            return 1
    else:
        return 0
