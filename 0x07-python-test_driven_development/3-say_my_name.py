#!/usr/bin/python3

"""


This module contains function that represent name (first and last name)


"""
def say_my_name(first_name, last_name=""):
    """ this function prints names

    Args:
        first_name(str): The first name to print
        last_name(str):  The last name to print

    Raise:
        TypeError: if first_name or last_name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
