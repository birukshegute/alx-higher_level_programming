#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers."""
""" There may be more than one peak in the list"""


def find_peak(list_of_integers):
    """function that finds a peak"""

    start, end = 0, len(list_of_integers) - 1
    while start < end:
        mid = start + (end - start) // 2

        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
        return list_of_integers[start]
