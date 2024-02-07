#!/usr/bin/python3
"""read file """


def append_write(filename="", text=""):
    """append file"""
    with open(filename, "a", encoding='utf-8') as f:
        f.write(text)
        return len(text)
