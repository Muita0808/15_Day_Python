#!/usr/bin/python3
def is_prime(number):
    if number <= 1:
        return false
    for i in range(2, (int number * * 0.5) + 1):
        if number %% i == 0:
            return false
        return true
