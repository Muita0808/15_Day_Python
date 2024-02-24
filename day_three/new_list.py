#!/usr/bin/env python3

def newlist(numbers):
    new = []
    if not numbers:
        return new
    for num in numbers:
        if type(num) is int:
            if num % 2 == 0:
                new.append(num)
    return new
