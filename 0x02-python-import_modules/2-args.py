#!/usr/bin/python3
import sys

aargs = sys.argv[1:]
num_args = len(aargs)

print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
for i, aarg in enumerate(aargs, start=1):
    print(f"{i}: {aarg}")
