#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    aargs = sys.argv[1:]
    num_args = len(aargs)

    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    for i, aarg in enumerate(aargs, start=1):
        print(f"{i}: {aarg}")
