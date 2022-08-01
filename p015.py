#!/usr/bin/env python3
### Lattice path

# in a 2x2 grid, you have 6 combinations,
# starting from top left, to arrive on botton right
# you need 2 left and 2 down movements in whichever order,
# therefore you have 4!/(2!*2!) = 6  -- permutations and combinations
# in a grid of 20x20 there will be 20 right and 20 down
# 40 movements in total
# (40!/(20!*20!)

from math import factorial

print(factorial(40)/(factorial(20)*factorial(20)))
