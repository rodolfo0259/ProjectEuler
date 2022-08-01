#!/usr/bin/env python3

sum_square = sum([x**2 for x in list(range(1, 101))])
square_sum = sum(list(range(1, 101)))**2
print(sum_square, square_sum, square_sum - sum_square)
