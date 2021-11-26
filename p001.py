'''
Challenge: 
> Find the sum of all the multiples of 3 or 5 below 1000

Base formula:
(n*(n+1))/2

Gauss concept:
1+2+3
3+2+1
-----
6+6+6 = 18 / 2 = 9

Works for even, odds, multiples
e.g. for multiples
sum of all multiples of 3 from 1 to 30 (below 31)
3*1 -> 3
3*2 -> 6
...
3*9 -> 27
3*10 -> 30
We want all multiples of 3, therefore we can make 30/3, 
to get the multiplication table of 3
if the target number n was 32, we would round it to the lowest value, 10

Can be "sum = avg * count" as well
avg = (1 + n)/2
'''
from euler_utils import get_gauss_sum

## all below 1000
target_number_n = 999

x = get_gauss_sum(target_number_n, 3)
y = get_gauss_sum(target_number_n, 5)
z = get_gauss_sum(target_number_n, 15)

## need to remove multiples of 15, since we want 3 OR 5
print(x+y-z)