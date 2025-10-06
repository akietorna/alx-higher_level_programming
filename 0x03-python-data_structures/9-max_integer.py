#!/usr/bin/python3
def max_integer(my_list=[]):
    big = 0
    if my_list is not None:
        for a in my_list:
            if a > big:
                big = a
        return big
    return None
