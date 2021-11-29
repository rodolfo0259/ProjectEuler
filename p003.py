'''
Find all primes factor of a number, e.g. 600851475143
and take the largest
'''
from euler_utils import is_prime

# number = 13195 # 600851475143
number = 600851475143

for prime in range(3, int(number**0.5+1),2):
    if number % prime == 0:
        if is_prime(prime):
            print(prime)