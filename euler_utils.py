'''
Utils function to use for math and Project Euler in general
'''

def get_gauss_sum(target_number_n: int, multiple_factor: int)->int:
    '''
    Base formula:
    (n*(n+1))/2

    Gauss concept:
    1+2+3
    3+2+1
    -----
    6+6+6 = 18 / 2 = 9

    e.g. for multiples
    sum of all multiples of 3 from 1 to 30 (below 31)

    We want all multiples of 3, therefore we can make 30/3, 
    to get the multiplication table of 3
    if the target number n was 32, we would round it to the lowest value, 10

    Args:
        target_number_n: the size of the the set n
        multiple_factor: the number which will sum all of its multiples
    Returns:
        gauss_sum: the sum of all the multiples from 1 to target_number
    '''
    factor = int(target_number_n / multiple_factor)
    gauss_sum = multiple_factor * (factor * (factor+1))/2
    return gauss_sum


def generate_fibonnaci(limit: int)->list:
    '''
    Generates the fibonnaci sequence that does not exceed limit
    '''
    fibonnaci_sequence = [1, 1]
    while fibonnaci_sequence[-1] < limit:
        fibonnaci_sequence.append(
            fibonnaci_sequence[-1] + fibonnaci_sequence[-2]
        )
    
    ## removes the last number which is bigger than limit
    return fibonnaci_sequence[:-1]


def find_primes_sieve(limit: int)->list:
    '''
    Find the primes based on sieve of eratosthenes
    '''
    prime_list = list()

    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            prime_list.append(i)
            for n in range(i*i, limit, i):  # Mark factors non-prime
                a[n] = False
    
    return prime_list


def is_prime(number: int)->bool:
    '''
    Find if a number is prime
    '''
    for i in range(2, int(number**0.5+1)):
        if number % i == 0:
            return False
    
    return True