#!/usr/bin/python3
import math
def list_sum_avg(numbers):
    if not numbers:
        return 0, 0
    total_sum = sum (numbers)
    average = total_sum / len(numbers)
    return total_sum, average
