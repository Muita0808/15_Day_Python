#!/usr/bin/python3
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum (c in vowels for c in text)
