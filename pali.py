#!/usr/bin/python3
def ispali(string):
    i = 0
    j = len(string) - 1
    while (i < j - 1):
        if (string[i] != string[j]):
            print("{} is not a palindrom".format(string))
            return
        i = i + 1
        j = j - 1
    if (i <= j or i == j - 1):
        print("{} is palindrome".format(string))
