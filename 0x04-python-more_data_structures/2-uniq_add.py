#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    for b in set(my_list):
        a += b
    return a
