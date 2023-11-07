#!/usr/bin/python3
def no_c(my_string):
    r = ""
    for i in my_string:
        if i == 'C' or i == 'c':
            r += ' '
        else:
            r += i
    return r
