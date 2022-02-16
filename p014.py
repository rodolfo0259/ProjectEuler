#!/usr/bin/env python3

from euler_utils import collatz_conjecture

n = 13

max_num_lis = 0
max_num = 0
while n < 10**6:
    result = len(collatz_conjecture(n))
    if max_num_lis < result:
        max_num_lis = result
        max_num = n

    n += 1

print(max_num, max_num_lis)
