#what is the 10001st prime number ?

def what_prime(n): #n is the position of the prime e.g. 6th = 13
    count = 2
    prime = 5
    while True:
        for i in range(2,prime+1):
            if prime % i == 0:
                if prime != i:
                    break;
                else:
                    count+=1
            
        prime+=1
        if count == n:
            return count, i
    



print(what_prime(6))
print(what_prime(10))
print(what_prime(10001))

#it works, but slow, the number is 104743
