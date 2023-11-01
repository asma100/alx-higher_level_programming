#!/usr/bin/python3
import random

n = random.randint(-10, 10)

if n > 0:
    print(f"{n:d} is positive")
elif n == 0:
    print(f"{n:d} is zero")
else:
    print(f"{n:d} is negative")
