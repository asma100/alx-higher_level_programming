#!/usr/bin/python3
"""read file """


def write_file(filename="", text=""):
    """read file"""
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
    with open(filename, "r", encoding='utf-8') as rf:
        a = rf.read()
        return rf.tell()
