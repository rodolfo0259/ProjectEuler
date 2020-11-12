#2520 is the smallest number that can be divided by 1 to 10, what number can be divided by 1 to 20 ?
#approach -> check if a number is divisible not by dividing, but by checking the number division rules
#narrowing
#d is the last digit of the number n
#the number need to end in 0 -> 2,5,10,15,20 <> d=0
#the d-1=even -> 4
#to the 3 the only even number is 30, so it need to be increase to 60, so the 6 and 3, walk together (to be divisible by 6, it need to be by 3 and 2)
#the 9 the only d=0 is the 90 but the d-1 is not even, so need to be increase to 180 (9*2x=18x)
#divisible by 8, the last 3 digits need to be divible by 8
#if a number is divisible by 9, it is by 3, both you need to sum the digits, and check if the final number is divisible by 9
#if divible by:
#18 is by 9 > 3
#16 is by 8 > 4
#15 > 6
#14 > 7
#12 > 6
#d=0 > 2,5
#1,2,3,4,5,6,7,8,9,10,11-20
##check if:
##d=0; d-1=even; n%19; n%18; n%17; n%16; n%15; n%14; n%13; n%12; n%11;


def divisible(number):
    for i in range(11,21):
        if number % i != 0:
            return False
    return True

number=2520
while True:
    if divisible(number):
        break
    number+=20

print(number)
