#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = "Last digit of "
if number < 0:
    last_digit = -last_digit
print("{}{} is {} and is ".format(message, number, last_digit), end="")
if last_digit > 5:
    print("greater than five")
elif last_digit == 0:
    print("zero")
else:
    print("less than six and not zero")
