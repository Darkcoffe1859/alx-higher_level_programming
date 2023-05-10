#!/usr/bin/python3

def uppercase(input_string):
    for c in input_string:
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()
