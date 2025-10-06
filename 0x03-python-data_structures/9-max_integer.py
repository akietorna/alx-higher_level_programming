#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None
    big = my_list[0]
    for a in my_list:
        if a > big:
            big = a
    return big
