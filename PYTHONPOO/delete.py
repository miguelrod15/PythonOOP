#number = int(input('Type the factorial you want calculate: '))
#if number > 0 and type(number) == int:
#    factorial = 1
#    for item in range (1, number+1):
#        print(f'{factorial} * {item}')
#        factorial *= item
#        print(f'{factorial}')
#else: 
#    print('PLEASE, inform just positive integer')
#print(f'The factorial of {number} is {factorial}')

from random import randint

value = randint(1, 10)
check = False
while check == False:
    number = int(input('Type your integer: '))
    if number > value:
        print('Type a lower value')
    elif number < value:
        print('Type a higher value')
    elif number == value:
        break

print('ITS OVER! YOU WON')
