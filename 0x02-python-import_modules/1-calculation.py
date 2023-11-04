#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    i = add(a, b)
    print("{} + {} = {}".format(a, b, i))
    i = sub(a, b)
    print("{} - {} = {}".format(a, b, i))
    i = mul(a, b)
    print("{} * {} = {}".format(a, b, i))
    i = div(a, b)
    print("{} / {} = {}".format(a, b, i))
