#!/usr/bin/python3
def find_max_min(numbers=[]):
    if not numbers:
        return null, null
    max_number = numbers[0]
    min_number = numbers[0]
#    max_value = min_value = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            mun_number = number
    return(max_number, min_number)
