#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = -10
while (i != number):
    if number > 0:
        print(" {:d} is positive".format(number))
        i += 1
    elif number == 0:
        print(" {:d} is zero".format(number))
        i += 1
    else:
        print(" {:d} is negative".format(number))
    break
