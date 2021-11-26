#find the value of the first triangle number to have over 500 divisors
# 7th triangle number is sum of 1-7= 28
# factor it, and it yield 6 divisors(1,2,4,7,14,28)
#there are no need to keep dividing after past the half of the total sum, bc there will only be the number 1 left, e.g. 10/5 =2, all divisors after the half_of_the_sum(5) will be between 1 and 2
#if taken the sqrt of the sum, there will be 1 number before and another after the sqrt_number e.g. sqrt(16)=4 (1,2),4,(8,16) the same for every other number
#only trick is if it is a perfect square like 16
#sqrt(10)=2*sqrt(2) ~= 3 -- 1,2,5,10 (2 before, 2 after)
import math

target = 500 #the qtt of factors i want

def factors(number, sumup):
    factor_count = 0
    global target
    sqrt = math.floor(sumup**(1/2)) 
    if sqrt**2 == sumup:
        factor_count-=1
    for x in range(1,sqrt):
        if sumup % x == 0:
            factor_count+=2
    if factor_count > target:
        return True
    else:
        return False


def sumup():
    number = 1
    sumup = 0
    while True:
        sumup += number
        if factors(number,sumup):
            return number, sumup
        else:
            number+=1


print(sumup())
#76576500
