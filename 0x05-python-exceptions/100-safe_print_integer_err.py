#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        raise_exception_msg("Exception: Unknown format code 'd' for object of type '{}'".format(type(value)))
        return False
