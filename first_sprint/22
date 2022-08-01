#!/bin/python
#A=65, Z=90
with open('22_names.txt') as f:
    lst = sorted((f.read()).split(','))

total = 0
position = 1
for i in lst:
    sun = 0
    for l in i:
        if l == '"':
            pass
        else:
            sun += ord(l) - 64
    total += position*sun
    position += 1

print(total)
