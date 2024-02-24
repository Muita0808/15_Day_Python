#!/usr/bin/env python3
def is_prime(number):
    if number <= 1:
        print("Number is 1 or less than 1")
        return

    num = 2

    while num < number:
        if number % num == 0:
            print("Number is not prime")
            return
        num = num + 1
    print("Number is prime")
    return

