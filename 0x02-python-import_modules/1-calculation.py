#!/usr/bin/env python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

sum = add(a, b)
diff = sub(a, b)
product = mul(a, b)
quotient = div(a, b)

print("{0:d} + {1:d} = {2:d}".format(a, b, sum))
print("{0:d} - {1:d} = {2:d}".format(a, b, diff))
print("{0:d} * {1:d} = {2:d}".format(a, b, product))
print("{0:d} / {1:d} = {2:d}".format(a, b, quotient))
