#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers."""
""" There may be more than one peak in the list"""


def find_peak(list_of_integers):
    """function that finds a peak"""

    int_max = None
    for i in list_of_integers:
        if int_max is None or int_max < i:
            int_max = i
    return int_max
