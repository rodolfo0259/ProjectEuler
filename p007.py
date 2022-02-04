#!/usr/bin/env python3

from euler_utils import find_primes_sieve


primes = find_primes_sieve(110000)
print(len(primes))
print(primes[10000])
