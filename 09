#there is a pythagorean triplet that a+b+c = 1000
#what is the product of this abc ?
#obs pythagorean triplet is a**2 + b**2 = c**2
#i.e. 3**2 + 4**2 = 5**2
# a<b<c

def triplet(limit):
    for a in range(3, limit):
        for b in range(4, limit):
            c = a**2 + b**2
            c = c**(1/2)
    
            if (a+b+c) == limit:
                answer = a*b*c
                return answer


print(triplet(1000))
