#!/usr/bin/python3
def is_pangram(text):
    lower_text = text.lower().replace(" " , "")
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(lowercase_text)
