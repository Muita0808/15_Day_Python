#!/usr/bin/python3
def is_palindrome(text):
     lowercase_text = text.lower().replace(" ", "")  # Handle case and spaces
         return lowercase_text == lowercase_text[::-1]

