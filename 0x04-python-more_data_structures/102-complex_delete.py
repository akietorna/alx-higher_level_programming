#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    num = []
    for a, b in a_dictionary.items():
        if b == value:
            num.append(a)
    if len(num) > 0:
        for i in num:
            a_dictionary.pop(i)
    return a_dictionary
