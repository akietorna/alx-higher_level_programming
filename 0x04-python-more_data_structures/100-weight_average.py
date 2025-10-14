#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    avg = 0
    if my_list == None or my_list == []:
        return 0
    for a in my_list:
        score += a[0] * a[1]
        avg += a[1]
    return score / avg
