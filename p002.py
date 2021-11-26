'''
Fibonnaci sequence
Find sum of all multiples of two that do not exceed 4 million
'''

from euler_utils import generate_fibonnaci


fibonnaci_sequence = generate_fibonnaci(limit=4*10**6)

sum_multiple_two = 0
for number in fibonnaci_sequence:
    if number%2 == 0:
        sum_multiple_two += number

print(fibonnaci_sequence)
print(sum_multiple_two)