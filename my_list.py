#!/usr/bin/python3
def find_max_min(numbers):
    if not numbers:
        return null, null
    max_value = min_value = numbers[0]
    for number in numbers:
        max_value = max(max_value, number)
        min_value = min(min_value, number)
        return(max_value, min_value)
