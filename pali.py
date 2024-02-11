#!/usr/bin/python3
<<<<<<< HEAD
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
=======
#program checks if string or text is palindrome 
#palindrome = if a string or text reads the same as the reverse of itself.
def is_palindrome(text):
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    #above converts characters given in tet in lower case, removes any numeric and punctuation and finally joins the changed text into a cleaned text

    return cleaned_text = cleaned_text[::-1]

#above returns a cleaned_text if the reversal of the text (::-1]) is same as the original text.
>>>>>>> 046b2cd6023fa0eae0e2f43349d4acececc08907
