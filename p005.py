'''
Smallest number that is divisible by 1 to 20
'''
from euler_utils import find_smallest_number_divisible, is_divisible

number_sequence = 20
result = find_smallest_number_divisible(number_sequence)
print(result)

print(is_divisible(result)[:number_sequence])
