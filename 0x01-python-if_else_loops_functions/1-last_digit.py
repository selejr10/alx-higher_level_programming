#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lDig = abs(number) % 10
if number < 0:
    lDig = -lDig
    print(f'Last digit of {number:d} is {lDig} and is less than 6 and not 0')
if lDig > 5:
    print(f'Last digit of {number:d} is {lDig} and is greater than 5')
elif lDig == 0:
    print(f'Last digit of {number:d} is {lDig} and is 0')
