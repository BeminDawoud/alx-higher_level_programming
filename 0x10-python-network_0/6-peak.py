#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    '''
    function that finds a peak of a list
    '''

    if list_of_integers and isinstance(list_of_integers, list):
        return max(list_of_integers)
    return None
