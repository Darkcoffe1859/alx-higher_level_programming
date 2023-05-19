#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    for y in new_dict.keys():
        new_dict[y] *= 2
    return (new_dict)
