#!/bin/python

#a) sum of the squares 1^2 + 2^2 + 3^2 ...
#b) the square of the sums (1 + 2 + 3 ...)^2
#do them both and find the difference (b-a)
#from 1 to 100

def sum_squares(n):
    result=0
    for i in range(1,n+1):
        result+=i**2
    return result

def square_of_sum(n):
    total=(n*(n+1))/2
    return total**2

n=100
print(square_of_sum(n) - sum_squares(n))
