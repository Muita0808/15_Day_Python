#!/usr/bin/python3
def minutes_hours_minutes(minutes):
    minutes = minutes // 60
    hours= minutes % 60
    return hours, minutes
