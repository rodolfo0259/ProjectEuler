'''
Palindrome number of 3 digits
'''

a = b = 999
max_value = 0

for n in range(1,100):
    for i in range(1,100):
        number = a * b
        if str(number) == str(number)[::-1]:
            # print(f'{number} = {a} * {b}')
            if max_value < number:
                max_value = number
            break
        else:
            b -= 1
    
    a -= 1
    b = 999


print(max_value)