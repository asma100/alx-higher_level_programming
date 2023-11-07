#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        f = None
    else:
        le = len(sentence)
        f = sentence[0]

    return le, f
