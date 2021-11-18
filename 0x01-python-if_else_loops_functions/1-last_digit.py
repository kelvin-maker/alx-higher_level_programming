#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print("Last digit of {} is {}".format(number, last))

if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and less than 6 and not 0")
