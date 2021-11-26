#!/bin/python
#fibonacci 1000 term

def check(f):
    if len(str(f)) >= 1000:
        return True
    else:
        return False

lst = [1,1]
c=1
while 1:
    f = lst[c]+lst[c-1]
    if check(f):
        print(c+2)
        break
    lst.append(f)
    c+=1


