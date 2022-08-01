#!/usr/bin/env python3

from euler_utils import is_divisible

n = 2  # base number to sum
tn = 3  # triagle number

while len(is_divisible(tn)) < 500:
    n += 1
    tn += n

print(n)
print(tn)
