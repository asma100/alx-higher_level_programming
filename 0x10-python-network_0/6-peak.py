#!/usr/bin/python3

"""Docstring"""


def find_peak(list_of_integers):
    """
    peak

    """

    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for num in list_of_integers[1:]:
        if num > peak:
            peak = num
    return peak
