#!/usr/bin/env python3

## amicable numbers

from euler_utils import is_divisible


def amicable(number: int):
    soma_divs_one = sum(is_divisible(number)[:-1])
    soma_divs_two = sum(is_divisible(soma_divs_one)[:-1])
    if number == soma_divs_two and (soma_divs_one != number):
        return [number, soma_divs_one]
    return False



amicable_list = [False for i in range(10000)]
for index, bool_value in enumerate(amicable_list):
    if bool_value:
        continue
    amicable_pair = amicable(index)
    if amicable_pair:
        print(amicable_pair)
        for amicable_number in amicable_pair:
            amicable_list[amicable_number] = True

amicable_numbers = [i for i, val in enumerate(amicable_list) if val]
print(sum(amicable_list))  # quantity amicables
print(sum(amicable_numbers))  # sum amicable values
