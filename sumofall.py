#!/usr/bin/python3
def sum_pos(list=[]):
    if not list:
        return null
    sums = 0
    for nums in list:
        if nums > 0:
            sums = nums + sums
    return sums
