#!/bin/python
#Let d(n) be defined as the sum of proper divisors of n 
#amicable numbers
#d(a) = b  and  d(b) = a ; but a!=b
lst = []
total = 10000
n = 2 #if start in 1 d(1) = 1, a!=b (and will loop)
def amicable(n,sun):
    if n == d(sun) and n != sun:
        lst.append(n)


def d(n):
    sun = 0
    for i in range(1,n):
        if n % i == 0:
            sun+=i
    return sun


while n <= total:
    amicable(n,d(n))
    n += 1

print(sum(lst))

