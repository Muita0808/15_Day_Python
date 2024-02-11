#!/usr/bin/python3
import sys

def greeting(name='', age=0):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        if type(name) is not str or type(age) is not int:
            print("Error, name must be str and age must be int")
            return

        print(f"hey, {name}, you are {age} years old.")
