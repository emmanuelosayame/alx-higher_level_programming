#!/usr/bin/python3
import random
num = random.randint(-10, 10)
if num > 0:
    print(f"{num:d} is positive")
elif num == 0:
    print(f"{num:d} is zero")
else:
    print(f"{num:d} is negative")
