#!/usr/bin/env python3

from euler_utils import find_tree_bigger_path


# why not requests ;o  ?!
# please avoid to not get unnecessary request to eulers server
# import requests

# test_triangle_euler_67 = requests.get(
#     'https://projecteuler.net/project/resources/p067_triangle.txt'
# ).text
# with open('euler_triangle_67.txt', 'w', encoding='utf-8') as f:
#     f.write(test_triangle_euler_67)

with open('euler_triangle_67.txt', 'r', encoding='utf-8') as f:
    test_triangle_euler_67 = [
        line.replace('\n', '').split(' ') for line in f.readlines()
    ]

print(find_tree_bigger_path(test_triangle_euler_67))
