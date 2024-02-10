#!/usr/bin/python3
"""
Module takes a sentence and counts words
"""
def count_char(sentence):
    """
    function takes a sentence and returns no of characters
    """
    if isinstance(sentence, str):
        return len(sentence)
    else:
        pass
