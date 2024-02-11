#!/usr/bin/python3
def convert_days(num_days):
    years = num_days // 365

    remaining_days = num_days % 365

    weeks = remaining_days // 7

    days = remaining_days % 7

    return years, weeks, days
