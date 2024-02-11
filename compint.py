#!/usr/bin/python3
"""
Module Calculatesthe compound interest given principal, rate and time
"""

def compound_int(principal, rate, time):
    '''
    Function calculates compound interest

    Parameters:
    - principal(int): Principal amount
    - rate(int (%)): interest rate
    - time(int): time period running the loan

    Returns:
    - int - compounded amount
    '''
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal) ** time

    return amount
