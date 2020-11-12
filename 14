# n = n/2   > n == even
# n = 3n + 1 > n == odd
#Which starting number, under one million, produces the longest chain?
#obs: Once the chain starts the terms are allowed to go above one million.
# 9 => 28>14>7>22>11>34>17>52>26>13>40>20>10>5>16>8>4>2>1 == 20

largest_number = 0
largest_chain = 0
total = 1000000
start = 2
while start < total:
    chain = 0
    n = start
    while True:
        chain+=1 #chain includes the number itself and the 1
        if n == 1:
            break 
        elif n % 2 == 0:
            n = n//2
        else:
            n = (3*n)+1

    print('start, chain: ', start,chain)
    if chain > largest_chain:
        largest_chain, largest_number = chain, start
    
    start+=1


print(largest_number, largest_chain)

