#!/usr/bin/python3
import random

n = random.randint(-100, 100)

if n > 0:
  print(f"{n} is positive")
elif n == 0:
  print(f"{n} is zero")
else:
  print(f"{n} is negative")
