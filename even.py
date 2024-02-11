#!/usr/bin/python3
#checking if number is even or odd
def check_even_odd(number):
    if not isinstance(number, int):
        print("Error")
        return
    if number % 2 == 0:
        return ("even")
    else:
        return ("odd")
