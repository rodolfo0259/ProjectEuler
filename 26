#!/bin/python

limit = 1000
max_div = 0
d = 2
while d < limit:
    unit = 1
    lst = []
    while True:
        x = unit % d
        if x in lst:
            first = lst.index(x)
            last = len(lst)
            if last-first > max_div:
                max_div = last-first
                div = d
            break

        unit = x*10
        lst.append(x)
        
    d+=1

print('max digits and div ',max_div, div)
