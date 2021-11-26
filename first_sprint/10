import time

limit = 2000000
prime_array = [True] * limit

def prime_sieve(prime_array):
    for i in range(2, len(prime_array)):
        if prime_array[i]:
            k = i*2
            while k < len(prime_array):
                prime_array[k] = False
                k+=i

start_time = time.time()
prime_sieve(prime_array)
sun = 0
for i in range(2, limit):
    if prime_array[i]:
        sun += i

print(sun)
print('time: ', time.time() - start_time, ' s')
