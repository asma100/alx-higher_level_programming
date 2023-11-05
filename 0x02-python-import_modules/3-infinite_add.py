#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    aargs = sys.argv[1:]
    num_args = len(aargs)

    sum = 0
    for i, aarg in enumerate(aargs, start=1):
        n = int(aargs[i-1])
        sum = sum + n
    print(sum)
