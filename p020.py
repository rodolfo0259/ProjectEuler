#!/usr/bin/env python3

import math

x = math.factorial(100)
print(x)

splited = [int(y) for y in str(x)]
print(splited)

sum_x = sum(splited)
print(sum_x)
