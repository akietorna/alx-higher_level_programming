#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        big = my_list[0]
        for a in my_list:
            if a > big:
                big = a
        return big
    return None
