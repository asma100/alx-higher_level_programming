#!/usr/bin/python3
def no_c(my_string):
    r = ""
    for c in my_string:
        if c != 'C' and c != 'c':
            r += c
    return r
