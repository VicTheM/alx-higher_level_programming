#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    number = -num % 10
    number *= -1
else:
    number = num % 10
print(f"Last digit of {num} is {number}", end=" ")
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
elif number < 6 and number != 0:
    print("and is less than 6 and not 0")
