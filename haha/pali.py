#!/usr/bin/python3
def pali(string):
    i = 0
    j = len(string) - 1
    while (i < j):
        if (string[i] != string[j]):
            print("{} is not a palindrom".format(string))
        i = i + 1
        j = j - 1
    if (i <= j):
        print("{} is palindrome".format(string))
